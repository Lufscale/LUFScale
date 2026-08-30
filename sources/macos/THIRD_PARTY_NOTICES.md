# LUFScale 2.1.12 for macOS - third-party notices

This inventory accompanies the GPL-3.0-or-later LUFScale source and binary
packages. It must remain with every binary distribution. Original LUFScale
code and documentation are licensed by Perez Philippe; third-party components
retain the terms stated below.

| Component | Version | Licence | Upstream |
|---|---:|---|---|
| Python runtime (CPython, portable Astral build) | 3.13.15 | PSF License Agreement | https://github.com/astral-sh/python-build-standalone |
| uv bootstrap, build only | 0.12.5 | Apache-2.0 OR MIT | https://github.com/astral-sh/uv/releases/tag/0.12.5 |
| PySide6 Essentials / Qt for Python | 6.8.3 | LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only | https://code.qt.io/cgit/pyside/pyside-setup.git/ |
| Qt | 6.8.3 family | Commercial or LGPL-3.0/GPL-3.0 according to the selected terms | https://doc.qt.io/qt-6/licensing.html |
| psutil | 7.2.2 | BSD-3-Clause | https://github.com/giampaolo/psutil |
| FFmpeg, native macOS source build | 7.1.5 | LGPL-2.1-or-later for the generated configuration | https://ffmpeg.org/releases/ffmpeg-7.1.5.tar.xz |
| LAME / libmp3lame | 4.0 | LGPL-2.0-or-later | https://downloads.sourceforge.net/project/lame/lame/4.0/lame-4.0.tar.gz |
| libogg | 1.3.6 | BSD-3-Clause | https://ftp.osuosl.org/pub/xiph/releases/ogg/libogg-1.3.6.tar.gz |
| libvorbis | 1.3.7 | BSD-3-Clause | https://ftp.osuosl.org/pub/xiph/releases/vorbis/libvorbis-1.3.7.tar.xz |
| Opus / libopus | 1.6.1 | BSD-3-Clause | https://ftp.osuosl.org/pub/xiph/releases/opus/opus-1.6.1.tar.gz |
| Noto Sans JP/SC/KR/Devanagari | bundled | SIL Open Font License 1.1 | https://github.com/notofonts |
| DejaVu Sans / Serif | 2.37, bundled for guide generation | Bitstream Vera licence; DejaVu changes are public domain | https://dejavu-fonts.github.io/ |

Licence texts for the Python dependencies and fonts are stored in
`third_party_licenses` or beside the font files.

## Embedded runtime record

`LUFSCALE_RUNTIME_MANIFEST.json` is generated for every native application
build. It records the exact Python, PySide6/Qt, psutil and PyInstaller versions,
the target architecture, and the SHA-256 of the embedded FFmpeg executable.
The record states explicitly that no external end-user runtime is required.

## FFmpeg distribution record

The macOS builder compiles FFmpeg 7.1.5 from pinned archives with LAME,
libogg, libvorbis and Opus linked statically. It rejects GPL and non-free
configuration switches and creates `FFMPEG_BUILD_MANIFEST.json`, exact source
archives, distribution notices and extracted licence copies. See the official
FFmpeg redistribution checklist: https://ffmpeg.org/legal.html.

## Qt / PySide distribution record

Qt documents commercial and open-source alternatives. A redistributor using
the LGPL option must preserve notices and permit replacement or relinking of
the LGPL libraries under the applicable terms. Qt publishes licensing and
third-party information, including SPDX SBOM data, at
https://doc.qt.io/qt-6/licensing.html. LUFScale provides the complete
application source and native macOS build scripts.

## Build-only components

PyInstaller 6.21.0 and ReportLab 4.4.3 build the native application and PDF
guides. They are used in the publisher's isolated environment. The builder
downloads the architecture-specific uv 0.12.5 archive, verifies its published
SHA-256 and uses uv's managed `python-build-standalone` distribution to place
CPython 3.13.15 only below `.build-tools`. It never invokes the system Python
installer. LUFScale's GPL-licensed build-local `pkg-config` helper reads the
generated `.pc` metadata without requiring Homebrew. PyInstaller packages
Python and Qt into `LUFScale.app`; no separate runtime is required by end users.
