"""Découverte et validation du moteur FFmpeg, sans dépendance Qt."""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from functools import lru_cache
from pathlib import Path

from ..audio.core import REQUIRED_AUDIO_ENCODERS
from ..i18n.loader import translate
from ..resources import application_folder, application_resource_folder
from .runtime import process_flags


@lru_cache(maxsize=1)
def find_ffmpeg() -> str | None:
    """Resolve the bundled engine, or development fallbacks from source."""
    executable_name = "ffmpeg.exe" if os.name == "nt" else "ffmpeg"
    # PyInstaller 6 places native binaries in Contents/Frameworks and creates
    # the matching cross-link in Contents/Resources.  Source/legacy layouts
    # may still place the executable next to the program, so both roots are
    # checked before any external fallback.
    for root in (application_resource_folder(), application_folder()):
        bundled = root / executable_name
        if bundled.is_file():
            return str(bundled)

    # A released application is deliberately autonomous.  Falling back to a
    # Homebrew, MacPorts, imageio or PATH executable could hide a damaged app
    # bundle and make results depend on unrelated software installed by the
    # user.  Development launches from the source tree retain those fallbacks.
    if getattr(sys, "frozen", False):
        return None

    explicit = Path(os.environ.get("IMAGEIO_FFMPEG_EXE", "")).expanduser()
    if explicit.is_file():
        return str(explicit)

    if os.name != "nt":
        # Finder does not always give GUI applications the shell PATH.  Check
        # the conventional Homebrew and MacPorts locations explicitly.
        for candidate in (
            Path("/opt/homebrew/bin/ffmpeg"),
            Path("/usr/local/bin/ffmpeg"),
            Path("/opt/local/bin/ffmpeg"),
        ):
            if candidate.is_file():
                return str(candidate)

    try:
        import imageio_ffmpeg

        imageio_executable = Path(imageio_ffmpeg.get_ffmpeg_exe())
        if imageio_executable.is_file():
            return str(imageio_executable)
    except (ImportError, OSError, RuntimeError):
        pass

    return shutil.which("ffmpeg")


@lru_cache(maxsize=8)
def ffmpeg_capability_error(
    ffmpeg: str,
    language: str = "fr",
) -> str | None:
    """Retourne une erreur localisée si le moteur requis est incomplet."""
    try:
        # The resolved executable is invoked directly without a shell.
        filters = subprocess.run(  # noqa: S603
            [ffmpeg, "-hide_banner", "-filters"],
            stdin=subprocess.DEVNULL,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=20,
            creationflags=process_flags(),
        )
        encoders = subprocess.run(  # noqa: S603
            [ffmpeg, "-hide_banner", "-encoders"],
            stdin=subprocess.DEVNULL,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=20,
            creationflags=process_flags(),
        )
    except (OSError, subprocess.SubprocessError) as exc:
        return translate(language, "ffmpeg_execution_error", error=exc)

    if filters.returncode != 0 or encoders.returncode != 0:
        return translate(language, "ffmpeg_not_responding")
    if " loudnorm " not in filters.stdout:
        return translate(language, "ffmpeg_no_loudnorm")
    missing_encoders = [
        encoder
        for encoder in REQUIRED_AUDIO_ENCODERS
        if not re.search(
            rf"\b{re.escape(encoder)}\b",
            encoders.stdout,
        )
    ]
    if missing_encoders:
        return translate(
            language,
            "ffmpeg_missing_encoders",
            encoders=", ".join(missing_encoders),
        )
    return None


__all__ = ["ffmpeg_capability_error", "find_ffmpeg"]
