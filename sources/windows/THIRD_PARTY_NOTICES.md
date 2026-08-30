# LUFScale 2.1.12 for Windows - third-party notices

This inventory accompanies the GPL-3.0-or-later LUFScale Windows source and
binary packages. It must remain with every binary distribution. Original
LUFScale code and documentation are licensed by Perez Philippe; third-party
components retain the terms stated below.

| Component | Version | Licence | Upstream |
|---|---:|---|---|
| Python runtime | 3.13.15 | PSF License Agreement | https://www.python.org/downloads/release/python-31315/ |
| PySide6 Essentials / Qt for Python | 6.8.3 | LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only | https://code.qt.io/cgit/pyside/pyside-setup.git/ |
| Qt | 6.8.3 family | Commercial or LGPL-3.0/GPL-3.0 according to the selected terms | https://doc.qt.io/qt-6/licensing.html |
| psutil | 7.2.2 | BSD-3-Clause | https://github.com/giampaolo/psutil |
| imageio-ffmpeg | 0.6.0 | BSD-2-Clause for the Python wrapper/build distribution | https://github.com/imageio/imageio-ffmpeg |
| FFmpeg Windows runtime | version and configuration recorded at build time | LGPL-2.1-or-later or GPL-compatible according to configuration; non-free builds are rejected | https://ffmpeg.org/ |
| Noto Sans JP/SC/KR/Devanagari | bundled | SIL Open Font License 1.1 | https://github.com/notofonts |
| DejaVu Sans / Serif | 2.37, bundled for deterministic PDF generation | Bitstream Vera licence; DejaVu changes are public domain | https://dejavu-fonts.github.io/ |
| Inno Setup installer engine | 6.7.3 | Inno Setup License | https://jrsoftware.org/files/is/license.txt |

Licence texts for Python dependencies and fonts are stored in
`third_party_licenses` or beside the font files.

## FFmpeg distribution record

The builder installs the pinned native `imageio-ffmpeg==0.6.0` wheel, locates
its x86-64 `ffmpeg.exe`, and copies it without modification only after checking
the PE architecture, `loudnorm`, every encoder advertised by LUFScale, and the
absence of `--enable-nonfree`. The generated
`FFMPEG_WINDOWS_BUILD_MANIFEST.json` records the executable SHA-256, reported
FFmpeg version, configuration category and source/build projects.
`FFMPEG_WINDOWS_DISTRIBUTION_NOTICE.txt` accompanies the executable.

The imageio projects publish wrapper source and binary-build recipes at:

- https://github.com/imageio/imageio-ffmpeg
- https://github.com/imageio/imageio-ffmpeg-builds

Redistributors must review the recorded FFmpeg configuration and fulfil the
corresponding LGPL/GPL source and notice obligations. LUFScale is
GPL-3.0-or-later, but this does not waive any third-party requirement.

## Qt / PySide distribution record

Qt documents commercial and open-source alternatives. A redistributor using
the LGPL option must preserve notices and permit replacement or relinking of
the LGPL libraries under the applicable terms. Qt publishes licensing and
third-party information, including SPDX SBOM data, at
https://doc.qt.io/qt-6/licensing.html. LUFScale uses a visible one-folder
layout and provides the complete application source and build scripts.

## Build-only component

PyInstaller 6.21.0 builds the native application on Windows. It is not a
cross-compiler. Build tools and the isolated Python environment are not
required by end users. Inno Setup 6.7.3 compiles the single-file setup; its
compiler is build-only, while its setup and uninstall engine are carried by
the generated installer under the Inno Setup License.
