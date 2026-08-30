# LUFScale 2.1.12 macOS validation

Source validation date: August 23, 2026.

## Automated and platform-neutral checks

- Python syntax compilation for the application, tools and tests;
- regression tests for audio commands, quality thresholds, translations,
  licences, versioning and macOS-only package records;
- checks that the first processing-log block is detected through the Qt text
  cursor, remains visible, and has a fixed 16-pixel line height with zero top
  and bottom margins;
- checks that Japanese and Chinese use the same compact 16-pixel line box and
  15-pixel inverse-colour LUFS badge as the validated French reference; the
  CJK badge is raised by two pixels to preserve the next line's glyphs while
  retaining exactly one separator pixel between consecutive backgrounds;
- checks that the status-bar address uses the source-safety message's muted
  colour, 12-pixel type size and regular weight;
- checks that every PDF footer prints `https://lufscale.net` at the right and
  that the free-software card appears on page 1 rather than page 5;
- checks that page 1 restores both macOS distribution bullets, aligns the four
  quick-start cards with the interface image and preserves the complete
  localized Start label beside a circular marker;
- checks that the official `https://lufscale.net` link remains visible in the
  status bar, localized for accessibility, present in the Version dialog and
  connected to the operating system's default-browser service;
- generation, metadata inspection and rendering of twelve localized macOS PDF
  guides using the fonts supplied in `assets/fonts`;
- checks that the macOS spec embeds one explicit FFmpeg binary, Python/Qt
  resources, guides, licences and the exact runtime manifest;
- checks that a frozen release cannot use an external FFmpeg fallback;
- checks that the builder pins uv 0.12.5 and both native macOS SHA-256 values,
  requires an uv-managed CPython 3.13.15 below `.build-tools`, contains no
  `sudo` or macOS package installation, and activates the private `pkg-config`;
- checks that the LAME 4.0 configure step first validates the native LP64 ABI,
  seeds all ten required Autoconf size values and preserves a complete
  `config.log` after any configure failure;
- tests both accepted forms of LAME's `--atleast-pkgconfig-version` probe and
  confirms that `--exists --print-errors` returns promptly for a missing
  optional package;
- isolated tests of the private `pkg-config` dependency and static-link flag
  resolution;
- checks that Windows builders, package definitions, deployment documents and
  generated Windows guides are absent;
- checks that public file names and text contain only project-relevant release
  content and that caches, validation environments, generated previews and
  download fragments are absent from the source archive;
- CycloneDX SBOM JSON validation and source archive checksum verification.

## Required checks on target macOS hardware

1. Build with `Create_Community_Distribution_macOS.command` on an Apple Silicon
   Mac running macOS 12 or later with no Python, Homebrew or `pkg-config`
   installation. Confirm first that it is the only `.command` file at the
   project root. If macOS requests the Xcode Command Line Tools, complete that
   installation while leaving Terminal open and confirm that the same builder
   resumes automatically.
   Confirm that Python preparation itself requests no administrator password
   and creates its managed runtime only below `.build-tools`.
2. Confirm that `dist/LUFScale.app`, the community ZIP and its SHA-256 checksum
   are produced.
   In the Terminal, confirm that `lame-abi-check` completes before LAME is
   configured. If configuration still fails, attach
   `packaging/generated/build-diagnostics/lame-config.log` to the report.
3. Review the build size report and `LUFSCALE_RUNTIME_MANIFEST.json`; verify the
   embedded Python 3.13.15, PySide6/Qt and FFmpeg versions and architecture.
4. Temporarily remove Python, FFmpeg, Homebrew and MacPorts from the interactive
   shell `PATH`, then launch `LUFScale.app` from Finder.
5. Test Normalize, ReplayGain and Analyze only with MP3, FLAC, WAV, AIFF, M4A,
   OGG and Opus files.
6. Verify before/after graphs, warnings, CSV output, skipped existing files,
   pause, resume, cancel, close confirmation and clean relaunch.
7. Inspect the packaged FFmpeg filters and encoders and verify that its Mach-O
   dependencies are limited to Apple system libraries.
8. Verify the application and FFmpeg with `file` and `codesign --verify --deep
   --strict`.
9. Test extraction and launch from short ASCII, Unicode and long paths.
10. Test the downloaded ZIP with Gatekeeper enabled and verify SHA-256.
11. Confirm that every PDF guide and licence opens from the packaged app.
12. Monitor the application with networking disabled and confirm that normal
    launch and audio processing require no download.
13. With networking restored, click `https://lufscale.net` in the status bar,
    confirm that the default browser opens the official site, and verify that
    the Version dialog lists the same address before the GPL information.
14. Process the same file set in French, Japanese, Hindi, Chinese and Korean.
    Confirm that every result is visible in the log, that the log keeps the
    same compact line spacing in every language, and that accents, CJK glyphs
    and Devanagari marks are not clipped.

An Intel build may only be produced natively on an Intel Mac. One native Intel
build and first launch have succeeded, but it must not be advertised as fully
validated without completing the same functional suite on Intel hardware.
