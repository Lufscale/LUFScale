# LUFScale 2.1.12 macOS open-source distribution

LUFScale 2.1.12 is a maintenance release of the independent, self-contained
macOS edition. It is free of charge and distributed under GNU
GPL-3.0-or-later.

## Changes in 2.1.12

- The processing log is visible again: the first compact text block is now
  detected with the Qt text cursor instead of an unavailable document method.
  The fixed 16-pixel line height therefore works for Latin, CJK and
  Devanagari text without interrupting log rendering.
- The Japanese and Chinese processing logs now match the validated French
  geometry: a compact 16-pixel line box containing a 15-pixel inverse-colour
  LUFS badge and one external separator pixel. The CJK badge is raised by two
  pixels so its lower edge cannot cover the next line's glyphs, without
  changing the badge font, weight or colours.
- The official-site address is aligned with the right edge of the loudness
  evolution panel while retaining the muted status-bar typography.
- Page 1 of every localized guide restores the Apple Silicon/Intel validation
  boundary and the complete bundled-runtime description in the main-features
  card. Its four quick-start cards now align with the application illustration;
  the fourth marker stays circular and the complete localized Start label is
  no longer truncated.
- Every processing-log entry is now inserted into an explicitly formatted
  block with a fixed 16-pixel line height and zero paragraph margins. This
  also constrains mixed Latin/CJK and Latin/Devanagari lines.
- The official-site link in the status bar now uses the same font, size,
  weight and muted colour as the source-safety message at the left.
- Every localized PDF page now shows `https://lufscale.net` at the lower right
  in the same footer style. The free-software and redistribution card moves
  from page 5 to page 1, immediately below the introductory purpose card.
- The status bar now keeps `https://lufscale.net` visible at its lower-right
  edge. The compact muted-colour link opens the official site in the default
  browser, underlines only on hover, and has a localized tooltip.
- The Version dialog also identifies the official site immediately before the
  GPL licence information.
- A complete public-content review now covers source files, documents, guides,
  metadata and filenames before publication.
- All twelve localized guides now explain that, after the Xcode Command Line
  Tools installation, the open builder resumes automatically and must not be
  launched a second time.
- Page 5 of every localized guide now has one technical build appendix for
  Apple Silicon (arm64), Intel Mac (x86_64), and Windows (x64), with the
  correct native builder and outputs for each target.
- The eight automatic-quality-control formula cards now have their own
  calculation-specific explanations instead of sharing generic duplicate
  text. The low-loudness card also shows the resulting internal-target update.

- The private `pkg-config` helper now accepts LAME 4.0's two-argument
  `--atleast-pkgconfig-version 0.20` probe as well as the equivalent `=` form.
  Informational options such as `--print-errors` also advance correctly, so a
  missing optional package is reported instead of stalling the configure step.
- Before configuring LAME 4.0, the builder now compiles and runs a native ABI
  probe with the selected Apple SDK, architecture and deployment target.
- The verified LP64 type sizes are supplied to LAME's Autoconf cache so its
  fragile `sizeof` probes cannot incorrectly return zero and abort with exit
  status 1.
- Compiler-related environment variables are sanitized to prevent Homebrew,
  MacPorts, user `config.site` files or inherited make flags from changing the
  self-contained build.
- A failed configure step now copies its complete `config.log` to
  `packaging/generated/build-diagnostics` for a persistent, actionable report.
- The single `Create_Community_Distribution_macOS.command` entry point no
  longer requires Python, Homebrew or `pkg-config` to be installed beforehand.
- The builder pins uv 0.12.5, verifies the published architecture-specific
  SHA-256, and uses its managed `python-build-standalone` distribution to place
  CPython 3.13.15 entirely below `.build-tools`.
- Python preparation no longer invokes `sudo`, writes to `/Library`, modifies
  the shell path or requires an administrator password.
- A build-local `pkg-config` implementation replaces the previous Homebrew
  prerequisite. Missing Xcode Command Line Tools are requested through macOS;
  the builder now waits for Apple to finish and resumes automatically instead
  of requiring a second launch.
- CSV report creation and automatic start after a drop or paste are now off on
  a fresh installation. Existing saved user choices remain unchanged.
- A native Intel build and first application launch have succeeded. Complete
  functional validation on Intel hardware remains required before publication.
- The public source tree and archive are rebuilt from a clean staging tree.
- Local validation environments, bytecode caches, generated previews,
  incomplete download fragments and unrelated workspace metadata are excluded.
- Version records, the CycloneDX SBOM, packaging definitions and all twelve
  localized PDF guides use the 2.1.12 identity.
- The autonomous application runtime, audio processing and quality-control behaviour remain
  unchanged from the validated 2.1 series: the published `LUFScale.app` embeds
  Python, PySide6/Qt and one verified native FFmpeg engine.

## Validation boundary

Static, translation, packaging and PDF checks can run on another platform. The
final application must be built and functionally validated on a real Mac of
the target architecture. This source package does not claim that an unbuilt or
untested macOS bundle is ready for public deployment.
