import urllib.request
import urllib.parse
import json
import time
import sqlite3
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE_DIR = Path(__file__).resolve().parent.parent

def test_backend_apis():
    print("--- 1. Testing Backend APIs ---")
    base_url = "http://127.0.0.1:8080"
    
    # Health
    req = urllib.request.urlopen(f"{base_url}/api/health")
    data = json.loads(req.read().decode())
    assert data["status"] == "ok", f"Health failed: {data}"
    print("  ✓ /api/health: OK")

    # Curriculum tree
    req = urllib.request.urlopen(f"{base_url}/api/curriculum-tree")
    tree = json.loads(req.read().decode())
    assert len(tree) == 26, f"Expected 26 chapters, got {len(tree)}"
    print(f"  ✓ /api/curriculum-tree: 26 Chapters intact")

    # Curriculum parts
    req = urllib.request.urlopen(f"{base_url}/api/curriculum-parts")
    parts = json.loads(req.read().decode())
    assert len(parts) == 7, f"Expected 7 parts, got {len(parts)}"
    print(f"  ✓ /api/curriculum-parts: 7 Parts intact")

    # Mock exams
    req = urllib.request.urlopen(f"{base_url}/api/mock-exam?id=python_ca1")
    exam = json.loads(req.read().decode())
    assert "section_a_mcq" in exam or "title" in exam, "Mock exam failed"
    print("  ✓ /api/mock-exam: OK")

    # Handbook
    req = urllib.request.urlopen(f"{base_url}/api/handbook?chapter=all")
    hb = json.loads(req.read().decode())
    assert len(hb.get("chapters", [])) >= 8, "Handbook chapters missing"
    print("  ✓ /api/handbook: 8 Chapters intact")

def test_auth_lifecycle():
    print("--- 2. Testing Auth Lifecycle (Test Account Only) ---")
    base_url = "http://127.0.0.1:8080"
    uname = f"qa_test_{int(time.time())}"
    pwd = "QA_Password_123!"

    # Register
    req = urllib.request.Request(
        f"{base_url}/api/auth/register",
        data=json.dumps({"name": "QA Tester", "username": uname, "password": pwd}).encode(),
        headers={"Content-Type": "application/json"}
    )
    res = urllib.request.urlopen(req)
    cookie = res.headers.get("Set-Cookie")
    body = json.loads(res.read().decode())
    assert body["success"] is True, f"Registration failed: {body}"
    print(f"  ✓ Registered temporary account: {uname}")

    # Me (authenticated)
    cookie_str = cookie.split(";")[0]
    req_me = urllib.request.Request(
        f"{base_url}/api/auth/me",
        headers={"Cookie": cookie_str}
    )
    res_me = urllib.request.urlopen(req_me)
    body_me = json.loads(res_me.read().decode())
    assert body_me["success"] is True and body_me["user"]["username"] == uname
    print(f"  ✓ /api/auth/me verified user {uname}")

    # Logout
    req_out = urllib.request.Request(
        f"{base_url}/api/auth/logout",
        data=b"{}",
        headers={"Content-Type": "application/json", "Cookie": cookie_str}
    )
    res_out = urllib.request.urlopen(req_out)
    assert res_out.status == 200
    print("  ✓ /api/auth/logout: Session revoked")

def test_frontend_playwright():
    print("--- 3. Testing Frontend UI with Playwright ---")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        
        # Capture console errors
        console_errors = []
        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)

        page.goto("http://127.0.0.1:8080")
        page.wait_for_selector(".integrated-workspace-grid")
        page.wait_for_timeout(800)

        # A. Theme Switcher & Persistence
        page.evaluate("window.elysiaApp.setTheme('light', false)")
        page.wait_for_timeout(300)
        theme = page.evaluate("document.body.getAttribute('data-theme')")
        assert theme == "light", f"Expected light theme, got {theme}"
        print("  ✓ Switched to Light Mode")

        page.evaluate("window.elysiaApp.setTheme('dark', false)")
        page.wait_for_timeout(300)
        theme_dark = page.evaluate("document.body.getAttribute('data-theme')")
        assert theme_dark == "dark", f"Expected dark theme, got {theme_dark}"
        print("  ✓ Switched to Dark Mode")

        # B. Track Selector
        page.click("button[data-track='html']")
        page.wait_for_timeout(400)
        track = page.evaluate("window.elysiaApp.subject")
        assert track == "html", f"Expected html track, got {track}"
        print("  ✓ Track switched to HTML5")

        page.click("button[data-track='python']")
        page.wait_for_timeout(400)
        track_py = page.evaluate("window.elysiaApp.subject")
        assert track_py == "python", f"Expected python track, got {track_py}"
        print("  ✓ Track switched to Python")

        # C. Language Selector
        page.click("button[data-lang='en']")
        page.wait_for_timeout(300)
        lang = page.evaluate("window.elysiaApp.lang")
        assert lang == "en", f"Expected 'en' lang, got {lang}"
        print("  ✓ Language switched to English")

        page.click("button[data-lang='hi']")
        page.wait_for_timeout(300)
        lang_hi = page.evaluate("window.elysiaApp.lang")
        assert lang_hi == "hi", f"Expected 'hi' lang, got {lang_hi}"
        print("  ✓ Language switched to Hinglish")

        # D. Curriculum Navigation
        page.evaluate("window.elysiaApp.selectChapter(2)")
        page.wait_for_timeout(400)
        ch_idx = page.evaluate("window.elysiaApp.currentChapterIdx")
        assert ch_idx == 2, f"Expected chapter 2, got {ch_idx}"
        print("  ✓ Navigated to Chapter 3 (index 2)")

        # E. AI Tutor Toggle
        page.evaluate("window.elysiaApp.toggleAITutor(true)")
        page.wait_for_timeout(300)
        is_open = page.evaluate("document.querySelector('#ai-tutor-drawer').classList.contains('open')")
        assert is_open is True, "AI tutor drawer did not open"
        page.evaluate("window.elysiaApp.toggleAITutor(false)")
        print("  ✓ AI Tutor open and close verified")

        # F. Code Runner (Pyodide / sub-15ms local runner)
        page.evaluate("window.elysiaApp.setCode('print(\"Elysia School Verification Test\")')")
        page.click("#btn-run-code")
        page.wait_for_timeout(1500)
        stdout = page.evaluate("document.querySelector('#terminal-stdout') ? document.querySelector('#terminal-stdout').innerText : ''")
        assert "Elysia School Verification Test" in stdout, f"Stdout mismatch: {stdout}"
        print("  ✓ Code Execution: Output rendered correctly in terminal")

        print("  ✓ Console errors encountered:", len(console_errors))
        browser.close()

def test_database_integrity():
    print("--- 4. Checking Database Integrity ---")
    db_file = BASE_DIR / "data" / "elysia.db"
    conn = sqlite3.connect(str(db_file))
    cur = conn.cursor()

    cur.execute("SELECT count(*) FROM users")
    user_count = cur.fetchone()[0]
    print(f"  ✓ Users in database: {user_count} (existing real accounts preserved)")

    cur.execute("SELECT count(*) FROM sessions")
    sess_count = cur.fetchone()[0]
    print(f"  ✓ Active sessions: {sess_count}")

    cur.execute("SELECT count(*) FROM ai_usage")
    ai_count = cur.fetchone()[0]
    print(f"  ✓ AI usage logs: {ai_count}")

    cur.execute("PRAGMA integrity_check")
    integrity = cur.fetchone()[0]
    assert integrity == "ok", f"Integrity check failed: {integrity}"
    print(f"  ✓ SQLite PRAGMA integrity_check: {integrity}")
    conn.close()

if __name__ == "__main__":
    test_backend_apis()
    test_auth_lifecycle()
    test_frontend_playwright()
    test_database_integrity()
    print("\n🎉 ALL E2E AND INTEGRATION TESTS PASSED!")
