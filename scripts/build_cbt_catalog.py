# scripts/build_cbt_catalog.py
# Re-brand the 50 practice questions as "CBT Questions" (Computer Based Test questions)
# Generates data/cbt_questions_verified.json, updates data/questions.json and data/elysia.db

import json
import sqlite3
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from scripts.p50_definitions import P50_QUESTIONS_RAW

QUESTIONS_JSON = BASE_DIR / "data" / "questions.json"
CBT_VERIFIED_JSON = BASE_DIR / "data" / "cbt_questions_verified.json"
DB_PATH = BASE_DIR / "data" / "elysia.db"

def build_cbt_catalog():
    print(f"Building CBT catalog from {len(P50_QUESTIONS_RAW)} definitions...")
    
    formatted_questions = []
    for q in P50_QUESTIONS_RAW:
        q_num = q["q_num"]
        qid = f"py_cbt_{q_num:03d}"
        title = f"[CBT-{q_num:03d}] {q['title']}"
        
        desc_en = f"""### 📖 Scenario
{q['scenario']}

### 🎯 Task
{q['task']}

### ⚙️ Constraints
`{q['constraints']}`

### 📥 Sample Input
```text
{q['sample_input']}
```

### 📤 Expected Output
```text
{q['expected_output']}
```"""

        desc_hi = f"""### 📖 Scenario (CBT Exam Question)
{q['scenario']}

### 🎯 Task (Aapko kya karna hai)
{q['task']}

### ⚙️ Constraints (Shartein)
`{q['constraints']}`

### 📥 Sample Input (Input Values)
```text
{q['sample_input']}
```

### 📤 Expected Output (Ye result aana chahiye)
```text
{q['expected_output']}
```"""

        # Update starter code title tag if present
        starter = q["starter_code"].replace(f"[P50-{q_num:03d}]", f"[CBT-{q_num:03d}]")

        item = {
            "id": qid,
            "subject": "python",
            "topic": "py_cbt",
            "difficulty": q["difficulty"],
            "xp": q["xp"],
            "title_en": title,
            "title_hi": title,
            "desc_en": desc_en,
            "desc_hi": desc_hi,
            "starter_code": starter,
            "solution_code": q["solution_code"],
            "expected_output": q["expected_output"],
            "hint_en": q["hint"],
            "hint_hi": q["hint"],
            "sample_input": q["sample_input"],
            "category": f"CBT Exam - {q['part']}",
            "is_scenario": True,
            "tag": "🖥️ CBT Question"
        }
        formatted_questions.append(item)

    # Save to cbt_questions_verified.json
    with open(CBT_VERIFIED_JSON, "w", encoding="utf-8") as f:
        json.dump(formatted_questions, f, indent=2, ensure_ascii=False)
    print(f"✅ Saved {len(formatted_questions)} questions to {CBT_VERIFIED_JSON.name}")

    # Merge into data/questions.json
    with open(QUESTIONS_JSON, "r", encoding="utf-8") as f:
        master_qs = json.load(f)

    # Remove any old py_p50_* questions so we don't duplicate
    master_qs = [q for q in master_qs if not q.get("id", "").startswith("py_p50_") and not q.get("id", "").startswith("py_cbt_")]

    # Append new CBT questions
    master_qs.extend(formatted_questions)

    with open(QUESTIONS_JSON, "w", encoding="utf-8") as f:
        json.dump(master_qs, f, indent=2, ensure_ascii=False)

    print(f"✅ Master questions.json updated: Total {len(master_qs)} questions (CBT questions saved as py_cbt_001 to py_cbt_050)")

    # Seed into SQLite elysia.db if present
    if DB_PATH.is_file():
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='questions'")
        if cur.fetchone():
            # Delete old py_p50_* and py_cbt_*
            cur.execute("DELETE FROM questions WHERE id LIKE 'py_p50_%' OR id LIKE 'py_cbt_%'")
            
            for q in formatted_questions:
                cur.execute("""
                    INSERT INTO questions (
                        id, subject, topic, difficulty, xp,
                        title_en, title_hi, desc_en, desc_hi,
                        starter_code, solution_code, expected_output,
                        hint_en, hint_hi
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    q["id"], q["subject"], q["topic"], q["difficulty"], q["xp"],
                    q["title_en"], q["title_hi"], q["desc_en"], q["desc_hi"],
                    q["starter_code"], q["solution_code"], q["expected_output"],
                    q["hint_en"], q["hint_hi"]
                ))
            conn.commit()
            print(f"✅ Synced {len(formatted_questions)} CBT questions into SQLite database {DB_PATH.name}")
        conn.close()

if __name__ == "__main__":
    build_cbt_catalog()
