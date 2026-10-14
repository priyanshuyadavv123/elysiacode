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


if __name__ == "__main__":
    unittest.main()
