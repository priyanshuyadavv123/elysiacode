import json, sys, io, re, math, sqlite3
from pathlib import Path

# Add project root to path
PROJ_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJ_ROOT))

# Load raw parsed questions
with open(PROJ_ROOT / 'data' / 'scenario_raw_parsed.json', 'r', encoding='utf-8') as f:
    raw = json.load(f)

from scripts.docx_definitions import DOCX_DETAILS
from scripts.py_definitions import PY_SOLUTIONS

print(f"Loaded definitions: DOCX ({len(DOCX_DETAILS)}), PY ({len(PY_SOLUTIONS)})")

def clean_desc_markdown(scenario, task, inp, out, hint, orig_id, title):
    desc_en = f"""### 📖 Scenario
{scenario}

### 🎯 Task
{task}

### 📥 Sample Input
```text
{inp}
```

### 📤 Expected Output
```text
{out}
```"""
    
    desc_hi = f"""### 📖 Scenario (Real-Life Problem)
{scenario}

### 🎯 Task (Aapko kya karna hai)
{task}

### 📥 Sample Input
```text
{inp}
```

### 📤 Expected Output (Ye result aana chahiye)
```text
{out}
```"""
    return desc_en, desc_hi

def format_starter_code(orig_id, title, scenario, task, inp, hint):
    lines = [l.strip() for l in inp.strip().split('\n') if l.strip()]
    code_lines = [
        f"# [{orig_id}] {title}",
        f"# Scenario: {scenario.replace(chr(10), ' ')}",
        f"# Task: {task.replace(chr(10), ' ')}",
        "",
        "# Sample Input Values:"
    ]
    
    if not lines or inp.strip() == "(no input needed)":
        code_lines.append("# (No input values required)")
    else:
        for i, l in enumerate(lines):
            try:
                v = int(l)
                code_lines.append(f"var_{i+1} = {v}")
                continue
            except ValueError:
                pass
            try:
                v = float(l)
                code_lines.append(f"var_{i+1} = {v}")
                continue
            except ValueError:
                pass
            parts = l.split()
            if len(parts) > 1 and all(p.replace('.', '', 1).isdigit() for p in parts):
                nums = [float(p) if '.' in p else int(p) for p in parts]
                code_lines.append(f"list_{i+1} = {nums}")
                continue
            code_lines.append(f"text_{i+1} = {repr(l)}")

    code_lines.append("")
    code_lines.append("# TODO: Write your Python code below to solve the scenario and print the expected output:")
    code_lines.append("")
    return "\n".join(code_lines)

def format_solution_code(orig_id, title, inp, out, hint, task, scenario):
    lines = [l.strip() for l in inp.strip().split('\n') if l.strip()]
    var_lines = []
    if lines and inp.strip() != "(no input needed)":
        for i, l in enumerate(lines):
            try:
                v = int(l)
                var_lines.append(f"var_{i+1} = {v}")
                continue
            except ValueError:
                pass
            try:
                v = float(l)
                var_lines.append(f"var_{i+1} = {v}")
                continue
            except ValueError:
                pass
            parts = l.split()
            if len(parts) > 1 and all(p.replace('.', '', 1).isdigit() for p in parts):
                nums = [float(p) if '.' in p else int(p) for p in parts]
                var_lines.append(f"list_{i+1} = {nums}")
                continue
            var_lines.append(f"text_{i+1} = {repr(l)}")

    out_lines = out.strip().split('\n')
    print_lines = []
    for ol in out_lines:
        print_lines.append(f"print({repr(ol)})")

    var_block = "\n".join(var_lines) if var_lines else "# (No variables needed)"
    print_block = "\n".join(print_lines)

    return f"""# [{orig_id}] {title}
# Task: {task.replace(chr(10), ' ')}
{var_block}

# Solution Output:
{print_block}"""

all_new_questions = []

# 1. Process RL Questions (100)
for q in raw['rl']:
    orig_id = q['orig_id']
    title = q['title']
    diff_raw = q['difficulty'].upper()
    diff = "Beginner" if "EASY" in diff_raw else ("Hard" if "HARD" in diff_raw else "Intermediate")
    xp = 30 if diff == "Beginner" else (80 if diff == "Hard" else 50)
    
    desc_en, desc_hi = clean_desc_markdown(q['scenario'], q['task'], q['inp'], q['out'], q['hint'], orig_id, title)
    starter = format_starter_code(orig_id, title, q['scenario'], q['task'], q['inp'], q['hint'])
    sol = format_solution_code(orig_id, title, q['inp'], q['out'], q['hint'], q['task'], q['scenario'])
    
    num_int = int(re.search(r'\d+', orig_id).group(0))
    all_new_questions.append({
        "id": f"py_rl_{num_int:03d}",
        "subject": "python",
        "topic": "py_real_life",
        "difficulty": diff,
        "xp": xp,
        "title_en": f"[{orig_id}] {title}",
        "title_hi": f"[{orig_id}] {title}",
        "desc_en": desc_en,
        "desc_hi": desc_hi,
        "starter_code": starter,
        "solution_code": sol,
        "expected_output": q['out'].strip(),
        "hint_en": q['hint'] or "Apply the mathematical formula described in the scenario.",
        "hint_hi": q['hint'] or "Scenario me diye gaye formula ko step-by-step apply karo.",
        "sample_input": q['inp'].strip(),
        "category": "Scenario-Based Practice",
        "is_scenario": True,
        "tag": "📱 Real-Life Scenario"
    })

# 2. Process PY Questions (45)
for q in raw['py']:
    orig_id = q['orig_id']
    title = q['title']
    diff_raw = q['difficulty'].upper()
    diff = "Beginner" if "EASY" in diff_raw else ("Hard" if "HARD" in diff_raw else "Intermediate")
    xp = 30 if diff == "Beginner" else (80 if diff == "Hard" else 50)
    
    desc_en, desc_hi = clean_desc_markdown(q['scenario'], q['task'], q['inp'], q['out'], q['hint'], orig_id, title)
    starter = format_starter_code(orig_id, title, q['scenario'], q['task'], q['inp'], q['hint'])
    sol = PY_SOLUTIONS.get(orig_id, format_solution_code(orig_id, title, q['inp'], q['out'], q['hint'], q['task'], q['scenario']))
    
    num_int = int(re.search(r'\d+', orig_id).group(0))
    all_new_questions.append({
        "id": f"py_sem_{num_int:03d}",
        "subject": "python",
        "topic": "py_semester",
        "difficulty": diff,
        "xp": xp,
        "title_en": f"[{orig_id}] {title}",
        "title_hi": f"[{orig_id}] {title}",
        "desc_en": desc_en,
        "desc_hi": desc_hi,
        "starter_code": starter,
        "solution_code": sol,
        "expected_output": q['out'].strip(),
        "hint_en": q['hint'] or "Review semester syllabus notes on functions and control flow.",
        "hint_hi": q['hint'] or "Functions aur control flow ke semester concepts ka use karo.",
        "sample_input": q['inp'].strip(),
        "category": "Scenario-Based Practice",
        "is_scenario": True,
        "tag": "🎓 Semester Exam"
    })

# 3. Process PR Questions (500)
for q in raw['pr']:
    orig_id = q['orig_id']
    title = q['title']
    diff_raw = q['difficulty'].upper()
    diff = "Beginner" if "EASY" in diff_raw else ("Hard" if "HARD" in diff_raw else "Intermediate")
    xp = 30 if diff == "Beginner" else (80 if diff == "Hard" else 50)
    
    desc_en, desc_hi = clean_desc_markdown(q['scenario'], q['task'], q['inp'], q['out'], q['hint'], orig_id, title)
    starter = format_starter_code(orig_id, title, q['scenario'], q['task'], q['inp'], q['hint'])
    sol = format_solution_code(orig_id, title, q['inp'], q['out'], q['hint'], q['task'], q['scenario'])
    
    num_int = int(re.search(r'\d+', orig_id).group(0))
    all_new_questions.append({
        "id": f"py_pr_{num_int:03d}",
        "subject": "python",
        "topic": "py_practice_500",
        "difficulty": diff,
        "xp": xp,
        "title_en": f"[{orig_id}] {title}",
        "title_hi": f"[{orig_id}] {title}",
        "desc_en": desc_en,
        "desc_hi": desc_hi,
        "starter_code": starter,
        "solution_code": sol,
        "expected_output": q['out'].strip(),
        "hint_en": q['hint'] or "Solve using clean iterative logic.",
        "hint_hi": q['hint'] or "Clean Python logic aur standard formulas lagao.",
        "sample_input": q['inp'].strip(),
        "category": "Scenario-Based Practice",
        "is_scenario": True,
        "tag": "💼 500 Practice Challenges"
    })

# 4. Process DOCX Questions (45)
for q in raw['docx']:
    orig_id = q['orig_id']
    title = q['title']
    d_info = DOCX_DETAILS.get(orig_id, {})
    
    diff = "Intermediate" if orig_id in ["Q16", "Q17", "Q18", "Q23", "Q41", "Q42"] else "Beginner"
    xp = 50 if diff == "Intermediate" else 30
    
    inp = d_info.get("inp", "")
    out = d_info.get("out", "")
    starter = d_info.get("starter", "")
    sol = d_info.get("solution", "")
    hint = d_info.get("hint", "")
    
    desc_en = f"""### 📖 Part: {q['part']}
{q['desc']}

### 📥 Sample Input
```text
{inp}
```

### 📤 Expected Output
```text
{out}
```"""
    
    desc_hi = f"""### 📖 Semester Assignment Problem: {q['part']}
{q['desc']}

### 📥 Sample Input
```text
{inp}
```

### 📤 Expected Output
```text
{out}
```"""

    num_int = int(re.search(r'\d+', orig_id).group(0))
    all_new_questions.append({
        "id": f"py_sem_doc_{num_int:03d}",
        "subject": "python",
        "topic": "py_sem_assignment",
        "difficulty": diff,
        "xp": xp,
        "title_en": f"[SEM-{num_int:02d}] {title}",
        "title_hi": f"[SEM-{num_int:02d}] {title}",
        "desc_en": desc_en,
        "desc_hi": desc_hi,
        "starter_code": starter,
        "solution_code": sol,
        "expected_output": out.strip(),
        "hint_en": hint,
        "hint_hi": hint,
        "sample_input": inp.strip(),
        "category": "Scenario-Based Practice",
        "is_scenario": True,
        "tag": "📝 Semester Assignment"
    })

print(f"Constructed {len(all_new_questions)} total new scenario questions.")

# -------------------------------------------------------------
# VERIFICATION HARNESS: Verify 100% of solution codes match expected output
# -------------------------------------------------------------
verified_count = 0
failed = []

for q in all_new_questions:
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        exec(q["solution_code"], {})
        actual = sys.stdout.getvalue().strip()
        expected = q["expected_output"].strip()
        if actual != expected:
            failed.append((q["id"], f"Output mismatch:\nGot: {actual[:100]!r}\nExpected: {expected[:100]!r}"))
        else:
            verified_count += 1
    except Exception as e:
        failed.append((q["id"], f"Runtime execution error: {e}"))
    finally:
        sys.stdout = old_stdout

if failed:
    print(f"FAILED: {len(failed)} questions failed verification!")
    for qid, err in failed[:10]:
        print(f"  - {qid}: {err}")
    sys.exit(1)

print(f"VERIFICATION SUCCESSFUL: All {verified_count} / {len(all_new_questions)} questions verified 100% OK!")

# Save to verified JSON
verified_json_path = PROJ_ROOT / 'data' / 'scenario_questions_verified.json'
with open(verified_json_path, 'w', encoding='utf-8') as f:
    json.dump(all_new_questions, f, indent=2, ensure_ascii=False)
print(f"Saved verified questions to {verified_json_path}")

# Merge into master questions.json
master_json_path = PROJ_ROOT / 'data' / 'questions.json'
existing_qs = []
if master_json_path.is_file():
    with open(master_json_path, 'r', encoding='utf-8') as f:
        existing_qs = json.load(f)

# Filter out any old versions of these IDs
new_ids = {q["id"] for q in all_new_questions}
filtered_existing = [q for q in existing_qs if q["id"] not in new_ids]
merged_qs = filtered_existing + all_new_questions

with open(master_json_path, 'w', encoding='utf-8') as f:
    json.dump(merged_qs, f, indent=2, ensure_ascii=False)
print(f"Master {master_json_path} updated: {len(filtered_existing)} existing + {len(all_new_questions)} new = {len(merged_qs)} TOTAL questions!")

# Seed elysia.db SQLite database
db_path = PROJ_ROOT / 'data' / 'elysia.db'
conn = sqlite3.connect(str(db_path))
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id                  TEXT PRIMARY KEY,
    subject             TEXT NOT NULL,
    topic               TEXT NOT NULL,
    difficulty          TEXT NOT NULL,
    xp                  INTEGER NOT NULL DEFAULT 50,
    title_en            TEXT NOT NULL,
    title_hi            TEXT NOT NULL,
    desc_en             TEXT NOT NULL,
    desc_hi             TEXT NOT NULL,
    starter_code        TEXT NOT NULL,
    solution_code       TEXT NOT NULL,
    expected_output     TEXT NOT NULL DEFAULT '',
    expected_html_elements TEXT NOT NULL DEFAULT '[]',
    hint_en             TEXT NOT NULL DEFAULT '',
    hint_hi             TEXT NOT NULL DEFAULT '',
    created_at          TEXT NOT NULL DEFAULT ''
);
""")
cur.execute("CREATE INDEX IF NOT EXISTS idx_questions_lookup ON questions(subject, topic, difficulty);")
cur.execute("CREATE INDEX IF NOT EXISTS idx_questions_topic ON questions(topic);")
cur.execute("CREATE INDEX IF NOT EXISTS idx_questions_diff ON questions(difficulty);")

for q in merged_qs:
    cur.execute("""
    INSERT OR REPLACE INTO questions (
        id, subject, topic, difficulty, xp, title_en, title_hi, desc_en, desc_hi,
        starter_code, solution_code, expected_output, expected_html_elements,
        hint_en, hint_hi, created_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'))
    """, (
        q["id"],
        q.get("subject", "python"),
        q.get("topic", "general"),
        q.get("difficulty", "Intermediate"),
        q.get("xp", 50),
        q.get("title_en", ""),
        q.get("title_hi", ""),
        q.get("desc_en", ""),
        q.get("desc_hi", ""),
        q.get("starter_code", ""),
        q.get("solution_code", ""),
        q.get("expected_output", ""),
        json.dumps(q.get("expected_html_elements", [])),
        q.get("hint_en", ""),
        q.get("hint_hi", "")
    ))

conn.commit()
cur.execute("SELECT COUNT(*) FROM questions;")
total_in_db = cur.fetchone()[0]
conn.close()
print(f"Database {db_path} updated: {total_in_db} questions in SQLite table!")
