/**
 * =============================================================================
 * ELYSIA NEXT — THE LIVING IDE APPLICATION ENGINE
 * Full Reactivity · Visual Learning Engine · Pyodide WASM · Socratic AI
 * =============================================================================
 */

class ElysiaNextApp {
  constructor() {
    this.lang = localStorage.getItem("elysia_lang") || "hi";
    this.track = localStorage.getItem("elysia_track") || "python";
    this.theme = localStorage.getItem("elysia_theme") || "dark";
    this.execEngine = localStorage.getItem("elysia_exec_engine") || "pyodide";
    
    this.currentPartIdx = 0;
    this.currentChapterIdx = 0;
    this.currentSubtopicIdx = 0;
    
    this.completedSubtopics = new Set(
      JSON.parse(localStorage.getItem("elysia_completed_subtopics") || "[]")
    );
    this.xp = parseInt(localStorage.getItem("elysia_xp") || "120", 10);
    this.streak = parseInt(localStorage.getItem("elysia_streak") || "1", 10);
    this.runCount = 0;

    this.codeMirror = null;
    this.activeTab = "code"; // "code", "tests", "preview"
    this.activeConsoleTab = "output"; // "output", "errors", "repl", "memory"

    // Stepper state
    this.stepLine = 0;
    this.stepHistory = [];
  }

  async init() {
    this.applyTheme(this.theme);
    this._initCodeMirror();
    this._setupEventListeners();
    this.loadCurriculum();
    this.updateHUD();
    
    // Initialize Pyodide engine in background
    if (window.pyodideManager) {
      window.pyodideManager.init().catch(err => {
        console.warn("Pyodide preloading background notice:", err);
      });
    }

    console.log("🚀 Elysia Next Living IDE initialized.");
  }

  // ===========================================================================
  // 1. THEME & DISPLAY
  // ===========================================================================
  applyTheme(theme) {
    this.theme = theme;
    document.body.setAttribute("data-theme", theme);
    localStorage.setItem("elysia_theme", theme);
    
    const themeBtn = document.getElementById("next-theme-toggle-btn");
    if (themeBtn) {
      themeBtn.textContent = theme === "light" ? "🌙" : "☀️";
      themeBtn.title = theme === "light" ? "Switch to Dark OLED Theme" : "Switch to Light Editorial Theme";
    }

    if (this.codeMirror) {
      this.codeMirror.refresh();
    }
  }

  toggleTheme() {
    this.applyTheme(this.theme === "light" ? "dark" : "light");
  }

  setLanguage(lang) {
    this.lang = lang;
    localStorage.setItem("elysia_lang", lang);
    document.querySelectorAll(".next-switch-btn[data-lang]").forEach(btn => {
      btn.classList.toggle("active", btn.dataset.lang === lang);
    });
    this.renderActiveLesson();
  }

  setTrack(track) {
    this.track = track;
    localStorage.setItem("elysia_track", track);
    document.querySelectorAll(".next-switch-btn[data-track]").forEach(btn => {
      btn.classList.toggle("active", btn.dataset.track === track);
    });
    
    if (track === "html") {
      this.setEditorMode("html");
      const previewTab = document.getElementById("tab-ide-preview");
      if (previewTab) previewTab.style.display = "inline-flex";
    } else {
      this.setEditorMode("python");
      const previewTab = document.getElementById("tab-ide-preview");
      if (previewTab) previewTab.style.display = "none";
    }
    
    this.loadCurriculum();
  }

  // ===========================================================================
  // 2. CURRICULUM LOADING & EXPLORER RAIL
  // ===========================================================================
  loadCurriculum() {
    this.curriculumParts = window.PYTHON_CURRICULUM_PARTS || [];
    this.flatChapters = [];
    (this.curriculumParts || []).forEach(p => {
      (p.chapters || []).forEach(c => this.flatChapters.push(c));
    });
    this.renderExplorerRail();
    this.renderActiveLesson();
  }

  getActiveSubtopic() {
    if (!this.flatChapters || this.flatChapters.length === 0) return null;
    const ch = this.flatChapters[this.currentChapterIdx];
    if (!ch || !ch.subtopics) return null;
    return ch.subtopics[this.currentSubtopicIdx] || null;
  }

  renderExplorerRail() {
    const container = document.getElementById("next-tree-container");
    if (!container) return;

    if (!this.curriculumParts || this.curriculumParts.length === 0) {
      container.innerHTML = `<div style="padding:14px; color:var(--next-text-muted); font-size:0.8rem;">Loading curriculum...</div>`;
      return;
    }

    let globalChapterIndex = 0;
    let html = "";

    this.curriculumParts.forEach((part, partIdx) => {
      const partNum = part.part_number;
      const partTitle = (part.part_title || "").replace(/^PART\s*\d+\s*:\s*/i, '');
      const chapters = part.chapters || [];
      const isPartActive = partIdx === this.currentPartIdx;

      html += `
        <div class="next-part-node ${isPartActive ? 'open' : ''}" data-part-idx="${partIdx}">
          <div class="next-part-head" onclick="window.elysiaNext.togglePart(${partIdx})">
            <span>Part ${partNum}: ${this._escapeHtml(partTitle)}</span>
            <span style="font-size:0.68rem; color:var(--next-text-faint);">${chapters.length} Ch</span>
          </div>
          <div class="next-part-chapters" style="${isPartActive ? 'display:block;' : 'display:none;'}">
      `;

      chapters.forEach((ch) => {
        const thisChIndex = globalChapterIndex++;
        const isChapterActive = thisChIndex === this.currentChapterIdx;
        const subtopics = ch.subtopics || [];

        html += `
          <div class="next-chapter-node">
            <div class="next-ch-head ${isChapterActive ? 'active' : ''}" onclick="window.elysiaNext.selectChapter(${thisChIndex})">
              <span>${ch.icon || '🐍'} ${this._escapeHtml(ch.title || '')}</span>
              <span style="font-size:0.68rem; opacity:0.7;">${subtopics.length}</span>
            </div>
            <div class="next-subtopics-list" style="${isChapterActive ? 'display:flex;' : 'display:none;'}">
        `;

        subtopics.forEach((sub, subIdx) => {
          const isSubActive = isChapterActive && subIdx === this.currentSubtopicIdx;
          const isDone = this.completedSubtopics.has(sub.id);
          html += `
            <div class="next-subtopic-item ${isSubActive ? 'active' : ''}" onclick="window.elysiaNext.selectSubtopic(${thisChIndex}, ${subIdx})">
              <span class="next-sub-indicator">${isDone ? '✓' : (isSubActive ? '●' : '○')}</span>
              <span style="flex:1; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">${this._escapeHtml(sub.title || '')}</span>
            </div>
          `;
        });

        html += `
            </div>
          </div>
        `;
      });

      html += `
          </div>
        </div>
      `;
    });

    container.innerHTML = html;
  }

  togglePart(partIdx) {
    this.currentPartIdx = partIdx;
    this.renderExplorerRail();
  }

  selectChapter(chIdx) {
    this.currentChapterIdx = chIdx;
    this.currentSubtopicIdx = 0;
    this.renderExplorerRail();
    this.renderActiveLesson();
  }

  selectSubtopic(chIdx, subIdx) {
    this.currentChapterIdx = chIdx;
    this.currentSubtopicIdx = subIdx;
    this.renderExplorerRail();
    this.renderActiveLesson();
  }

  filterExplorer(query) {
    const q = (query || "").toLowerCase().trim();
    if (!q) {
      this.renderExplorerRail();
      return;
    }
    const container = document.getElementById("next-tree-container");
    if (!container) return;

    const items = container.querySelectorAll(".next-subtopic-item, .next-ch-head, .next-part-head");
    items.forEach(el => {
      const match = el.textContent.toLowerCase().includes(q);
      el.style.display = match ? "flex" : "none";
      if (match) {
        // Expand parents
        let parent = el.parentElement;
        while (parent && parent !== container) {
          parent.style.display = "block";
          parent = parent.parentElement;
        }
      }
    });
  }

  // ===========================================================================
  // 3. LESSON READER & VISUAL LEARNING ENGINE
  // ===========================================================================
  renderActiveLesson() {
    const flatChapters = [];
    (this.curriculumParts || []).forEach(p => {
      (p.chapters || []).forEach(c => flatChapters.push(c));
    });

    if (flatChapters.length === 0) return;
    const chapter = flatChapters[this.currentChapterIdx] || flatChapters[0];
    const subtopics = chapter.subtopics || [];
    const subtopic = subtopics[this.currentSubtopicIdx] || subtopics[0];

    const isHi = this.lang === "hi";

    // 1. Update Breadcrumbs
    const bcPart = document.getElementById("next-bc-part");
    const bcCh = document.getElementById("next-bc-ch");
    const bcSub = document.getElementById("next-bc-sub");
    if (bcPart) bcPart.textContent = `Part ${chapter.part_number || 1}`;
    if (bcCh) bcCh.textContent = chapter.title || `Chapter ${this.currentChapterIdx + 1}`;
    if (bcSub) bcSub.textContent = isHi ? (subtopic.title_hi || subtopic.title) : subtopic.title;

    // 2. Update Lesson Header
    const chPill = document.getElementById("next-lesson-ch-pill");
    const titleEl = document.getElementById("next-lesson-title");
    const leadEl = document.getElementById("next-lesson-lead");

    if (chPill) chPill.textContent = `${chapter.icon || '🐍'} Chapter ${chapter.chapter_number || (this.currentChapterIdx + 1)} • ${chapter.estimated_time || '30 mins'}`;
    if (titleEl) titleEl.textContent = isHi ? (subtopic.title_hi || subtopic.title) : subtopic.title;
    if (leadEl) leadEl.textContent = isHi ? (subtopic.concept_hi || subtopic.what_is_it_hi || subtopic.concept_en) : (subtopic.concept_en || subtopic.what_is_it_en);

    // 3. Structured Callout Cards
    const whyCard = document.getElementById("next-card-why");
    const syntaxCard = document.getElementById("next-card-syntax");
    const rulesCard = document.getElementById("next-card-rules");
    const analogyCard = document.getElementById("next-card-analogy");

    if (whyCard) {
      const whyText = isHi ? (subtopic.why_need_it_hi || subtopic.why_need_it_en) : (subtopic.why_need_it_en || subtopic.why_need_it_hi);
      whyCard.querySelector(".next-card-body").innerHTML = `<p>${this._escapeHtml(whyText || 'Understanding the purpose behind this tool.')}</p>`;
    }

    if (syntaxCard) {
      const syntax = subtopic.syntax || "";
      const how = isHi ? (subtopic.how_to_use_hi || subtopic.how_to_use_en) : (subtopic.how_to_use_en || subtopic.how_to_use_hi);
      syntaxCard.querySelector(".next-card-body").innerHTML = `
        <div class="next-code-block" style="margin-top:4px;">
          <div class="next-code-head">
            <span>SYNTAX BLUEPRINT</span>
            <button class="next-load-ide-btn" onclick="window.elysiaNext.setCode(${JSON.stringify(syntax)})">⚡ Load into IDE</button>
          </div>
          <pre class="next-code-pre">${this._escapeHtml(syntax)}</pre>
        </div>
        <p style="margin-top:8px;">${this._escapeHtml(how || '')}</p>
      `;
    }

    if (rulesCard) {
      const rules = isHi ? (subtopic.rules_hi || subtopic.rules_en || []) : (subtopic.rules_en || subtopic.rules_hi || []);
      const rulesHtml = rules.map(r => `<li>${this._escapeHtml(r)}</li>`).join("");
      rulesCard.querySelector(".next-card-body").innerHTML = `<ul>${rulesHtml || '<li>Follow standard Python indentation and syntax.</li>'}</ul>`;
    }

    if (analogyCard) {
      const analogy = isHi ? (subtopic.analogy_hi || subtopic.analogy_en) : (subtopic.analogy_en || subtopic.analogy_hi);
      analogyCard.querySelector(".next-card-body").innerHTML = `<p>${this._escapeHtml(analogy || 'Relatable mental model for intuitive comprehension.')}</p>`;
    }

    // 4. Code Examples
    const exWrap = document.getElementById("next-examples-container");
    if (exWrap) {
      let exHtml = "";
      if (subtopic.example_1) {
        const ex1 = subtopic.example_1;
        exHtml += `
          <div class="next-code-block">
            <div class="next-code-head">
              <span>EXAMPLE 1: ${this._escapeHtml(isHi ? (ex1.title_hi || ex1.title) : ex1.title)}</span>
              <button class="next-load-ide-btn" onclick="window.elysiaNext.setCode(${JSON.stringify(ex1.code)})">⚡ Try in IDE</button>
            </div>
            <pre class="next-code-pre">${this._escapeHtml(ex1.code)}</pre>
            <div style="padding:8px 14px; font-size:0.8rem; color:var(--next-text-secondary); background:rgba(255,255,255,0.02); border-top:1px solid var(--next-border-subtle);">
              ${this._escapeHtml(isHi ? (ex1.explanation_hi || ex1.explanation_en) : ex1.explanation_en)}
            </div>
          </div>
        `;
      }
      if (subtopic.example_2) {
        const ex2 = subtopic.example_2;
        exHtml += `
          <div class="next-code-block">
            <div class="next-code-head">
              <span>EXAMPLE 2 (PRACTICAL): ${this._escapeHtml(isHi ? (ex2.title_hi || ex2.title) : ex2.title)}</span>
              <button class="next-load-ide-btn" onclick="window.elysiaNext.setCode(${JSON.stringify(ex2.code)})">⚡ Try in IDE</button>
            </div>
            <pre class="next-code-pre">${this._escapeHtml(ex2.code)}</pre>
            <div style="padding:8px 14px; font-size:0.8rem; color:var(--next-text-secondary); background:rgba(255,255,255,0.02); border-top:1px solid var(--next-border-subtle);">
              ${this._escapeHtml(isHi ? (ex2.explanation_hi || ex2.explanation_en) : ex2.explanation_en)}
            </div>
          </div>
        `;
      }
      exWrap.innerHTML = exHtml;
    }

    // 5. Challenge Card
    const chCard = document.getElementById("next-challenge-container");
    if (chCard && subtopic.challenge) {
      const ch = subtopic.challenge;
      const hintsHtml = (ch.hints && ch.hints.length > 0) ? `
        <div class="next-hints-wrap">
          <button class="next-hint-toggle-btn" onclick="window.elysiaNext.toggleHints()">
            <span>💡 Need a hint? (${ch.hints.length})</span>
          </button>
          <div id="next-hints-content" class="next-hint-box" style="display:none;">
            ${ch.hints.map(h => `<div>• ${this._escapeHtml(h)}</div>`).join('')}
          </div>
        </div>
      ` : '';

      const solutionHtml = ch.solution_code ? `
        <div id="next-solution-content" class="next-solution-box" style="display:none;">
          <div class="next-sol-head">
            <span>💡 Official Solution Code:</span>
            <button class="next-btn-micro-primary" onclick="window.elysiaNext.setCode(${JSON.stringify(ch.solution_code)})">Copy to IDE</button>
          </div>
          <pre class="next-sol-pre">${this._escapeHtml(ch.solution_code)}</pre>
          ${ch.solution_explanation_en ? `<div style="font-size:0.75rem; color:var(--next-text-muted); margin-top:6px;">${this._escapeHtml(isHi ? (ch.solution_explanation_hi || ch.solution_explanation_en) : ch.solution_explanation_en)}</div>` : ''}
        </div>
      ` : '';

      chCard.innerHTML = `
        <div class="next-challenge-card">
          <div class="next-challenge-head">
            <span class="next-challenge-title">🎯 Hands-on Coding Challenge</span>
            <span class="next-challenge-xp-badge">Earn +${subtopic.xp || 50} XP</span>
          </div>
          <div class="next-challenge-prompt">${this._escapeHtml(isHi ? (ch.prompt_hi || ch.prompt_en) : ch.prompt_en)}</div>
          ${ch.expected_output ? `
            <div class="next-expected-output-box">
              <span>Expected Output: </span><code>${this._escapeHtml(ch.expected_output)}</code>
            </div>
          ` : ''}
          ${hintsHtml}
          <div style="display:flex; flex-wrap:wrap; gap:8px;">
            <button class="next-step-btn primary" onclick="window.elysiaNext.setCode(${JSON.stringify(ch.starter_code || subtopic.starter_code || '')})">
              🚀 Load Starter Code
            </button>
            <button class="next-btn-test-prominent" onclick="window.elysiaNext.runTests()">
              🧪 Run Tests & Submit
            </button>
            ${ch.solution_code ? `
              <button class="next-step-btn" onclick="window.elysiaNext.toggleSolution()">
                👁️ Toggle Solution
              </button>
            ` : ''}
          </div>
          ${solutionHtml}
        </div>
      `;

      // Synchronize Test Cases Console View
      const tc1Expected = document.getElementById("next-tc1-expected");
      const tc1Actual = document.getElementById("next-tc1-actual");
      const tc1Badge = document.getElementById("next-tc1-badge");
      const tc1Dot = document.getElementById("next-tc1-dot");
      const tc2Badge = document.getElementById("next-tc2-badge");
      const overallBadge = document.getElementById("next-tests-overall-badge");
      const summaryBadge = document.getElementById("next-test-summary-badge");
      const banner = document.getElementById("next-tests-success-banner");

      if (tc1Expected) tc1Expected.textContent = ch.expected_output || "Program completes execution without error.";
      if (tc1Actual) tc1Actual.textContent = "[Not run yet — click Run Tests]";
      if (tc1Badge) { tc1Badge.className = "next-tc-badge"; tc1Badge.textContent = "Pending"; }
      if (tc1Dot) { tc1Dot.className = "next-tc-dot"; }
      if (tc2Badge) { tc2Badge.className = "next-tc-badge"; tc2Badge.textContent = "Pending"; }
      if (overallBadge) { overallBadge.className = "next-status-tag pending"; overallBadge.textContent = "Ready to verify"; }
      if (summaryBadge) { summaryBadge.textContent = "1 Spec"; summaryBadge.style.color = ""; }
      if (banner) banner.style.display = "none";
    }

    // 6. Set Starter Code in IDE
    const starter = (subtopic.challenge && subtopic.challenge.starter_code) ||
                    (subtopic.example_1 && subtopic.example_1.code) ||
                    subtopic.starter_code ||
                    "# Write your Python code here\n";
    this.setCode(starter);

    // Initial Memory Trace & Stepper
    this.updateVisualEngineWithCode(starter);
  }

  // ===========================================================================
  // 4. VISUAL LEARNING ENGINE (Memory RAM & Stepper)
  // ===========================================================================
  updateVisualEngineWithCode(code) {
    const parsed = this._parseCodeVariables(code);
    this.renderRAMCells(parsed);
    this._setupStepper(code);
  }

  renderRAMCells(variables) {
    const grid = document.getElementById("next-ram-cells-grid");
    if (!grid) return;

    const entries = Object.entries(variables || {});
    if (entries.length === 0) {
      grid.innerHTML = `<div style="grid-column: 1/-1; padding: 12px; font-size:0.78rem; color:var(--next-text-muted);">Run code or step through execution to inspect variables in RAM.</div>`;
      return;
    }

    grid.innerHTML = entries.map(([name, data], idx) => {
      const val = typeof data === "object" ? data.val : String(data);
      const type = typeof data === "object" ? data.type : "var";
      const hex = `0x7f${(1024 + idx * 16).toString(16)}`;

      return `
        <div class="next-ram-cell" title="Virtual Address: ${hex}">
          <div class="next-cell-meta">
            <span class="next-cell-name">${this._escapeHtml(name)}</span>
            <span class="next-cell-type">${this._escapeHtml(type)}</span>
          </div>
          <div class="next-cell-val">${this._escapeHtml(val)}</div>
          <div class="next-cell-addr">${hex}</div>
        </div>
      `;
    }).join("");
  }

  _setupStepper(code) {
    const lines = (code || "").split("\n").filter(l => l.trim() && !l.trim().startsWith("#"));
    this.stepperLines = lines;
    this.currentStepIdx = 0;
    this.updateStepperUI();
  }

  stepForward() {
    if (!this.stepperLines || this.stepperLines.length === 0) return;
    if (this.currentStepIdx < this.stepperLines.length) {
      this.currentStepIdx++;
      // Execute slice of code up to this step
      const partialCode = this.stepperLines.slice(0, this.currentStepIdx).join("\n");
      const vars = this._parseCodeVariables(partialCode);
      this.renderRAMCells(vars);
      this.updateStepperUI();
    }
  }

  stepReset() {
    this.currentStepIdx = 0;
    const initialCode = this.getCode();
    const vars = this._parseCodeVariables(initialCode);
    this.renderRAMCells(vars);
    this.updateStepperUI();
  }

  updateStepperUI() {
    const ind = document.getElementById("next-step-indicator");
    if (ind) {
      const total = this.stepperLines ? this.stepperLines.length : 0;
      ind.textContent = `Line ${this.currentStepIdx} of ${total}`;
    }
  }

  // ===========================================================================
  // 5. CODING WORKSPACE & IDE
  // ===========================================================================
  _initCodeMirror() {
    const area = document.getElementById("next-code-textarea");
    if (!area || typeof window.CodeMirror === "undefined") return;

    this.codeMirror = window.CodeMirror.fromTextArea(area, {
      mode: "python",
      theme: "dracula",
      lineNumbers: true,
      matchBrackets: true,
      autoCloseBrackets: true,
      indentUnit: 4,
      tabSize: 4,
      indentWithTabs: false,
      lineWrapping: true,
      extraKeys: {
        "Tab": cm => cm.replaceSelection("    ", "end"),
        "Ctrl-Enter": () => this.runCode(),
        "Cmd-Enter": () => this.runCode(),
        "Ctrl-Shift-Enter": () => this.runTests(),
        "Cmd-Shift-Enter": () => this.runTests()
      }
    });

    this.codeMirror.on("change", () => {
      area.value = this.codeMirror.getValue();
    });
  }

  getCode() {
    if (this.codeMirror) return this.codeMirror.getValue();
    const el = document.getElementById("next-code-textarea");
    return el ? el.value : "";
  }

  setCode(code) {
    const text = String(code || "");
    const el = document.getElementById("next-code-textarea");
    if (el) el.value = text;
    if (this.codeMirror) {
      this.codeMirror.setValue(text);
      setTimeout(() => this.codeMirror.refresh(), 20);
    }
    this.updateVisualEngineWithCode(text);
  }

  setEditorMode(mode) {
    if (this.codeMirror) {
      this.codeMirror.setOption("mode", mode === "html" ? "htmlmixed" : "python");
    }
  }

  async runCode() {
    const t0 = performance.now();
    const code = this.getCode();
    const runBtn = document.getElementById("next-btn-run");
    const statusEl = document.getElementById("next-exec-status");
    const outEl = document.getElementById("next-stdout");

    if (runBtn) runBtn.textContent = "⚡ Running...";
    if (statusEl) statusEl.textContent = "Running...";
    if (outEl) outEl.textContent = "⚡ Executing program...";

    // Ensure output tab is active
    this.setConsoleTab("output");

    let stdout = "";
    let stderr = "";
    let vars = {};

    try {
      if (this.track === "html") {
        const frame = document.getElementById("next-html-preview-frame");
        if (frame && window.htmlRunner) {
          window.htmlRunner.setIframe(frame);
          window.htmlRunner.render(code);
          stdout = "✅ HTML rendered into live viewport.";
        }
      } else {
        if (this.execEngine === "pyodide" && window.pyodideManager) {
          const res = await window.pyodideManager.run(code, "", 5000);
          stdout = res.stdout || "";
          stderr = res.stderr || "";
          vars = res.vars || {};
        } else {
          // Server execution
          const resp = await fetch("/api/execute", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ code: code, timeout: 5 })
          });
          if (resp.ok) {
            const data = await resp.json();
            stdout = data.stdout || "";
            stderr = data.stderr || "";
          }
        }
      }
    } catch (err) {
      stderr = String(err && err.message ? err.message : err);
    }

    const duration = Math.max(1, Math.round(performance.now() - t0));

    if (runBtn) runBtn.innerHTML = `<span>Run Code</span> <span class="next-run-shortcut-tip">⌘↵</span>`;
    if (statusEl) statusEl.textContent = `⚡ ${duration}ms (${this.execEngine})`;

    if (stderr) {
      if (outEl) outEl.textContent = stdout;
      const errEl = document.getElementById("next-stderr");
      if (errEl) errEl.textContent = stderr;
      const errBanner = document.getElementById("next-error-ai-banner");
      if (errBanner) errBanner.style.display = "flex";
      this.setConsoleTab("errors");
      this.suggestAIDiagnosis(stderr, code);
      if (window.elysiaAudio) window.elysiaAudio.playError();
    } else {
      if (outEl) outEl.textContent = stdout || "[Executed with no console output]";
      const errEl = document.getElementById("next-stderr");
      if (errEl) errEl.textContent = "";
      const errBanner = document.getElementById("next-error-ai-banner");
      if (errBanner) errBanner.style.display = "none";
      if (window.elysiaAudio) window.elysiaAudio.playClick();
      
      // Update RAM visualizer
      if (Object.keys(vars).length > 0) {
        this.renderRAMCells(vars);
      } else {
        const parsed = this._parseCodeVariables(code);
        this.renderRAMCells(parsed);
      }

      this.xp += 10;
      this.runCount++;
      this.updateHUD();
    }
  }

  clearConsole() {
    const stdout = document.getElementById("next-stdout");
    const stderr = document.getElementById("next-stderr");
    if (stdout) stdout.textContent = "";
    if (stderr) stderr.textContent = "";
    const status = document.getElementById("next-exec-status");
    if (status) status.textContent = "Ready";
    const errBanner = document.getElementById("next-error-ai-banner");
    if (errBanner) errBanner.style.display = "none";
  }

  setConsoleTab(tab) {
    this.activeConsoleTab = tab;
    document.querySelectorAll(".next-c-tab").forEach(t => {
      t.classList.toggle("active", t.dataset.tab === tab);
    });

    const outView = document.getElementById("next-console-output-view");
    const testView = document.getElementById("next-console-tests-view");
    const errView = document.getElementById("next-console-errors-view");
    const aiView = document.getElementById("next-console-ai-view");
    const replView = document.getElementById("next-console-repl-view");

    if (outView) outView.style.display = tab === "output" ? "block" : "none";
    if (testView) testView.style.display = tab === "tests" ? "block" : "none";
    if (errView) errView.style.display = tab === "errors" ? "block" : "none";
    if (aiView) aiView.style.display = tab === "ai" ? "block" : "none";
    if (replView) replView.style.display = tab === "repl" ? "block" : "none";
  }

  // ===========================================================================
  // 6. INTERACTIVE TEST SUITE RUNNER
  // ===========================================================================
  async runTests() {
    if (window.elysiaAudio) window.elysiaAudio.playClick();
    const testBtn = document.getElementById("next-btn-test");
    if (testBtn) {
      testBtn.innerHTML = `<span>⏳ Verifying...</span>`;
      testBtn.disabled = true;
    }

    // Switch to test cases view
    this.setConsoleTab("tests");

    const overallBadge = document.getElementById("next-tests-overall-badge");
    const summaryBadge = document.getElementById("next-test-summary-badge");
    const tc1Badge = document.getElementById("next-tc1-badge");
    const tc1Dot = document.getElementById("next-tc1-dot");
    const tc1Actual = document.getElementById("next-tc1-actual");
    const tc1Feedback = document.getElementById("next-tc1-feedback");
    const tc2Badge = document.getElementById("next-tc2-badge");
    const tc2Dot = document.getElementById("next-tc2-dot");
    const banner = document.getElementById("next-tests-success-banner");

    if (overallBadge) {
      overallBadge.className = "next-status-tag pending";
      overallBadge.textContent = "Running test suite...";
    }
    if (banner) banner.style.display = "none";
    if (tc1Feedback) tc1Feedback.style.display = "none";

    const ch = this.flatChapters[this.currentChapterIdx];
    const sub = ch ? ch.subtopics[this.currentSubtopicIdx] : null;
    const code = this.getCode();

    let stdout = "";
    let stderr = "";

    try {
      if (this.execEngine === "pyodide" && window.pyodideManager) {
        const res = await window.pyodideManager.run(code, "", 5000);
        stdout = res.stdout || "";
        stderr = res.stderr || "";
      } else {
        const resp = await fetch("/api/execute", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ code: code, timeout: 5 })
        });
        if (resp.ok) {
          const data = await resp.json();
          stdout = data.stdout || "";
          stderr = data.stderr || "";
        }
      }
    } catch (err) {
      stderr = String(err && err.message ? err.message : err);
    }

    if (testBtn) {
      testBtn.innerHTML = `<span>🧪 Run Tests</span> <span class="next-test-status-pill" id="next-test-summary-badge">1 Spec</span>`;
      testBtn.disabled = false;
    }

    const cleanActual = stdout.trim().replace(/\r\n/g, "\n");
    const expected = (sub && sub.challenge && sub.challenge.expected_output ? sub.challenge.expected_output : "").trim().replace(/\r\n/g, "\n");

    if (tc1Actual) {
      tc1Actual.textContent = cleanActual || (stderr ? `[Runtime Error: ${stderr.split('\n').pop()}]` : "[No Output]");
    }

    // Evaluate Test Case 1: Output Match
    let tc1Passed = false;
    if (!stderr && (cleanActual === expected || (expected && cleanActual.includes(expected)))) {
      tc1Passed = true;
    }

    // Evaluate Test Case 2: Code Completeness & Clean syntax
    let tc2Passed = false;
    if (!stderr && code.trim().length > 0) {
      tc2Passed = true;
    }

    // Update Test Case 1 UI
    if (tc1Passed) {
      if (tc1Badge) { tc1Badge.className = "next-tc-badge passed"; tc1Badge.textContent = "✔ Passed"; }
      if (tc1Dot) { tc1Dot.className = "next-tc-dot passed"; }
      if (tc1Feedback) tc1Feedback.style.display = "none";
    } else {
      if (tc1Badge) { tc1Badge.className = "next-tc-badge failed"; tc1Badge.textContent = "❌ Failed"; }
      if (tc1Dot) { tc1Dot.className = "next-tc-dot failed"; }
      if (tc1Feedback) {
        tc1Feedback.className = "next-tc-feedback error";
        tc1Feedback.style.display = "block";
        if (stderr) {
          tc1Feedback.innerHTML = `⚠️ Syntax / Execution Error: <code>${this._escapeHtml(stderr.split('\n').pop())}</code>. Click <strong>🧠 AI Mentor</strong> to diagnose!`;
        } else {
          tc1Feedback.innerHTML = `⚠️ Output Mismatch: Expected exact match for <code>"${this._escapeHtml(expected)}"</code>. Got <code>"${this._escapeHtml(cleanActual)}"</code>.`;
        }
      }
    }

    // Update Test Case 2 UI
    if (tc2Passed) {
      if (tc2Badge) { tc2Badge.className = "next-tc-badge passed"; tc2Badge.textContent = "✔ Passed"; }
      if (tc2Dot) { tc2Dot.className = "next-tc-dot passed"; }
    } else {
      if (tc2Badge) { tc2Badge.className = "next-tc-badge failed"; tc2Badge.textContent = "❌ Failed"; }
      if (tc2Dot) { tc2Dot.className = "next-tc-dot failed"; }
    }

    // Overall Status
    if (tc1Passed && tc2Passed) {
      if (overallBadge) {
        overallBadge.className = "next-status-tag passed";
        overallBadge.textContent = "✔ 100% Passed (All Specs)";
      }
      if (summaryBadge) {
        summaryBadge.textContent = "✔ Passed";
        summaryBadge.style.color = "var(--next-emerald)";
      }
      if (banner) banner.style.display = "flex";

      if (window.elysiaAudio) window.elysiaAudio.playSuccess();
      this.launchConfetti();

      // Award XP
      const earnedXP = (sub && sub.xp) || 50;
      this.xp += earnedXP;
      this.updateHUD();

      // Mark solved in curriculum explorer rail
      const activeNavEl = document.querySelector(`.next-tree-sub[data-sub-idx="${this.currentSubtopicIdx}"]`);
      if (activeNavEl && !activeNavEl.textContent.includes("✔")) {
        const titleEl = activeNavEl.querySelector(".next-sub-title");
        if (titleEl) titleEl.textContent = `✔ ${titleEl.textContent}`;
      }
    } else {
      if (overallBadge) {
        overallBadge.className = "next-status-tag failed";
        overallBadge.textContent = "❌ Tests Failed";
      }
      if (summaryBadge) {
        summaryBadge.textContent = "0/2 Passed";
        summaryBadge.style.color = "var(--next-rose)";
      }
      if (window.elysiaAudio) window.elysiaAudio.playError();
    }
  }

  // ===========================================================================
  // 7. SENIOR AI MENTOR & CODE DOCTOR
  // ===========================================================================
  openAI(target = "tutor") {
    if (window.elysiaAudio) window.elysiaAudio.playClick();
    this.setConsoleTab("ai");
    const input = document.getElementById("next-console-ai-input");
    if (input) setTimeout(() => input.focus(), 100);
  }

  async diagnoseCodeWithAI() {
    if (window.elysiaAudio) window.elysiaAudio.playClick();
    this.openAI("tutor");
    const code = this.getCode();
    const thread = document.getElementById("next-console-ai-thread");
    if (!thread) return;

    if (!code.trim()) {
      this._appendAIMessage("bot", "⚠️ Your code editor is empty! Write some Python code or click 'Load Starter Code' first.");
      return;
    }

    this._appendAIMessage("user", "🔍 Scan my code in the editor for syntax bugs, logical pitfalls, and style tips.");
    const botMsgEl = this._appendAIMessage("bot", "⚡ AI Doctor is analyzing your code...");

    try {
      const resp = await fetch("/api/decode-error", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          error: "Analyze this Python code. Check for any syntax errors, indentation issues, wrong types, infinite loops, or logical mistakes. If there are mistakes, explain where and why using an intuitive analogy. If the code is correct and clean, confirm that it looks solid!",
          lang: this.lang,
          code: code
        })
      });
      if (resp.ok) {
        const data = await resp.json();
        botMsgEl.innerHTML = `<strong>${data.title || "⚡ AI Code Diagnosis"}:</strong><br>${this._escapeHtml(data.advice || data.explanation || "Code looks solid!")}`;
      } else {
        botMsgEl.textContent = "Your syntax looks clear! Ensure your variable names match what the challenge expects.";
      }
    } catch (e) {
      botMsgEl.textContent = "Code diagnosis: No critical syntax flaws detected. Run tests to verify the challenge specification.";
    }
  }

  async decodeErrorWithAI() {
    if (window.elysiaAudio) window.elysiaAudio.playClick();
    this.openAI("tutor");
    const errEl = document.getElementById("next-stderr");
    const stderr = errEl ? errEl.textContent : "";
    const code = this.getCode();

    this._appendAIMessage("user", "🧠 Can you explain this error and guide me on how to fix it without giving away the full answer?");
    const botMsgEl = this._appendAIMessage("bot", "⚡ Socratic Mentor is decoding the traceback...");

    try {
      const resp = await fetch("/api/decode-error", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          error: stderr || "Python syntax error",
          lang: this.lang,
          code: code
        })
      });
      if (resp.ok) {
        const data = await resp.json();
        botMsgEl.innerHTML = `<strong>💡 ${data.title || "Senior AI Diagnosis"}:</strong><br>${this._escapeHtml(data.advice || "Check your spelling and matching brackets.")}`;
      } else {
        botMsgEl.textContent = "Check line indentation, matching quotation marks, and make sure variables are assigned before being called.";
      }
    } catch (e) {
      botMsgEl.textContent = "Python error tip: Inspect the last line of the traceback carefully — it points directly to the line and symbol where Python stopped.";
    }
  }

  async quickAskAI(type) {
    if (window.elysiaAudio) window.elysiaAudio.playClick();
    this.openAI("tutor");
    const ch = this.flatChapters[this.currentChapterIdx];
    const sub = ch ? ch.subtopics[this.currentSubtopicIdx] : null;
    const title = sub ? (this.lang === "hi" ? (sub.title_hi || sub.title) : sub.title) : "Python";

    if (type === "debug") {
      this.diagnoseCodeWithAI();
    } else if (type === "explain") {
      this._appendAIMessage("user", `💡 Explain "${title}" simply in plain language.`);
      const botMsgEl = this._appendAIMessage("bot", "Thinking...");
      try {
        const resp = await fetch("/api/decode-error", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            error: `Explain the concept of "${title}" to a beginner student in simple ${this.lang === "hi" ? "Hinglish" : "English"} with an intuitive breakdown.`,
            lang: this.lang,
            code: this.getCode()
          })
        });
        if (resp.ok) {
          const data = await resp.json();
          botMsgEl.innerHTML = `<strong>💡 Concept Breakdown (${title}):</strong><br>${this._escapeHtml(data.advice || (sub && sub.what_is_it_en) || "Concept loaded.")}`;
        } else {
          botMsgEl.textContent = (sub && (this.lang === "hi" ? (sub.what_is_it_hi || sub.what_is_it_en) : sub.what_is_it_en)) || "Mastering this concept helps you write clean, modular Python programs.";
        }
      } catch (e) {
        botMsgEl.textContent = (sub && (this.lang === "hi" ? (sub.what_is_it_hi || sub.what_is_it_en) : sub.what_is_it_en)) || "Python syntax is designed to read like concise English.";
      }
    } else if (type === "analogy") {
      this._appendAIMessage("user", `🍕 Give a real-life analogy for "${title}".`);
      const botMsgEl = this._appendAIMessage("bot", "Thinking of an analogy...");
      const analogy = sub && (this.lang === "hi" ? (sub.analogy_hi || sub.analogy_en) : (sub.analogy_en || sub.analogy_hi));
      setTimeout(() => {
        botMsgEl.innerHTML = `<strong>🍕 Real-World Analogy:</strong><br>${this._escapeHtml(analogy || "Think of a variable as a labeled storage box in your room. When you assign a value, you put an item in the box!")}`;
      }, 300);
    } else if (type === "hint") {
      this._appendAIMessage("user", "🎯 Give me a subtle hint for the coding challenge.");
      const botMsgEl = this._appendAIMessage("bot", "Finding a hint...");
      const hint = sub && sub.challenge && sub.challenge.hints && sub.challenge.hints[0] ? sub.challenge.hints[0] : (sub && sub.challenge && sub.challenge.expected_output ? `Aim for the output: ${sub.challenge.expected_output}` : "Focus on syntax fundamentals.");
      setTimeout(() => {
        botMsgEl.innerHTML = `<strong>🎯 Challenge Hint:</strong><br>${this._escapeHtml(hint)}`;
      }, 300);
    }
  }

  async sendConsoleAIMessage() {
    const input = document.getElementById("next-console-ai-input");
    if (!input) return;
    const text = input.value.trim();
    if (!text) return;
    input.value = "";

    this._appendAIMessage("user", text);
    const botMsgEl = this._appendAIMessage("bot", "Thinking...");

    try {
      const resp = await fetch("/api/decode-error", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          error: text,
          lang: this.lang,
          code: this.getCode()
        })
      });
      if (resp.ok) {
        const data = await resp.json();
        botMsgEl.innerHTML = this._escapeHtml(data.advice || data.explanation || "Keep experimenting! Every error brings you closer to mastery.");
      } else {
        botMsgEl.textContent = "Check your syntax carefully, ensure matched brackets, and verify indentation.";
      }
    } catch (e) {
      botMsgEl.textContent = "Python tip: Check if your variables are defined before using them, and ensure all parentheses are balanced.";
    }
  }

  _appendAIMessage(sender, text) {
    const thread = document.getElementById("next-console-ai-thread");
    const div = document.createElement("div");
    div.className = `next-ai-msg ${sender}`;
    div.textContent = text;
    if (thread) {
      thread.appendChild(div);
      thread.scrollTop = thread.scrollHeight;
    }
    return div;
  }

  copyCode() {
    if (window.elysiaAudio) window.elysiaAudio.playClick();
    const code = this.getCode();
    navigator.clipboard.writeText(code).then(() => {
      const btn = document.getElementById("next-btn-run");
      if (btn) {
        const orig = btn.innerHTML;
        btn.innerHTML = `<span>📋 Copied!</span>`;
        setTimeout(() => { btn.innerHTML = orig; }, 1500);
      }
    });
  }

  resetCode() {
    if (window.elysiaAudio) window.elysiaAudio.playClick();
    const ch = this.flatChapters[this.currentChapterIdx];
    const sub = ch ? ch.subtopics[this.currentSubtopicIdx] : null;
    const starter = (sub && sub.challenge && sub.challenge.starter_code) ||
                    (sub && sub.example_1 && sub.example_1.code) ||
                    (sub && sub.starter_code) ||
                    "# Write your Python code here\n";
    this.setCode(starter);
    this.updateVisualEngineWithCode(starter);
  }

  nextSubtopic() {
    if (window.elysiaAudio) window.elysiaAudio.playClick();
    const ch = this.flatChapters[this.currentChapterIdx];
    if (!ch) return;
    if (this.currentSubtopicIdx + 1 < (ch.subtopics || []).length) {
      this.selectSubtopic(this.currentChapterIdx, this.currentSubtopicIdx + 1);
    } else if (this.currentChapterIdx + 1 < this.curriculum.length) {
      this.selectSubtopic(this.currentChapterIdx + 1, 0);
    }
  }

  toggleHints() {
    const box = document.getElementById("next-hints-content");
    if (box) {
      box.style.display = box.style.display === "none" ? "block" : "none";
    }
  }

  toggleSolution() {
    const box = document.getElementById("next-solution-content");
    if (box) {
      box.style.display = box.style.display === "none" ? "block" : "none";
    }
  }

  launchConfetti() {
    const canvas = document.getElementById("next-confetti-canvas");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const colors = ["#00f0ff", "#a855f7", "#10b981", "#fbbf24", "#f43f5e", "#ffffff"];
    const particles = [];
    for (let i = 0; i < 90; i++) {
      particles.push({
        x: window.innerWidth / 2 + (Math.random() * 200 - 100),
        y: window.innerHeight / 2 + (Math.random() * 100 - 50),
        vx: (Math.random() - 0.5) * 18,
        vy: (Math.random() - 1.2) * 16,
        size: Math.random() * 8 + 4,
        color: colors[Math.floor(Math.random() * colors.length)],
        rotation: Math.random() * 360,
        vr: (Math.random() - 0.5) * 12,
        alpha: 1
      });
    }

    function animate() {
      if (particles.length === 0) {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        return;
      }
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      for (let i = particles.length - 1; i >= 0; i--) {
        const p = particles[i];
        p.x += p.vx;
        p.y += p.vy;
        p.vy += 0.45;
        p.rotation += p.vr;
        p.alpha -= 0.012;

        if (p.alpha <= 0) {
          particles.splice(i, 1);
          continue;
        }

        ctx.save();
        ctx.globalAlpha = Math.max(0, p.alpha);
        ctx.translate(p.x, p.y);
        ctx.rotate((p.rotation * Math.PI) / 180);
        ctx.fillStyle = p.color;
        ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size);
        ctx.restore();
      }
      if (particles.length > 0) {
        requestAnimationFrame(animate);
      } else {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
      }
    }
    requestAnimationFrame(animate);
  }

  toggleAIDrawer() {
    const drawer = document.getElementById("next-ai-drawer");
    if (drawer) drawer.classList.toggle("open");
  }

  async sendAIMessage() {
    const input = document.getElementById("next-ai-input");
    const chatBody = document.getElementById("next-ai-chat-body");
    if (!input || !chatBody) return;

    const userMsg = input.value.trim();
    if (!userMsg) return;
    input.value = "";

    // Append user message
    const userDiv = document.createElement("div");
    userDiv.className = "next-ai-msg user";
    userDiv.textContent = userMsg;
    chatBody.appendChild(userDiv);

    // Bot response placeholder
    const botDiv = document.createElement("div");
    botDiv.className = "next-ai-msg bot";
    botDiv.textContent = "Thinking...";
    chatBody.appendChild(botDiv);
    chatBody.scrollTop = chatBody.scrollHeight;

    try {
      const resp = await fetch("/api/decode-error", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ error: userMsg, lang: this.lang, code: this.getCode() })
      });
      if (resp.ok) {
        const data = await resp.json();
        botDiv.textContent = data.advice || data.explanation || "Look closely at your syntax and variable types.";
      } else {
        botDiv.textContent = "Python is case-sensitive! Check your spellings, variable definitions, and matching brackets.";
      }
    } catch (e) {
      botDiv.textContent = "Python tip: Check if your variables are defined before using them, and ensure all parentheses are balanced.";
    }
    chatBody.scrollTop = chatBody.scrollHeight;
  }

  suggestAIDiagnosis(stderr, code) {
    const drawer = document.getElementById("next-ai-drawer");
    const chatBody = document.getElementById("next-ai-chat-body");
    if (!chatBody) return;

    const alertDiv = document.createElement("div");
    alertDiv.className = "next-ai-msg bot";
    alertDiv.innerHTML = `
      <strong style="color:var(--next-rose);">⚠️ Error Detected:</strong><br>
      <code>${this._escapeHtml(stderr.split('\n').pop())}</code><br>
      <button class="next-step-btn primary" style="margin-top:6px;" onclick="window.elysiaNext.decodeErrorWithAI()">
        🧠 Decode Error with AI Mentor
      </button>
    `;
    chatBody.appendChild(alertDiv);
  }

  async askAIToFix() {
    this.decodeErrorWithAI();
  }

  // ===========================================================================
  // 7. COMMAND PALETTE (⌘ K)
  // ===========================================================================
  openCommandPalette() {
    const modal = document.getElementById("next-palette-modal");
    const input = document.getElementById("next-palette-input");
    if (modal) modal.classList.add("open");
    if (input) {
      input.value = "";
      input.focus();
      this.filterPalette("");
    }
  }

  closeCommandPalette() {
    const modal = document.getElementById("next-palette-modal");
    if (modal) modal.classList.remove("open");
  }

  filterPalette(query) {
    const results = document.getElementById("next-palette-results");
    if (!results) return;

    const q = (query || "").toLowerCase().trim();
    let flat = [];
    (this.curriculumParts || []).forEach(p => {
      (p.chapters || []).forEach(c => {
        (c.subtopics || []).forEach((s, sIdx) => {
          flat.push({
            part: p.part_number,
            chapter: c.title,
            subtopic: s.title,
            chIdx: flat.length, // approximation
            subIdx: sIdx
          });
        });
      });
    });

    const filtered = q ? flat.filter(item => 
      item.chapter.toLowerCase().includes(q) || 
      item.subtopic.toLowerCase().includes(q)
    ).slice(0, 8) : flat.slice(0, 8);

    results.innerHTML = filtered.map(item => `
      <div class="next-palette-item" onclick="window.elysiaNext.selectSubtopicByName('${this._escapeHtml(item.subtopic)}')">
        <div>
          <span style="font-weight:600;">${this._escapeHtml(item.subtopic)}</span>
          <div style="font-size:0.7rem; color:var(--next-text-muted);">${this._escapeHtml(item.chapter)}</div>
        </div>
        <span class="next-palette-item-tag">Part ${item.part}</span>
      </div>
    `).join("");
  }

  selectSubtopicByName(name) {
    (this.curriculumParts || []).forEach((p, pIdx) => {
      let chCount = 0;
      (p.chapters || []).forEach((c, cIdx) => {
        (c.subtopics || []).forEach((s, sIdx) => {
          if (s.title === name) {
            this.currentPartIdx = pIdx;
            this.currentChapterIdx = chCount;
            this.currentSubtopicIdx = sIdx;
            this.renderExplorerRail();
            this.renderActiveLesson();
            this.closeCommandPalette();
          }
        });
        chCount++;
      });
    });
  }

  // ===========================================================================
  // 8. HELPERS & HUD
  // ===========================================================================
  updateHUD() {
    const streakEl = document.getElementById("next-hud-streak-val");
    const xpEl = document.getElementById("next-hud-xp-val");
    const levelEl = document.getElementById("next-hud-level-val");

    if (streakEl) streakEl.textContent = `${this.streak}d`;
    if (xpEl) xpEl.textContent = `${this.xp} XP`;
    if (levelEl) levelEl.textContent = `Lv. ${Math.floor(this.xp / 100) + 1}`;

    localStorage.setItem("elysia_xp", this.xp);
    localStorage.setItem("elysia_streak", this.streak);
  }

  _parseCodeVariables(code) {
    const vars = {};
    if (!code) return vars;
    const lines = String(code).split("\n");
    for (const line of lines) {
      const trimmed = line.trim();
      if (!trimmed || trimmed.startsWith("#")) continue;
      const assignMatch = trimmed.match(/^([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(.+)$/);
      if (assignMatch) {
        const name = assignMatch[1];
        let rawVal = assignMatch[2].split("#")[0].trim();
        let type = "var";
        if (/^-?\d+$/.test(rawVal)) type = "int";
        else if (/^-?\d+\.\d+$/.test(rawVal)) type = "float";
        else if (/^["'].*["']$/.test(rawVal)) {
          type = "str";
          rawVal = rawVal.replace(/^["']|["']$/g, "");
        } else if (/^\[.*\]$/.test(rawVal)) type = "list";
        else if (/^\{.*\}$/.test(rawVal)) type = "dict";
        else if (/^\(.*\)$/.test(rawVal)) type = "tuple";
        else if (rawVal === "True" || rawVal === "False") type = "bool";
        vars[name] = { val: rawVal, type: type };
      }
    }
    return vars;
  }

  _escapeHtml(text) {
    return String(text || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  _setupEventListeners() {
    // Keyboard Shortcuts
    window.addEventListener("keydown", (e) => {
      // ⌘ K or Ctrl+K for Command Palette
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") {
        e.preventDefault();
        this.openCommandPalette();
      }
      // Esc closes modals
      if (e.key === "Escape") {
        this.closeCommandPalette();
        const drawer = document.getElementById("next-ai-drawer");
        if (drawer) drawer.classList.remove("open");
      }
    });
  }
}

// Global Singleton
window.elysiaNext = new ElysiaNextApp();
document.addEventListener("DOMContentLoaded", () => {
  window.elysiaNext.init();
});
