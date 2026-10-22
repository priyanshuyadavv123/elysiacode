#!/usr/bin/env python3
"""
=============================================================================
ELYSIA SCHOOL - BACKEND SERVER & REST API  (hardened version)
=============================================================================
Runs with the Python standard library only (no pip packages).

Environment variables
  PORT                       port to listen on (default 8080)
  HOST                       address to bind. Default 127.0.0.1 (only YOUR computer
                             can open the site). Hosting platforms need 0.0.0.0.
  ELYSIA_DATA_DIR            folder for the SQLite database (default ./data).
                             On Render attach a persistent disk and point this to it.
  ELYSIA_ALLOW_SERVER_EXEC   1 / 0. Run student code on the SERVER. Default: ON when
                             HOST is localhost, OFF otherwise. On a public site the
                             code runs in the browser (Pyodide) instead - this is
                             the safe setup.
  ELYSIA_TRUST_PROXY         1 if you are behind a proxy that sets X-Forwarded-For
                             (Render does; detected automatically via RENDER).

Security summary (what this file enforces)
  * Login creates an HttpOnly session cookie; profile/progress endpoints use the
    session, never a username from the request body.
  * POST requests must be JSON and (if an Origin header exists) same-origin -> CSRF.
  * No wildcard CORS, request size limit, security headers, no directory listing.
  * /api/execute is gated and limited (see core/limited_runner.py).
=============================================================================
"""

import http.cookies
import http.server
import json
import logging
import os
import socketserver
import sys
import threading
import urllib.parse
import gzip
import mimetypes
from pathlib import Path

logger = logging.getLogger("elysia")

BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

from core import config
from core.config import get_env_flag as _env_flag
from core.curriculum import CURRICULUM_DATA
from core.curriculum_builder import PARTS_REGISTRY, get_all_chapters as get_all_curriculum_chapters
from core.ai_tutor import ai_tutor
from core.question_bank import get_questions, QUESTIONS_DATABASE
from core.mock_tests import get_mock_exam, MOCK_EXAMS
from core.socratic_ai import decode_error
from core.lab_exporter import generate_lab_record_html
from core.handbook_data import get_all_chapters, get_chapter, HANDBOOK_CHAPTERS
from core import auth
from core.auth import register_user, login_user, update_profile, sync_user_progress
from core.limited_runner import run_python


# ----------------------------------------------------------------- configuration
PORT = int(os.environ.get("PORT", 8080))
HOST = os.environ.get("HOST", "127.0.0.1")
WEB_DIR = BASE_DIR / "web"
LOCAL_ONLY = HOST in ("127.0.0.1", "localhost", "::1")
SERVER_EXEC_ENABLED = _env_flag("ELYSIA_ALLOW_SERVER_EXEC", LOCAL_ONLY)
TRUST_PROXY = _env_flag("ELYSIA_TRUST_PROXY", bool(os.environ.get("RENDER")))

SESSION_COOKIE = "elysia_session"
MAX_BODY_BYTES = 2 * 1024 * 1024          # 2 MB (profile photos are the biggest payload)
MAX_CONCURRENT_RUNS = 4

_run_slots = threading.BoundedSemaphore(MAX_CONCURRENT_RUNS)
_exec_limiter = auth._RateLimiter()
EXEC_LIMIT_PER_MINUTE = 60


def _safe_int(value, low, high, default):
    try:
        return max(low, min(high, int(value)))
    except (TypeError, ValueError):
        return default


def load_curriculum_tree():
    try:
        json_path = BASE_DIR / "data" / "curriculum_tree.json"
        if json_path.exists():
            with open(json_path, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception as e:
        print("Curriculum json load warning:", e)
    return get_all_curriculum_chapters()


PYTHON_CURRICULUM_TREE_BACKEND = load_curriculum_tree()
_CURRICULUM_TREE_BYTES = json.dumps(PYTHON_CURRICULUM_TREE_BACKEND).encode("utf-8")
_PARTS_REGISTRY_BYTES = json.dumps(PARTS_REGISTRY).encode("utf-8")
_CURRICULUM_DATA_BYTES = json.dumps(CURRICULUM_DATA).encode("utf-8")

_ai_limiter = auth._RateLimiter()
AI_LIMIT_PER_MINUTE = 20
BLOCKED_BOT_TOKENS = ("sqlmap", "nikto", "masscan", "wpscan", "acunetix", "dirbuster", "nmap", "gobuster")


class ThreadedServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    """One thread per request, so one slow request cannot freeze the whole site."""
    daemon_threads = True
    allow_reuse_address = True
    request_queue_size = 64


class ElysiaHandler(http.server.SimpleHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(WEB_DIR), **kwargs)

    # ------------------------------------------------------------- helpers
    def _is_suspicious_bot(self):
        ua = self.headers.get("User-Agent", "").lower()
        return any(b in ua for b in BLOCKED_BOT_TOKENS)

    def send_error(self, code, message=None, explain=None):
        if code == 404:
            parsed = urllib.parse.urlparse(self.path)
            if parsed.path.startswith("/api/"):
                return self._send_json({"error": "Endpoint not found"}, 404)
            page_404 = WEB_DIR / "404.html"
            if page_404.exists():
                try:
                    content = page_404.read_bytes()
                    self.send_response(404)
                    self.send_header("Content-Type", "text/html; charset=utf-8")
                    self.send_header("Content-Length", str(len(content)))
                    self.send_header("Cache-Control", "no-cache")
                    self.end_headers()
                    self.wfile.write(content)
                    return
                except Exception as exc:
                    logger.warning("Failed to serve custom 404 page: %s", exc)
        super().send_error(code, message=message, explain=explain)

    def end_headers(self):
        # Added to EVERY response (API and static files)
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "SAMEORIGIN")
        self.send_header("Referrer-Policy", "same-origin")
        self.send_header("Permissions-Policy", "geolocation=(), camera=(), microphone=()")
        if self._is_https():
            self.send_header("Strict-Transport-Security", "max-age=31536000; includeSubDomains")
        parsed = urllib.parse.urlparse(self.path)
        if not parsed.path.startswith("/api/"):
            ext = os.path.splitext(parsed.path)[1].lower()
            if ext in (".css", ".js", ".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg", ".wasm", ".woff2", ".ico"):
                self.send_header("Cache-Control", "public, max-age=86400, stale-while-revalidate=604800")
        super().end_headers()

    def list_directory(self, path):
        self.send_error(404, "Not found")          # never show folder listings
        return None

    def _should_redirect_to_https(self):
        if not TRUST_PROXY:
            return False
        return self.headers.get("X-Forwarded-Proto", "").lower() == "http"

    def _redirect_to_https(self):
        host = self.headers.get("Host", "")
        if not host:
            return False
        self.send_response(301)
        self.send_header("Location", "https://%s%s" % (host, self.path))
        self.send_header("Connection", "close")
        self.end_headers()
        return True

    def _client_ip(self):
        if TRUST_PROXY:
            forwarded = self.headers.get("X-Forwarded-For", "")
            if forwarded:
                return forwarded.split(",")[-1].strip()    # last hop = added by OUR proxy
        return self.client_address[0]

    def _is_https(self):
        return self.headers.get("X-Forwarded-Proto", "").lower() == "https" if TRUST_PROXY else False

    def _session_token(self):
        raw = self.headers.get("Cookie", "")
        if not raw:
            return ""
        try:
            jar = http.cookies.SimpleCookie()
            jar.load(raw)
            return jar[SESSION_COOKIE].value if SESSION_COOKIE in jar else ""
        except Exception:
            return ""

    def _current_user(self):
        return auth.user_for_token(self._session_token())

    def _cookie_header(self, token, max_age):
        parts = ["%s=%s" % (SESSION_COOKIE, token), "Path=/", "HttpOnly", "SameSite=Lax",
                 "Max-Age=%d" % max_age]
        if self._is_https():
            parts.append("Secure")
        return "; ".join(parts)

    def _send_precomputed_json(self, body_bytes, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body_bytes)))
        self.send_header("Cache-Control", "public, max-age=300")
        self.end_headers()
        self.wfile.write(body_bytes)

    def _send_json(self, data, status=200, cookie=None):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        if cookie:
            self.send_header("Set-Cookie", cookie)
        self.end_headers()
        self.wfile.write(body)

    def _send_html(self, html_str, status=200):
        body = html_str.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _read_json_body(self):
        """Return (dict, error_response_sent). Enforces JSON, size and same-origin."""
        origin = self.headers.get("Origin")
        if origin:
            host = urllib.parse.urlparse(origin).netloc
            if host != self.headers.get("Host", ""):
                self._send_json({"success": False, "error": "Cross-site request blocked."}, 403)
                return None
        ctype = (self.headers.get("Content-Type") or "").split(";")[0].strip().lower()
        if ctype != "application/json":
            self._send_json({"success": False, "error": "Content-Type must be application/json."}, 415)
            return None
        try:
            length = int(self.headers.get("Content-Length", 0))
        except ValueError:
            length = -1
        if length < 0 or length > MAX_BODY_BYTES:
            self._send_json({"success": False, "error": "Request too large."}, 413)
            return None
        raw = self.rfile.read(length) if length else b"{}"
        try:
            body = json.loads(raw.decode("utf-8"))
        except Exception:
            body = {}
        return body if isinstance(body, dict) else {}

    # ------------------------------------------------------------- GET
    def _serve_static_file(self, is_head=False):
        parsed = urllib.parse.urlparse(self.path)
        clean_path = parsed.path.lstrip("/")
        if not clean_path or clean_path.endswith("/"):
            clean_path = (clean_path + "index.html").lstrip("/")

        try:
            target_path = (WEB_DIR / clean_path).resolve()
            if not str(target_path).startswith(str(WEB_DIR.resolve())):
                self.send_error(404, "Not found")
                return True
        except Exception:
            self.send_error(404, "Not found")
            return True

        if not target_path.is_file():
            return False

        accept_encoding = self.headers.get("Accept-Encoding", "").lower()
        supports_gzip = "gzip" in accept_encoding
        ext = target_path.suffix.lower()

        compressible_exts = {".js", ".css", ".json", ".html", ".svg", ".txt"}
        if supports_gzip and ext in compressible_exts:
            gz_path = target_path.with_name(target_path.name + ".gz")
            if gz_path.is_file() and gz_path.stat().st_mtime >= target_path.stat().st_mtime:
                content_len = gz_path.stat().st_size
                content = None if is_head else gz_path.read_bytes()
            else:
                raw_bytes = target_path.read_bytes()
                if len(raw_bytes) > 256:
                    gzipped = gzip.compress(raw_bytes, compresslevel=6)
                    content_len = len(gzipped)
                    content = None if is_head else gzipped
                else:
                    content_len = len(raw_bytes)
                    content = None if is_head else raw_bytes
                    supports_gzip = False

            mime_type, _ = mimetypes.guess_type(str(target_path))
            if not mime_type:
                mime_type = "application/octet-stream"
            if mime_type.startswith("text/") or mime_type in ("application/javascript", "application/json"):
                mime_type += "; charset=utf-8"

            self.send_response(200)
            self.send_header("Content-Type", mime_type)
            if supports_gzip:
                self.send_header("Content-Encoding", "gzip")
                self.send_header("Vary", "Accept-Encoding")
            self.send_header("Content-Length", str(content_len))
            self.end_headers()
            if not is_head and content:
                self.wfile.write(content)
            return True

        return False

    def do_HEAD(self):
        try:
            if self._should_redirect_to_https():
                return self._redirect_to_https()
            if self._is_suspicious_bot():
                return self._send_json({"error": "Automated security scanning blocked."}, 403)
            if self._serve_static_file(is_head=True):
                return
            return super().do_HEAD()
        except (BrokenPipeError, ConnectionResetError):
            return
        except Exception as exc:
            logger.warning("HEAD error: %s", exc)

    def do_GET(self):
        try:
            if self._should_redirect_to_https():
                return self._redirect_to_https()
            if self._is_suspicious_bot():
                return self._send_json({"error": "Automated security scanning blocked."}, 403)
            if self._handle_get_api():
                return
            if self._serve_static_file():
                return
            return super().do_GET()
        except (BrokenPipeError, ConnectionResetError):
            return
        except Exception as exc:                       # never leak a traceback to the browser
            print("GET error:", repr(exc))
            self._send_json({"error": "Server error"}, 500)

    def _handle_get_api(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        query = urllib.parse.parse_qs(parsed.query)

        if path in ("/api/health", "/healthz"):
            return self._send_json({"status": "ok", "app": "elysiacode", "version": "1.0.0"}) or True

        if path == "/api/config":
            return self._send_json({"server_exec": SERVER_EXEC_ENABLED}) or True

        if path == "/api/auth/me":
            user = self._current_user()
            return self._send_json({"success": bool(user), "user": user}) or True

        # ---------------------------------------------------------------------
        # 1. CURRICULUM API: Python aur HTML/CSS ke core topics deta hai
        # ---------------------------------------------------------------------
        if path == "/api/curriculum":
            subject = query.get("subject", ["all"])[0]
            if subject in CURRICULUM_DATA:
                return self._send_json(CURRICULUM_DATA[subject]) or True
            return self._send_precomputed_json(_CURRICULUM_DATA_BYTES) or True

        elif path == "/api/curriculum-tree":
            return self._send_precomputed_json(_CURRICULUM_TREE_BYTES) or True

        elif path == "/api/curriculum-parts":
            return self._send_precomputed_json(_PARTS_REGISTRY_BYTES) or True

        elif path == "/api/ai/status":
            return self._send_json(ai_tutor.get_status()) or True

        # ---------------------------------------------------------------------
        # 2. QUESTIONS API: Dynamic Question Bank ke custom sets generate karta hai
        # ---------------------------------------------------------------------
        elif path == "/api/questions":
            subj = query.get("subject", ["python"])[0]
            topic = query.get("topic", ["all"])[0]
            diff = query.get("difficulty", ["all"])[0]
            count = _safe_int(query.get("count", [5])[0], 1, 50, 5)
            questions = get_questions(subj, topic, diff, count)
            return self._send_json({"questions": questions, "count": len(questions)}) or True

        # ---------------------------------------------------------------------
        # 3. MOCK EXAM API: College practical CA1/CA2 exam format return karta hai
        # ---------------------------------------------------------------------
        elif path == "/api/mock-exam":
            exam_id = query.get("id", ["python_ca1"])[0]
            return self._send_json(get_mock_exam(exam_id)) or True

        # ---------------------------------------------------------------------
        # 4. HANDBOOK (E-BOOK) API: Visual Handbook ke saare slides aur notes deta hai
        # ---------------------------------------------------------------------
        elif path == "/api/handbook":
            ch_id = query.get("chapter", ["all"])[0]
            if ch_id == "all":
                return self._send_json({"chapters": get_all_chapters()}) or True
            return self._send_json(get_chapter(ch_id)) or True

        # ---------------------------------------------------------------------
        # 5. HANDBOOK SEARCH API: E-book ke andar keyword search karta hai
        # ---------------------------------------------------------------------
        elif path == "/api/handbook-search":
            q_term = query.get("q", [""])[0].strip().lower()
            results = []
            for ch in HANDBOOK_CHAPTERS:
                for slide in ch["slides"]:
                    if (q_term in slide["title"].lower() or 
                        q_term in slide["concept"].lower() or 
                        q_term in slide.get("analogy_en", "").lower() or
                        q_term in slide.get("analogy_hi", "").lower() or
                        any(q_term in n.lower() for n in slide.get("notes_en", []))):
                        results.append({
                            "chapter_id": ch["id"],
                            "chapter_title": ch["title"],
                            "slide": slide
                        })
            return self._send_json({"query": q_term, "results": results}) or True

        # ---------------------------------------------------------------------
        # 6. INSTANT DOUBT SEARCH API: 60-Second doubt buster search
        # ---------------------------------------------------------------------
        elif path == "/api/search":
            q_term = query.get("q", [""])[0].strip().lower()
            lang = query.get("lang", ["hi"])[0]
            results = []
            
            # 1. Search in 19 Subtopics Curriculum Tree
            for ch in PYTHON_CURRICULUM_TREE_BACKEND:
                for sub in ch.get("subtopics", []):
                    title_en = sub.get("title", "").lower()
                    title_hi = sub.get("title_hi", "").lower()
                    what_en = sub.get("what_is_it_en", "").lower()
                    what_hi = sub.get("what_is_it_hi", "").lower()
                    syntax = sub.get("syntax", "").lower()
                    rules = " ".join(sub.get("rules_en", []) + sub.get("rules_hi", [])).lower()
                    
                    if (q_term in title_en or q_term in title_hi or 
                        q_term in what_en or q_term in what_hi or 
                        q_term in syntax or q_term in rules):
                        rules_list = sub.get("rules_hi") if lang == "hi" else sub.get("rules_en")
                        first_mistake = rules_list[0] if (rules_list and len(rules_list) > 0) else "Check syntax rules."
                        results.append({
                            "type": "subtopic",
                            "subject": "python",
                            "id": sub.get("id"),
                            "title": sub.get("title_hi") if lang == "hi" else sub.get("title"),
                            "icon": sub.get("icon", "🐍"),
                            "tag": ch.get("title", "Python Core"),
                            "intro": sub.get("what_is_it_hi") if lang == "hi" else sub.get("what_is_it_en"),
                            "mistakes": [{"mistake": sub.get("syntax", ""), "why_it_fails_hi": first_mistake, "why_it_fails_en": first_mistake}],
                            "starter_code": (sub.get("challenge") or {}).get("starter_code", ""),
                            "viva": []
                        })

            # 2. Search in Legacy Curriculum Topics
            for subj_key, subj_data in CURRICULUM_DATA.items():
                for topic in subj_data.get("topics", []):
                    title = topic["title"].lower()
                    intro_en = topic.get("intro_en", "").lower()
                    intro_hi = topic.get("intro_hi", "").lower()
                    
                    if q_term in title or q_term in intro_en or q_term in intro_hi:
                        results.append({
                            "type": "topic",
                            "subject": subj_key,
                            "id": topic["id"],
                            "title": topic["title"],
                            "icon": topic["icon"],
                            "tag": topic["tag"],
                            "intro": topic["intro_hi"] if lang == "hi" else topic["intro_en"],
                            "mistakes": topic.get("common_mistakes", []),
                            "starter_code": topic.get("starter_code", ""),
                            "viva": topic.get("viva_questions", [])
                        })
            
            return self._send_json({"query": q_term, "results": results[:12]}) or True


        return False   # not an API route -> serve static file

    # ------------------------------------------------------------- POST
    def do_POST(self):
        try:
            if self._is_suspicious_bot():
                return self._send_json({"error": "Automated security scanning blocked."}, 403)
            self._handle_post()
        except (BrokenPipeError, ConnectionResetError):
            return
        except Exception as exc:
            print("POST error:", repr(exc))
            self._send_json({"success": False, "error": "Server error"}, 500)

    def _handle_post(self):
        path = urllib.parse.urlparse(self.path).path
        body = self._read_json_body()
        if body is None:
            return                                      # error already sent

        if path == "/api/decode-error":
            raw_err = str(body.get("error", ""))[:5000]
            code = str(body.get("code", ""))[:10000]
            lang = "en" if body.get("lang") == "en" else "hi"
            return self._send_json(decode_error(raw_err, lang, code=code))

        if path in ("/api/ai/tutor", "/api/questions/generate-ai"):
            user = self._current_user()
            if not user:
                return self._send_json({
                    "status": "error",
                    "error": "Authentication required. Please log in to use AI.",
                    "message": "Authentication required. Please log in to use AI."
                }, 401)

            allowed, count = auth.check_and_increment_ai_quota(user["id"], limit=30)
            if not allowed:
                return self._send_json({"status": "rate_limited", "error": "Daily AI limit of 30 requests reached. Please try again tomorrow."}, 429)

            client_ip = self._client_ip()
            if _ai_limiter.blocked("ai:" + client_ip, AI_LIMIT_PER_MINUTE, 60):
                return self._send_json({"status": "rate_limited", "error": "AI request limit exceeded. Please wait a minute."}, 429)
            _ai_limiter.fail("ai:" + client_ip, 60)

        if path == "/api/ai/tutor":
            query = str(body.get("query", ""))[:2000]
            code = str(body.get("code", ""))[:10000]
            topic = str(body.get("topic", ""))[:200]
            provider = str(body.get("provider", "auto"))[:50]
            res = ai_tutor.ask(query=query, code=code, topic=topic, provider=provider)
            status_code = 200 if res.get("status") in ("success", "unconfigured") else 500
            return self._send_json(res, status_code)

        if path == "/api/questions/generate-ai":
            subj = str(body.get("subject", "python"))[:50]
            topic = str(body.get("topic", "all"))[:100]
            diff = str(body.get("difficulty", "Intermediate"))[:50]
            prompt = str(body.get("prompt", ""))[:500]
            res = ai_tutor.generate_question(subject=subj, topic=topic, difficulty=diff, prompt_hint=prompt)
            return self._send_json(res)

        if path == "/api/generate-lab-sheet":
            html = generate_lab_record_html(
                student_name=body.get("student_name", "Student Name"),
                roll_no=body.get("roll_no", "12200001"),
                course_code=body.get("course_code", "CSE205 / INT108"),
                exp_no=_safe_int(body.get("exp_no", 1), 1, 999, 1),
                title=body.get("title", "Python Lab Practical"),
                aim=body.get("aim", "Demonstrate problem solving via Python programming."),
                algorithm=body.get("algorithm", ["Start the program.", "Initialize input values.",
                                                 "Perform calculation.", "Print the output."]),
                code=body.get("code", "# Python program source code"),
                sample_output=body.get("sample_output", "Success"),
                viva_qa=body.get("viva_qa", []))
            return self._send_html(html)

        # ---------------- accounts
        if path == "/api/auth/register":
            ident = body.get("username") or body.get("identifier") or body.get("email") or ""
            hp_val = body.get("hp") or body.get("website_hp") or body.get("school_verify_blank") or ""
            res = register_user(
                name=body.get("name", ""), identifier=ident, password=body.get("password", ""),
                avatar=body.get("avatar", "\U0001F40D"), motto=body.get("motto", ""),
                username=body.get("username", ident), email=body.get("email", ""),
                xp=body.get("xp", 0), streak=body.get("streak", 1),
                completed_subtopics=body.get("completed_subtopics", []),
                today_seconds=body.get("today_seconds", 0), client_ip=self._client_ip(),
                hp=hp_val)
            cookie = None
            if res["success"]:
                token = auth.create_session(res["user"]["id"])
                cookie = self._cookie_header(token, auth.SESSION_DAYS * 86400)
            return self._send_json(res, 200 if res["success"] else 400, cookie=cookie)

        if path == "/api/auth/login":
            ident = body.get("identifier") or body.get("username") or body.get("email") or ""
            res = login_user(identifier=ident, password=body.get("password", ""),
                             client_ip=self._client_ip())
            cookie = None
            if res["success"]:
                token = auth.create_session(res["user"]["id"])
                cookie = self._cookie_header(token, auth.SESSION_DAYS * 86400)
            status = 200 if res["success"] else (429 if res.get("rate_limited") else 400)
            return self._send_json(res, status, cookie=cookie)

        if path == "/api/auth/logout":
            auth.delete_session(self._session_token())
            return self._send_json({"success": True}, cookie=self._cookie_header("", 0))

        if path in ("/api/auth/update-profile", "/api/auth/sync-progress"):
            user = self._current_user()                 # identity comes from the cookie ONLY
            if not user:
                return self._send_json({"success": False, "login_required": True,
                                        "error": "Please log in again."}, 401)
            if path == "/api/auth/update-profile":
                res = update_profile(identifier=user["username"], name=body.get("name"),
                                     avatar=body.get("avatar"), motto=body.get("motto"))
                return self._send_json(res, 200 if res["success"] else 400)
            res = sync_user_progress(
                identifier=user["username"], xp=body.get("xp", 0), streak=body.get("streak", 1),
                completed=body.get("completed_subtopics", []),
                today_sec=body.get("today_seconds", 0), total_sec=body.get("total_seconds", 0))
            return self._send_json(res)

        # ---------------- optional server-side code execution
        if path == "/api/execute":
            if not SERVER_EXEC_ENABLED:
                return self._send_json({"status": "disabled",
                                        "stderr": "Server-side execution is disabled. Code runs in your browser."}, 403)
            ip = self._client_ip()
            if _exec_limiter.blocked("run:" + ip, EXEC_LIMIT_PER_MINUTE, 60):
                return self._send_json({"status": "error", "stdout": "", "exit_code": 1,
                                        "stderr": "Too many runs. Please wait a minute."}, 429)
            _exec_limiter.fail("run:" + ip, 60)         # counts every run

            stdin_data = body.get("stdin", "")
            if isinstance(stdin_data, list):
                stdin_str = "\n".join(str(s) for s in stdin_data[:200]) + "\n"
            else:
                stdin_str = str(stdin_data)
                if stdin_str and not stdin_str.endswith("\n"):
                    stdin_str += "\n"
            code = str(body.get("code", ""))
            if "input(" in code and not stdin_str:
                stdin_str = "\n\n\n\n\n"                # same behaviour as before: blank answers

            if not _run_slots.acquire(blocking=False):
                return self._send_json({"status": "error", "stdout": "", "exit_code": 1,
                                        "stderr": "Server is busy running other programs. Try again in a moment."}, 503)
            try:
                result = run_python(code, stdin_str, timeout=body.get("timeout", 3.0))
            finally:
                _run_slots.release()
            return self._send_json(result)

        self.send_error(404, "Endpoint not found")


def run():
    port = PORT
    httpd = None
    for p in range(port, port + 10):                   # port busy? try the next ones
        try:
            httpd = ThreadedServer((HOST, p), ElysiaHandler)
            port = p
            break
        except OSError:
            continue

    if not httpd:
        print("Could not bind to any port in range %d-%d" % (PORT, PORT + 10))
        return

    shown = "localhost" if LOCAL_ONLY else HOST
    print("==================================================")
    print("ElysiaCode server running on %s:%d" % (HOST, port))
    print("Open: http://%s:%d" % (shown, port))
    print("Server-side code execution:", "ON (local use)" if SERVER_EXEC_ENABLED else "OFF (browser Pyodide)")
    print("==================================================")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
        httpd.shutdown()


if __name__ == "__main__":
    run()
