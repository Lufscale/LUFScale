# LUFScale 2.1.12 for macOS

This repository is the independent macOS edition of LUFScale. It measures and
normalizes perceived audio loudness while prioritizing a stable final level,
preservation of source files and verification of the result.

## Main features

- **Normalize** re-encodes each file so its physical audio approaches the
  selected LUFS target while respecting the True Peak ceiling.
- **ReplayGain** preserves the audio samples and writes gain tags for
  compatible players.
- **Analyze only** measures files without creating audio output.
- Optional quality control, CSV reports, interrupted-job recovery, fixed-scale
  before/after graphs and an interface in twelve languages. CSV creation and
  automatic start after a drop or paste are off by default.

Supported formats: MP3, FLAC, WAV, AIF, AIFF, M4A, OGG and Opus.

## Licence

The original LUFScale code and documentation are free software distributed
under **GNU GPL-3.0-or-later**. See `LICENSE` and `COPYRIGHT`. Dependencies,
fonts and bundled tools retain their own licences; see
`THIRD_PARTY_NOTICES.md`, `SBOM.cdx.json` and `third_party_licenses`.

## Self-contained application for users

The public package contains `LUFScale.app`. The application bundle already
contains its Python runtime, PySide6/Qt libraries, the verified FFmpeg engine,
required codecs, twelve guides, fonts, licences and notices. An end user does
not install Python, Qt, FFmpeg, Homebrew, MacPorts or another package manager.
After extracting the community ZIP, move `LUFScale.app` to Applications and
open it. See `OPEN_LUFSCALE_ON_MACOS.md` for the unsigned-community Gatekeeper
procedure.

The published build targets Apple Silicon and macOS 12 or later. A native
Intel build and first launch have also succeeded on an Intel Mac. The complete
functional suite must still be repeated on each target architecture before
publication.

## Build the community distribution from source

PyInstaller must build the application on macOS and FFmpeg must be compiled
natively for the target architecture. On the publisher's Mac, extract this
source package completely and double-click:

```text
Create_Community_Distribution_macOS.command
```

This is the only user-facing build launcher at the project root. Files inside
`tools` are implementation components invoked automatically by that launcher.

No prior Python, `pkg-config`, Homebrew or MacPorts installation is required.
The publisher's Mac needs an Internet connection. If the Xcode Command Line
Tools are absent, the launcher requests them through macOS, waits in the same
Terminal window and resumes the build automatically as soon as Apple finishes
the installation. It downloads the pinned uv 0.12.5 bootstrap for the native
Mac architecture, verifies the published SHA-256, and uses uv to place CPython
3.13.15 entirely below `.build-tools`.
Python is not installed in `/Library`, no shell path is modified, and no
administrator password is required for the Python preparation step.

The script then creates an isolated build environment, activates its included
`pkg-config` helper (including LAME 4.0's version probe), generates the twelve
guides, validates the native C ABI before configuring LAME, compiles and
validates FFmpeg, packages Python and
PySide6/Qt, verifies the autonomous bundle, and writes these results to `dist`.
If an upstream configure script fails, its complete log is preserved below
`packaging/generated/build-diagnostics`. Successful results are:

- `LUFScale.app` for local validation;
- `LUFScale-2.1.12-macOS-<architecture>-community.zip` for publication;
- the adjacent `.sha256` checksum.

See `VALIDATION_2.1.12.md` before publication. This community build uses an
ad-hoc internal signature and is neither identified with Apple Developer ID
nor notarized.

## Run from source

```zsh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python app.py
```

Source execution requires a compatible development FFmpeg selected explicitly
or available locally. A released frozen application never falls back to an
external FFmpeg installation.

## Project structure

- `Create_Community_Distribution_macOS.command`: the only build launcher at
  the project root; double-click this file.
- `tools/Internal_Application_Builder_macOS.command`: internal worker called
  automatically by the public launcher; do not run it directly.
- `packaging/macos/LUFScale.spec`: PyInstaller application definition.
- `tools/build_bundled_ffmpeg_macos.py`: verified native FFmpeg source builder.
- the internal bootstrap downloads verified uv 0.12.5 and uses its managed
  `python-build-standalone` distribution only below `.build-tools`;
- `tools/pkg-config` and `tools/pkg_config_lite.py`: private build-only
  `pkg-config` implementation; no Homebrew installation is required.
- `tools/generate_runtime_manifest.py`: exact Python/Qt/FFmpeg build record.
- `output/pdf`: the twelve macOS PDF guides.

This macOS project deliberately contains no Windows builder, installer,
deployment guide or Windows PDF set.
