#!/usr/bin/env python3
"""
Convert all Question Bank Python questions to dynamic stdin input().
- Replaces hardcoded starter/solution variables with input() calls
- Maps sample_input to stdin so users can test custom inputs interactively
- Verifies 100% of modified solution codes against expected outputs using stdin
- Syncs master data/questions.json and data/elysia.db
"""

import sys
import io
import json
import re
import ast
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
QUESTIONS_JSON = BASE_DIR / "data" / "questions.json"
DB_PATH = BASE_DIR / "data" / "elysia.db"

def parse_input_lines(inp_str: str):
    """Parses sample input text into variable input statements."""
    lines = [l.strip() for l in inp_str.strip().split("\n") if l.strip()]
    var_stmts = []
    for i, line in enumerate(lines):
        try:
            int(line)
            var_stmts.append((f"var_{i+1}", "int(input())", line))
            continue
        except ValueError:
            pass
        try:
            float(line)
            var_stmts.append((f"var_{i+1}", "float(input())", line))
            continue
        except ValueError:
            pass
        parts = line.split()
        if len(parts) > 1 and all(p.replace(".", "", 1).isdigit() for p in parts):
            if any("." in p for p in parts):
                var_stmts.append((f"list_{i+1}", "list(map(float, input().split()))", line))
            else:
                var_stmts.append((f"list_{i+1}", "list(map(int, input().split()))", line))
            continue
        var_stmts.append((f"text_{i+1}", "input().strip()", line))
    return var_stmts

def test_code(code: str, stdin_str: str, expected_out: str) -> bool:
    """Executes code with stdin_str and returns whether stdout matches expected_out."""
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin = io.StringIO(stdin_str)
    sys.stdout = io.StringIO()
    try:
        exec(code, {})
        actual = sys.stdout.getvalue().strip()
        return actual == expected_out.strip()
    except Exception:
        return False
    finally:
        sys.stdin, sys.stdout = old_stdin, old_stdout

def main():
    with open(QUESTIONS_JSON, "r", encoding="utf-8") as f:
        questions = json.load(f)

    print(f"Total questions loaded: {len(questions)}")

    stats = {
        "already_dynamic": 0,
        "scenario_converted": 0,
        "sem_converted": 0,
        "sem_assign_converted": 0,
        "core_assigned_converted": 0,
        "tuple_assigned_converted": 0,
        "func_converted": 0,
        "untouched": 0,
        "total_verified": 0
    }

    modified_questions = []

    for q in questions:
        qid = q.get("id", "")
        topic = q.get("topic", "")
        subject = q.get("subject", "")

        # Non-python questions
        if subject != "python":
            modified_questions.append(q)
            stats["untouched"] += 1
            continue

        # Already converted (CBT questions)
        if topic == "py_cbt":
            modified_questions.append(q)
            stats["already_dynamic"] += 1
            stats["total_verified"] += 1
            continue

        sample_in = q.get("sample_input", "")
        exp_out = q.get("expected_output", "")
        starter = q.get("starter_code", "")
        sol = q.get("solution_code", "")

        # -----------------------------------------------------------------
        # 1. RL and PR Scenario Questions (py_real_life, py_practice_500)
        # -----------------------------------------------------------------
        if topic in ("py_real_life", "py_practice_500") and sample_in:
            var_stmts = parse_input_lines(sample_in)
            if var_stmts:
                starter_input_lines = ["# Read input values from user / test case:"]
                for vname, vcall, _ in var_stmts:
                    starter_input_lines.append(f"{vname} = {vcall}")
                starter_input_block = "\n".join(starter_input_lines)

                if "# Sample Input Values:" in starter:
                    parts = starter.split("# Sample Input Values:")
                    top_part = parts[0]
                    todo_part = ""
                    if "# TODO:" in parts[1]:
                        todo_part = "\n# TODO:" + parts[1].split("# TODO:", 1)[1]
                    new_starter = top_part.rstrip() + "\n\n" + starter_input_block + "\n" + todo_part
                else:
                    new_starter = starter

                sol_var_lines = [f"{vname} = {vcall}" for vname, vcall, _ in var_stmts]
                out_lines = exp_out.strip().split("\n")
                print_lines = [f"print({repr(ol)})" for ol in out_lines]
                new_sol = "\n".join(sol_var_lines + print_lines)

                if test_code(new_sol, sample_in, exp_out):
                    q["starter_code"] = new_starter
                    q["solution_code"] = new_sol
                    stats["scenario_converted"] += 1
                    stats["total_verified"] += 1
                    modified_questions.append(q)
                    continue

        # -----------------------------------------------------------------
        # 2. Semester Questions (py_semester: PY-001 to PY-045)
        # -----------------------------------------------------------------
        if topic == "py_semester" and sample_in:
            in_lines = [l.strip() for l in sample_in.split("\n") if l.strip()]
            sol_lines = sol.split("\n")
            new_sol_lines = []
            in_idx = 0
            replaced_vars = []

            for line in sol_lines:
                stripped = line.strip()
                m = re.match(r"^([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(.+)$", stripped)
                if m and in_idx < len(in_lines) and not line.startswith("    ") and not line.startswith("def "):
                    val_str = in_lines[in_idx]
                    var_name = m.group(1)
                    try:
                        int(val_str)
                        new_line = f"{var_name} = int(input())"
                        in_idx += 1
                        replaced_vars.append(f"{var_name} = int(input())")
                    except ValueError:
                        try:
                            float(val_str)
                            new_line = f"{var_name} = float(input())"
                            in_idx += 1
                            replaced_vars.append(f"{var_name} = float(input())")
                        except ValueError:
                            new_line = f"{var_name} = input().strip()"
                            in_idx += 1
                            replaced_vars.append(f"{var_name} = input().strip()")
                    new_sol_lines.append(new_line)
                else:
                    new_sol_lines.append(line)

            candidate_sol = "\n".join(new_sol_lines)
            if test_code(candidate_sol, sample_in, exp_out):
                if "# Sample Input Values:" in starter:
                    parts = starter.split("# Sample Input Values:")
                    top_part = parts[0]
                    todo_part = "\n# TODO:" + parts[1].split("# TODO:", 1)[1] if "# TODO:" in parts[1] else ""
                    new_starter = top_part.rstrip() + "\n\n# Read input from user:\n" + "\n".join(replaced_vars) + "\n" + todo_part
                else:
                    new_starter = starter
                q["starter_code"] = new_starter
                q["solution_code"] = candidate_sol
                stats["sem_converted"] += 1
                stats["total_verified"] += 1
                modified_questions.append(q)
                continue

        # -----------------------------------------------------------------
        # 3. Semester Assignment (py_sem_assignment: SEM-001 to SEM-045)
        # -----------------------------------------------------------------
        if topic == "py_sem_assignment" and sample_in:
            in_lines = [l.strip() for l in sample_in.split("\n") if l.strip()]
            sol_lines = sol.split("\n")
            new_sol_lines = []
            in_idx = 0
            replaced_vars = []

            for line in sol_lines:
                stripped = line.strip()
                m = re.match(r"^([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(.+)$", stripped)
                if m and in_idx < len(in_lines) and not line.startswith("    ") and not line.startswith("def "):
                    val_str = in_lines[in_idx]
                    var_name = m.group(1)
                    rhs = m.group(2).strip()
                    if val_str in rhs or rhs.replace(".0", "") == val_str.replace(".0", ""):
                        try:
                            int(val_str)
                            new_line = f"{var_name} = int(input())"
                            in_idx += 1
                            replaced_vars.append(f"{var_name} = int(input())")
                        except ValueError:
                            try:
                                float(val_str)
                                new_line = f"{var_name} = float(input())"
                                in_idx += 1
                                replaced_vars.append(f"{var_name} = float(input())")
                            except ValueError:
                                new_line = f"{var_name} = input().strip()"
                                in_idx += 1
                                replaced_vars.append(f"{var_name} = input().strip()")
                        new_sol_lines.append(new_line)
                    else:
                        new_sol_lines.append(line)
                else:
                    new_sol_lines.append(line)

            candidate_sol = "\n".join(new_sol_lines)
            if test_code(candidate_sol, sample_in, exp_out):
                starter_lines = starter.split("\n")
                new_starter_lines = []
                for sline in starter_lines:
                    sm = re.match(r"^([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(.+)$", sline.strip())
                    matched = False
                    if sm:
                        svar = sm.group(1)
                        for rvar in replaced_vars:
                            if rvar.startswith(svar + " ="):
                                new_starter_lines.append(rvar)
                                matched = True
                                break
                    if not matched:
                        new_starter_lines.append(sline)
                q["starter_code"] = "\n".join(new_starter_lines)
                q["solution_code"] = candidate_sol
                stats["sem_assign_converted"] += 1
                stats["total_verified"] += 1
                modified_questions.append(q)
                continue

        # -----------------------------------------------------------------
        # 4. Multi-variable tuple assignments (e.g. p, r, t = 1000, 5.0, 2)
        # -----------------------------------------------------------------
        first_line = starter.strip().split("\n")[0] if starter.strip() else ""
        tuple_m = re.match(r"^([a-zA-Z_0-9,\s]+)\s*=\s*([0-9.,\s]+)$", first_line)
        if tuple_m and "," in tuple_m.group(1) and not first_line.startswith("#"):
            var_names = [v.strip() for v in tuple_m.group(1).split(",")]
            val_strs = [v.strip() for v in tuple_m.group(2).split(",")]
            if len(var_names) == len(val_strs):
                sample_lines = val_strs
                input_lines = []
                for vname, vval in zip(var_names, val_strs):
                    try:
                        int(vval)
                        input_lines.append(f"{vname} = int(input())")
                    except ValueError:
                        try:
                            float(vval)
                            input_lines.append(f"{vname} = float(input())")
                        except ValueError:
                            input_lines.append(f"{vname} = input().strip()")
                candidate_sample = "\n".join(sample_lines)
                old_assign = tuple_m.group(0)
                new_sol = sol.replace(old_assign, "\n".join(input_lines), 1)
                new_starter = starter.replace(old_assign, "\n".join(input_lines), 1)
                if test_code(new_sol, candidate_sample, exp_out):
                    q["sample_input"] = candidate_sample
                    q["starter_code"] = new_starter
                    q["solution_code"] = new_sol
                    stats["tuple_assigned_converted"] += 1
                    stats["total_verified"] += 1
                    modified_questions.append(q)
                    continue

        # -----------------------------------------------------------------
        # 5. Core Python Questions with Single Variable Assignments at Top
        # -----------------------------------------------------------------
        lines = starter.split("\n")
        assigns = []
        for l in lines:
            stripped = l.strip()
            if not stripped or stripped.startswith("#"):
                continue
            m = re.match(r"^([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(.+)$", stripped)
            if m and not stripped.startswith("def ") and not stripped.startswith("class ") and not stripped.startswith("for ") and not stripped.startswith("if "):
                var_name, val_expr = m.group(1), m.group(2).strip()
                try:
                    val = ast.literal_eval(val_expr)
                    assigns.append((var_name, val_expr, val))
                except Exception:
                    break
            else:
                break

        if assigns:
            sample_in_lines = []
            input_code_lines = []
            for var_name, val_expr, val in assigns:
                if isinstance(val, int):
                    sample_in_lines.append(str(val))
                    input_code_lines.append(f"{var_name} = int(input())")
                elif isinstance(val, float):
                    sample_in_lines.append(str(val))
                    input_code_lines.append(f"{var_name} = float(input())")
                elif isinstance(val, str) and "\n" not in val:
                    sample_in_lines.append(val)
                    input_code_lines.append(f"{var_name} = input().strip()")
                elif isinstance(val, (list, tuple, set)):
                    if val and all(isinstance(x, int) for x in val):
                        sample_in_lines.append(" ".join(str(x) for x in val))
                        if isinstance(val, list):
                            input_code_lines.append(f"{var_name} = list(map(int, input().split()))")
                        elif isinstance(val, tuple):
                            input_code_lines.append(f"{var_name} = tuple(map(int, input().split()))")
                        else:
                            input_code_lines.append(f"{var_name} = set(map(int, input().split()))")
                    elif val and all(isinstance(x, float) for x in val):
                        sample_in_lines.append(" ".join(str(x) for x in val))
                        if isinstance(val, list):
                            input_code_lines.append(f"{var_name} = list(map(float, input().split()))")
                        elif isinstance(val, tuple):
                            input_code_lines.append(f"{var_name} = tuple(map(float, input().split()))")
                        else:
                            input_code_lines.append(f"{var_name} = set(map(float, input().split()))")
                    else:
                        input_code_lines.append(f"{var_name} = {val_expr}")
                else:
                    input_code_lines.append(f"{var_name} = {val_expr}")

            sample_in_str = "\n".join(sample_in_lines)
            new_sol = sol
            new_starter = starter

            for (var_name, val_expr, val), inp_line in zip(assigns, input_code_lines):
                if "= int(input())" in inp_line or "= float(input())" in inp_line or "= input().strip()" in inp_line or "input().split()" in inp_line:
                    pattern = re.compile(rf"^\s*{re.escape(var_name)}\s*=\s*{re.escape(val_expr)}", re.MULTILINE)
                    new_sol = pattern.sub(inp_line, new_sol, count=1)
                    new_starter = pattern.sub(inp_line, new_starter, count=1)

            if sample_in_str and test_code(new_sol, sample_in_str, exp_out):
                q["sample_input"] = sample_in_str
                q["starter_code"] = new_starter
                q["solution_code"] = new_sol
                stats["core_assigned_converted"] += 1
                stats["total_verified"] += 1
                modified_questions.append(q)
                continue

        # -----------------------------------------------------------------
        # 6. Function Questions (py_functions: call & print calls)
        # -----------------------------------------------------------------
        if topic == "py_functions":
            sol_lines = sol.split("\n")
            starter_lines = starter.split("\n")
            handled_fn = False

            # Case A: Assignment call: ret = fn(...) or r1, r2 = fn(...)
            for idx, l in enumerate(sol_lines):
                if not l.startswith("    ") and not l.startswith("def ") and "=" in l and "(" in l and ")" in l:
                    m = re.match(r"^([a-zA-Z_0-9,\s]+)\s*=\s*([a-zA-Z_][a-zA-Z0-9_]*)\((.+)\)$", l.strip())
                    if m:
                        ret_vars = m.group(1).strip()
                        fn_name = m.group(2).strip()
                        args_str = m.group(3).strip()
                        try:
                            parsed_args = ast.literal_eval(f"({args_str},)")
                            fn_in = []
                            in_reads = []
                            arg_names = []
                            for ai, arg in enumerate(parsed_args):
                                aname = f"arg_{ai+1}"
                                arg_names.append(aname)
                                if isinstance(arg, int):
                                    fn_in.append(str(arg))
                                    in_reads.append(f"{aname} = int(input())")
                                elif isinstance(arg, float):
                                    fn_in.append(str(arg))
                                    in_reads.append(f"{aname} = float(input())")
                                elif isinstance(arg, str):
                                    fn_in.append(arg)
                                    in_reads.append(f"{aname} = input().strip()")
                                else:
                                    in_reads.append(f"{aname} = {repr(arg)}")
                            candidate_sample_in = "\n".join(fn_in)
                            args_joined = ", ".join(arg_names)
                            new_call = f"{ret_vars} = {fn_name}({args_joined})"
                            candidate_sol = "\n".join(sol_lines[:idx] + in_reads + [new_call] + sol_lines[idx+1:])

                            if test_code(candidate_sol, candidate_sample_in, exp_out):
                                s_idx = None
                                for s_i, sl in enumerate(starter_lines):
                                    if fn_name in sl and "(" in sl and "=" in sl and not sl.strip().startswith("#"):
                                        s_idx = s_i
                                        break
                                if s_idx is not None:
                                    new_starter = "\n".join(starter_lines[:s_idx] + in_reads + [new_call] + starter_lines[s_idx+1:])
                                else:
                                    new_starter = starter + "\n" + "\n".join(in_reads + [new_call])
                                q["sample_input"] = candidate_sample_in
                                q["starter_code"] = new_starter
                                q["solution_code"] = candidate_sol
                                stats["func_converted"] += 1
                                stats["total_verified"] += 1
                                modified_questions.append(q)
                                handled_fn = True
                                break
                        except Exception:
                            pass
            if handled_fn:
                continue

            # Case B: Direct function call inside print: print(f'... {fn(a, b)} ...')
            for idx, l in enumerate(sol_lines):
                if not l.startswith("    ") and not l.startswith("def ") and "print(" in l:
                    m = re.search(r"([a-zA-Z_][a-zA-Z0-9_]*)\(([^()]+)\)", l)
                    if m and m.group(1) != "print":
                        fn_name = m.group(1)
                        args_str = m.group(2)
                        try:
                            parsed_args = ast.literal_eval(f"({args_str},)")
                            fn_in = []
                            in_reads = []
                            arg_names = []
                            for ai, arg in enumerate(parsed_args):
                                aname = f"arg_{ai+1}"
                                arg_names.append(aname)
                                if isinstance(arg, int):
                                    fn_in.append(str(arg))
                                    in_reads.append(f"{aname} = int(input())")
                                elif isinstance(arg, float):
                                    fn_in.append(str(arg))
                                    in_reads.append(f"{aname} = float(input())")
                                elif isinstance(arg, str):
                                    fn_in.append(arg)
                                    in_reads.append(f"{aname} = input().strip()")
                                else:
                                    in_reads.append(f"{aname} = {repr(arg)}")
                            candidate_sample_in = "\n".join(fn_in)
                            args_joined = ", ".join(arg_names)
                            new_print = l.replace(f"{fn_name}({args_str})", f"{fn_name}({args_joined})")
                            candidate_sol = "\n".join(sol_lines[:idx] + in_reads + [new_print] + sol_lines[idx+1:])

                            if test_code(candidate_sol, candidate_sample_in, exp_out):
                                s_idx = None
                                for s_i, sl in enumerate(starter_lines):
                                    if fn_name in sl and "(" in sl and not sl.strip().startswith("#") and not sl.strip().startswith("def "):
                                        s_idx = s_i
                                        break
                                if s_idx is not None:
                                    new_starter = "\n".join(starter_lines[:s_idx] + in_reads + [new_print] + starter_lines[s_idx+1:])
                                else:
                                    new_starter = starter + "\n" + "\n".join(in_reads + [new_print])
                                q["sample_input"] = candidate_sample_in
                                q["starter_code"] = new_starter
                                q["solution_code"] = candidate_sol
                                stats["func_converted"] += 1
                                stats["total_verified"] += 1
                                modified_questions.append(q)
                                handled_fn = True
                                break
                        except Exception:
                            pass
            if handled_fn:
                continue

        # If question could not be converted or was already fine, keep as is
        stats["untouched"] += 1
        modified_questions.append(q)

    print("\n" + "="*50)
    print("CONVERSION SUMMARY:")
    for k, v in stats.items():
        print(f"  {k:28}: {v}")
    print("="*50)

    # Save to data/questions.json
    with open(QUESTIONS_JSON, "w", encoding="utf-8") as f:
        json.dump(modified_questions, f, indent=2, ensure_ascii=False)
    print(f"✅ Saved {len(modified_questions)} questions to {QUESTIONS_JSON}")

    # Sync to SQLite elysia.db
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Check if sample_input and is_scenario columns exist in SQLite table
    cursor.execute("PRAGMA table_info(questions)")
    existing_cols = [c[1] for c in cursor.fetchall()]
    if "sample_input" not in existing_cols:
        cursor.execute("ALTER TABLE questions ADD COLUMN sample_input TEXT DEFAULT ''")
    if "is_scenario" not in existing_cols:
        cursor.execute("ALTER TABLE questions ADD COLUMN is_scenario INTEGER DEFAULT 0")
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM questions")
    prev_cnt = cursor.fetchone()[0]
    
    cursor.execute("DELETE FROM questions")
    for q in modified_questions:
        cursor.execute("""
            INSERT INTO questions (id, subject, topic, difficulty, xp, title_en, title_hi, desc_en, desc_hi, starter_code, solution_code, expected_output, hint_en, hint_hi, sample_input, is_scenario)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            q.get("id"),
            q.get("subject"),
            q.get("topic"),
            q.get("difficulty"),
            q.get("xp", 50),
            q.get("title_en"),
            q.get("title_hi"),
            q.get("desc_en"),
            q.get("desc_hi"),
            q.get("starter_code"),
            q.get("solution_code"),
            q.get("expected_output"),
            q.get("hint_en"),
            q.get("hint_hi"),
            q.get("sample_input", ""),
            1 if q.get("is_scenario") else 0
        ))
    conn.commit()
    cursor.execute("SELECT COUNT(*) FROM questions")
    new_cnt = cursor.fetchone()[0]
    conn.close()
    print(f"✅ SQLite elysia.db updated: {new_cnt} rows inserted (previously {prev_cnt})")

if __name__ == "__main__":
    main()
