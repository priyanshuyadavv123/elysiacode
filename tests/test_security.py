"""
Security & robustness tests for Elysia Code.
Run:  python3 -m unittest discover -s tests -v
"""
import http.client
import json
import os
import sqlite3
import sys
import threading
import time
import unittest
import uuid
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _env  # noqa: F401

from core import auth, db
from core.lab_exporter import generate_lab_record_html
from core.limited_runner import run_python

PNG_1PX = ("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==")


def uname(prefix="u"):
    return "%s_%s" % (prefix, uuid.uuid4().hex[:10])


class TestPasswords(unittest.TestCase):
    def setUp(self):
        auth.reset_rate_limits_for_tests()

    def test_scrypt_format_and_verify(self):
        h = auth._hash_password("correct horse")
        self.assertTrue(h.startswith("scrypt$"))
        self.assertEqual(auth._verify_password("correct horse", h), (True, False))
        self.assertEqual(auth._verify_password("wrong", h), (False, False))
        self.assertNotEqual(auth._hash_password("correct horse"), h)      # random salt each time

    def test_legacy_sha256_user_can_login_and_is_upgraded(self):
        import hashlib
        name = uname("legacy")
        salt = "ab" * 16
        legacy = "%s:%s" % (salt, hashlib.sha256((salt + "oldpassword").encode()).hexdigest())
        with db.connect() as c:
            c.execute("INSERT INTO users (id, username, name, password_hash) VALUES (?,?,?,?)",
                      ("usr_legacy_" + name, name, "Old User", legacy))
        res = auth.login_user(name, "oldpassword")
        self.assertTrue(res["success"])
        with db.connect() as c:
            new_hash = c.execute("SELECT password_hash FROM users WHERE username=?", (name,)).fetchone()[0]
        self.assertTrue(new_hash.startswith("scrypt$"))                    # silently upgraded
        self.assertTrue(auth.login_user(name, "oldpassword")["success"])   # still works afterwards

    def test_registration_validation(self):
        r = auth.register_user(name="A", username=uname(), password="short")
        self.assertFalse(r["success"])
        r = auth.register_user(name="A", username="bad name!", password="longenough1")
        self.assertFalse(r["success"])
        r = auth.register_user(name="", username=uname(), password="longenough1")
        self.assertFalse(r["success"])
        r = auth.register_user(name="x" * 200, username=uname(), password="longenough1")
        self.assertFalse(r["success"])

    def test_duplicate_username_rejected(self):
        name = uname("dup")
        self.assertTrue(auth.register_user(name="A", username=name, password="longenough1")["success"])
        self.assertFalse(auth.register_user(name="B", username=name.upper(), password="longenough1")["success"])

    def test_avatar_rules(self):
        ok = auth.register_user(name="A", username=uname(), password="longenough1", avatar=PNG_1PX)
        self.assertTrue(ok["success"])
        for bad in ("data:image/svg+xml;base64,PHN2Zz48L3N2Zz4=", "data:text/html;base64,PGI+", "<script>alert(1)</script>",
                    "x" * 50, PNG_1PX + "A" * 500_000):
            r = auth.register_user(name="A", username=uname(), password="longenough1", avatar=bad)
            self.assertFalse(r["success"], bad[:30])

    def test_login_rate_limit(self):
        name = uname("rl")
        auth.register_user(name="A", username=name, password="longenough1")
        for _ in range(5):
            self.assertFalse(auth.login_user(name, "nope-nope")["success"])
        blocked = auth.login_user(name, "longenough1")                      # even the CORRECT one
        self.assertFalse(blocked["success"])
        self.assertTrue(blocked.get("rate_limited"))

    def test_progress_is_clamped_and_garbage_safe(self):
        name = uname("sync")
        auth.register_user(name="A", username=name, password="longenough1")
        r = auth.sync_user_progress(name, xp="99999999999999999999", streak="abc", completed=[{"x": 1}, "ok", "y" * 999],
                                    today_sec=-5, total_sec=None)
        self.assertTrue(r["success"])
        self.assertLessEqual(r["user"]["xp"], auth.MAX_XP)
        self.assertEqual(r["user"]["completed_subtopics"], ["ok"])
        self.assertEqual(r["user"]["today_seconds"], 0)

    def test_total_time_never_goes_backwards(self):
        name = uname("t")
        auth.register_user(name="A", username=name, password="longenough1")
        auth.sync_user_progress(name, total_sec=5000)
        r = auth.sync_user_progress(name, total_sec=0)       # old client that forgot to send it
        self.assertEqual(r["user"]["total_seconds"], 5000)


class TestSessions(unittest.TestCase):
    def test_session_lifecycle(self):
        name = uname("s")
        user = auth.register_user(name="A", username=name, password="longenough1")["user"]
        token = auth.create_session(user["id"])
        self.assertEqual(auth.user_for_token(token)["username"], name)
        self.assertIsNone(auth.user_for_token(token + "x"))
        self.assertIsNone(auth.user_for_token(""))
        auth.delete_session(token)
        self.assertIsNone(auth.user_for_token(token))

    def test_token_is_stored_hashed_and_expiry_works(self):
        name = uname("e")
        user = auth.register_user(name="A", username=name, password="longenough1")["user"]
        token = auth.create_session(user["id"])
        with db.connect() as c:
            stored = [r[0] for r in c.execute("SELECT token_hash FROM sessions")]
            self.assertNotIn(token, stored)                                  # raw token never stored
            c.execute("UPDATE sessions SET expires_at = 1")
        self.assertIsNone(auth.user_for_token(token))                        # expired


class TestMigration(unittest.TestCase):
    def test_import_from_old_users_json_once(self):
        import tempfile
        old_env, old_init = os.environ["ELYSIA_DATA_DIR"], set(db._initialised)
        tmp = tempfile.mkdtemp(prefix="elysia_mig_")
        try:
            os.environ["ELYSIA_DATA_DIR"] = tmp
            (Path(tmp) / "users.json").write_text(json.dumps({
                "ravi": {"id": "usr_1", "name": "Ravi", "username": "ravi", "password_hash": "aa:bb",
                         "xp": 120, "streak": 4, "completed_subtopics": ["a", "b"]},
                "broken": "not-a-dict"}))
            with db.connect() as c:
                rows = c.execute("SELECT username, xp, streak FROM users").fetchall()
            self.assertEqual([tuple(r) for r in rows], [("ravi", 120, 4)])
            with db.connect() as c:                                          # delete + reconnect: must not re-import
                c.execute("DELETE FROM users")
            db._initialised.clear()
            with db.connect() as c:
                self.assertEqual(c.execute("SELECT COUNT(*) FROM users").fetchone()[0], 0)
        finally:
            os.environ["ELYSIA_DATA_DIR"] = old_env
            db._initialised.clear(); db._initialised.update(old_init)


class TestLabSheetXSS(unittest.TestCase):
    def test_html_is_escaped(self):
        evil = "<script>alert(1)</script>"
        html = generate_lab_record_html(evil, evil, evil, "not-a-number", evil, evil, [evil, 5], "</pre>" + evil, evil,
                                        [{"q": evil, "a": evil}, "junk", None])
        body = html.split("</style>", 1)[1]
        self.assertNotIn("<script>alert(1)</script>", body)
        self.assertIn("&lt;script&gt;alert(1)&lt;/script&gt;", body)
        self.assertNotIn("</pre><script>", html)


class TestLimitedRunner(unittest.TestCase):
    def test_basic_and_stdin(self):
        self.assertEqual(run_python("print('hi')")["stdout"], "hi\n")
        self.assertEqual(run_python("n=input()\nprint(n*2)", "ab\n")["stdout"], "abab\n")

    def test_traceback_shows_only_student_code(self):
        r = run_python("x = 1\nprint(undefined_name)")
        self.assertIn("NameError", r["stderr"])
        self.assertNotIn("bootstrap", r["stderr"].lower())
        self.assertNotIn("exec(", r["stderr"])

    def test_timeout_kills_infinite_loop(self):
        t = time.time()
        r = run_python("while True: pass", timeout=1)
        self.assertEqual(r["status"], "timeout")
        self.assertLess(time.time() - t, 3)

    def test_output_flood_is_capped(self):
        r = run_python("while True: print('x' * 200)", timeout=5)
        self.assertEqual(r["status"], "output_limit")
        self.assertLessEqual(len(r["stdout"]), 100_000)

    def test_server_secrets_are_not_inherited(self):
        os.environ["ELYSIA_SECRET_FOR_TEST"] = "top-secret"
        try:
            r = run_python("import os\nprint(os.environ.get('ELYSIA_SECRET_FOR_TEST'), os.environ.get('HOME'))")
        finally:
            del os.environ["ELYSIA_SECRET_FOR_TEST"]
        self.assertEqual(r["stdout"].strip(), "None None")

    def test_runs_in_empty_temp_folder_not_project_folder(self):
        r = run_python("import os; print(sorted(os.listdir('.')))")
        self.assertEqual(r["stdout"].strip(), "['main.py']")

    def test_bad_timeout_values_do_not_crash(self):
        for t in ("abc", None, float("nan"), float("inf"), -3, 0):
            self.assertIn(run_python("print(1)", timeout=t)["status"], ("ok", "timeout"))

    def test_memory_bomb_is_stopped(self):
        r = run_python("x = [0] * (10 ** 10)")
        self.assertNotEqual(r["exit_code"], 0)


class TestHttpServer(unittest.TestCase):
    """Starts the real server on a free port and attacks it."""

    @classmethod
    def setUpClass(cls):
        import main
        cls.main = main
        cls.srv = main.ThreadedServer(("127.0.0.1", 0), main.ElysiaHandler)
        cls.port = cls.srv.server_address[1]
        threading.Thread(target=cls.srv.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls):
        cls.srv.shutdown(); cls.srv.server_close()

    def setUp(self):
        auth.reset_rate_limits_for_tests()
        self.main.SERVER_EXEC_ENABLED = True
        self.main._exec_limiter._fails.clear()
        self.main._ai_limiter._fails.clear()

    # --- tiny HTTP client that keeps cookies
    def call(self, method, path, body=None, cookie=None, headers=None, raw_body=None):
        c = http.client.HTTPConnection("127.0.0.1", self.port, timeout=20)
        h = {"Host": "127.0.0.1:%d" % self.port}
        data = None
        if body is not None:
            data = json.dumps(body); h["Content-Type"] = "application/json"
        if raw_body is not None:
            data = raw_body
        if cookie:
            h["Cookie"] = cookie
        h.update(headers or {})
        c.request(method, path, body=data, headers=h)
        r = c.getresponse()
        text = r.read().decode("utf-8", "replace")
        out = {"status": r.status, "headers": {k.lower(): v for k, v in r.getheaders()}, "text": text}
        try:
            out["json"] = json.loads(text)
        except Exception:
            out["json"] = None
        c.close()
        return out

    def signup(self, prefix="h"):
        name = uname(prefix)
        r = self.call("POST", "/api/auth/register", {"name": "N " + name, "username": name, "password": "longenough1"})
        self.assertEqual(r["status"], 200, r["text"])
        cookie = r["headers"]["set-cookie"].split(";")[0]
        return name, cookie, r

    # --- the attacks
    def test_cookie_flags(self):
        _, _, r = self.signup()
        sc = r["headers"]["set-cookie"]
        self.assertIn("HttpOnly", sc); self.assertIn("SameSite=Lax", sc)

    def test_cannot_edit_other_users_without_login(self):
        victim, _, _ = self.signup("victim")
        r = self.call("POST", "/api/auth/update-profile", {"username": victim, "name": "HACKED"})
        self.assertEqual(r["status"], 401)
        r = self.call("POST", "/api/auth/sync-progress", {"username": victim, "xp": 999999})
        self.assertEqual(r["status"], 401)

    def test_logged_in_attacker_cannot_edit_victim_by_naming_them(self):
        victim, vcookie, _ = self.signup("victim")
        attacker, acookie, _ = self.signup("attacker")
        self.call("POST", "/api/auth/update-profile", {"username": victim, "identifier": victim, "name": "HACKED"}, cookie=acookie)
        me = self.call("GET", "/api/auth/me", cookie=vcookie)["json"]["user"]
        self.assertNotEqual(me["name"], "HACKED")
        mine = self.call("GET", "/api/auth/me", cookie=acookie)["json"]["user"]
        self.assertEqual(mine["name"], "HACKED")             # it changed the ATTACKER's own profile only

    def test_profile_update_with_valid_session(self):
        _, cookie, _ = self.signup()
        r = self.call("POST", "/api/auth/update-profile", {"name": "New Name", "motto": "m"}, cookie=cookie)
        self.assertEqual(r["json"]["user"]["name"], "New Name")

    def test_logout_invalidates_session(self):
        _, cookie, _ = self.signup()
        self.assertTrue(self.call("GET", "/api/auth/me", cookie=cookie)["json"]["success"])
        self.call("POST", "/api/auth/logout", {}, cookie=cookie)
        self.assertFalse(self.call("GET", "/api/auth/me", cookie=cookie)["json"]["success"])

    def test_login_sets_cookie_and_wrong_password_does_not(self):
        name, _, _ = self.signup()
        bad = self.call("POST", "/api/auth/login", {"identifier": name, "password": "wrongwrong"})
        self.assertEqual(bad["status"], 400); self.assertNotIn("set-cookie", bad["headers"])
        good = self.call("POST", "/api/auth/login", {"identifier": name, "password": "longenough1"})
        self.assertEqual(good["status"], 200); self.assertIn("elysia_session=", good["headers"]["set-cookie"])
        self.assertNotIn("password", json.dumps(good["json"]["user"]))

    def test_http_login_rate_limit_returns_429(self):
        name, _, _ = self.signup()
        for _ in range(5):
            self.call("POST", "/api/auth/login", {"identifier": name, "password": "wrongwrong"})
        r = self.call("POST", "/api/auth/login", {"identifier": name, "password": "longenough1"})
        self.assertEqual(r["status"], 429)

    def test_csrf_protections(self):
        r = self.call("POST", "/api/decode-error", raw_body="error=x", headers={"Content-Type": "application/x-www-form-urlencoded"})
        self.assertEqual(r["status"], 415)
        r = self.call("POST", "/api/decode-error", {"error": "x"}, headers={"Origin": "https://evil.example"})
        self.assertEqual(r["status"], 403)
        r = self.call("POST", "/api/decode-error", {"error": "x"}, headers={"Origin": "http://127.0.0.1:%d" % self.port})
        self.assertEqual(r["status"], 200)

    def test_oversized_body_rejected(self):
        r = self.call("POST", "/api/decode-error", raw_body="{}", headers={"Content-Type": "application/json", "Content-Length": "99999999"})
        self.assertEqual(r["status"], 413)

    def test_no_wildcard_cors_and_security_headers(self):
        for path in ("/api/config", "/"):
            r = self.call("GET", path)
            self.assertNotIn("access-control-allow-origin", r["headers"], path)
            self.assertEqual(r["headers"].get("x-content-type-options"), "nosniff")
            self.assertEqual(r["headers"].get("x-frame-options"), "SAMEORIGIN")

    def test_static_hardening(self):
        self.assertEqual(self.call("GET", "/js/")["status"], 404)                      # no directory listing
        r = self.call("GET", "/../main.py")
        self.assertNotIn("class ElysiaHandler", r["text"])
        r = self.call("GET", "/%2e%2e/core/auth.py")
        self.assertNotIn("def register_user", r["text"])
        self.assertEqual(self.call("GET", "/")["status"], 200)

    def test_execute_gate(self):
        self.main.SERVER_EXEC_ENABLED = False
        self.assertEqual(self.call("GET", "/api/config")["json"], {"server_exec": False})
        r = self.call("POST", "/api/execute", {"code": "print(1)"})
        self.assertEqual(r["status"], 403); self.assertEqual(r["json"]["status"], "disabled")
        self.main.SERVER_EXEC_ENABLED = True
        r = self.call("POST", "/api/execute", {"code": "print(1)"})
        self.assertEqual(r["json"]["stdout"], "1\n")

    def test_execute_cannot_read_the_database_folder(self):
        r = self.call("POST", "/api/execute", {"code": "import os; print(os.path.exists('elysia.db'), os.path.exists('users.json'))"})
        self.assertEqual(r["json"]["stdout"].strip(), "False False")

    def test_server_is_threaded(self):
        t0 = time.time(); results = []
        def job():
            results.append(self.call("POST", "/api/execute", {"code": "import time; time.sleep(1)"})["status"])
        ths = [threading.Thread(target=job) for _ in range(3)]
        [t.start() for t in ths]; [t.join() for t in ths]
        self.assertEqual(results, [200, 200, 200])
        self.assertLess(time.time() - t0, 2.4)               # sequential would be >= 3 s

    def test_execute_rate_limit(self):
        for _ in range(self.main.EXEC_LIMIT_PER_MINUTE):
            self.main._exec_limiter.fail("run:127.0.0.1", 60)
        r = self.call("POST", "/api/execute", {"code": "print(1)"})
        self.assertEqual(r["status"], 429)

    def test_bad_inputs_do_not_crash_server(self):
        self.assertEqual(self.call("GET", "/api/questions?count=abc")["status"], 200)
        self.assertEqual(self.call("GET", "/api/questions?count=999999")["status"], 200)
        self.assertEqual(self.call("POST", "/api/execute", {"code": "print(1)", "timeout": "nan"})["status"], 200)
        r = self.call("POST", "/api/execute", {"code": 12345, "stdin": {"a": 1}})
        self.assertEqual(r["status"], 200)
        self.assertEqual(self.call("POST", "/api/generate-lab-sheet", {"exp_no": "x", "algorithm": "oops", "viva_qa": 5})["status"], 200)
        self.assertEqual(self.call("GET", "/api/config")["status"], 200)       # still alive

    def test_lab_sheet_over_http_is_escaped(self):
        r = self.call("POST", "/api/generate-lab-sheet", {"student_name": "<script>alert(1)</script>", "code": "</pre><script>x()</script>"})
        self.assertNotIn("<script>alert(1)</script>", r["text"].split("</style>", 1)[1])

    def test_ai_endpoints_require_login(self):
        # Anonymous POST /api/questions/generate-ai returns 401
        r = self.call("POST", "/api/questions/generate-ai", {"subject": "python"})
        self.assertEqual(r["status"], 401)
        self.assertIn("Authentication required", r["json"]["error"])

        # Anonymous POST /api/ai/tutor returns 401
        r2 = self.call("POST", "/api/ai/tutor", {"query": "hello"})
        self.assertEqual(r2["status"], 401)
        self.assertIn("Authentication required", r2["json"]["error"])

    def test_ai_endpoints_quota_and_rate_limit(self):
        from unittest.mock import patch
        name, cookie, _ = self.signup("ai_user")

        mock_q = {
            "status": "success",
            "question": {
                "id": "q_test",
                "title_en": "Test Question",
                "solution_code": "print('ok')",
                "expected_output": "ok\n",
                "output_verified": True
            }
        }
        with patch.object(self.main.ai_tutor, "generate_question", return_value=mock_q):
            # Calls 1 to 30 should succeed
            for i in range(30):
                self.main._ai_limiter._fails.clear()
                r = self.call("POST", "/api/questions/generate-ai", {"subject": "python"}, cookie=cookie)
                self.assertEqual(r["status"], 200, f"Call {i+1} failed with status {r['status']}: {r['text']}")
                self.assertEqual(r["json"]["status"], "success")

            # The 31st call should return 429 daily quota exceeded
            self.main._ai_limiter._fails.clear()
            r31 = self.call("POST", "/api/questions/generate-ai", {"subject": "python"}, cookie=cookie)
            self.assertEqual(r31["status"], 429)
            self.assertIn("Daily AI limit of 30 requests reached", r31["json"]["error"])


class TestSecretsAndDeployment(unittest.TestCase):
    def test_gitignore_and_dockerignore_exclude_secrets(self):
        gitignore = (BASE_DIR / ".gitignore").read_text(encoding="utf-8")
        dockerignore = (BASE_DIR / ".dockerignore").read_text(encoding="utf-8")

        # Both must explicitly exclude .env
        self.assertTrue(
            any(line.strip() == ".env" or line.strip().startswith(".env") for line in gitignore.splitlines()),
            ".gitignore must exclude .env"
        )
        self.assertTrue(
            any(line.strip() == ".env" or line.strip().startswith(".env") for line in dockerignore.splitlines()),
            ".dockerignore must exclude .env"
        )

        # Both must explicitly exclude data/*.db
        self.assertTrue(
            any("data/*.db" in line or "*.db" in line for line in gitignore.splitlines()),
            ".gitignore must exclude data/*.db"
        )
        self.assertTrue(
            any("data/*.db" in line or "*.db" in line for line in dockerignore.splitlines()),
            ".dockerignore must exclude data/*.db"
        )

        # .env.example must not contain SESSION_SECRET
        env_example = (BASE_DIR / ".env.example").read_text(encoding="utf-8")
        self.assertNotIn("SESSION_SECRET", env_example)


if __name__ == "__main__":
    unittest.main()
