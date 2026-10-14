"""
Unit tests for Elysia Code Dual-Engine Database Architecture (core/db.py).
Tests:
- Default SQLite operations and row dict access
- Query parameter mapping (? to %s in MySQL adapter)
- Database URL parsing for MySQL
- Engine type detection
- Unified IntegrityError behavior
"""

import os
import unittest
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _env  # noqa: F401

from core import db, auth


class TestDatabaseArchitecture(unittest.TestCase):
    def test_default_engine_is_sqlite(self):
        self.assertEqual(db.get_engine_type(), "sqlite")
        self.assertFalse(db.is_mysql_mode())

    def test_database_url_parsing(self):
        old_url = os.environ.get("DATABASE_URL")
        try:
            os.environ["DATABASE_URL"] = "mysql://elysia_user:secret123@db.internal.net:3307/elysiadb"
            cfg = db.get_mysql_config()
            self.assertEqual(cfg["host"], "db.internal.net")
            self.assertEqual(cfg["port"], 3307)
            self.assertEqual(cfg["user"], "elysia_user")
            self.assertEqual(cfg["password"], "secret123")
            self.assertEqual(cfg["database"], "elysiadb")
            self.assertEqual(db.get_engine_type(), "mysql")
            self.assertTrue(db.is_mysql_mode())
        finally:
            if old_url is not None:
                os.environ["DATABASE_URL"] = old_url
            else:
                os.environ.pop("DATABASE_URL", None)

    def test_sqlite_basic_operations(self):
        with db.connect() as conn:
            conn.execute("INSERT OR REPLACE INTO meta (`key`, `value`) VALUES (?, ?)", ("test_k", "test_v"))
            row = conn.execute("SELECT `value` FROM meta WHERE `key`=?", ("test_k",)).fetchone()
            self.assertIsNotNone(row)
            self.assertEqual(row["value"], "test_v")

    def test_auth_with_unified_db(self):
        # Register a test user
        uname = "testuser_%d" % int(db.now() * 1000)
        res = auth.register_user(name="Test User", identifier=uname, password="Password123!")
        self.assertTrue(res["success"], res.get("error"))

        # Duplicate registration should trigger db.IntegrityError cleanly
        res2 = auth.register_user(name="Test User", identifier=uname, password="Password123!")
        self.assertFalse(res2["success"])
        self.assertIn("already exists", res2.get("error", ""))

    def test_database_indexes(self):
        """Verify that performance indexes exist in the database."""
        with db.connect() as conn:
            user_indexes = [r[1] for r in conn.execute("PRAGMA index_list('users')").fetchall()]
            session_indexes = [r[1] for r in conn.execute("PRAGMA index_list('sessions')").fetchall()]
            self.assertIn("idx_users_username", user_indexes)
            self.assertIn("idx_users_email", user_indexes)
            self.assertIn("idx_users_xp", user_indexes)
            self.assertIn("idx_sessions_user", session_indexes)
            self.assertIn("idx_sessions_expires", session_indexes)

    def test_honeypot_spam_block(self):
        """Verify that bot registrations filling honeypots are rejected."""
        res = auth.register_user(
            name="Bot User", identifier="bot_user_123", password="Password123!",
            hp="http://spam-link.ru"
        )
        self.assertFalse(res["success"])
        self.assertIn("spam", res.get("error", "").lower())

    def test_session_caching_and_invalidation(self):
        """Verify in-memory session cache hit and invalidation on update."""
        uname = "cacheuser_%d" % int(db.now() * 1000)
        auth.register_user(name="Cache Test", identifier=uname, password="Password123!")
        log_res = auth.login_user(identifier=uname, password="Password123!")
        self.assertTrue(log_res["success"])
        token = auth.create_session(log_res["user"]["id"])

        # First read (populates cache)
        u1 = auth.user_for_token(token)
        self.assertIsNotNone(u1)
        self.assertEqual(u1["username"], uname)

        # Second read (cache hit)
        u2 = auth.user_for_token(token)
        self.assertEqual(u1["id"], u2["id"])

        # Update profile invalidates cache
        auth.update_profile(identifier=uname, name="Updated Name")
        u3 = auth.user_for_token(token)
        self.assertEqual(u3["name"], "Updated Name")

    def test_legacy_migration_filters_test_fixtures(self):
        """Verify _migrate_legacy_json imports valid users but filters out test_user_* fixtures."""
        import json
        import tempfile
        import shutil

        temp_dir = tempfile.mkdtemp(prefix="elysia_mig_test_")
        try:
            legacy_file = Path(temp_dir) / "users.json"
            sample_data = {
                "real_student": {
                    "id": "usr_real_001",
                    "username": "real_student",
                    "name": "Real Student",
                    "email": "student@college.edu",
                    "password_hash": "dummy_hash",
                    "xp": 100
                },
                "test_user_3": {
                    "id": "usr_test_003",
                    "username": "test_user_3",
                    "name": "Test User 3",
                    "email": "test_user_3@test.local",
                    "password_hash": "dummy_hash_test",
                    "xp": 450
                },
                "loadtest_123": {
                    "id": "usr_load_001",
                    "username": "loadtest_123",
                    "name": "Load Test",
                    "email": "loadtest@test.local",
                    "password_hash": "dummy_hash_load",
                    "xp": 0
                }
            }
            legacy_file.write_text(json.dumps(sample_data), encoding="utf-8")

            # Run migration in a fresh isolated sqlite connection
            conn = db.sqlite3.connect(":memory:")
            conn.row_factory = db.sqlite3.Row
            conn.executescript(db.SCHEMA_SQLITE)

            old_data_dir = os.environ.get("ELYSIA_DATA_DIR")
            try:
                os.environ["ELYSIA_DATA_DIR"] = temp_dir
                db._migrate_legacy_json(conn)
            finally:
                if old_data_dir is not None:
                    os.environ["ELYSIA_DATA_DIR"] = old_data_dir

            rows = conn.execute("SELECT username, email FROM users").fetchall()
            usernames = [r["username"] for r in rows]

            # Real student must be migrated
            self.assertIn("real_student", usernames)
            # Test fixtures must NOT be migrated
            self.assertNotIn("test_user_3", usernames)
            self.assertNotIn("loadtest_123", usernames)
            self.assertEqual(len(usernames), 1)
        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)

    def test_production_seed_has_no_test_users(self):
        """Verify data/users.json does not contain any test fixtures."""
        prod_json_path = db.BASE_DIR / "data" / "users.json"
        if prod_json_path.exists():
            import json
            data = json.loads(prod_json_path.read_text(encoding="utf-8"))
            for key, user in data.items():
                username = str(user.get("username") or key).lower()
                self.assertFalse(username.startswith("test_user"), f"Test user found in production data: {username}")
                self.assertFalse(username.startswith("loadtest_"), f"Loadtest user found in production data: {username}")


    def test_postgres_engine_detection(self):
        """Verify PostgreSQL detection via DATABASE_URL and DB_TYPE without affecting defaults."""
        old_url = os.environ.get("DATABASE_URL")
        old_type = os.environ.get("DB_TYPE")
        try:
            # 1. postgresql:// url
            os.environ["DATABASE_URL"] = "postgresql://user:pass@ep-cool-db.aws.supabase.com:6543/postgres"
            os.environ.pop("DB_TYPE", None)
            self.assertEqual(db.get_engine_type(), "postgres")
            self.assertTrue(db.is_postgres_mode())
            self.assertFalse(db.is_mysql_mode())

            # 2. postgres:// url
            os.environ["DATABASE_URL"] = "postgres://user:pass@localhost:5432/elysia"
            self.assertEqual(db.get_engine_type(), "postgres")
            self.assertTrue(db.is_postgres_mode())

            # 3. DB_TYPE=postgres
            os.environ.pop("DATABASE_URL", None)
            os.environ["DB_TYPE"] = "postgres"
            self.assertEqual(db.get_engine_type(), "postgres")
            self.assertTrue(db.is_postgres_mode())

            # 4. DB_TYPE=postgresql
            os.environ["DB_TYPE"] = "postgresql"
            self.assertEqual(db.get_engine_type(), "postgres")
            self.assertTrue(db.is_postgres_mode())

            # 5. Default remains sqlite
            os.environ.pop("DB_TYPE", None)
            self.assertEqual(db.get_engine_type(), "sqlite")
            self.assertFalse(db.is_postgres_mode())
            self.assertFalse(db.is_mysql_mode())
        finally:
            if old_url is not None:
                os.environ["DATABASE_URL"] = old_url
            else:
                os.environ.pop("DATABASE_URL", None)
            if old_type is not None:
                os.environ["DB_TYPE"] = old_type
            else:
                os.environ.pop("DB_TYPE", None)

    def test_postgres_url_sanitization_and_config(self):
        """Verify get_postgres_config correctly extracts parameters and masks credentials."""
        old_url = os.environ.get("DATABASE_URL")
        try:
            secret_url = "postgresql://supa_admin:super_secret_password_123@aws-0-ap-south-1.pooler.supabase.com:6543/postgres?sslmode=require"
            os.environ["DATABASE_URL"] = secret_url
            cfg = db.get_postgres_config()
            self.assertEqual(cfg["host"], "aws-0-ap-south-1.pooler.supabase.com")
            self.assertEqual(cfg["port"], 6543)
            self.assertEqual(cfg["user"], "supa_admin")
            self.assertEqual(cfg["password"], "super_secret_password_123")
            self.assertEqual(cfg["database"], "postgres")
            self.assertEqual(cfg["sslmode"], "require")

            # Sanitization must NEVER show password
            sanitized = db.sanitize_db_url(secret_url)
            self.assertNotIn("super_secret_password_123", sanitized)
            self.assertIn("supa_admin:***@", sanitized)
            self.assertIn("aws-0-ap-south-1.pooler.supabase.com", sanitized)
        finally:
            if old_url is not None:
                os.environ["DATABASE_URL"] = old_url
            else:
                os.environ.pop("DATABASE_URL", None)

    def test_postgres_safe_failure_without_driver(self):
        """Verify connecting to PostgreSQL when driver is absent raises clean error without falling back to SQLite."""
        old_url = os.environ.get("DATABASE_URL")
        try:
            os.environ["DATABASE_URL"] = "postgresql://user:secret123@127.0.0.1:5432/elysia"
            # If neither driver is installed, connect must fail explicitly
            if not db.HAS_PSYCOPG2 and not db.HAS_PSYCOPG:
                with self.assertRaises(RuntimeError) as cm:
                    with db.connect():
                        pass
                err_msg = str(cm.exception)
                self.assertIn("PostgreSQL engine is configured", err_msg)
                self.assertNotIn("secret123", err_msg)
        finally:
            if old_url is not None:
                os.environ["DATABASE_URL"] = old_url
            else:
                os.environ.pop("DATABASE_URL", None)

    def test_sql_translation_for_postgres(self):
        """Verify SQL translation preserves string literals while mapping placeholders and keywords."""
        t = db.translate_sql_for_postgres

        # 1. Placeholders outside vs inside strings
        q1 = "SELECT * FROM users WHERE name = 'Why? What?' AND id = ?"
        self.assertEqual(t(q1), "SELECT * FROM users WHERE name = 'Why? What?' AND id = %s")

        # 2. Multiple placeholders
        q2 = "UPDATE users SET xp = ?, streak = ? WHERE id = ?"
        self.assertEqual(t(q2), "UPDATE users SET xp = %s, streak = %s WHERE id = %s")

        # 3. Backtick identifier escaping
        q3 = "SELECT `value` FROM meta WHERE `key` = ?"
        self.assertEqual(t(q3), 'SELECT "value" FROM meta WHERE "key" = %s')

        # 4. INSERT OR IGNORE INTO
        q4 = "INSERT OR IGNORE INTO users (id, username) VALUES (?, ?);"
        self.assertEqual(t(q4), "INSERT INTO users (id, username) VALUES (%s, %s) ON CONFLICT DO NOTHING;")

        # 5. REPLACE INTO meta
        q5 = "REPLACE INTO meta (`key`, `value`) VALUES (?, ?)"
        self.assertEqual(t(q5), 'INSERT INTO meta ("key", "value") VALUES (%s, %s) ON CONFLICT ("key") DO UPDATE SET "value" = EXCLUDED."value"')

        # 6. INSERT OR REPLACE INTO meta
        q6 = "INSERT OR REPLACE INTO meta (`key`, `value`) VALUES (?, ?);"
        self.assertEqual(t(q6), 'INSERT INTO meta ("key", "value") VALUES (%s, %s) ON CONFLICT ("key") DO UPDATE SET "value" = EXCLUDED."value";')

        # 7. PRAGMA no-op
        q7 = "PRAGMA foreign_keys = ON"
        self.assertTrue(t(q7).startswith("-- PRAGMA_NOOP:"))

    def test_postgres_row_wrapper_parity(self):
        """Verify PostgresRow supports dict lookup, positional index, tuple cast, and keys."""
        data_dict = {"id": "usr_abc123", "username": "priyanshu", "xp": 350}
        data_tuple = ("usr_abc123", "priyanshu", 350)
        row = db.PostgresRow(data_dict, data_tuple)

        # Dict access (case-insensitive)
        self.assertEqual(row["id"], "usr_abc123")
        self.assertEqual(row["ID"], "usr_abc123")
        self.assertEqual(row["username"], "priyanshu")
        self.assertEqual(row["xp"], 350)

        # Positional index access
        self.assertEqual(row[0], "usr_abc123")
        self.assertEqual(row[1], "priyanshu")
        self.assertEqual(row[2], 350)

        # Tuple conversion
        self.assertEqual(tuple(row), ("usr_abc123", "priyanshu", 350))

        # Length and keys
        self.assertEqual(len(row), 3)
        self.assertIn("id", row.keys())
        self.assertIn("username", row.keys())

        # Missing key raises KeyError
        with self.assertRaises(KeyError):
            _ = row["nonexistent_column"]

    def test_postgres_simulated_connection_and_transaction(self):
        """Verify PostgresConnectionWrapper transaction, commit, rollback, and cursor handling using simulated mocks."""
        from unittest.mock import MagicMock

        mock_raw_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.description = [("id",), ("username",), ("xp",)]
        mock_cursor.fetchone.return_value = ("usr_sim_1", "sim_coder", 100)
        mock_cursor.fetchall.return_value = [("usr_sim_1", "sim_coder", 100)]
        mock_raw_conn.cursor.return_value = mock_cursor

        wrapper = db.PostgresConnectionWrapper(mock_raw_conn)

        # 1. Execute query and fetchone
        res = wrapper.execute("SELECT `id`, `username`, `xp` FROM users WHERE id = ?", ("usr_sim_1",))
        row = res.fetchone()
        self.assertIsNotNone(row)
        self.assertEqual(row["id"], "usr_sim_1")
        self.assertEqual(row["username"], "sim_coder")
        self.assertEqual(row[0], "usr_sim_1")

        # Verify underlying call translated SQL
        mock_cursor.execute.assert_called_with('SELECT "id", "username", "xp" FROM users WHERE id = %s', ('usr_sim_1',))

        # 2. PRAGMA must be a no-op
        pragma_res = wrapper.execute("PRAGMA foreign_keys=ON")
        self.assertIsNone(pragma_res.fetchone())
        self.assertEqual(pragma_res.fetchall(), [])

        # 3. Commit and rollback
        wrapper.commit()
        mock_raw_conn.commit.assert_called_once()
        wrapper.rollback()
        mock_raw_conn.rollback.assert_called_once()
        wrapper.close()
        mock_cursor.close.assert_called()

    def test_postgres_pool_thread_safety_simulated(self):
        """Verify _PostgresPool handles multi-threaded acquisitions and returns correctly."""
        from unittest.mock import MagicMock
        import threading

        pool = db._PostgresPool(max_size=5)

        # Populate pool with simulated connections
        mock_conns = []
        for i in range(5):
            mc = MagicMock()
            mc.closed = 0
            mock_cur = MagicMock()
            mc.cursor.return_value.__enter__.return_value = mock_cur
            mock_conns.append(mc)
            pool.put(mc)
        pool._created_count = 5

        errors = []

        def worker():
            try:
                c = pool.get()
                import time
                time.sleep(0.005)
                pool.put(c)
            except Exception as e:
                errors.append(e)

        threads = [threading.Thread(target=worker) for _ in range(15)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        self.assertEqual(len(errors), 0)


if __name__ == "__main__":
    unittest.main()
