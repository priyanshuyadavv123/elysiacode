with open('web/js/app.js.bak', 'r') as f:
    code = f.read()

# Let's inspect how init() ends
init_target = "this._initPyodideEngine(); // ⚡ Live Pyodide WebAssembly engine initialize & preload kiya\n  }"
assert init_target in code, "Could not find init target"

new_init_call = """this._initPyodideEngine(); // ⚡ Live Pyodide WebAssembly engine initialize & preload kiya
    this.setupReferenceUI(); // 🏛️ Reference UI Bindings & Tree Accordion
  }"""

code = code.replace(init_target, new_init_call)

# Let's add setupReferenceUI, renderReferenceTree, loadProject, toggleThemeQuick methods
# We will attach them right after switchTab or before the end of the class

reference_methods = """
  // =========================================================================
  // 🏛️ MASTER REFERENCE UI ORCHESTRATOR & INTERACTIONS
  // =========================================================================

  toggleThemeQuick() {
    const nextTheme = this.currentTheme === 'light' ? 'midnight' : 'light';
    this.setTheme(nextTheme, true);
    const quickBtn = document.getElementById("btn-quick-theme-toggle");
    if (quickBtn) quickBtn.textContent = nextTheme === 'light' ? '🌙' : '☀️';
  }

  setupReferenceUI() {
    // 1. Sidebar Nav Destination buttons
    document.querySelectorAll(".side-nav-btn").forEach(btn => {
      btn.addEventListener("click", (e) => {
        const dest = e.currentTarget.dataset.dest;
        window.elysiaAudio?.playClick();

        document.querySelectorAll(".side-nav-btn").forEach(b => b.classList.remove("active"));
        e.currentTarget.classList.add("active");

        const viewport = document.getElementById("app-main-viewport");

        if (dest === "dashboard") {
          this.switchTab("learn");
          viewport?.scrollTo({ top: 0, behavior: "smooth" });
        } else if (dest === "course") {
          this.switchTab("learn");
          document.getElementById("integrated-course-workspace")?.scrollIntoView({ behavior: "smooth" });
        } else if (dest === "lab") {
          this.switchTab("learn");
          this.focusEditor();
          document.getElementById("code-editor-textarea")?.scrollIntoView({ behavior: "smooth" });
        } else if (dest === "projects") {
          this.switchTab("learn");
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
        document.getElementById("integrated-course-workspace")?.scrollIntoView({ behavior: "smooth" });
        this.focusEditor();
      });
    }

    const btnCurriculum = document.getElementById("btn-hero-curriculum");
    if (btnCurriculum) {
      btnCurriculum.addEventListener("click", () => {
        window.elysiaAudio?.playClick();
        document.getElementById("integrated-course-workspace")?.scrollIntoView({ behavior: "smooth" });
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
      this.setCode(`# Interactive Welcome Chatbot Project\\nuser_name = input("Enter your name: ")\\nprint(f"Hello, {user_name}! Welcome to Elysia Code!")\\n`);
      this.focusEditor();
      document.getElementById("integrated-course-workspace")?.scrollIntoView({ behavior: "smooth" });
    }
  }
"""

# Let's insert reference_methods right after switchTab
switch_tab_end = "if (tabName === \"handbook\") this.loadHandbook();\n  }"
assert switch_tab_end in code, "Could not find switchTab end"
code = code.replace(switch_tab_end, switch_tab_end + "\n" + reference_methods)

# Now, let's update renderCurrentSubtopic() to sync the reference UI:
render_sub_target = "if (solBox) solBox.classList.add(\"hidden\");"
sync_reference_snippet = """if (solBox) solBox.classList.add("hidden");

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
    if (sub.example_1 && snippetCode) {
      snippetCode.textContent = sub.example_1.code || 'print("Hello, World!")';
    }
    if (snippetOut) {
      snippetOut.textContent = (sub.challenge && sub.challenge.expected_output) || 'Hello, World!';
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
"""

assert render_sub_target in code, "Could not find renderCurrentSubtopic target"
code = code.replace(render_sub_target, sync_reference_snippet)

# Also update updateAuthUI to sync sidebar user chip:
auth_ui_target = "if (rankEl) rankEl.textContent = tier.rank;"
auth_ui_sync = """if (rankEl) rankEl.textContent = tier.rank;

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
"""
assert auth_ui_target in code, "Could not find updateAuthUI target"
code = code.replace(auth_ui_target, auth_ui_sync)

with open('web/js/app.js', 'w') as f:
    f.write(code)

print("Updated web/js/app.js successfully!")
