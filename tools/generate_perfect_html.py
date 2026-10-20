import re

with open('web/index.html.bak', 'r') as f:
    orig_html = f.read()

# Find the start of tab-handbook
tab_handbook_pos = orig_html.find('<section id="tab-handbook"')
tail_content = orig_html[tab_handbook_pos:]

# Split out the tabs part and modals part
closing_app_wrapper_pos = tail_content.find('</div>\n\n  <!--\n    ===========================================================================\n    MODAL 1:')
if closing_app_wrapper_pos != -1:
    tabs_part = tail_content[:closing_app_wrapper_pos]
    modals_part = tail_content[closing_app_wrapper_pos + 7:]
else:
    split_target = '<div id="modal-lab-exporter"'
    idx = tail_content.find(split_target)
    div_idx = tail_content.rfind('</div>', 0, idx)
    tabs_part = tail_content[:div_idx]
    modals_part = tail_content[idx:]

new_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Elysia Code — Learn • Build • Evolve</title>
  
  <!-- Google Fonts: Elegant Display Serif for Hero Headline, Modern Sans for UI, JetBrains Mono for Code -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,600;0,700;0,800;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  
  <!-- Main Cinematic Design System -->
  <link rel="stylesheet" href="css/style.css">
  <!-- Visual Handbook / E-Book Styles -->
  <link rel="stylesheet" href="css/handbook.css">
  
  <!-- CodeMirror Syntax Highlighting (Dark IDE Theme) -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/theme/dracula.min.css">
</head>
<body>

  <!-- Ambient Background Lighting -->
  <div class="aurora-container">
    <div class="aurora-orb orb-1"></div>
    <div class="aurora-orb orb-2"></div>
    <div class="aurora-orb orb-3"></div>
  </div>

  <!-- Master App Shell -->
  <div class="app-layout">
    
    <!-- =========================================================================
         LEFT NAVIGATION SIDEBAR (Compact Dark Sidebar matching Reference)
         ========================================================================= -->
    <aside class="app-sidebar" id="app-sidebar">
      <div class="sidebar-header">
        <a href="#" class="sidebar-brand">
          <div class="brand-crystal-logo">
            <svg width="26" height="26" viewBox="0 0 28 28" fill="none">
              <path d="M14 2L24 8V20L14 26L4 20V8L14 2Z" stroke="url(#elysia-logo-grad)" stroke-width="2" fill="rgba(99,102,241,0.15)"/>
              <path d="M14 7L19 10.5V17.5L14 21L9 17.5V10.5L14 7Z" fill="url(#elysia-logo-grad)"/>
              <defs>
                <linearGradient id="elysia-logo-grad" x1="4" y1="2" x2="24" y2="26" gradientUnits="userSpaceOnUse">
                  <stop stop-color="#38bdf8"/>
                  <stop offset="0.5" stop-color="#818cf8"/>
                  <stop offset="1" stop-color="#c084fc"/>
                </linearGradient>
              </defs>
            </svg>
          </div>
          <div class="brand-text-block">
            <span class="brand-title-text">ELYSIA CODE</span>
            <span class="brand-sub-text">Learn • Build • Evolve</span>
          </div>
        </a>
      </div>

      <!-- Navigation Destinations -->
      <nav class="sidebar-nav">
        <button class="side-nav-btn active" data-dest="dashboard">
          <span class="side-nav-icon">⊞</span>
          <span class="side-nav-label">Dashboard</span>
        </button>
        <button class="side-nav-btn" data-dest="course">
          <span class="side-nav-icon">📖</span>
          <span class="side-nav-label">Python Course</span>
        </button>
        <button class="side-nav-btn" data-dest="lab">
          <span class="side-nav-icon">💻</span>
          <span class="side-nav-label">Coding Lab</span>
          <span class="side-nav-chevron">›</span>
        </button>
        <button class="side-nav-btn" data-dest="projects">
          <span class="side-nav-icon">📦</span>
          <span class="side-nav-label">Projects</span>
        </button>
        <button class="side-nav-btn" data-dest="mock">
          <span class="side-nav-icon">📋</span>
          <span class="side-nav-label">Mock Exams</span>
        </button>
        <button class="side-nav-btn" data-dest="handbook">
          <span class="side-nav-icon">📑</span>
          <span class="side-nav-label">Handbook</span>
        </button>
        <button class="side-nav-btn" data-dest="xray">
          <span class="side-nav-icon">🛡️</span>
          <span class="side-nav-label">Error Decoder</span>
        </button>
        <button class="side-nav-btn" data-dest="viva">
          <span class="side-nav-icon">🎙️</span>
          <span class="side-nav-label">Viva Questions</span>
        </button>
        <button class="side-nav-btn" data-dest="records">
          <span class="side-nav-icon">📝</span>
          <span class="side-nav-label">Notes & Records</span>
        </button>
        <button class="side-nav-btn" data-dest="community">
          <span class="side-nav-icon">🌐</span>
          <span class="side-nav-label">Community</span>
        </button>
      </nav>

      <!-- Bottom User Profile Chip in Sidebar -->
      <div class="sidebar-footer">
        <div class="side-user-chip" id="side-user-profile-chip" title="Click to view profile">
          <div class="side-avatar-circle" id="side-avatar-box">
            <img id="side-avatar-img" class="side-avatar-img" style="display:none;" />
            <span id="side-avatar-emoji" class="side-avatar-emoji">🐍</span>
          </div>
          <div class="side-user-meta">
            <span class="side-user-name" id="side-user-name">Priyanshu</span>
            <span class="side-user-role" id="side-user-role">Student</span>
          </div>
          <button class="side-settings-btn" id="btn-side-settings" title="Profile Settings">⚙️</button>
        </div>
      </div>
    </aside>

    <!-- =========================================================================
         MAIN CONTENT VIEWPORT (Right Scrollable Area)
         ========================================================================= -->
    <main class="app-main-viewport" id="app-main-viewport">

      <!-- TOP BAR OVER HERO / HEADER -->
      <header class="viewport-top-header">
        <div class="viewport-top-left">
          <button class="hero-back-tag" id="btn-hero-back" title="Course Track">
            <span>←</span>
            <span>PYTHON: ZERO TO PEAK</span>
          </button>
          
          <!-- Bilingual Engine Toggle -->
          <div class="pill-group top-lang-pill-group">
            <button class="pill-btn lang-btn active" data-lang="hi">🇮🇳 Hinglish</button>
            <button class="pill-btn lang-btn" data-lang="en">🇬🇧 English</button>
          </div>

          <!-- Track Switcher -->
          <div class="pill-group top-track-pill-group">
            <button class="pill-btn track-btn active" data-track="python">🐍 Python 3</button>
            <button class="pill-btn track-btn" data-track="html">🌐 HTML5</button>
          </div>

          <!-- Tactile Sound Effect (SFX) -->
          <button id="audio-toggle-btn" class="icon-btn-3d" title="Toggle Tactile Audio Sound">🔊</button>
        </div>

        <div class="viewport-top-right">
          <!-- Search Bar with cmd+K shortcut -->
          <div class="hero-search-box">
            <span class="search-lens-icon">🔍</span>
            <input type="text" id="hero-global-search" placeholder="Search lessons, topics or projects..." />
            <kbd class="kbd-shortcut">⌘ K</kbd>
          </div>

          <!-- Quick Theme Toggle Button -->
          <button class="hero-icon-round-btn" id="btn-quick-theme-toggle" title="Switch Theme">☀️</button>
          
          <!-- Hidden theme select for legacy state syncing -->
          <select id="theme-select" style="display:none;">
            <option value="midnight" selected>🌌 Midnight</option>
            <option value="dracula">🧛 Dracula</option>
            <option value="emerald">🌲 Emerald</option>
            <option value="sunset">🌅 Sunset</option>
            <option value="royal">👑 Royal</option>
            <option value="light">☀️ Light</option>
          </select>

          <!-- Notification Bell -->
          <button class="hero-icon-round-btn" id="btn-notifications" title="Notifications">🔔</button>

          <!-- User Avatar Circle -->
          <button class="hero-avatar-round-btn" id="btn-hero-profile" title="My Profile">P</button>

          <!-- Hidden legacy navbar triggers kept for full JS event compatibility -->
          <div style="display:none;">
            <span id="nav-streak-count">1</span>
            <span id="nav-xp-count">0</span>
            <span id="nav-timer-display">00:00:00</span>
            <button id="btn-open-auth"></button>
            <button id="btn-open-profile"></button>
            <img id="nav-user-avatar-img" />
            <span id="nav-user-avatar-emoji"></span>
            <span id="nav-user-display-name"></span>
            <span id="nav-profile-rank"></span>
            <button id="btn-open-exporter"></button>
            <button id="btn-open-flex"></button>
          </div>
        </div>
      </header>

      <!-- =======================================================================
           TAB 1: MAIN DASHBOARD & COURSE WORKSPACE
           ======================================================================= -->
      <section id="tab-learn" class="tab-content active">

        <!-- 1. CINEMATIC HERO SECTION (Pixel-Close to Reference Artwork) -->
        <div class="hero-banner-container">
          <div class="hero-main-content-wrap">
            <div class="hero-text-col">
              <h1 class="hero-display-headline">
                Turn Curiosity<br>
                <span class="headline-accent">Into Creation.</span>
              </h1>
              <p class="hero-support-desc">
                A complete Python learning journey from absolute basics to real-world mastery — structured, interactive and built for you.
              </p>
              <div class="hero-buttons-row">
                <button class="hero-btn-continue" id="btn-hero-continue">Continue Learning →</button>
                <button class="hero-btn-curriculum" id="btn-hero-curriculum">View Curriculum</button>
              </div>
            </div>

            <!-- Environmental Atmospheric Quote near Character -->
            <div class="hero-character-quote-tag">
              Discipline today,<br>freedom tomorrow.
            </div>
          </div>

          <!-- Floating Upper-Right Card: Keep Going Panel -->
          <div class="keep-going-panel">
            <div class="keep-going-top-row">
              <span class="keep-going-heading">Keep Going</span>
              <span class="streak-badge-flame">🔥 <span id="keep-streak-num">3</span> day streak</span>
            </div>
            <div class="week-calendar-strip" id="hero-week-calendar">
              <div class="cal-day-col"><span class="cal-d-name">Mon</span><span class="cal-d-num">15</span></div>
              <div class="cal-day-col"><span class="cal-d-name">Tue</span><span class="cal-d-num">16</span></div>
              <div class="cal-day-col"><span class="cal-d-name">Wed</span><span class="cal-d-num">17</span></div>
              <div class="cal-day-col"><span class="cal-d-name">Thu</span><span class="cal-d-num">18</span></div>
              <div class="cal-day-col active"><span class="cal-d-name">Fri</span><span class="cal-d-num">19</span></div>
              <div class="cal-day-col"><span class="cal-d-name">Sat</span><span class="cal-d-num">20</span></div>
              <div class="cal-day-col"><span class="cal-d-name">Sun</span><span class="cal-d-num">21</span></div>
            </div>
            <div class="keep-going-quote-box">
              <span class="kg-quote-mark">“</span>
              <p class="kg-quote-text">Code is not just a skill.<br>It's a way of thinking.</p>
              <span class="kg-author">— Elysia</span>
            </div>
          </div>
        </div>

        <!-- 2. PROGRESS & QUICK ACTIONS ROW (4 Cards below Hero) -->
        <div class="dashboard-stats-grid">
          <!-- Card 1: Your Progress -->
          <div class="stat-card-ref stat-card-progress">
            <div class="stat-card-title">Your Progress</div>
            <div class="progress-card-body">
              <div class="progress-circle-wrap">
                <svg class="stat-ring-svg" width="76" height="76" viewBox="0 0 76 76">
                  <defs>
                    <linearGradient id="stat-ring-grad" x1="0%" y1="0%" x2="100%" y2="100%">
                      <stop offset="0%" stop-color="#38bdf8"/>
                      <stop offset="100%" stop-color="#a855f7"/>
                    </linearGradient>
                  </defs>
                  <circle class="stat-ring-bg" cx="38" cy="38" r="30"/>
                  <circle class="stat-ring-bar" id="dash-ring-bar" cx="38" cy="38" r="30"/>
                </svg>
                <span class="stat-ring-text" id="dash-progress-percent">12%</span>
              </div>
              <div class="progress-breakdown-list">
                <div class="breakdown-item">
                  <span><span class="dot dot-blue"></span>7 Parts</span>
                  <span class="item-val" id="stat-parts-val">1/7</span>
                </div>
                <div class="breakdown-item">
                  <span><span class="dot dot-cyan"></span>26 Chapters</span>
                  <span class="item-val" id="stat-chapters-val">3/26</span>
                </div>
                <div class="breakdown-item">
                  <span><span class="dot dot-purple"></span>100+ Exercises</span>
                  <span class="item-val" id="stat-exercises-val">12/86</span>
                </div>
                <div class="breakdown-item">
                  <span><span class="dot dot-emerald"></span>5 Projects</span>
                  <span class="item-val" id="stat-projects-val">0/5</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Card 2: Current Chapter -->
          <div class="stat-card-ref stat-card-chapter">
            <div class="stat-card-header-row">
              <span class="stat-card-title">Current Chapter</span>
              <span class="badge-part" id="dash-part-badge">Part 1</span>
            </div>
            <div class="current-chapter-body">
              <div class="chapter-icon-box">🐍</div>
              <div class="chapter-info">
                <div class="chapter-name" id="dash-chapter-title">Chapter 1: Welcome to the World of Python</div>
                <div class="chapter-progress-bar-wrap">
                  <div class="chapter-progress-fill" id="dash-chapter-fill" style="width: 42%;"></div>
                </div>
                <div class="chapter-topics-count" id="dash-topics-count">3 / 7 topics</div>
              </div>
            </div>
          </div>

          <!-- Card 3: Next Topic -->
          <div class="stat-card-ref stat-card-next">
            <div class="stat-card-title">Next Topic</div>
            <div class="next-topic-body" id="dash-next-topic-btn">
              <div class="play-icon-box">▶</div>
              <div class="next-info">
                <div class="next-title" id="dash-next-title">How computers understand code<br>(The Translator Analogy)</div>
                <div class="next-meta">
                  <span id="dash-next-time">~ 8 min</span>
                  <span class="arrow-sym">→</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Card 4: Quick Actions -->
          <div class="stat-card-ref stat-card-actions">
            <div class="stat-card-title">Quick Actions</div>
            <div class="quick-actions-row">
              <button class="qa-btn" id="qa-btn-practice" title="Open Code Editor">
                <span class="qa-icon">&lt;/&gt;</span>
                <span class="qa-label">Practice Code</span>
              </button>
              <button class="qa-btn" id="qa-btn-quiz" title="Take Concept Quiz">
                <span class="qa-icon">📄</span>
                <span class="qa-label">Take Quiz</span>
              </button>
              <button class="qa-btn" id="qa-btn-project" title="Build Project">
                <span class="qa-icon">📦</span>
                <span class="qa-label">Build Project</span>
              </button>
              <button class="qa-btn" id="qa-btn-handbook" title="Explore Visual Handbook">
                <span class="qa-icon">📖</span>
                <span class="qa-label">Explore Handbook</span>
              </button>
            </div>
          </div>
        </div>

        <!-- 3. INTEGRATED TEXTBOOK WORKSPACE (3-COLUMN REGION) -->
        <div class="integrated-workspace-grid" id="integrated-course-workspace">
          
          <!-- REGION 1: LEFT - Course Chapters Navigation Tree -->
          <div class="workspace-panel tree-panel">
            <div class="tree-panel-header">
              <span class="tree-title">Python Course</span>
              <button class="tree-toggle-btn" title="Toggle view">⊞</button>
            </div>
            <div class="tree-search-bar">
              <span class="search-icon">🔍</span>
              <input type="text" id="course-tree-search" placeholder="Search chapters..." />
              <span class="filter-icon">⚙</span>
            </div>
            
            <!-- Dynamic Tree Accordion -->
            <div class="course-tree-content" id="course-tree-accordion">
              <!-- Rendered dynamically by app.js using window.PYTHON_CURRICULUM_PARTS -->
            </div>

            <!-- Legacy selectors kept hidden for complete JS compatibility -->
            <div style="display:none;">
              <div id="chapter-selector-strip"></div>
              <div id="subtopic-selector-strip"></div>
            </div>
          </div>

          <!-- REGION 2: CENTER - Lesson Reader & Interactive Content -->
          <div class="workspace-panel lesson-panel">
            <!-- Breadcrumbs -->
            <div class="lesson-breadcrumb-row">
              <span class="bc-item">🌐</span>
              <span class="bc-item" id="lesson-bc-part">Part 1</span>
              <span class="bc-sep">&gt;</span>
              <span class="bc-item" id="lesson-bc-ch">Chapter 1</span>
              <span class="bc-sep">&gt;</span>
              <span class="bc-item active" id="lesson-bc-sub">What is Python and why is it so popular?</span>
            </div>

            <!-- Lesson Main Header -->
            <div class="lesson-title-meta-wrap">
              <h2 class="lesson-h2" id="lesson-title">What is Python and why is it so popular?</h2>
              <div class="lesson-meta-badges">
                <span class="meta-badge-time" id="lesson-duration-tag">⏱️ Reading Time ~ 5 min</span>
                <span id="lesson-xp-badge" style="display:none;">⚡ +50 XP</span>
                <span id="lesson-chapter-tag" style="display:none;">PART 1</span>
                <div class="circle-fraction-badge" id="lesson-circle-fraction">1/7</div>
              </div>
            </div>
            
            <p class="lesson-summary-p" id="lesson-active-summary">
              Python is a high-level, easy-to-read programming language used for web development, data science, automation, artificial intelligence and much more. It is popular because it is simple, powerful and beginner-friendly.
            </p>

            <!-- Lesson Tabs -->
            <div class="lesson-pill-tabs">
              <button class="l-tab active" data-subtab="explanation">Explanation</button>
              <button class="l-tab" data-subtab="examples">Examples</button>
              <button class="l-tab" data-subtab="hinglish">Hinglish</button>
              <button class="l-tab" data-subtab="practice">Practice</button>
              <button class="l-tab" data-subtab="quiz">Quiz</button>
              <button class="l-tab" data-subtab="notes">Notes</button>
            </div>

            <div class="lesson-content-layout">
              <!-- Main Content Column -->
              <div class="lesson-main-col">
                <!-- Sub-block: Your First Python Program -->
                <div class="lesson-sub-block" id="block-first-program">
                  <h3 class="block-title" id="lesson-block-title">Your First Python Program</h3>
                  <p class="block-desc" id="lesson-block-desc">The simplest Python program is just one line:</p>

                  <div class="code-snippet-box">
                    <div class="code-snippet-header">
                      <span class="lang-tag">python</span>
                      <button class="copy-btn" id="btn-copy-snippet">📋 Copy</button>
                    </div>
                    <pre class="snippet-pre"><code id="lesson-snippet-code">print("Hello, World!")</code></pre>
                  </div>

                  <div class="output-preview-card">
                    <div class="output-preview-head">
                      <span>Output</span>
                      <button class="btn-run-snippet" id="btn-run-snippet-code">▶ Run Code</button>
                    </div>
                    <div class="output-preview-text" id="lesson-snippet-output">Hello, World!</div>
                  </div>

                  <div class="educational-tip-box" id="lesson-tip-box">
                    <span class="tip-icon">💡</span>
                    <span class="tip-text" id="lesson-tip-text">The print() function tells Python to display the text inside the parentheses.</span>
                  </div>
                </div>

                <!-- Concept Breakdown (Explanation Tab Content) -->
                <div class="theory-details-wrap" id="block-theory-details">
                  <div class="concept-card" style="margin-top:14px;">
                    <div class="box-label">📖 <span data-i18n-en="Concept Foundation" data-i18n-hi="Concept Foundation">Concept Foundation</span></div>
                    <p id="lesson-what" class="analogy-text">Loading...</p>
                  </div>

                  <div class="why-card" style="margin-top:12px;">
                    <div class="box-label" style="color: #38bdf8;">💡 <span>Why We Need It</span></div>
                    <p id="lesson-why" class="analogy-text">Loading...</p>
                  </div>

                  <div class="syntax-card" style="margin-top:12px;">
                    <div class="box-label" style="color: #c084fc;">⚙️ <span>Syntax & Blueprint</span></div>
                    <pre class="syntax-pre"><code id="lesson-syntax"></code></pre>
                    <p id="lesson-how" class="analogy-text" style="margin-top: 8px; font-size: 0.86rem;"></p>
                  </div>

                  <div class="rules-card" style="margin-top:12px;">
                    <div class="box-label" style="color: #fbbf24;">📜 <span>Golden Rules</span></div>
                    <ul id="lesson-rules-list" class="rules-bullet-list"></ul>
                  </div>

                  <!-- Example 1 & 2 Cards -->
                  <div class="example-card" id="lesson-example-1-card" style="margin-top:12px;">
                    <div class="example-header">
                      <span class="example-label">🧪 Example 1: <strong id="example-1-title">Basic Syntax</strong></span>
                      <button id="btn-try-example-1" class="btn-micro" title="Copy code into editor">⚡ Try in IDE</button>
                    </div>
                    <pre class="example-code-pre"><code id="example-1-code">print("Hello, World!")</code></pre>
                    <div class="example-expl" id="example-1-expl">Line by line breakdown...</div>
                  </div>

                  <div class="example-card" id="lesson-example-2-card" style="margin-top:12px;">
                    <div class="example-header">
                      <span class="example-label">💼 Example 2: <strong id="example-2-title">Real World Project</strong></span>
                      <button id="btn-try-example-2" class="btn-micro" title="Copy code into editor">⚡ Try in IDE</button>
                    </div>
                    <pre class="example-code-pre"><code id="example-2-code"># Example code</code></pre>
                    <div class="example-expl" id="example-2-expl">Real world application details...</div>
                  </div>

                  <div class="analogy-box" style="margin-top:12px;">
                    <div class="box-label">🧠 <span>Mental Model & Relatable Analogy</span></div>
                    <p id="lesson-analogy" class="analogy-text">Loading...</p>
                  </div>
                </div>

                <!-- Subtopic Challenge Card (Practice Tab Content) -->
                <div class="challenge-card" id="lesson-challenge-card" style="margin-top:16px;">
                  <div class="challenge-header">
                    <span class="challenge-badge">🎯 SUBTOPIC CHALLENGE</span>
                    <span class="challenge-reward" id="challenge-reward-badge">Earn +50 XP</span>
                  </div>
                  <p id="challenge-prompt" class="challenge-prompt-text">Challenge task will appear here.</p>
                  <div class="challenge-expected-box">
                    <span class="expected-label">Expected Terminal Output:</span>
                    <code id="challenge-expected-output">I am a future Python Pro</code>
                  </div>
                  <div class="challenge-actions-row">
                    <button id="btn-load-starter-code" class="btn-micro">📝 Load Starter Code</button>
                    <button id="btn-toggle-solution" class="btn-micro btn-ghost">👁️ Reveal Solution</button>
                  </div>
                  <div id="challenge-solution-box" class="solution-box hidden">
                    <div class="solution-header">
                      <span>💡 Official Solution Code:</span>
                      <button id="btn-copy-solution" class="btn-micro" style="font-size:0.7rem;">Copy to IDE</button>
                    </div>
                    <pre class="solution-code-pre"><code id="solution-code-display"></code></pre>
                    <p id="solution-explanation-text" class="solution-expl-text"></p>
                  </div>
                </div>

                <!-- Navigation Controls -->
                <div class="subtopic-nav-footer" style="margin-top: 18px;">
                  <button id="btn-prev-subtopic" class="pill-btn">⏮️ Previous</button>
                  <span id="subtopic-counter-indicator" style="font-size:0.85rem; color:#94a3b8; font-weight:600;">1 of 7 Subtopics</span>
                  <button id="btn-next-subtopic" class="btn-primary-3d">Next Topic ⏭️</button>
                </div>
              </div>

              <!-- Right Sub-rail inside Center Panel (as seen in the reference) -->
              <div class="lesson-subrail-col">
                <div class="subrail-section">
                  <div class="subrail-heading">On This Page</div>
                  <div class="subrail-links-list" id="subrail-on-this-page">
                    <a href="#intro" class="subrail-link active">Introduction</a>
                    <a href="#example" class="subrail-link">A Simple Example</a>
                    <a href="#why" class="subrail-link">Why is it so popular?</a>
                    <a href="#uses" class="subrail-link">Real-world uses</a>
                    <a href="#takeaways" class="subrail-link">Key takeaways</a>
                  </div>
                </div>

                <div class="subrail-section">
                  <div class="subrail-heading">Quick Notes</div>
                  <ul class="subrail-bullets-list" id="subrail-quick-notes">
                    <li>Python is easy to read</li>
                    <li>Used in many industries</li>
                    <li>Beginner-friendly</li>
                    <li>Large community support</li>
                  </ul>
                </div>

                <div class="subrail-section">
                  <div class="subrail-heading">Related Topics</div>
                  <div class="subrail-related-list" id="subrail-related-topics">
                    <a href="#" class="related-link">📄 Downloading Python</a>
                    <a href="#" class="related-link">📄 Your first program</a>
                    <a href="#" class="related-link">📄 Using the terminal</a>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- REGION 3: RIGHT - Code Editor & Interactive Playground -->
          <div class="workspace-panel editor-panel">
            <div class="editor-panel-tabs">
              <div class="editor-tabs-group">
                <button class="e-tab active" data-ed-tab="code">Code</button>
                <button class="e-tab" data-ed-tab="tests">Test Cases</button>
                <button class="e-tab" data-ed-tab="ai">AI Help</button>
              </div>
              <button class="e-expand-btn" id="btn-fullscreen-editor" title="Expand Fullscreen">⛶</button>
            </div>

            <!-- Python Runtime Selector -->
            <div class="editor-engine-bar">
              <div class="engine-pill">
                <span class="py-icon">🐍</span>
                <select id="select-exec-engine" class="engine-dropdown" title="Choose Execution Engine">
                  <option value="pyodide" selected>Python 3 (Pyodide)</option>
                  <option value="server">Python 3 (Server Engine)</option>
                </select>
              </div>
              <button class="btn-editor-reset" id="btn-reset-code" title="Reset starter code">↺ Reset</button>
            </div>

            <!-- CodeMirror Editor Textarea -->
            <div class="monaco-like-editor-wrapper">
              <textarea id="code-editor-textarea" class="code-textarea" spellcheck="false"></textarea>
              <iframe id="html-preview-frame" class="html-preview-frame" style="display:none;"></iframe>
            </div>

            <div style="display:none;">
              <span id="editor-lang-indicator">python_workspace.py</span>
              <span id="editor-cursor-pos">Ln 1, Col 1</span>
              <button id="btn-copy-code"></button>
              <button id="btn-download-code"></button>
              <button id="btn-ai-find-errors"></button>
              <button id="btn-ai-ask-tutor"></button>
              <button id="btn-submit-code"></button>
            </div>

            <!-- Big Electric Blue Run Button -->
            <button class="btn-run-prominent" id="btn-run-code" title="Shortcut: Ctrl+Enter or Cmd+Enter">
              <span>Run</span>
              <span class="run-play-triangle">▶</span>
              <span class="run-key-hint">Ctrl + Enter</span>
            </button>

            <!-- Output Terminal Box -->
            <div class="terminal-box-ref">
              <div class="term-tabs-row">
                <div class="term-left-tabs">
                  <button class="term-tab active" id="term-tab-output">Output</button>
                  <button class="term-tab" id="term-tab-errors">Errors</button>
                  <button class="term-tab" id="term-tab-input">Input</button>
                  <button class="term-tab" id="term-tab-repl">REPL</button>
                </div>
                <button class="term-clear-btn" id="btn-clear-terminal">🗑️ Clear</button>
              </div>
              <div class="term-console-body">
                <div id="terminal-stdout" class="stdout-text">
                  <span class="status-circle-green">🟢</span> Hello, Elysia!
                </div>
                <div id="terminal-stderr" class="stderr-text"></div>
                
                <!-- Interactive Stdin Input Bar -->
                <div id="terminal-input-bar" class="terminal-input-bar" style="display:none;">
                  <span class="terminal-prompt-sym">❯</span>
                  <input type="text" id="terminal-stdin-input" class="terminal-stdin-field" placeholder="Type here and press Enter..." />
                  <button id="btn-submit-stdin" class="btn-micro">Send ↵</button>
                </div>

                <!-- Original Interactive REPL Console -->
                <div id="terminal-repl-view" style="display:none;">
                  <div id="repl-history" class="repl-history">
                    <div class="repl-line system-line">Python 3.11 (Pyodide WASM) Console:</div>
                  </div>
                  <div class="repl-input-row">
                    <span class="repl-prompt">&gt;&gt;&gt;&nbsp;</span>
                    <input type="text" id="repl-input" class="repl-input-field" placeholder="Type command..." />
                    <button id="btn-repl-send" class="btn-micro">Run ↵</button>
                  </div>
                </div>
              </div>
            </div>

            <!-- 3D Live Variable Memory Visualizer (RAM boxes) -->
            <div id="memory-tracker-card" class="memory-tracker-card" style="margin-bottom:12px;">
              <div class="memory-header">
                <span>🧠 3D Variable Memory Tracker</span>
                <span style="font-size:0.7rem; color: var(--text-dim);">Live RAM</span>
              </div>
              <div id="memory-grid" class="memory-grid"></div>
            </div>

            <!-- Try It Yourself Challenge Box -->
            <div class="try-yourself-card">
              <div class="try-yourself-header">
                <div class="try-head-left">
                  <span class="lightbulb-sym">💡</span>
                  <span class="try-title">Try It Yourself</span>
                </div>
                <button class="try-hint-btn" id="btn-show-hint">Hint</button>
              </div>
              <p class="try-prompt-p" id="try-prompt-text">Modify the code to print your own name.</p>
              <div class="try-footer-row">
                <button class="try-sol-btn" id="btn-show-solution">
                  <span>👁️</span> Show Solution
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- 4. LOWER SHOWCASE PREVIEWS ROW (Matching bottom of Reference) -->
        <div class="bottom-showcase-row" id="bottom-showcase-row">
          
          <!-- Card 1: Projects Showcase -->
          <div class="showcase-card showcase-projects" style="background-image: linear-gradient(180deg, rgba(8,12,20,0.45) 0%, rgba(8,12,20,0.94) 100%), url('images/projects-bg.jpg');">
            <div class="sc-header">
              <div class="sc-title-block">
                <h3 class="sc-title">Projects</h3>
                <p class="sc-subtitle">Build real applications and apply what you learn</p>
              </div>
              <div class="sc-tabs">
                <button class="sc-tab active">All Projects</button>
                <button class="sc-tab">By Chapter</button>
                <button class="sc-tab">Completed</button>
              </div>
            </div>
            <div class="sc-items-grid">
              <div class="sc-item-box" onclick="window.elysiaApp.loadProject('ch2_sub5_mini_project_chatbot')">
                <div class="sc-item-thumb">💬</div>
                <div class="sc-item-info">
                  <div class="sc-item-title">Interactive Welcome Chatbot</div>
                  <div class="sc-item-meta">
                    <span>Part 1 • Chapter 2</span>
                    <span class="level-tag beginner">Beginner</span>
                  </div>
                  <p class="sc-item-desc">Build a simple chatbot using input() and print().</p>
                </div>
              </div>
              <div class="sc-item-box" onclick="window.elysiaApp.loadProject('ch6_sub7_mini_project_adventure_game')">
                <div class="sc-item-thumb">🎮</div>
                <div class="sc-item-info">
                  <div class="sc-item-title">Choose-Your-Own-Adventure Game</div>
                  <div class="sc-item-meta">
                    <span>Part 2 • Chapter 6</span>
                    <span class="level-tag beginner">Beginner</span>
                  </div>
                  <p class="sc-item-desc">A text-based story game using if, else and loops.</p>
                </div>
              </div>
              <div class="sc-item-box" onclick="window.elysiaApp.loadProject('ch7_sub9_mini_project_password_guesser')">
                <div class="sc-item-thumb">🔐</div>
                <div class="sc-item-info">
                  <div class="sc-item-title">Password Guesser Game</div>
                  <div class="sc-item-meta">
                    <span>Part 2 • Chapter 7</span>
                    <span class="level-tag intermediate">Intermediate</span>
                  </div>
                  <p class="sc-item-desc">Guess the password using while loops.</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Card 2: Mock Exams Showcase -->
          <div class="showcase-card showcase-exams" style="background-image: linear-gradient(180deg, rgba(8,12,20,0.45) 0%, rgba(8,12,20,0.94) 100%), url('images/exams-bg.jpg');">
            <div class="sc-header">
              <div class="sc-title-block">
                <h3 class="sc-title">Mock Exams</h3>
                <p class="sc-subtitle">Test your knowledge and track your progress</p>
              </div>
              <div class="sc-tabs">
                <button class="sc-tab active">Chapter Tests</button>
                <button class="sc-tab">Full Tests</button>
                <button class="sc-tab">Custom Test</button>
              </div>
            </div>
            <div class="sc-items-grid">
              <div class="sc-exam-card" onclick="window.elysiaApp.switchTab('mock')">
                <div class="exam-icon-circle blue-icon">📄</div>
                <div class="exam-card-title">Part 1 Test</div>
                <div class="exam-card-sub">Chapters 1–5</div>
                <div class="exam-card-meta">⏱️ 20 Questions</div>
                <button class="btn-start-exam">Start Test</button>
              </div>
              <div class="sc-exam-card" onclick="window.elysiaApp.switchTab('mock')">
                <div class="exam-icon-circle purple-icon">📄</div>
                <div class="exam-card-title">Part 2 Test</div>
                <div class="exam-card-sub">Chapters 6–7</div>
                <div class="exam-card-meta">⏱️ 15 Questions</div>
                <button class="btn-start-exam">Start Test</button>
              </div>
              <div class="sc-exam-card" onclick="window.elysiaApp.switchTab('mock')">
                <div class="exam-icon-circle green-icon">📄</div>
                <div class="exam-card-title">Part 3 Test</div>
                <div class="exam-card-sub">Chapters 8–11</div>
                <div class="exam-card-meta">⏱️ 20 Questions</div>
                <button class="btn-start-exam">Start Test</button>
              </div>
            </div>
          </div>

          <!-- Card 3: Mobile View (Responsive) Preview -->
          <div class="showcase-card showcase-device-preview mobile-preview-card">
            <div class="preview-badge-header">Mobile View (Responsive)</div>
            <div class="device-mockup-frame">
              <div class="mockup-header-bar">
                <span class="mockup-logo">⚡ ELYSIA CODE</span>
                <span class="mockup-menu-icon">☰</span>
              </div>
              <div class="mockup-body">
                <div class="mockup-greet">Good evening,<br><strong>Priyanshu 👑</strong></div>
                <button class="mockup-hero-btn" onclick="window.elysiaApp.focusEditor()">Continue Learning →</button>
                <div class="mockup-course-title">Python Course</div>
                <div class="mockup-part-row"><span>Part 1: The Absolute Basics</span> <span class="part-prog">1/5</span></div>
                <div class="mockup-ch-row"><span>Chapter 1: Welcome to the World of Python</span> <span class="ch-prog">3/7</span></div>
              </div>
            </div>
          </div>

          <!-- Card 4: Theme Switch (Adaptive) Preview -->
          <div class="showcase-card showcase-device-preview light-theme-preview-card">
            <div class="preview-badge-header">Theme Switch (Adaptive)</div>
            <div class="device-mockup-frame light-frame">
              <div class="mockup-header-bar light">
                <span class="mockup-logo">⚡ ELYSIA CODE</span>
                <span class="mockup-menu-icon">☀️</span>
              </div>
              <div class="mockup-body light">
                <div class="mockup-greet light">Good evening,<br><strong>Priyanshu 👑</strong></div>
                <button class="mockup-hero-btn light-btn" onclick="window.elysiaApp.toggleThemeQuick()">Switch to Light Theme →</button>
                <div class="mockup-course-title light">Python Course</div>
                <div class="mockup-part-row light"><span>Part 1: The Absolute Basics</span> <span class="part-prog light">1/5</span></div>
                <div class="mockup-ch-row light"><span>Chapter 1: Welcome to the World of Python</span> <span class="ch-prog light">3/7</span></div>
              </div>
            </div>
          </div>
        </div>

      </section>

      <!-- =======================================================================
           OTHER FEATURE TABS (Preserved with 100% full functionality)
           ======================================================================= -->
{tabs_part}

    </main>
  </div>

  <!-- =========================================================================
       MODALS, AI TUTOR & SCRIPTS (Preserved with 100% full functionality)
       ========================================================================= -->
{modals_part}
"""

with open('web/index.html', 'w') as f:
    f.write(new_html)

print("Generated web/index.html successfully, length:", len(new_html))
