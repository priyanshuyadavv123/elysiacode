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
import os
import queue
import sqlite3
import threading
import time
from contextlib import contextmanager
from pathlib import Path
from urllib.parse import urlparse, unquote

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

# Unified IntegrityError tuple so callers can catch constraint violations across engines
_err_list = [sqlite3.IntegrityError]
if HAS_PYMYSQL:
    _err_list.append(pymysql.err.IntegrityError)
if HAS_MYSQL_CONNECTOR:
    _err_list.append(mysql.connector.errors.IntegrityError)
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


def get_engine_type() -> str:
    """Return 'mysql' or 'sqlite' based on environment settings."""
    db_type = os.environ.get("DB_TYPE", "").strip().lower()
    db_url = os.environ.get("DATABASE_URL", "").strip().lower()
    if db_type == "mysql" or db_url.startswith("mysql://") or db_url.startswith("mysql+pymysql://"):
        return "mysql"
    return "sqlite"


def is_mysql_mode() -> bool:
    return get_engine_type() == "mysql"


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
    except Exception:
        pass

    path = legacy_json_path()
    imported = 0
    if path.exists():
        try:
            users = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
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
            except Exception:
                continue
    try:
        conn.execute("REPLACE INTO meta (`key`, `value`) VALUES ('legacy_json_imported', ?)",
                     (str(imported),))
    except Exception:
        pass


# ----------------------------------------------------------------- MySQL Connection Pool & Adapter
class MySQLCursorWrapper:
    """Wraps MySQL cursor to provide a unified API matching SQLite syntax and row access."""

    def __init__(self, cursor):
        self._cursor = cursor

    def execute(self, sql, params=None):
        clean_sql = sql
        # Adapt common SQLite syntax to MySQL
        if "INSERT OR IGNORE INTO" in clean_sql:
            clean_sql = clean_sql.replace("INSERT OR IGNORE INTO", "INSERT IGNORE INTO")
        if "INSERT OR REPLACE INTO" in clean_sql:
            clean_sql = clean_sql.replace("INSERT OR REPLACE INTO", "REPLACE INTO")
        # Replace ? with %s for MySQL parameter binding
        if params is not None and "?" in clean_sql:
            clean_sql = clean_sql.replace("?", "%s")

        if params is not None:
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
        except Exception:
            pass


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
            except Exception:
                pass
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
                    except Exception:
                        pass
            except queue.Empty:
                break
        return self._create_connection()

    def put(self, conn):
        try:
            self._pool.put_nowait(conn)
        except queue.Full:
            try:
                conn.close()
            except Exception:
                pass


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
    if is_mysql_mode():
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
