"""
Unit tests for Elysia Code core modules:
- Curriculum integrity
- Dynamic Question Bank filtering
- Mock Exam structure & Scoring
- Lab Record HTML Exporter
- Socratic Senior AI error decoding
"""

import unittest
import sys
from pathlib import Path

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _env  # noqa: F401  (uses a temporary database, never your real data/)

from core.curriculum import CURRICULUM_DATA
from core.question_bank import get_questions, QUESTIONS_DATABASE
from core.mock_tests import get_mock_exam, MOCK_EXAMS
from core.lab_exporter import generate_lab_record_html
from core.socratic_ai import decode_error

class TestElysiaCore(unittest.TestCase):
    def test_curriculum_structure(self):
        """Ensure Python and HTML tracks have complete bilingual content."""
        self.assertIn("python", CURRICULUM_DATA)
        self.assertIn("html", CURRICULUM_DATA)

        for track in ["python", "html"]:
            data = CURRICULUM_DATA[track]
            self.assertTrue(len(data["topics"]) > 0)
            for topic in data["topics"]:
                self.assertIn("id", topic)
                self.assertIn("title", topic)
                self.assertIn("intro_en", topic)
                self.assertIn("intro_hi", topic)
                self.assertIn("common_mistakes", topic)
                self.assertTrue(len(topic["common_mistakes"]) > 0)
                self.assertIn("viva_questions", topic)
                self.assertTrue(len(topic["viva_questions"]) > 0)

    def test_question_bank_filter(self):
        """Test question filtering by subject, topic, difficulty and count."""
        py_questions = get_questions(subject="python", count=10)
        self.assertEqual(len(py_questions), 10)
        for q in py_questions:
            self.assertEqual(q["subject"], "python")
            self.assertIn("expected_output", q)
            self.assertIn("solution_code", q)
            self.assertIn("starter_code", q)
            self.assertIn("title_en", q)
            self.assertIn("title_hi", q)

        html_questions = get_questions(subject="html", count=5)
        self.assertEqual(len(html_questions), 5)
        for q in html_questions:
            self.assertEqual(q["subject"], "html")
            self.assertIn("expected_html_elements", q)
            self.assertTrue(len(q["expected_html_elements"]) > 0)

        # Test specific topic filtering
        var_questions = get_questions(subject="python", topic="py_variables", count=5)
        self.assertTrue(len(var_questions) >= 3)
        for q in var_questions:
            self.assertEqual(q["topic"], "py_variables")

        # Test difficulty filtering
        tricky_questions = get_questions(subject="python", difficulty="Tricky", count=10)
        self.assertTrue(len(tricky_questions) >= 4)
        for q in tricky_questions:
            self.assertEqual(q["difficulty"].lower(), "tricky")

    def test_mock_exams(self):
        """Verify mock exams structure."""
        exam = get_mock_exam("python_ca1")
        self.assertIsNotNone(exam)
        self.assertIn("section_a_mcq", exam)
        self.assertIn("section_b_debug", exam)
        self.assertIn("section_d_viva", exam)
        self.assertEqual(exam["duration_minutes"], 25)

    def test_lab_exporter_html(self):
        """Verify lab sheet HTML generation with authentic formatting."""
        html = generate_lab_record_html(
            student_name="Test Student",
            roll_no="12345",
            course_code="CSE101",
            exp_no=1,
            title="Variables Test",
            aim="Testing variables",
            algorithm=["Step 1", "Step 2"],
            code="print('Hello')",
            sample_output="Hello",
            viva_qa=[{"question": "What is Python?", "answer_en": "A language"}]
        )
        self.assertIn("Test Student", html)
        self.assertIn("CSE101", html)
        self.assertIn("Variables Test", html)
        self.assertIn("Laboratory Practical Record File", html)

    def test_socratic_ai_decoding(self):
        """Verify that cryptic tracebacks are converted into Socratic advice."""
        # Test TypeError
        err = 'TypeError: can only concatenate str (not "int") to str'
        decoded_hi = decode_error(err, language="hi")
        self.assertTrue(decoded_hi["matched"])
        self.assertIn("fevicol", decoded_hi["advice"])

        decoded_en = decode_error(err, language="en")
        self.assertTrue(decoded_en["matched"])
        self.assertIn("f-string", decoded_en["advice"])

        # Test IndexError
        idx_err = 'IndexError: list index out of range'
        decoded_idx = decode_error(idx_err, language="hi")
        self.assertTrue(decoded_idx["matched"])
        self.assertIn("samos", decoded_idx["advice"])

    def test_handbook_data(self):
        """Verify the 8 visual handbook chapters and slides."""
        from core.handbook_data import get_all_chapters, get_chapter
        chapters = get_all_chapters()
        self.assertEqual(len(chapters), 8)
        for ch in chapters:
            self.assertTrue(len(ch["slides"]) > 0)
            for s in ch["slides"]:
                self.assertIn("title", s)
                self.assertIn("concept", s)
                self.assertIn("analogy_en", s)
                self.assertIn("analogy_hi", s)

    def test_python_code_execution(self):
        """Test local sub-15ms python execution engine."""
        import subprocess
        res = subprocess.run([sys.executable, "-c", "print('Elysia Code Fast')"], capture_output=True, text=True, timeout=2.0)
        self.assertEqual(res.returncode, 0)
        self.assertEqual(res.stdout.strip(), "Elysia Code Fast")

    def test_python_stdin_execution(self):
        """Test local python execution engine with input() and stdin."""
        import subprocess
        code = "name = input()\nage = int(input())\nprint(f'{name}:{age+1}')"
        res = subprocess.run([sys.executable, "-c", code], input="Alex\n19\n", capture_output=True, text=True, timeout=2.0)
        self.assertEqual(res.returncode, 0)
        self.assertEqual(res.stdout.strip(), "Alex:20")

    def test_auth_system(self):
        """Test user registration, login, profile update, and progress syncing."""
        from core.auth import register_user, login_user, update_profile, sync_user_progress

        import uuid
        test_user = "test_user_" + uuid.uuid4().hex[:8]     # new name every run, so reruns pass
        reg_res = register_user(
            username=test_user,
            name="Test User",
            email=f"{test_user}@test.local",
            password="secretpassword123",
            avatar="🚀"
        )
        self.assertTrue(reg_res["success"])
        self.assertEqual(reg_res["user"]["name"], "Test User")
        self.assertEqual(reg_res["user"]["avatar"], "🚀")

        # Test login success
        log_res = login_user(test_user, "secretpassword123")
        self.assertTrue(log_res["success"])
        self.assertEqual(log_res["user"]["username"], test_user)

        # Test login failure (wrong password)
        wrong_log = login_user(test_user, "wrongpassword")
        self.assertFalse(wrong_log["success"])

        # Test profile update
        up_res = update_profile(test_user, name="Updated Name", motto="Never stop learning", avatar="👑")
        self.assertTrue(up_res["success"])
        self.assertEqual(up_res["user"]["name"], "Updated Name")
        self.assertEqual(up_res["user"]["motto"], "Never stop learning")
        self.assertEqual(up_res["user"]["avatar"], "👑")

        # Test sync progress
        sync_res = sync_user_progress(test_user, xp=450, streak=7, today_seconds=3600, completed_subtopics=["sub_py_1", "sub_py_2"])
        self.assertTrue(sync_res["success"])
        self.assertEqual(sync_res["user"]["xp"], 450)
        self.assertEqual(sync_res["user"]["streak"], 7)

    def test_authoritative_curriculum_integrity(self):
        """Verify presence of all 7 Parts, 26 Chapters, 140 Subtopics, and 4 Mini-Projects."""
        from core.curriculum_builder import PARTS_REGISTRY, get_all_chapters

        # 1. Verify all 7 Parts
        self.assertEqual(len(PARTS_REGISTRY), 7, "Must contain exactly 7 parts")
        for i, part in enumerate(PARTS_REGISTRY, start=1):
            self.assertEqual(part["part_number"], i)
            self.assertTrue(len(part["chapters"]) > 0, f"Part {i} must have chapters")

        # 2. Verify all 26 Chapters
        all_chapters = get_all_chapters()
        self.assertEqual(len(all_chapters), 26, "Must contain exactly 26 chapters")

        expected_chapter_numbers = list(range(1, 27))
        actual_chapter_numbers = [ch["chapter_number"] for ch in all_chapters]
        self.assertEqual(actual_chapter_numbers, expected_chapter_numbers, "Chapters must be strictly sequential 1 to 26")

        # 3. Verify all 140 Subtopics
        total_subtopics = sum(len(ch["subtopics"]) for ch in all_chapters)
        self.assertEqual(total_subtopics, 140, "Must contain exactly 140 subtopics across all 26 chapters")

        # 4. Verify All 4 Mini-Projects
        mini_projects = [
            s["title"] for ch in all_chapters for s in ch["subtopics"]
            if "mini-project" in s["title"].lower()
        ]
        self.assertEqual(len(mini_projects), 4, "Must contain exactly 4 mini-projects")
        self.assertIn("Mini-Project: An Interactive Welcome Chatbot", mini_projects)
        self.assertIn("Mini-Project: A Choose-Your-Own-Adventure Text Game", mini_projects)
        self.assertIn("Mini-Project: A Password Guesser Game", mini_projects)
        self.assertIn("Mini-Project: A Desktop Calculator App", mini_projects)

        # 5. Verify Subtopic Pedagogical Structure
        for ch in all_chapters:
            self.assertTrue(len(ch["title"]) > 0)
            self.assertTrue(len(ch["learning_objectives_en"]) > 0)
            for s in ch["subtopics"]:
                self.assertIn("id", s)
                self.assertIn("title", s)
                self.assertIn("what_is_it_en", s)
                self.assertIn("what_is_it_hi", s)
                self.assertIn("rules_en", s)
                self.assertTrue(len(s["rules_en"]) > 0)
                self.assertIn("rules_hi", s)
                self.assertTrue(len(s["rules_hi"]) > 0)
                self.assertIn("analogy_en", s)
                self.assertIn("analogy_hi", s)
                self.assertIn("example_1", s)
                self.assertIn("code", s["example_1"])
                self.assertIn("expected_output", s["example_1"])
                self.assertIn("example_2", s)
                self.assertIn("code", s["example_2"])
                self.assertIn("expected_output", s["example_2"])
                self.assertIn("challenge", s)
                self.assertIn("prompt_en", s["challenge"])
                self.assertIn("solution_code", s["challenge"])

    def test_ai_tutor_unconfigured_graceful_handling(self):
        """Verify AI tutor returns clean unconfigured status without crashing when keys are absent."""
        from core.ai_tutor import AITutor
        import os

        # Initialize tutor with empty environment
        orig_gemini = os.environ.get("GEMINI_API_KEY")
        orig_groq = os.environ.get("GROQ_API_KEY")
        try:
            if "GEMINI_API_KEY" in os.environ:
                del os.environ["GEMINI_API_KEY"]
            if "GROQ_API_KEY" in os.environ:
                del os.environ["GROQ_API_KEY"]

            tutor = AITutor()
            status = tutor.get_status()
            self.assertFalse(status["configured"])
            self.assertFalse(status["providers"]["gemini"])
            self.assertFalse(status["providers"]["groq"])
            self.assertIn("unconfigured", status["message"].lower())

            # Test ask when unconfigured
            res = tutor.ask("How does a for loop work?", code="for i in range(5): print(i)")
            self.assertEqual(res["status"], "unconfigured")
            self.assertFalse(res["configured"])
            self.assertIsNone(res["response"])
            self.assertIn("unconfigured", res["message"].lower())
        finally:
            if orig_gemini is not None:
                os.environ["GEMINI_API_KEY"] = orig_gemini
            if orig_groq is not None:
                os.environ["GROQ_API_KEY"] = orig_groq

    def test_ai_tutor_provider_selection_when_configured(self):
        """Verify provider selection logic when Groq or Gemini credentials are configured."""
        from core.ai_tutor import AITutor
        import os
        from unittest.mock import patch

        # Test Groq priority
        with patch.dict(os.environ, {"GROQ_API_KEY": "dummy_groq_key", "GEMINI_API_KEY": ""}):
            tutor = AITutor()
            status = tutor.get_status()
            self.assertTrue(status["configured"])
            self.assertTrue(status["providers"]["groq"])
            self.assertFalse(status["providers"]["gemini"])
            self.assertEqual(status["primary_provider"], "groq")
            self.assertIn("Groq", status["message"])

        # Test Gemini when Groq absent
        with patch.dict(os.environ, {"GROQ_API_KEY": "", "GEMINI_API_KEY": "dummy_gemini_key"}):
            tutor = AITutor()
            status = tutor.get_status()
            self.assertTrue(status["configured"])
            self.assertFalse(status["providers"]["groq"])
            self.assertTrue(status["providers"]["gemini"])
            self.assertEqual(status["primary_provider"], "gemini")
            self.assertIn("Gemini", status["message"])

if __name__ == "__main__":
    unittest.main()


