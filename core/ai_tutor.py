"""
Elysia Code - Provider-Agnostic AI Tutor Engine.
Prepares an optional, modular AI interface for Groq and Gemini.
Designed for zero-dependency execution: if credentials are not configured,
it returns a clear, structured 'unconfigured' status without crashing.
No hardcoded API keys.
"""

import os
import json
import logging
import urllib.request
import urllib.error
import time
import re
import sys
from io import StringIO
from pathlib import Path
from typing import Dict, Any, Optional, List

from core.config import load_env

logger = logging.getLogger("elysia")

BASE_DIR = Path(__file__).resolve().parent.parent

def _ensure_env_loaded():
    """Reads .env into os.environ via centralized core.config loader."""
    load_env()

_ensure_env_loaded()

SOCRATIC_SYSTEM_PROMPT = """You are Elysia AI, a world-class, empathetic Python tutor and hostel senior for college engineering students.
Guide students Socratically:
- Explain intuition clearly using simple real-world analogies (e.g. samosa-chai, cricket, everyday hostel life).
- Point out syntax rules and why Python requires them.
- If code has a bug, explain WHY it fails and guide them to fix it rather than dumping the whole solution.
- Be concise, supportive, and bilingual (clear English + natural Hinglish terms when helpful).
"""

GROQ_MODELS = [
    "qwen/qwen3.8-27b",
    "openai/gpt-oss-120b",
    "openai/gpt-oss-20b",
    "allam-2-7b",
    "llama-3.3-70b-versatile",
    "llama-3.1-8b-instant",
    "mixtral-8x7b-32768"
]

HTTP_HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)"
}


class AITutor:
    def __init__(self):
        _ensure_env_loaded()
        self.gemini_key = os.environ.get("GEMINI_API_KEY", "").strip()
        self.groq_key = os.environ.get("GROQ_API_KEY", "").strip()

    def _refresh_keys(self):
        _ensure_env_loaded()
        self.gemini_key = os.environ.get("GEMINI_API_KEY", "").strip()
        self.groq_key = os.environ.get("GROQ_API_KEY", "").strip()

    def get_status(self) -> Dict[str, Any]:
        """Returns provider readiness status without revealing key values."""
        self._refresh_keys()
        has_gemini = bool(self.gemini_key)
        has_groq = bool(self.groq_key)
        configured = has_gemini or has_groq

        return {
            "configured": configured,
            "providers": {
                "gemini": has_gemini,
                "groq": has_groq
            },
            "primary_provider": "groq" if has_groq else ("gemini" if has_gemini else None),
            "message": (
                "AI Senior Tutor is active (Powered by Groq High-Speed Inference)."
                if has_groq
                else ("AI Tutor is active (Powered by Google Gemini)."
                      if has_gemini
                      else "AI Tutor is currently unconfigured. Set GROQ_API_KEY or GEMINI_API_KEY in your .env file to enable live AI mentoring.")
            )
        }

    def ask(self, query: str, code: str = "", topic: str = "", provider: str = "auto") -> Dict[str, Any]:
        """
        Sends student query to available AI provider.
        Returns clean JSON result or structured unconfigured/error status.
        Never crashes the application.
        """
        self._refresh_keys()
        status = self.get_status()
        if not status["configured"]:
            return {
                "status": "unconfigured",
                "configured": False,
                "provider": None,
                "message": (
                    "AI Tutor is currently unconfigured. "
                    "To enable real-time AI guidance, add your GROQ_API_KEY or GEMINI_API_KEY "
                    "to a .env file or system environment variables. "
                    "In the meantime, full lesson notes, bilingual analogies, syntax rules, "
                    "and automated hints remain 100% functional!"
                ),
                "response": None
            }

        # Select provider (default to Groq for ultra-fast response)
        target_provider = provider.lower()
        if target_provider == "auto":
            target_provider = "groq" if self.groq_key else "gemini"

        if os.environ.get("ELYSIA_OFFLINE_AI") == "1":
            return {
                "status": "offline_mode",
                "configured": True,
                "provider": target_provider,
                "message": "AI Tutor offline mode is active (testing environment).",
                "response": "Offline tutor response."
            }

        if target_provider == "groq" and self.groq_key:
            return self._call_groq(query, code, topic)
        elif target_provider == "gemini" and self.gemini_key:
            return self._call_gemini(query, code, topic)
        else:
            return {
                "status": "error",
                "configured": True,
                "provider": target_provider,
                "message": f"Requested provider '{target_provider}' is not configured.",
                "response": None
            }

    def diagnose_error(self, error: str, code: str = "", lang: str = "hi") -> Dict[str, Any]:
        """
        Specialized debugger: analyzes runtime tracebacks, syntax errors, or logical bugs
        and returns intuitive Socratic mentor feedback in Hinglish/English.
        """
        self._refresh_keys()
        if os.environ.get("ELYSIA_OFFLINE_AI") == "1":
            return {"status": "offline_mode", "matched": False}
        if not self.groq_key and not self.gemini_key:
            return {"status": "unconfigured", "matched": False}

        lang_label = "natural, friendly Hinglish (Hindi + English)" if lang == "hi" else "clear beginner-friendly English"
        user_prompt = (
            f"The student encountered this Python issue:\n\n"
            f"Traceback / Error Message:\n{error}\n\n"
        )
        if code.strip():
            user_prompt += f"Student's Code:\n```python\n{code}\n```\n\n"

        user_prompt += (
            f"Please diagnose this error in 3 to 5 clear sentences in {lang_label}.\n"
            f"1. Pinpoint the exact line number and what caused the error.\n"
            f"2. Explain WHY Python threw this error using an intuitive everyday analogy (e.g. samosa-chai, cricket, hostel life).\n"
            f"3. Give a clear Socratic clue or step-by-step fix so the student understands how to correct it.\n"
            f"Keep it concise, friendly, and practical."
        )

        res = self.ask(query=user_prompt, code="", topic="Error Diagnosis & Debugging", provider="auto")
        if res.get("status") == "success" and res.get("response"):
            advice_text = res["response"].strip()
            return {
                "status": "success",
                "matched": True,
                "ai_powered": True,
                "title": "🤖 Senior AI Error Diagnosis",
                "advice": advice_text,
                "advice_en": advice_text,
                "advice_hi": advice_text
            }

        return {"status": "error", "matched": False, "message": res.get("message")}

    def _call_groq(self, query: str, code: str, topic: str) -> Dict[str, Any]:
        """Calls Groq REST API using standard urllib with model fallback and custom User-Agent."""
        endpoint = "https://api.groq.com/openai/v1/chat/completions"
        user_prompt = f"Topic: {topic}\n" if topic else ""
        if code:
            user_prompt += f"Code:\n```python\n{code}\n```\n"
        user_prompt += f"Student Request: {query}"

        last_error = ""
        for model_name in GROQ_MODELS:
            payload = {
                "model": model_name,
                "messages": [
                    {"role": "system", "content": SOCRATIC_SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt}
                ],
                "temperature": 0.4,
                "max_tokens": 800
            }

            headers = dict(HTTP_HEADERS)
            headers["Authorization"] = f"Bearer {self.groq_key}"

            try:
                req = urllib.request.Request(
                    endpoint,
                    data=json.dumps(payload).encode("utf-8"),
                    headers=headers,
                    method="POST"
                )
                with urllib.request.urlopen(req, timeout=12) as response:
                    result = json.loads(response.read().decode("utf-8"))
                    text = result["choices"][0]["message"]["content"]
                    return {
                        "status": "success",
                        "configured": True,
                        "provider": "groq",
                        "model": model_name,
                        "response": text
                    }
            except urllib.error.HTTPError as e:
                err_body = ""
                try:
                    err_body = e.read().decode("utf-8")
                except Exception as exc:
                    logger.warning("Could not decode HTTP error body: %s", exc)
                last_error = f"HTTP {e.code}: {err_body or e.reason}"
                # If model not found or quota issue, continue loop to try fallback model
                if e.code in (404, 400) and ("model" in err_body or "not exist" in err_body):
                    continue
                break
            except Exception as e:
                last_error = str(e)
                break

        return {
            "status": "error",
            "configured": True,
            "provider": "groq",
            "message": f"Groq API error: {last_error}",
            "response": None
        }

    def _call_gemini(self, query: str, code: str, topic: str) -> Dict[str, Any]:
        """Calls Google Gemini REST API using urllib (zero external pip dependencies)."""
        endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={self.gemini_key}"
        user_prompt = f"Topic: {topic}\nCode:\n```python\n{code}\n```\nStudent Question: {query}"

        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": f"{SOCRATIC_SYSTEM_PROMPT}\n\n{user_prompt}"}]
                }
            ],
            "generationConfig": {
                "temperature": 0.4,
                "maxOutputTokens": 800
            }
        }

        try:
            req = urllib.request.Request(
                endpoint,
                data=json.dumps(payload).encode("utf-8"),
                headers=HTTP_HEADERS,
                method="POST"
            )
            with urllib.request.urlopen(req, timeout=12) as response:
                result = json.loads(response.read().decode("utf-8"))
                text = (
                    result.get("candidates", [{}])[0]
                    .get("content", {})
                    .get("parts", [{}])[0]
                    .get("text", "")
                )
                return {
                    "status": "success",
                    "configured": True,
                    "provider": "gemini",
                    "response": text
                }
        except Exception as e:
            return {
                "status": "error",
                "configured": True,
                "provider": "gemini",
                "message": f"Gemini API error: {str(e)}",
                "response": None
            }

    def generate_question(self, subject: str = "python", topic: str = "all", difficulty: str = "Intermediate", prompt_hint: str = "") -> Dict[str, Any]:
        """
        Uses Groq (with model fallback) to dynamically generate a practical coding question
        with starter code, solution code, and verified expected output.
        """
        self._refresh_keys()
        if not self.groq_key and not self.gemini_key:
            return {
                "status": "unconfigured",
                "message": "Groq API key is not configured in .env. Please set GROQ_API_KEY to generate live AI questions."
            }

        is_python = subject.lower() == "python"
        target_topic = topic if topic and topic != "all" else ("py_variables" if is_python else "html_tags")
        target_diff = difficulty if difficulty and difficulty != "all" else "Intermediate"
        topic_clean = target_topic.replace("py_", "").replace("html_", "").replace("_", " ").title()

        sys_prompt = (
            "You are Elysia AI, an expert computer science curriculum designer and Python architect. "
            "Your task is to generate realistic, practical college coding problems for students. "
            "You must return ONLY a single valid JSON object without any markdown wrapping or extra commentary."
        )

        expected_field_spec = (
            '"expected_output": "The exact string printed by solution_code (no trailing newline)",'
            if is_python
            else '"expected_html_elements": ["element1", "element2"],'
        )
        hint_line = f"Custom Context/Idea: {prompt_hint}" if prompt_hint else ""
        user_prompt = f"""Generate a brand new, creative coding problem for an engineering student.
Subject: {subject}
Topic: {topic_clean} ({target_topic})
Difficulty: {target_diff}
{hint_line}

Return a single JSON object with EXACTLY these keys:
{{
  "id": "ai_q_{int(time.time())}",
  "subject": "{subject.lower()}",
  "topic": "{target_topic}",
  "difficulty": "{target_diff}",
  "xp": {75 if target_diff.lower() == 'tricky' else (50 if target_diff.lower() == 'intermediate' else 30)},
  "title_en": "Creative English Title (e.g. Campus Cafeteria Bill Splitter)",
  "title_hi": "Creative Hinglish Title (e.g. Canteen Bill Splitter Problem)",
  "desc_en": "Clear problem statement explaining given variables, exact calculation, and what to print.",
  "desc_hi": "Problem statement in natural, friendly college Hinglish.",
  "starter_code": "Clean starter code template with comments for the student.",
  "solution_code": "Complete working solution that prints the exact expected output.",
  {expected_field_spec}
  "hint_en": "Helpful conceptual hint in English.",
  "hint_hi": "Helpful conceptual hint in Hinglish."
}}

MANDATORY RULES:
1. The code must NOT use input(). All test values must be hardcoded in variables.
2. In solution_code, print the answer using print(f'...').
3. Keep the output format simple and deterministic.
4. Output ONLY valid raw JSON."""

        last_error = ""
        for model_name in GROQ_MODELS:
            payload = {
                "model": model_name,
                "messages": [
                    {"role": "system", "content": sys_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                "response_format": {"type": "json_object"},
                "temperature": 0.5,
                "max_tokens": 1200
            }

            headers = dict(HTTP_HEADERS)
            headers["Authorization"] = f"Bearer {self.groq_key}"

            try:
                req = urllib.request.Request(
                    "https://api.groq.com/openai/v1/chat/completions",
                    data=json.dumps(payload).encode("utf-8"),
                    headers=headers,
                    method="POST"
                )
                with urllib.request.urlopen(req, timeout=15) as response:
                    raw_result = json.loads(response.read().decode("utf-8"))
                    content = raw_result["choices"][0]["message"]["content"].strip()

                    if content.startswith("```"):
                        content = re.sub(r"^```(?:json)?\s*", "", content)
                        content = re.sub(r"\s*```$", "", content)

                    q_data = json.loads(content)
                    q_data["ai_generated"] = True
                    if not q_data.get("id"):
                        q_data["id"] = f"ai_q_{int(time.time())}"
                    q_data["subject"] = subject.lower()
                    if not q_data.get("topic"):
                        q_data["topic"] = target_topic
                    if not q_data.get("difficulty"):
                        q_data["difficulty"] = target_diff
                    if not q_data.get("xp"):
                        q_data["xp"] = 50

                    # Verify Python solution_code safely in browser Pyodide (never on server)
                    if is_python and q_data.get("solution_code"):
                        q_data["output_verified"] = False

                    # Verify HTML elements
                    if not is_python and not q_data.get("expected_html_elements"):
                        tags = re.findall(r"<([a-zA-Z0-9]+)", q_data.get("solution_code", ""))
                        q_data["expected_html_elements"] = list(dict.fromkeys(tags))[:4] or ["div", "p"]

                    return {
                        "status": "success",
                        "model": model_name,
                        "question": q_data
                    }
            except urllib.error.HTTPError as e:
                err_body = ""
                try:
                    err_body = e.read().decode("utf-8")
                except Exception as exc:
                    logger.warning("Could not decode HTTP error body: %s", exc)
                last_error = f"HTTP {e.code}: {err_body or e.reason}"
                if e.code == 429:
                    time.sleep(1.0)
                continue
            except Exception as e:
                last_error = str(e)
                continue

        # Smart Graceful Fallback: Never leave the student stranded with an error popup!
        try:
            from core.question_bank import get_questions
            fallback_list = get_questions(subject=subject, topic=target_topic, difficulty=target_diff, count=1)
            if not fallback_list:
                fallback_list = get_questions(subject=subject, topic="all", difficulty="all", count=1)
            if fallback_list:
                fb_q = dict(fallback_list[0])
                fb_q["ai_generated"] = False
                fb_q["fallback_mode"] = True
                return {
                    "status": "success",
                    "rate_limited": True,
                    "notice": "Groq AI free tier rate limit was reached. Loaded a matching curriculum challenge!",
                    "question": fb_q
                }
        except Exception as exc:
            logger.warning("Question bank fallback lookup failed: %s", exc)

        return {
            "status": "error",
            "rate_limited": "429" in last_error,
            "message": "Groq AI is cooling down (Rate Limit). Please try again in a few seconds." if "429" in last_error else f"Failed to generate question via AI: {last_error}"
        }


ai_tutor = AITutor()

