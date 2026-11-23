# scripts/build_p50_catalog.py
# Ingest and merge all 50 practice questions into ElysiaCode

import json
import sqlite3
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from scripts.p50_definitions import P50_QUESTIONS_RAW
QUESTIONS_JSON = BASE_DIR / "data" / "questions.json"
P50_VERIFIED_JSON = BASE_DIR / "data" / "p50_questions_verified.json"
DB_PATH = BASE_DIR / "data" / "elysia.db"

def build_catalog():
    print(f"Building P50 catalog from {len(P50_QUESTIONS_RAW)} definitions...")
    
    formatted_questions = []
    for q in P50_QUESTIONS_RAW:
        q_num = q["q_num"]
        qid = f"py_p50_{q_num:03d}"
        title = f"[P50-{q_num:03d}] {q['title']}"
        
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

        desc_hi = f"""### 📖 Scenario (Real-Life Problem)
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

        item = {
            "id": qid,
            "subject": "python",
            "topic": "py_practice_50",
            "difficulty": q["difficulty"],
            "xp": q["xp"],
            "title_en": title,
            "title_hi": title,
            "desc_en": desc_en,
            "desc_hi": desc_hi,
            "starter_code": q["starter_code"],
            "solution_code": q["solution_code"],
            "expected_output": q["expected_output"],
            "hint_en": q["hint"],
            "hint_hi": q["hint"],
            "sample_input": q["sample_input"],
            "category": q["part"],
            "is_scenario": True,
            "tag": "🎯 Practice 50"
        }
        formatted_questions.append(item)

    # Save to p50_questions_verified.json
    with open(P50_VERIFIED_JSON, "w", encoding="utf-8") as f:
        json.dump(formatted_questions, f, indent=2, ensure_ascii=False)
    print(f"✅ Saved {len(formatted_questions)} questions to {P50_VERIFIED_JSON.name}")

    # Merge into data/questions.json
    with open(QUESTIONS_JSON, "r", encoding="utf-8") as f:
        master_qs = json.load(f)

    existing_ids = {x["id"] for x in master_qs}
    added_count = 0
    updated_count = 0

    # Map existing items
    id_to_idx = {x["id"]: idx for idx, x in enumerate(master_qs)}

    for q in formatted_questions:
        if q["id"] in id_to_idx:
            master_qs[id_to_idx[q["id"]]] = q
            updated_count += 1
        else:
            master_qs.append(q)
            added_count += 1

    with open(QUESTIONS_JSON, "w", encoding="utf-8") as f:
        json.dump(master_qs, f, indent=2, ensure_ascii=False)

    print(f"✅ Master questions.json updated: Total {len(master_qs)} questions (Added: {added_count}, Updated: {updated_count})")

    # Seed into SQLite elysia.db if present
    if DB_PATH.is_file():
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        
        # Check if table exists
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='questions'")
        if cur.fetchone():
            cur.execute("PRAGMA table_info(questions)")
            cols = [col[1] for col in cur.fetchall()]
            
            for q in formatted_questions:
                cur.execute("DELETE FROM questions WHERE id = ?", (q["id"],))
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
            print(f"✅ Synced {len(formatted_questions)} questions into SQLite database {DB_PATH.name}")
        conn.close()

if __name__ == "__main__":
    build_catalog()
