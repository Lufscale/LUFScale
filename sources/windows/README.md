# LUFScale 2.1.12 for Windows

This repository is the independent Windows edition of LUFScale. It measures
and normalizes perceived audio loudness while prioritizing a stable final
level, preservation of source files and verification of the result.

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

## Installer or portable application for users

Two self-contained Windows packages target x86-64 Windows 11 and Windows 10
version 1809 or later:

- `LUFScale-2.1.12-Setup-x64.exe` installs LUFScale for the current user and
  provides Start menu and optional desktop shortcuts;
- `LUFScale-2.1.12-Portable-x64.exe` is a single portable executable: copy it
  to another compatible computer and launch it directly, without installation.

Both already contain LUFScale, the Python runtime, PySide6/Qt, FFmpeg, required
codecs, guides and licence notices. They download nothing and do not launch a
PowerShell script on the end user's computer. The portable executable unpacks
its private runtime into a temporary directory at launch, so its first opening
can be slower than the installed edition.

After installation, LUFScale is available from the Start menu and can be
removed through Windows **Installed apps**. An optional desktop shortcut can
be selected in the setup wizard. See `OPEN_LUFSCALE_ON_WINDOWS.md`.

The community installer has no commercial code-signing certificate.
SmartScreen may therefore request confirmation after download. Do not disable
Windows security globally; publish the adjacent SHA-256 checksum and source
package with the installer.

## Build the installer from source

PyInstaller must build the application on Windows; it is not a cross-compiler.
On a real x86-64 Windows 10/11 PC, extract the source package completely and
double-click:

```text
Create_Offline_Installer_Windows.cmd
```

This is the only user-facing build launcher at the project root. Files inside
`tools` are implementation components invoked automatically by that launcher.

No Python installation, manual Python selection or manual PowerShell command
is required. The builder always uses its private pinned Python 3.13.15 copy.
When absent, it downloads the official CPython NuGet build package, verifies
its pinned SHA-512 and the extracted Python Software Foundation Authenticode
signature, then extracts it only below the project's `.build-tools` folder.
It does not install Python, change the Windows registry, alter `PATH` or touch
any existing Python installation.
It prepares Inno Setup in the same private folder, creates an isolated Python
environment, validates FFmpeg, generates the twelve guides, packages the
autonomous application, compiles the final offline setup and creates the
portable single-file executable.
The setup language dialog provides the same twelve languages as LUFScale. The
Chinese and current Indonesian message files not bundled with Inno Setup 6.7.3
are downloaded from pinned official source revisions and SHA-256 verified on
the publisher's build computer. The pinned official Hindi 5.5.3 translation is
then modernized with a LUFScale-maintained supplement, filtered against the
installed Inno Setup 6.7.3 `Default.isl`, and rejected if a current message or
placeholder is missing or obsolete. Inno's missing and unrecognized message
warnings remain enabled during compilation.

An Internet connection is therefore required once on the **publisher's build
computer**, but never on the **end user's computer during installation**. The
results are written to `dist`:

- `LUFScale-2.1.12-Setup-x64.exe`;
- `LUFScale-2.1.12-Setup-x64.exe.sha256`;
- `LUFScale-2.1.12-Portable-x64.exe`;
- `LUFScale-2.1.12-Portable-x64.exe.sha256`;
- `LUFScale`, the unpacked application used to create the setup.

See `VALIDATION_2.1.12.md` before publication.

## Run from source

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

Source execution may use the development `imageio-ffmpeg` dependency. The
offline installer builder validates and packages one explicit native x86-64
FFmpeg executable.

## Project structure

- `Create_Offline_Installer_Windows.cmd`: the only build launcher at the
  project root; double-click this file.
- `tools\Internal_Installer_Orchestrator_Windows.ps1`: internal prerequisite
  and setup orchestration called automatically by the public launcher.
- `tools\Internal_Application_Builder_Windows.ps1`: internal autonomous
  application builder. The two PowerShell workers are not user entry points.
- `packaging\windows\LUFScale.iss`: offline Inno Setup definition.
- `packaging\windows\LUFScale.spec`: PyInstaller one-folder definition used by
  the installer.
- `packaging\windows\LUFScale-Portable.spec`: PyInstaller single-file portable
  application definition.
- `tools\prepare_bundled_ffmpeg_windows.py`: native FFmpeg validation and
  distribution-record generator.
- `output\pdf`: the twelve Windows PDF guides.

This Windows project deliberately contains no builders, application bundles,
deployment instructions or guides for another operating system.
