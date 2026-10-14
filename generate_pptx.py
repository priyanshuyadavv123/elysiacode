"""
=============================================================================
✨ ELYSIA CODE: MASTER PRESENTATION GENERATOR (.pptx)
=============================================================================
Generates a 14-slide 16:9 widescreen PowerPoint deck covering every
single detail of the Elysia Code platform:
- Architecture, Habit Engineering, Zero-to-Advanced Pedagogy
- Split-screen IDE, Interactive Stdin, Pyodide WASM
- Visual Handbook, Socratic Senior AI, 60s Doubt Buster
- Question Bank, 25-Min Semester Mock Exam
- 1-Click College Lab File Exporter (PDF)
- Authentication & Profile Picture System
- 3D Holographic Flex Card & Gamification
- Technical Stack, Benchmarks, Future Roadmap
=============================================================================
"""

import sys
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# Widescreen 16:9 Dimensions
SLIDE_WIDTH = Inches(13.333)
SLIDE_HEIGHT = Inches(7.5)

# Cyber Theme Palette
COLOR_BG = RGBColor(10, 15, 29)          # Deep Navy/Obsidian #0a0f1d
COLOR_CARD = RGBColor(21, 30, 50)        # Dark Slate #151e32
COLOR_BORDER = RGBColor(42, 59, 92)      # Slate Border #2a3b5c
COLOR_CYAN = RGBColor(56, 189, 248)      # Electric Cyan #38bdf8
COLOR_PURPLE = RGBColor(168, 85, 247)    # Neon Purple #a855f7
COLOR_GREEN = RGBColor(52, 211, 153)     # Emerald Green #34d399
COLOR_AMBER = RGBColor(251, 191, 36)     # Amber Gold #fbbf24
COLOR_ROSE = RGBColor(244, 63, 94)       # Rose Red #f43f5e
COLOR_WHITE = RGBColor(255, 255, 255)    # Pure White
COLOR_MUTED = RGBColor(148, 163, 184)    # Slate Gray #94a3b8
COLOR_CODE_BG = RGBColor(3, 7, 18)       # Black Code Box #030712


def set_slide_background(slide, color=COLOR_BG):
    """Fill slide background with solid dark color."""
    bg_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SLIDE_WIDTH, SLIDE_HEIGHT)
    bg_shape.fill.solid()
    bg_shape.fill.fore_color.rgb = color
    bg_shape.line.fill.background()
    return bg_shape


def add_header(slide, badge_text, title_text, subtitle_text, badge_color=COLOR_CYAN):
    """Add standard top header block with badge, title, and subtitle."""
    # 1. Badge Pill
    badge_box = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.45), Inches(3.2), Inches(0.38)
    )
    badge_box.fill.solid()
    badge_box.fill.fore_color.rgb = RGBColor(18, 36, 64)
    badge_box.line.color.rgb = badge_color
    badge_box.line.width = Pt(1)
    
    tf_b = badge_box.text_frame
    tf_b.word_wrap = True
    tf_b.margin_left = tf_b.margin_right = tf_b.margin_top = tf_b.margin_bottom = 0
    p_b = tf_b.paragraphs[0]
    p_b.text = badge_text.upper()
    p_b.font.size = Pt(10)
    p_b.font.bold = True
    p_b.font.color.rgb = badge_color
    p_b.alignment = PP_ALIGN.CENTER

    # 2. Title & Subtitle Box
    header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.95), Inches(11.7), Inches(1.3))
    tf_h = header_box.text_frame
    tf_h.word_wrap = True
    tf_h.margin_left = tf_h.margin_right = tf_h.margin_top = tf_h.margin_bottom = 0

    p_title = tf_h.paragraphs[0]
    p_title.text = title_text
    p_title.font.size = Pt(26)
    p_title.font.bold = True
    p_title.font.color.rgb = COLOR_WHITE

    p_sub = tf_h.add_paragraph()
    p_sub.text = subtitle_text
    p_sub.font.size = Pt(13)
    p_sub.font.color.rgb = COLOR_MUTED
    p_sub.space_before = Pt(4)


def add_card(slide, left, top, width, height, title, body="", icon="", border_color=COLOR_BORDER):
    """Add a glassmorphism style content card."""
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = COLOR_CARD
    card.line.color.rgb = border_color
    card.line.width = Pt(1.5)

    tf = card.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.25)
    tf.margin_right = Inches(0.25)
    tf.margin_top = Inches(0.25)
    tf.margin_bottom = Inches(0.25)

    # Title with icon
    p_title = tf.paragraphs[0]
    p_title.text = f"{icon} {title}".strip()
    p_title.font.size = Pt(14)
    p_title.font.bold = True
    p_title.font.color.rgb = COLOR_WHITE

    # Body text
    if body:
        p_body = tf.add_paragraph()
        p_body.text = body
        p_body.font.size = Pt(11)
        p_body.font.color.rgb = COLOR_MUTED
        p_body.space_before = Pt(8)

    return card, tf


def add_footer(slide, current_slide, total_slides=14):
    """Add bottom branding and slide number."""
    footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(6.9), Inches(11.7), Inches(0.4))
    tf = footer_box.text_frame
    p = tf.paragraphs[0]
    p.text = f"Elysia Code Master Architecture Deck  •  Slide {current_slide} of {total_slides}  •  http://localhost:8080"
    p.font.size = Pt(9.5)
    p.font.color.rgb = RGBColor(100, 116, 139)


def build_presentation():
    prs = Presentation()
    prs.slide_width = SLIDE_WIDTH
    prs.slide_height = SLIDE_HEIGHT
    blank_layout = prs.slide_layouts[6]

    # =========================================================================
    # SLIDE 1: Title & Hero
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)

    # Hero Badge
    b1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.8), Inches(4.2), Inches(0.45))
    b1.fill.solid()
    b1.fill.fore_color.rgb = RGBColor(18, 36, 64)
    b1.line.color.rgb = COLOR_CYAN
    b1.text_frame.paragraphs[0].text = "🚀 MASTER ENGINEERING PRESENTATION"
    b1.text_frame.paragraphs[0].font.size = Pt(11)
    b1.text_frame.paragraphs[0].font.bold = True
    b1.text_frame.paragraphs[0].font.color.rgb = COLOR_CYAN
    b1.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER

    # Title & Tagline
    t_box = s1.shapes.add_textbox(Inches(0.8), Inches(1.4), Inches(11.7), Inches(2.2))
    tf = t_box.text_frame
    tf.word_wrap = True
    p1 = tf.paragraphs[0]
    p1.text = "ELYSIA CODE"
    p1.font.size = Pt(44)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_WHITE

    p2 = tf.add_paragraph()
    p2.text = "The Next-Generation Gamified Python Mastery & Zero-to-Advanced IDE Ecosystem"
    p2.font.size = Pt(18)
    p2.font.color.rgb = COLOR_CYAN
    p2.space_before = Pt(6)

    p3 = tf.add_paragraph()
    p3.text = "Engineered with habit psychology, sub-15ms execution, cognitive visual handbooks, and automated college lab manual generation."
    p3.font.size = Pt(13)
    p3.font.color.rgb = COLOR_MUTED
    p3.space_before = Pt(8)

    # 3 High Impact Callout Cards
    add_card(s1, Inches(0.8), Inches(3.9), Inches(3.64), Inches(2.5),
             "Addictive Pedagogy",
             "Re-engineering coding education using YouTube/Instagram habit psychology, loss-aversion daily streaks, dopamine confetti physics, and senior mentorship.",
             "🧠", COLOR_CYAN)

    add_card(s1, Inches(4.84), Inches(3.9), Inches(3.64), Inches(2.5),
             "Split-Screen Live IDE",
             "Sub-15ms local execution engine, interactive stdin input bar for input(), client-side Pyodide WebAssembly fallback, and VS Code-grade keybindings.",
             "⚡", COLOR_PURPLE)

    add_card(s1, Inches(8.88), Inches(3.9), Inches(3.64), Inches(2.5),
             "1-Click Lab Exporter",
             "Industry-first automated college practical file generator producing academic A4 print-ready manuals with Aim, Algorithm, Code, Output, and Viva Q&A.",
             "📄", COLOR_GREEN)

    add_footer(s1, 1)

    # =========================================================================
    # SLIDE 2: Problem Statement
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header(s2, "The Core Problem", "Why 90% of Coding Beginners Drop Out",
               "Traditional computer science education treats beginners like compilers, ignoring cognitive science, human psychology, and fear of failure.", COLOR_ROSE)

    cards_data_s2 = [
        ("Cognitive Friction", "Complex environment setups (PATH errors, IDE crashes, package conflicts) exhaust student motivation before writing their first line.", "🛑", COLOR_ROSE),
        ("Boring Wall of Text", "500-page dry PDF textbooks full of academic jargon. Zero real-world mechanical models, interactive discovery, or street analogies.", "📖", COLOR_AMBER),
        ("Cryptic Tracebacks", "Scary red terminal tracebacks (TypeError, IndexError) terrify junior students without explaining why the mistake occurred in plain language.", "💀", COLOR_PURPLE),
        ("No Habit Engineering", "Zero positive reinforcement or accountability loops. Students lack the dopamine triggers needed to return day after day.", "📉", COLOR_CYAN)
    ]
    w = Inches(2.7)
    gap = Inches(0.3)
    for i, (title, desc, icon, border) in enumerate(cards_data_s2):
        add_card(s2, Inches(0.8) + i * (w + gap), Inches(2.5), w, Inches(4.1), title, desc, icon, border)

    add_footer(s2, 2)

    # =========================================================================
    # SLIDE 3: The Elysia Philosophy & Habit Engineering
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_header(s3, "Educational Philosophy", "Habit Engineering & Psychological Hooks",
               "Applying modern neurological retention mechanics (TikTok, Instagram, Duolingo) to turn programming into a daily addictive ritual.", COLOR_PURPLE)

    add_card(s3, Inches(0.8), Inches(2.5), Inches(3.64), Inches(4.1),
             "Ego-Driven Rank Ladder",
             "Nobody wants to remain a beginner. Elysia playfully provokes the user's ego to climb through 5 distinct developer ranks:\n\n"
             "• Level 1: NOOB (🐣)\n• Level 2: KEYBOARD TOURIST (💻)\n• Level 3: SYNTAX WARRIOR (⚔️)\n• Level 4: PYTHON SLAYER (🐍)\n• Level 5: GRANDMASTER (👑)\n\n"
             "Each tier unlocks new badges, status titles, and flex privileges.", "👑", COLOR_PURPLE)

    add_card(s3, Inches(4.84), Inches(2.5), Inches(3.64), Inches(4.1),
             "Streak Loss Aversion",
             "Daily Streak Engine tracking continuous days of coding.\n\n"
             "• Behavioral Economics: People fear losing existing progress 2x more than gaining new rewards.\n"
             "• Glowing navbar flame icon acts as a constant visual commitment device.\n"
             "• Skips reset the streak, motivating students to write at least one line of code every 24 hours.", "🔥", COLOR_CYAN)

    add_card(s3, Inches(8.88), Inches(2.5), Inches(3.64), Inches(4.1),
             "Dopamine Particle Physics",
             "Instant neurological gratification upon code submission:\n\n"
             "• 90-particle canvas confetti explosion with realistic gravity and rotation physics.\n"
             "• Web Audio API synthesized fanfare chords (no external sound files required).\n"
             "• Immediate +50 XP reward pop-up and Senior Bhaiya victory congratulations.", "🎉", COLOR_AMBER)

    add_footer(s3, 3)

    # =========================================================================
    # SLIDE 4: Curriculum Architecture (7 Units & 19 Subtopics)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_header(s4, "Academic Curriculum", "19 Granular Subtopics: Zero to Advanced",
               "Structured step-by-step so that even a junior school student with zero computer background can master Python architecture.", COLOR_CYAN)

    units_top = [
        ("Unit 1: Foundations", "Python genesis, variables, memory boxes, data types, type casting, print(), input(), f-strings.", "📦", COLOR_CYAN),
        ("Unit 2: Logic & Decisions", "Comparison operators, if-elif-else roadblocks, logical and/or/not, nested conditional checks.", "🚥", COLOR_PURPLE),
        ("Unit 3: Loops & Iteration", "while loops, counters, for loops with range(), loop control (break & continue), nested patterns.", "🎡", COLOR_GREEN),
        ("Unit 4: Data Collections", "Lists, indexing & slicing, tuples (immutable locks), dictionaries (key-value), sets & hashing.", "🗄️", COLOR_AMBER)
    ]
    w4 = Inches(2.7)
    gap4 = Inches(0.3)
    for i, (title, desc, icon, border) in enumerate(units_top):
        add_card(s4, Inches(0.8) + i * (w4 + gap4), Inches(2.5), w4, Inches(2.0), title, desc, icon, border)

    units_bottom = [
        ("Unit 5: Modular Functions", "def keyword, parameters, return values, default arguments, and local vs global scoping.", "🧩", COLOR_CYAN),
        ("Unit 6: Object-Oriented OOP", "Classes, blueprints, __init__ constructor, self pointer, inheritance, and encapsulation.", "🏛️", COLOR_PURPLE),
        ("Unit 7: Bulletproof Exceptions", "try-except-finally blocks, error catching, clean file reading and writing operations.", "🛡️", COLOR_ROSE)
    ]
    w3 = Inches(3.64)
    gap3 = Inches(0.38)
    for i, (title, desc, icon, border) in enumerate(units_bottom):
        add_card(s4, Inches(0.8) + i * (w3 + gap3), Inches(4.75), w3, Inches(1.85), title, desc, icon, border)

    add_footer(s4, 4)

    # =========================================================================
    # SLIDE 5: Anatomy of a Subtopic
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5)
    add_header(s5, "Micro-Pedagogy", "Anatomy of Every Subtopic Mastery Card",
               "Every subtopic follows a standardized 7-step pedagogical structure to guarantee clarity, comprehension, and muscle memory.", COLOR_GREEN)

    add_card(s5, Inches(0.8), Inches(2.5), Inches(5.66), Inches(4.1),
             "Conceptual Foundation & Rules",
             "1. Dual-Language Theory & Metaphor:\n"
             "   Bilingual explanation (English & Hinglish) paired with mechanical real-world analogies (e.g. Variables as labeled lunchboxes).\n\n"
             "2. Golden Syntax Rule (Kanoon):\n"
             "   Explicit rules on why the syntax exists, proper punctuation (colons, quotes), and what happens if broken.\n\n"
             "3. Two Ready-to-Try Examples:\n"
             "   1-click 'Try Example 1' and 'Try Example 2' buttons auto-populate the IDE for immediate zero-friction experimentation.",
             "📚", COLOR_CYAN)

    add_card(s5, Inches(6.86), Inches(2.5), Inches(5.66), Inches(4.1),
             "Active Practice & Verification",
             "4. Hands-On Challenge:\n"
             "   Specific coding problem with strict Expected Output test cases to verify true mastery.\n\n"
             "5. Senior Bhaiya Cheer & Ego Reward:\n"
             "   Humorous street-smart encouragement (e.g. 'Maan gaye Ustaad! Ab loops tumhare aage hath jodenge!').\n\n"
             "6. Hidden Solution & Hint Accordion:\n"
             "   Prevents dropout panic by allowing stuck students to reveal hints and drop-in solutions with 1-click clipboard copy.",
             "🎯", COLOR_PURPLE)

    add_footer(s5, 5)

    # =========================================================================
    # SLIDE 6: Split-Screen Live IDE Architecture
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6)
    add_header(s6, "Engineering Excellence", "Split-Screen Interactive IDE Architecture",
               "Zero window switching. Theory sits on the left; high-speed execution sandbox sits on the right.", COLOR_CYAN)

    add_card(s6, Inches(0.8), Inches(2.5), Inches(3.64), Inches(2.5),
             "Sub-15ms Execution",
             "Native Python 3 execution worker via subprocess with 3.0s threshold timeout protection preventing infinite loop crashes.",
             "⚡", COLOR_CYAN)

    add_card(s6, Inches(4.84), Inches(2.5), Inches(3.64), Inches(2.5),
             "Dynamic Stdin Input Bar",
             "Interactive terminal input bar supporting input() and int(input()) dynamically without socket deadlocks or browser hangs.",
             "⌨️", COLOR_GREEN)

    add_card(s6, Inches(8.88), Inches(2.5), Inches(3.64), Inches(2.5),
             "Pyodide WASM Fallback",
             "Client-side CPython compiled to WebAssembly running directly inside the browser for true 100% offline functionality.",
             "🌐", COLOR_PURPLE)

    add_card(s6, Inches(0.8), Inches(5.2), Inches(11.7), Inches(1.4),
             "VS Code-Grade Keyboard Shortcuts & Controls",
             "• Tab Key Indentation: Inserts 4 true spaces instead of losing browser focus  |  • Ctrl+Enter / Cmd+Enter: Instant Code Run\n"
             "• Auto-Closing Brackets & Quotes: (), [], {}, '', \"\"  |  • Live Caret Tracker: Ln X, Col Y  |  • 1-Click .py Script Exporter",
             "🛠️", COLOR_AMBER)

    add_footer(s6, 6)

    # =========================================================================
    # SLIDE 7: The Visual Handbook
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7)
    add_header(s7, "Visual Cognition", "The Visual Handbook: Mental Models & Analogies",
               "8 multimedia chapters transforming abstract programming syntax into intuitive mechanical physical models.", COLOR_CYAN)

    handbook_cards = [
        ("Ch 1: Python Superpower", "Why Python syntax reads like human English compared to C++ and Java boilerplate.", "🚀", COLOR_CYAN),
        ("Ch 2: Memory Boxes", "Variables as physical warehouse storage boxes with data type labels and addresses.", "📦", COLOR_PURPLE),
        ("Ch 4: Traffic Signals", "Control flow and if-elif-else logic visualized as railroad tracks and track switches.", "🚥", COLOR_GREEN),
        ("Ch 5: Ferris Wheels", "Loops visualized as rotating carnival wheels with safety break switches and step counters.", "🎡", COLOR_AMBER)
    ]
    for i, (title, desc, icon, border) in enumerate(handbook_cards):
        add_card(s7, Inches(0.8) + i * (w4 + gap4), Inches(2.5), w4, Inches(2.6), title, desc, icon, border)

    add_card(s7, Inches(0.8), Inches(5.35), Inches(11.7), Inches(1.25),
             "1-Click Sandbox Transfer & Slide Carousel",
             "Every slide features an interactive slide carousel with keyboard arrows, progress dots, and a 'Send to Sandbox' button that loads the concept code directly into the IDE editor with 1 click.",
             "✨", COLOR_CYAN)

    add_footer(s7, 7)

    # =========================================================================
    # SLIDE 8: Socratic Senior AI & 60s Doubt Buster
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8)
    add_header(s8, "Intelligent Mentorship", "Socratic Senior AI & 60s Doubt Buster",
               "Elysia acts like a street-smart college senior bhaiya who explains the 'why' behind errors instead of spoon-feeding code.", COLOR_AMBER)

    add_card(s8, Inches(0.8), Inches(2.5), Inches(5.66), Inches(4.1),
             "Cryptic Traceback Decoder",
             "Translates terrifying Python terminal tracebacks into humorous Indian street analogies:\n\n"
             "• TypeError (str + int):\n"
             "  'Bhai! String aur Number ko + se jodne ki koshish kar rahe ho? Ye waisa hi hai jaise Fevicol se Samosa chipkana! str() lagao ya f-string use karo!'\n\n"
             "• IndexError (list out of range):\n"
             "  'List me 3 samose hain aur tum 5th mang rahe ho! Python me counting 0 se shuru hoti hai!'",
             "🕵️‍♂️", COLOR_AMBER)

    add_card(s8, Inches(6.86), Inches(2.5), Inches(5.66), Inches(4.1),
             "60-Second Instant Doubt Buster",
             "High-speed indexed instant search across all 19 subtopics and question bank for emergency pre-exam revision:\n\n"
             "• Type 'input': Instant rule on why input() returns strings and how int(input()) type-casts.\n\n"
             "• Type 'slice': Visual slice formula [start:stop:step] explained with index numbers.\n\n"
             "• Type 'colon': Explains indentation hierarchy and loop syntax rules.",
             "🔍", COLOR_CYAN)

    add_footer(s8, 8)

    # =========================================================================
    # SLIDE 9: Dynamic Question Bank & Mock Exam
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9)
    add_header(s9, "Assessment Engine", "Question Bank & Semester Mock Exam Mode",
               "Transforming pre-exam anxiety into mastery through filterable question banks and realistic timed examination simulations.", COLOR_PURPLE)

    add_card(s9, Inches(0.8), Inches(2.5), Inches(5.66), Inches(4.1),
             "Dynamic Multi-Filter Question Bank",
             "Students can customize targeted practice tests across 4 dimensions:\n\n"
             "• Subject Filter: Python vs HTML/CSS\n"
             "• Topic Selector: All 19 Subtopics individually selectable\n"
             "• Difficulty Levels: Easy, Medium, Hard\n"
             "• Question Batching: 5, 10, or 20 questions at a time\n\n"
             "Includes expandable glowing Amber Senior Hints that provide guidance without spoiling answers.",
             "🎯", COLOR_PURPLE)

    add_card(s9, Inches(6.86), Inches(2.5), Inches(5.66), Inches(4.1),
             "25-Minute Timed Mock Exam",
             "Simulates university terminal semester practical and written exams:\n\n"
             "• Section A: Conceptual MCQs & Syntax Traps\n"
             "• Section B: Bug Squashing & Code Debugging\n"
             "• Section C: Logic Building & Algorithm Writing\n"
             "• Section D: Rapid-Fire Viva Voce Preparation\n\n"
             "Features automated grading, percentage scoring, and detailed answer explanations.",
             "⏱️", COLOR_CYAN)

    add_footer(s9, 9)

    # =========================================================================
    # SLIDE 10: 1-Click College Lab Practical Exporter
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10)
    add_header(s10, "Industry First Innovation", "1-Click Printable College Lab Practical File",
               "Eliminating the #1 frustration of engineering and computer students: spending hours formatting manual laboratory practical files.", COLOR_GREEN)

    add_card(s10, Inches(0.8), Inches(2.5), Inches(3.64), Inches(3.0),
             "University Header",
             "Auto-populates Student Name, Roll Number, Subject Code (e.g. CSE101), Date, and Experiment Index following standard academic university guidelines.",
             "🎓", COLOR_GREEN)

    add_card(s10, Inches(4.84), Inches(2.5), Inches(3.64), Inches(3.0),
             "Algorithm & Code",
             "Generates step-by-step numbered pseudo-algorithm, formatted syntax-highlighted Python code, and realistic sample terminal execution output.",
             "📐", COLOR_CYAN)

    add_card(s10, Inches(8.88), Inches(2.5), Inches(3.64), Inches(3.0),
             "Oral Viva Prep",
             "Automatically attaches the professor's top viva examination questions and model answers corresponding directly to the experiment topic.",
             "🗣️", COLOR_PURPLE)

    add_card(s10, Inches(0.8), Inches(5.75), Inches(11.7), Inches(0.9),
             "Zero Word Processing Needed",
             "Click 'Generate' ➔ Instant window.print() opens ➔ Save directly as standard A4 PDF or print on physical sheets!",
             "🖨️", COLOR_GREEN)

    add_footer(s10, 10)

    # =========================================================================
    # SLIDE 11: Security & Authentication System
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_background(s11)
    add_header(s11, "Security & Architecture", "Pure Python Auth & Profile Picture System",
               "Zero external database dependencies. Built entirely using standard Python cryptographic security libraries.", COLOR_CYAN)

    add_card(s11, Inches(0.8), Inches(2.5), Inches(3.64), Inches(2.6),
             "SHA-256 + Salt Hashing",
             "Passwords are never stored in plain text. Securely salted with unique random cryptographic hex strings in data/users.json.",
             "🛡️", COLOR_CYAN)

    add_card(s11, Inches(4.84), Inches(2.5), Inches(3.64), Inches(2.6),
             "Profile Picture Engine",
             "Upload custom device photos (Base64 file stream) or choose from 8 developer avatars with glowing preview circles.",
             "📸", COLOR_PURPLE)

    add_card(s11, Inches(8.88), Inches(2.5), Inches(3.64), Inches(2.6),
             "Multi-User Isolation",
             "Each user account maintains separate XP, daily streak, completed subtopic checklists, and study stopwatch times.",
             "🔄", COLOR_GREEN)

    add_card(s11, Inches(0.8), Inches(5.35), Inches(11.7), Inches(1.25),
             "Dynamic Navbar Capsule & Profile Management",
             "• Logged Out: Glowing '✨ Sign In / Log In' button  |  • Logged In: Coder capsule with circular avatar photo, name, and rank tag\n"
             "• Edit Profile Modal: Update display name, developer motto, or photo anytime  |  • Safe 1-Click Logout",
             "👤", COLOR_AMBER)

    add_footer(s11, 11)

    # =========================================================================
    # SLIDE 12: Gamification & Social 3D Flex Card
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_background(s12)
    add_header(s12, "Viral Growth Mechanics", "Gamification & 3D Holographic Flex Card",
               "Designed to tap into peer motivation by making coding achievements instantly shareable on social networks.", COLOR_PURPLE)

    add_card(s12, Inches(0.8), Inches(2.5), Inches(5.66), Inches(4.1),
             "3D Holographic Parallax Card",
             "Spatial computing perspective physics that dynamically tilts and highlights based on cursor movement:\n\n"
             "• Displays User Avatar Photo & Real Name\n"
             "• Active Ego Rank Title (e.g. PYTHON SLAYER)\n"
             "• Total Subtopics Mastered Fraction & Daily Streak\n"
             "• Formatted for instant 1-click sharing on Instagram Stories, WhatsApp Status, and LinkedIn.",
             "🎴", COLOR_PURPLE)

    add_card(s12, Inches(6.86), Inches(2.5), Inches(5.66), Inches(4.1),
             "Live Productivity Stopwatch",
             "Real-time tick-by-tick time counter tracking active study duration:\n\n"
             "• Time Spent Today: Measures daily focus blocks (HH:MM:SS)\n"
             "• All-Time Learning Time: Accumulates total hours invested in Python\n"
             "• Automatic Persistence: Saves every 5 seconds and syncs to user profile and flex card.",
             "⏱️", COLOR_CYAN)

    add_footer(s12, 12)

    # =========================================================================
    # SLIDE 13: System Architecture & Tech Stack
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    set_slide_background(s13)
    add_header(s13, "Technical Blueprint", "Zero-Bloat System Architecture",
               "High performance, zero heavy pip frameworks, and sub-15ms response times across all endpoints.", COLOR_CYAN)

    add_card(s13, Inches(0.8), Inches(2.5), Inches(3.64), Inches(4.1),
             "Frontend Architecture",
             "• Semantic HTML5 & CSS3 Glassmorphism\n"
             "• Vanilla ES6+ Class Controller (app.js)\n"
             "• Pyodide WebAssembly Client Sandbox\n"
             "• Web Audio API Synthesizer (audio.js)\n"
             "• Canvas Confetti Physics Engine\n"
             "• Responsive Desktop & Tablet Layouts",
             "🖥️", COLOR_CYAN)

    add_card(s13, Inches(4.84), Inches(2.5), Inches(3.64), Inches(4.1),
             "Backend Engine",
             "• Standard Python 3 http.server\n"
             "• Non-blocking Threaded Request Handler\n"
             "• Subprocess Execution Sandbox\n"
             "• SHA-256 + Salt Cryptographic Auth\n"
             "• Atomic JSON Data Store (data/)\n"
             "• Zero SQL Database Dependencies",
             "⚙️", COLOR_PURPLE)

    add_card(s13, Inches(8.88), Inches(2.5), Inches(3.64), Inches(4.1),
             "Reliability & Benchmarks",
             "• 9/9 Automated Unit Tests (tests/)\n"
             "• Test Execution Speed: 0.034 seconds\n"
             "• Local Code Execution: <15 milliseconds\n"
             "• 100% Offline Capability via WASM\n"
             "• Cross-Platform: Mac, Windows, Linux\n"
             "• Zero External Pip Packages Needed",
             "🚀", COLOR_GREEN)

    add_footer(s13, 13)

    # =========================================================================
    # SLIDE 14: Future Roadmap & Conclusion
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    set_slide_background(s14)
    add_header(s14, "Vision & Roadmap", "The Future of Elysia Code & Conclusion",
               "Evolving from a standalone mastery platform into the world's most engaging computer science learning network.", COLOR_GREEN)

    add_card(s14, Inches(0.8), Inches(2.5), Inches(3.64), Inches(2.5),
             "Phase 2: 1v1 Code Duels",
             "Real-time WebSocket multiplayer battles where students race head-to-head to squash syntax errors and solve algorithms.",
             "⚔️", COLOR_CYAN)

    add_card(s14, Inches(4.84), Inches(2.5), Inches(3.64), Inches(2.5),
             "Phase 3: Web Dev & AI Tracks",
             "Expanding beyond Python to full interactive sandboxes for HTML/CSS/JavaScript, SQL queries, and beginner Machine Learning.",
             "🌐", COLOR_PURPLE)

    add_card(s14, Inches(8.88), Inches(2.5), Inches(3.64), Inches(2.5),
             "Phase 4: College Portal",
             "Professor dashboard for assigning weekly lab exercises, auto-evaluating submissions, and detecting batch-wide knowledge gaps.",
             "🏫", COLOR_GREEN)

    # Thank you banner
    thank_card = s14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.2), Inches(11.7), Inches(1.4))
    thank_card.fill.solid()
    thank_card.fill.fore_color.rgb = RGBColor(18, 36, 64)
    thank_card.line.color.rgb = COLOR_CYAN
    thank_card.line.width = Pt(1.5)

    tf_t = thank_card.text_frame
    tf_t.word_wrap = True
    p_t1 = tf_t.paragraphs[0]
    p_t1.text = "Thank You! Questions & Live Demonstration"
    p_t1.font.size = Pt(22)
    p_t1.font.bold = True
    p_t1.font.color.rgb = COLOR_WHITE
    p_t1.alignment = PP_ALIGN.CENTER

    p_t2 = tf_t.add_paragraph()
    p_t2.text = "Platform Running Live at: http://localhost:8080  •  Presentation Deck: http://localhost:8080/presentation.html"
    p_t2.font.size = Pt(12)
    p_t2.font.color.rgb = COLOR_CYAN
    p_t2.alignment = PP_ALIGN.CENTER
    p_t2.space_before = Pt(4)

    add_footer(s14, 14)

    # Save outputs
    output_path = Path("/Users/priyanshuyadav/.gemini/antigravity/scratch/elysia-code/Elysia_Code_Master_Presentation.pptx")
    prs.save(str(output_path))
    print(f"✅ Master Presentation saved successfully at: {output_path}")

    # Also copy to Desktop
    desktop_path = Path("/Users/priyanshuyadav/Desktop/Elysia_Code_Master_Presentation.pptx")
    prs.save(str(desktop_path))
    print(f"✅ Desktop Presentation saved successfully at: {desktop_path}")


if __name__ == "__main__":
    build_presentation()
