"""
Elysia School - Pluggable Storage Layer (SQLite + MySQL/MariaDB).

Why Dual-Engine Architecture?
  1. Zero Setup for Development:
     - SQLite runs out-of-the-box with standard library only (zero pip dependencies).
     - Perfect for local development, offline study, university viva, and portable zip distributions.
     - Configured with WAL (Write-Ahead Logging) mode for fast concurrent reading.
  2. Enterprise Concurrency for High Traffic:
     - When your site scales to thousands of concurrent active learners, set DB_TYPE=mysql
       or supply DATABASE_URL.
     - MySQL / MariaDB provides row-level locking (user A updating progress never locks user B),
       dedicated thread-safe connection pooling, and multi-server horizontal scaling.
"""

import json
import logging
import os
import queue
import re
import sqlite3
import threading
import time
from contextlib import contextmanager
from pathlib import Path
from urllib.parse import urlparse, unquote

logger = logging.getLogger("elysia")

BASE_DIR = Path(__file__).resolve().parent.parent

_init_lock = threading.Lock()
_initialised = set()  # paths or host identifiers whose schema already ran in this process

# ----------------------------------------------------------------- Driver detection
try:
    import pymysql
    import pymysql.cursors
    HAS_PYMYSQL = True
except ImportError:
    HAS_PYMYSQL = False

try:
    import mysql.connector
    import mysql.connector.errors
    HAS_MYSQL_CONNECTOR = True
except ImportError:
    HAS_MYSQL_CONNECTOR = False

try:
    import psycopg2
    import psycopg2.extras
    import psycopg2.pool
    import psycopg2.errors
    HAS_PSYCOPG2 = True
except ImportError:
    HAS_PSYCOPG2 = False

try:
    import psycopg
    from psycopg import errors as psycopg_errors
    HAS_PSYCOPG = True
except ImportError:
    HAS_PSYCOPG = False

# Unified IntegrityError tuple so callers can catch constraint violations across engines
_err_list = [sqlite3.IntegrityError]
if HAS_PYMYSQL:
    _err_list.append(pymysql.err.IntegrityError)
if HAS_MYSQL_CONNECTOR:
    _err_list.append(mysql.connector.errors.IntegrityError)
if HAS_PSYCOPG2:
    _err_list.append(psycopg2.IntegrityError)
if HAS_PSYCOPG:
    _err_list.append(psycopg.errors.IntegrityError)
IntegrityError = tuple(_err_list)


# ----------------------------------------------------------------- Schemas
SCHEMA_SQLITE = """
CREATE TABLE IF NOT EXISTS users (
    id                  TEXT PRIMARY KEY,
    username            TEXT NOT NULL UNIQUE,
    name                TEXT NOT NULL,
    email               TEXT NOT NULL DEFAULT '',
    password_hash       TEXT NOT NULL,
    avatar              TEXT NOT NULL DEFAULT '',
    motto               TEXT NOT NULL DEFAULT '',
    xp                  INTEGER NOT NULL DEFAULT 0,
    streak              INTEGER NOT NULL DEFAULT 1,
    completed_subtopics TEXT NOT NULL DEFAULT '[]',
    today_seconds       INTEGER NOT NULL DEFAULT 0,
    total_seconds       INTEGER NOT NULL DEFAULT 0,
    created_at          TEXT NOT NULL DEFAULT ''
);
CREATE TABLE IF NOT EXISTS sessions (
    token_hash TEXT PRIMARY KEY,
    user_id    TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    created_at REAL NOT NULL,
    expires_at REAL NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_users_xp ON users(xp DESC);
CREATE INDEX IF NOT EXISTS idx_sessions_user ON sessions(user_id);
CREATE INDEX IF NOT EXISTS idx_sessions_expires ON sessions(expires_at);
CREATE TABLE IF NOT EXISTS meta (
    `key`   TEXT PRIMARY KEY,
    `value` TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS ai_usage (
    user_id TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    day     TEXT NOT NULL,
    count   INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY (user_id, day)
);
"""

SCHEMA_MYSQL = """
CREATE TABLE IF NOT EXISTS users (
    id                  VARCHAR(64) PRIMARY KEY,
    username            VARCHAR(128) NOT NULL UNIQUE,
    name                VARCHAR(128) NOT NULL,
    email               VARCHAR(255) NOT NULL DEFAULT '',
    password_hash       VARCHAR(255) NOT NULL,
    avatar              LONGTEXT NOT NULL,
    motto               VARCHAR(255) NOT NULL DEFAULT '',
    xp                  INT NOT NULL DEFAULT 0,
    streak              INT NOT NULL DEFAULT 1,
    completed_subtopics LONGTEXT NOT NULL,
    today_seconds       INT NOT NULL DEFAULT 0,
    total_seconds       INT NOT NULL DEFAULT 0,
    created_at          VARCHAR(64) NOT NULL DEFAULT '',
    INDEX idx_users_username (username),
    INDEX idx_users_email (email),
    INDEX idx_users_xp (xp)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS sessions (
    token_hash VARCHAR(64) PRIMARY KEY,
    user_id    VARCHAR(64) NOT NULL,
    created_at DOUBLE NOT NULL,
    expires_at DOUBLE NOT NULL,
    INDEX idx_sessions_user (user_id),
    INDEX idx_sessions_expires (expires_at),
    CONSTRAINT fk_sessions_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS meta (
    `key`   VARCHAR(64) PRIMARY KEY,
    `value` LONGTEXT NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS ai_usage (
    user_id VARCHAR(64) NOT NULL,
    day     VARCHAR(10) NOT NULL,
    count   INT NOT NULL DEFAULT 0,
    PRIMARY KEY (user_id, day),
    CONSTRAINT fk_ai_usage_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
"""

SCHEMA_POSTGRES = """
CREATE TABLE IF NOT EXISTS users (
    id                  VARCHAR(64) PRIMARY KEY,
    username            VARCHAR(128) NOT NULL UNIQUE,
    name                VARCHAR(128) NOT NULL,
    email               VARCHAR(255) NOT NULL DEFAULT '',
    password_hash       VARCHAR(255) NOT NULL,
    avatar              TEXT NOT NULL DEFAULT '',
    motto               VARCHAR(255) NOT NULL DEFAULT '',
    xp                  INTEGER NOT NULL DEFAULT 0,
    streak              INTEGER NOT NULL DEFAULT 1,
    completed_subtopics TEXT NOT NULL DEFAULT '[]',
    today_seconds       INTEGER NOT NULL DEFAULT 0,
    total_seconds       INTEGER NOT NULL DEFAULT 0,
    created_at          VARCHAR(64) NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS sessions (
    token_hash VARCHAR(64) PRIMARY KEY,
    user_id    VARCHAR(64) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    created_at DOUBLE PRECISION NOT NULL,
    expires_at DOUBLE PRECISION NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_users_xp ON users(xp DESC);
CREATE INDEX IF NOT EXISTS idx_sessions_user ON sessions(user_id);
CREATE INDEX IF NOT EXISTS idx_sessions_expires ON sessions(expires_at);

CREATE TABLE IF NOT EXISTS meta (
    "key"   VARCHAR(64) PRIMARY KEY,
    "value" TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ai_usage (
    user_id VARCHAR(64) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    day     VARCHAR(10) NOT NULL,
    count   INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY (user_id, day)
);
"""


# ----------------------------------------------------------------- Config & Path Helpers
def data_dir():
    """Read the env var on every call so tests can point to a temp folder."""
    override = os.environ.get("ELYSIA_DATA_DIR")
    return Path(override) if override else BASE_DIR / "data"


def db_path():
    return data_dir() / "elysia.db"


def legacy_json_path():
    return data_dir() / "users.json"


def sanitize_db_url(url: str) -> str:
    """Mask password credentials in database connection URLs for safe, secret-free reporting/errors."""
    if not url:
        return ""
    try:
        parsed = urlparse(url)
        if parsed.password:
            user = parsed.username or ""
            host = parsed.hostname or ""
            port = f":{parsed.port}" if parsed.port else ""
            netloc = f"{user}:***@{host}{port}"
            return parsed._replace(netloc=netloc).geturl()
        return url
    except Exception:
        return "<redacted_database_url>"


def get_engine_type() -> str:
    """Return 'postgres', 'mysql', or 'sqlite' based on environment settings."""
    db_type = os.environ.get("DB_TYPE", "").strip().lower()
    db_url = os.environ.get("DATABASE_URL", "").strip().lower()
    if db_type in ("postgres", "postgresql") or db_url.startswith("postgresql://") or db_url.startswith("postgres://"):
        return "postgres"
    if db_type == "mysql" or db_url.startswith("mysql://") or db_url.startswith("mysql+pymysql://"):
        return "mysql"
    return "sqlite"


def is_postgres_mode() -> bool:
    return get_engine_type() == "postgres"


def is_mysql_mode() -> bool:
    return get_engine_type() == "mysql"


def get_postgres_config() -> dict:
    """Parse connection parameters from DATABASE_URL or individual PG* env vars."""
    db_url = os.environ.get("DATABASE_URL", "").strip()
    if db_url and (db_url.startswith("postgresql://") or db_url.startswith("postgres://")):
        parsed = urlparse(db_url)
        sslmode = "prefer"
        if parsed.query:
            for part in parsed.query.split("&"):
                if part.startswith("sslmode="):
                    sslmode = part.split("=", 1)[1]
        return {
            "host": parsed.hostname or "localhost",
            "port": parsed.port or 5432,
            "user": unquote(parsed.username) if parsed.username else "postgres",
            "password": unquote(parsed.password) if parsed.password else "",
            "database": parsed.path.lstrip("/") if parsed.path else "postgres",
            "sslmode": os.environ.get("PGSSLMODE") or sslmode,
        }
    return {
        "host": os.environ.get("PGHOST", "localhost"),
        "port": int(os.environ.get("PGPORT", 5432)),
        "user": os.environ.get("PGUSER", "postgres"),
        "password": os.environ.get("PGPASSWORD", ""),
        "database": os.environ.get("PGDATABASE", "postgres"),
        "sslmode": os.environ.get("PGSSLMODE", "prefer"),
    }


def get_mysql_config() -> dict:
    """Parse connection parameters from DATABASE_URL or individual MYSQL_* env vars."""
    db_url = os.environ.get("DATABASE_URL", "").strip()
    if db_url and (db_url.startswith("mysql://") or db_url.startswith("mysql+pymysql://")):
        clean_url = db_url.replace("mysql+pymysql://", "mysql://", 1)
        parsed = urlparse(clean_url)
        return {
            "host": parsed.hostname or "localhost",
            "port": parsed.port or 3306,
            "user": unquote(parsed.username) if parsed.username else "root",
            "password": unquote(parsed.password) if parsed.password else "",
            "database": parsed.path.lstrip("/") if parsed.path else "elysia_code",
        }
    return {
        "host": os.environ.get("MYSQL_HOST", "localhost"),
        "port": int(os.environ.get("MYSQL_PORT", 3306)),
        "user": os.environ.get("MYSQL_USER", "root"),
        "password": os.environ.get("MYSQL_PASSWORD", ""),
        "database": os.environ.get("MYSQL_DATABASE") or os.environ.get("MYSQL_DB", "elysia_code"),
    }


# ----------------------------------------------------------------- Migration & Seed
def _migrate_legacy_json(conn):
    """Import users from legacy data/users.json ONE time (file is left untouched)."""
    try:
        done = conn.execute("SELECT `value` FROM meta WHERE `key`='legacy_json_imported'").fetchone()
        if done:
            return
    except Exception as exc:
        logger.warning("Could not check legacy migration metadata: %s", exc)

    path = legacy_json_path()
    imported = 0
    if path.exists():
        try:
            users = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            logger.warning("Could not parse legacy users.json: %s", exc)
            users = {}
        for ident, u in (users or {}).items():
            if not isinstance(u, dict):
                continue
            username = str(u.get("username") or ident).strip().lower()
            # Safety filter: never seed synthetic test accounts or test fixtures into production database
            if username.startswith("test_user") or username.startswith("loadtest_"):
                continue
            try:
                conn.execute(
                    "INSERT OR IGNORE INTO users (id, username, name, email, password_hash, avatar,"
                    " motto, xp, streak, completed_subtopics, today_seconds, total_seconds, created_at)"
                    " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (
                        str(u.get("id") or "usr_%s" % os.urandom(6).hex()),
                        username,
                        str(u.get("name") or "Coder"),
                        str(u.get("email") or ""),
                        str(u.get("password_hash") or ""),
                        str(u.get("avatar") or ""),
                        str(u.get("motto") or ""),
                        int(u.get("xp") or 0),
                        max(1, int(u.get("streak") or 1)),
                        json.dumps(list(u.get("completed_subtopics") or [])),
                        int(u.get("today_seconds") or 0),
                        int(u.get("total_seconds") or 0),
                        str(u.get("created_at") or ""),
                    ),
                )
                imported += 1
            except Exception as exc:
                logger.warning("Failed importing user %s during legacy migration: %s", username, exc)
                continue
    try:
        conn.execute("REPLACE INTO meta (`key`, `value`) VALUES ('legacy_json_imported', ?)",
                     (str(imported),))
    except Exception as exc:
        logger.warning("Could not save legacy migration meta flag: %s", exc)


# ----------------------------------------------------------------- PostgreSQL Connection Pool & Adapter
def translate_sql_for_postgres(sql: str) -> str:
    """
    Translates SQLite/MySQL-style SQL statements to PostgreSQL syntax:
    1. Replaces ? placeholders outside of single-quoted string literals with %s.
    2. Replaces backticks (`identifier`) with standard double quotes ("identifier").
    3. Translates INSERT OR IGNORE INTO <table> (...) to INSERT INTO <table> (...) ON CONFLICT DO NOTHING.
    4. Translates INSERT OR REPLACE INTO / REPLACE INTO meta (...) to ON CONFLICT ("key") DO UPDATE.
    5. Recognizes PRAGMA statements as no-ops.
    """
    if not sql or not sql.strip():
        return sql

    clean_sql = sql.strip()

    # Check for SQLite PRAGMAs
    if clean_sql.upper().startswith("PRAGMA "):
        return "-- PRAGMA_NOOP: " + clean_sql

    # Translate INSERT OR IGNORE INTO ... -> INSERT INTO ... ON CONFLICT DO NOTHING
    if re.match(r"^\s*INSERT\s+OR\s+IGNORE\s+INTO\s+", clean_sql, re.IGNORECASE):
        clean_sql = re.sub(r"^\s*INSERT\s+OR\s+IGNORE\s+INTO\s+", "INSERT INTO ", clean_sql, flags=re.IGNORECASE)
        if "ON CONFLICT" not in clean_sql.upper():
            had_semicolon = clean_sql.endswith(";")
            clean_sql = clean_sql.rstrip("; \t\r\n") + " ON CONFLICT DO NOTHING"
            if had_semicolon:
                clean_sql += ";"

    # Translate REPLACE INTO / INSERT OR REPLACE INTO meta ... -> INSERT INTO meta ... ON CONFLICT ("key") DO UPDATE ...
    if re.match(r"^\s*(INSERT\s+OR\s+REPLACE|REPLACE)\s+INTO\s+meta\b", clean_sql, re.IGNORECASE):
        clean_sql = re.sub(r"^\s*(INSERT\s+OR\s+REPLACE|REPLACE)\s+INTO\s+", "INSERT INTO ", clean_sql, flags=re.IGNORECASE)
        if "ON CONFLICT" not in clean_sql.upper():
            had_semicolon = clean_sql.endswith(";")
            clean_sql = clean_sql.rstrip("; \t\r\n") + ' ON CONFLICT ("key") DO UPDATE SET "value" = EXCLUDED."value"'
            if had_semicolon:
                clean_sql += ";"

    # State-machine replacement of ? -> %s and ` -> " outside of string literals
    out = []
    in_single_quote = False
    in_double_quote = False
    in_comment = False
    i = 0
    n = len(clean_sql)

    while i < n:
        c = clean_sql[i]

        # Handle line comments (-- ...)
        if not in_single_quote and not in_double_quote and c == '-' and i + 1 < n and clean_sql[i+1] == '-':
            in_comment = True
            out.append(c)
            i += 1
            continue
        if in_comment:
            out.append(c)
            if c == '\n':
                in_comment = False
            i += 1
            continue

        # Handle single quotes
        if c == "'":
            if in_single_quote:
                # Check for escaped single quote ''
                if i + 1 < n and clean_sql[i+1] == "'":
                    out.append("''")
                    i += 2
                    continue
                in_single_quote = False
            else:
                if not in_double_quote:
                    in_single_quote = True
            out.append(c)
            i += 1
            continue

        # Handle double quotes
        if c == '"':
            if in_double_quote:
                in_double_quote = False
            else:
                if not in_single_quote:
                    in_double_quote = True
            out.append(c)
            i += 1
            continue

        # Inside single-quoted strings: preserve exact characters
        if in_single_quote:
            out.append(c)
            i += 1
            continue

        # Outside single quotes: replace ` with "
        if c == '`':
            out.append('"')
            i += 1
            continue

        # Outside single quotes: replace ? with %s
        if c == '?':
            out.append('%s')
            i += 1
            continue

        out.append(c)
        i += 1

    return "".join(out)


class PostgresRow:
    """Provides dual access (by column name or positional index) matching sqlite3.Row."""

    def __init__(self, data_dict: dict, data_tuple: tuple, description=None):
        self._dict = {str(k).lower(): v for k, v in data_dict.items()} if data_dict else {}
        self._tuple = data_tuple or ()
        self._desc = description

    def __getitem__(self, key):
        if isinstance(key, int):
            return self._tuple[key]
        lower_k = str(key).lower()
        if lower_k in self._dict:
            return self._dict[lower_k]
        raise KeyError(key)

    def __iter__(self):
        return iter(self._tuple)

    def __len__(self):
        return len(self._tuple)

    def __contains__(self, key):
        if isinstance(key, int):
            return 0 <= key < len(self._tuple)
        return str(key).lower() in self._dict

    def keys(self):
        return list(self._dict.keys())

    def get(self, key, default=None):
        if isinstance(key, int):
            return self._tuple[key] if 0 <= key < len(self._tuple) else default
        return self._dict.get(str(key).lower(), default)

    def __eq__(self, other):
        if isinstance(other, (tuple, list)):
            return self._tuple == tuple(other)
        if isinstance(other, dict):
            return self._dict == {str(k).lower(): v for k, v in other.items()}
        return super().__eq__(other)

    def __repr__(self):
        return f"<PostgresRow {self._dict}>"


class PostgresCursorWrapper:
    """Wraps PostgreSQL cursor to provide an API matching SQLite syntax and row access."""

    def __init__(self, cursor):
        self._cursor = cursor

    def execute(self, sql, params=None):
        clean_sql = translate_sql_for_postgres(sql)
        if clean_sql.startswith("-- PRAGMA_NOOP:"):
            return self
        if params is not None:
            self._cursor.execute(clean_sql, tuple(params) if isinstance(params, list) else params)
        else:
            self._cursor.execute(clean_sql)
        return self

    def fetchone(self):
        raw = self._cursor.fetchone()
        if raw is None:
            return None
        return self._wrap_row(raw)

    def fetchall(self):
        rows = self._cursor.fetchall()
        return [self._wrap_row(r) for r in rows]

    def _wrap_row(self, raw):
        desc = getattr(self._cursor, "description", None)
        if desc:
            col_names = [d[0] for d in desc]
            if isinstance(raw, dict):
                return PostgresRow(raw, tuple(raw.get(c) for c in col_names), desc)
            else:
                raw_tuple = tuple(raw)
                return PostgresRow(dict(zip(col_names, raw_tuple)), raw_tuple, desc)
        if isinstance(raw, dict):
            return PostgresRow(raw, tuple(raw.values()))
        return PostgresRow({}, tuple(raw))

    def close(self):
        try:
            self._cursor.close()
        except Exception as exc:
            logger.warning("Error closing Postgres cursor: %s", exc)


class PostgresNoOpCursor:
    """No-op cursor for SQLite PRAGMAs executed against PostgreSQL."""

    def execute(self, sql, params=None):
        return self

    def fetchone(self):
        return None

    def fetchall(self):
        return []

    def close(self):
        pass


class PostgresConnectionWrapper:
    """Provides a connection wrapper that supports .execute() directly like sqlite3.Connection."""

    def __init__(self, raw_conn):
        self._raw_conn = raw_conn
        self._cursors = []

    def execute(self, sql, params=None):
        clean_sql = translate_sql_for_postgres(sql)
        if clean_sql.startswith("-- PRAGMA_NOOP:"):
            return PostgresNoOpCursor()
        raw_cur = self._raw_conn.cursor()
        self._cursors.append(raw_cur)
        wrapper = PostgresCursorWrapper(raw_cur)
        wrapper.execute(sql, params)
        return wrapper

    def commit(self):
        self._raw_conn.commit()

    def rollback(self):
        self._raw_conn.rollback()

    def close(self):
        for c in self._cursors:
            try:
                c.close()
            except Exception as exc:
                logger.warning("Error closing cursor: %s", exc)
        self._cursors.clear()


class _PostgresPool:
    """Thread-safe connection pool for PostgreSQL with automatic reconnection and password sanitization."""

    def __init__(self, max_size=25):
        self._max_size = max_size
        self._pool = queue.Queue(maxsize=max_size)
        self._created_lock = threading.Lock()
        self._created_count = 0

    def _create_connection(self):
        cfg = get_postgres_config()
        if not HAS_PSYCOPG2 and not HAS_PSYCOPG:
            raise RuntimeError(
                "PostgreSQL engine is configured, but neither 'psycopg2' nor 'psycopg' is installed. "
                "Please run: pip install psycopg2-binary"
            )

        sanitized_info = f"{cfg['user']}@{cfg['host']}:{cfg['port']}/{cfg['database']}"
        raw_url = os.environ.get("DATABASE_URL", "")
        if raw_url:
            sanitized_info = sanitize_db_url(raw_url)

        try:
            if HAS_PSYCOPG2:
                return psycopg2.connect(
                    host=cfg["host"],
                    port=cfg["port"],
                    user=cfg["user"],
                    password=cfg["password"],
                    dbname=cfg["database"],
                    sslmode=cfg.get("sslmode", "prefer"),
                    connect_timeout=10,
                )
            elif HAS_PSYCOPG:
                return psycopg.connect(
                    host=cfg["host"],
                    port=cfg["port"],
                    user=cfg["user"],
                    password=cfg["password"],
                    dbname=cfg["database"],
                    sslmode=cfg.get("sslmode", "prefer"),
                    connect_timeout=10,
                )
        except Exception as e:
            clean_err = str(e)
            if cfg.get("password") and cfg["password"] in clean_err:
                clean_err = clean_err.replace(cfg["password"], "***")
            raise ConnectionError(
                f"Failed to connect to PostgreSQL at {sanitized_info}: {clean_err}"
            ) from None

    def _is_live(self, conn):
        try:
            if hasattr(conn, "closed") and conn.closed != 0:
                return False
            with conn.cursor() as cur:
                cur.execute("SELECT 1")
            return True
        except Exception:
            return False

    def _safely_close(self, conn):
        with self._created_lock:
            if self._created_count > 0:
                self._created_count -= 1
        try:
            conn.close()
        except Exception as exc:
            logger.warning("Error safely closing connection: %s", exc)

    def get(self, timeout=10.0):
        # 1. Try to get an idle connection from the pool without blocking
        while not self._pool.empty():
            try:
                conn = self._pool.get_nowait()
                if self._is_live(conn):
                    return conn
                self._safely_close(conn)
            except queue.Empty:
                break

        # 2. If under max_size, create a new connection
        with self._created_lock:
            if self._created_count < self._max_size:
                conn = self._create_connection()
                self._created_count += 1
                return conn

        # 3. Max capacity reached: block and wait for a connection to be returned
        try:
            deadline = time.time() + timeout
            while time.time() < deadline:
                remaining = max(0.1, deadline - time.time())
                conn = self._pool.get(timeout=remaining)
                if self._is_live(conn):
                    return conn
                self._safely_close(conn)
                with self._created_lock:
                    if self._created_count < self._max_size:
                        conn = self._create_connection()
                        self._created_count += 1
                        return conn
        except queue.Empty:
            raise TimeoutError("PostgreSQL connection pool exhausted. Timeout waiting for available connection.")

        return self._create_connection()

    def put(self, conn):
        try:
            if hasattr(conn, "closed") and conn.closed == 0:
                self._pool.put_nowait(conn)
            else:
                self._safely_close(conn)
        except queue.Full:
            self._safely_close(conn)


_postgres_pool_instance = None
_postgres_pool_lock = threading.Lock()


def _get_postgres_pool():
    global _postgres_pool_instance
    if _postgres_pool_instance is None:
        with _postgres_pool_lock:
            if _postgres_pool_instance is None:
                _postgres_pool_instance = _PostgresPool(max_size=25)
    return _postgres_pool_instance


def _init_postgres(raw_conn):
    """Run DDL statements to ensure users, sessions, and meta tables exist in PostgreSQL."""
    wrapper = PostgresConnectionWrapper(raw_conn)
    for stmt in SCHEMA_POSTGRES.strip().split(";"):
        clean_stmt = stmt.strip()
        if clean_stmt:
            wrapper.execute(clean_stmt)
    _migrate_legacy_json(wrapper)
    wrapper.commit()
    wrapper.close()


# ----------------------------------------------------------------- MySQL Connection Pool & Adapter
def _translate_sqlite_to_mysql(sql: str, has_params: bool = False) -> str:
    """
    Translates SQLite SQL statements to MySQL syntax:
    1. INSERT OR IGNORE INTO -> INSERT IGNORE INTO
    2. INSERT OR REPLACE INTO -> REPLACE INTO
    3. State-machine parses SQL outside of string literals:
       - Replaces ? parameter placeholders with %s
       - Does NOT replace ? inside single or double-quoted string literals
       - When params are passed (has_params=True), escapes literal % as %% so MySQL DB-API
         format string substitution does not fail on LIKE patterns (e.g. LIKE '%x%').
    """
    clean_sql = sql.strip()
    if re.match(r"^\s*INSERT\s+OR\s+IGNORE\s+INTO\s+", clean_sql, re.IGNORECASE):
        clean_sql = re.sub(r"^\s*INSERT\s+OR\s+IGNORE\s+INTO\s+", "INSERT IGNORE INTO ", clean_sql, flags=re.IGNORECASE)
    elif re.match(r"^\s*INSERT\s+OR\s+REPLACE\s+INTO\s+", clean_sql, re.IGNORECASE):
        clean_sql = re.sub(r"^\s*INSERT\s+OR\s+REPLACE\s+INTO\s+", "REPLACE INTO ", clean_sql, flags=re.IGNORECASE)

    out = []
    in_single_quote = False
    in_double_quote = False
    in_comment = False
    i = 0
    n = len(clean_sql)

    while i < n:
        c = clean_sql[i]

        # Handle line comments (-- ...)
        if not in_single_quote and not in_double_quote and c == '-' and i + 1 < n and clean_sql[i+1] == '-':
            in_comment = True
            out.append(c)
            i += 1
            continue
        if in_comment:
            out.append(c)
            if c == '\n':
                in_comment = False
            i += 1
            continue

        # Single quote tracking
        if c == "'" and not in_double_quote:
            in_single_quote = not in_single_quote
            out.append(c)
            i += 1
            continue

        # Double quote tracking
        if c == '"' and not in_single_quote:
            in_double_quote = not in_double_quote
            out.append(c)
            i += 1
            continue

        # Inside quoted string:
        if in_single_quote or in_double_quote:
            if has_params and c == '%':
                if i + 1 < n and clean_sql[i+1] == '%':
                    out.append('%%')
                    i += 2
                    continue
                else:
                    out.append('%%')
                    i += 1
                    continue
            out.append(c)
            i += 1
            continue

        # Outside strings:
        if c == '?':
            out.append('%s')
            i += 1
            continue

        if has_params and c == '%':
            if i + 1 < n and clean_sql[i+1] == '%':
                out.append('%%')
                i += 2
                continue
            else:
                out.append('%%')
                i += 1
                continue

        out.append(c)
        i += 1

    return "".join(out)


class MySQLCursorWrapper:
    """Wraps MySQL cursor to provide a unified API matching SQLite syntax and row access."""

    def __init__(self, cursor):
        self._cursor = cursor

    def execute(self, sql, params=None):
        has_params = params is not None
        clean_sql = _translate_sqlite_to_mysql(sql, has_params=has_params)

        if has_params:
            self._cursor.execute(clean_sql, params)
        else:
            self._cursor.execute(clean_sql)
        return self

    def fetchone(self):
        return self._cursor.fetchone()

    def fetchall(self):
        return self._cursor.fetchall()

    def close(self):
        try:
            self._cursor.close()
        except Exception as exc:
            logger.warning("Error closing Postgres cursor: %s", exc)


class MySQLConnectionWrapper:
    """Provides a connection wrapper that supports .execute() directly like sqlite3.Connection."""

    def __init__(self, raw_conn):
        self._raw_conn = raw_conn
        self._cursors = []

    def execute(self, sql, params=None):
        if HAS_PYMYSQL:
            raw_cur = self._raw_conn.cursor(cursor=pymysql.cursors.DictCursor)
        elif HAS_MYSQL_CONNECTOR:
            raw_cur = self._raw_conn.cursor(dictionary=True)
        else:
            raw_cur = self._raw_conn.cursor()
        self._cursors.append(raw_cur)
        wrapper = MySQLCursorWrapper(raw_cur)
        wrapper.execute(sql, params)
        return wrapper

    def commit(self):
        self._raw_conn.commit()

    def rollback(self):
        self._raw_conn.rollback()

    def close(self):
        for c in self._cursors:
            try:
                c.close()
            except Exception as exc:
                logger.warning("Error closing cursor: %s", exc)
        self._cursors.clear()


class _MySQLPool:
    """Thread-safe connection pool with automatic reconnect."""

    def __init__(self, max_size=20):
        self._max_size = max_size
        self._pool = queue.Queue(maxsize=max_size)

    def _create_connection(self):
        cfg = get_mysql_config()
        if HAS_PYMYSQL:
            return pymysql.connect(
                host=cfg["host"],
                port=cfg["port"],
                user=cfg["user"],
                password=cfg["password"],
                database=cfg["database"],
                charset="utf8mb4",
                autocommit=False,
                cursorclass=pymysql.cursors.DictCursor,
                connect_timeout=10,
            )
        elif HAS_MYSQL_CONNECTOR:
            return mysql.connector.connect(
                host=cfg["host"],
                port=cfg["port"],
                user=cfg["user"],
                password=cfg["password"],
                database=cfg["database"],
                charset="utf8mb4",
                autocommit=False,
                connection_timeout=10,
            )
        else:
            raise RuntimeError(
                "DB_TYPE='mysql' is set, but neither 'pymysql' nor "
                "'mysql-connector-python' is installed.\nPlease run: pip install pymysql"
            )

    def get(self):
        while not self._pool.empty():
            try:
                conn = self._pool.get_nowait()
                # Test connection liveness
                try:
                    if hasattr(conn, "ping"):
                        conn.ping(reconnect=True)
                    return conn
                except Exception:
                    try:
                        conn.close()
                    except Exception as exc:
                        logger.warning("Error closing dead connection from pool: %s", exc)
            except queue.Empty:
                break
        return self._create_connection()

    def put(self, conn):
        try:
            self._pool.put_nowait(conn)
        except queue.Full:
            try:
                conn.close()
            except Exception as exc:
                logger.warning("Error closing excess pooled connection: %s", exc)


_mysql_pool_instance = None
_mysql_pool_lock = threading.Lock()


def _get_mysql_pool():
    global _mysql_pool_instance
    if _mysql_pool_instance is None:
        with _mysql_pool_lock:
            if _mysql_pool_instance is None:
                _mysql_pool_instance = _MySQLPool(max_size=25)
    return _mysql_pool_instance


def _init_mysql(raw_conn):
    """Run DDL statements to ensure users, sessions, and meta tables exist in MySQL."""
    wrapper = MySQLConnectionWrapper(raw_conn)
    for stmt in SCHEMA_MYSQL.strip().split(";"):
        clean_stmt = stmt.strip()
        if clean_stmt:
            wrapper.execute(clean_stmt)
    _migrate_legacy_json(wrapper)
    wrapper.commit()
    wrapper.close()


def _init_sqlite(path):
    """Run DDL statements for SQLite."""
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(path), timeout=10)
    try:
        conn.execute("PRAGMA journal_mode=WAL")
        conn.executescript(SCHEMA_SQLITE)
        _migrate_legacy_json(conn)
        conn.commit()
    finally:
        conn.close()


# ----------------------------------------------------------------- Public Context Manager
@contextmanager
def connect():
    """
    Open a short-lived connection (thread-safe, auto-committing on success).
    Yields a connection that supports .execute(sql, params) and returns row dictionaries.
    """
    if is_postgres_mode():
        pool = _get_postgres_pool()
        raw_conn = pool.get()
        cfg = get_postgres_config()
        pool_key = "postgres_%s_%s" % (cfg.get("host"), cfg.get("database"))
        if pool_key not in _initialised:
            with _init_lock:
                if pool_key not in _initialised:
                    _init_postgres(raw_conn)
                    _initialised.add(pool_key)
        wrapper = PostgresConnectionWrapper(raw_conn)
        try:
            yield wrapper
            wrapper.commit()
        except Exception:
            wrapper.rollback()
            raise
        finally:
            wrapper.close()
            pool.put(raw_conn)
    elif is_mysql_mode():
        pool = _get_mysql_pool()
        raw_conn = pool.get()
        cfg = get_mysql_config()
        pool_key = "mysql_%s_%s" % (cfg.get("host"), cfg.get("database"))
        if pool_key not in _initialised:
            with _init_lock:
                if pool_key not in _initialised:
                    _init_mysql(raw_conn)
                    _initialised.add(pool_key)
        wrapper = MySQLConnectionWrapper(raw_conn)
        try:
            yield wrapper
            wrapper.commit()
        except Exception:
            wrapper.rollback()
            raise
        finally:
            wrapper.close()
            pool.put(raw_conn)
    else:
        path = db_path()
        key = str(path)
        if key not in _initialised:
            with _init_lock:
                if key not in _initialised:
                    _init_sqlite(path)
                    _initialised.add(key)
        conn = sqlite3.connect(key, timeout=10)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys=ON")
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()


def now():
    return time.time()
