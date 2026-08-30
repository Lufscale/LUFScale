#!/usr/bin/env python3
"""Record the exact autonomous runtime embedded in the macOS application."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
from pathlib import Path
from runpy import run_path

import PyInstaller
import PySide6
import psutil


PROJECT_ROOT = Path(__file__).resolve().parents[1]
APP_VERSION = str(
    run_path(PROJECT_ROOT / "src" / "lufscale" / "version.py")["APP_VERSION"]
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ffmpeg", type=Path, required=True)
    parser.add_argument("--target-arch", choices=("arm64", "x86_64"), required=True)
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()

    ffmpeg = arguments.ffmpeg.resolve()
    if not ffmpeg.is_file():
        raise FileNotFoundError(f"Bundled FFmpeg not found: {ffmpeg}")

    host_arch = platform.machine()
    if host_arch != arguments.target_arch:
        raise RuntimeError(
            f"Native build required: host is {host_arch}, target is "
            f"{arguments.target_arch}."
        )

    manifest = {
        "schema": 1,
        "application": {"name": "LUFScale", "version": APP_VERSION},
        "platform": {
            "system": "macOS",
            "architecture": arguments.target_arch,
            "minimum_version": "12.0",
        },
        "embedded_runtime": {
            "python": platform.python_version(),
            "pyside6_qt": PySide6.__version__,
            "psutil": psutil.__version__,
            "ffmpeg": {
                "filename": "ffmpeg",
                "sha256": sha256(ffmpeg),
            },
        },
        "packager": {
            "name": "PyInstaller",
            "version": PyInstaller.__version__,
            "isolated_python": str(Path(sys.executable).resolve()),
        },
        "end_user_external_runtime_required": False,
    }
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(arguments.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
