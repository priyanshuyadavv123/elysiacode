# Elysia Code — Changelog & Remediation Log

## Security & Quality Remediation (Comprehensive 8-Phase Update)

### Step 0: Prerequisite Security Gate
- Removed raw `exec()` call on model output in `core/ai_tutor.py`.
- Removed dangerous GET route for `/api/questions/generate-ai` from `main.py`.
- Created `tests/test_ai_safety.py` enforcing AST quarantine of `exec()` and `eval()` strictly to `core/limited_runner.py`.
- Verified 69 unit tests passing.

### Phase 1: Secrets and Deployment
- Added `.dockerignore` excluding `.env`, `.env.*`, `data/*.db*`, `data/users.json*`, `tests/`, `*.bak`, `__pycache__/`, `.git/`, `*.png`, `*.pptx`, `*.zip`.
- Removed deprecated `SESSION_SECRET` variable from `.env.example`.
- Added unit test `test_gitignore_and_dockerignore_exclude_secrets` to `tests/test_security.py`.

### Phase 2: Verify AI Answers in the Browser
- Implemented client-side Pyodide Web Worker validation for AI question cards (`output_verified === false`).
- Added real-time badge updates: "✔ Verified in your browser" vs "⚠️ AI answer differs - trust your own run" (displaying the student's actual output).
- Enforced worker-side execution timeout with zero server round-trips.
- Added automated Chrome DevTools Protocol test (`tools/test_browser_ai_verify.js`) validating matching and mismatched AI questions.

### Phase 3: Access Control and Daily Quota for AI Routes
- Gated `POST /api/questions/generate-ai` and `POST /api/ai/tutor` behind active session authentication (`auth.user_for_token`). Anonymous requests return HTTP 401.
- Created `ai_usage` table in SQLite schema (`core/db.py`), `data/schema_mysql.sql`, and PostgreSQL schema.
- Implemented atomic per-user daily quota of 30 AI calls, returning HTTP 429 when exceeded while retaining per-IP rate limiting.
- Updated frontend UI to show "Log in to generate AI questions" for unauthenticated guests.
- Added unit tests for 401 anonymous block, 200 authenticated call, and 429 quota exhaustion.

### Phase 4: Frontend Bugs and Curriculum Examples
- Replaced inline `onclick` handler in `renderMockExam()` with `data-*` attributes and a delegated listener, eliminating SyntaxErrors when explanations contain single quotes/apostrophes (e.g. `'b = a'` in `python_ca1`).
- Escaped MCQ question code and option text so HTML tags (e.g. `<div class='nav'>` in `html_ca1`) render cleanly as literal text.
- Updated `_escapeHtml()` to escape single quotes (`&#39;`).
- Made curriculum examples 100% deterministic:
  - `ch11_sub1`: sorted set output representation.
  - `ch1_sub3` & `ch1_sub6`: removed OS, Python version, and path-dependent outputs.
  - `ch21_sub4` & `ch22_sub2`: removed non-deterministic float timing values.
  - `ch25`: tagged Tkinter GUI examples as `desktop_only` with clear explanatory notices.
- Built `tools/verify_curriculum_outputs.py` running all 140 subtopics (418 passed / 2 skipped / 0 failed).
- Added automated CDP test `tools/test_browser_mock_exam.js`.

### Phase 5: Auth and Rate Limiting
- Keyed failed login tracking on dual-layer `(username, client_ip)` (`LOGIN_LIMIT_PER_USER_IP = 5`) with a higher global threshold across all IPs combined (`LOGIN_LIMIT_PER_USER_GLOBAL = 25`), completely preventing cross-IP DoS lockout attacks.
- Replaced catastrophic 50,000-key cache wipes in `_RateLimiter` with an LRU `OrderedDict` oldest-key eviction mechanism.
- Added unit tests verifying legitimate users on IP A cannot be locked out by attackers on IP B, and that active entries survive cache eviction.

### Phase 6: Code Hygiene and Tooling
- Created `core/config.py` as the centralized single source of truth for `.env` loading, removing duplicate loaders in `main.py` and `core/ai_tutor.py`.
- Replaced all unlogged `except Exception: pass` blocks across `core/` and `main.py` with structured `logger.warning` entries.
- Upgraded MySQL adapter in `core/db.py` with an intelligent state-machine query translator that preserves `?` in string literals and comments, and escapes `%` wildcards to `%%` when query parameters are supplied.
- Verified `sys.stdout` is never reassigned globally.
- Relocated 6 standalone generation and maintenance scripts to `tools/` with comprehensive documentation in `tools/README.md`.

### Phase 7: Mobile Layout and Load Time
- Sanitized responsive layouts at 390x844 (mobile) and 768x1024 (tablet), achieving zero page-level horizontal scroll (`hasHorizontalScroll: false`) and zero overflowing elements (`pageOverflows: []`).
- Restructured mobile header with collapsible preferences drawer (`#mobile-prefs-collapse`) toggled via `⚙️ Options ▾`, housing language toggles (`Hinglish`/`English`), track toggles (`Python 3`/`HTML5`), and sound FX.
- Expanded search bar to full width on mobile (370px) and tablet (748px), completely eliminating placeholder text truncation.
- Resized floating Senior AI Tutor FAB to a compact 46x46px glowing circular icon docked to the bottom-right corner respecting `safe-area-inset`, eliminating overlap with cards and CTAs.
- Added static gzip compression to `main.py` (`_serve_static_file` & `do_HEAD`), delivering pre-compressed [`web/js/curriculum_tree.js.gz`](file:///Users/priyanshuyadav/.gemini/antigravity/scratch/elysia-code/web/js/curriculum_tree.js.gz) (395 KB vs 1.5 MB uncompressed, 74% data reduction).
- Automated Fast 3G first-render benchmark via CDP (`tools/measure_mobile_phase7.js`): FCP improved to **1,080 ms**; DOM content loaded improved by **~10 seconds**.
- Saved before and after comparison screenshots to `docs/screenshots/`.

---

# Elysia Code - Security & Stability Update (Step 1)

## Problems found in the original code (all reproduced before fixing)
| # | Problem | Impact |
|---|---|---|
| 1 | `/api/execute` ran any Python on the server with no sandbox, and the browser tried the server FIRST | Anyone could read `data/users.json` (all password hashes), delete files, use your server |
| 2 | `update-profile` / `sync-progress` trusted a username typed in the request | Anyone could rename any user or give them 99,999,999 XP, no password needed |
| 3 | Server was single-threaded (`TCPServer`, not threaded) although the deck said "threaded" | 3 parallel 2-second jobs took 6.1 s; one infinite loop froze the site for everybody |
| 4 | Fake "fallback Python": regex-parsed `print()` and returned hard-coded numbers (320, 82, 207.5 ...) | When Pyodide failed to load, students saw WRONG output that did not come from their code |
| 5 | Pyodide ran on the main thread, with variables kept between runs | `while True:` would freeze the tab; old variables hid NameError bugs |
| 6 | SHA-256 + salt, JSON file as database | Passwords crackable fast; data race / corruption; lost on every Render redeploy |
| 7 | Lab sheet HTML built from unescaped input, written into a same-origin window | HTML/script injection (e.g. via pasted code) |
| 8 | `Access-Control-Allow-Origin: *`, no body-size limit, `int()` on raw input | CSRF-style abuse, memory DoS, crashes on bad input |
| 9 | Tests wrote into the real `data/users.json` and failed on the 2nd run | "9/9 tests pass" was only true once |
| 10 | Sync wiped `total_seconds` to 0 (client never sent it) | All-time study time reset on every sync |

## What changed
**New:** `core/db.py` (SQLite + one-time import of old users.json), `core/limited_runner.py` (hardened runner),
`web/js/pyodide_worker.js` (Python in a Web Worker), `tests/_env.py`, `tests/test_security.py` (37 tests), `.gitignore`.

**Rewritten:** `core/auth.py` (scrypt, sessions, rate limit, validation), `main.py` (threaded, cookies, gating, limits),
`web/js/pyodide_runner.js` (worker manager: timeout kills infinite loops, honest errors, no fake output).

**Edited:** `core/lab_exporter.py` (escape everything), `web/js/app.js` (one `runPythonCode()` helper, session handling,
8-char password rule), `web/index.html`, `render.yaml`, `README.md`, `tests/test_core.py`.

## Behaviour you will notice
* Running locally (`python3 main.py`): server runs code (fast), site reachable only from your own computer.
* Deployed (`HOST=0.0.0.0`): code runs in the visitor's browser. Server execution returns 403 unless you force it on.
* After this update every logged-in user must **log in once again** (new session cookie). Old accounts and their XP/streak are kept.
* New passwords need 8+ characters. Old short passwords still work.
* Too many wrong passwords (5 in 5 minutes) locks that username for 5 minutes.

## You still must do (I could not test these)
1. **Browser test of the Pyodide worker** (my sandbox has no internet, so I tested the page-side logic with a fake worker only).
   Run `ELYSIA_ALLOW_SERVER_EXEC=0 python3 main.py` and check in Chrome:
   - `print("hi")` works; first run shows "Loading Python engine".
   - `while True: pass` -> after ~4 s you get the "Infinite loop detected" message and the page stays responsive.
   - `name = input("x")` using the input bar; a syntax error; a NameError (decoder hint appears).
   - Run `x = 5` then run `print(x)` -> must now give NameError (fresh namespace each run).
   - Turn off Wi-Fi before first load -> clear "could not be loaded" message (no fake output).
2. **Deploy:** push, redeploy, then open `/api/config` on your live URL: it must show `{"server_exec": false}`.
3. **Persistence:** on Render's free plan the disk is wiped on every deploy/restart. Attach a persistent disk and set
   `ELYSIA_DATA_DIR` (see `render.yaml`) or use a real hosted database before real users arrive.
4. **If the site was already public with the old code:** treat existing passwords as exposed (the old runner could read
   the hash file). Ask users to change passwords, and do not reuse any secret that lived on that server.
5. Remove `data/users.json` from anything you share or commit (it is now in `.gitignore`).

## Known limits (honest list)
* `limited_runner` is hardening, not a true sandbox. Never enable server execution on a public site without containers.
* XP/streak are reported by the browser, so they can be faked. Do not use them for leaderboards or certificates yet.
* No Content-Security-Policy yet (the app uses inline scripts/handlers); that needs a front-end refactor.
* In-memory rate limits reset on restart and are per-process.
* Lab sheet "Sample Output" still comes from the form, not from a real run.
