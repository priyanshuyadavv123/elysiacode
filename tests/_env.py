"""Imported first by every test file: point the database at a throw-away temp folder,
so running tests can NEVER touch your real data/ folder or leave test users behind."""
import atexit
import os
import shutil
import tempfile

_TMP = tempfile.mkdtemp(prefix="elysia_test_")
os.environ["ELYSIA_DATA_DIR"] = _TMP
os.environ["ELYSIA_TESTING"] = "1"
os.environ["ELYSIA_OFFLINE_AI"] = "1"
# Ensure tests run deterministically offline without calling live external AI APIs
os.environ["GROQ_API_KEY"] = ""
os.environ["GEMINI_API_KEY"] = ""
atexit.register(lambda: shutil.rmtree(_TMP, ignore_errors=True))

