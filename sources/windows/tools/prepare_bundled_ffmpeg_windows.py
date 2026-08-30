#!/usr/bin/env python3
"""Prepare and validate the FFmpeg executable embedded in the Windows build.

The Windows builder installs the pinned imageio-ffmpeg wheel for the native
x86-64 host.  This tool copies that wheel's executable into the packaging
staging area only after checking its PE architecture, filters, encoders and
licence-sensitive configuration.  The application itself never downloads a
runtime component.
"""

from __future__ import annotations

import hashlib
import json
import os
import platform
import re
import shutil
import struct
import subprocess
import sys
from importlib import metadata
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from lufscale.audio.core import REQUIRED_AUDIO_ENCODERS  # noqa: E402
from lufscale.version import APP_VERSION  # noqa: E402


OUTPUT_DIR = PROJECT_ROOT / "packaging" / "generated" / "windows-x86_64"
OUTPUT_FFMPEG = OUTPUT_DIR / "ffmpeg.exe"
OUTPUT_MANIFEST = OUTPUT_DIR / "FFMPEG_WINDOWS_BUILD_MANIFEST.json"
OUTPUT_NOTICE = OUTPUT_DIR / "FFMPEG_WINDOWS_DISTRIBUTION_NOTICE.txt"


def fail(message: str) -> "NoReturn":
    raise SystemExit(f"ERROR - {message}")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def pe_machine(path: Path) -> int:
    """Return the COFF machine field from a Windows PE executable."""
    with path.open("rb") as stream:
        if stream.read(2) != b"MZ":
            fail(f"not a Windows PE executable: {path}")
        stream.seek(0x3C)
        pe_offset = struct.unpack("<I", stream.read(4))[0]
        stream.seek(pe_offset)
        if stream.read(4) != b"PE\0\0":
            fail(f"invalid PE header: {path}")
        return struct.unpack("<H", stream.read(2))[0]


def run(executable: Path, *arguments: str) -> str:
    completed = subprocess.run(  # noqa: S603
        [str(executable), *arguments],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=60,
        check=False,
        creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
    )
    if completed.returncode != 0:
        fail(
            f"FFmpeg command failed ({completed.returncode}): "
            f"{' '.join(arguments)}\n{completed.stdout[-4000:]}"
        )
    return completed.stdout


def main() -> int:
    if os.name != "nt":
        fail("the bundled Windows FFmpeg must be prepared on Windows")
    if platform.machine().lower() not in {"amd64", "x86_64"}:
        fail(f"unsupported Windows architecture: {platform.machine()}")

    try:
        import imageio_ffmpeg
    except ImportError as exc:
        fail(f"imageio-ffmpeg 0.6.0 is not installed: {exc}")

    installed_version = metadata.version("imageio-ffmpeg")
    if installed_version != "0.6.0":
        fail(
            "the Windows runtime must come from the pinned "
            f"imageio-ffmpeg 0.6.0 wheel, found {installed_version}"
        )

    source = Path(imageio_ffmpeg.get_ffmpeg_exe()).resolve()
    if not source.is_file():
        fail(f"imageio-ffmpeg executable not found: {source}")
    if pe_machine(source) != 0x8664:
        fail("the imageio-ffmpeg executable is not Windows x86-64")

    version_output = run(source, "-hide_banner", "-version")
    filters_output = run(source, "-hide_banner", "-filters")
    encoders_output = run(source, "-hide_banner", "-encoders")
    if not re.search(r"\bloudnorm\b", filters_output):
        fail("the FFmpeg binary does not provide the loudnorm filter")
    missing = [
        encoder
        for encoder in REQUIRED_AUDIO_ENCODERS
        if not re.search(rf"\b{re.escape(encoder)}\b", encoders_output)
    ]
    if missing:
        fail("required FFmpeg encoders are missing: " + ", ".join(missing))
    if "--enable-nonfree" in version_output:
        fail("the FFmpeg build is non-free and cannot be redistributed")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    temporary = OUTPUT_FFMPEG.with_suffix(".exe.tmp")
    shutil.copy2(source, temporary)
    temporary.replace(OUTPUT_FFMPEG)

    first_line = version_output.splitlines()[0] if version_output else "unknown"
    configuration = next(
        (line.strip() for line in version_output.splitlines() if "configuration:" in line),
        "configuration: unavailable",
    )
    manifest = {
        "application": f"LUFScale {APP_VERSION}",
        "platform": "Windows x86-64",
        "source_package": "imageio-ffmpeg",
        "source_package_version": installed_version,
        "source_project": "https://github.com/imageio/imageio-ffmpeg",
        "binary_build_project": "https://github.com/imageio/imageio-ffmpeg-builds",
        "ffmpeg_version_line": first_line,
        "ffmpeg_configuration": configuration,
        "binary": OUTPUT_FFMPEG.name,
        "binary_sha256": sha256(OUTPUT_FFMPEG),
        "pe_machine": "0x8664 (AMD64)",
        "required_filter": "loudnorm",
        "required_encoders": list(REQUIRED_AUDIO_ENCODERS),
    }
    OUTPUT_MANIFEST.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    licence_mode = "GPL-compatible" if "--enable-gpl" in configuration else "LGPL"
    OUTPUT_NOTICE.write_text(
        f"LUFScale {APP_VERSION} - bundled FFmpeg for Windows x86-64\n\n"
        f"The executable was supplied by imageio-ffmpeg {installed_version} and "
        "was copied without modification after capability and architecture checks.\n"
        f"FFmpeg reports: {first_line}\n"
        f"Configuration category: {licence_mode}; non-free builds are rejected.\n"
        f"SHA-256: {manifest['binary_sha256']}\n\n"
        "Projects and source/build information:\n"
        "https://ffmpeg.org/\n"
        "https://github.com/imageio/imageio-ffmpeg\n"
        "https://github.com/imageio/imageio-ffmpeg-builds\n\n"
        "See THIRD_PARTY_NOTICES.md, SBOM.cdx.json, the bundled licence files "
        "and FFMPEG_WINDOWS_BUILD_MANIFEST.json.\n",
        encoding="utf-8",
    )
    print(OUTPUT_FFMPEG)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
