#!/usr/bin/env python3
"""
Build & verify the 50 Functions & Recursion (FR-01 to FR-50) questions.
Generates data/fr50_questions_verified.json and merges into data/questions.json and data/elysia.db.
"""

import io
import json
import sqlite3
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from scripts.fr50_definitions import FR50_QUESTIONS_RAW

QUESTIONS_JSON = BASE_DIR / "data" / "questions.json"
FR50_VERIFIED_JSON = BASE_DIR / "data" / "fr50_questions_verified.json"
DB_PATH = BASE_DIR / "data" / "elysia.db"


def verify_solution(q_num: int, sol_code: str, sample_in: str, exp_out: str) -> None:
    """Executes solution code with sample_input on stdin and checks stdout."""
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin = io.StringIO(sample_in)
    sys.stdout = io.StringIO()
    try:
        exec(sol_code, {})
        actual = sys.stdout.getvalue().strip()
        if actual != exp_out.strip():
            raise AssertionError(
                f"FR-{q_num:02d} output mismatch!\nExpected:\n{exp_out.strip()!r}\nGot:\n{actual!r}"
            )
    finally:
        sys.stdin, sys.stdout = old_stdin, old_stdout


def build_fr50_catalog() -> None:
    print(f"Building Functions & Recursion catalog from {len(FR50_QUESTIONS_RAW)} definitions...")
    formatted_questions = []

    for q in FR50_QUESTIONS_RAW:
        q_num = q["q_num"]
        verify_solution(q_num, q["solution_code"], q["sample_input"], q["expected_output"])

        qid = f"py_fr_{q_num:03d}"
        title = f"[FR-{q_num:02d}] {q['title']}"
        sample_in_display = q["sample_input"] if q["sample_input"] else "(no input needed)"

        desc_en = f"""### 📚 {q['level']} — *{q['subtopic']}*

### 📖 Scenario
{q['scenario']}

### 🎯 Task
{q['task']}

### 📥 Sample Input
```text
{sample_in_display}
```

### 📤 Expected Output
```text
{q['expected_output']}
```"""

        desc_hi = f"""### 📚 {q['level']} — *{q['subtopic']}*

### 📖 Scenario (Real-Life Problem)
{q['scenario']}

### 🎯 Task (Aapko kya karna hai)
{q['task']}

### 📥 Sample Input
```text
{sample_in_display}
```

### 📤 Expected Output (Ye result aana chahiye)
```text
{q['expected_output']}
```"""

        item = {
            "id": qid,
            "subject": "python",
            "topic": "py_func_recursion",
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
            "category": f"Functions & Recursion - {q['level']}",
            "is_scenario": True,
            "tag": "🔁 Functions & Recursion"
        }
        formatted_questions.append(item)

    print(f"✅ All {len(formatted_questions)}/{len(FR50_QUESTIONS_RAW)} solutions passed verification!")

    with open(FR50_VERIFIED_JSON, "w", encoding="utf-8") as f:
        json.dump(formatted_questions, f, indent=2, ensure_ascii=False)
    print(f"✅ Saved verified catalog to {FR50_VERIFIED_JSON.name}")

    # Merge into data/questions.json
    with open(QUESTIONS_JSON, "r", encoding="utf-8") as f:
        master_qs = json.load(f)

    master_qs = [q for q in master_qs if not q.get("id", "").startswith("py_fr_")]
    master_qs.extend(formatted_questions)

    with open(QUESTIONS_JSON, "w", encoding="utf-8") as f:
        json.dump(master_qs, f, indent=2, ensure_ascii=False)
    print(f"✅ Master questions.json updated: Total {len(master_qs)} questions")

    # Sync into SQLite elysia.db
    if DB_PATH.is_file():
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='questions'")
        if cur.fetchone():
            cur.execute("PRAGMA table_info(questions)")
            existing_cols = [c[1] for c in cur.fetchall()]
            has_sample = "sample_input" in existing_cols
            has_scenario = "is_scenario" in existing_cols

            cur.execute("DELETE FROM questions WHERE id LIKE 'py_fr_%'")
            for q in formatted_questions:
                if has_sample and has_scenario:
                    cur.execute("""
                        INSERT INTO questions (
                            id, subject, topic, difficulty, xp,
                            title_en, title_hi, desc_en, desc_hi,
                            starter_code, solution_code, expected_output,
                            hint_en, hint_hi, sample_input, is_scenario
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        q["id"], q["subject"], q["topic"], q["difficulty"], q["xp"],
                        q["title_en"], q["title_hi"], q["desc_en"], q["desc_hi"],
                        q["starter_code"], q["solution_code"], q["expected_output"],
                        q["hint_en"], q["hint_hi"], q["sample_input"], 1
                    ))
                else:
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
            print(f"✅ Synced {len(formatted_questions)} FR questions into SQLite {DB_PATH.name}")
        conn.close()


if __name__ == "__main__":
    build_fr50_catalog()
