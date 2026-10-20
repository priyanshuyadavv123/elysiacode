# ⚡ Elysia Code
### Next-Generation 3D Spatial Bilingual Coding & Lab Mastery Platform

**Elysia Code** is a high-concept interactive coding learning platform designed for college students and beginners who are terrified by programming syntax and university lab evaluations.

Engineered with a **3D Spatial Glassmorphic UI**, **Bilingual (English & Hinglish)** pedagogy, **Client-Side WebAssembly (Pyodide)** execution, and an **Anti-Cheating Socratic Senior Mentor**, Elysia Code eliminates the fear of coding from Day 1.

---

## 🚀 Key Features

1. **3D Spatial Glassmorphic Interface:**
   - Deep obsidian cosmic canvas with ethereal aurora mesh lighting.
   - Interactive 3D tilt cards, floating pill docks, and tactile audio soundscapes.

2. **Side-by-Side Learn & Code:**
   - Left side: Intuitive real-life college analogies, industry use cases, and explicit **🚨 "What NOT to do" (Common Beginner Mistakes & Fixes)**.
   - Right side: In-browser code editor, instant execution, and live **3D Variable Memory Visualizer**.

3. **Bilingual Engine (🇬🇧 English / 🇮🇳 Hinglish):**
   - 1-Click persistent language toggle across all theory, error decoders, and hints.

4. **Dynamic Question Bank:**
   - Customize problem sets by Subject (Python, HTML/CSS), Topic, Difficulty, and Count.
   - Real-world campus problems (Swiggy bill splitters, 75% attendance checkers).

5. **College Mock Test & Lab Viva Simulator:**
   - Realistic university CA practical exam simulator (Output Guessing, Doctor Mode Bug-Fixing, Coding Challenges, and rapid Oral Viva with scoring answers).

6. **🚨 10-Minute Lab Panic Button:**
   - Instant triage mode for students before entering the practical lab.

7. **📄 1-Click Printable Lab Practical Record (PDF Ready):**
   - Generates authentic university practical files complete with Aim, Algorithm, Source Code, Sample I/O, Viva Q&A, and Faculty Signature grid.

8. **🔬 Line-by-Line Code X-Ray (Viva Shield):**
   - Paste any code snippet and get an instant line-by-line breakdown with anticipated professor viva questions!

---

## 🛠️ Quick Start

```bash
# Run locally with standard Python (zero pip packages)
python3 main.py

# Open in your browser:
http://localhost:8080

# Run the tests (they use a temporary database, never your real data)
python3 -m unittest discover -s tests -v
```

## ⚙️ Configuration (environment variables)

| Variable | Default | Meaning |
|---|---|---|
| `PORT` | `8080` | port to listen on |
| `HOST` | `127.0.0.1` | `127.0.0.1` = only your computer. Hosting platforms need `0.0.0.0` |
| `ELYSIA_DATA_DIR` | `./data` | folder with the SQLite database (`elysia.db`). Use a persistent disk in production |
| `ELYSIA_ALLOW_SERVER_EXEC` | on for localhost, **off** otherwise | run student code on the server. Keep it OFF on a public site |
| `ELYSIA_TRUST_PROXY` | auto on Render | read the real visitor IP from `X-Forwarded-For` |

## 🔐 Security model (short)

* **Public site:** code runs in the visitor's browser (Pyodide in a Web Worker). The server never executes student code.
* **Local use:** server-side execution is on for speed. It is limited (timeout, memory, output cap, empty environment) but is *hardening, not a sandbox*.
* Passwords: scrypt. Sessions: random token in an `HttpOnly` cookie. Login attempts are rate limited.
* Old `data/users.json` accounts are imported into SQLite automatically on first start (old SHA-256 hashes are upgraded at the next login).

---

## 📋 Production Deployment Checklist

Before going live on Render, Railway, Fly.io, or an Ubuntu VPS:

- [ ] **Attach Persistent Disk for Database Storage:** Set `ELYSIA_DATA_DIR` to a mounted persistent volume path (e.g., `/var/data` or `/data`). Ephemeral container disks will wipe SQLite databases on restart.
- [ ] **Ensure Server Execution is Disabled:** Set `ELYSIA_ALLOW_SERVER_EXEC=0`. Verify by opening `/api/config` on your production URL — it must return `{"server_exec": false}`.
- [ ] **Rotate AI API Keys:** Generate fresh keys for Groq and Gemini. Supply them via your platform's environment variables dashboard (`GROQ_API_KEY`, `GEMINI_API_KEY`).
- [ ] **Never Commit `.env` or Credentials:** Verify `.env` is never staged or committed to Git. `.gitignore` and `.dockerignore` both exclude `.env`, `.env.*`, `data/*.db*`, and `data/users.json*`.
- [ ] **Configure Reverse Proxy Trust:** Set `ELYSIA_TRUST_PROXY=1` when running behind a cloud load balancer or reverse proxy (Render, Cloudflare, Nginx) so that brute-force protection correctly inspects `X-Forwarded-For`.
- [ ] **Run Full Test Suite:** Execute `python3 -m unittest discover -s tests -v` on your build container to verify all 77 tests pass before traffic is routed.
