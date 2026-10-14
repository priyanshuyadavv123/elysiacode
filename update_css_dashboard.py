import os

css_path = "/Users/priyanshuyadav/.gemini/antigravity/scratch/elysia-code/web/css/style.css"
with open(css_path, "r", encoding="utf-8") as f:
    content = f.read()

start_marker = "/* 8. Lower Showcase Previews Row */"
end_marker = "/* 9. Light Theme Complete Overrides */"

if start_marker not in content or end_marker not in content:
    print("Markers not found!")
    exit(1)

replacement_css = """/* =========================================================================
   8. MASTER LOWER DASHBOARD CANVAS (Pixel-Matched to Reference Screenshot)
   ========================================================================= */
.master-dashboard-canvas,
.bottom-showcase-row {
  width: 100%;
  max-width: 100%;
  box-sizing: border-box;
  background: #f1f5f9;
  border-radius: 18px;
  padding: 24px;
  margin-top: 4px;
  border: 1px solid rgba(0, 0, 0, 0.06);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03);
  display: flex;
  flex-direction: column;
  gap: 20px;
}

/* Universal Dashboard White Card Surface */
.dash-card {
  background: #ffffff;
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: 14px;
  padding: 20px;
  box-shadow: 0 2px 14px rgba(0, 0, 0, 0.03);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  box-sizing: border-box;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.dash-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06);
}

.dash-card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 14px;
}

.dash-card-title {
  font-size: 0.86rem;
  font-weight: 800;
  color: #0f172a;
  letter-spacing: -0.2px;
}

.dash-card-badge {
  font-size: 0.65rem;
  font-weight: 700;
  background: #f1f5f9;
  color: #475569;
  padding: 3px 8px;
  border-radius: 9999px;
  border: 1px solid #e2e8f0;
}

.dash-see-all-link {
  font-size: 0.72rem;
  font-weight: 700;
  color: #2563eb;
  cursor: pointer;
  text-decoration: none;
  transition: color 0.15s ease;
}

.dash-see-all-link:hover {
  color: #1d4ed8;
  text-decoration: underline;
}

/* --- ROW 1 GRID --- */
.dash-row-1 {
  display: grid;
  grid-template-columns: 1.15fr 1.35fr 1.1fr;
  gap: 18px;
  width: 100%;
}

/* Card 1: Resume Learning */
.dash-card-resume {
  cursor: pointer;
}

.resume-card-body {
  display: flex;
  gap: 14px;
  align-items: center;
}

.resume-media-wrap {
  position: relative;
  width: 110px;
  height: 90px;
  border-radius: 10px;
  overflow: hidden;
  flex-shrink: 0;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.resume-thumb-img {
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  transition: transform 0.3s ease;
}

.dash-card-resume:hover .resume-thumb-img {
  transform: scale(1.08);
}

.resume-play-bubble {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 34px;
  height: 34px;
  border-radius: 50%;
  background: #2563eb;
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.8rem;
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.5);
  transition: transform 0.2s;
}

.dash-card-resume:hover .resume-play-bubble {
  transform: translate(-50%, -50%) scale(1.12);
  background: #1d4ed8;
}

.resume-details {
  flex: 1;
  min-width: 0;
}

.resume-part-tag {
  font-size: 0.65rem;
  font-weight: 700;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 0.4px;
}

.resume-topic-title {
  font-size: 0.88rem;
  font-weight: 700;
  color: #0f172a;
  margin: 3px 0 8px 0;
  line-height: 1.3;
}

.resume-progress-meta {
  display: flex;
  justify-content: space-between;
  font-size: 0.7rem;
  color: #64748b;
  font-weight: 600;
  margin-bottom: 5px;
}

.resume-pct-val {
  font-weight: 800;
  color: #2563eb;
}

.resume-bar-track {
  width: 100%;
  height: 6px;
  background: #e2e8f0;
  border-radius: 9999px;
  overflow: hidden;
}

.resume-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, #3b82f6, #06b6d4);
  border-radius: 9999px;
}

/* Card 2: Quick Actions (5 Colored Action Tiles) */
.quick-actions-tiles-row {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 10px;
}

.qa-tile {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 12px 6px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
  text-align: center;
}

.qa-tile:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.06);
}

.qa-tile-icon-box {
  width: 36px;
  height: 36px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.05rem;
  font-weight: 800;
}

.tile-practice .qa-tile-icon-box { background: rgba(6, 182, 212, 0.15); color: #0891b2; }
.tile-quiz .qa-tile-icon-box { background: rgba(168, 85, 247, 0.15); color: #9333ea; }
.tile-project .qa-tile-icon-box { background: rgba(99, 102, 241, 0.15); color: #4f46e5; }
.tile-handbook .qa-tile-icon-box { background: rgba(245, 158, 11, 0.15); color: #d97706; }
.tile-ai .qa-tile-icon-box { background: rgba(16, 185, 129, 0.15); color: #059669; }

.qa-tile-name {
  font-size: 0.72rem;
  font-weight: 700;
  color: #1e293b;
  line-height: 1.2;
}

.qa-tile-sub {
  font-size: 0.6rem;
  color: #64748b;
  line-height: 1.15;
}

/* Card 3: Elysia AI (Contrasting Dark Card with Orb & Interactive Prompts) */
.dash-card-ai {
  background: #090e18 !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  color: #ffffff;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.25) !important;
}

.dash-ai-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 8px;
}

.dash-ai-title-wrap {
  display: flex;
  align-items: center;
  gap: 8px;
}

.dash-ai-title {
  font-size: 0.95rem;
  font-weight: 800;
  color: #ffffff;
}

.dash-ai-status {
  font-size: 0.65rem;
  font-weight: 700;
  color: #34d399;
  display: flex;
  align-items: center;
  gap: 4px;
}

.pulse-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #10b981;
  box-shadow: 0 0 8px #10b981;
}

.dash-ai-orb-mini {
  font-size: 1.1rem;
}

.dash-ai-desc {
  font-size: 0.74rem;
  color: #94a3b8;
  margin: 0 0 10px 0;
  line-height: 1.35;
}

.dash-ai-prompts-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px;
}

.ai-prompt-btn {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  padding: 7px 8px;
  color: #cbd5e1;
  font-size: 0.68rem;
  text-align: left;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: all 0.18s ease;
  line-height: 1.25;
}

.ai-prompt-btn:hover {
  background: rgba(56, 189, 248, 0.15);
  border-color: #38bdf8;
  color: #ffffff;
  transform: translateY(-1px);
}

/* --- ROW 2 GRID --- */
.dash-row-2 {
  display: grid;
  grid-template-columns: 1.1fr 1.35fr 1.1fr;
  gap: 18px;
  width: 100%;
}

/* Card 1: Your Learning Path */
.dash-card-path {
  position: relative;
  overflow: hidden;
}

.learning-path-scroll-body {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 24px;
}

.path-part-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.path-part-header {
  display: flex;
  align-items: center;
  gap: 8px;
}

.path-part-dot {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.7rem;
  font-weight: 800;
}

.path-part-dot.active {
  background: #10b981;
  color: #ffffff;
}

.path-part-dot.locked {
  background: #f1f5f9;
  color: #94a3b8;
  border: 1px solid #cbd5e1;
}

.path-part-title {
  font-size: 0.78rem;
  font-weight: 700;
  color: #0f172a;
}

.path-part-group.locked .path-part-title {
  color: #64748b;
}

.path-chapters-timeline {
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin-left: 11px;
  padding-left: 16px;
  border-left: 2px solid #e2e8f0;
}

.path-ch-item {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.72rem;
  color: #334155;
  cursor: pointer;
  padding: 3px 0;
  transition: color 0.15s ease;
}

.path-ch-item:hover {
  color: #2563eb;
}

.path-ch-item .ch-marker.done { color: #10b981; font-size: 0.85rem; }
.path-ch-item .ch-marker.current { color: #3b82f6; font-size: 0.85rem; }
.path-ch-item .ch-marker.locked { color: #94a3b8; font-size: 0.75rem; }

.path-ch-item.locked {
  color: #94a3b8;
  cursor: default;
}

.path-ch-item .ch-status {
  margin-left: auto;
  font-size: 0.62rem;
  color: #94a3b8;
  font-weight: 600;
}

.path-ch-item .ch-status.current {
  color: #2563eb;
  font-weight: 700;
}

.path-bottom-scenic-fade {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 60px;
  background-size: cover;
  background-position: center bottom;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  padding-bottom: 8px;
}

.path-scenic-quote {
  font-size: 0.68rem;
  font-style: italic;
  color: #334155;
  font-weight: 600;
}

/* Card 2: Continue Where You Left Off */
.continue-cards-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.continue-item-row {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 12px;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.18s ease;
}

.continue-item-row:hover {
  background: #f1f5f9;
  border-color: #cbd5e1;
  transform: translateX(3px);
}

.continue-item-thumb {
  width: 38px;
  height: 38px;
  border-radius: 8px;
  background: rgba(59, 130, 246, 0.15);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.1rem;
  flex-shrink: 0;
}

.continue-item-thumb.purple { background: rgba(168, 85, 247, 0.15); }
.continue-item-thumb.emerald { background: rgba(16, 185, 129, 0.15); }

.continue-item-info {
  flex: 1;
  min-width: 0;
}

.continue-part-tag {
  font-size: 0.62rem;
  font-weight: 700;
  color: #64748b;
  text-transform: uppercase;
}

.continue-item-title {
  font-size: 0.8rem;
  font-weight: 700;
  color: #0f172a;
  margin: 2px 0 3px 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.continue-item-meta {
  font-size: 0.66rem;
  color: #64748b;
}

.continue-btn-action {
  background: #2563eb;
  color: #ffffff;
  border: none;
  border-radius: 6px;
  padding: 6px 12px;
  font-size: 0.72rem;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.15s ease;
  flex-shrink: 0;
}

.continue-btn-action:hover {
  background: #1d4ed8;
}

.continue-btn-action.secondary {
  background: #f1f5f9;
  color: #334155;
  border: 1px solid #cbd5e1;
}

.continue-btn-action.secondary:hover {
  background: #e2e8f0;
  color: #0f172a;
}

/* Card 3: Featured Project (Japanese Temple Torii Artwork) */
.dash-card-featured-project {
  position: relative;
  background-size: cover;
  background-position: center;
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.35) !important;
  justify-content: space-between;
  min-height: 230px;
}

.featured-proj-badge {
  align-self: flex-start;
  background: rgba(16, 185, 129, 0.25);
  border: 1px solid rgba(16, 185, 129, 0.4);
  color: #34d399;
  font-size: 0.65rem;
  font-weight: 800;
  padding: 3px 8px;
  border-radius: 9999px;
  text-transform: uppercase;
}

.featured-proj-body {
  margin-top: auto;
}

.featured-proj-title {
  font-size: 1.05rem;
  font-weight: 800;
  color: #ffffff;
  margin: 0 0 6px 0;
}

.featured-proj-desc {
  font-size: 0.72rem;
  color: #cbd5e1;
  line-height: 1.4;
  margin: 0 0 10px 0;
}

.featured-proj-meta {
  display: flex;
  gap: 12px;
  font-size: 0.68rem;
  color: #94a3b8;
  margin-bottom: 14px;
}

.btn-start-featured-proj {
  background: #ffffff;
  color: #090d16;
  border: none;
  border-radius: 8px;
  padding: 8px 16px;
  font-size: 0.78rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 4px 12px rgba(255, 255, 255, 0.25);
}

.btn-start-featured-proj:hover {
  background: #f1f5f9;
  transform: translateY(-1px);
}

/* --- ROW 3 GRID --- */
.dash-row-3 {
  display: grid;
  grid-template-columns: 1.25fr 1.15fr 1.1fr;
  gap: 18px;
  width: 100%;
}

/* Card 1: Mock Exams */
.dash-exams-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.dash-exam-row {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 9px 12px;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.16s ease;
}

.dash-exam-row:hover {
  background: #f1f5f9;
  border-color: #cbd5e1;
}

.dash-exam-icon {
  width: 30px;
  height: 30px;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.95rem;
  flex-shrink: 0;
}

.dash-exam-icon.blue { background: rgba(59, 130, 246, 0.15); color: #2563eb; }
.dash-exam-icon.purple { background: rgba(168, 85, 247, 0.15); color: #9333ea; }
.dash-exam-icon.emerald { background: rgba(16, 185, 129, 0.15); color: #059669; }

.dash-exam-info {
  flex: 1;
  min-width: 0;
}

.dash-exam-name {
  display: block;
  font-size: 0.76rem;
  font-weight: 700;
  color: #0f172a;
}

.dash-exam-sub {
  display: block;
  font-size: 0.64rem;
  color: #64748b;
}

.btn-dash-exam-start {
  background: #ffffff;
  border: 1px solid #cbd5e1;
  color: #1e293b;
  border-radius: 6px;
  padding: 4px 10px;
  font-size: 0.68rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.15s ease;
}

.dash-exam-row:hover .btn-dash-exam-start {
  background: #2563eb;
  border-color: #2563eb;
  color: #ffffff;
}

/* Card 2: Visual Handbook */
.dash-handbook-list {
  display: flex;
  flex-direction: column;
  gap: 7px;
}

.dash-handbook-row {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 10px;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.16s ease;
}

.dash-handbook-row:hover {
  background: #f1f5f9;
  border-color: #cbd5e1;
  transform: translateX(2px);
}

.dash-hb-icon {
  font-size: 0.9rem;
}

.dash-hb-title {
  font-size: 0.73rem;
  font-weight: 600;
  color: #334155;
  flex: 1;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.dash-hb-arrow {
  color: #94a3b8;
  font-size: 0.85rem;
  font-weight: 700;
}

/* Card 3: My Stats (2x2 Grid) */
.my-stats-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}

.my-stat-box {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  padding: 10px 12px;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.my-stat-icon {
  font-size: 1rem;
  margin-bottom: 2px;
}

.my-stat-val {
  font-size: 1.15rem;
  font-weight: 800;
  color: #0f172a;
}

.my-stat-lbl {
  font-size: 0.65rem;
  color: #64748b;
  font-weight: 600;
}

/* Dark mode styling support for Master Dashboard Canvas */
body[data-theme="dark"] .master-dashboard-canvas,
body[data-theme="midnight"] .master-dashboard-canvas {
  background: #090e18;
  border-color: rgba(255, 255, 255, 0.08);
}

body[data-theme="dark"] .dash-card:not(.dash-card-ai):not(.dash-card-featured-project),
body[data-theme="midnight"] .dash-card:not(.dash-card-ai):not(.dash-card-featured-project) {
  background: #0d1322;
  border-color: rgba(255, 255, 255, 0.08);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.35);
}

body[data-theme="dark"] .dash-card-title,
body[data-theme="midnight"] .dash-card-title,
body[data-theme="dark"] .resume-topic-title,
body[data-theme="midnight"] .resume-topic-title,
body[data-theme="dark"] .path-part-title,
body[data-theme="midnight"] .path-part-title,
body[data-theme="dark"] .continue-item-title,
body[data-theme="midnight"] .continue-item-title,
body[data-theme="dark"] .dash-exam-name,
body[data-theme="midnight"] .dash-exam-name,
body[data-theme="dark"] .my-stat-val,
body[data-theme="midnight"] .my-stat-val {
  color: #ffffff;
}

body[data-theme="dark"] .continue-item-row,
body[data-theme="midnight"] .continue-item-row,
body[data-theme="dark"] .dash-exam-row,
body[data-theme="midnight"] .dash-exam-row,
body[data-theme="dark"] .dash-handbook-row,
body[data-theme="midnight"] .dash-handbook-row,
body[data-theme="dark"] .my-stat-box,
body[data-theme="midnight"] .my-stat-box,
body[data-theme="dark"] .qa-tile,
body[data-theme="midnight"] .qa-tile {
  background: rgba(255, 255, 255, 0.04);
  border-color: rgba(255, 255, 255, 0.08);
}

body[data-theme="dark"] .qa-tile-name,
body[data-theme="midnight"] .qa-tile-name,
body[data-theme="dark"] .dash-hb-title,
body[data-theme="midnight"] .dash-hb-title,
body[data-theme="dark"] .path-ch-item,
body[data-theme="midnight"] .path-ch-item {
  color: #cbd5e1;
}

"""

new_content = content[:content.find(start_marker)] + replacement_css + content[content.find(end_marker):]

# Also ensure sidebar stays dark navy in light theme
light_sidebar_override = """body[data-theme="light"] .app-sidebar {
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
}"""

if light_sidebar_override in new_content:
    new_content = new_content.replace(light_sidebar_override, "/* Sidebar retains signature dark navy aesthetic */")

with open(css_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("CSS updated successfully!")
