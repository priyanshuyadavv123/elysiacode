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
