"""
Curriculum Builder & Compiler for Elysia Code.
Combines all 7 parts (26 chapters, 140 subtopics, 4 mini-projects)
and compiles them into web/js/curriculum_tree.js, data/curriculum_tree.json,
and exposes helper functions for backend APIs.
"""

import json
from pathlib import Path
from typing import List, Dict, Any

from core.curriculum_parts.part1 import CHAPTERS as PART1_CHAPTERS
from core.curriculum_parts.part2 import CHAPTERS as PART2_CHAPTERS
from core.curriculum_parts.part3 import CHAPTERS as PART3_CHAPTERS
from core.curriculum_parts.part4 import CHAPTERS as PART4_CHAPTERS
from core.curriculum_parts.part5 import CHAPTERS as PART5_CHAPTERS
from core.curriculum_parts.part6 import CHAPTERS as PART6_CHAPTERS
from core.curriculum_parts.part7 import CHAPTERS as PART7_CHAPTERS

PARTS_REGISTRY = [
    {
        "part_number": 1,
        "part_title": "PART 1: THE ABSOLUTE BASICS (ZERO TO CODE)",
        "description": "Start from zero: Python philosophy, setup, terminal, print, input, variables, data types, and operators.",
        "chapters": PART1_CHAPTERS
    },
    {
        "part_number": 2,
        "part_title": "PART 2: MAKING DECISIONS AND REPEATING ACTIONS",
        "description": "Control flow: conditionals, indentation, while loops, for loops, range, break/continue, pass, and nested loops.",
        "chapters": PART2_CHAPTERS
    },
    {
        "part_number": 3,
        "part_title": "PART 3: ORGANIZING LOTS OF DATA (DATA STRUCTURES)",
        "description": "Core collections: Lists, Tuples, Dictionaries, and Sets with full indexing, slicing, methods, and set theory.",
        "chapters": PART3_CHAPTERS
    },
    {
        "part_number": 4,
        "part_title": "PART 4: WRITING REUSABLE CODE (FUNCTIONS AND MODULES)",
        "description": "Modular design: functions, parameters, return values, default arguments, *args/**kwargs, scope (LEGB), built-in modules, and custom packages.",
        "chapters": PART4_CHAPTERS
    },
    {
        "part_number": 5,
        "part_title": "PART 5: THE REAL WORLD (FILES, ERRORS, AND OBJECTS)",
        "description": "Production engineering: persistent file handling, CSV/JSON, exception hierarchies, and OOP classes, inheritance, polymorphism, and dunders.",
        "chapters": PART5_CHAPTERS
    },
    {
        "part_number": 6,
        "part_title": "PART 6: THE PEAK (ADVANCED PYTHON CONCEPTS)",
        "description": "Advanced Python: comprehensions, iterators, generators with yield, decorators with @ syntax, context managers with with, and regex pattern matching.",
        "chapters": PART6_CHAPTERS
    },
    {
        "part_number": 7,
        "part_title": "PART 7: GOING PROFESSIONAL (APPLIED PYTHON)",
        "description": "Industry engineering: HTTP requests, REST APIs, web scraping, desktop GUI apps with Tkinter, Desktop Calculator project, PEP 8, Git, venv, pytest, and packaging.",
        "chapters": PART7_CHAPTERS
    }
]


def get_all_chapters() -> List[Dict[str, Any]]:
    """Flattened list of all 26 chapters with part_number and part_title attached."""
    chapters = []
    for part in PARTS_REGISTRY:
        for ch in part["chapters"]:
            ch_copy = dict(ch)
            ch_copy["part_number"] = part["part_number"]
            ch_copy["part_title"] = part["part_title"]
            chapters.append(ch_copy)
    return chapters


def compile_curriculum_tree():
    """Compiles all chapters into JSON and JavaScript tree representations."""
    all_chapters = get_all_chapters()
    base_dir = Path(__file__).resolve().parent.parent

    # 1. Write to data/curriculum_tree.json
    data_dir = base_dir / "data"
    data_dir.mkdir(exist_ok=True)
    json_path = data_dir / "curriculum_tree.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_chapters, f, indent=2, ensure_ascii=False)

    # 2. Write to web/js/curriculum_tree.js
    js_path = base_dir / "web" / "js" / "curriculum_tree.js"
    json_str = json.dumps(all_chapters, indent=2, ensure_ascii=False)
    js_content = f"/**\n * ELYSIA CODE: AUTHORITATIVE PYTHON CURRICULUM TREE\n * All 7 Parts, 26 Chapters, 140 Subtopics, and 4 Mini-Projects.\n */\n\nwindow.PYTHON_CURRICULUM_PARTS = {json.dumps(PARTS_REGISTRY, indent=2, ensure_ascii=False)};\n\nwindow.PYTHON_CURRICULUM_TREE = {json_str};\n"
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js_content)

    print(f"Compiled {len(all_chapters)} chapters across {len(PARTS_REGISTRY)} parts.")
    total_subtopics = sum(len(ch["subtopics"]) for ch in all_chapters)
    print(f"Total subtopics: {total_subtopics}")
    return all_chapters


if __name__ == "__main__":
    compile_curriculum_tree()
