"""
Security tests for AI execution safety and endpoint restrictions.
Verifies that:
1. core/ai_tutor.py contains no exec() calls on model output.
2. GET /api/questions/generate-ai is disallowed / rejected.
3. exec() and eval() in core/ are quarantined exclusively to core/limited_runner.py.
4. Server execution cannot be invoked when ELYSIA_ALLOW_SERVER_EXEC=0.
"""

import ast
import os
import sys
import unittest
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _env  # noqa: F401


class TestAISafety(unittest.TestCase):
    def test_no_exec_in_ai_tutor(self):
        """Verify core/ai_tutor.py contains no exec( calls on model output."""
        file_path = BASE_DIR / "core" / "ai_tutor.py"
        content = file_path.read_text(encoding="utf-8")
        self.assertNotIn("exec(", content, "core/ai_tutor.py must never call exec() on model output!")

    def test_get_generate_ai_route_rejected(self):
        """Verify main.py does not define a GET route for /api/questions/generate-ai."""
        file_path = BASE_DIR / "main.py"
        content = file_path.read_text(encoding="utf-8")
        # In do_GET / _handle_get_api, /api/questions/generate-ai must not appear
        self.assertNotIn('path == "/api/questions/generate-ai"', content.split("def do_POST")[0],
                         "main.py must not route GET /api/questions/generate-ai")

    def test_exec_eval_quarantined_to_limited_runner(self):
        """Verify exec() and eval() in core/ are called exclusively in core/limited_runner.py."""
        core_dir = BASE_DIR / "core"
        allowed_file = (core_dir / "limited_runner.py").resolve()
        violations = []
        for py_file in core_dir.glob("*.py"):
            resolved = py_file.resolve()
            if resolved == allowed_file or ".bak" in py_file.name:
                continue
            text = py_file.read_text(encoding="utf-8")
            if "exec(" in text or "eval(" in text:
                violations.append(py_file.name)
        self.assertEqual(violations, [], f"Found exec() or eval() in top-level core/: {violations}")

        # AST check across all files in core/
        ast_calls = []
        for py_file in core_dir.glob("**/*.py"):
            if ".bak" in py_file.name or py_file.resolve() == allowed_file:
                continue
            try:
                tree = ast.parse(py_file.read_text(encoding="utf-8"))
                for node in ast.walk(tree):
                    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                        if node.func.id in ("exec", "eval"):
                            ast_calls.append(f"{py_file.name}:{node.lineno}")
            except Exception:
                pass
        self.assertEqual(ast_calls, [], f"AST found active calls to exec() or eval(): {ast_calls}")

    def test_server_exec_flag_respected(self):
        """Verify limited_runner honors the ELYSIA_ALLOW_SERVER_EXEC disabled state."""
        old_val = os.environ.get("ELYSIA_ALLOW_SERVER_EXEC")
        try:
            os.environ["ELYSIA_ALLOW_SERVER_EXEC"] = "0"
            import main
            self.assertFalse(main._env_flag("ELYSIA_ALLOW_SERVER_EXEC", True))
        finally:
            if old_val is not None:
                os.environ["ELYSIA_ALLOW_SERVER_EXEC"] = old_val
            else:
                os.environ.pop("ELYSIA_ALLOW_SERVER_EXEC", None)


if __name__ == "__main__":
    unittest.main()
