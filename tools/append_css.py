css_content = """

/* =============================================================================
   🏛️ PIXEL-CLOSE ELYSIA CODE MASTER DESIGN SYSTEM & LAYOUT SPECIFICATION
   Directly matching reference image composition, hero, sidebar, and workspace.
   ============================================================================= */

/* 1. App Shell Container */
.app-layout {
  display: flex;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  background-color: #07090e;
  color: #f8fafc;
  font-family: var(--font-sans);
}

/* 2. Left Sidebar Navigation */
.app-sidebar {
  width: 220px;
  min-width: 220px;
  height: 100vh;
  background: #090d16;
  border-right: 1px solid rgba(255, 255, 255, 0.06);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  z-index: 50;
  user-select: none;
  flex-shrink: 0;
}

.sidebar-header {
  padding: 20px 16px 14px 16px;
}

.sidebar-brand {
  display: flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
}

.brand-crystal-logo {
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.brand-text-block {
  display: flex;
  flex-direction: column;
}

.brand-title-text {
  font-size: 0.98rem;
  font-weight: 800;
  letter-spacing: 0.8px;
  color: #ffffff;
}

.brand-sub-text {
  font-size: 0.62rem;
  color: #64748b;
  font-weight: 500;
  letter-spacing: 0.3px;
}

.sidebar-nav {
  padding: 6px 10px;
  display: flex;
  flex-direction: column;
  gap: 3px;
  overflow-y: auto;
  flex: 1;
}

.side-nav-btn {
  display: flex;
  align-items: center;
  gap: 10px;
  width: 100%;
  padding: 8.5px 12px;
  border-radius: 8px;
  border: none;
  background: transparent;
  color: #94a3b8;
  font-size: 0.82rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.16s ease;
  text-align: left;
}

.side-nav-btn:hover {
  background: rgba(255, 255, 255, 0.05);
  color: #ffffff;
}

.side-nav-btn.active {
  background: #182030;
  color: #ffffff;
  font-weight: 700;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.08);
}

.side-nav-btn.active .side-nav-icon {
  color: #38bdf8;
}

.side-nav-icon {
  font-size: 0.95rem;
  width: 18px;
  display: inline-flex;
  justify-content: center;
  flex-shrink: 0;
}

.side-nav-chevron {
  margin-left: auto;
  color: #64748b;
  font-size: 0.9rem;
}

.sidebar-footer {
  padding: 12px;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
}

.side-user-chip {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 6px 8px;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.03);
  cursor: pointer;
  transition: background 0.2s;
}

.side-user-chip:hover {
  background: rgba(255, 255, 255, 0.07);
}

.side-avatar-circle {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: #1e293b;
  border: 1.5px solid #38bdf8;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.95rem;
  overflow: hidden;
  flex-shrink: 0;
}

.side-avatar-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.side-user-meta {
  display: flex;
  flex-direction: column;
  overflow: hidden;
  flex: 1;
}

.side-user-name {
  font-size: 0.82rem;
  font-weight: 700;
  color: #ffffff;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.side-user-role {
  font-size: 0.65rem;
  color: #64748b;
}

.side-settings-btn {
  background: transparent;
  border: none;
  color: #64748b;
  cursor: pointer;
  font-size: 0.9rem;
  padding: 4px;
  transition: color 0.2s;
}

.side-settings-btn:hover {
  color: #ffffff;
}

/* 3. Main Viewport & Header */
.app-main-viewport {
  flex: 1;
  height: 100vh;
  overflow-y: auto;
  overflow-x: hidden;
  padding: 16px 24px 48px 24px;
  background: #07090e;
  display: flex;
  flex-direction: column;
  gap: 16px;
  scroll-behavior: smooth;
}

.viewport-top-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  width: 100%;
  margin-bottom: 2px;
}

.viewport-top-left {
  display: flex;
  align-items: center;
  gap: 12px;
}

.hero-back-tag {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: transparent;
  border: none;
  color: #94a3b8;
  font-size: 0.74rem;
  font-weight: 700;
  letter-spacing: 0.8px;
  text-transform: uppercase;
  cursor: pointer;
  padding: 0;
  transition: color 0.2s;
}

.hero-back-tag:hover {
  color: #ffffff;
}

.viewport-top-right {
  display: flex;
  align-items: center;
  gap: 10px;
}

.hero-search-box {
  display: flex;
  align-items: center;
  gap: 8px;
  background: rgba(13, 18, 30, 0.75);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 9999px;
  padding: 6px 14px;
  width: 250px;
  transition: all 0.2s;
}

.hero-search-box:focus-within {
  width: 300px;
  border-color: #38bdf8;
  background: rgba(13, 18, 30, 0.95);
}

.hero-search-box input {
  background: transparent;
  border: none;
  outline: none;
  color: #ffffff;
  font-size: 0.8rem;
  width: 100%;
}

.hero-search-box kbd {
  background: rgba(255, 255, 255, 0.08);
  border-radius: 4px;
  padding: 2px 5px;
  font-size: 0.65rem;
  color: #94a3b8;
  font-family: inherit;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.hero-icon-round-btn {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  background: rgba(13, 18, 30, 0.75);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: #f8fafc;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 0.9rem;
  transition: all 0.2s;
}

.hero-icon-round-btn:hover {
  background: rgba(30, 41, 59, 0.9);
  border-color: rgba(255, 255, 255, 0.25);
  transform: translateY(-1px);
}

.hero-avatar-round-btn {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  background: linear-gradient(135deg, #1e293b, #0f172a);
  border: 1.5px solid rgba(255, 255, 255, 0.25);
  color: #ffffff;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 0.84rem;
  transition: all 0.2s;
}

.hero-avatar-round-btn:hover {
  border-color: #38bdf8;
  transform: scale(1.05);
}

/* 4. Cinematic Hero Banner */
.hero-banner-container {
  position: relative;
  width: 100%;
  min-height: 400px;
  border-radius: 18px;
  background-image: 
    linear-gradient(90deg, rgba(7, 9, 14, 0.98) 0%, rgba(7, 9, 14, 0.9) 36%, rgba(7, 9, 14, 0.42) 62%, rgba(7, 9, 14, 0.12) 100%),
    url('../images/elysia-hero.jpg');
  background-size: cover;
  background-position: center right;
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 30px 32px 36px 32px;
  box-sizing: border-box;
  overflow: hidden;
}

.hero-main-content-wrap {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  position: relative;
  z-index: 5;
  width: 100%;
}

.hero-text-col {
  max-width: 500px;
}

.hero-display-headline {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 3.1rem;
  font-weight: 700;
  line-height: 1.15;
  color: #ffffff;
  letter-spacing: -0.5px;
  margin: 0 0 12px 0;
}

.hero-display-headline .headline-accent {
  background: linear-gradient(135deg, #818cf8 0%, #38bdf8 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-support-desc {
  font-size: 0.94rem;
  line-height: 1.6;
  color: #94a3b8;
  margin: 0 0 24px 0;
  max-width: 440px;
}

.hero-buttons-row {
  display: flex;
  align-items: center;
  gap: 14px;
}

.hero-btn-continue {
  background: #ffffff;
  color: #090d16;
  border: none;
  border-radius: 9999px;
  padding: 12px 24px;
  font-size: 0.88rem;
  font-weight: 700;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  transition: all 0.2s ease;
  box-shadow: 0 6px 20px rgba(255, 255, 255, 0.2);
}

.hero-btn-continue:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(255, 255, 255, 0.35);
  background: #f1f5f9;
}

.hero-btn-curriculum {
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 9999px;
  padding: 12px 22px;
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.hero-btn-curriculum:hover {
  background: rgba(255, 255, 255, 0.16);
  border-color: rgba(255, 255, 255, 0.35);
}

.hero-character-quote-tag {
  font-size: 0.78rem;
  color: rgba(255, 255, 255, 0.6);
  font-style: italic;
  line-height: 1.4;
  margin-right: 310px;
  text-align: right;
  z-index: 4;
}

/* 5. Keep Going Panel (Upper-Right Floating Card) */
.keep-going-panel {
  position: absolute;
  top: 26px;
  right: 28px;
  width: 275px;
  background: rgba(10, 14, 24, 0.82);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 14px;
  padding: 16px 18px;
  box-shadow: 0 16px 36px rgba(0, 0, 0, 0.45);
  z-index: 10;
}

.keep-going-top-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
}

.keep-going-heading {
  font-size: 0.88rem;
  font-weight: 700;
  color: #ffffff;
}

.streak-badge-flame {
  background: rgba(245, 158, 11, 0.15);
  border: 1px solid rgba(245, 158, 11, 0.35);
  color: #fbbf24;
  font-size: 0.72rem;
  font-weight: 700;
  padding: 3px 9px;
  border-radius: 9999px;
}

.week-calendar-strip {
  display: flex;
  justify-content: space-between;
  margin-bottom: 14px;
}

.cal-day-col {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  padding: 4px 3px;
  border-radius: 6px;
  min-width: 26px;
}

.cal-d-name {
  font-size: 0.62rem;
  color: #64748b;
  font-weight: 600;
}

.cal-d-num {
  font-size: 0.74rem;
  color: #94a3b8;
  font-weight: 700;
}

.cal-day-col.active {
  background: #3b82f6;
  border-radius: 16px;
  padding: 6px 4px;
  box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
}

.cal-day-col.active .cal-d-name,
.cal-day-col.active .cal-d-num {
  color: #ffffff;
}

.keep-going-quote-box {
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  padding-top: 10px;
  display: flex;
  gap: 8px;
  align-items: flex-start;
}

.kg-quote-mark {
  font-size: 1.3rem;
  line-height: 1;
  color: #64748b;
  font-family: Georgia, serif;
}

.kg-quote-text {
  font-size: 0.74rem;
  color: #94a3b8;
  line-height: 1.45;
  margin: 0;
}

.kg-author {
  font-size: 0.68rem;
  color: #64748b;
  display: block;
  margin-top: 2px;
}

/* 6. Dashboard Progress & Quick Action Cards */
.dashboard-stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px;
  width: 100%;
}

.stat-card-ref {
  background: #0d121d;
  border: 1px solid rgba(255, 255, 255, 0.07);
  border-radius: 14px;
  padding: 16px 18px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.25);
  transition: transform 0.2s ease, border-color 0.2s ease;
}

.stat-card-ref:hover {
  transform: translateY(-2px);
  border-color: rgba(255, 255, 255, 0.15);
}

.stat-card-title {
  font-size: 0.78rem;
  font-weight: 700;
  color: #94a3b8;
  margin-bottom: 10px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.progress-card-body {
  display: flex;
  align-items: center;
  gap: 16px;
}

.progress-circle-wrap {
  position: relative;
  width: 72px;
  height: 72px;
  flex-shrink: 0;
}

.stat-ring-svg {
  transform: rotate(-90deg);
}

.stat-ring-bg {
  fill: none;
  stroke: rgba(255, 255, 255, 0.08);
  stroke-width: 6;
}

.stat-ring-bar {
  fill: none;
  stroke: url(#stat-ring-grad);
  stroke-width: 6;
  stroke-linecap: round;
  stroke-dasharray: 188;
  stroke-dashoffset: 165;
  transition: stroke-dashoffset 0.8s ease;
}

.stat-ring-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 1.1rem;
  font-weight: 800;
  color: #ffffff;
}

.progress-breakdown-list {
  display: flex;
  flex-direction: column;
  gap: 4px;
  flex: 1;
}

.breakdown-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.74rem;
  color: #94a3b8;
}

.breakdown-item .dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  display: inline-block;
  margin-right: 6px;
}

.dot-blue { background: #3b82f6; }
.dot-cyan { background: #38bdf8; }
.dot-purple { background: #a855f7; }
.dot-emerald { background: #10b981; }

.breakdown-item .item-val {
  font-weight: 700;
  color: #ffffff;
}

.stat-card-header-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 10px;
}

.badge-part {
  background: rgba(245, 158, 11, 0.15);
  border: 1px solid rgba(245, 158, 11, 0.35);
  color: #fbbf24;
  font-size: 0.68rem;
  font-weight: 700;
  padding: 2px 7px;
  border-radius: 5px;
}

.current-chapter-body {
  display: flex;
  align-items: center;
  gap: 12px;
}

.chapter-icon-box {
  width: 42px;
  height: 42px;
  border-radius: 10px;
  background: rgba(30, 41, 59, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.4rem;
  flex-shrink: 0;
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.chapter-info {
  flex: 1;
}

.chapter-name {
  font-size: 0.84rem;
  font-weight: 700;
  color: #ffffff;
  line-height: 1.35;
  margin-bottom: 6px;
}

.chapter-progress-bar-wrap {
  width: 100%;
  height: 5px;
  background: rgba(255, 255, 255, 0.08);
  border-radius: 9999px;
  overflow: hidden;
  margin-bottom: 5px;
}

.chapter-progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #6366f1, #38bdf8);
  border-radius: 9999px;
}

.chapter-topics-count {
  font-size: 0.7rem;
  color: #64748b;
  font-weight: 600;
}

.next-topic-body {
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
}

.play-icon-box {
  width: 40px;
  height: 40px;
  border-radius: 10px;
  background: rgba(56, 189, 248, 0.12);
  border: 1px solid rgba(56, 189, 248, 0.3);
  color: #38bdf8;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.95rem;
  flex-shrink: 0;
  transition: all 0.2s;
}

.next-topic-body:hover .play-icon-box {
  background: #38bdf8;
  color: #0f172a;
}

.next-info {
  flex: 1;
}

.next-title {
  font-size: 0.82rem;
  font-weight: 700;
  color: #ffffff;
  line-height: 1.35;
  margin-bottom: 5px;
}

.next-meta {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.72rem;
  color: #64748b;
  font-weight: 600;
}

.arrow-sym {
  font-size: 0.88rem;
  color: #38bdf8;
}

.quick-actions-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 6px;
}

.qa-btn {
  background: rgba(30, 41, 59, 0.5);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 8px;
  padding: 8px 3px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  cursor: pointer;
  color: #94a3b8;
  transition: all 0.2s;
}

.qa-btn:hover {
  background: rgba(56, 189, 248, 0.12);
  border-color: rgba(56, 189, 248, 0.35);
  color: #ffffff;
  transform: translateY(-2px);
}

.qa-icon {
  font-size: 1rem;
}

.qa-label {
  font-size: 0.65rem;
  font-weight: 600;
  text-align: center;
  line-height: 1.2;
}

/* 7. Integrated Course Workspace (Three Coordinated Regions) */
.integrated-workspace-grid {
  display: grid;
  grid-template-columns: 270px minmax(0, 1fr) 420px;
  gap: 14px;
  width: 100%;
}

.workspace-panel {
  background: #0d121d;
  border: 1px solid rgba(255, 255, 255, 0.07);
  border-radius: 14px;
  display: flex;
  flex-direction: column;
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.3);
  overflow: hidden;
}

/* Tree Panel */
.tree-panel {
  padding: 14px;
  max-height: 760px;
}

.tree-panel-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 10px;
}

.tree-title {
  font-size: 0.92rem;
  font-weight: 800;
  color: #ffffff;
}

.tree-toggle-btn {
  background: transparent;
  border: none;
  color: #64748b;
  cursor: pointer;
  font-size: 0.95rem;
}

.tree-search-bar {
  display: flex;
  align-items: center;
  gap: 8px;
  background: rgba(30, 41, 59, 0.5);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 8px;
  padding: 6px 10px;
  margin-bottom: 12px;
}

.tree-search-bar input {
  background: transparent;
  border: none;
  outline: none;
  color: #ffffff;
  font-size: 0.78rem;
  width: 100%;
}

.course-tree-content {
  overflow-y: auto;
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding-right: 2px;
}

.tree-part-group {
  margin-bottom: 4px;
}

.tree-part-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 6px 8px;
  font-size: 0.76rem;
  font-weight: 700;
  color: #94a3b8;
  cursor: pointer;
  border-radius: 6px;
  transition: background 0.15s;
}

.tree-part-header:hover {
  background: rgba(255, 255, 255, 0.04);
  color: #ffffff;
}

.tree-part-badge {
  font-size: 0.68rem;
  color: #64748b;
}

.tree-chapters-list {
  padding-left: 6px;
  display: flex;
  flex-direction: column;
  gap: 2px;
  margin-top: 2px;
}

.tree-ch-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 5px 8px;
  font-size: 0.76rem;
  font-weight: 600;
  color: #cbd5e1;
  cursor: pointer;
  border-radius: 6px;
  transition: background 0.15s;
}

.tree-ch-header:hover {
  background: rgba(255, 255, 255, 0.05);
}

.tree-subtopics-list {
  padding-left: 10px;
  display: flex;
  flex-direction: column;
  gap: 2px;
  margin-top: 2px;
}

.tree-sub-item {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 5px 8px;
  font-size: 0.74rem;
  color: #94a3b8;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.15s;
}

.tree-sub-item:hover {
  background: rgba(255, 255, 255, 0.05);
  color: #ffffff;
}

.tree-sub-item.active {
  background: #1e3a8a;
  color: #ffffff;
  font-weight: 700;
}

/* Lesson Reader Panel */
.lesson-panel {
  padding: 20px 22px;
  overflow-y: auto;
  max-height: 760px;
}

.lesson-breadcrumb-row {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.72rem;
  color: #64748b;
  margin-bottom: 12px;
}

.bc-item.active {
  color: #38bdf8;
  font-weight: 600;
}

.lesson-title-meta-wrap {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 14px;
  margin-bottom: 8px;
}

.lesson-h2 {
  font-size: 1.4rem;
  font-weight: 800;
  color: #ffffff;
  line-height: 1.3;
  margin: 0;
}

.lesson-meta-badges {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-shrink: 0;
}

.meta-badge-time {
  font-size: 0.7rem;
  color: #94a3b8;
  background: rgba(255, 255, 255, 0.06);
  padding: 3px 8px;
  border-radius: 6px;
}

.circle-fraction-badge {
  width: 26px;
  height: 26px;
  border-radius: 50%;
  border: 1.5px solid #38bdf8;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.68rem;
  font-weight: 700;
  color: #38bdf8;
}

.lesson-summary-p {
  font-size: 0.86rem;
  line-height: 1.6;
  color: #cbd5e1;
  margin-bottom: 16px;
}

.lesson-pill-tabs {
  display: flex;
  gap: 6px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  padding-bottom: 10px;
  margin-bottom: 16px;
}

.l-tab {
  background: transparent;
  border: none;
  padding: 5px 12px;
  border-radius: 9999px;
  font-size: 0.78rem;
  font-weight: 600;
  color: #94a3b8;
  cursor: pointer;
  transition: all 0.15s;
}

.l-tab:hover {
  color: #ffffff;
  background: rgba(255, 255, 255, 0.05);
}

.l-tab.active {
  background: #3b82f6;
  color: #ffffff;
  font-weight: 700;
}

.lesson-content-layout {
  display: grid;
  grid-template-columns: 1fr 180px;
  gap: 16px;
}

.block-title {
  font-size: 1rem;
  font-weight: 700;
  color: #ffffff;
  margin: 0 0 6px 0;
}

.block-desc {
  font-size: 0.82rem;
  color: #94a3b8;
  margin: 0 0 10px 0;
}

.code-snippet-box {
  background: #060912;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 8px;
  overflow: hidden;
  margin-bottom: 10px;
}

.code-snippet-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 5px 10px;
  background: rgba(255, 255, 255, 0.03);
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  font-size: 0.7rem;
  color: #64748b;
}

.copy-btn {
  background: transparent;
  border: none;
  color: #94a3b8;
  cursor: pointer;
  font-size: 0.7rem;
}

.copy-btn:hover {
  color: #ffffff;
}

.snippet-pre {
  padding: 10px 12px;
  margin: 0;
  font-family: var(--font-mono);
  font-size: 0.82rem;
  color: #e2e8f0;
}

.output-preview-card {
  background: #060912;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 8px;
  padding: 8px 12px;
  margin-bottom: 12px;
}

.output-preview-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.72rem;
  font-weight: 700;
  color: #64748b;
  margin-bottom: 4px;
}

.btn-run-snippet {
  background: #3b82f6;
  border: none;
  border-radius: 5px;
  color: #ffffff;
  padding: 3px 8px;
  font-size: 0.7rem;
  font-weight: 700;
  cursor: pointer;
}

.output-preview-text {
  font-family: var(--font-mono);
  font-size: 0.82rem;
  color: #10b981;
}

.educational-tip-box {
  background: rgba(245, 158, 11, 0.08);
  border: 1px solid rgba(245, 158, 11, 0.25);
  border-radius: 8px;
  padding: 10px 12px;
  display: flex;
  align-items: flex-start;
  gap: 8px;
  font-size: 0.8rem;
  color: #fef3c7;
  line-height: 1.5;
}

.lesson-subrail-col {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.subrail-heading {
  font-size: 0.7rem;
  font-weight: 700;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 6px;
}

.subrail-links-list {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.subrail-link {
  font-size: 0.74rem;
  color: #94a3b8;
  text-decoration: none;
  padding: 3px 6px;
  border-radius: 4px;
  border-left: 2px solid transparent;
}

.subrail-link:hover {
  color: #ffffff;
}

.subrail-link.active {
  color: #38bdf8;
  border-left-color: #38bdf8;
  background: rgba(56, 189, 248, 0.08);
  font-weight: 600;
}

.subrail-bullets-list {
  padding-left: 14px;
  margin: 0;
  font-size: 0.74rem;
  color: #94a3b8;
  line-height: 1.6;
}

.related-link {
  display: block;
  font-size: 0.73rem;
  color: #94a3b8;
  text-decoration: none;
  margin-bottom: 5px;
}

.related-link:hover {
  color: #38bdf8;
}

/* Editor Panel */
.editor-panel {
  padding: 14px;
  max-height: 760px;
}

.editor-panel-tabs {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 8px;
}

.editor-tabs-group {
  display: flex;
  gap: 4px;
}

.e-tab {
  background: transparent;
  border: none;
  font-size: 0.78rem;
  font-weight: 600;
  color: #94a3b8;
  padding: 5px 10px;
  border-radius: 6px;
  cursor: pointer;
}

.e-tab.active {
  background: rgba(255, 255, 255, 0.08);
  color: #ffffff;
  font-weight: 700;
}

.e-expand-btn {
  background: transparent;
  border: none;
  color: #64748b;
  cursor: pointer;
  font-size: 0.95rem;
}

.editor-engine-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 8px;
}

.engine-pill {
  display: flex;
  align-items: center;
  gap: 6px;
  background: rgba(30, 41, 59, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 6px;
  padding: 3px 8px;
}

.engine-dropdown {
  background: transparent;
  border: none;
  outline: none;
  color: #38bdf8;
  font-size: 0.72rem;
  font-weight: 700;
  cursor: pointer;
}

.btn-editor-reset {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 6px;
  padding: 3px 8px;
  font-size: 0.72rem;
  color: #94a3b8;
  cursor: pointer;
}

.monaco-like-editor-wrapper {
  background: #060912;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 8px;
  min-height: 200px;
  max-height: 260px;
  overflow: hidden;
  margin-bottom: 10px;
}

.btn-run-prominent {
  width: 100%;
  background: linear-gradient(135deg, #4f46e5, #3b82f6);
  border: none;
  border-radius: 8px;
  color: #ffffff;
  font-size: 0.88rem;
  font-weight: 700;
  padding: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  cursor: pointer;
  margin-bottom: 12px;
  box-shadow: 0 4px 18px rgba(79, 70, 229, 0.35);
  transition: all 0.2s;
}

.btn-run-prominent:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 24px rgba(79, 70, 229, 0.5);
}

.run-key-hint {
  font-size: 0.7rem;
  opacity: 0.7;
  font-weight: 500;
}

.terminal-box-ref {
  background: #060912;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 8px;
  padding: 8px 10px;
  margin-bottom: 12px;
}

.term-tabs-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  padding-bottom: 4px;
  margin-bottom: 6px;
}

.term-left-tabs {
  display: flex;
  gap: 2px;
}

.term-tab {
  background: transparent;
  border: none;
  font-size: 0.7rem;
  color: #64748b;
  cursor: pointer;
  padding: 2px 5px;
}

.term-tab.active {
  color: #38bdf8;
  font-weight: 700;
}

.term-clear-btn {
  background: transparent;
  border: none;
  color: #64748b;
  cursor: pointer;
  font-size: 0.7rem;
}

.stdout-text {
  font-family: var(--font-mono);
  font-size: 0.8rem;
  color: #10b981;
  min-height: 36px;
}

.stderr-text {
  font-family: var(--font-mono);
  font-size: 0.8rem;
  color: #f43f5e;
}

.try-yourself-card {
  background: rgba(30, 41, 59, 0.4);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 8px;
  padding: 10px;
}

.try-yourself-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 5px;
}

.try-head-left {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.78rem;
  font-weight: 700;
  color: #fbbf24;
}

.try-hint-btn {
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 5px;
  color: #ffffff;
  padding: 2px 6px;
  font-size: 0.68rem;
  cursor: pointer;
}

.try-prompt-p {
  font-size: 0.76rem;
  color: #cbd5e1;
  line-height: 1.4;
  margin: 0 0 6px 0;
}

.try-footer-row {
  display: flex;
  justify-content: flex-end;
}

.try-sol-btn {
  background: transparent;
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 5px;
  color: #94a3b8;
  font-size: 0.68rem;
  padding: 2px 6px;
  cursor: pointer;
}

/* 8. Lower Showcase Previews Row */
.bottom-showcase-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px;
  width: 100%;
  margin-top: 4px;
}

.showcase-card {
  border-radius: 14px;
  padding: 16px 18px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  background-size: cover;
  background-position: center;
  min-height: 260px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
}

.sc-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  margin-bottom: 12px;
}

.sc-title {
  font-size: 1rem;
  font-weight: 800;
  color: #ffffff;
  margin: 0 0 2px 0;
}

.sc-subtitle {
  font-size: 0.7rem;
  color: #94a3b8;
  margin: 0;
}

.sc-tabs {
  display: flex;
  gap: 3px;
}

.sc-tab {
  background: rgba(255, 255, 255, 0.06);
  border: none;
  border-radius: 9999px;
  padding: 2px 6px;
  font-size: 0.62rem;
  color: #94a3b8;
  cursor: pointer;
}

.sc-tab.active {
  background: #3b82f6;
  color: #ffffff;
}

.sc-items-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
}

.sc-item-box {
  background: rgba(13, 18, 30, 0.88);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 8px;
  padding: 8px;
  cursor: pointer;
  transition: transform 0.2s, border-color 0.2s;
}

.sc-item-box:hover {
  transform: translateY(-2px);
  border-color: #38bdf8;
}

.sc-item-thumb {
  width: 28px;
  height: 28px;
  border-radius: 6px;
  background: rgba(56, 189, 248, 0.15);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1rem;
  margin-bottom: 6px;
}

.sc-item-title {
  font-size: 0.74rem;
  font-weight: 700;
  color: #ffffff;
  line-height: 1.25;
  margin-bottom: 3px;
}

.sc-item-meta {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.62rem;
  color: #64748b;
  margin-bottom: 3px;
}

.level-tag {
  padding: 1px 4px;
  border-radius: 3px;
  font-weight: 700;
}

.level-tag.beginner {
  background: rgba(16, 185, 129, 0.15);
  color: #34d399;
}

.level-tag.intermediate {
  background: rgba(245, 158, 11, 0.15);
  color: #fbbf24;
}

.sc-item-desc {
  font-size: 0.65rem;
  color: #94a3b8;
  line-height: 1.3;
  margin: 0;
}

.sc-exam-card {
  background: rgba(13, 18, 30, 0.88);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 8px;
  padding: 10px 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  cursor: pointer;
  transition: transform 0.2s, border-color 0.2s;
}

.sc-exam-card:hover {
  transform: translateY(-2px);
  border-color: #a855f7;
}

.exam-icon-circle {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.9rem;
  margin-bottom: 4px;
}

.exam-icon-circle.blue-icon { background: rgba(56, 189, 248, 0.15); color: #38bdf8; }
.exam-icon-circle.purple-icon { background: rgba(168, 85, 247, 0.15); color: #c084fc; }
.exam-icon-circle.green-icon { background: rgba(16, 185, 129, 0.15); color: #34d399; }

.exam-card-title {
  font-size: 0.74rem;
  font-weight: 700;
  color: #ffffff;
}

.exam-card-sub {
  font-size: 0.65rem;
  color: #64748b;
  margin-bottom: 4px;
}

.exam-card-meta {
  font-size: 0.64rem;
  color: #94a3b8;
  margin-bottom: 6px;
}

.btn-start-exam {
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 5px;
  color: #ffffff;
  font-size: 0.66rem;
  font-weight: 600;
  padding: 2px 8px;
  cursor: pointer;
}

.preview-badge-header {
  font-size: 0.72rem;
  font-weight: 700;
  color: #94a3b8;
  margin-bottom: 8px;
}

.device-mockup-frame {
  background: #090d16;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 10px;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.device-mockup-frame.light-frame {
  background: #ffffff;
  border-color: rgba(0, 0, 0, 0.1);
}

.mockup-header-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.72rem;
  font-weight: 700;
  color: #ffffff;
  padding-bottom: 6px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.mockup-header-bar.light {
  color: #0f172a;
  border-bottom-color: rgba(0, 0, 0, 0.08);
}

.mockup-body {
  padding: 6px 0;
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.mockup-greet {
  font-size: 0.72rem;
  color: #cbd5e1;
  line-height: 1.3;
}

.mockup-greet.light {
  color: #334155;
}

.mockup-hero-btn {
  background: #ffffff;
  color: #090d16;
  font-size: 0.68rem;
  font-weight: 700;
  border-radius: 9999px;
  padding: 4px 10px;
  text-align: center;
  margin: 3px 0;
  border: none;
  cursor: pointer;
}

.mockup-hero-btn.light-btn {
  background: #3b82f6;
  color: #ffffff;
}

.mockup-course-title {
  font-size: 0.7rem;
  font-weight: 700;
  color: #94a3b8;
}

.mockup-course-title.light {
  color: #64748b;
}

.mockup-part-row, .mockup-ch-row {
  font-size: 0.65rem;
  color: #64748b;
  display: flex;
  justify-content: space-between;
}

.part-prog, .ch-prog {
  font-weight: 700;
  color: #38bdf8;
}

/* 9. Light Theme Complete Overrides */
body[data-theme="light"] .app-layout,
body[data-theme="light"] .app-main-viewport {
  background: #f8fafc;
  color: #0f172a;
}

body[data-theme="light"] .app-sidebar {
  background: #ffffff;
  border-right-color: rgba(0, 0, 0, 0.07);
}

body[data-theme="light"] .brand-title-text {
  color: #0f172a;
}

body[data-theme="light"] .side-nav-btn {
  color: #64748b;
}

body[data-theme="light"] .side-nav-btn:hover {
  background: #f1f5f9;
  color: #0f172a;
}

body[data-theme="light"] .side-nav-btn.active {
  background: #e2e8f0;
  color: #0f172a;
}

body[data-theme="light"] .side-user-chip {
  background: #f1f5f9;
}

body[data-theme="light"] .side-user-name {
  color: #0f172a;
}

body[data-theme="light"] .hero-back-tag {
  color: #475569;
}
body[data-theme="light"] .hero-back-tag:hover {
  color: #0f172a;
}

body[data-theme="light"] .hero-search-box {
  background: rgba(255, 255, 255, 0.9);
  border-color: rgba(0, 0, 0, 0.1);
}
body[data-theme="light"] .hero-search-box input {
  color: #0f172a;
}

body[data-theme="light"] .hero-icon-round-btn {
  background: #ffffff;
  border-color: rgba(0, 0, 0, 0.1);
  color: #0f172a;
}

body[data-theme="light"] .hero-avatar-round-btn {
  background: #ffffff;
  color: #0f172a;
  border-color: rgba(0, 0, 0, 0.15);
}

body[data-theme="light"] .hero-banner-container {
  background-image: 
    linear-gradient(90deg, rgba(255, 255, 255, 0.97) 0%, rgba(255, 255, 255, 0.88) 38%, rgba(255, 255, 255, 0.38) 64%, rgba(255, 255, 255, 0.08) 100%),
    url('../images/elysia-hero-light.jpg');
  border-color: rgba(0, 0, 0, 0.08);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.06);
}

body[data-theme="light"] .hero-display-headline {
  color: #0f172a;
}

body[data-theme="light"] .hero-support-desc {
  color: #475569;
}

body[data-theme="light"] .hero-character-quote-tag {
  color: rgba(15, 23, 42, 0.6);
}

body[data-theme="light"] .hero-btn-curriculum {
  background: rgba(15, 23, 42, 0.06);
  color: #0f172a;
  border-color: rgba(15, 23, 42, 0.15);
}

body[data-theme="light"] .keep-going-panel {
  background: rgba(255, 255, 255, 0.9);
  border-color: rgba(0, 0, 0, 0.08);
  box-shadow: 0 10px 24px rgba(0, 0, 0, 0.08);
}

body[data-theme="light"] .keep-going-heading {
  color: #0f172a;
}

body[data-theme="light"] .stat-card-ref,
body[data-theme="light"] .workspace-panel {
  background: #ffffff;
  border-color: rgba(0, 0, 0, 0.07);
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.04);
}

body[data-theme="light"] .stat-card-title,
body[data-theme="light"] .tree-part-header,
body[data-theme="light"] .block-desc {
  color: #64748b;
}

body[data-theme="light"] .stat-ring-text,
body[data-theme="light"] .item-val,
body[data-theme="light"] .chapter-name,
body[data-theme="light"] .next-title,
body[data-theme="light"] .tree-title,
body[data-theme="light"] .lesson-h2,
body[data-theme="light"] .block-title {
  color: #0f172a;
}

body[data-theme="light"] .tree-search-bar {
  background: #f1f5f9;
  border-color: rgba(0, 0, 0, 0.08);
}
body[data-theme="light"] .tree-search-bar input {
  color: #0f172a;
}

body[data-theme="light"] .tree-sub-item.active {
  background: #dbeafe;
  color: #1e40af;
}

body[data-theme="light"] .qa-btn {
  background: #f1f5f9;
  border-color: rgba(0, 0, 0, 0.06);
  color: #475569;
}
body[data-theme="light"] .qa-btn:hover {
  background: #e2e8f0;
  color: #0f172a;
}

body[data-theme="light"] .lesson-summary-p,
body[data-theme="light"] .breakdown-item {
  color: #475569;
}

body[data-theme="light"] .educational-tip-box {
  background: #fffbeb;
  border-color: #fcd34d;
  color: #92400e;
}

/* 10. Responsive Design for Smaller Devices */
@media (max-width: 1200px) {
  .integrated-workspace-grid {
    grid-template-columns: 240px 1fr;
  }
  .editor-panel {
    grid-column: span 2;
  }
  .bottom-showcase-row {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 900px) {
  .app-sidebar {
    display: none;
  }
  .dashboard-stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .integrated-workspace-grid {
    grid-template-columns: 1fr;
  }
  .editor-panel {
    grid-column: span 1;
  }
  .bottom-showcase-row {
    grid-template-columns: 1fr;
  }
  .hero-character-quote-tag {
    display: none;
  }
  .keep-going-panel {
    position: static;
    width: 100%;
    margin-top: 18px;
  }
  .lesson-content-layout {
    grid-template-columns: 1fr;
  }
  .lesson-subrail-col {
    display: none;
  }
}
"""

with open('web/css/style.css', 'a') as f:
    f.write(css_content)

print("Appended reference styles successfully to web/css/style.css")
