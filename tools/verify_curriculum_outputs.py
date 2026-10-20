#!/usr/bin/env python3
"""
Elysia Code: Curriculum Output Verifier
Executes every subtopic's example_1, example_2, and challenge solution
across all 26 chapters (140 subtopics) and checks exact stdout output.

Desktop-only examples (such as Tkinter window initializations requiring a local
display server) are skipped with an explicit stated reason.
"""

import io
import json
import sys
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CURRICULUM_PATH = BASE_DIR / "data" / "curriculum_tree.json"


def verify_all_curriculum_outputs():
    if not CURRICULUM_PATH.exists():
        print(f"Error: Curriculum file not found at {CURRICULUM_PATH}")
        sys.exit(1)

    with open(CURRICULUM_PATH, "r", encoding="utf-8") as f:
        tree = json.load(f)

    total_subtopics = 0
    passed = 0
    skipped = 0
    failures = []

    print(f"Loaded curriculum with {len(tree)} chapters. Verifying examples & challenges...")

    for ch in tree:
        ch_title = ch.get("title", ch.get("id"))
        for s in ch.get("subtopics", []):
            total_subtopics += 1
            sub_id = s.get("id", "unknown_subtopic")

            for k in ["example_1", "example_2", "challenge"]:
                item = s.get(k)
                if not item:
                    continue

                title = item.get("title") or k
                if item.get("desktop_only"):
                    reason = item.get("desktop_only_note") or "Requires local desktop GUI display server"
                    print(f"  [SKIP] {sub_id} -> {k} ({title}): {reason}")
                    skipped += 1
                    continue

                code = item.get("code") or item.get("solution_code") or ""
                expected = str(item.get("expected_output", "")).strip()

                out_buf = io.StringIO()
                err_buf = io.StringIO()
                exec_globals = {"__name__": "__main__"}

                try:
                    with redirect_stdout(out_buf), redirect_stderr(err_buf):
                        exec(code, exec_globals)
                    actual = out_buf.getvalue().strip()

                    if actual == expected:
                        passed += 1
                    else:
                        failures.append({
                            "subtopic": sub_id,
                            "type": k,
                            "title": title,
                            "expected": expected,
                            "actual": actual,
                            "error": None
                        })
                except Exception as exc:
                    failures.append({
                        "subtopic": sub_id,
                        "type": k,
                        "title": title,
                        "expected": expected,
                        "actual": out_buf.getvalue().strip(),
                        "error": f"{type(exc).__name__}: {exc}"
                    })

    print("\n" + "=" * 60)
    print(f"Curriculum Verification Summary:")
    print(f"  Total Subtopics Evaluated: {total_subtopics}")
    print(f"  Passed Verifications:     {passed}")
    print(f"  Skipped (Desktop-Only):    {skipped}")
    print(f"  Failed Verifications:     {len(failures)}")
    print("=" * 60)

    if failures:
        print("\nFAILURES DETECTED:")
        for idx, f in enumerate(failures, 1):
            print(f"\n[{idx}] Subtopic: {f['subtopic']} ({f['type']} - {f['title']})")
            print(f"  Expected:\n{repr(f['expected'])}")
            print(f"  Actual:\n{repr(f['actual'])}")
            if f["error"]:
                print(f"  Runtime Exception: {f['error']}")
        return False

    print("\nALL CURRICULUM OUTPUTS VERIFIED PERFECTLY! (100% Deterministic)")
    return True


if __name__ == "__main__":
    success = verify_all_curriculum_outputs()
    sys.exit(0 if success else 1)
