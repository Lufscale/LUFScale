"""Unified access to the standalone Windows translation catalogue."""

from __future__ import annotations

from typing import Any

from .catalog_windows import EXTRA_TEXTS, LANGUAGES, TEXTS


SUPPORTED_LANGUAGES = {code for code, _label in LANGUAGES}


def translate(language: str, key: str, **values: Any) -> str:
    if language in EXTRA_TEXTS:
        template = EXTRA_TEXTS[language].get(key, TEXTS[key][1])
    else:
        selected = 1 if language == "en" else 0
        template = TEXTS[key][selected]
    return template.format(**values)


__all__ = [
    "EXTRA_TEXTS",
    "LANGUAGES",
    "SUPPORTED_LANGUAGES",
    "TEXTS",
    "translate",
]
