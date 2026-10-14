"""
=============================================================================
ELYSIA SCHOOL - USER AUTHENTICATION & PROFILE ENGINE  (hardened version)
=============================================================================
What changed compared to the first version
  * Passwords use scrypt (slow on purpose) instead of a single SHA-256.
    Old SHA-256 accounts still work and are upgraded to scrypt on next login.
  * Users live in SQLite (core/db.py) instead of data/users.json.
  * Login creates a random SESSION TOKEN (sent as an HttpOnly cookie by main.py).
    Profile/progress endpoints trust the session, NOT a username typed in the
    request body, so nobody can edit another person's account any more.
  * Login attempts are rate limited (stops password guessing).
  * Every input is validated and size-limited.
=============================================================================
"""

import base64
import hashlib
import hmac
import json
import os
import re
import secrets
import sqlite3
import threading
import time
from collections import defaultdict, deque
from typing import Any, Dict, Optional, Tuple

from core import db

# ----------------------------------------------------------------- limits
MIN_PASSWORD_LEN = 8
MAX_PASSWORD_LEN = 128
MAX_NAME_LEN = 60
MAX_MOTTO_LEN = 120
MAX_AVATAR_LEN = 400_000          # ~300 KB image as base64
MAX_COMPLETED = 500
MAX_XP = 10_000_000
MAX_STREAK = 3650
MAX_SECONDS = 60 * 60 * 24 * 365 * 10
SESSION_DAYS = 30
USERNAME_RE = re.compile(r"^[a-z0-9_.@+\-]{3,64}$")
AVATAR_IMG_RE = re.compile(r"^data:image/(png|jpeg|jpg|webp|gif);base64,[A-Za-z0-9+/=]+$")
DEFAULT_MOTTO = "Code doesn't lie, syntax errors do."

# scrypt parameters (about 16 MB memory, ~50 ms per hash on a normal laptop)
SCRYPT_N, SCRYPT_R, SCRYPT_P = 2 ** 14, 8, 1


# ----------------------------------------------------------------- passwords
def _scrypt(password: str, salt: bytes, n=SCRYPT_N, r=SCRYPT_R, p=SCRYPT_P) -> bytes:
    return hashlib.scrypt(password.encode("utf-8"), salt=salt, n=n, r=r, p=p,
                          maxmem=64 * 1024 * 1024, dklen=32)


def _hash_password(password: str) -> str:
    salt = os.urandom(16)
    digest = _scrypt(password, salt)
    return "scrypt$%d$%d$%d$%s$%s" % (SCRYPT_N, SCRYPT_R, SCRYPT_P, salt.hex(), digest.hex())


def _verify_password(password: str, stored: str) -> Tuple[bool, bool]:
    """Return (is_correct, needs_upgrade_to_scrypt)."""
    try:
        if stored.startswith("scrypt$"):
            _, n, r, p, salt_hex, hash_hex = stored.split("$")
            digest = _scrypt(password, bytes.fromhex(salt_hex), int(n), int(r), int(p))
            return hmac.compare_digest(digest.hex(), hash_hex), False
        # Legacy format from the first version: "salt:sha256hex"
        salt, old_hash = stored.split(":", 1)
        candidate = hashlib.sha256((salt + password).encode("utf-8")).hexdigest()
        ok = hmac.compare_digest(candidate, old_hash)
        return ok, ok
    except Exception:
        return False, False


# A fake hash so that "user does not exist" takes as long as "wrong password"
_DUMMY_HASH = _hash_password("not-a-real-password")


# ----------------------------------------------------------------- rate limiting
class _RateLimiter:
    """Keeps recent failures in memory: key -> timestamps. Thread-safe."""

    def __init__(self):
        self._lock = threading.Lock()
        self._fails = defaultdict(deque)

    def _trim(self, key, window, now):
        dq = self._fails[key]
        while dq and now - dq[0] > window:
            dq.popleft()
        return dq

    def blocked(self, key: str, limit: int, window: int) -> bool:
        with self._lock:
            return len(self._trim(key, window, time.time())) >= limit

    def fail(self, key: str, window: int):
        with self._lock:
            now = time.time()
            self._trim(key, window, now).append(now)
            if len(self._fails) > 50_000:      # memory guard
                self._fails.clear()

    def reset(self, key: str):
        with self._lock:
            self._fails.pop(key, None)


_limiter = _RateLimiter()
LOGIN_WINDOW = 300          # seconds
LOGIN_LIMIT_PER_USER = 5    # wrong passwords per username per window
LOGIN_LIMIT_PER_IP = 20     # wrong passwords per IP per window
REGISTER_LIMIT_PER_IP = 10  # accounts per IP per hour


# ----------------------------------------------------------------- in-memory session cache
_SESSION_CACHE = {}          # token_hash -> (expiry_time, user_dict)
_SESSION_CACHE_LOCK = threading.Lock()
_SESSION_CACHE_TTL = 30.0    # 30 seconds TTL


def _get_cached_user(token_hash: str) -> Optional[Dict[str, Any]]:
    now = time.time()
    with _SESSION_CACHE_LOCK:
        item = _SESSION_CACHE.get(token_hash)
        if item:
            exp, user = item
            if now < exp:
                return user
            _SESSION_CACHE.pop(token_hash, None)
    return None


def _set_cached_user(token_hash: str, user: Dict[str, Any]):
    with _SESSION_CACHE_LOCK:
        if len(_SESSION_CACHE) > 20_000:
            _SESSION_CACHE.clear()
        _SESSION_CACHE[token_hash] = (time.time() + _SESSION_CACHE_TTL, user)


def _invalidate_cached_user(ident_or_token: str):
    with _SESSION_CACHE_LOCK:
        keys_to_del = []
        for th, (_, u) in _SESSION_CACHE.items():
            if th == ident_or_token or u.get("id") == ident_or_token or u.get("username") == ident_or_token:
                keys_to_del.append(th)
        for k in keys_to_del:
            _SESSION_CACHE.pop(k, None)


def reset_rate_limits_for_tests():
    _limiter._fails.clear()
    with _SESSION_CACHE_LOCK:
        _SESSION_CACHE.clear()


# ----------------------------------------------------------------- helpers
def _row_to_user(row) -> Dict[str, Any]:
    """Database row -> dict for the browser (never includes the password hash)."""
    raw_sub = row["completed_subtopics"] if row else "[]"
    if isinstance(raw_sub, list):
        completed = raw_sub
    else:
        try:
            completed = json.loads(raw_sub or "[]")
        except Exception:
            completed = []
    return {
        "id": row["id"],
        "name": row["name"],
        "identifier": row["username"],
        "username": row["username"],
        "email": row["email"],
        "avatar": row["avatar"] or "\U0001F40D",
        "motto": row["motto"] or DEFAULT_MOTTO,
        "xp": row["xp"],
        "streak": row["streak"],
        "completed_subtopics": completed,
        "today_seconds": row["today_seconds"],
        "total_seconds": row["total_seconds"],
        "created_at": row["created_at"],
    }


def _clamp_int(value, low: int, high: int, default: int = 0) -> int:
    try:
        return max(low, min(high, int(value)))
    except (TypeError, ValueError, OverflowError):
        return default


def _clean_completed(value) -> list:
    if not isinstance(value, (list, tuple, set)):
        return []
    out = []
    for item in value:
        if isinstance(item, (str, int)) and len(str(item)) <= 64:
            out.append(str(item))
        if len(out) >= MAX_COMPLETED:
            break
    return out


def _validate_avatar(avatar) -> Optional[str]:
    """Return the cleaned avatar, or None if it is not acceptable."""
    if avatar is None:
        return ""
    if not isinstance(avatar, str):
        return None
    avatar = avatar.strip()
    if avatar.startswith("data:"):
        if len(avatar) > MAX_AVATAR_LEN or not AVATAR_IMG_RE.match(avatar):
            return None
        try:   # make sure the base64 part really decodes
            base64.b64decode(avatar.split(",", 1)[1], validate=True)
        except Exception:
            return None
        return avatar
    if len(avatar) > 16 or "<" in avatar or ">" in avatar:
        return None          # a short emoji only
    return avatar


# ----------------------------------------------------------------- register / login
def register_user(
    name: str,
    identifier: str = "",
    password: str = "",
    avatar: str = "\U0001F40D",
    motto: str = DEFAULT_MOTTO,
    username: str = "",
    email: str = "",
    xp: int = 0,
    streak: int = 1,
    completed_subtopics: Optional[list] = None,
    today_seconds: int = 0,
    total_seconds: int = 0,
    client_ip: str = "",
    honeypot: str = "",
    hp: str = "",
) -> Dict[str, Any]:
    # Honeypot spam bot trap
    if (honeypot or hp or "").strip():
        return {"success": False, "error": "Automated spam submission detected."}

    name = (name or "").strip()
    ident = (identifier or username or email or "").strip().lower()
    password = (password or "").strip()

    if not name:
        return {"success": False, "error": "Please enter your full name."}
    if len(name) > MAX_NAME_LEN:
        return {"success": False, "error": "Name is too long (max %d characters)." % MAX_NAME_LEN}
    if not ident:
        return {"success": False, "error": "Please enter a username or email."}
    if not USERNAME_RE.match(ident):
        return {"success": False, "error": "Username must be 3-64 characters: letters, numbers and . _ - @ + only."}
    if len(password) < MIN_PASSWORD_LEN:
        return {"success": False, "error": "Password must be at least %d characters long." % MIN_PASSWORD_LEN}
    if len(password) > MAX_PASSWORD_LEN:
        return {"success": False, "error": "Password is too long (max %d characters)." % MAX_PASSWORD_LEN}

    clean_avatar = _validate_avatar(avatar)
    if clean_avatar is None:
        return {"success": False, "error": "Profile picture must be a PNG/JPEG/WEBP/GIF under 300 KB, or an emoji."}
    motto = (motto or DEFAULT_MOTTO).strip()[:MAX_MOTTO_LEN]
    email = (str(email or "").strip()[:120]) or (ident if "@" in ident else "%s@elysia.local" % ident)

    if client_ip and _limiter.blocked("reg:" + client_ip, REGISTER_LIMIT_PER_IP, 3600):
        return {"success": False, "error": "Too many accounts created from this network. Please try later."}

    user_id = "usr_%d_%s" % (int(time.time()), secrets.token_hex(3))
    try:
        with db.connect() as conn:
            conn.execute(
                "INSERT INTO users (id, username, name, email, password_hash, avatar, motto, xp, streak,"
                " completed_subtopics, today_seconds, total_seconds, created_at)"
                " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (user_id, ident, name, email, _hash_password(password), clean_avatar or "\U0001F40D", motto,
                 _clamp_int(xp, 0, MAX_XP), max(1, _clamp_int(streak, 0, MAX_STREAK, 1)),
                 json.dumps(_clean_completed(completed_subtopics)),
                 _clamp_int(today_seconds, 0, MAX_SECONDS), _clamp_int(total_seconds, 0, MAX_SECONDS),
                 time.strftime("%Y-%m-%d %H:%M:%S")),
            )
            row = conn.execute("SELECT * FROM users WHERE id=?", (user_id,)).fetchone()
    except db.IntegrityError:
        return {"success": False,
                "error": "An account with this username or email already exists. Please Log In."}

    if client_ip:
        _limiter.fail("reg:" + client_ip, 3600)   # counts each created account
    return {"success": True, "message": "Account created successfully!", "user": _row_to_user(row)}


def login_user(identifier: str = "", password: str = "", username: str = "", email: str = "",
               client_ip: str = "") -> Dict[str, Any]:
    ident = (identifier or username or email or "").strip().lower()
    password = (password or "").strip()

    if not ident or not password:
        return {"success": False, "error": "Please enter both username and password."}
    if len(ident) > 128 or len(password) > MAX_PASSWORD_LEN:
        return {"success": False, "error": "Invalid username or password. Please try again."}

    user_key, ip_key = "user:" + ident, "ip:" + client_ip
    if _limiter.blocked(user_key, LOGIN_LIMIT_PER_USER, LOGIN_WINDOW) or \
            (client_ip and _limiter.blocked(ip_key, LOGIN_LIMIT_PER_IP, LOGIN_WINDOW)):
        return {"success": False, "rate_limited": True,
                "error": "Too many failed attempts. Please wait 5 minutes and try again."}

    with db.connect() as conn:
        row = conn.execute("SELECT * FROM users WHERE username=?", (ident,)).fetchone()
        if row is None:
            _verify_password(password, _DUMMY_HASH)          # keep timing similar
            ok, upgrade = False, False
        else:
            ok, upgrade = _verify_password(password, row["password_hash"])

        if not ok:
            _limiter.fail(user_key, LOGIN_WINDOW)
            if client_ip:
                _limiter.fail(ip_key, LOGIN_WINDOW)
            return {"success": False, "error": "Invalid username or password. Please try again."}

        if upgrade:   # old SHA-256 hash -> modern scrypt, silently
            conn.execute("UPDATE users SET password_hash=? WHERE id=?", (_hash_password(password), row["id"]))

    _limiter.reset(user_key)
    return {"success": True, "message": "Welcome back, %s!" % row["name"], "user": _row_to_user(row)}


# ----------------------------------------------------------------- sessions
def create_session(user_id: str) -> str:
    """Return a new random token. Only its SHA-256 is stored in the database."""
    token = secrets.token_urlsafe(32)
    token_hash = hashlib.sha256(token.encode("ascii")).hexdigest()
    now = db.now()
    with db.connect() as conn:
        conn.execute("DELETE FROM sessions WHERE expires_at < ?", (now,))
        conn.execute("INSERT INTO sessions (token_hash, user_id, created_at, expires_at) VALUES (?,?,?,?)",
                     (token_hash, user_id, now, now + SESSION_DAYS * 86400))
    return token


def user_for_token(token: str) -> Optional[Dict[str, Any]]:
    if not token or len(token) > 200:
        return None
    token_hash = hashlib.sha256(token.encode("utf-8", "ignore")).hexdigest()
    cached = _get_cached_user(token_hash)
    if cached is not None:
        return cached

    with db.connect() as conn:
        row = conn.execute(
            "SELECT u.* FROM sessions s JOIN users u ON u.id = s.user_id "
            "WHERE s.token_hash=? AND s.expires_at > ?", (token_hash, db.now())).fetchone()
    user = _row_to_user(row) if row else None
    if user:
        _set_cached_user(token_hash, user)
    return user


def delete_session(token: str):
    if not token:
        return
    token_hash = hashlib.sha256(token.encode("utf-8", "ignore")).hexdigest()
    _invalidate_cached_user(token_hash)
    with db.connect() as conn:
        conn.execute("DELETE FROM sessions WHERE token_hash=?", (token_hash,))


# ----------------------------------------------------------------- profile / progress
def update_profile(identifier: str = "", name: Optional[str] = None, avatar: Optional[str] = None,
                   motto: Optional[str] = None, username: str = "", email: str = "") -> Dict[str, Any]:
    """`identifier` must come from a verified session (main.py does that), never from user input."""
    ident = (identifier or username or email or "").strip().lower()

    updates = {}
    if name is not None and str(name).strip():
        if len(str(name).strip()) > MAX_NAME_LEN:
            return {"success": False, "error": "Name is too long (max %d characters)." % MAX_NAME_LEN}
        updates["name"] = str(name).strip()
    if avatar:
        clean = _validate_avatar(avatar)
        if clean is None:
            return {"success": False, "error": "Profile picture must be a PNG/JPEG/WEBP/GIF under 300 KB, or an emoji."}
        updates["avatar"] = clean
    if motto is not None and str(motto).strip():
        updates["motto"] = str(motto).strip()[:MAX_MOTTO_LEN]

    with db.connect() as conn:
        row = conn.execute("SELECT * FROM users WHERE username=?", (ident,)).fetchone()
        if row is None:
            return {"success": False, "error": "User account not found."}
        if updates:
            cols = ", ".join("%s=?" % c for c in updates)          # column names are fixed above
            conn.execute("UPDATE users SET %s WHERE id=?" % cols, list(updates.values()) + [row["id"]])
            row = conn.execute("SELECT * FROM users WHERE id=?", (row["id"],)).fetchone()
    _invalidate_cached_user(ident)
    return {"success": True, "message": "Profile updated successfully!", "user": _row_to_user(row)}


def sync_user_progress(identifier: str = "", xp: int = 0, streak: int = 1, completed: Optional[list] = None,
                       today_sec: int = 0, total_sec: int = 0, username: str = "", email: str = "",
                       completed_subtopics: Optional[list] = None, today_seconds: int = 0,
                       total_seconds: int = 0) -> Dict[str, Any]:
    ident = (identifier or username or email or "").strip().lower()
    done = _clean_completed(completed or completed_subtopics or [])

    with db.connect() as conn:
        row = conn.execute("SELECT * FROM users WHERE username=?", (ident,)).fetchone()
        if row is None:
            return {"success": False, "error": "User not found."}
        raw_old = row["completed_subtopics"] if row else "[]"
        if isinstance(raw_old, list):
            old_done = raw_old
        else:
            try:
                old_done = json.loads(raw_old or "[]")
            except Exception:
                old_done = []
        merged = _clean_completed(list(dict.fromkeys(list(old_done) + done)))
        conn.execute(
            "UPDATE users SET xp=?, streak=?, completed_subtopics=?, today_seconds=?, total_seconds=? WHERE id=?",
            (max(row["xp"], _clamp_int(xp, 0, MAX_XP)),
             max(row["streak"], _clamp_int(streak, 1, MAX_STREAK, 1)),
             json.dumps(merged),
             _clamp_int(today_sec or today_seconds, 0, MAX_SECONDS),
             max(row["total_seconds"], _clamp_int(total_sec or total_seconds, 0, MAX_SECONDS)),   # never goes backwards
             row["id"]))
        row = conn.execute("SELECT * FROM users WHERE id=?", (row["id"],)).fetchone()
    _invalidate_cached_user(ident)
    return {"success": True, "user": _row_to_user(row)}
