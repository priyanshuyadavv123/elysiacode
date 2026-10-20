"""
Central configuration and environment loader for Elysia Code.
Loads .env safely without clobbering existing environment variables,
and provides helper utilities for typed configuration access.
"""

import logging
import os
from pathlib import Path
from typing import Any

logger = logging.getLogger("elysia")

BASE_DIR = Path(__file__).resolve().parent.parent


def load_env(env_path: Path = None, override: bool = False):
    """
    Loads environment variables from .env file into os.environ.
    Respects ELYSIA_TESTING=1 by not loading credentials during tests.
    Does not overwrite existing environment variables unless override=True.
    """
    if os.environ.get("ELYSIA_TESTING") == "1":
        return

    target = env_path or (BASE_DIR / ".env")
    if not target.is_file():
        return

    try:
        with open(target, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                k = k.strip()
                v = v.strip().strip("'\"")
                if k and (override or k not in os.environ):
                    os.environ[k] = v
    except Exception as exc:
        logger.warning("Failed to load .env from %s: %s", target, exc)


# Auto-load on module import
load_env()


def get_env_flag(name: str, default: bool = False) -> bool:
    """Reads a boolean flag from os.environ."""
    raw = os.environ.get(name)
    if raw is None or raw.strip() == "":
        return default
    return raw.strip().lower() in ("1", "true", "yes", "on")


def get_env_str(name: str, default: str = "") -> str:
    """Reads a string variable from os.environ."""
    return os.environ.get(name, default)


def get_env_int(name: str, default: int = 0) -> int:
    """Reads an integer variable from os.environ."""
    raw = os.environ.get(name)
    if raw is None or raw.strip() == "":
        return default
    try:
        return int(raw.strip())
    except ValueError:
        return default
