# LUFScale 2.1.12 Windows validation

Source validation date: August 26, 2026.

## Automated checks

- checks that only Hindi LUFS ranges on Windows 11 use the journal's
  fixed-height, vertically centred viewport overlay instead of DirectWrite's
  unbounded character background. The underlying range remains selectable
  native text; Windows 10 and all other languages retain their previous path;
- checks that the dedicated Windows language selector paints one bare check
  beside its current item only in the popup list, leaves the closed field
  unchanged and retains all twelve localized choices;
- Python syntax compilation for the application, Windows tools and tests;
- regression tests for audio commands, quality thresholds, translations,
  licences, versioning and Windows packaging records;
- checks that the first processing-log block is detected through the Qt text
  cursor and remains visible. Latin rows use a fixed 16-pixel height, Japanese
  and Korean use 17 pixels, and Chinese and Devanagari use 19 and 20 pixels.
  Every localized LUFS range is inserted as native Qt document text, never as
  a bitmap. Standard ranges invert the cloned adjacent format directly. On
  Windows 11 only, Hindi uses the same font properties in a fixed-height
  viewport overlay because DirectWrite can paint the native character
  background outside the paragraph box. The reserved block margin keeps
  consecutive highlights separated. Japanese and Korean runs continue to use
  bundled Noto faces at 11 pixels and weight 600;
- checks that macOS AppleDouble sidecars such as `._song.mp3` and
  `._sample.wav` are rejected both as direct inputs and during recursive
  discovery, while a genuine dot-prefixed audio file remains accepted;
- checks that a selected source folder is treated as the relative-tree root:
  files directly inside it are written directly into the chosen destination,
  genuine subfolders are preserved, and the selected folder's own name is not
  recreated. Multiple roots with the same relative file path receive a suffix
  before the audio extension instead of targeting the same output;
- checks that accepted sources never replace the permanent source-safety
  notice with a temporary count;
- checks that the status-bar address uses the source-safety message's muted
  colour, 12-pixel type size and regular weight;
- checks that every PDF footer prints `https://lufscale.net` at the right and
  that the free-software card appears on page 1 rather than page 5;
- checks that the four page-1 quick-start cards align with the interface image
  and preserve the complete localized Start label beside a circular marker;
- checks that the official `https://lufscale.net` link remains visible in the
  status bar, localized for accessibility, present in the Version dialog and
  connected to the operating system's default-browser service;
- generation and rendering of twelve localized Windows PDF guides;
- PDF generation uses bundled DejaVu Sans, DejaVu Sans Bold and DejaVu Serif
  files and has no dependency on Linux or Windows system font directories;
- the Windows builder recreates `output\pdf`, stops immediately when the PDF
  generator fails and validates that exactly twelve guides were produced;
- PowerShell structure checks, PyInstaller one-folder and one-file checks, and
  static Inno Setup checks;
- PowerShell file-count checks always wrap `Get-ChildItem` results in `@(...)`
  so zero, one or several matches expose a reliable `Count` property under
  strict mode;
- checks that the official CPython NuGet 3.13.15 build package is downloaded to
  a private project folder and is accepted only after SHA-512, Authenticode,
  exact-version and x86-64 validation;
- checks that the Python package is extracted without invoking Windows
  Installer, reading or writing Python registry keys, or touching another
  Python installation, even if an earlier MSI registration is incomplete;
- checks that every run recreates the isolated Python build environment;
- checks that Inno Setup receives one explicitly quoted argument string,
  including installation paths containing spaces, and writes its installer log
  beside the verified download;
- checks that the downloaded Inno Setup 6.7.3 executable has a valid
  Authenticode signature whose certificate subject starts with the official
  publisher identity `CN=Pyrsys B.V., O=Pyrsys B.V.`;
- checks that the setup language dialog is enabled and contains exactly the
  application's twelve languages. The additional Chinese and current
  Indonesian Inno message files are pinned to official source revisions and
  accepted only after SHA-256 verification. The pinned official legacy Hindi
  file is completed by a maintained supplement, filtered to the exact current
  `Default.isl` message set, and rejected if any name or placeholder is missing,
  obsolete or incompatible; both Inno message warning classes remain enabled;
- the setup definition includes the complete autonomous application tree,
  Start menu entries, an optional desktop icon and a Windows uninstaller;
- the setup definition contains no downloader, URL or custom network code;
- checks that the FFmpeg preparer requires PE x86-64, rejects non-free builds
  and validates `loudnorm` plus every advertised audio encoder;
- checks that no non-Windows builder, deployment guide or package definition
  is present;
- checks that public file names and text contain only project-relevant release
  content and that caches, validation environments, generated previews and
  download fragments are absent from the source archive;
- CycloneDX SBOM JSON validation and source archive checksum verification.

## Required checks on Windows x86-64 hardware

1. Double-click `Create_Offline_Installer_Windows.cmd` on a clean publisher
   computer without Python or Inno Setup and verify that the portable Python
   3.13.15 package and Inno Setup are prepared automatically below
   `.build-tools`.
   Confirm first that it is the only `.cmd` file and that no `.ps1` file is
   present at the project root.
2. Confirm that `dist\LUFScale-2.1.12-Setup-x64.exe`,
   `dist\LUFScale-2.1.12-Portable-x64.exe` and both SHA-256 files are produced
   and that their sizes are plausible for the complete payload.
3. Start the setup and confirm that its language dialog offers English, French,
   Spanish, Italian, Portuguese, Russian, Japanese, Hindi, Simplified Chinese,
   Korean, Indonesian and Turkish. Then install for a standard user from short
   ASCII, Unicode and long paths.
4. Launch from the Start menu without a global Python or FFmpeg installation.
5. Test Normalize, ReplayGain and Analyze only with MP3, FLAC, WAV, AIFF, M4A,
   OGG and Opus files.
6. On a fresh profile, confirm that CSV creation and automatic start after a
   drop or paste are off. Then enable them and verify graphs, warnings, CSV
   output, skipped files, pause, resume, cancel, close confirmation and clean
   relaunch.
7. Inspect the installed FFmpeg version, filters and encoders.
8. Install 2.1.12 over an earlier per-user LUFScale version and confirm settings
   and application launch.
9. Uninstall from **Installed apps** and confirm that installed program files
   and shortcuts are removed without deleting user-created audio outputs.
10. Test the downloaded setup with SmartScreen enabled and verify SHA-256.
11. Confirm that every PDF guide and licence opens from the installed app.
12. Copy the portable executable alone to a second clean computer with no
    Python or FFmpeg installation. Launch it directly and repeat the supported
    format, PDF guide and relaunch checks.
13. Monitor setup and portable launch with Windows networking disabled and
    confirm that neither requests nor attempts a download.
14. With networking restored, click `https://lufscale.net` in the status bar,
    confirm that the default browser opens the official site, and verify that
    the Version dialog lists the same address before the GPL information.
15. Process the same file set in French, Japanese, Hindi, Chinese and Korean.
    Confirm that every result is visible in the log, that the log keeps the
    same compact rhythm in every language, that a narrow background-colour gap
    remains visible between consecutive LUFS highlights, that the inverted LUFS
    values use the same typography as the text immediately before and after,
    and that accents, CJK glyphs and Devanagari marks are not clipped or
    superimposed.
16. Recursively add a folder copied from macOS that contains real audio files
    and matching `._` AppleDouble sidecars. Confirm that only the real files
    are counted and that no FFmpeg error is reported for a `._` name.
17. Add a folder containing one audio file at its root and another inside a
    subfolder. Choose a separate destination and confirm that the root file is
    written directly into that destination, the real subfolder is preserved,
    and the selected source folder name is not inserted between them.
18. Open the language selector in both dark and light themes on Windows 10 and
    Windows 11. Confirm that exactly one bare check appears to the left of the
    active language, that it follows every language change, and that no check
    appears in the closed selector field.
19. On Windows 11 at 100%, 125%, 150% and 200% display scaling, process Hindi
    entries that begin with Devanagari text and contain an inverse-colour LUFS
    range. Confirm that every background remains inside its own row and that
    the text family, size and weight match the adjacent Latin text. Repeat one
    Hindi run on Windows 10 to confirm the previously validated path is
    unchanged.

Windows 11 is the recommended release platform. If Windows 10 compatibility is
advertised, repeat the functional suite on version 1809 or later and record the
exact build number.
