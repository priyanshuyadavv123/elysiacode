/**
 * =============================================================================
 * ✨ ELYSIA CODE: MASTER JAVASCRIPT CONTROLLER (app.js)
 * =============================================================================
 * 📌 KYA KAAM HAI IS FILE KA (WHAT IT DOES):
 *   Ye pure website ka "Brain" (Controller) hai. Ye saare events sunta hai (button clicks,
 *   typing), Python WebAssembly (Pyodide) ko run karta hai, tabs switch karta hai,
 *   bilingual (English/Hinglish) text change karta hai, countdown timer chalata hai,
 *   aur visual handbook ke slides ko navigate karwata hai.
 *
 * 👁️ WEB PAGE PE KYA DIKHTA/HOTA HAI:
 *   Jab user kisi button par click karta hai, run code dabata hai, ya chapter badalta hai,
 *   to bina page reload huye instant changes isi file ki wajah se hote hain.
 *
 * 💡 KYUN USE KIYA (WHY WE USE THIS):
 *   Bina JavaScript ke HTML sirf ek 'static dummy page' hota hai jisme click karne par
 *   kuchh nahi hota. JavaScript page me jaan daalta hai (DOM manipulation aur event handling).
 *
 * ⚠️ AGAR ISKO CHANGE YA DELETE KAREIN TO:
 *   Pura application freeze ho jayega! Na Python code run hoga, na tabs change honge,
 *   na handbook chalegi, aur na timer tik-tik karega.
 * =============================================================================
 */

class ElysiaApp {
  /**
   * 📌 CONSTRUCTOR: App ka state (memory) initialize karta hai
   * 💡 Kyun: Har feature ko track karne ke liye variables chahiye hote hain 
   *    (jaise abhi konsi language selected hai, konsa tab khula hai).
   */
  constructor() {
    // User ki preferred language localStorage se nikaal rahe hain (Default: 'hi' for Hinglish)
    this.lang = localStorage.getItem("elysia_lang") || "hi";
    
    // Active track: 'python' ya 'html'
    this.subject = "python";
    
    // Active navigation tab: 'learn', 'handbook', 'qbank', 'mock', 'search', 'xray', 'panic'
    this.activeTab = "learn";
    
    // Server se aane wala curriculum data yahan store hota hai
    this.curriculum = null;
    this.currentTopicIndex = 0;
    
    // Mock exam state aur 25-minute timer
    this.mockExamData = null;
    this.examTimerInterval = null;
    this.examSecondsRemaining = 25 * 60; // 25 minutes in seconds
    
    // Visual Handbook chapters aur current slide index
    this.handbookChapters = null;
    this.currentHandbookChIdx = 0;
    this.currentHandbookSlideIdx = 0;

    // 🌳 Curriculum Tree for Granular Topics & Subtopics
    this.curriculumTree = window.PYTHON_CURRICULUM_TREE || [];
    this.currentChapterIdx = parseInt(localStorage.getItem("elysia_ch_idx") || "0");
    this.currentSubtopicIdx = parseInt(localStorage.getItem("elysia_sub_idx") || "0");
    this.completedSubtopics = new Set(JSON.parse(localStorage.getItem("elysia_completed_subtopics") || "[]"));

    // ⚡ Habit & Gamification Engine State
    this.xp = parseInt(localStorage.getItem("elysia_xp") || "0");
    this.streak = parseInt(localStorage.getItem("elysia_streak") || "1");
    this.todaySeconds = parseInt(localStorage.getItem("elysia_today_sec") || "0");
    this.totalSeconds = parseInt(localStorage.getItem("elysia_total_sec") || "0");
    this.lastStudyDate = localStorage.getItem("elysia_last_study_date") || new Date().toISOString().slice(0, 10);

    // 👤 Authentication & User Profile State
    this.currentUser = JSON.parse(localStorage.getItem("elysia_current_user") || "null");
    this.selectedAvatar = '🐍';
    this.selectedEditAvatar = null;
    if (this.currentUser) {
      if (typeof this.currentUser.xp === 'number') this.xp = this.currentUser.xp;
      if (typeof this.currentUser.streak === 'number') this.streak = this.currentUser.streak;
      if (Array.isArray(this.currentUser.completed_subtopics)) {
        this.currentUser.completed_subtopics.forEach(id => this.completedSubtopics.add(id));
      }
      if (typeof this.currentUser.today_seconds === 'number' && this.currentUser.today_seconds > 0) {
        this.todaySeconds = Math.max(this.todaySeconds, this.currentUser.today_seconds);
      }
    }

    // ⚙️ Python Execution Engine State (pyodide vs server)
    this.execEngine = localStorage.getItem("elysia_exec_engine") || "pyodide";

    // 🎨 Theme State (midnight, dracula, emerald, sunset, royal, light)
    this.currentTheme = localStorage.getItem("elysia_theme") || "midnight";

    // 🎯 Question Bank Map & Solved State
    this.qbankQuestionsMap = {};
    this.solvedQBankSet = new Set(JSON.parse(localStorage.getItem("elysia_solved_qbank") || "[]"));

    // 📄 Question Bank Pagination State
    this.qbankCurrentPage = 1;
    this.qbankPageSize = 5;
    this.qbankAllQuestions = [];
  }

  /**
   * 📌 INIT: Website load hone par sabse pehla function jo run hota hai
   * 👁️ Web Page Pe Effect: Saare buttons ko click listeners mil jaate hain, 
   *    Pyodide WebAssembly background me load hona shuru hota hai, aur pehla lesson render hota hai.
   */
  async init() {
    this._bindEvents();       // Saare buttons aur inputs par event listener lagaya
    this._initTheme();        // 🎨 Multi-Theme Engine (Midnight, Dracula, Emerald, Sunset, Royal, Light)
    this._initCodeMirror();   // ✨ CodeMirror Syntax Highlighter (Dark IDE with live text color changing)
    this._initInteractiveREPL(); // 🐚 Original Pyodide Interactive Console (>>>)
    this._init3DParallax();   // Modern flat card styles
    this._initStudyTimer();   // Live productivity and time spent tracker
    this._initStreak();       // Daily streak engine
    this._initConfetti();     // Dopamine particle engine
    await this.loadCurriculum(); // Backend se syllabus aur topic data mangwaya
    this.populateQBankTopics(); // 🎯 Question bank topics filter populated
    this.updateLanguageUI();  // Buttons par EN ya HI active class lagayi
    this.updateGamificationUI(); // Navbar streak, XP aur study timer update
    this.updateAuthUI();      // Navbar avatar, display name ya sign in button render
    this.renderCurrentLesson(); // Screen par lesson load kiya
    this.loadHandbook();      // Visual handbook ke chapters ready kiye
    this._initPyodideEngine(); // ⚡ Live Pyodide WebAssembly engine initialize & preload kiya
    this.setupReferenceUI(); // 🏛️ Reference UI Bindings & Tree Accordion
  }

  showOptimisticToast(msg, type = "success") {
    let toast = document.getElementById("elysia-optimistic-toast");
    if (!toast) {
      toast = document.createElement("div");
      toast.id = "elysia-optimistic-toast";
      toast.style.cssText = "position:fixed; bottom:28px; right:28px; z-index:99999; padding:12px 20px; border-radius:12px; font-weight:700; font-size:0.9rem; display:flex; align-items:center; gap:10px; box-shadow:0 12px 30px rgba(0,0,0,0.5); backdrop-filter:blur(16px); transition:all 0.3s cubic-bezier(0.16, 1, 0.3, 1); transform:translateY(80px); opacity:0;";
      document.body.appendChild(toast);
    }
    if (type === "success") {
      toast.style.background = "rgba(16, 185, 129, 0.22)";
      toast.style.border = "1px solid rgba(52, 211, 153, 0.45)";
      toast.style.color = "#6ee7b7";
    } else {
      toast.style.background = "rgba(244, 63, 94, 0.22)";
      toast.style.border = "1px solid rgba(251, 113, 133, 0.45)";
      toast.style.color = "#fda4af";
    }
    toast.innerHTML = `<span>✨</span><span>${msg}</span>`;
    toast.style.transform = "translateY(0)";
    toast.style.opacity = "1";
    if (this._toastTimer) clearTimeout(this._toastTimer);
    this._toastTimer = setTimeout(() => {
      toast.style.transform = "translateY(80px)";
      toast.style.opacity = "0";
    }, 2800);
  }

  /**
   * 📌 _BIND EVENTS: HTML elements par 'click' aur 'input' listeners jodta hai
   * 💡 Kyun: Jab user kisi button par click kare, to browser ko pata chalna chahiye 
   *    ki konsa JavaScript function chalana hai (`addEventListener`).
   * ⚠️ Agar hata dein: Buttons click karne par koi action nahi hoga.
   */
  _bindEvents() {
    // 1. Language Toggle Buttons (EN / HI)
    document.querySelectorAll(".lang-btn").forEach(btn => {
      btn.addEventListener("click", (e) => {
        const lang = e.currentTarget.dataset.lang;
        this.setLanguage(lang);
      });
    });

    // 2. Subject Track Toggles (Python vs HTML/CSS)
    document.querySelectorAll(".track-btn").forEach(btn => {
      btn.addEventListener("click", (e) => {
        const track = e.currentTarget.dataset.track;
        this.setSubject(track);
      });
    });

    // 3. Audio SFX Sound Toggle (Mute / Unmute)
    const audioBtn = document.getElementById("audio-toggle-btn");
    if (audioBtn) {
      audioBtn.addEventListener("click", () => {
        const isEnabled = window.elysiaAudio.toggle();
        audioBtn.textContent = isEnabled ? "🔊" : "🔇";
      });
    }

    // 4. Mode Dock Tab Navigation (Learn, Handbook, Q-Bank, Mock, etc.)
    document.querySelectorAll(".dock-item").forEach(item => {
      item.addEventListener("click", (e) => {
        const tab = e.currentTarget.dataset.tab;
        this.switchTab(tab);
      });
    });

    // 5. Code Execution Buttons (Run Code & Submit Code)
    const runBtn = document.getElementById("btn-run-code");
    if (runBtn) {
      runBtn.addEventListener("click", () => this.runCode());
    }

    const submitBtn = document.getElementById("btn-submit-code");
    if (submitBtn) {
      submitBtn.addEventListener("click", () => this.submitCode());
    }

    // 6. Reset Starter Code Button
    const resetBtn = document.getElementById("btn-reset-code");
    if (resetBtn) {
      resetBtn.addEventListener("click", () => this.resetCode());
    }

    // 6a. AI Debugger & AI Tutor Buttons (Powered by Groq)
    const btnFindErrors = document.getElementById("btn-ai-find-errors");
    if (btnFindErrors) {
      btnFindErrors.addEventListener("click", () => this.findErrorsWithAI());
    }

    const btnAskTutor = document.getElementById("btn-ai-ask-tutor");
    if (btnAskTutor) {
      btnAskTutor.addEventListener("click", () => this.toggleAITutor());
    }

    const chatInput = document.getElementById("ai-chat-input");
    if (chatInput) {
      chatInput.addEventListener("keydown", (e) => {
        if (e.key === "Enter" && !e.shiftKey) {
          e.preventDefault();
          this.sendAIChat();
        }
      });
    }

    // 6b. Advanced IDE Keyboard Controls (Tab Indentation, Ctrl+Enter, Auto-Brackets, Caret Tracker)
    const codeArea = document.getElementById("code-editor-textarea");
    const cursorPosEl = document.getElementById("editor-cursor-pos");

    const updateCursorPos = () => {
      if (!codeArea || !cursorPosEl) return;
      const text = codeArea.value.substring(0, codeArea.selectionStart);
      const lines = text.split("\n");
      const currentLine = lines.length;
      const currentCol = lines[lines.length - 1].length + 1;
      cursorPosEl.textContent = `Ln ${currentLine}, Col ${currentCol}`;
    };

    if (codeArea) {
      codeArea.addEventListener("keydown", (e) => {
        // Ctrl+Enter or Cmd+Enter to Run Code
        if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
          e.preventDefault();
          this.runCode();
          return;
        }

        // Tab key: Insert 4 spaces instead of losing browser focus
        if (e.key === "Tab") {
          e.preventDefault();
          const start = codeArea.selectionStart;
          const end = codeArea.selectionEnd;
          codeArea.value = codeArea.value.substring(0, start) + "    " + codeArea.value.substring(end);
          codeArea.selectionStart = codeArea.selectionEnd = start + 4;
          updateCursorPos();
          return;
        }

        // Auto-close brackets and quotes
        const pairs = { '(': ')', '[': ']', '{': '}', '"': '"', "'": "'" };
        if (pairs[e.key] && codeArea.selectionStart === codeArea.selectionEnd) {
          const start = codeArea.selectionStart;
          const closeChar = pairs[e.key];
          // If typing quote and next char is the same quote, just advance cursor
          if ((e.key === '"' || e.key === "'") && codeArea.value[start] === e.key) {
            e.preventDefault();
            codeArea.selectionStart = codeArea.selectionEnd = start + 1;
            return;
          }
          // Don't auto-close single quote inside words (like don't)
          if (e.key === "'" && start > 0 && /[a-zA-Z0-9]/.test(codeArea.value[start - 1])) {
            return;
          }
          e.preventDefault();
          codeArea.value = codeArea.value.substring(0, start) + e.key + closeChar + codeArea.value.substring(start);
          codeArea.selectionStart = codeArea.selectionEnd = start + 1;
          updateCursorPos();
        }
      });

      codeArea.addEventListener("keyup", updateCursorPos);
      codeArea.addEventListener("click", updateCursorPos);
      codeArea.addEventListener("input", updateCursorPos);
    }

    // 6c. Copy Code to Clipboard Button
    const copyCodeBtn = document.getElementById("btn-copy-code");
    if (copyCodeBtn) {
      copyCodeBtn.addEventListener("click", () => {
        navigator.clipboard.writeText(this.getCode()).then(() => {
          window.elysiaAudio.playClick();
          const original = copyCodeBtn.textContent;
          copyCodeBtn.textContent = "✓ Copied!";
          setTimeout(() => copyCodeBtn.textContent = original, 1500);
        }).catch(() => {});
      });
    }

    // 6d. Download .py Script Button
    const downloadCodeBtn = document.getElementById("btn-download-code");
    if (downloadCodeBtn) {
      downloadCodeBtn.addEventListener("click", () => {
        window.elysiaAudio.playClick();
        const blob = new Blob([this.getCode()], { type: "text/plain;charset=utf-8" });
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = "elysia_script.py";
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
      });
    }

    // 6e. Clear Terminal Output Button
    const clearTerminalBtn = document.getElementById("btn-clear-terminal");
    if (clearTerminalBtn) {
      clearTerminalBtn.addEventListener("click", () => {
        window.elysiaAudio.playClick();
        const stdoutEl = document.getElementById("terminal-stdout");
        const stderrEl = document.getElementById("terminal-stderr");
        const inputBar = document.getElementById("terminal-input-bar");
        if (stdoutEl) stdoutEl.textContent = "Terminal cleared. Click 'Run Code' or press Ctrl+Enter.";
        if (stderrEl) stderrEl.textContent = "";
        if (inputBar) inputBar.style.display = "none";
      });
    }

    // 6f. Interactive Terminal Stdin Input Bar Submit
    const submitStdinBtn = document.getElementById("btn-submit-stdin");
    const stdinInput = document.getElementById("terminal-stdin-input");
    const submitInteractiveInput = () => {
      if (!stdinInput) return;
      const val = stdinInput.value;
      stdinInput.value = "";
      this.runCode(val);
    };

    if (submitStdinBtn) {
      submitStdinBtn.addEventListener("click", submitInteractiveInput);
    }
    if (stdinInput) {
      stdinInput.addEventListener("keydown", (e) => {
        if (e.key === "Enter") {
          e.preventDefault();
          submitInteractiveInput();
        }
      });
    }

    // 6g. Escape Key to Close All Modals
    window.addEventListener("keydown", (e) => {
      if (e.key === "Escape") {
        this.closeAllModals();
      }
    });

    // 6h. Modal Backdrop Click to Close
    document.querySelectorAll(".modal-overlay").forEach(modal => {
      modal.addEventListener("click", (e) => {
        if (e.target === modal) {
          this.closeModal(modal.id);
        }
      });
    });

    // 7. 60-Sec Doubt Buster Instant Search Input
    const searchInput = document.getElementById("search-input");
    if (searchInput) {
      searchInput.addEventListener("input", (e) => this.handleSearch(e.target.value));
    }

    // 8. Question Bank Filter Trigger Button & Dynamic Dropdowns
    const qbankFilterBtn = document.getElementById("btn-filter-qbank");
    if (qbankFilterBtn) {
      qbankFilterBtn.addEventListener("click", () => this.loadQuestionBank());
    }
    const qbankTopicSelect = document.getElementById("qbank-topic-select");
    if (qbankTopicSelect) {
      qbankTopicSelect.addEventListener("change", () => this.loadQuestionBank());
    }
    const qbankDiffSelect = document.getElementById("qbank-diff-select");
    if (qbankDiffSelect) {
      qbankDiffSelect.addEventListener("change", () => this.loadQuestionBank());
    }
    const qbankCountSelect = document.getElementById("qbank-count-select");
    if (qbankCountSelect) {
      qbankCountSelect.addEventListener("change", () => this.loadQuestionBank());
    }

    const aiQBankBtn = document.getElementById("btn-ai-generate-qbank");
    if (aiQBankBtn) {
      aiQBankBtn.addEventListener("click", () => this.generateAIQuestion());
    }
    const aiPromptInput = document.getElementById("qbank-ai-custom-prompt");
    if (aiPromptInput) {
      aiPromptInput.addEventListener("keydown", (e) => {
        if (e.key === "Enter") this.generateAIQuestion();
      });
    }

    // 9. Code X-Ray Line-by-Line Dissect Button
    const xrayBtn = document.getElementById("btn-analyze-xray");
    if (xrayBtn) {
      xrayBtn.addEventListener("click", () => this.analyzeCodeXRay());
    }

    // 10. Lab File Exporter Popup Modal Trigger
    const exportBtn = document.getElementById("btn-open-exporter");
    if (exportBtn) {
      exportBtn.addEventListener("click", () => this.openLabExporterModal());
    }

    // 11. 3D Achievement Flex Card Modal Trigger
    const flexBtn = document.getElementById("btn-open-flex");
    if (flexBtn) {
      flexBtn.addEventListener("click", () => this.openFlexModal());
    }

    // 12. Panic Mode Call-to-Action (CTA) Button
    const panicCta = document.getElementById("btn-panic-cta");
    if (panicCta) {
      panicCta.addEventListener("click", () => this.switchTab("panic"));
    }

    // 13. Visual Handbook Slide Controls (Prev, Next, Send to Sandbox)
    const prevSlideBtn = document.getElementById("btn-prev-slide");
    if (prevSlideBtn) {
      prevSlideBtn.addEventListener("click", () => this.prevHandbookSlide());
    }

    const nextSlideBtn = document.getElementById("btn-next-slide");
    if (nextSlideBtn) {
      nextSlideBtn.addEventListener("click", () => this.nextHandbookSlide());
    }

    const sendToSandboxBtn = document.getElementById("btn-send-to-sandbox");
    if (sendToSandboxBtn) {
      sendToSandboxBtn.addEventListener("click", () => this.sendSlideToSandbox());
    }

    const handbookSearchInput = document.getElementById("handbook-search-input");
    if (handbookSearchInput) {
      handbookSearchInput.addEventListener("input", (e) => this.handleHandbookSearch(e.target.value));
    }

    // 14. Profile & Auth Modal Triggers
    const authBtn = document.getElementById("btn-open-auth");
    if (authBtn) {
      authBtn.addEventListener("click", () => this.openAuthModal());
    }

    const profBtn = document.getElementById("btn-open-profile");
    if (profBtn) {
      profBtn.addEventListener("click", () => this.openModal("modal-user-profile"));
    }

    const loginSubmitBtn = document.getElementById("btn-submit-login");
    if (loginSubmitBtn) {
      loginSubmitBtn.addEventListener("click", () => this.handleLoginSubmit());
    }

    const signupSubmitBtn = document.getElementById("btn-submit-signup");
    if (signupSubmitBtn) {
      signupSubmitBtn.addEventListener("click", () => this.handleSignupSubmit());
    }

    const loginPassInput = document.getElementById("auth-login-password");
    if (loginPassInput) {
      loginPassInput.addEventListener("keydown", (e) => {
        if (e.key === "Enter") this.handleLoginSubmit();
      });
    }

    const signupPassInput = document.getElementById("auth-signup-password");
    if (signupPassInput) {
      signupPassInput.addEventListener("keydown", (e) => {
        if (e.key === "Enter") this.handleSignupSubmit();
      });
    }

    // 15. Subtopic Interactive Controls
    const tryEx1Btn = document.getElementById("btn-try-example-1");
    if (tryEx1Btn) {
      tryEx1Btn.addEventListener("click", () => this.tryExample(1));
    }

    const tryEx2Btn = document.getElementById("btn-try-example-2");
    if (tryEx2Btn) {
      tryEx2Btn.addEventListener("click", () => this.tryExample(2));
    }

    const loadStarterBtn = document.getElementById("btn-load-starter-code");
    if (loadStarterBtn) {
      loadStarterBtn.addEventListener("click", () => this.loadStarterCode());
    }

    const toggleSolBtn = document.getElementById("btn-toggle-solution");
    if (toggleSolBtn) {
      toggleSolBtn.addEventListener("click", () => this.toggleSolution());
    }

    const copySolBtn = document.getElementById("btn-copy-solution");
    if (copySolBtn) {
      copySolBtn.addEventListener("click", () => this.copySolution());
    }

    const prevSubBtn = document.getElementById("btn-prev-subtopic");
    if (prevSubBtn) {
      prevSubBtn.addEventListener("click", () => this.prevSubtopic());
    }

    const nextSubBtn = document.getElementById("btn-next-subtopic");
    if (nextSubBtn) {
      nextSubBtn.addEventListener("click", () => this.nextSubtopic());
    }
  }

  /**
   * 📌 _INIT 3D PARALLAX: Mouse movement se dynamic perspective physics banata hai
   * 👁️ Web Page Pe Effect: Mouse ghumane par cards halka sa 3D tilt hote hain.
   * 💡 Kyun: Pinterest spatial computing look replicate karne ke liye clientX aur clientY se angle calculate kiya.
   */
  _init3DParallax() {
    // 3D parallax tilt removed for a clean, user-friendly, non-wobbly interface.
  }

  /**
   * 🎨 _INIT THEME: Dynamic Theme Switcher (Midnight, Dracula, Emerald, Sunset, Royal, Light)
   */
  _initTheme() {
    const urlTheme = new URLSearchParams(window.location.search).get('theme');
    const savedTheme = urlTheme || localStorage.getItem("elysia_theme") || "midnight";
    this.setTheme(savedTheme, false);

    const themeSelect = document.getElementById("theme-select");
    if (themeSelect) {
      themeSelect.value = savedTheme;
      themeSelect.addEventListener("change", (e) => {
        this.setTheme(e.target.value, true);
      });
    }
  }

  setTheme(themeName, playSound = true) {
    this.currentTheme = themeName;
    localStorage.setItem("elysia_theme", themeName);
    document.body.setAttribute("data-theme", themeName);

    const themeSelect = document.getElementById("theme-select");
    if (themeSelect && themeSelect.value !== themeName) {
      themeSelect.value = themeName;
    }

    if (playSound && window.elysiaAudio) {
      window.elysiaAudio.playClick();
    }

    if (this.codeMirror) {
      setTimeout(() => this.codeMirror.refresh(), 30);
    }
  }

  /**
   * ✨ _INIT CODEMIRROR: Professional syntax-highlighted editor with vibrant token colors
   */
  _initCodeMirror() {
    const codeArea = document.getElementById("code-editor-textarea");
    if (!codeArea) return;

    if (typeof window.CodeMirror !== "undefined") {
      try {
        this.codeMirror = window.CodeMirror.fromTextArea(codeArea, {
          mode: this.subject === "html" ? "htmlmixed" : "python",
          theme: "dracula",
          lineNumbers: true,
          matchBrackets: true,
          autoCloseBrackets: true,
          indentUnit: 4,
          tabSize: 4,
          indentWithTabs: false,
          lineWrapping: true,
          extraKeys: {
            "Tab": (cm) => cm.replaceSelection("    ", "end"),
            "Ctrl-Enter": () => this.runCode(),
            "Cmd-Enter": () => this.runCode()
          }
        });

        const cursorPosEl = document.getElementById("editor-cursor-pos");
        this.codeMirror.on("cursorActivity", () => {
          if (!cursorPosEl) return;
          const cursor = this.codeMirror.getCursor();
          cursorPosEl.textContent = `Ln ${cursor.line + 1}, Col ${cursor.ch + 1}`;
        });

        this.codeMirror.on("change", () => {
          codeArea.value = this.codeMirror.getValue();
        });

        if (codeArea.value && !this.codeMirror.getValue()) {
          this.codeMirror.setValue(codeArea.value);
        }
      } catch (err) {
        console.warn("CodeMirror initialization notice:", err);
      }
    }
  }

  getCode() {
    if (this.codeMirror) return this.codeMirror.getValue();
    const el = document.getElementById("code-editor-textarea");
    return el ? el.value : "";
  }

  setCode(val) {
    const text = String(val || "");
    const el = document.getElementById("code-editor-textarea");
    if (el) el.value = text;
    if (this.codeMirror) {
      this.codeMirror.setValue(text);
      setTimeout(() => this.codeMirror.refresh(), 20);
    }
  }

  setEditorMode(mode) {
    if (this.codeMirror) {
      this.codeMirror.setOption("mode", mode === "html" ? "htmlmixed" : "python");
      setTimeout(() => this.codeMirror.refresh(), 20);
    }
  }

  _ansiToHtml(text) {
    if (!text) return "";
    let escaped = String(text)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");

    const ansiMap = {
      "30": "ansi-black", "31": "ansi-red", "32": "ansi-green", "33": "ansi-yellow",
      "34": "ansi-blue", "35": "ansi-magenta", "36": "ansi-cyan", "37": "ansi-white",
      "90": "ansi-black", "91": "ansi-red", "92": "ansi-green", "93": "ansi-yellow",
      "94": "ansi-blue", "95": "ansi-magenta", "96": "ansi-cyan", "97": "ansi-white"
    };

    escaped = escaped.replace(/\x1b\[([0-9;]+)m/g, (match, p1) => {
      const codes = p1.split(";");
      if (codes.includes("0")) return "</span>";
      let classes = [];
      if (codes.includes("1")) classes.push("ansi-bold");
      for (const c of codes) {
        if (ansiMap[c]) classes.push(ansiMap[c]);
      }
      return classes.length ? `<span class="${classes.join(" ")}">` : "";
    });

    return escaped;
  }

  _formatTracebackHtml(tb) {
    if (!tb) return "";
    let lines = String(tb).split("\n");
    let formatted = lines.map(line => {
      let escaped = line.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
      if (escaped.includes("Traceback (most recent call last):")) {
        return `<span style="color:#94a3b8; font-weight:600;">${escaped}</span>`;
      }
      if (/^\s*File\s+"[^"]+",\s+line\s+\d+/.test(escaped)) {
        return `<span style="color:#38bdf8;">${escaped}</span>`;
      }
      if (/^[A-Za-z0-9_]+Error:/.test(escaped) || /^[A-Za-z0-9_]+Exception:/.test(escaped)) {
        return `<span style="color:#f87171; font-weight:700; background:rgba(239,68,68,0.12); padding:1px 4px; border-radius:3px;">${escaped}</span>`;
      }
      return escaped;
    }).join("\n");
    return formatted;
  }

  _initInteractiveREPL() {
    const tabOutput = document.getElementById("term-tab-output");
    const tabRepl = document.getElementById("term-tab-repl");
    const viewOutput = document.getElementById("terminal-output-view");
    const viewRepl = document.getElementById("terminal-repl-view");
    const replInput = document.getElementById("repl-input");
    const btnSend = document.getElementById("btn-repl-send");
    const historyBox = document.getElementById("repl-history");

    if (!tabOutput || !tabRepl) return;

    tabOutput.addEventListener("click", () => {
      tabOutput.classList.add("active");
      tabRepl.classList.remove("active");
      if (viewOutput) viewOutput.style.display = "block";
      if (viewRepl) viewRepl.style.display = "none";
    });

    tabRepl.addEventListener("click", () => {
      tabRepl.classList.add("active");
      tabOutput.classList.remove("active");
      if (viewOutput) viewOutput.style.display = "none";
      if (viewRepl) viewRepl.style.display = "block";
      if (replInput) replInput.focus();
    });

    const replHistoryList = [];
    let historyIdx = -1;

    const executeReplCommand = async () => {
      if (!replInput) return;
      const cmd = replInput.value.trim();
      if (!cmd) return;
      replInput.value = "";
      replHistoryList.push(cmd);
      historyIdx = replHistoryList.length;

      const inLine = document.createElement("div");
      inLine.className = "repl-line input-line";
      inLine.textContent = `>>> ${cmd}`;
      historyBox.appendChild(inLine);

      if (!window.pyodideManager) {
        const errLine = document.createElement("div");
        errLine.className = "repl-line error-line";
        errLine.textContent = "Pyodide engine is not available.";
        historyBox.appendChild(errLine);
        return;
      }

      const res = await window.pyodideManager.runRepl(cmd, 4000);
      if (res.stdout) {
        const outLine = document.createElement("div");
        outLine.className = "repl-line output-line";
        outLine.innerHTML = this._ansiToHtml(res.stdout);
        historyBox.appendChild(outLine);
      }
      if (res.result) {
        const resLine = document.createElement("div");
        resLine.className = "repl-line result-line";
        resLine.textContent = res.result;
        historyBox.appendChild(resLine);
      }
      if (res.stderr) {
        const errLine = document.createElement("div");
        errLine.className = "repl-line error-line";
        errLine.innerHTML = this._formatTracebackHtml(res.stderr);
        historyBox.appendChild(errLine);
      }
      historyBox.scrollTop = historyBox.scrollHeight;
    };

    if (btnSend) {
      btnSend.addEventListener("click", executeReplCommand);
    }
    if (replInput) {
      replInput.addEventListener("keydown", (e) => {
        if (e.key === "Enter") {
          e.preventDefault();
          executeReplCommand();
        } else if (e.key === "ArrowUp") {
          if (historyIdx > 0) {
            historyIdx--;
            replInput.value = replHistoryList[historyIdx] || "";
          }
        } else if (e.key === "ArrowDown") {
          if (historyIdx < replHistoryList.length - 1) {
            historyIdx++;
            replInput.value = replHistoryList[historyIdx] || "";
          } else {
            historyIdx = replHistoryList.length;
            replInput.value = "";
          }
        }
      });
    }

    const btnClear = document.getElementById("btn-clear-terminal");
    if (btnClear) {
      btnClear.addEventListener("click", () => {
        if (viewRepl && viewRepl.style.display !== "none") {
          if (historyBox) {
            historyBox.innerHTML = `
              <div class="repl-line system-line">Python 3.11.3 (Pyodide WebAssembly Console) — Type commands below:</div>
            `;
          }
        }
      });
    }
  }

  /**
   * 📌 LOAD CURRICULUM: Server se syllabus JSON data fetch karta hai
   * 💡 Kyun: `fetch('/api/curriculum')` use karke hum dynamic data load karte hain.
   *    Agar network offline ho to graceful fallback use hota hai.
   */
  async loadCurriculum() {
    try {
      const res = await fetch("/api/curriculum");
      this.curriculum = await res.json();
    } catch (err) {
      console.warn("API load failed, using local curriculum fallback.");
    }
  }

  /**
   * 📌 SET LANGUAGE: English aur Hinglish ke beech toggle karta hai
   * 👁️ Web Page Pe Effect: Bina reload hue poore page ki theory, tips, aur viva answers
   *    Hinglish se English ya English se Hinglish me instant translate ho jaate hain.
   * 💡 Kyun: `localStorage.setItem` use kiya taaki user kal wapas aaye to uski 
   *    language preference yaad rahe.
   */
  setLanguage(lang) {
    this.lang = lang;
    localStorage.setItem("elysia_lang", lang);
    window.elysiaAudio.playClick();
    this.updateLanguageUI();
    this.renderCurrentLesson();

    // Active tab ke content ko nayi language me re-render kiya
    if (this.activeTab === "qbank") this.loadQuestionBank();
    if (this.activeTab === "mock") this.renderMockExam();
    if (this.activeTab === "panic") this.renderPanicMode();
    if (this.activeTab === "handbook") this.renderHandbookSlide();
  }

  /**
   * 📌 SET SUBJECT: Python aur HTML/CSS track ke beech switch karta hai
   * 👁️ Web Page Pe Effect:
   *   - Agar 'python' select ho: Python IDE + Terminal + 3D Memory Tracker dikhta hai.
   *   - Agar 'html' select ho: HTML Editor + Live Browser Viewport (iframe) dikhta hai.
   */
  setSubject(subject) {
    this.subject = subject;
    this.currentTopicIndex = 0;
    window.elysiaAudio.playClick();

    document.querySelectorAll(".track-btn").forEach(btn => {
      btn.classList.toggle("active", btn.dataset.track === subject);
    });

    const isHtml = subject === "html";
    const pyEditor = document.getElementById("code-editor-textarea");
    const htmlFrame = document.getElementById("html-preview-frame");
    const memCard = document.getElementById("memory-tracker-card");

    if (pyEditor && htmlFrame) {
      if (isHtml) {
        htmlFrame.style.display = "block";
        if (memCard) memCard.style.display = "none";
      } else {
        htmlFrame.style.display = "none";
        if (memCard) memCard.style.display = "block";
      }
    }

    this.setEditorMode(subject);
    this.populateQBankTopics();
    if (this.activeTab === "qbank") {
      this.loadQuestionBank();
    }
    this.renderCurrentLesson();
  }

  /**
   * 📌 UPDATE LANGUAGE UI: Navbar buttons aur static HTML labels ko update karta hai
   */
  updateLanguageUI() {
    document.querySelectorAll(".lang-btn").forEach(btn => {
      btn.classList.toggle("active", btn.dataset.lang === this.lang);
    });

    // Static HTML me jahan `data-i18n-en` attribute hai, wahan text update kiya
    const isHi = this.lang === "hi";
    document.querySelectorAll("[data-i18n-en]").forEach(el => {
      const text = isHi ? el.dataset.i18nHi : el.dataset.i18nEn;
      if (text) el.innerHTML = text;
    });

    this.populateQBankTopics();
  }

  /**
   * 📌 SWITCH TAB: Single-Page Application (SPA) navigation karta hai
   * 👁️ Web Page Pe Effect: Bina page refresh kiye clicked tab open hota hai aur baki hide ho jaate hain.
   * 💡 Kyun: Modern fast web app experience ke liye hum multi-page navigation ke badle
   *    CSS classes `.active` toggle karte hain.
   */
  switchTab(tabName) {
    this.activeTab = tabName;
    window.elysiaAudio.playClick();

    // Dock ke button par glowing active indicator lagaya
    document.querySelectorAll(".dock-item").forEach(item => {
      item.classList.toggle("active", item.dataset.tab === tabName);
    });

    // Content area me sirf select huye tab ko `.active` (display: block) kiya
    document.querySelectorAll(".tab-content").forEach(content => {
      content.classList.toggle("active", content.id === `tab-${tabName}`);
    });

    // Specific tab khulne par uska data load kiya
    if (tabName === "qbank") {
      this.populateQBankTopics();
      this.loadQuestionBank();
    }
    if (tabName === "mock") this.loadMockExam();
    if (tabName === "panic") this.renderPanicMode();
    if (tabName === "handbook") this.loadHandbook();
  }

  // =========================================================================
  // 🏛️ MASTER REFERENCE UI ORCHESTRATOR & INTERACTIONS
  // =========================================================================

  enterCourseMode() {
    this.switchTab("learn");
    document.querySelectorAll(".side-nav-btn").forEach(b => {
      b.classList.toggle("active", b.dataset.dest === "course");
    });
    const workspace = document.getElementById("integrated-course-workspace");
    workspace?.scrollIntoView({ behavior: "smooth" });
  }

  enterDashboardMode() {
    this.switchTab("learn");
    document.querySelectorAll(".side-nav-btn").forEach(b => {
      b.classList.toggle("active", b.dataset.dest === "dashboard");
    });
    const viewport = document.getElementById("app-main-viewport");
    viewport?.scrollTo({ top: 0, behavior: "smooth" });
  }

  toggleThemeQuick() {
    const nextTheme = this.currentTheme === 'light' ? 'midnight' : 'light';
    this.setTheme(nextTheme, true);
    const quickBtn = document.getElementById("btn-quick-theme-toggle");
    if (quickBtn) quickBtn.textContent = nextTheme === 'light' ? '🌙' : '☀️';
  }

  setupReferenceUI() {
    // 0. Mobile Drawer & Backdrop Controls
    const btnMobileToggle = document.getElementById("btn-mobile-sidebar-toggle");
    const appSidebar = document.querySelector(".app-sidebar");
    const sidebarBackdrop = document.getElementById("sidebar-backdrop");

    if (btnMobileToggle && appSidebar) {
      btnMobileToggle.addEventListener("click", () => {
        window.elysiaAudio?.playClick();
        const isOpen = appSidebar.classList.toggle("mobile-open");
        if (sidebarBackdrop) sidebarBackdrop.classList.toggle("active", isOpen);
      });
    }

    if (sidebarBackdrop && appSidebar) {
      sidebarBackdrop.addEventListener("click", () => {
        appSidebar.classList.remove("mobile-open");
        sidebarBackdrop.classList.remove("active");
      });
    }

    // 0b. Tree Panel Collapse Toggle
    document.querySelectorAll(".tree-toggle-btn").forEach(treeBtn => {
      treeBtn.addEventListener("click", () => {
        window.elysiaAudio?.playClick();
        const treePanel = document.querySelector(".tree-panel");
        const workspaceGrid = document.getElementById("integrated-course-workspace");
        if (treePanel) {
          const isCollapsed = treePanel.classList.toggle("collapsed");
          if (workspaceGrid) workspaceGrid.classList.toggle("tree-collapsed", isCollapsed);
          treeBtn.textContent = isCollapsed ? "📖" : "⊞";
          treeBtn.title = isCollapsed ? "Expand chapters" : "Collapse chapters";
        }
      });
    });

    // 1. Sidebar Nav Destination buttons
    document.querySelectorAll(".side-nav-btn").forEach(btn => {
      btn.addEventListener("click", (e) => {
        const dest = e.currentTarget.dataset.dest;
        window.elysiaAudio?.playClick();

        document.querySelectorAll(".side-nav-btn").forEach(b => b.classList.remove("active"));
        e.currentTarget.classList.add("active");

        // Auto-close mobile drawer on destination click if on mobile viewport
        if (window.innerWidth <= 768 && appSidebar && appSidebar.classList.contains("mobile-open")) {
          appSidebar.classList.remove("mobile-open");
          if (sidebarBackdrop) sidebarBackdrop.classList.remove("active");
        }

        const viewport = document.getElementById("app-main-viewport");

        if (dest === "dashboard") {
          this.switchTab("learn");
          this.enterDashboardMode();
        } else if (dest === "course") {
          this.switchTab("learn");
          this.enterCourseMode();
        } else if (dest === "lab") {
          this.switchTab("learn");
          this.enterCourseMode();
          this.focusEditor();
        } else if (dest === "projects") {
          this.switchTab("learn");
          this.enterDashboardMode();
          document.getElementById("bottom-showcase-row")?.scrollIntoView({ behavior: "smooth" });
        } else if (dest === "mock") {
          this.switchTab("mock");
        } else if (dest === "handbook") {
          this.switchTab("handbook");
        } else if (dest === "xray") {
          this.switchTab("xray");
        } else if (dest === "viva") {
          this.switchTab("mock");
        } else if (dest === "records") {
          this.openModal("modal-lab-exporter");
        } else if (dest === "community") {
          this.openModal("modal-flex-card");
        }
      });
    });

    // 2. Hero Action Buttons
    const btnContinue = document.getElementById("btn-hero-continue");
    if (btnContinue) {
      btnContinue.addEventListener("click", () => {
        window.elysiaAudio?.playClick();
        this.enterCourseMode();
        this.focusEditor();
      });
    }

    const btnCurriculum = document.getElementById("btn-hero-curriculum");
    if (btnCurriculum) {
      btnCurriculum.addEventListener("click", () => {
        window.elysiaAudio?.playClick();
        this.enterCourseMode();
      });
    }

    const btnBackDash = document.getElementById("btn-back-dashboard");
    if (btnBackDash) {
      btnBackDash.addEventListener("click", () => {
        window.elysiaAudio?.playClick();
        this.enterDashboardMode();
      });
    }

    // 3. Quick Theme Toggle
    const btnThemeToggle = document.getElementById("btn-quick-theme-toggle");
    if (btnThemeToggle) {
      btnThemeToggle.textContent = this.currentTheme === 'light' ? '🌙' : '☀️';
      btnThemeToggle.addEventListener("click", () => this.toggleThemeQuick());
    }

    // 4. User Profile & Settings Triggers
    const btnHeroProf = document.getElementById("btn-hero-profile");
    if (btnHeroProf) {
      btnHeroProf.addEventListener("click", () => {
        window.elysiaAudio?.playClick();
        if (this.currentUser) this.openModal("modal-user-profile");
        else this.openModal("modal-auth");
      });
    }

    const sideUserChip = document.getElementById("side-user-profile-chip");
    if (sideUserChip) {
      sideUserChip.addEventListener("click", (e) => {
        if (e.target.id === "btn-side-settings") return;
        window.elysiaAudio?.playClick();
        if (this.currentUser) this.openModal("modal-user-profile");
        else this.openModal("modal-auth");
      });
    }

    const btnSideSettings = document.getElementById("btn-side-settings");
    if (btnSideSettings) {
      btnSideSettings.addEventListener("click", (e) => {
        e.stopPropagation();
        window.elysiaAudio?.playClick();
        if (this.currentUser) this.openEditProfile();
        else this.openModal("modal-auth");
      });
    }

    // 5. Global Search Bar & Keyboard Shortcut (Cmd+K / Ctrl+K)
    const heroSearch = document.getElementById("hero-global-search");
    if (heroSearch) {
      heroSearch.addEventListener("keydown", (e) => {
        if (e.key === "Enter" && heroSearch.value.trim()) {
          const query = heroSearch.value.trim().toLowerCase();
          // Filter tree or switch to doubt buster
          const treeSearch = document.getElementById("course-tree-search");
          if (treeSearch) {
            treeSearch.value = query;
            this.filterCourseTree(query);
            document.getElementById("integrated-course-workspace")?.scrollIntoView({ behavior: "smooth" });
          }
        }
      });

      window.addEventListener("keydown", (e) => {
        if ((e.metaKey || e.ctrlKey) && e.key === "k") {
          e.preventDefault();
          heroSearch.focus();
          heroSearch.select();
        }
      });
    }

    // 6. Tree Search Input
    const treeSearch = document.getElementById("course-tree-search");
    if (treeSearch) {
      treeSearch.addEventListener("input", (e) => {
        this.filterCourseTree(e.target.value.trim().toLowerCase());
      });
    }

    // 7. Quick Action Cards (Under Hero)
    const qaPractice = document.getElementById("qa-btn-practice");
    if (qaPractice) {
      qaPractice.addEventListener("click", () => {
        window.elysiaAudio?.playClick();
        this.focusEditor();
        document.getElementById("code-editor-textarea")?.scrollIntoView({ behavior: "smooth" });
      });
    }

    const qaQuiz = document.getElementById("qa-btn-quiz");
    if (qaQuiz) {
      qaQuiz.addEventListener("click", () => {
        window.elysiaAudio?.playClick();
        this.switchLessonSubtab("practice");
        document.getElementById("lesson-challenge-card")?.scrollIntoView({ behavior: "smooth" });
      });
    }

    const qaProject = document.getElementById("qa-btn-project");
    if (qaProject) {
      qaProject.addEventListener("click", () => {
        window.elysiaAudio?.playClick();
        this.loadProject("ch2_sub5_mini_project_chatbot");
      });
    }

    const qaHandbook = document.getElementById("qa-btn-handbook");
    if (qaHandbook) {
      qaHandbook.addEventListener("click", () => {
        this.switchTab("handbook");
      });
    }

    // 8. Next Topic card trigger
    const nextTopicBtn = document.getElementById("dash-next-topic-btn");
    if (nextTopicBtn) {
      nextTopicBtn.addEventListener("click", () => {
        this.nextSubtopic();
        document.getElementById("integrated-course-workspace")?.scrollIntoView({ behavior: "smooth" });
      });
    }

    // 9. Lesson Pill Tabs (Explanation, Examples, Hinglish, Practice, Quiz, Notes)
    document.querySelectorAll(".l-tab").forEach(tabBtn => {
      tabBtn.addEventListener("click", (e) => {
        const subtab = e.currentTarget.dataset.subtab;
        this.switchLessonSubtab(subtab);
      });
    });

    // 10. Snippet Run and Copy buttons
    const btnRunSnippet = document.getElementById("btn-run-snippet-code");
    if (btnRunSnippet) {
      btnRunSnippet.addEventListener("click", () => {
        const snippetEl = document.getElementById("lesson-snippet-code");
        if (snippetEl) {
          this.setCode(snippetEl.textContent);
          this.runCode();
        }
      });
    }

    const btnCopySnippet = document.getElementById("btn-copy-snippet");
    if (btnCopySnippet) {
      btnCopySnippet.addEventListener("click", () => {
        const snippetEl = document.getElementById("lesson-snippet-code");
        if (snippetEl) {
          navigator.clipboard.writeText(snippetEl.textContent);
          btnCopySnippet.textContent = "✓ Copied!";
          setTimeout(() => { btnCopySnippet.textContent = "📋 Copy"; }, 1500);
        }
      });
    }

    // 11. Try It Yourself Hint and Show Solution triggers
    const btnHint = document.getElementById("btn-show-hint");
    if (btnHint) {
      btnHint.addEventListener("click", () => {
        const ch = this.curriculumTree[this.currentChapterIdx];
        const sub = ch ? ch.subtopics[this.currentSubtopicIdx] : null;
        const hintText = (sub && sub.challenge && (sub.challenge.solution_explanation_en || sub.challenge.prompt_en)) 
          ? sub.challenge.solution_explanation_en 
          : "Try using the print() function with parentheses!";
        alert(`💡 Hint: ${hintText}`);
      });
    }

    const btnShowSol = document.getElementById("btn-show-solution");
    if (btnShowSol) {
      btnShowSol.addEventListener("click", () => {
        this.toggleSolution();
        document.getElementById("challenge-solution-box")?.scrollIntoView({ behavior: "smooth" });
      });
    }

    // 12. Fullscreen Editor Button
    const btnFullscreen = document.getElementById("btn-fullscreen-editor");
    if (btnFullscreen) {
      btnFullscreen.addEventListener("click", () => {
        const editorCard = document.querySelector(".editor-panel");
        if (editorCard) {
          editorCard.classList.toggle("fullscreen-mode");
          setTimeout(() => this.codeMirror?.refresh(), 50);
        }
      });
    }

    // Render tree accordion
    this.renderReferenceTree();
  }

  switchLessonSubtab(subtab) {
    window.elysiaAudio?.playClick();
    document.querySelectorAll(".l-tab").forEach(b => {
      b.classList.toggle("active", b.dataset.subtab === subtab);
    });

    const firstProgramBlock = document.getElementById("block-first-program");
    const theoryWrap = document.getElementById("block-theory-details");
    const challengeCard = document.getElementById("lesson-challenge-card");

    if (subtab === "examples") {
      if (firstProgramBlock) firstProgramBlock.style.display = "block";
      if (theoryWrap) theoryWrap.style.display = "none";
      if (challengeCard) challengeCard.style.display = "none";
    } else if (subtab === "practice" || subtab === "quiz") {
      if (firstProgramBlock) firstProgramBlock.style.display = "none";
      if (theoryWrap) theoryWrap.style.display = "none";
      if (challengeCard) challengeCard.style.display = "block";
    } else {
      // explanation, hinglish, notes
      if (firstProgramBlock) firstProgramBlock.style.display = "block";
      if (theoryWrap) theoryWrap.style.display = "block";
      if (challengeCard) challengeCard.style.display = "block";
    }
  }

  renderReferenceTree() {
    const treeContainer = document.getElementById("course-tree-accordion");
    if (!treeContainer) return;

    const parts = window.PYTHON_CURRICULUM_PARTS || [];
    if (parts.length === 0) return;

    let globalChIndex = 0;
    let html = "";

    parts.forEach((part, partIdx) => {
      const partNum = part.part_number;
      const partTitle = part.part_title.replace(/^PART\s*\d+\s*:\s*/i, '');
      const chapters = part.chapters || [];

      // Check if current chapter belongs to this part
      const isPartActive = this.curriculumTree[this.currentChapterIdx]?.part_number === partNum;

      html += `
        <div class="tree-part-group" data-part="${partNum}">
          <div class="tree-part-header" onclick="this.parentElement.classList.toggle('collapsed')">
            <span>▼ Part ${partNum}: ${partTitle}</span>
            <span class="tree-part-badge">0/${chapters.length}</span>
          </div>
          <div class="tree-chapters-list">
      `;

      chapters.forEach((ch) => {
        const thisChIndex = globalChIndex++;
        const isChapterActive = thisChIndex === this.currentChapterIdx;
        const subtopics = ch.subtopics || [];

        html += `
          <div class="tree-ch-item ${isChapterActive ? 'open' : ''}" data-ch-idx="${thisChIndex}">
            <div class="tree-ch-header" onclick="window.elysiaApp.selectChapter(${thisChIndex})">
              <span>${ch.title}</span>
              <span class="tree-part-badge">${isChapterActive ? `${this.currentSubtopicIdx + 1}/${subtopics.length}` : `0/${subtopics.length}`}</span>
            </div>
            <div class="tree-subtopics-list" style="${isChapterActive ? 'display:flex;' : 'display:none;'}">
        `;

        subtopics.forEach((sub, subIdx) => {
          const isSubActive = isChapterActive && subIdx === this.currentSubtopicIdx;
          html += `
            <div class="tree-sub-item ${isSubActive ? 'active' : ''}" onclick="window.elysiaApp.selectSubtopic(${thisChIndex}, ${subIdx})">
              <span>${isSubActive ? '●' : '○'}</span>
              <span>${sub.title}</span>
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

    treeContainer.innerHTML = html;
  }

  filterCourseTree(query) {
    const treeContainer = document.getElementById("course-tree-accordion");
    if (!treeContainer) return;

    if (!query) {
      this.renderReferenceTree();
      return;
    }

    const items = treeContainer.querySelectorAll(".tree-sub-item, .tree-ch-item, .tree-part-group");
    items.forEach(el => {
      const text = el.textContent.toLowerCase();
      if (text.includes(query)) {
        el.style.display = "";
        if (el.classList.contains("tree-ch-item")) {
          const subList = el.querySelector(".tree-subtopics-list");
          if (subList) subList.style.display = "flex";
        }
      } else {
        if (el.classList.contains("tree-sub-item")) {
          el.style.display = "none";
        }
      }
    });
  }

  loadProject(projectId) {
    window.elysiaAudio?.playClick();
    this.switchTab("learn");

    // Search across curriculum tree
    let foundCh = -1;
    let foundSub = -1;

    for (let c = 0; c < this.curriculumTree.length; c++) {
      const subs = this.curriculumTree[c].subtopics || [];
      for (let s = 0; s < subs.length; s++) {
        if (subs[s].id === projectId) {
          foundCh = c;
          foundSub = s;
          break;
        }
      }
      if (foundCh !== -1) break;
    }

    if (foundCh !== -1) {
      this.selectSubtopic(foundCh, foundSub);
      this.loadStarterCode();
      document.getElementById("integrated-course-workspace")?.scrollIntoView({ behavior: "smooth" });
      this.focusEditor();
    } else {
      // Default to chapter 2 chatbot project starter code
      this.setCode(`# Interactive Welcome Chatbot Project\nuser_name = input("Enter your name: ")\nprint(f"Hello, {user_name}! Welcome to Elysia Code!")\n`);
      this.focusEditor();
      document.getElementById("integrated-course-workspace")?.scrollIntoView({ behavior: "smooth" });
    }
  }


  // =========================================================================
  // PAGE 1: LEARN & CODE (Side-by-Side Split View)
  // =========================================================================

  /**
   * 📌 RENDER CURRENT LESSON: Screen par select huye topic ka pura data load karta hai
   * 👁️ WEB PAGE PE KYA DIKHTA HAI:
   *   - Left side: Topic title, Mental model analogy, Common traps (mistakes), aur Viva questions.
   *   - Right side: Starter python code aur 3D RAM memory visualizer.
   * 💡 KYUN USE KIYA:
   *   DOM elements (`document.getElementById`) ko grab karke unka `.textContent` 
   *   aur `.innerHTML` dynamically update karte hain taaki page bina refresh huye naya topic dikhaye.
   * ⚠️ AGAR CHANGE/DELETE KAREIN TO:
   *   Topic badalna band ho jayega aur purana topic hi screen par chipka rahega.
   */
  renderCurrentLesson() {
    const isPython = this.subject === "python";
    const navContainer = document.querySelector(".curriculum-nav-container");
    const topicSelectorStrip = document.getElementById("topic-selector-strip");
    const whyCard = document.querySelector(".why-card");
    const syntaxCard = document.querySelector(".syntax-card");
    const rulesCard = document.querySelector(".rules-card");

    if (isPython) {
      if (navContainer) navContainer.style.display = "flex";
      if (topicSelectorStrip) topicSelectorStrip.style.display = "none";
      if (whyCard) whyCard.style.display = "block";
      if (syntaxCard) syntaxCard.style.display = "block";
      if (rulesCard) rulesCard.style.display = "block";
      this.renderPythonCurriculumNav();
      this.renderCurrentSubtopic();
      return;
    }

    // HTML Track handling
    if (navContainer) navContainer.style.display = "none";
    if (topicSelectorStrip) topicSelectorStrip.style.display = "flex";
    if (whyCard) whyCard.style.display = "none";
    if (syntaxCard) syntaxCard.style.display = "none";
    if (rulesCard) rulesCard.style.display = "none";

    if (!this.curriculum || !this.curriculum[this.subject]) return;
    const topics = this.curriculum[this.subject].topics || [];
    if (topics.length === 0) return;

    const topic = topics[this.currentTopicIndex] || topics[0];
    const isHi = this.lang === "hi";

    // Render HTML topics in strip
    if (topicSelectorStrip) {
      topicSelectorStrip.innerHTML = topics.map((t, idx) => `
        <button class="topic-chip ${idx === this.currentTopicIndex ? 'active' : ''}" onclick="window.elysiaApp.selectTopic(${idx})">
          <span>${t.icon}</span> ${t.title}
        </button>
      `).join("");
    }

    // Update Header
    const chapterTag = document.getElementById("lesson-chapter-tag");
    const durationTag = document.getElementById("lesson-duration-tag");
    const xpBadge = document.getElementById("lesson-xp-badge");
    const titleEl = document.getElementById("lesson-title");

    if (chapterTag) chapterTag.textContent = `${topic.tag} • WEB DEV`;
    if (durationTag) durationTag.textContent = `⏱️ ${topic.duration}`;
    if (xpBadge) xpBadge.textContent = `⚡ +50 XP`;
    if (titleEl) titleEl.innerHTML = `<span>${topic.icon}</span> ${topic.title}`;

    const whatEl = document.getElementById("lesson-what") || document.getElementById("lesson-concept");
    const analogyEl = document.getElementById("lesson-analogy");
    if (whatEl) whatEl.textContent = isHi ? topic.intro_hi : topic.intro_en;
    if (analogyEl) analogyEl.textContent = isHi ? topic.use_case_hi : topic.use_case_en;

    this.setCode(topic.starter_code || "");

    if (window.htmlRunner) {
      const frame = document.getElementById("html-preview-frame");
      window.htmlRunner.setIframe(frame);
      window.htmlRunner.render(topic.starter_code || "");
    }
  }

  /**
   * 📌 RENDER PYTHON CURRICULUM NAV: Chapter & Subtopic Pills render karta hai
   */
  renderPythonCurriculumNav() {
    const chStrip = document.getElementById("chapter-selector-strip");
    const subStrip = document.getElementById("subtopic-selector-strip");
    if (!chStrip || !subStrip) return;

    if (!this.curriculumTree || this.curriculumTree.length === 0) {
      this.curriculumTree = window.PYTHON_CURRICULUM_TREE || [];
    }
    if (this.curriculumTree.length === 0) return;

    if (this.currentChapterIdx >= this.curriculumTree.length) {
      this.currentChapterIdx = 0;
    }

    // 1. Render Chapter Pills
    chStrip.innerHTML = this.curriculumTree.map((ch, idx) => `
      <button class="chapter-pill ${idx === this.currentChapterIdx ? 'active' : ''}" onclick="window.elysiaApp.selectChapter(${idx})">
        <span>${ch.icon}</span> ${ch.title}
      </button>
    `).join("");

    // 2. Render Subtopic Pills
    const ch = this.curriculumTree[this.currentChapterIdx];
    const subtopics = ch.subtopics || [];

    if (this.currentSubtopicIdx >= subtopics.length) {
      this.currentSubtopicIdx = 0;
    }

    subStrip.innerHTML = subtopics.map((sub, idx) => {
      const isCompleted = this.completedSubtopics.has(sub.id);
      const isActive = idx === this.currentSubtopicIdx;
      return `
        <button class="subtopic-pill ${isActive ? 'active' : ''} ${isCompleted ? 'completed' : ''}" onclick="window.elysiaApp.selectSubtopic(${this.currentChapterIdx}, ${idx})">
          <span>${sub.icon}</span> ${this.lang === "hi" ? (sub.title_hi || sub.title) : sub.title}
        </button>
      `;
    }).join("");
  }

  /**
   * 📌 RENDER CURRENT SUBTOPIC: Active subtopic ki theory, mental model, examples aur challenge dikhata hai
   */
  renderCurrentSubtopic() {
    if (!this.curriculumTree || this.curriculumTree.length === 0) {
      this.curriculumTree = window.PYTHON_CURRICULUM_TREE || [];
    }
    const ch = this.curriculumTree[this.currentChapterIdx];
    if (!ch) return;
    const subtopics = ch.subtopics || [];
    const sub = subtopics[this.currentSubtopicIdx] || subtopics[0];
    if (!sub) return;

    const isHi = this.lang === "hi";

    // Subtopic Metadata Tags
    const chapterTag = document.getElementById("lesson-chapter-tag");
    const durationTag = document.getElementById("lesson-duration-tag");
    const xpBadge = document.getElementById("lesson-xp-badge");
    const titleEl = document.getElementById("lesson-title");

    if (chapterTag) chapterTag.textContent = `${ch.title.toUpperCase()}`;
    if (durationTag) durationTag.textContent = `⏱️ ${sub.duration || '5 mins'}`;
    if (xpBadge) xpBadge.textContent = `⚡ +${sub.xp || 50} XP`;
    if (titleEl) titleEl.innerHTML = `<span>${sub.icon}</span> ${isHi ? (sub.title_hi || sub.title) : sub.title}`;

    // 1. What is it / Kya Hai Ye
    const whatEl = document.getElementById("lesson-what") || document.getElementById("lesson-concept");
    if (whatEl) {
      whatEl.textContent = isHi ? (sub.what_is_it_hi || sub.concept_hi || sub.what_is_it_en) : (sub.what_is_it_en || sub.concept_en || sub.what_is_it_hi);
    }

    // 2. Why Do We Need It / Kyun Use Hota Hai
    const whyEl = document.getElementById("lesson-why");
    if (whyEl) {
      whyEl.textContent = isHi ? (sub.why_need_it_hi || sub.why_need_it_en || "") : (sub.why_need_it_en || sub.why_need_it_hi || "");
    }

    // 3. How To Use It / Syntax & Blueprint
    const syntaxEl = document.getElementById("lesson-syntax");
    const howEl = document.getElementById("lesson-how");
    if (syntaxEl) syntaxEl.textContent = sub.syntax || "";
    if (howEl) {
      howEl.textContent = isHi ? (sub.how_to_use_hi || sub.how_to_use_en || "") : (sub.how_to_use_en || sub.how_to_use_hi || "");
    }

    // 4. Golden Rules & Compiler Laws / Sunehre Niyam (List formatting)
    const rulesListEl = document.getElementById("lesson-rules-list");
    if (rulesListEl) {
      const rules = isHi ? (sub.rules_hi || sub.rules_en || []) : (sub.rules_en || sub.rules_hi || []);
      rulesListEl.innerHTML = rules.map(r => `<li>${r}</li>`).join("");
    }

    // 5. Core Concept & Relatable Mental Model
    const analogyEl = document.getElementById("lesson-analogy");
    if (analogyEl) analogyEl.textContent = isHi ? (sub.analogy_hi || sub.analogy_en) : sub.analogy_en;

    // Example 1 (Core Concept)
    const ex1Title = document.getElementById("example-1-title");
    const ex1Code = document.getElementById("example-1-code");
    const ex1Expl = document.getElementById("example-1-expl");
    if (sub.example_1) {
      if (ex1Title) ex1Title.textContent = isHi ? (sub.example_1.title_hi || sub.example_1.title) : sub.example_1.title;
      if (ex1Code) ex1Code.textContent = sub.example_1.code;
      if (ex1Expl) ex1Expl.textContent = isHi ? (sub.example_1.explanation_hi || sub.example_1.explanation_en) : sub.example_1.explanation_en;
    }

    // Example 2 (Real World Use Case)
    const ex2Title = document.getElementById("example-2-title");
    const ex2Code = document.getElementById("example-2-code");
    const ex2Expl = document.getElementById("example-2-expl");
    if (sub.example_2) {
      if (ex2Title) ex2Title.textContent = isHi ? (sub.example_2.title_hi || sub.example_2.title) : sub.example_2.title;
      if (ex2Code) ex2Code.textContent = sub.example_2.code;
      if (ex2Expl) ex2Expl.textContent = isHi ? (sub.example_2.explanation_hi || sub.example_2.explanation_en) : sub.example_2.explanation_en;
    }

    // Interactive Challenge Card
    const promptEl = document.getElementById("challenge-prompt");
    const expectedEl = document.getElementById("challenge-expected-output");
    const rewardEl = document.getElementById("challenge-reward-badge");
    const solCodeDisplay = document.getElementById("solution-code-display");
    const solExplDisplay = document.getElementById("solution-explanation-text");
    const solBox = document.getElementById("challenge-solution-box");

    if (sub.challenge) {
      if (promptEl) promptEl.textContent = isHi ? (sub.challenge.prompt_hi || sub.challenge.prompt_en) : sub.challenge.prompt_en;
      if (expectedEl) expectedEl.textContent = sub.challenge.expected_output || "";
      if (rewardEl) rewardEl.textContent = `Earn +${sub.xp || 50} XP`;
      if (solCodeDisplay) solCodeDisplay.textContent = sub.challenge.solution_code || "";
      if (solExplDisplay) solExplDisplay.textContent = isHi ? (sub.challenge.solution_explanation_hi || "") : (sub.challenge.solution_explanation_en || sub.challenge.solution_explanation_hi || "");
    }
    if (solBox) solBox.classList.add("hidden");

    // 🏛️ Synchronize Reference UI Elements
    const bcPart = document.getElementById("lesson-bc-part");
    const bcCh = document.getElementById("lesson-bc-ch");
    const bcSub = document.getElementById("lesson-bc-sub");
    if (bcPart) bcPart.textContent = `Part ${ch.part_number || 1}`;
    if (bcCh) bcCh.textContent = `Chapter ${ch.chapter_number || (this.currentChapterIdx + 1)}`;
    if (bcSub) bcSub.textContent = isHi ? (sub.title_hi || sub.title) : sub.title;

    const summaryEl = document.getElementById("lesson-active-summary");
    if (summaryEl) {
      summaryEl.textContent = isHi ? (sub.concept_hi || sub.what_is_it_hi || sub.concept_en) : (sub.concept_en || sub.what_is_it_en);
    }

    const circleFraction = document.getElementById("lesson-circle-fraction");
    if (circleFraction) {
      circleFraction.textContent = `${this.currentSubtopicIdx + 1}/${(ch.subtopics || []).length}`;
    }

    const snippetCode = document.getElementById("lesson-snippet-code");
    const snippetOut = document.getElementById("lesson-snippet-output");
    const blockTitle = document.getElementById("lesson-block-title");
    const blockDesc = document.getElementById("lesson-block-desc");

    if (blockTitle) {
      if (sub.example_1 && (sub.example_1.title_hi || sub.example_1.title)) {
        blockTitle.textContent = isHi ? (sub.example_1.title_hi || sub.example_1.title) : (sub.example_1.title || sub.example_1.title_hi);
      } else {
        blockTitle.textContent = isHi ? `🧪 Code Demo: ${sub.title_hi || sub.title}` : `🧪 Code Demo: ${sub.title}`;
      }
    }
    if (blockDesc) {
      if (sub.example_1 && (sub.example_1.explanation_hi || sub.example_1.explanation_en)) {
        blockDesc.textContent = isHi ? (sub.example_1.explanation_hi || sub.example_1.explanation_en) : (sub.example_1.explanation_en || sub.example_1.explanation_hi);
      } else {
        blockDesc.textContent = isHi ? "Neeche diye gaye code ko samjhein aur run karke dekhein:" : "Inspect and run the example code below:";
      }
    }

    if (sub.example_1 && snippetCode) {
      snippetCode.textContent = sub.example_1.code || 'print("Hello, World!")';
    }
    if (snippetOut) {
      snippetOut.textContent = (sub.challenge && sub.challenge.expected_output) || 'Hello, World!';
    }

    const focusPill = document.getElementById("focus-chapter-pill");
    if (focusPill) {
      focusPill.textContent = `Part ${ch.part_number || 1} • Chapter ${ch.chapter_number || (this.currentChapterIdx + 1)}: ${sub.title}`;
    }

    const tipText = document.getElementById("lesson-tip-text");
    if (tipText) {
      const rules = isHi ? (sub.rules_hi || sub.rules_en || []) : (sub.rules_en || sub.rules_hi || []);
      if (rules.length > 0) tipText.textContent = rules[0];
    }

    const tryPrompt = document.getElementById("try-prompt-text");
    if (tryPrompt) {
      tryPrompt.textContent = (sub.challenge && (isHi ? sub.challenge.prompt_hi : sub.challenge.prompt_en)) || "Modify the code to print your own name.";
    }

    // Dashboard Metric Cards update
    const dashPartBadge = document.getElementById("dash-part-badge");
    const dashChTitle = document.getElementById("dash-chapter-title");
    const dashTopicsCount = document.getElementById("dash-topics-count");
    const dashChFill = document.getElementById("dash-chapter-fill");
    const dashNextTitle = document.getElementById("dash-next-title");

    if (dashPartBadge) dashPartBadge.textContent = `Part ${ch.part_number || 1}`;
    if (dashChTitle) dashChTitle.textContent = ch.title;
    if (dashTopicsCount) dashTopicsCount.textContent = `${this.currentSubtopicIdx + 1} / ${(ch.subtopics || []).length} topics`;
    if (dashChFill) {
      const pct = Math.round(((this.currentSubtopicIdx + 1) / (ch.subtopics || [1]).length) * 100);
      dashChFill.style.width = `${pct}%`;
    }

    const nextSub = ch.subtopics[this.currentSubtopicIdx + 1] || (this.curriculumTree[this.currentChapterIdx + 1]?.subtopics[0]);
    if (dashNextTitle && nextSub) {
      dashNextTitle.innerHTML = `${nextSub.title}`;
    }

    // Sync tree accordion highlights
    this.renderReferenceTree();


    // Ego Roast & Motivation Banner
    const egoText = document.getElementById("ego-roast-text");
    const egoTitle = document.getElementById("ego-roast-title");
    if (egoText) {
      const isCompleted = this.completedSubtopics.has(sub.id);
      if (isCompleted && sub.challenge && sub.challenge.ego_cheer_hi) {
        egoText.textContent = sub.challenge.ego_cheer_hi;
        if (egoTitle) egoTitle.textContent = "Senior Bhaiya Ka Salute: 🏆";
      } else if (sub.challenge && sub.challenge.ego_roast_hi) {
        egoText.textContent = sub.challenge.ego_roast_hi;
        if (egoTitle) egoTitle.textContent = "Senior Bhaiya Ka Challenge: 🔥";
      }
    }

    // Counter Indicator
    const counterEl = document.getElementById("subtopic-counter-indicator");
    const totalSub = this.getTotalSubtopicsCount();
    const currentGlobal = this.getCurrentGlobalSubtopicIndex();
    if (counterEl) {
      counterEl.textContent = `Subtopic ${currentGlobal} of ${totalSub}`;
    }

    this.setCode((sub.challenge && sub.challenge.starter_code) || "# Type your Python code here:\n");

    // Terminal Status
    const stdoutEl = document.getElementById("terminal-stdout");
    const stderrEl = document.getElementById("terminal-stderr");
    if (stdoutEl) stdoutEl.textContent = "Terminal ready. Click 'Run Code' or 'Submit & Test' to test your logic!";
    if (stderrEl) stderrEl.textContent = "";

    // Save Position
    localStorage.setItem("elysia_ch_idx", this.currentChapterIdx.toString());
    localStorage.setItem("elysia_sub_idx", this.currentSubtopicIdx.toString());
  }

  selectChapter(chIdx) {
    window.elysiaAudio.playClick();
    this.currentChapterIdx = chIdx;
    this.currentSubtopicIdx = 0;
    this.renderPythonCurriculumNav();
    this.renderCurrentSubtopic();
  }

  selectSubtopic(chIdx, subIdx) {
    window.elysiaAudio.playClick();
    this.currentChapterIdx = chIdx;
    this.currentSubtopicIdx = subIdx;
    this.renderPythonCurriculumNav();
    this.renderCurrentSubtopic();
  }

  prevSubtopic() {
    window.elysiaAudio.playClick();
    if (this.currentSubtopicIdx > 0) {
      this.currentSubtopicIdx--;
    } else if (this.currentChapterIdx > 0) {
      this.currentChapterIdx--;
      const prevCh = this.curriculumTree[this.currentChapterIdx];
      this.currentSubtopicIdx = Math.max(0, (prevCh.subtopics || []).length - 1);
    }
    this.renderPythonCurriculumNav();
    this.renderCurrentSubtopic();
  }

  nextSubtopic() {
    window.elysiaAudio.playClick();
    const ch = this.curriculumTree[this.currentChapterIdx];
    if (ch && this.currentSubtopicIdx < (ch.subtopics || []).length - 1) {
      this.currentSubtopicIdx++;
    } else if (this.currentChapterIdx < this.curriculumTree.length - 1) {
      this.currentChapterIdx++;
      this.currentSubtopicIdx = 0;
    }
    this.renderPythonCurriculumNav();
    this.renderCurrentSubtopic();
  }

  focusEditor() {
    if (this.codeMirror) this.codeMirror.focus();
    else {
      const el = document.getElementById("code-editor-textarea");
      if (el) el.focus();
    }
  }

  loadStarterCode() {
    window.elysiaAudio.playClick();
    const ch = this.curriculumTree[this.currentChapterIdx];
    const sub = ch ? ch.subtopics[this.currentSubtopicIdx] : null;
    if (sub && sub.challenge) {
      this.setCode(sub.challenge.starter_code || "");
      this.focusEditor();
    }
  }

  tryExample(num) {
    window.elysiaAudio.playClick();
    const ch = this.curriculumTree[this.currentChapterIdx];
    const sub = ch ? ch.subtopics[this.currentSubtopicIdx] : null;
    if (!sub) return;
    if (num === 1 && sub.example_1) {
      this.setCode(sub.example_1.code || "");
    } else if (num === 2 && sub.example_2) {
      this.setCode(sub.example_2.code || "");
    }
    this.focusEditor();
  }

  toggleSolution() {
    window.elysiaAudio.playClick();
    const solBox = document.getElementById("challenge-solution-box");
    if (solBox) {
      solBox.classList.toggle("hidden");
    }
  }

  copySolution() {
    window.elysiaAudio.playClick();
    const ch = this.curriculumTree[this.currentChapterIdx];
    const sub = ch ? ch.subtopics[this.currentSubtopicIdx] : null;
    if (sub && sub.challenge && sub.challenge.solution_code) {
      this.setCode(sub.challenge.solution_code);
      this.focusEditor();
    }
  }

  selectTopic(index) {
    this.currentTopicIndex = index;
    window.elysiaAudio.playClick();
    this.renderCurrentLesson();
  }

  renderMemoryTrace(trace) {
    const memContainer = document.getElementById("memory-grid");
    if (!memContainer) return;
    if (!trace || trace.length === 0) {
      memContainer.innerHTML = `<span style="font-size:0.8rem; color:#64748b;">No active memory variables</span>`;
      return;
    }
    const latest = trace[trace.length - 1];
    memContainer.innerHTML = Object.entries(latest.vars || {}).map(([k, v]) => `
      <div class="var-box-3d">
        <div class="var-name">${k}</div>
        <div class="var-val">${Array.isArray(v) ? JSON.stringify(v) : v}</div>
      </div>
    `).join("");
  }

  /**
   * 📌 RUN CODE: Instant Sub-15ms Python Execution Engine with Interactive Stdin Support
   */
  async runCode(providedStdin = null) {
    window.elysiaAudio.playClick();
    const code = this.getCode();
    const stdoutEl = document.getElementById("terminal-stdout");
    const stderrEl = document.getElementById("terminal-stderr");
    const seniorBox = document.getElementById("senior-advice-bubble");
    const inputBar = document.getElementById("terminal-input-bar");
    const stdinInput = document.getElementById("terminal-stdin-input");

    // Ensure output tab is active if user was on REPL tab
    const tabOutput = document.getElementById("term-tab-output");
    const tabRepl = document.getElementById("term-tab-repl");
    const viewOutput = document.getElementById("terminal-output-view");
    const viewRepl = document.getElementById("terminal-repl-view");
    if (tabOutput && tabRepl && viewOutput && viewRepl && viewRepl.style.display !== "none") {
      tabOutput.classList.add("active");
      tabRepl.classList.remove("active");
      viewOutput.style.display = "block";
      viewRepl.style.display = "none";
    }

    if (stdoutEl) stdoutEl.textContent = "⚡ Running execution...";
    if (stderrEl) stderrEl.textContent = "";
    if (seniorBox) seniorBox.classList.remove("active");

    if (this.subject === "html") {
      const frame = document.getElementById("html-preview-frame");
      window.htmlRunner.setIframe(frame);
      window.htmlRunner.render(code);
      if (stdoutEl) stdoutEl.textContent = "✅ HTML Rendered into live viewport.";
      return { stdout: "HTML Rendered", stderr: "" };
    }

    let stdinVal = providedStdin;
    if (stdinVal === null && code.includes("input(")) {
      if (inputBar && stdinInput && stdinInput.value.trim()) {
        stdinVal = stdinInput.value;
      } else {
        if (inputBar) inputBar.style.display = "flex";
        const promptRes = window.prompt("🐍 Python input() prompt:\nType the input value you want to send to the program (e.g. Priyanshu or 25):");
        if (promptRes !== null) {
          stdinVal = promptRes;
          if (stdinInput) stdinInput.value = promptRes;
        }
      }
    }

    // First time the browser loads Pyodide WebAssembly
    if (stdoutEl && this.execEngine === "pyodide" && window.pyodideManager && !window.pyodideManager.isReady) {
      stdoutEl.textContent = "\u23F3 Loading Pyodide WebAssembly engine (first time only, a few seconds)...";
    }
    const runResult = await this.runPythonCode(code, stdinVal || "", 4.0);
    let stdout = runResult.stdout;
    let stderr = runResult.stderr;

    if (stderr) {
      window.elysiaAudio.playError();
      if (stdoutEl) stdoutEl.innerHTML = this._ansiToHtml(stdout);
      if (stderrEl) stderrEl.innerHTML = this._formatTracebackHtml(stderr);
      this.decodeErrorWithSenior(stderr);
    } else {
      window.elysiaAudio.playSuccess();
      if (stdoutEl) stdoutEl.innerHTML = this._ansiToHtml(stdout || "[Executed with no console output]");
      if (stderrEl) stderrEl.innerHTML = "";
    }

    if (code.includes("input(")) {
      if (inputBar) inputBar.style.display = "flex";
      if (stdinInput) {
        stdinInput.placeholder = "Enter next input value...";
        stdinInput.focus();
      }
    } else {
      if (inputBar) inputBar.style.display = "none";
    }

    return { stdout, stderr };
  }

  /**
   * ⚡ INITIALIZE PYODIDE WEBENGINE
   */
  _initPyodideEngine() {
    const engineSelect = document.getElementById("select-exec-engine");
    const statusBadge = document.getElementById("pyodide-status-badge");
    const terminalEngineTag = document.getElementById("terminal-engine-tag");

    if (engineSelect) {
      engineSelect.value = this.execEngine;
      engineSelect.addEventListener("change", (e) => {
        this.execEngine = e.target.value;
        localStorage.setItem("elysia_exec_engine", this.execEngine);
        if (terminalEngineTag) {
          terminalEngineTag.textContent = this.execEngine === "pyodide" ? "⚡ Pyodide WASM" : "🖥️ Server Python";
        }
      });
    }

    if (terminalEngineTag) {
      terminalEngineTag.textContent = this.execEngine === "pyodide" ? "⚡ Pyodide WASM" : "🖥️ Server Python";
    }

    const setBadgeReady = () => {
      if (!statusBadge) return;
      statusBadge.textContent = "● Ready";
      statusBadge.style.background = "rgba(16, 185, 129, 0.15)";
      statusBadge.style.color = "#6ee7b7";
      statusBadge.style.borderColor = "rgba(16, 185, 129, 0.3)";
      statusBadge.title = "Pyodide WebAssembly is active and ready in browser";
    };

    const setBadgeError = (err) => {
      if (!statusBadge) return;
      statusBadge.textContent = "⚠️ Offline";
      statusBadge.style.background = "rgba(244, 63, 94, 0.15)";
      statusBadge.style.color = "#fda4af";
      statusBadge.style.borderColor = "rgba(244, 63, 94, 0.3)";
      statusBadge.title = `Pyodide load issue: ${err || "Check connection"}`;
    };

    window.addEventListener("pyodide:ready", setBadgeReady);
    window.addEventListener("pyodide:error", (e) => setBadgeError(e.detail));

    // Preload Pyodide engine immediately
    if (window.pyodideManager) {
      if (window.pyodideManager.isReady) {
        setBadgeReady();
      } else {
        window.pyodideManager.init().then(setBadgeReady).catch(setBadgeError);
      }
    }
  }

  /**
   * Does this server allow running code on the SERVER? (Only on localhost by default.)
   * On a public site it answers false and every program runs in the browser instead.
   */
  async _serverExecEnabled() {
    if (this._serverExec === undefined) {
      try {
        const r = await fetch("/api/config");
        const j = await r.json();
        this._serverExec = !!j.server_exec;
      } catch (e) {
        this._serverExec = false;
      }
    }
    return this._serverExec;
  }

  /**
   * ONE place that runs Python. Returns { stdout, stderr }.
   * Pyodide WebAssembly Web Worker by default, with option to use Local Server.
   */
  async runPythonCode(code, stdin, timeoutSec) {
    const engine = this.execEngine || "pyodide";
    const terminalEngineTag = document.getElementById("terminal-engine-tag");

    // 1. If user explicitly chose server AND server execution is permitted:
    if (engine === "server" && (await this._serverExecEnabled())) {
      if (terminalEngineTag) terminalEngineTag.textContent = "🖥️ Server Python";
      try {
        const resp = await fetch("/api/execute", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ code: code, stdin: stdin || "", timeout: timeoutSec })
        });
        if (resp.ok) {
          const data = await resp.json();
          let stderr = data.stderr || "";
          if (data.status === "timeout") {
            stderr = `\u23F1\uFE0F Execution timed out (>${timeoutSec}s)! Infinite loop detected.`;
          }
          return { stdout: data.stdout || "", stderr: stderr };
        }
        if (resp.status === 403) this._serverExec = false;   // server says "disabled" -> use browser
      } catch (e) {
        // server not reachable -> browser engine below
      }
    }

    // 2. Default & Preferred: Run inside Pyodide WebAssembly Web Worker
    if (terminalEngineTag) terminalEngineTag.textContent = "⚡ Pyodide WASM";
    const r = await window.pyodideManager.run(code, stdin || "", timeoutSec * 1000);
    return { stdout: r.stdout || "", stderr: r.stderr || r.error || "" };
  }

  /**
   * 📌 SUBMIT CODE: Instant Challenge Verification + XP Reward + Confetti
   */
  async submitCode() {
    window.elysiaAudio.playClick();
    const result = await this.runCode();
    if (!result) return;

    const stdoutEl = document.getElementById("terminal-stdout");
    const stderrEl = document.getElementById("terminal-stderr");
    const egoText = document.getElementById("ego-roast-text");
    const egoTitle = document.getElementById("ego-roast-title");

    if (this.subject === "html") {
      const frame = document.getElementById("html-preview-frame");
      window.htmlRunner.setIframe(frame);
      window.htmlRunner.render(this.getCode());
      const val = window.htmlRunner.validateElements(["h1"]);
      if (val.valid) {
        window.elysiaAudio.playSuccess();
        this.launchConfetti();
        if (stdoutEl) stdoutEl.textContent = "🎉 HTML Verified! 100% Passed.";
      } else {
        window.elysiaAudio.playError();
        if (stderrEl) stderrEl.textContent = `Missing elements: ${val.missing.join(", ")}`;
      }
      return;
    }

    const ch = this.curriculumTree[this.currentChapterIdx];
    const sub = ch ? ch.subtopics[this.currentSubtopicIdx] : null;
    if (!sub || !sub.challenge) return;

    const expected = (sub.challenge.expected_output || "").trim();
    const actual = (result.stdout || "").trim();

    if (result.stderr) {
      if (egoText && sub.challenge.ego_roast_hi) {
        egoText.textContent = sub.challenge.ego_roast_hi;
        if (egoTitle) egoTitle.textContent = "Senior Bhaiya: ⚠️ Syntax Error!";
      }
      return;
    }

    if (actual === expected || (expected && actual.includes(expected))) {
      window.elysiaAudio.playSuccess();
      this.launchConfetti();

      const earnedXP = sub.xp || 50;
      if (!this.completedSubtopics.has(sub.id)) {
        this.completedSubtopics.add(sub.id);
        this.addXP(earnedXP);
        localStorage.setItem("elysia_completed_subtopics", JSON.stringify(Array.from(this.completedSubtopics)));
      }

      if (stdoutEl) {
        stdoutEl.textContent = `${result.stdout}\n\n🏆 ALL TEST CASES PASSED! (+${earnedXP} XP Earned!)\n${sub.challenge.ego_cheer_hi || 'Great job!'}`;
      }
      if (egoText && sub.challenge.ego_cheer_hi) {
        egoText.textContent = sub.challenge.ego_cheer_hi;
        if (egoTitle) egoTitle.textContent = "Senior Bhaiya Ka Salute: 🏆";
      }

      this.renderPythonCurriculumNav();
      this.updateGamificationUI();
    } else {
      window.elysiaAudio.playError();
      if (stderrEl) {
        stderrEl.textContent = `❌ Output Mismatch!\nExpected Output: "${expected}"\nYour Code Output: "${actual}"\nHint: Check quotes, spelling, and whitespace!`;
      }
      if (egoText && sub.challenge.ego_roast_hi) {
        egoText.textContent = sub.challenge.ego_roast_hi;
        if (egoTitle) egoTitle.textContent = "Senior Bhaiya Ka Roast: 😅";
      }
    }
  }

  /**
   * 📌 DECODE ERROR WITH SENIOR: Python traceback ko student-friendly Hinglish me convert karta hai (Groq AI powered)
   * 👁️ Web Page Pe Effect: Screen par floating golden bubble khulta hai jo batata hai ki galti kahan hui.
   */
  async decodeErrorWithSenior(rawError) {
    try {
      const currentCode = this.getCode();
      const res = await fetch("/api/decode-error", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ error: rawError, lang: this.lang, code: currentCode })
      });
      const data = await res.json();
      const seniorBox = document.getElementById("senior-advice-bubble");
      if (seniorBox) {
        seniorBox.classList.add("active");
        const titleLabel = data.ai_powered ? "⚡ Senior AI Error Diagnosis" : (data.title || "Code Error");
        seniorBox.innerHTML = `<span>💡</span> <div><strong>${titleLabel}:</strong> ${data.advice}</div>`;
        seniorBox.scrollIntoView({ behavior: "smooth", block: "nearest" });
      }
    } catch (e) {
      console.warn("Decode error fallback", e);
    }
  }

  /**
   * 📌 FIND ERRORS (AI): Analyzes current code in editor before execution and finds bugs/improvements.
   */
  async findErrorsWithAI() {
    const currentCode = this.getCode().trim();
    const seniorBox = document.getElementById("senior-advice-bubble");
    const btn = document.getElementById("btn-ai-find-errors");

    if (!currentCode) {
      if (seniorBox) {
        seniorBox.classList.add("active");
        seniorBox.innerHTML = `<span>⚠️</span> <div><strong>Editor Khali Hai:</strong> Pehle kuch Python code likho ya challenge load karo!</div>`;
        seniorBox.scrollIntoView({ behavior: "smooth", block: "nearest" });
      }
      return;
    }

    if (btn) {
      btn.disabled = true;
      btn.textContent = "⏳ Analyzing...";
    }

    if (seniorBox) {
      seniorBox.classList.add("active");
      seniorBox.innerHTML = `<span>⚡</span> <div><strong>Groq Senior AI:</strong> Tera code analyze kar raha hoon, bas 1 second ruko...</div>`;
      seniorBox.scrollIntoView({ behavior: "smooth", block: "nearest" });
    }

    try {
      const res = await fetch("/api/decode-error", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          error: "Analyze this Python code. Check for any syntax errors, indentation issues, wrong types, infinite loops, or logical mistakes. If there are mistakes, explain where and why using an intuitive analogy. If the code is correct and clean, confirm that it looks solid!",
          lang: this.lang,
          code: currentCode
        })
      });
      const data = await res.json();
      if (seniorBox) {
        seniorBox.classList.add("active");
        const titleLabel = data.ai_powered ? "⚡ Senior AI Error Diagnosis" : (data.title || "AI Error Diagnosis");
        seniorBox.innerHTML = `<span>💡</span> <div><strong>${titleLabel}:</strong> ${data.advice}</div>`;
        seniorBox.scrollIntoView({ behavior: "smooth", block: "nearest" });
      }
      if (window.elysiaAudio) window.elysiaAudio.playChord();
    } catch (err) {
      if (seniorBox) {
        seniorBox.innerHTML = `<span>❌</span> <div><strong>Network Error:</strong> AI response fetch karne me dikkat aayi. Check your connection.</div>`;
      }
    } finally {
      if (btn) {
        btn.disabled = false;
        btn.textContent = "🔍 Find Errors (AI)";
      }
    }
  }

  /**
   * 📌 TOGGLE AI TUTOR DRAWER
   */
  toggleAITutor(forceOpen = null) {
    const drawer = document.getElementById("ai-tutor-drawer");
    if (!drawer) return;
    const shouldOpen = forceOpen !== null ? forceOpen : !drawer.classList.contains("open");
    if (shouldOpen) {
      drawer.classList.add("open");
      const input = document.getElementById("ai-chat-input");
      if (input) setTimeout(() => input.focus(), 150);
    } else {
      drawer.classList.remove("open");
    }
  }

  /**
   * 📌 QUICK ASK AI (Prompt Chips)
   */
  quickAskAI(type) {
    this.toggleAITutor(true);
    const currentCode = this.getCode().trim();
    const activeSub = this.activeSubtopicData || {};
    const topicTitle = activeSub.title || "Python Programming";

    if (type === "debug") {
      if (!currentCode) {
        this._appendAIChatMessage("bot", "Editor me abhi koi code nahi hai bhai! Pehle editor me apna Python code likho ya koi lesson kholo.");
        return;
      }
      this._appendAIChatMessage("user", "Mera editor ka code check karo aur batao kya koi error ya improvement hai?");
      this._callAITutorAPI("Check this code for any syntax, indentation, type, or logic bugs. Explain where the problem is and guide me how to fix it.", currentCode, topicTitle);
    } else if (type === "explain") {
      this._appendAIChatMessage("user", `Mujhe "${topicTitle}" simple Hinglish me samjhao.`);
      this._callAITutorAPI(`Explain the concept of "${topicTitle}" to a complete beginner in simple, friendly Hinglish with real-world intuition.`, currentCode, topicTitle);
    } else if (type === "analogy") {
      this._appendAIChatMessage("user", `"${topicTitle}" ke liye ek hostel/college life analogy do.`);
      this._callAITutorAPI(`Give a funny and memorable everyday college/hostel life analogy to explain "${topicTitle}".`, currentCode, topicTitle);
    }
  }

  /**
   * 📌 SEND AI CHAT MESSAGE
   */
  async sendAIChat() {
    const input = document.getElementById("ai-chat-input");
    if (!input) return;
    const text = input.value.trim();
    if (!text) return;
    input.value = "";

    const currentCode = this.getCode().trim();
    const activeSub = this.activeSubtopicData || {};
    const topicTitle = activeSub.title || "Python Basics";

    this._appendAIChatMessage("user", text);
    await this._callAITutorAPI(text, currentCode, topicTitle);
  }

  _appendAIChatMessage(sender, text) {
    const container = document.getElementById("ai-chat-messages");
    if (!container) return;
    const msgDiv = document.createElement("div");
    msgDiv.className = `ai-msg ai-msg-${sender}`;
    const avatar = sender === "bot" ? "🤖" : "👤";
    
    let formatted = String(text)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
      .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
      .replace(/```python([\s\S]*?)```/g, "<pre style='background:#0f172a; padding:8px; border-radius:6px; margin:6px 0; overflow-x:auto;'><code>$1</code></pre>")
      .replace(/```([\s\S]*?)```/g, "<pre style='background:#0f172a; padding:8px; border-radius:6px; margin:6px 0; overflow-x:auto;'><code>$1</code></pre>")
      .replace(/`([^`]+)`/g, "<code style='background:rgba(56,189,248,0.2); color:#38bdf8; padding:2px 5px; border-radius:4px;'>$1</code>")
      .replace(/\n/g, "<br>");

    msgDiv.innerHTML = `
      <div class="ai-msg-avatar">${avatar}</div>
      <div class="ai-msg-body">${formatted}</div>
    `;
    container.appendChild(msgDiv);
    container.scrollTop = container.scrollHeight;
    return msgDiv;
  }

  async _callAITutorAPI(query, code, topic) {
    const container = document.getElementById("ai-chat-messages");
    const loadingDiv = document.createElement("div");
    loadingDiv.className = "ai-msg ai-msg-bot";
    loadingDiv.innerHTML = `
      <div class="ai-msg-avatar">🤖</div>
      <div class="ai-msg-body" style="color:#94a3b8; font-style:italic;">⚡ Senior soch raha hai (Groq sub-second inference)...</div>
    `;
    if (container) {
      container.appendChild(loadingDiv);
      container.scrollTop = container.scrollHeight;
    }

    try {
      const res = await fetch("/api/ai/tutor", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query, code, topic, provider: "groq" })
      });
      const data = await res.json();
      if (loadingDiv.parentNode) loadingDiv.parentNode.removeChild(loadingDiv);

      if (data.status === "success" && data.response) {
        this._appendAIChatMessage("bot", data.response);
      } else if (data.status === "unconfigured") {
        this._appendAIChatMessage("bot", data.message || "AI Tutor key not configured in .env.");
      } else {
        this._appendAIChatMessage("bot", `Arre bhai! API issue aayi: ${data.message || "Unknown error"}`);
      }
    } catch (err) {
      if (loadingDiv.parentNode) loadingDiv.parentNode.removeChild(loadingDiv);
      this._appendAIChatMessage("bot", "Network connection me dikkat aayi bhai. Dubara try karo.");
    }
  }

  /**
   * 📌 RESET CODE: Editor me original starter template code restore karta hai
   */
  resetCode() {
    const topics = this.curriculum[this.subject].topics || [];
    const topic = topics[this.currentTopicIndex];
    if (topic) {
      this.setCode(topic.starter_code || "");
    }
  }

  // =========================================================================
  // PAGE 2: DYNAMIC QUESTION BANK
  // =========================================================================

  /**
   * 📌 POPULATE Q-BANK TOPICS: Subject aur language ke mutabiq dynamic topics populate karta hai
   * 👁️ Web Page Pe Effect: Python par Python ke saare topics aate hain, HTML par HTML ke topics.
   */
  populateQBankTopics() {
    const select = document.getElementById("qbank-topic-select");
    if (!select) return;

    const currentVal = select.value;
    const isPython = this.subject === "python";
    const isHi = this.lang === "hi";

    const pythonTopics = [
      { id: "all", label_en: "All Topics (All Syllabus)", label_hi: "Saare Topics (Full Syllabus)" },
      { id: "py_variables", label_en: "Variables & Arithmetic", label_hi: "Variables aur Math" },
      { id: "py_conditionals", label_en: "Conditionals & Logic (If-Else)", label_hi: "Conditionals (If-Else)" },
      { id: "py_loops", label_en: "Loops & Iterations (While/For)", label_hi: "Loops aur Patterns" },
      { id: "py_lists", label_en: "Lists & Matrices", label_hi: "Lists aur Slicing" },
      { id: "py_tuples", label_en: "Tuples & Immutability", label_hi: "Tuples aur Coordinates" },
      { id: "py_dicts", label_en: "Dictionaries & Mappings", label_hi: "Dictionaries aur Lookup" },
      { id: "py_sets", label_en: "Sets & Mathematical Ops", label_hi: "Sets aur Unions" },
      { id: "py_functions", label_en: "Functions & *args", label_hi: "Functions aur Parameters" },
      { id: "py_strings", label_en: "Strings & Text Processing", label_hi: "Strings aur Formatting" },
      { id: "py_oop", label_en: "OOP & Inheritance", label_hi: "Classes aur Objects" },
      { id: "py_exceptions", label_en: "Exception Handling (Try-Except)", label_hi: "Try-Except aur Errors" },
      { id: "py_files", label_en: "File Handling & Log Parsing", label_hi: "Files aur CSV Parsing" }
    ];

    const htmlTopics = [
      { id: "all", label_en: "All Topics (All Syllabus)", label_hi: "Saare Topics (Full Syllabus)" },
      { id: "html_tags", label_en: "Semantic Tags & Structure", label_hi: "Semantic Tags (Header, Nav)" },
      { id: "html_forms", label_en: "Forms & User Inputs", label_hi: "Forms aur Inputs" },
      { id: "html_tables", label_en: "Tables & Data Grids", label_hi: "Tables (Thead, Tbody)" },
      { id: "html_media", label_en: "Media (Images & Audio)", label_hi: "Media (Img aur Audio)" },
      { id: "css_basics", label_en: "CSS Styling & Flexbox", label_hi: "CSS Styles aur Flexbox" }
    ];

    const topics = isPython ? pythonTopics : htmlTopics;
    select.innerHTML = topics.map(t => `<option value="${t.id}">${isHi ? t.label_hi : t.label_en}</option>`).join("");

    if (topics.some(t => t.id === currentVal)) {
      select.value = currentVal;
    } else {
      select.value = "all";
    }
  }

  /**
   * 📌 LOAD QUESTION BANK: Backend API se filtered practice questions fetch karta hai
   */
  async loadQuestionBank() {
    const topic = document.getElementById("qbank-topic-select")?.value || "all";
    const diff = document.getElementById("qbank-diff-select")?.value || "all";
    const count = document.getElementById("qbank-count-select")?.value || 5;

    try {
      const res = await fetch(`/api/questions?subject=${this.subject}&topic=${topic}&difficulty=${diff}&count=${count}`);
      const data = await res.json();
      this.currentQBankQuestions = data.questions || [];
      this.renderQuestions(this.currentQBankQuestions);
    } catch (e) {
      console.warn("Q-Bank fetch failed:", e);
    }
  }

  /**
   * 📌 RENDER QUESTIONS: Question cards with full pagination support
   */
  renderQuestions(questions) {
    this.qbankAllQuestions = questions || [];
    this.qbankCurrentPage = 1;
    this.renderQBankPage();
  }

  renderQBankPage() {
    const container = document.getElementById("questions-grid");
    if (!container) return;

    const isHi = this.lang === "hi";
    const questions = this.qbankAllQuestions || [];
    const total = questions.length;
    const paginationControls = document.getElementById("qbank-pagination-controls");

    if (total === 0) {
      if (paginationControls) paginationControls.style.display = "none";
      container.innerHTML = `
        <div style="grid-column: 1/-1; text-align:center; padding: 48px 24px; color:#94a3b8; background:rgba(15,23,42,0.6); border-radius:16px; border:1px dashed #334155;">
          <div style="font-size:2rem; margin-bottom:8px;">🔍</div>
          <h4 style="color:#f8fafc; font-size:1.1rem; margin-bottom:4px;">${isHi ? "Koi Question Nahi Mila" : "No Questions Found"}</h4>
          <p style="font-size:0.88rem; color:#64748b;">${isHi ? "Filter adjust karke 'All Topics' ya dusra difficulty level try karo." : "Try selecting 'All Topics' or a different difficulty filter."}</p>
        </div>`;
      return;
    }

    const pageSize = this.qbankPageSize || 5;
    const totalPages = Math.ceil(total / pageSize);
    if (this.qbankCurrentPage > totalPages) this.qbankCurrentPage = totalPages;
    if (this.qbankCurrentPage < 1) this.qbankCurrentPage = 1;

    const startIdx = (this.qbankCurrentPage - 1) * pageSize;
    const endIdx = Math.min(startIdx + pageSize, total);
    const pageQuestions = questions.slice(startIdx, endIdx);

    this.qbankQuestionsMap = {};
    questions.forEach(q => {
      this.qbankQuestionsMap[q.id] = q;
    });

    container.innerHTML = pageQuestions.map((q, idx) => {
      const globalIdx = startIdx + idx;
      const isSolved = this.solvedQBankSet && this.solvedQBankSet.has(q.id);
      const isAI = Boolean(q.ai_generated);
      const isPython = q.subject === "python";
      const diffClass = `diff-${(q.difficulty || "Beginner").toLowerCase()}`;
      const title = isHi ? (q.title_hi || q.title_en) : q.title_en;
      const desc = isHi ? (q.desc_hi || q.desc_en) : q.desc_en;
      const hint = isHi ? (q.hint_hi || q.hint_en) : (q.hint_en || q.hint_hi);
      const xp = q.xp || 50;

      return `
        <div id="q-card-${q.id}" class="question-card-3d card-3d-tilt ${isSolved ? 'card-solved' : ''} ${isAI ? 'card-ai-generated' : ''}" style="${isAI ? 'border-color: rgba(168,85,247,0.45); box-shadow: 0 0 20px rgba(168,85,247,0.12);' : ''}">
          <div>
            <div class="q-badge-row" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
              <div style="display:flex; gap:8px; align-items:center; flex-wrap:wrap;">
                <span class="q-diff-badge ${diffClass}">${q.difficulty}</span>
                ${isAI ? `<span style="font-size:0.75rem; color:#c084fc; background:rgba(168,85,247,0.18); border:1px solid rgba(168,85,247,0.4); padding:2px 8px; border-radius:9999px; font-weight:800;">✨ Groq AI</span>` : ''}
                ${isAI && isPython ? `
                  <span id="q-verify-badge-${q.id}" class="q-verify-badge" style="font-size:0.75rem; padding:2px 8px; border-radius:9999px; font-weight:700; transition:all 0.2s ease; ${
                    q.output_verified === true
                      ? 'color:#34d399; background:rgba(16,185,129,0.15); border:1px solid rgba(16,185,129,0.4);'
                      : (q.output_verified === 'differs'
                      ? 'color:#fbbf24; background:rgba(245,158,11,0.18); border:1px solid rgba(245,158,11,0.4);'
                      : 'color:#94a3b8; background:rgba(148,163,184,0.12); border:1px solid rgba(148,163,184,0.25);')
                  }">
                    ${
                      q.output_verified === true
                        ? '✔ Verified in your browser'
                        : (q.output_verified === 'differs'
                        ? '⚠️ AI answer differs - trust your own run'
                        : '⏳ Verifying in browser...')
                    }
                  </span>
                ` : ''}
                ${q.fallback_mode ? `<span style="font-size:0.75rem; color:#fbbf24; background:rgba(245,158,11,0.18); border:1px solid rgba(245,158,11,0.4); padding:2px 8px; border-radius:9999px; font-weight:800;">⚡ Bank (AI Cooldown)</span>` : ''}
                <span style="font-size:0.75rem; color:#38bdf8; background:rgba(56,189,248,0.12); padding:2px 8px; border-radius:9999px; font-weight:700;">⭐ +${xp} XP</span>
                <span id="q-solved-badge-${q.id}" class="solved-badge" style="display:${isSolved ? 'inline-block' : 'none'};">✔ Solved</span>
              </div>
              <span style="font-size:0.75rem; color:#64748b; font-weight:800;">#${globalIdx + 1}</span>
            </div>

            <h3 class="q-title" style="margin-top:0;">${this._escapeHtml(title)}</h3>
            <p class="q-desc">${this._escapeHtml(desc)}</p>

            ${isPython && q.expected_output ? `
              <div style="margin-bottom:12px; font-size:0.78rem; background:rgba(15,23,42,0.7); border:1px solid #334155; border-radius:8px; padding:8px 12px;">
                <span style="color:#94a3b8; font-weight:700;">🎯 Expected Output:</span>
                <pre style="margin:4px 0 0; color:#38bdf8; font-family:var(--font-mono); font-size:0.76rem; white-space:pre-wrap; max-height:80px; overflow-y:auto;">${this._escapeHtml(q.expected_output)}</pre>
              </div>
            ` : ''}

            ${isAI && isPython ? `
              <div id="q-verify-diff-${q.id}" style="${q.output_verified === 'differs' ? 'display:block;' : 'display:none;'} margin-bottom:12px; font-size:0.78rem; background:rgba(245,158,11,0.1); border:1px solid rgba(245,158,11,0.3); border-radius:8px; padding:8px 12px; color:#fde68a;">
                <span style="font-weight:700;">⚠️ Actual Browser Output:</span>
                <pre id="q-verify-diff-out-${q.id}" style="margin:4px 0 0; color:#fbbf24; font-family:var(--font-mono); font-size:0.76rem; white-space:pre-wrap; max-height:80px; overflow-y:auto;">${this._escapeHtml(q.actual_browser_output || "")}</pre>
              </div>
            ` : ''}

            ${!isPython && q.expected_html_elements ? `
              <div style="margin-bottom:12px; font-size:0.78rem; background:rgba(15,23,42,0.7); border:1px solid #334155; border-radius:8px; padding:8px 12px;">
                <span style="color:#94a3b8; font-weight:700;">🎯 Required Tags:</span>
                <span style="color:#38bdf8; font-family:var(--font-mono); font-weight:700; margin-left:6px;">&lt;${q.expected_html_elements.join('&gt;, &lt;')}&gt;</span>
              </div>
            ` : ''}
          </div>

          <div>
            <div class="code-editor-wrapper" style="min-height: 150px; margin-bottom: 10px;">
              <textarea id="q-code-${q.id}" class="code-textarea" spellcheck="false" style="min-height: 150px; font-family:var(--font-mono); font-size:0.84rem; line-height:1.5;">${this._escapeHtml(q.starter_code || "")}</textarea>
            </div>

            <div id="q-out-${q.id}" class="q-out-box" style="display:none; font-family:var(--font-mono); font-size:0.8rem; margin:8px 0; padding:10px 12px; border-radius:8px; border:1px solid #334155; background:#0f172a; white-space:pre-wrap; line-height:1.4;"></div>

            <div id="q-hint-${q.id}" class="senior-advice-bubble" style="display:none; margin:8px 0;">
              <span>💡 <strong>Senior Advice:</strong> ${this._escapeHtml(hint)}</span>
            </div>

            <div id="q-sol-${q.id}" style="display:none; margin:8px 0; background:rgba(6,78,59,0.3); border:1px solid #059669; border-radius:8px; padding:12px;">
              <div style="font-size:0.75rem; color:#34d399; font-weight:700; margin-bottom:6px;">💡 Model Solution:</div>
              <pre style="margin:0; color:#a7f3d0; font-family:var(--font-mono); font-size:0.78rem; white-space:pre-wrap;">${this._escapeHtml(q.solution_code || "")}</pre>
            </div>

            <div class="q-actions" style="display:flex; flex-wrap:wrap; gap:8px; justify-content:space-between; align-items:center; border-top:1px solid var(--border-glass); padding-top:12px;">
              <div style="display:flex; gap:6px; flex-wrap:wrap;">
                <button class="btn-primary-3d" style="padding:6px 14px; font-size:0.82rem;" onclick="window.elysiaApp.solveQBankItem('${q.id}')">
                  <span>▶</span> ${isHi ? "Run & Test" : "Run & Test"}
                </button>
                <button class="pill-btn" style="padding:6px 10px; font-size:0.8rem;" onclick="window.elysiaApp.toggleQBankHint('${q.id}')">
                  💡 ${isHi ? "Hint" : "Hint"}
                </button>
                <button class="pill-btn" style="padding:6px 10px; font-size:0.8rem;" onclick="window.elysiaApp.toggleQBankSolution('${q.id}')">
                  👁️ ${isHi ? "Solution" : "Solution"}
                </button>
              </div>

              <div style="display:flex; gap:6px;">
                <button class="pill-btn" title="Reset starter code" style="padding:6px 8px; font-size:0.8rem;" onclick="window.elysiaApp.resetQBankCode('${q.id}')">
                  ↺ Reset
                </button>
                <button class="pill-btn" title="Send to Main IDE" style="padding:6px 8px; font-size:0.8rem;" onclick="window.elysiaApp.sendQBankToEditor('${q.id}')">
                  ⚡ Open in IDE
                </button>
              </div>
            </div>
          </div>
        </div>
      `;
    }).join("");

    // Update Pagination UI Bar
    if (paginationControls) {
      paginationControls.style.display = total > 0 ? "flex" : "none";
      const startEl = document.getElementById("qbank-page-start");
      const endEl = document.getElementById("qbank-page-end");
      const totalEl = document.getElementById("qbank-page-total");
      const prevBtn = document.getElementById("qbank-btn-prev");
      const nextBtn = document.getElementById("qbank-btn-next");
      const numContainer = document.getElementById("qbank-page-numbers");

      if (startEl) startEl.textContent = (startIdx + 1).toString();
      if (endEl) endEl.textContent = endIdx.toString();
      if (totalEl) totalEl.textContent = total.toString();

      if (prevBtn) {
        prevBtn.disabled = this.qbankCurrentPage <= 1;
        prevBtn.style.opacity = this.qbankCurrentPage <= 1 ? "0.4" : "1";
        prevBtn.style.cursor = this.qbankCurrentPage <= 1 ? "not-allowed" : "pointer";
      }
      if (nextBtn) {
        nextBtn.disabled = this.qbankCurrentPage >= totalPages;
        nextBtn.style.opacity = this.qbankCurrentPage >= totalPages ? "0.4" : "1";
        nextBtn.style.cursor = this.qbankCurrentPage >= totalPages ? "not-allowed" : "pointer";
      }

      if (numContainer) {
        numContainer.innerHTML = Array.from({ length: totalPages }, (_, i) => i + 1).map(p => `
          <button class="pill-btn ${p === this.qbankCurrentPage ? 'active' : ''}" 
                  style="padding:4px 10px; font-size:0.8rem; min-width:32px; ${p === this.qbankCurrentPage ? 'background:linear-gradient(135deg, #6366f1, #818cf8); color:#fff; border-color:#818cf8; font-weight:800;' : ''}" 
                  onclick="window.elysiaApp.goToQBankPage(${p})">
            ${p}
          </button>
        `).join("");
      }
    }

    // Phase 2: Verify unverified AI questions client-side in the Pyodide Web Worker
    pageQuestions.forEach(q => {
      if (q.ai_generated && q.output_verified === false && q.solution_code && q.subject === "python") {
        this.verifyAIQuestionInBrowser(q);
      }
    });
  }

  async verifyAIQuestionInBrowser(q) {
    if (!q || !q.solution_code || q.subject !== "python") return;
    const badge = document.getElementById(`q-verify-badge-${q.id}`);
    const diffBox = document.getElementById(`q-verify-diff-${q.id}`);
    const diffOut = document.getElementById(`q-verify-diff-out-${q.id}`);

    try {
      if (!window.pyodideManager) return;
      // Run solution_code in background Web Worker (never touches server)
      const res = await window.pyodideManager.run(q.solution_code, "", 4000);
      const actualOut = (res.stdout || "").trimEnd();
      const expectedOut = (q.expected_output || "").trimEnd();

      if (res.success && actualOut === expectedOut) {
        q.output_verified = true;
        if (badge) {
          badge.innerHTML = "✔ Verified in your browser";
          badge.style.color = "#34d399";
          badge.style.background = "rgba(16,185,129,0.15)";
          badge.style.border = "1px solid rgba(16,185,129,0.4)";
        }
        if (diffBox) diffBox.style.display = "none";
      } else {
        q.output_verified = "differs";
        q.actual_browser_output = actualOut || res.stderr || "(no output)";
        if (badge) {
          badge.innerHTML = "⚠️ AI answer differs - trust your own run";
          badge.style.color = "#fbbf24";
          badge.style.background = "rgba(245,158,11,0.18)";
          badge.style.border = "1px solid rgba(245,158,11,0.4)";
        }
        if (diffBox && diffOut) {
          diffBox.style.display = "block";
          diffOut.textContent = q.actual_browser_output;
        }
      }
    } catch (e) {
      console.warn("Browser verification error:", e);
      if (badge) {
        badge.innerHTML = "⚠️ AI answer differs - trust your own run";
        badge.style.color = "#fbbf24";
        badge.style.background = "rgba(245,158,11,0.18)";
        badge.style.border = "1px solid rgba(245,158,11,0.4)";
      }
    }
  }

  prevQBankPage() {
    if (this.qbankCurrentPage > 1) {
      this.qbankCurrentPage--;
      this.renderQBankPage();
    }
  }

  nextQBankPage() {
    const totalPages = Math.ceil((this.qbankAllQuestions || []).length / (this.qbankPageSize || 5));
    if (this.qbankCurrentPage < totalPages) {
      this.qbankCurrentPage++;
      this.renderQBankPage();
    }
  }

  goToQBankPage(p) {
    this.qbankCurrentPage = p;
    this.renderQBankPage();
  }

  changeQBankPageSize(newSize) {
    this.qbankPageSize = parseInt(newSize) || 5;
    this.qbankCurrentPage = 1;
    this.renderQBankPage();
  }

  toggleQBankHint(qId) {
    window.elysiaAudio.playClick();
    const hintEl = document.getElementById(`q-hint-${qId}`);
    if (hintEl) {
      hintEl.style.display = hintEl.style.display === "none" ? "flex" : "none";
    }
  }

  toggleQBankSolution(qId) {
    window.elysiaAudio.playClick();
    const solEl = document.getElementById(`q-sol-${qId}`);
    if (solEl) {
      solEl.style.display = solEl.style.display === "none" ? "block" : "none";
    }
  }

  resetQBankCode(qId) {
    window.elysiaAudio.playClick();
    const q = this.qbankQuestionsMap ? this.qbankQuestionsMap[qId] : null;
    const codeEl = document.getElementById(`q-code-${qId}`);
    const outEl = document.getElementById(`q-out-${qId}`);
    if (q && codeEl) {
      codeEl.value = q.starter_code || "";
      if (outEl) outEl.style.display = "none";
    }
  }

  sendQBankToEditor(qId) {
    window.elysiaAudio.playClick();
    const q = this.qbankQuestionsMap ? this.qbankQuestionsMap[qId] : null;
    const codeEl = document.getElementById(`q-code-${qId}`);
    if (!q) return;

    const codeToTransfer = (codeEl && codeEl.value) ? codeEl.value : (q.starter_code || "");
    if (this.subject !== q.subject) {
      this.setSubject(q.subject);
    }
    this.setCode(codeToTransfer);
    this.switchTab("learn");

    const stdoutEl = document.getElementById("terminal-stdout");
    if (stdoutEl) {
      stdoutEl.textContent = `🚀 Transferred Question "${q.title_en}" into IDE! Click 'Run Code' or edit freely.`;
    }
  }

  /**
   * 📌 GENERATE AI QUESTION: Groq LLM se instant creative campus coding challenge banwata hai
   */
  async generateAIQuestion() {
    window.elysiaAudio.playClick();
    if (!this.currentUser) {
      this.openAuthModal();
      return;
    }
    const btn = document.getElementById("btn-ai-generate-qbank");
    const promptInput = document.getElementById("qbank-ai-custom-prompt");
    const statusMsg = document.getElementById("qbank-ai-status-msg");
    const topic = document.getElementById("qbank-topic-select")?.value || "all";
    const diff = document.getElementById("qbank-diff-select")?.value || "Intermediate";
    const prompt = promptInput?.value?.trim() || "";

    const originalHtml = btn ? btn.innerHTML : "";
    if (btn) {
      btn.disabled = true;
      btn.style.opacity = "0.75";
      btn.innerHTML = `<span>⏳</span> Generating with Groq...`;
    }
    if (statusMsg) {
      statusMsg.style.display = "block";
      statusMsg.innerHTML = `<span style="color:#38bdf8;">⚡ Consulting Groq AI inference engine...</span>`;
    }

    try {
      const res = await fetch("/api/questions/generate-ai", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          subject: this.subject,
          topic: topic,
          difficulty: diff,
          prompt: prompt
        })
      });

      const data = await res.json();

      if (data.status === "success" && data.question) {
        window.elysiaAudio.playSuccess();
        const newQ = data.question;

        if (!this.currentQBankQuestions) {
          this.currentQBankQuestions = [];
        }
        // Place the newly generated question at the very top!
        this.currentQBankQuestions.unshift(newQ);
        this.renderQuestions(this.currentQBankQuestions);

        if (promptInput) promptInput.value = "";

        if (statusMsg) {
          if (data.rate_limited) {
            statusMsg.innerHTML = `<span style="color:#fbbf24; font-weight:600;">⚡ Note: Groq free tier quota is cooling down. Loaded a high-yield matching challenge from the question bank!</span>`;
          } else {
            statusMsg.innerHTML = `<span style="color:#34d399; font-weight:600;">✨ Fresh challenge generated by Groq AI! See card below.</span>`;
            this.launchConfetti();
          }
        }

        setTimeout(() => {
          const card = document.getElementById(`q-card-${newQ.id}`);
          if (card) {
            card.scrollIntoView({ behavior: "smooth", block: "center" });
          }
        }, 120);
      } else if (data.status === "unconfigured") {
        window.elysiaAudio.playError();
        if (statusMsg) {
          statusMsg.innerHTML = `<span style="color:#f87171; font-weight:600;">⚠️ ${this._escapeHtml(data.message || "Groq key not configured in .env")}</span>`;
        }
      } else {
        window.elysiaAudio.playError();
        if (statusMsg) {
          statusMsg.innerHTML = `<span style="color:#f87171; font-weight:600;">⚠️ ${this._escapeHtml(data.message || "Could not generate question from Groq right now.")}</span>`;
        }
      }
    } catch (err) {
      console.warn("AI generation failed:", err);
      window.elysiaAudio.playError();
      if (statusMsg) {
        statusMsg.innerHTML = `<span style="color:#f87171; font-weight:600;">⚠️ Network connection issue while contacting server.</span>`;
      }
    } finally {
      if (btn) {
        btn.disabled = false;
        btn.style.opacity = "1";
        btn.innerHTML = originalHtml;
      }
    }
  }

  /**
   * 📌 SOLVE Q-BANK ITEM: Python aur HTML questions ko test cases se verify karta hai
   */
  async solveQBankItem(qId) {
    window.elysiaAudio.playClick();
    const q = this.qbankQuestionsMap ? this.qbankQuestionsMap[qId] : null;
    const codeEl = document.getElementById(`q-code-${qId}`);
    const outEl = document.getElementById(`q-out-${qId}`);
    const cardEl = document.getElementById(`q-card-${qId}`);
    const solvedBadge = document.getElementById(`q-solved-badge-${qId}`);

    if (!codeEl || !outEl || !q) return;

    outEl.style.display = "block";
    outEl.style.borderColor = "#38bdf8";
    outEl.style.background = "rgba(15, 23, 42, 0.9)";
    outEl.innerHTML = '<span style="color:#38bdf8;">⚡ Running test execution...</span>';

    const isPython = q.subject === "python";
    const userCode = codeEl.value;

    if (isPython) {
      const qResult = await this.runPythonCode(userCode, "", 4.0);
      const stdout = qResult.stdout || "";
      const stderr = qResult.stderr || "";

      if (stderr) {
        window.elysiaAudio.playError();
        outEl.style.borderColor = "#f43f5e";
        outEl.style.background = "rgba(244, 63, 94, 0.08)";
        outEl.innerHTML = `
          <div style="color:#fb7185; font-weight:700; margin-bottom:4px;">❌ Runtime / Syntax Error:</div>
          <div style="color:#fca5a5; font-size:0.78rem;">${this._formatTracebackHtml(stderr)}</div>
        `;
        return;
      }

      const cleanActual = stdout.trim().replace(/\r\n/g, "\n");
      const cleanExpected = (q.expected_output || "").trim().replace(/\r\n/g, "\n");

      if (cleanActual === cleanExpected) {
        window.elysiaAudio.playSuccess();
        this.launchConfetti();

        if (cardEl) cardEl.classList.add("card-solved");
        if (solvedBadge) solvedBadge.style.display = "inline-block";

        if (!this.solvedQBankSet.has(q.id)) {
          this.solvedQBankSet.add(q.id);
          this.addXP(q.xp || 50);
          localStorage.setItem("elysia_solved_qbank", JSON.stringify(Array.from(this.solvedQBankSet)));
        }

        outEl.style.borderColor = "#10b981";
        outEl.style.background = "rgba(16, 185, 129, 0.1)";
        outEl.innerHTML = `
          <div style="color:#34d399; font-weight:800; margin-bottom:6px;">🎉 ALL TEST CASES PASSED! (+${q.xp || 50} XP)</div>
          <div style="color:#94a3b8; font-size:0.75rem;">Actual Output Matches Expected Output:</div>
          <pre style="margin:4px 0 0; color:#a7f3d0; font-weight:600; font-size:0.78rem;">${this._escapeHtml(cleanActual)}</pre>
        `;
      } else {
        window.elysiaAudio.playError();
        outEl.style.borderColor = "#f59e0b";
        outEl.style.background = "rgba(245, 158, 11, 0.08)";
        outEl.innerHTML = `
          <div style="color:#fbbf24; font-weight:800; margin-bottom:6px;">⚠️ Test Failed: Output Mismatch</div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; margin-top:6px; font-size:0.76rem;">
            <div>
              <strong style="color:#94a3b8;">Expected Output:</strong>
              <pre style="margin:2px 0 0; color:#38bdf8; background:#0b1120; padding:6px; border-radius:4px;">${this._escapeHtml(cleanExpected)}</pre>
            </div>
            <div>
              <strong style="color:#94a3b8;">Your Output:</strong>
              <pre style="margin:2px 0 0; color:#fca5a5; background:#0b1120; padding:6px; border-radius:4px;">${this._escapeHtml(cleanActual) || '[No output]'}</pre>
            </div>
          </div>
          <div style="margin-top:6px; font-size:0.74rem; color:#cbd5e1;">💡 Tip: Check punctuation, variable names, and case sensitivity!</div>
        `;
      }
    } else {
      // HTML Validation
      const parser = new DOMParser();
      const doc = parser.parseFromString(userCode, "text/html");
      const missing = [];
      const expectedTags = q.expected_html_elements || [];

      for (const tag of expectedTags) {
        if (!doc.querySelector(tag)) {
          missing.push(tag);
        }
      }

      if (missing.length === 0) {
        window.elysiaAudio.playSuccess();
        this.launchConfetti();

        if (cardEl) cardEl.classList.add("card-solved");
        if (solvedBadge) solvedBadge.style.display = "inline-block";

        if (!this.solvedQBankSet.has(q.id)) {
          this.solvedQBankSet.add(q.id);
          this.addXP(q.xp || 50);
          localStorage.setItem("elysia_solved_qbank", JSON.stringify(Array.from(this.solvedQBankSet)));
        }

        outEl.style.borderColor = "#10b981";
        outEl.style.background = "rgba(16, 185, 129, 0.1)";
        outEl.innerHTML = `
          <div style="color:#34d399; font-weight:800; margin-bottom:4px;">🎉 HTML STRUCTURE VERIFIED! (+${q.xp || 50} XP)</div>
          <div style="color:#94a3b8; font-size:0.75rem;">All required elements detected: <span style="color:#38bdf8; font-family:var(--font-mono);">&lt;${expectedTags.join("&gt;, &lt;")}&gt;</span></div>
        `;
      } else {
        window.elysiaAudio.playError();
        outEl.style.borderColor = "#f43f5e";
        outEl.style.background = "rgba(244, 63, 94, 0.08)";
        outEl.innerHTML = `
          <div style="color:#fb7185; font-weight:800; margin-bottom:4px;">❌ HTML Test Failed: Missing Elements</div>
          <div style="color:#fca5a5; font-size:0.78rem;">Please include the following tags: <span style="font-family:var(--font-mono); font-weight:700; color:#fff;">&lt;${missing.join("&gt;, &lt;")}&gt;</span></div>
        `;
      }
    }
  }

  // =========================================================================
  // PAGE 3: COLLEGE MOCK TEST & VIVA SIMULATOR
  // =========================================================================

  /**
   * 📌 LOAD MOCK EXAM: Semester practical exam paper load karta hai
   * 👁️ Web Page Pe Effect: Section A (MCQs), Section B (Debugging / Doctor Mode),
   *    aur Section D (Viva Simulator) load hota hai aur timer chalu hota hai.
   */
  async loadMockExam() {
    try {
      const examId = this.subject === "html" ? "html_ca1" : "python_ca1";
      const res = await fetch(`/api/mock-exam?id=${examId}`);
      this.mockExamData = await res.json();
      this.renderMockExam();
      this.startExamTimer();
    } catch (e) {
      console.warn("Mock exam fetch failed");
    }
  }

  /**
   * 📌 START EXAM TIMER: 25-minute ka real-time ticking countdown timer
   * 👁️ Web Page Pe Effect: 25:00 se ghadi ulte daudti hai (24:59, 24:58...).
   * 💡 Kyun: `setInterval(..., 1000)` har second `this.examSecondsRemaining` ko 1 se ghataata hai.
   * ⚠️ Agar hata dein: Student ko pata nahi chalega ki exam me kitna waqt bacha hai.
   */
  startExamTimer() {
    if (this.examTimerInterval) clearInterval(this.examTimerInterval);
    const timerEl = document.getElementById("exam-timer-display");

    this.examTimerInterval = setInterval(() => {
      this.examSecondsRemaining--;
      if (this.examSecondsRemaining <= 0) {
        clearInterval(this.examTimerInterval);
        if (timerEl) timerEl.textContent = "00:00 - TIME UP!";
        alert("Time is up! Submitting your practical exam.");
        return;
      }

      const mins = Math.floor(this.examSecondsRemaining / 60);
      const secs = this.examSecondsRemaining % 60;
      if (timerEl) timerEl.textContent = `⏱️ ${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
    }, 1000);
  }

  /**
   * 📌 RENDER MOCK EXAM: Exam sections (MCQ, Debugging, Viva) render karta hai
   */
  renderMockExam() {
    if (!this.mockExamData) return;
    const exam = this.mockExamData;
    const isHi = this.lang === "hi";

    const titleEl = document.getElementById("mock-exam-title");
    const instEl = document.getElementById("mock-exam-instructions");
    if (titleEl) titleEl.textContent = exam.title;
    if (instEl) instEl.textContent = isHi ? exam.instructions_hi : exam.instructions_en;

    // Render Section A: MCQs
    const mcqContainer = document.getElementById("mock-mcq-container");
    if (mcqContainer && exam.section_a_mcq) {
      mcqContainer.innerHTML = exam.section_a_mcq.map((mcq, idx) => `
        <div style="margin-bottom: 20px; background: rgba(0,0,0,0.3); padding: 16px; border-radius: var(--radius-md);">
          <div style="font-size:0.95rem; font-weight:700; color:#fff; margin-bottom:8px;">
            Q${idx+1}: ${isHi ? mcq.question_hi : mcq.question_en} (${mcq.marks} Marks)
          </div>
          <pre class="code-textarea" style="min-height: 80px; padding: 10px; background:#000; border-radius: 8px; margin-bottom: 10px;">${mcq.code}</pre>
          <div class="mcq-options-grid">
            ${mcq.options.map((opt, optIdx) => `
              <button class="mcq-option-btn" onclick="window.elysiaApp.selectMcqOption(this, ${optIdx}, ${mcq.correct_index}, '${this._escapeHtml(isHi ? mcq.explanation_hi : mcq.explanation_en)}')">
                ${String.fromCharCode(65 + optIdx)}. ${opt}
              </button>
            `).join("")}
          </div>
          <div class="mcq-feedback" style="margin-top: 10px; font-size: 0.85rem; display:none;"></div>
        </div>
      `).join("");
    }

    // Render Section B: Doctor Mode (Find & Fix bugs)
    const debugContainer = document.getElementById("mock-debug-container");
    if (debugContainer && exam.section_b_debug) {
      const d = exam.section_b_debug[0];
      debugContainer.innerHTML = `
        <div style="background: rgba(0,0,0,0.3); padding: 18px; border-radius: var(--radius-md);">
          <div style="font-size:1.05rem; font-weight:700; color:#fb7185; margin-bottom:6px;">${d.title} (${d.marks} Marks)</div>
          <p style="font-size:0.9rem; color:#94a3b8; margin-bottom:12px;">${isHi ? d.desc_hi : d.desc_en}</p>
          <div class="code-editor-wrapper" style="min-height: 160px; margin-bottom: 12px;">
            <textarea id="mock-debug-textarea" class="code-textarea" style="min-height: 160px;">${d.broken_code}</textarea>
          </div>
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <button class="btn-success-3d" onclick="window.elysiaApp.testDoctorMode()">
              🩺 ${isHi ? "Bugs Theek Ho Gaye? Test Karo" : "Verify Doctor Fix"}
            </button>
            <span id="doctor-feedback" style="font-size:0.85rem; font-weight:700;"></span>
          </div>
        </div>
      `;
    }

    // Render Section D: Oral Viva Simulator
    const vivaContainer = document.getElementById("mock-viva-container");
    if (vivaContainer && exam.section_d_viva) {
      vivaContainer.innerHTML = exam.section_d_viva.map((v, idx) => `
        <div class="viva-accordion" style="margin-bottom: 12px;">
          <div class="viva-title">🎙️ Viva Q${idx+1}: ${v.question}</div>
          <div style="color: #94a3b8; font-size: 0.88rem; margin-top: 6px;">
            <strong>${isHi ? "Teacher ko impress karne wala answer:" : "High-Scoring Viva Answer:"}</strong>
            <p style="color:#e2e8f0; margin-top: 4px;">${isHi ? v.answer_hi : v.answer_en}</p>
          </div>
        </div>
      `).join("");
    }
  }

  /**
   * 📌 SELECT MCQ OPTION: Multiple Choice Question ka live answer check
   * 👁️ Web Page Pe Effect: Sahi option par Green text aur galat par Red text with deep explanation aata hai.
   */
  selectMcqOption(btn, chosen, correct, explanation) {
    const parent = btn.parentElement;
    parent.querySelectorAll(".mcq-option-btn").forEach(b => b.classList.remove("selected"));
    btn.classList.add("selected");

    const feedbackEl = parent.parentElement.querySelector(".mcq-feedback");
    if (!feedbackEl) return;

    feedbackEl.style.display = "block";
    if (chosen === correct) {
      window.elysiaAudio.playSuccess();
      feedbackEl.style.color = "#34d399";
      feedbackEl.innerHTML = `✅ Correct! ${explanation}`;
    } else {
      window.elysiaAudio.playError();
      feedbackEl.style.color = "#fb7185";
      feedbackEl.innerHTML = `❌ Incorrect. ${explanation}`;
    }
  }

  /**
   * 📌 TEST DOCTOR MODE: Buggy code ko debug karke verify karta hai
   */
  async testDoctorMode() {
    window.elysiaAudio.playClick();
    const code = document.getElementById("mock-debug-textarea").value;
    const feedback = document.getElementById("doctor-feedback");

    const res = await window.pyodideManager.run(code);
    if (res.success && res.stdout.includes("Even count: 5")) {
      window.elysiaAudio.playSuccess();
      feedback.style.color = "#34d399";
      feedback.textContent = "🏆 ALL BUGS CURED! Full 6 Marks Awarded.";
    } else {
      window.elysiaAudio.playError();
      feedback.style.color = "#fb7185";
      feedback.textContent = "Bugs still exist! Expected: 'Even count: 5'";
    }
  }

  // =========================================================================
  // PAGE 4: 60-SEC INSTANT DOUBT BUSTER & SEARCH
  // =========================================================================

  /**
   * 📌 HANDLE SEARCH: 60-Second Instant Revision Search Engine
   * 👁️ Web Page Pe Effect: User ke type karte hi matches live search cards ke roop me appear hote hain.
   * 💡 Kyun: `encodeURIComponent(query)` use kiya taaki special symbols URL safe banein.
   */
  async handleSearch(query) {
    const container = document.getElementById("search-results-list");
    if (!container) return;

    if (!query || query.trim().length < 2) {
      container.innerHTML = `<div style="text-align:center; color:#64748b; padding: 20px;">Type any topic (e.g. input, type casting, loops, f-strings, list) to bust your doubt in 60s.</div>`;
      return;
    }

    const qLower = query.trim().toLowerCase();
    const isHi = this.lang === "hi";
    let results = [];

    try {
      const res = await fetch(`/api/search?q=${encodeURIComponent(query)}&lang=${this.lang}`);
      if (res.ok) {
        const data = await res.json();
        results = data.results || [];
      }
    } catch (e) {
      // Network fallback
    }

    // Client-side search enhancement across PYTHON_CURRICULUM_TREE
    if (results.length === 0 && window.PYTHON_CURRICULUM_TREE) {
      for (const ch of window.PYTHON_CURRICULUM_TREE) {
        for (const sub of (ch.subtopics || [])) {
          const tEn = (sub.title || "").toLowerCase();
          const tHi = (sub.title_hi || "").toLowerCase();
          const wEn = (sub.what_is_it_en || "").toLowerCase();
          const wHi = (sub.what_is_it_hi || "").toLowerCase();
          const syn = (sub.syntax || "").toLowerCase();
          const rules = (isHi ? (sub.rules_hi || []) : (sub.rules_en || [])).join(" ").toLowerCase();

          if (tEn.includes(qLower) || tHi.includes(qLower) || wEn.includes(qLower) || wHi.includes(qLower) || syn.includes(qLower) || rules.includes(qLower)) {
            const rulesArr = isHi ? (sub.rules_hi || []) : (sub.rules_en || []);
            results.push({
              subject: "python",
              icon: sub.icon || "🐍",
              title: isHi ? (sub.title_hi || sub.title) : sub.title,
              intro: isHi ? (sub.what_is_it_hi || sub.what_is_it_en) : (sub.what_is_it_en || sub.what_is_it_hi),
              mistakes: rulesArr.length > 0 ? [{ mistake: sub.syntax || "", why_it_fails_hi: rulesArr[0], why_it_fails_en: rulesArr[0] }] : []
            });
          }
        }
      }
    }

    if (results.length === 0) {
      container.innerHTML = `<div style="text-align:center; color:#94a3b8; padding: 20px;">No exact match found for "${this._escapeHtml(query)}". Try searching 'input', 'loops', 'variables', or 'syntax'.</div>`;
      return;
    }

    container.innerHTML = results.slice(0, 10).map(r => `
      <div class="theory-card-3d card-3d-tilt" style="max-height: none;">
        <div class="lesson-header">
          <span class="lesson-tag">${(r.subject || "PYTHON").toUpperCase()} • 60-Sec Crash Revision</span>
          <h2 class="lesson-title"><span>${r.icon || '⚡'}</span> ${r.title}</h2>
        </div>
        <div class="analogy-box">
          <div class="box-label">⚡ ${isHi ? "Core Concept 60 Seconds Me:" : "Quick Intuition:"}</div>
          <p class="analogy-text">${r.intro}</p>
        </div>
        ${r.mistakes && r.mistakes[0] ? `
          <div class="mistake-card">
            <div class="mistake-header">🚨 ${isHi ? "Sunehra Niyam / Trap:" : "Golden Rule / Trap:"}</div>
            ${r.mistakes[0].mistake ? `<div class="mistake-snippet">${this._escapeHtml(r.mistakes[0].mistake)}</div>` : ''}
            <div class="mistake-explain">${isHi ? (r.mistakes[0].why_it_fails_hi || r.mistakes[0].why_it_fails_en) : (r.mistakes[0].why_it_fails_en || r.mistakes[0].why_it_fails_hi)}</div>
          </div>
        ` : ''}
      </div>
    `).join("");
  }

  // =========================================================================
  // PAGE 5: CODE X-RAY (VIVA SHIELD)
  // =========================================================================

  /**
   * 📌 ANALYZE CODE X-RAY: Line-by-Line Code Dissector
   * 📌 KYA KAAM HAI:
   *   Code ko lines me tod kar har line ka viva role aur examiner question batata hai.
   * 👁️ WEB PAGE PE KYA DIKHTA HAI:
   *   Line 1, Line 2... har line ka card jisme loop complexity, slicing idiom ya conditional branching tip hoti hai.
   */
  analyzeCodeXRay() {
    window.elysiaAudio.playClick();
    const code = document.getElementById("xray-input-textarea").value;
    const outputContainer = document.getElementById("xray-breakdown-list");
    if (!outputContainer) return;

    const lines = code.split("\n");
    const isHi = this.lang === "hi";

    outputContainer.innerHTML = lines.map((line, idx) => {
      const trimmed = line.trim();
      let tip = isHi ? "Basic statement execution." : "Standard line execution.";
      let viva = isHi ? "Professor puchega: 'Is line ka role kya hai?'" : "Teacher question: 'Explain line logic.'";

      if (trimmed.startsWith("for ") || trimmed.startsWith("while ")) {
        tip = isHi ? "Loop execution — Har element par iterate kar raha hai." : "Iteration construct repeating over a sequence.";
        viva = isHi ? "Viva Tip: Loop ka time complexity O(N) batana!" : "Viva Tip: Mention O(N) time complexity.";
      } else if (trimmed.startsWith("if ") || trimmed.startsWith("elif ")) {
        tip = isHi ? "Conditional Branching — Condition True hogi to hi andar jayega." : "Decision branch evaluating a boolean test.";
        viva = isHi ? "Viva Tip: Double '==' vs Single '=' ka farq yaad rakhna!" : "Viva Tip: State difference between '==' and '='.";
      } else if (trimmed.includes("[::-1]")) {
        tip = isHi ? "List Slicing — Sequence ko reverse shallow-copy kar raha hai." : "List slicing idiom creating a reversed copy.";
        viva = isHi ? "Viva Tip: Iska time complexity O(N) hota hai." : "Viva Tip: Complexity is O(N).";
      } else if (trimmed.startsWith("def ")) {
        tip = isHi ? "Function Definition — Reusable modular logic block." : "Function declaration creating reusable block.";
        viva = isHi ? "Viva Tip: Parameters aur Arguments ka difference puch sakte hain." : "Viva Tip: Differentiate parameters vs arguments.";
      }

      return `
        <div class="xray-line-item">
          <div style="display:flex; justify-content:space-between; margin-bottom: 4px;">
            <span style="font-family:var(--font-mono); font-size:0.8rem; color:var(--accent-cyan);">Line ${idx+1}: <code>${this._escapeHtml(trimmed)}</code></span>
          </div>
          <div style="font-size:0.85rem; color:#cbd5e1;">${tip}</div>
          <div style="font-size:0.8rem; color:#fbbf24; margin-top:4px;">🎯 ${viva}</div>
        </div>
      `;
    }).join("");
  }

  // =========================================================================
  // PAGE 6: 10-MINUTE LAB PANIC MODE
  // =========================================================================

  /**
   * 📌 RENDER PANIC MODE: Emergency 10-minute lab survival kit
   * 👁️ WEB PAGE PE KYA DIKHTA HAI:
   *   Top 3 critical topics ke sabse khatarnak traps aur teacher ke favourite viva sawal.
   */
  renderPanicMode() {
    const isHi = this.lang === "hi";
    const container = document.getElementById("panic-content-container");
    if (!container || !this.curriculum) return;

    const topics = (this.curriculum[this.subject] && this.curriculum[this.subject].topics) || [];
    
    container.innerHTML = `
      <div style="text-align:center; margin-bottom: 24px;">
        <h2 style="font-size:1.8rem; font-weight:800; color:#f43f5e;">🚨 10-Minute Lab Panic Rescue</h2>
        <p style="color:#cbd5e1; font-size:1rem; margin-top:4px;">
          ${isHi ? "Lab shuru hone wali hai? In 3 high-yield topics ke common traps aur viva questions rat lo!" : "Entering the lab in 10 minutes? Memorize these high-yield traps and viva questions right now!"}
        </p>
      </div>

      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); gap: 20px;">
        ${topics.slice(0, 3).map((t, idx) => `
          <div class="theory-card-3d card-3d-tilt" style="max-height:none;">
            <div class="lesson-header">
              <span class="lesson-tag">CRITICAL TOPIC #${idx+1}</span>
              <h3 class="lesson-title"><span>${t.icon}</span> ${t.title}</h3>
            </div>
            <div class="mistake-card">
              <div class="mistake-header">⚠️ ${isHi ? "Sabse Badi Galti (Examiner Red Flag):" : "The #1 Trap:"}</div>
              <div class="mistake-snippet">${this._escapeHtml(t.common_mistakes[0].mistake)}</div>
              <div class="mistake-fix">${this._escapeHtml(t.common_mistakes[0].fix)}</div>
            </div>
            <div class="viva-accordion">
              <div class="viva-title">🎙️ ${isHi ? "Teacher ka Favourite Sawaal:" : "Top Viva Question:"}</div>
              <p style="font-size:0.88rem; color:#fff; font-weight:600;">${t.viva_questions[0].question}</p>
              <p style="font-size:0.82rem; color:#94a3b8; margin-top:4px;">
                <strong>${isHi ? "Bolna kya hai:" : "What to say:"}</strong> ${isHi ? t.viva_questions[0].answer_hi : t.viva_questions[0].answer_en}
              </p>
            </div>
          </div>
        `).join("")}
      </div>
    `;
  }

  // =========================================================================
  // MODALS: LAB RECORD EXPORTER & 3D FLEX CARD
  // =========================================================================

  /**
   * 📌 OPEN LAB EXPORTER MODAL: College Practical Lab Sheet popup kholta hai
   */
  openLabExporterModal() {
    window.elysiaAudio.playClick();
    const modal = document.getElementById("modal-lab-exporter");
    if (modal) modal.classList.add("active");
  }

  /**
   * 📌 CLOSE MODAL: Kisi bhi open popup modal ko close karta hai
   */
  closeModal(modalId) {
    window.elysiaAudio.playClick();
    const modal = document.getElementById(modalId);
    if (modal) modal.classList.remove("active");
  }

  closeAllModals() {
    window.elysiaAudio.playClick();
    document.querySelectorAll(".modal-overlay.active").forEach(m => m.classList.remove("active"));
  }

  /**
   * 📌 GENERATE LAB FILE: Ready-to-Print College Lab Manual HTML/PDF banata hai
   * 📌 KYA KAAM HAI:
   *   Student ka Name, Roll No, Experiment Aim, Algorithm, Code, aur Viva Q&A 
   *   lekar ek professional standard college lab file generate karta hai.
   * 👁️ WEB PAGE PE KYA DIKHTA HAI:
   *   Nayi browser tab me official looking printable lab record khulta hai (`window.print()` ready).
   * 💡 KYUN USE KIYA:
   *   College students ko lab file likhne me ghanton lagte hain; 
   *   ye automated generator unka 90% time bachaata hai.
   */
  async generateLabFile() {
    window.elysiaAudio.playClick();
    const name = document.getElementById("exporter-name").value || "Alex Doe";
    const roll = document.getElementById("exporter-roll").value || "12200123";
    const course = document.getElementById("exporter-course").value || "CSE205";

    const topics = this.curriculum[this.subject].topics || [];
    const t = topics[this.currentTopicIndex] || topics[0];

    const payload = {
      student_name: name,
      roll_no: roll,
      course_code: course,
      exp_no: this.currentTopicIndex + 1,
      title: t.title,
      aim: `To implement, test and analyze ${t.title} using ${this.subject.toUpperCase()} programming.`,
      algorithm: [
        "Start the program execution.",
        "Declare and initialize the primary data structures and variables.",
        "Execute logical expressions and constraints.",
        "Display output to standard output stream.",
        "Stop the program."
      ],
      code: t.solution_code || t.starter_code,
      sample_output: (t.test_cases && t.test_cases[0] && t.test_cases[0].expected_output) || "Execution completed successfully.",
      viva_qa: t.viva_questions || []
    };

    const res = await fetch("/api/generate-lab-sheet", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    const html = await res.text();
    const win = window.open("", "_blank");
    win.document.open();
    win.document.write(html);
    win.document.close();
  }

  /**
   * 📌 OPEN FLEX MODAL: 3D Achievement Flex Card modal open karta hai
   */
  openFlexModal() {
    window.elysiaAudio.playClick();
    const modal = document.getElementById("modal-flex-card");
    if (modal) modal.classList.add("active");
  }

  /**
   * 📌 SHARE ON WHATSAPP: Doston ke saath achievement share karne ka link banata hai
   */
  shareOnWhatsApp() {
    const text = encodeURIComponent("Bro! Maine Elysia Code par Python & HTML concepts 10 minute me master kar liye bina kisi jhanjhat ke! Check it out: " + window.location.href);
    window.open(`https://api.whatsapp.com/send?text=${text}`, "_blank");
  }

  // =========================================================================
  // VISUAL PYTHON HANDBOOK (E-BOOK) CONTROLLER
  // =========================================================================

  /**
   * 📌 LOAD HANDBOOK: 180+ Slides ki Visual Python E-Book load karta hai
   * 💡 Kyun: Pre-bundled `window.HANDBOOK_CHAPTERS` check karta hai taaki 
   *    bina server ya offline hone par bhi 0 millisecond me handbook khul sake.
   */
  async loadHandbook() {
    // 1. Instant offline / pre-bundled load
    if (window.HANDBOOK_CHAPTERS && window.HANDBOOK_CHAPTERS.length > 0) {
      this.handbookChapters = window.HANDBOOK_CHAPTERS;
      this.renderHandbookChaptersStrip();
      this.renderHandbookSlide();
    }

    // 2. Network sync if running on live server
    try {
      const res = await fetch("/api/handbook");
      if (res.ok) {
        const data = await res.json();
        if (data.chapters && data.chapters.length > 0) {
          this.handbookChapters = data.chapters;
          this.renderHandbookChaptersStrip();
          this.renderHandbookSlide();
        }
      }
    } catch (e) {
      // Pre-bundled data already active!
    }
  }

  /**
   * 📌 RENDER HANDBOOK CHAPTERS STRIP: 8 Chapters ka horizontal scroll strip banata hai
   */
  renderHandbookChaptersStrip() {
    const strip = document.getElementById("handbook-chapters-strip");
    if (!strip || !this.handbookChapters) return;

    strip.innerHTML = this.handbookChapters.map((ch, idx) => `
      <button class="handbook-chapter-btn ${idx === this.currentHandbookChIdx ? 'active' : ''}" onclick="window.elysiaApp.selectHandbookChapter(${idx})">
        <span>#${ch.number}</span> ${ch.title}
      </button>
    `).join("");
  }

  /**
   * 📌 SELECT HANDBOOK CHAPTER: Naya chapter choose hone par slide 0 se shuru karta hai
   */
  selectHandbookChapter(idx) {
    this.currentHandbookChIdx = idx;
    this.currentHandbookSlideIdx = 0;
    window.elysiaAudio.playClick();
    this.renderHandbookChaptersStrip();
    this.renderHandbookSlide();
  }

  /**
   * 📌 RENDER HANDBOOK SLIDE: Current slide ka visual diagram, notes, tips, aur code render karta hai
   * 👁️ WEB PAGE PE KYA DIKHTA HAI:
   *   Left panel me flowchart/mental-model aur Right panel me bullet notes aur executable code snippet.
   */
  renderHandbookSlide() {
    if (!this.handbookChapters || this.handbookChapters.length === 0) return;

    const ch = this.handbookChapters[this.currentHandbookChIdx];
    if (!ch || !ch.slides) return;

    const slide = ch.slides[this.currentHandbookSlideIdx] || ch.slides[0];
    const isHi = this.lang === "hi";

    // Text elements grab kiye
    const badgeEl = document.getElementById("slide-topic-badge");
    const numEl = document.getElementById("slide-number-indicator");
    const quickNumEl = document.getElementById("slide-quick-indicator");
    const titleEl = document.getElementById("slide-title");
    const conceptEl = document.getElementById("slide-concept");
    const analogyEl = document.getElementById("slide-analogy");
    const notesListEl = document.getElementById("slide-notes-list");
    const whenUseEl = document.getElementById("slide-when-use");
    const whenUseBox = document.getElementById("slide-when-use-box");
    const codeSnippetEl = document.getElementById("slide-code-snippet");

    if (badgeEl) badgeEl.textContent = `#${ch.number} ${ch.title.toUpperCase()}`;
    if (numEl) numEl.textContent = `Slide ${this.currentHandbookSlideIdx + 1} of ${ch.slides.length}`;
    if (quickNumEl) quickNumEl.textContent = `Slide ${this.currentHandbookSlideIdx + 1} / ${ch.slides.length}`;
    if (titleEl) titleEl.textContent = slide.title;
    if (conceptEl) conceptEl.textContent = slide.concept;
    if (analogyEl) analogyEl.textContent = isHi ? slide.analogy_hi : slide.analogy_en;
    if (codeSnippetEl) codeSnippetEl.textContent = slide.code || "# No code required";

    // Structured notes bullet points
    if (notesListEl) {
      const notes = isHi ? (slide.notes_hi || slide.notes_en) : slide.notes_en;
      notesListEl.innerHTML = (notes || []).map(n => `<li>${n}</li>`).join("");
    }

    // "When to use" production context box
    if (whenUseEl && whenUseBox) {
      const whenText = isHi ? (slide.when_to_use_hi || slide.when_to_use_en) : slide.when_to_use_en;
      if (whenText) {
        whenUseBox.style.display = "block";
        whenUseEl.textContent = whenText;
      } else {
        whenUseBox.style.display = "none";
      }
    }

    // Dynamic Visual Graphic render kiya
    this.renderHandbookVisual(slide);
  }

  /**
   * 📌 RENDER HANDBOOK VISUAL: Diagram type ke according custom graphics generate karta hai
   * 👁️ Web Page Pe Effect:
   *   - 'flow_diagram': Idea ➔ Python ➔ Output flowchart.
   *   - 'level_stack': Natural Language ⬇️ Python ⬇️ C/Assembly ⬇️ Machine Code stack.
   *   - 'pipeline': .py ➔ Compiler ➔ Bytecode (.pyc) ➔ PVM ➔ CPU pipeline.
   *   - 'slice_diagram': Positive (0 to 5) aur Negative (-6 to -1) index visualization.
   *   - 'truthy_table': Truthy vs Falsy comparison matrix.
   *   - 'pointer_diagram': `==` vs `is` identity memory address pointers.
   *   - 'for_else_cycle': For-Else loop completion vs break cycle.
   */
  renderHandbookVisual(slide) {
    const container = document.getElementById("slide-visual-display");
    if (!container) return;

    const vt = slide.visual_type || "";
    let html = "";

    if (vt === "flow_diagram") {
      html = `
        <div style="display:flex; align-items:center; justify-content:center; gap:14px; flex-wrap:wrap;">
          <div class="diagram-node" style="border-color:#38bdf8;">👤 Human Idea<br><span style="font-size:0.75rem; color:#94a3b8;">"Please add 5+5"</span></div>
          <span class="diagram-arrow">➔</span>
          <div class="diagram-node" style="border-color:#a855f7;">📜 Python Code<br><span style="font-family:var(--font-mono); font-size:0.75rem; color:#a7f3d0;">print(5 + 5)</span></div>
          <span class="diagram-arrow">➔</span>
          <div class="diagram-node" style="border-color:#10b981;">💻 Computer Output<br><span style="font-family:var(--font-mono); font-size:1.1rem; color:#34d399; font-weight:800;">10</span></div>
        </div>
      `;
    } else if (vt === "level_stack") {
      html = `
        <div style="display:flex; flex-direction:column; gap:8px; width:100%; max-width:380px;">
          <div style="background:rgba(56,189,248,0.15); border:1px solid #38bdf8; border-radius:8px; padding:8px 14px; font-weight:700; color:#fff; display:flex; justify-content:space-between;">
            <span>Natural Language</span> <span style="font-size:0.75rem; color:#38bdf8;">Human (English/Hindi)</span>
          </div>
          <div style="text-align:center; color:#64748b; font-size:0.8rem;">⬇️ High-Level Abstraction</div>
          <div style="background:rgba(168,85,247,0.2); border:2px solid #a855f7; border-radius:8px; padding:10px 14px; font-weight:800; color:#fff; display:flex; justify-content:space-between;">
            <span>Python 3.11</span> <span style="font-size:0.75rem; color:#c084fc;">Human-Friendly & Powerful</span>
          </div>
          <div style="text-align:center; color:#64748b; font-size:0.8rem;">⬇️ Low-Level Hardware Translation</div>
          <div style="background:rgba(245,158,11,0.15); border:1px solid #f59e0b; border-radius:8px; padding:8px 14px; font-weight:700; color:#fff; display:flex; justify-content:space-between;">
            <span>Assembly / C</span> <span style="font-size:0.75rem; color:#fcd34d;">Registers & Memory</span>
          </div>
          <div style="text-align:center; color:#64748b; font-size:0.8rem;">⬇️ Hardware Execution</div>
          <div style="background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:8px; padding:8px 14px; font-weight:700; color:#fff; display:flex; justify-content:space-between;">
            <span>Machine Code</span> <span style="font-family:var(--font-mono); font-size:0.75rem; color:#34d399;">1010011001</span>
          </div>
        </div>
      `;
    } else if (vt === "pipeline") {
      html = `
        <div style="display:flex; align-items:center; justify-content:center; gap:10px; flex-wrap:wrap;">
          <div class="diagram-node">📄 Source<br><span style="font-size:0.75rem; color:#38bdf8;">.py</span></div>
          <span class="diagram-arrow">➔</span>
          <div class="diagram-node" style="border-color:#f59e0b;">⚙️ Compiler<br><span style="font-size:0.75rem; color:#fcd34d;">Bytecode</span></div>
          <span class="diagram-arrow">➔</span>
          <div class="diagram-node" style="border-color:#a855f7;">📦 .pyc<br><span style="font-size:0.75rem; color:#c084fc;">Instructions</span></div>
          <span class="diagram-arrow">➔</span>
          <div class="diagram-node" style="border-color:#38bdf8;">🖥️ PVM<br><span style="font-size:0.75rem; color:#38bdf8;">Virtual Machine</span></div>
          <span class="diagram-arrow">➔</span>
          <div class="diagram-node" style="border-color:#10b981;">⚡ CPU<br><span style="font-size:0.75rem; color:#34d399;">Output</span></div>
        </div>
      `;
    } else if (vt === "slice_diagram") {
      html = `
        <div style="font-family:var(--font-mono);">
          <div style="display:flex; gap:6px; justify-content:center; margin-bottom:4px;">
            <span style="width:40px; text-align:center; color:#38bdf8; font-size:0.75rem;">0</span>
            <span style="width:40px; text-align:center; color:#38bdf8; font-size:0.75rem;">1</span>
            <span style="width:40px; text-align:center; color:#38bdf8; font-size:0.75rem;">2</span>
            <span style="width:40px; text-align:center; color:#38bdf8; font-size:0.75rem;">3</span>
            <span style="width:40px; text-align:center; color:#38bdf8; font-size:0.75rem;">4</span>
            <span style="width:40px; text-align:center; color:#38bdf8; font-size:0.75rem;">5</span>
          </div>
          <div style="display:flex; gap:6px; justify-content:center; margin-bottom:4px;">
            <div style="width:40px; height:40px; border:2px solid #a855f7; border-radius:6px; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:1.1rem; color:#fff;">P</div>
            <div style="width:40px; height:40px; border:2px solid #a855f7; border-radius:6px; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:1.1rem; color:#fff;">Y</div>
            <div style="width:40px; height:40px; border:2px solid #a855f7; border-radius:6px; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:1.1rem; color:#fff;">T</div>
            <div style="width:40px; height:40px; border:2px solid #a855f7; border-radius:6px; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:1.1rem; color:#fff;">H</div>
            <div style="width:40px; height:40px; border:2px solid #a855f7; border-radius:6px; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:1.1rem; color:#fff;">O</div>
            <div style="width:40px; height:40px; border:2px solid #a855f7; border-radius:6px; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:1.1rem; color:#fff;">N</div>
          </div>
          <div style="display:flex; gap:6px; justify-content:center;">
            <span style="width:40px; text-align:center; color:#f43f5e; font-size:0.75rem;">-6</span>
            <span style="width:40px; text-align:center; color:#f43f5e; font-size:0.75rem;">-5</span>
            <span style="width:40px; text-align:center; color:#f43f5e; font-size:0.75rem;">-4</span>
            <span style="width:40px; text-align:center; color:#f43f5e; font-size:0.75rem;">-3</span>
            <span style="width:40px; text-align:center; color:#f43f5e; font-size:0.75rem;">-2</span>
            <span style="width:40px; text-align:center; color:#f43f5e; font-size:0.75rem;">-1</span>
          </div>
          <div style="margin-top:16px; font-size:0.85rem; color:#a7f3d0;">text[1:4] ➔ Extracts 'YTH' (Index 1 to 3, Stop is excluded!)</div>
        </div>
      `;
    } else if (vt === "truthy_table") {
      html = `
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; width:100%; max-width:440px;">
          <div style="background:rgba(16,185,129,0.12); border:1px solid #10b981; border-radius:12px; padding:12px; text-align:left;">
            <div style="color:#34d399; font-weight:800; font-size:0.85rem; margin-bottom:6px;">🟢 TRUTHY (Meaningful)</div>
            <div style="font-family:var(--font-mono); font-size:0.8rem; color:#fff; line-height:1.8;">
              • True<br>• 5, -3, 0.1 (non-zero)<br>• 'Hi', 'False' (strings)<br>• [1, 2], {'a': 1}
            </div>
          </div>
          <div style="background:rgba(244,63,94,0.12); border:1px solid #f43f5e; border-radius:12px; padding:12px; text-align:left;">
            <div style="color:#fb7185; font-weight:800; font-size:0.85rem; margin-bottom:6px;">🔴 FALSY (Empty/Zero)</div>
            <div style="font-family:var(--font-mono); font-size:0.8rem; color:#fff; line-height:1.8;">
              • False<br>• None<br>• 0, 0.0<br>• '' (empty string)<br>• [], {}, set() (empty)
            </div>
          </div>
        </div>
      `;
    } else if (vt === "pointer_diagram") {
      html = `
        <div style="display:flex; flex-direction:column; gap:16px; align-items:center;">
          <div style="display:flex; gap:20px; align-items:center;">
            <div class="diagram-node" style="border-color:#38bdf8;">list1<br><span style="font-size:0.75rem; color:#94a3b8;">Address: 0x100</span></div>
            <span style="color:#10b981; font-weight:800; font-size:1.1rem;">== (True)</span>
            <div class="diagram-node" style="border-color:#38bdf8;">list2<br><span style="font-size:0.75rem; color:#94a3b8;">Address: 0x200</span></div>
          </div>
          <div style="background:rgba(244,63,94,0.15); border:1px solid #f43f5e; border-radius:8px; padding:8px 18px; color:#fecdd3; font-weight:700; font-size:0.85rem;">
            list1 is list2 ➔ ❌ FALSE (Different memory addresses!)
          </div>
        </div>
      `;
    } else if (vt === "for_else_cycle") {
      html = `
        <div style="display:flex; flex-direction:column; gap:12px; align-items:center;">
          <div style="background:rgba(0,0,0,0.4); border:2px dashed #a855f7; border-radius:14px; padding:14px 24px; text-align:center;">
            <span style="font-weight:800; color:#fff;">🔄 For Loop Execution</span>
          </div>
          <div style="display:flex; gap:24px;">
            <div style="background:rgba(244,63,94,0.15); border:1px solid #f43f5e; border-radius:8px; padding:10px 14px; font-size:0.8rem; text-align:center;">
              <strong style="color:#fb7185;">Case 1: Hit 'break'</strong><br>Loop broken ➔ <span style="color:#fecdd3;">else SKIPPED</span>
            </div>
            <div style="background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:8px; padding:10px 14px; font-size:0.8rem; text-align:center;">
              <strong style="color:#34d399;">Case 2: No 'break'</strong><br>Loop finished ➔ <span style="color:#a7f3d0;">else RUNS!</span>
            </div>
          </div>
        </div>
      `;
    } else {
      // Default interactive mental model display
      html = `
        <div style="display:flex; flex-direction:column; align-items:center; gap:12px;">
          <div style="font-size:2.8rem;">🧠</div>
          <div style="font-weight:800; color:#fff; font-size:1.1rem;">${slide.title}</div>
          <div style="color:#94a3b8; font-size:0.88rem; max-width:340px;">${slide.concept}</div>
        </div>
      `;
    }

    container.innerHTML = html;
  }

  /**
   * 📌 NEXT HANDBOOK SLIDE: Agli slide par move karta hai
   */
  nextHandbookSlide() {
    if (!this.handbookChapters) return;
    const ch = this.handbookChapters[this.currentHandbookChIdx];
    if (this.currentHandbookSlideIdx < ch.slides.length - 1) {
      this.currentHandbookSlideIdx++;
      window.elysiaAudio.playClick();
      this.renderHandbookSlide();
    } else if (this.currentHandbookChIdx < this.handbookChapters.length - 1) {
      // Current chapter khatam, agla chapter start kiya
      this.currentHandbookChIdx++;
      this.currentHandbookSlideIdx = 0;
      window.elysiaAudio.playClick();
      this.renderHandbookChaptersStrip();
      this.renderHandbookSlide();
    }
  }

  /**
   * 📌 PREV HANDBOOK SLIDE: Pichhli slide par move karta hai
   */
  prevHandbookSlide() {
    if (this.currentHandbookSlideIdx > 0) {
      this.currentHandbookSlideIdx--;
      window.elysiaAudio.playClick();
      this.renderHandbookSlide();
    } else if (this.currentHandbookChIdx > 0) {
      // Pichhle chapter ki aakhri slide par move kiya
      this.currentHandbookChIdx--;
      const ch = this.handbookChapters[this.currentHandbookChIdx];
      this.currentHandbookSlideIdx = ch.slides.length - 1;
      window.elysiaAudio.playClick();
      this.renderHandbookChaptersStrip();
      this.renderHandbookSlide();
    }
  }

  /**
   * 📌 SEND SLIDE TO SANDBOX: E-Book ke slide ke code snippet ko IDE me paste karke tab switch karta hai
   * 👁️ Web Page Pe Effect: Code editor me slide ka code copy ho jata hai aur student turant run karke dekh sakta hai.
   */
  sendSlideToSandbox() {
    if (!this.handbookChapters) return;
    const ch = this.handbookChapters[this.currentHandbookChIdx];
    const slide = ch.slides[this.currentHandbookSlideIdx];
    if (!slide || !slide.code) return;

    this.setCode(slide.code);

    // Switch to Learn & Code tab
    this.switchTab("learn");
  }

  /**
   * 📌 HANDLE HANDBOOK SEARCH: Handbook ke 180 slides me keyword search karta hai
   */
  handleHandbookSearch(query) {
    if (!query || query.trim().length < 2) return;
    const q = query.trim().toLowerCase();
    
    for (let c = 0; c < this.handbookChapters.length; c++) {
      const ch = this.handbookChapters[c];
      for (let s = 0; s < ch.slides.length; s++) {
        const slide = ch.slides[s];
        if (slide.title.toLowerCase().includes(q) || slide.concept.toLowerCase().includes(q)) {
          this.currentHandbookChIdx = c;
          this.currentHandbookSlideIdx = s;
          this.renderHandbookChaptersStrip();
          this.renderHandbookSlide();
          return;
        }
      }
    }
  }

  /**
   * 📌 _ESCAPE HTML: Cross-Site Scripting (XSS) attack se bachane ke liye special characters sanitize karta hai
   */
  _escapeHtml(str) {
    if (!str) return "";
    return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  // =========================================================================
  // ⚡ HABIT LOOP, PRODUCTIVITY & GAMIFICATION METHODS
  // =========================================================================

  /**
   * 📌 INIT STUDY TIMER: Real-time study time counter track karta hai
   */
  _initStudyTimer() {
    const today = new Date().toISOString().slice(0, 10);
    if (this.lastStudyDate !== today) {
      this.todaySeconds = 0;
      localStorage.setItem("elysia_today_sec", "0");
    }

    setInterval(() => {
      this.todaySeconds++;
      this.totalSeconds++;

      const timerEl = document.getElementById("nav-timer-display");
      if (timerEl) {
        timerEl.textContent = this.formatTime(this.todaySeconds);
      }

      if (this.todaySeconds % 5 === 0) {
        localStorage.setItem("elysia_today_sec", this.todaySeconds.toString());
        localStorage.setItem("elysia_total_sec", this.totalSeconds.toString());
        localStorage.setItem("elysia_last_study_date", today);
      }
    }, 1000);
  }

  /**
   * 📌 INIT STREAK: Daily learning streak verify aur increment karta hai
   */
  _initStreak() {
    const today = new Date().toISOString().slice(0, 10);
    if (this.lastStudyDate !== today) {
      const last = new Date(this.lastStudyDate);
      const now = new Date(today);
      const diffDays = Math.round((now - last) / (1000 * 60 * 60 * 24));
      if (diffDays === 1) {
        this.streak++;
      } else if (diffDays > 1) {
        this.streak = 1;
      }
      localStorage.setItem("elysia_streak", this.streak.toString());
      localStorage.setItem("elysia_last_study_date", today);
    }
  }

  formatTime(totalSec) {
    const hrs = Math.floor(totalSec / 3600).toString().padStart(2, "0");
    const mins = Math.floor((totalSec % 3600) / 60).toString().padStart(2, "0");
    const secs = (totalSec % 60).toString().padStart(2, "0");
    return `${hrs}:${mins}:${secs}`;
  }

  formatTimeHuman(totalSec) {
    const hrs = Math.floor(totalSec / 3600);
    const mins = Math.floor((totalSec % 3600) / 60);
    const secs = totalSec % 60;
    if (hrs > 0) return `${hrs}h ${mins}m`;
    if (mins > 0) return `${mins}m ${secs}s`;
    return `${secs}s`;
  }

  addXP(pts) {
    this.xp += pts;
    localStorage.setItem("elysia_xp", this.xp.toString());
    this.updateGamificationUI();
    this.showOptimisticToast(`⚡ +${pts} XP! Progress saved.`, "success");
    this.syncUserProgress();
  }

  getEgoTier() {
    if (this.xp >= 1000) return { title: "GRANDMASTER", rank: "Grandmaster", level: 5, emoji: "👑", motto: "Python is second nature. Ready for AI & Cloud!" };
    if (this.xp >= 600) return { title: "PYTHON SLAYER", rank: "Python Slayer", level: 4, emoji: "🐍", motto: "Functions, loops and logic bow before you." };
    if (this.xp >= 300) return { title: "SYNTAX WARRIOR", rank: "Syntax Warrior", level: 3, emoji: "⚔️", motto: "Bugs fear your debugging instinct." };
    if (this.xp >= 100) return { title: "KEYBOARD TOURIST", rank: "Keyboard Tourist", level: 2, emoji: "💻", motto: "Beyond the basics, stepping into real programming." };
    return { title: "NOOB", rank: "Noob", level: 1, emoji: "🐣", motto: "First steps into the matrix. The journey begins!" };
  }

  updateGamificationUI() {
    const tier = this.getEgoTier();

    const streakEl = document.getElementById("nav-streak-count");
    if (streakEl) streakEl.textContent = this.streak.toString();

    const xpEl = document.getElementById("nav-xp-count");
    if (xpEl) xpEl.textContent = this.xp.toString();

    const profileRankEl = document.getElementById("nav-profile-rank");
    if (profileRankEl) profileRankEl.textContent = tier.rank;

    this.updateAuthUI();
  }

  /**
   * 📌 OPEN MODAL: Generic Modal Opener
   */
  openModal(modalId) {
    window.elysiaAudio.playClick();
    const modal = document.getElementById(modalId);
    if (modal) modal.classList.add("active");
    if (modalId === "modal-user-profile") {
      this.updateProfileModalUI();
    }
  }

  /**
   * 📌 UPDATE PROFILE MODAL UI: Profile metrics, streak calendar aur rank calculate karta hai
   */
  updateProfileModalUI() {
    const tier = this.getEgoTier();

    const userNameEl = document.getElementById("prof-user-name");
    if (userNameEl) {
      userNameEl.textContent = this.currentUser?.name || "Future Python Architect";
    }

    const avatarImgEl = document.getElementById("prof-avatar-img");
    const avatarEmojiEl = document.getElementById("prof-avatar");
    const userAvatar = this.currentUser?.avatar;

    if (userAvatar && userAvatar.startsWith("data:image")) {
      if (avatarImgEl) {
        avatarImgEl.src = userAvatar;
        avatarImgEl.style.display = "block";
      }
      if (avatarEmojiEl) avatarEmojiEl.style.display = "none";
    } else {
      if (avatarImgEl) avatarImgEl.style.display = "none";
      if (avatarEmojiEl) {
        avatarEmojiEl.style.display = "inline-block";
        avatarEmojiEl.textContent = userAvatar || tier.emoji;
      }
    }

    const egoTierEl = document.getElementById("prof-ego-tier");
    if (egoTierEl) egoTierEl.textContent = tier.title;

    const levelTagEl = document.getElementById("prof-level-tag");
    if (levelTagEl) levelTagEl.textContent = `Level ${tier.level}`;

    const mottoEl = document.getElementById("prof-ego-motto");
    if (mottoEl) {
      mottoEl.textContent = this.currentUser?.motto ? `"${this.currentUser.motto}"` : `"${tier.motto}"`;
    }

    const timeTodayEl = document.getElementById("prof-time-today");
    if (timeTodayEl) timeTodayEl.textContent = this.formatTimeHuman(this.todaySeconds);

    const timeTotalEl = document.getElementById("prof-time-total");
    if (timeTotalEl) timeTotalEl.textContent = this.formatTimeHuman(this.totalSeconds);

    const streakValEl = document.getElementById("prof-streak-val");
    if (streakValEl) streakValEl.textContent = `${this.streak} Day${this.streak > 1 ? 's' : ''}`;

    const xpValEl = document.getElementById("prof-xp-val");
    if (xpValEl) xpValEl.textContent = `${this.xp} XP`;

    const xpDetailsEl = document.getElementById("prof-xp-details");
    const xpFillEl = document.getElementById("prof-xp-fill");
    const nextLevelXP = tier.level === 5 ? 1500 : (tier.level * 250);
    const prevLevelXP = (tier.level - 1) * 200;
    const progressPct = Math.min(100, Math.round(((this.xp - prevLevelXP) / Math.max(1, nextLevelXP - prevLevelXP)) * 100));
    if (xpDetailsEl) xpDetailsEl.textContent = `${this.xp} / ${nextLevelXP} XP`;
    if (xpFillEl) xpFillEl.style.width = `${Math.max(5, progressPct)}%`;

    const totalSub = this.getTotalSubtopicsCount();
    const completedCount = this.completedSubtopics.size;
    const subtopicsFractionEl = document.getElementById("prof-subtopics-fraction");
    const curriculumFillEl = document.getElementById("prof-curriculum-fill");
    if (subtopicsFractionEl) subtopicsFractionEl.textContent = `${completedCount} / ${totalSub} Subtopics`;
    if (curriculumFillEl) {
      const subPct = totalSub > 0 ? Math.round((completedCount / totalSub) * 100) : 0;
      curriculumFillEl.style.width = `${subPct}%`;
    }
  }

  // ===========================================================================
  // 🔐 AUTHENTICATION & PROFILE METHODS (SIGN IN, SIGN UP, PHOTO UPLOAD, LOGOUT)
  // ===========================================================================

  openAuthModal() {
    this.switchAuthTab("login");
    this.openModal("modal-auth");
  }

  updateAuthUI() {
    const authBtn = document.getElementById("btn-open-auth");
    const profileBtn = document.getElementById("btn-open-profile");
    const nameEl = document.getElementById("nav-user-display-name");
    const rankEl = document.getElementById("nav-profile-rank");
    const avatarImgEl = document.getElementById("nav-user-avatar-img");
    const avatarEmojiEl = document.getElementById("nav-user-avatar-emoji");
    const aiQBtn = document.getElementById("btn-ai-generate-qbank");
    const tier = this.getEgoTier();

    if (this.currentUser) {
      if (aiQBtn) {
        aiQBtn.innerHTML = `<span>✨</span> Generate with Groq AI`;
        aiQBtn.onclick = () => this.generateAIQuestion();
      }
      if (authBtn) authBtn.style.display = "none";
      if (profileBtn) profileBtn.style.display = "inline-flex";
      if (nameEl) nameEl.textContent = this.currentUser.name || this.currentUser.username || "Coder";
      if (rankEl) rankEl.textContent = tier.rank;

      const sideName = document.getElementById("side-user-name");
      const sideRole = document.getElementById("side-user-role");
      const sideAvatarImg = document.getElementById("side-avatar-img");
      const sideAvatarEmoji = document.getElementById("side-avatar-emoji");
      const heroProfBtn = document.getElementById("btn-hero-profile");

      const uName = this.currentUser.name || this.currentUser.username || "Priyanshu";
      if (sideName) sideName.textContent = uName;
      if (sideRole) sideRole.textContent = tier.rank || "Student";
      if (heroProfBtn) heroProfBtn.textContent = uName.charAt(0).toUpperCase();

      if (avatar && avatar.startsWith("data:image")) {
        if (sideAvatarImg) { sideAvatarImg.src = avatar; sideAvatarImg.style.display = "block"; }
        if (sideAvatarEmoji) sideAvatarEmoji.style.display = "none";
      } else {
        if (sideAvatarImg) sideAvatarImg.style.display = "none";
        if (sideAvatarEmoji) { sideAvatarEmoji.style.display = "inline-block"; sideAvatarEmoji.textContent = avatar || "🐍"; }
      }


      const avatar = this.currentUser.avatar;
      if (avatar && avatar.startsWith("data:image")) {
        if (avatarImgEl) {
          avatarImgEl.src = avatar;
          avatarImgEl.style.display = "block";
        }
        if (avatarEmojiEl) avatarEmojiEl.style.display = "none";
      } else {
        if (avatarImgEl) avatarImgEl.style.display = "none";
        if (avatarEmojiEl) {
          avatarEmojiEl.style.display = "inline-block";
          avatarEmojiEl.textContent = avatar || "🐍";
        }
      }
    } else {
      if (aiQBtn) {
        aiQBtn.innerHTML = `<span>🔒</span> Log in to generate AI questions`;
        aiQBtn.onclick = () => this.openAuthModal();
      }
      if (authBtn) authBtn.style.display = "inline-flex";
      if (profileBtn) profileBtn.style.display = "none";
    }
  }

  switchAuthTab(tab) {
    const tabLogin = document.getElementById("tab-btn-login");
    const tabSignup = document.getElementById("tab-btn-signup");
    const viewLogin = document.getElementById("auth-login-view");
    const viewSignup = document.getElementById("auth-signup-view");
    this.hideAuthFeedback();

    if (tab === "login") {
      if (tabLogin) tabLogin.classList.add("active");
      if (tabSignup) tabSignup.classList.remove("active");
      if (viewLogin) viewLogin.style.display = "block";
      if (viewSignup) viewSignup.style.display = "none";
    } else {
      if (tabSignup) tabSignup.classList.add("active");
      if (tabLogin) tabLogin.classList.remove("active");
      if (viewSignup) viewSignup.style.display = "block";
      if (viewLogin) viewLogin.style.display = "none";
    }
  }

  showAuthFeedback(message, isError = false) {
    const banner = document.getElementById("auth-feedback-banner");
    if (!banner) return;
    banner.textContent = message;
    banner.style.display = "block";
    if (isError) {
      banner.style.background = "rgba(239, 68, 68, 0.15)";
      banner.style.color = "#f87171";
      banner.style.borderColor = "rgba(239, 68, 68, 0.4)";
    } else {
      banner.style.background = "rgba(16, 185, 129, 0.15)";
      banner.style.color = "#34d399";
      banner.style.borderColor = "rgba(16, 185, 129, 0.4)";
    }
  }

  hideAuthFeedback() {
    const banner = document.getElementById("auth-feedback-banner");
    if (banner) banner.style.display = "none";
  }

  selectPresetAvatar(emoji, isEdit = false) {
    if (isEdit) {
      this.selectedEditAvatar = emoji;
      const previewImg = document.getElementById("edit-avatar-preview-img");
      const previewEmoji = document.getElementById("edit-avatar-preview-emoji");
      const fn = document.getElementById("edit-photo-filename");
      if (previewImg) previewImg.style.display = "none";
      if (previewEmoji) {
        previewEmoji.textContent = emoji;
        previewEmoji.style.display = "inline-block";
      }
      if (fn) fn.textContent = "";
      document.querySelectorAll("#modal-edit-profile .avatar-opt-btn").forEach(btn => {
        btn.classList.toggle("active", btn.dataset.avatar === emoji);
      });
    } else {
      this.selectedAvatar = emoji;
      const previewImg = document.getElementById("auth-avatar-preview-img");
      const previewEmoji = document.getElementById("auth-avatar-preview-emoji");
      const fn = document.getElementById("auth-photo-filename");
      if (previewImg) previewImg.style.display = "none";
      if (previewEmoji) {
        previewEmoji.textContent = emoji;
        previewEmoji.style.display = "inline-block";
      }
      if (fn) fn.textContent = "";
      document.querySelectorAll("#modal-auth .avatar-opt-btn").forEach(btn => {
        btn.classList.toggle("active", btn.dataset.avatar === emoji);
      });
    }
  }

  handleCustomPhotoUpload(event, isEdit = false) {
    const file = event.target && event.target.files && event.target.files[0];
    if (!file) return;

    if (!file.type.startsWith("image/")) {
      alert(this.lang === "hi" ? "Kripya valid image file chunein (JPG, PNG, GIF)!" : "Please choose a valid image file (JPG, PNG, GIF)!");
      return;
    }

    if (file.size > 2.5 * 1024 * 1024) {
      alert(this.lang === "hi" ? "Photo size 2.5MB se choti honi chahiye!" : "Photo must be smaller than 2.5MB!");
      return;
    }

    const reader = new FileReader();
    reader.onload = (e) => {
      const dataUrl = e.target.result;
      if (isEdit) {
        this.selectedEditAvatar = dataUrl;
        const previewImg = document.getElementById("edit-avatar-preview-img");
        const previewEmoji = document.getElementById("edit-avatar-preview-emoji");
        const fn = document.getElementById("edit-photo-filename");
        if (previewImg) {
          previewImg.src = dataUrl;
          previewImg.style.display = "block";
        }
        if (previewEmoji) previewEmoji.style.display = "none";
        if (fn) fn.textContent = file.name;
        document.querySelectorAll("#modal-edit-profile .avatar-opt-btn").forEach(btn => {
          btn.classList.remove("active");
        });
      } else {
        this.selectedAvatar = dataUrl;
        const previewImg = document.getElementById("auth-avatar-preview-img");
        const previewEmoji = document.getElementById("auth-avatar-preview-emoji");
        const fn = document.getElementById("auth-photo-filename");
        if (previewImg) {
          previewImg.src = dataUrl;
          previewImg.style.display = "block";
        }
        if (previewEmoji) previewEmoji.style.display = "none";
        if (fn) fn.textContent = file.name;
        document.querySelectorAll("#modal-auth .avatar-opt-btn").forEach(btn => {
          btn.classList.remove("active");
        });
      }
    };
    reader.readAsDataURL(file);
  }

  async handleSignupSubmit() {
    const nameInput = document.getElementById("auth-signup-name");
    const identInput = document.getElementById("auth-signup-identifier");
    const passInput = document.getElementById("auth-signup-password");

    const name = nameInput ? nameInput.value.trim() : "";
    const identifier = identInput ? identInput.value.trim() : "";
    const password = passInput ? passInput.value.trim() : "";

    if (!name) {
      this.showAuthFeedback(this.lang === "hi" ? "Kripya apna poora naam enter karein!" : "Please enter your full name!", true);
      return;
    }
    if (!identifier) {
      this.showAuthFeedback(this.lang === "hi" ? "Kripya username ya email enter karein!" : "Please enter a username or email!", true);
      return;
    }
    if (password.length < 8) {
      this.showAuthFeedback(this.lang === "hi" ? "Password kam se kam 8 characters ka hona chahiye!" : "Password must be at least 8 characters!", true);
      return;
    }

    const hpVal = document.getElementById("auth-signup-hp") ? document.getElementById("auth-signup-hp").value : "";
    const payload = {
      name,
      username: identifier,
      email: identifier.includes("@") ? identifier : `${identifier}@elysia.local`,
      password,
      hp: hpVal,
      avatar: this.selectedAvatar || "🐍",
      xp: this.xp,
      streak: this.streak,
      today_seconds: this.todaySeconds,
      completed_subtopics: Array.from(this.completedSubtopics)
    };

    try {
      const response = await fetch("/api/auth/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });
      const data = await response.json();

      if (response.ok && data.success) {
        this.currentUser = data.user;
        localStorage.setItem("elysia_current_user", JSON.stringify(this.currentUser));
        this.showAuthFeedback(this.lang === "hi" ? `🎉 Swagat hai, ${this.currentUser.name}! Account ban gaya!` : `🎉 Welcome, ${this.currentUser.name}! Account created!`, false);
        window.elysiaAudio.playVictory();
        this.launchConfetti();
        this.updateAuthUI();
        this.updateProfileModalUI();
        setTimeout(() => {
          this.closeModal("modal-auth");
          if (passInput) passInput.value = "";
        }, 1200);
      } else {
        this.showAuthFeedback(data.error || (this.lang === "hi" ? "Registration fail ho gaya!" : "Registration failed!"), true);
        window.elysiaAudio.playError();
      }
    } catch (err) {
      const localUser = {
        name,
        username: identifier,
        email: payload.email,
        avatar: this.selectedAvatar || "🐍",
        motto: "Code doesn't lie, syntax errors do.",
        xp: this.xp,
        streak: this.streak,
        today_seconds: this.todaySeconds,
        completed_subtopics: Array.from(this.completedSubtopics)
      };
      this.currentUser = localUser;
      localStorage.setItem("elysia_current_user", JSON.stringify(localUser));
      this.showAuthFeedback(this.lang === "hi" ? `🎉 Swagat hai, ${name}! Profile locally save ho gaya!` : `🎉 Welcome, ${name}! Profile saved locally!`, false);
      window.elysiaAudio.playVictory();
      this.launchConfetti();
      this.updateAuthUI();
      this.updateProfileModalUI();
      setTimeout(() => {
        this.closeModal("modal-auth");
        if (passInput) passInput.value = "";
      }, 1200);
    }
  }

  async handleLoginSubmit() {
    const identInput = document.getElementById("auth-login-identifier");
    const passInput = document.getElementById("auth-login-password");

    const identifier = identInput ? identInput.value.trim() : "";
    const password = passInput ? passInput.value.trim() : "";

    if (!identifier) {
      this.showAuthFeedback(this.lang === "hi" ? "Kripya username ya email enter karein!" : "Please enter your username or email!", true);
      return;
    }
    if (!password) {
      this.showAuthFeedback(this.lang === "hi" ? "Kripya apna password enter karein!" : "Please enter your password!", true);
      return;
    }

    try {
      const response = await fetch("/api/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ identifier, password })
      });
      const data = await response.json();

      if (response.ok && data.success) {
        this.currentUser = data.user;
        localStorage.setItem("elysia_current_user", JSON.stringify(this.currentUser));

        if (typeof data.user.xp === "number") {
          this.xp = Math.max(this.xp, data.user.xp);
          localStorage.setItem("elysia_xp", this.xp.toString());
        }
        if (typeof data.user.streak === "number") {
          this.streak = Math.max(this.streak, data.user.streak);
          localStorage.setItem("elysia_streak", this.streak.toString());
        }
        if (Array.isArray(data.user.completed_subtopics)) {
          data.user.completed_subtopics.forEach(id => this.completedSubtopics.add(id));
          localStorage.setItem("elysia_completed_subtopics", JSON.stringify(Array.from(this.completedSubtopics)));
        }
        if (typeof data.user.today_seconds === "number" && data.user.today_seconds > 0) {
          this.todaySeconds = Math.max(this.todaySeconds, data.user.today_seconds);
          localStorage.setItem("elysia_today_sec", this.todaySeconds.toString());
        }

        this.showAuthFeedback(this.lang === "hi" ? `🔓 Login safal! Wapas swagat hai, ${this.currentUser.name}!` : `🔓 Login successful! Welcome back, ${this.currentUser.name}!`, false);
        window.elysiaAudio.playVictory();
        this.updateAuthUI();
        this.updateGamificationUI();
        this.renderPythonCurriculumNav();
        this.updateProfileModalUI();
        setTimeout(() => {
          this.closeModal("modal-auth");
          if (passInput) passInput.value = "";
        }, 1000);
      } else {
        this.showAuthFeedback(data.error || (this.lang === "hi" ? "Galat credentials ya user nahi mila!" : "Invalid credentials or user not found!"), true);
        window.elysiaAudio.playError();
      }
    } catch (err) {
      const saved = localStorage.getItem("elysia_current_user");
      if (saved) {
        const u = JSON.parse(saved);
        if (u.username === identifier || u.email === identifier) {
          this.currentUser = u;
          this.showAuthFeedback(this.lang === "hi" ? `🔓 Login safal (offline mode)!` : `🔓 Login successful (offline mode)!`, false);
          window.elysiaAudio.playVictory();
          this.updateAuthUI();
          this.updateGamificationUI();
          this.updateProfileModalUI();
          setTimeout(() => {
            this.closeModal("modal-auth");
            if (passInput) passInput.value = "";
          }, 1000);
          return;
        }
      }
      this.showAuthFeedback(this.lang === "hi" ? "Login fail! Password ya username check karein." : "Login failed! Please check credentials.", true);
      window.elysiaAudio.playError();
    }
  }

  logoutUser() {
    window.elysiaAudio.playClick();
    fetch("/api/auth/logout", { method: "POST", headers: { "Content-Type": "application/json" }, body: "{}" })
      .catch(() => {});
    this.currentUser = null;
    localStorage.removeItem("elysia_current_user");
    this.closeModal("modal-user-profile");
    this.updateAuthUI();
  }

  openEditProfile() {
    this.closeModal("modal-user-profile");
    if (!this.currentUser) {
      this.openAuthModal();
      return;
    }

    const nameInput = document.getElementById("edit-profile-name");
    const mottoInput = document.getElementById("edit-profile-motto");
    if (nameInput) nameInput.value = this.currentUser.name || "";
    if (mottoInput) mottoInput.value = this.currentUser.motto || "";

    this.selectedEditAvatar = this.currentUser.avatar || "🐍";
    const previewImg = document.getElementById("edit-avatar-preview-img");
    const previewEmoji = document.getElementById("edit-avatar-preview-emoji");

    if (this.selectedEditAvatar.startsWith("data:image")) {
      if (previewImg) {
        previewImg.src = this.selectedEditAvatar;
        previewImg.style.display = "block";
      }
      if (previewEmoji) previewEmoji.style.display = "none";
    } else {
      if (previewImg) previewImg.style.display = "none";
      if (previewEmoji) {
        previewEmoji.textContent = this.selectedEditAvatar;
        previewEmoji.style.display = "inline-block";
      }
    }

    document.querySelectorAll("#modal-edit-profile .avatar-opt-btn").forEach(btn => {
      btn.classList.toggle("active", btn.dataset.avatar === this.selectedEditAvatar);
    });

    this.openModal("modal-edit-profile");
  }

  async saveProfileEdits() {
    if (!this.currentUser) return;
    const nameInput = document.getElementById("edit-profile-name");
    const mottoInput = document.getElementById("edit-profile-motto");

    const newName = nameInput ? nameInput.value.trim() : this.currentUser.name;
    const newMotto = mottoInput ? mottoInput.value.trim() : (this.currentUser.motto || "");

    if (newName) this.currentUser.name = newName;
    if (newMotto) this.currentUser.motto = newMotto;
    if (this.selectedEditAvatar) this.currentUser.avatar = this.selectedEditAvatar;

    // ⚡ OPTIMISTIC UI: Instant save, instant visual update, instant modal close
    localStorage.setItem("elysia_current_user", JSON.stringify(this.currentUser));
    this.updateAuthUI();
    this.updateProfileModalUI();
    this.closeModal("modal-edit-profile");
    window.elysiaAudio.playVictory();
    this.showOptimisticToast(this.lang === "hi" ? "⚡ Profile turant update ho gaya!" : "⚡ Profile updated instantly!", "success");

    // Background Network Sync
    fetch("/api/auth/update-profile", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name: this.currentUser.name,
        motto: this.currentUser.motto,
        avatar: this.currentUser.avatar
      })
    }).then(async upResp => {
      if (upResp.status === 401) {
        this.showOptimisticToast(this.lang === "hi" ? "Session expire ho gaya hai. Locally save ho gaya." : "Session expired. Saved locally.", "warning");
      }
    }).catch(e => {
      console.warn("Could not sync profile edits to server, saved locally:", e);
    });
  }

  async syncUserProgress() {
    if (!this.currentUser || !this.currentUser.username) return;
    try {
      const syncResp = await fetch("/api/auth/sync-progress", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          xp: this.xp,
          streak: this.streak,
          today_seconds: this.todaySeconds,
          total_seconds: this.totalSeconds,
          completed_subtopics: Array.from(this.completedSubtopics)
        })
      });
      if (syncResp.status === 401) {          // login session expired or missing
        this.currentUser = null;
        localStorage.removeItem("elysia_current_user");
        this.updateAuthUI();
      }
    } catch (e) {
      // Non-blocking sync
    }
  }

  getTotalSubtopicsCount() {
    let count = 0;
    for (const ch of (this.curriculumTree || [])) {
      count += (ch.subtopics || []).length;
    }
    return count || 15;
  }

  getCurrentGlobalSubtopicIndex() {
    let index = 1;
    for (let c = 0; c < this.currentChapterIdx; c++) {
      index += (this.curriculumTree[c]?.subtopics || []).length;
    }
    return index + this.currentSubtopicIdx;
  }

  /**
   * 📌 CONFETTI ENGINE: Physics particle explosion
   */
  _initConfetti() {
    this.confettiCanvas = document.getElementById("confetti-canvas");
    if (!this.confettiCanvas) return;
    this.confettiCtx = this.confettiCanvas.getContext("2d");
    this.confettiParticles = [];
    this.confettiRunning = false;

    const resize = () => {
      this.confettiCanvas.width = window.innerWidth;
      this.confettiCanvas.height = window.innerHeight;
    };
    window.addEventListener("resize", resize);
    resize();
  }

  launchConfetti() {
    if (!this.confettiCanvas || !this.confettiCtx) return;
    this.confettiCanvas.width = window.innerWidth;
    this.confettiCanvas.height = window.innerHeight;

    const colors = ["#38bdf8", "#a855f7", "#10b981", "#fbbf24", "#f43f5e", "#ffffff"];
    this.confettiParticles = [];
    for (let i = 0; i < 90; i++) {
      this.confettiParticles.push({
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

    if (!this.confettiRunning) {
      this.confettiRunning = true;
      this._animateConfetti();
    }
  }

  _animateConfetti() {
    if (!this.confettiRunning || this.confettiParticles.length === 0) {
      this.confettiRunning = false;
      if (this.confettiCtx && this.confettiCanvas) {
        this.confettiCtx.clearRect(0, 0, this.confettiCanvas.width, this.confettiCanvas.height);
      }
      return;
    }

    this.confettiCtx.clearRect(0, 0, this.confettiCanvas.width, this.confettiCanvas.height);

    for (let i = this.confettiParticles.length - 1; i >= 0; i--) {
      const p = this.confettiParticles[i];
      p.x += p.vx;
      p.y += p.vy;
      p.vy += 0.45;
      p.rotation += p.vr;
      p.alpha -= 0.012;

      if (p.alpha <= 0 || p.y > window.innerHeight) {
        this.confettiParticles.splice(i, 1);
        continue;
      }

      this.confettiCtx.save();
      this.confettiCtx.globalAlpha = Math.max(0, p.alpha);
      this.confettiCtx.translate(p.x, p.y);
      this.confettiCtx.rotate((p.rotation * Math.PI) / 180);
      this.confettiCtx.fillStyle = p.color;
      this.confettiCtx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size * 1.4);
      this.confettiCtx.restore();
    }

    requestAnimationFrame(() => this._animateConfetti());
  }
}

/**
 * 📌 DOM CONTENT LOADED: Browser jab HTML parse kar chuka hota hai, tab ElysiaApp instance banata hai
 */
window.addEventListener("DOMContentLoaded", () => {
  window.elysiaApp = new ElysiaApp();
  window.elysiaApp.init();
});
