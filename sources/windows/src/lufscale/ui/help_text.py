"""Mise en forme lisible et indépendante de Qt pour les textes d'aide."""

from __future__ import annotations

import re


_PARAGRAPH_BREAK = re.compile(r"\n[ \t]*\n+")
_SENTENCE_BREAK = re.compile(r"(?<=[.!?])\s+|(?<=[。！？।])")
_BULLET_PREFIXES = ("•", "- ", "* ")


def _split_dense_paragraph(
    paragraph: str,
    *,
    preferred_length: int = 280,
    maximum_sentences: int = 2,
) -> str:
    """Split a long prose block at real sentence boundaries."""
    paragraph = paragraph.strip()
    if (
        len(paragraph) <= preferred_length
        or "\n" in paragraph
    ):
        return paragraph

    sentences = [
        sentence.strip()
        for sentence in _SENTENCE_BREAK.split(paragraph)
        if sentence.strip()
    ]
    if len(sentences) < 2:
        return paragraph

    groups: list[str] = []
    current: list[str] = []
    for sentence in sentences:
        candidate = " ".join((*current, sentence))
        if current and (
            len(candidate) > preferred_length
            or len(current) >= maximum_sentences
        ):
            groups.append(" ".join(current))
            current = [sentence]
        else:
            current.append(sentence)
    if current:
        groups.append(" ".join(current))
    return "\n\n".join(groups)


def format_help_text(text: str) -> str:
    """Air long help text while preserving headings and bullet lists."""
    normalized = str(text).replace("\r\n", "\n").replace("\r", "\n").strip()
    if not normalized:
        return ""

    paragraphs = _PARAGRAPH_BREAK.split(normalized)
    formatted: list[str] = []
    for paragraph in paragraphs:
        cleaned = paragraph.strip()
        lines = cleaned.splitlines()
        if any(
            line.lstrip().startswith(_BULLET_PREFIXES)
            for line in lines
        ):
            formatted.append(cleaned)
        else:
            formatted.append(_split_dense_paragraph(cleaned))
    return "\n\n".join(formatted)


__all__ = ["format_help_text"]
