# Elysia Code — Utility & Testing Tools (`tools/`)

This directory houses utility generator scripts, offline presentation builders, and automated browser verification suites for Elysia Code.

---

## 🛠️ Generator & Patching Scripts

| Script | Purpose & Description |
|---|---|
| `append_css.py` | Appends pixel-accurate master design system rules and CSS variables for the app shell, sidebar navigation, and desktop workspaces to `web/css/style.css`. |
| `build_ui.py` | Utility script that assembled the handbook tabs, integrated course workspace, and modal layers into `web/index.html`. |
| `generate_perfect_html.py` | Template generator used to construct the complete reference UI layout, sidebar tree navigation, and main content viewports in `web/index.html`. |
| `generate_pptx.py` | Master presentation generator that outputs a 14-slide 16:9 widescreen PowerPoint deck (`.pptx`) detailing Elysia Code architecture, pedagogy, and technical benchmarks. |
| `update_app_js.py` | Patching script that bound the reference UI accordion, interactive tree listeners, and project loaders into `web/js/app.js`. |
| `update_css_dashboard.py` | Injects the lower dashboard canvas, metrics card grids, and theme override styling into `web/css/style.css`. |

---

## 🧪 Verification & Automated Testing Tools

| Script | Purpose & Description |
|---|---|
| `verify_curriculum_outputs.py` | Executes every code example (`example_1`, `example_2`) and challenge solution across all 26 chapters (140 subtopics) in `data/curriculum_tree.json` and verifies that runtime `stdout` matches `expected_output` deterministically. Skips display-dependent desktop Tkinter examples with explicit notices. |
| `test_browser_ai_verify.js` | Headless Google Chrome test via Chrome DevTools Protocol (CDP) that evaluates client-side Pyodide WebAssembly validation of AI-generated questions in `web/js/app.js`. |
| `test_browser_mock_exam.js` | Headless Google Chrome test via CDP verifying that mock exam Section A renders properly, option clicks with single quotes (e.g. `'b = a'`) run without SyntaxErrors, and HTML option tags (e.g. `<div class='nav'>`) are safely escaped. |

---

## 📌 Usage Guidelines

To run curriculum verification:
```bash
python3 tools/verify_curriculum_outputs.py
```

To run headless browser UI tests:
```bash
node tools/test_browser_ai_verify.js
node tools/test_browser_mock_exam.js
```
