# LUFScale 2.1.12 Windows open-source distribution

LUFScale 2.1.12 is a maintenance release of the independent Windows edition
distributed through a single-file offline setup. It is free of charge and
distributed under GNU GPL-3.0-or-later.

## Changes in 2.1.12

- On Windows 11, Hindi LUFS ranges no longer rely on DirectWrite's native
  character-background rectangle, which can extend beyond the fixed line when
  Devanagari metrics are active. The range remains selectable native document
  text, while the journal paints its inverse colours inside an explicitly
  fixed and vertically centred rectangle. This dedicated path does not change
  Windows 10 or the other eleven languages.
- The Windows language list now shows a bare check to the left of the active
  language, matching the macOS selector. The marker is painted only inside the
  open popup: the closed field remains unchanged, all twelve languages remain
  available, and the rendering follows the active dark or light palette.
- The processing log is visible again: the first compact text block is now
  detected with the Qt text cursor instead of an unavailable document method.
  Script-aware fixed heights use 16 pixels for Latin rows, 17 pixels for
  Japanese and Korean, 19 pixels for Chinese and 20 pixels for Devanagari.
  LUFS values in every language are native Qt text rather than inline bitmap
  badges. Standard ranges clone the adjacent character format and invert only
  its colours. The Windows 11 Hindi path keeps the same font properties and
  native document text but uses the journal's fixed-height viewport painter so
  DirectWrite cannot enlarge the background. A block margin outside the text
  layout separates consecutive highlights while preserving the established
  total row heights.
  Japanese and Korean runs use their bundled Noto fonts at 11 pixels and
  weight 600.
- Recursive source discovery now ignores macOS AppleDouble metadata sidecars
  whose names begin with `._`. Files such as `._song.mp3` retain an audio
  extension on Windows but contain no audio stream; they are no longer counted
  or passed to FFmpeg. Genuine dot-prefixed audio files remain supported.
- A selected source folder is now the relative root of the output tree rather
  than an extra destination level. Files directly inside it are written
  directly into the chosen destination, while genuine subfolders remain
  preserved. Conflicting relative paths from multiple selected roots receive
  a suffix before the audio extension.
- The lower edge of the source-files panel now uses the same visible neutral
  stroke as the Settings panel instead of inheriting the near-black bevel.
- The official-site address is aligned with the right edge of the loudness
  evolution panel while retaining the muted status-bar typography.
- Page 1 of every localized guide now aligns its four quick-start cards with
  the application illustration. The fourth marker stays circular and the
  complete localized Start label is no longer truncated.
- Every processing-log entry is inserted into an explicitly formatted block.
  Its final pixel is an external bottom margin rather than part of the text
  layout, so adjacent native-text highlights cannot touch.
- Adding accepted sources no longer replaces the permanent localized
  source-safety notice with a temporary source count. A no-new-source warning
  still returns automatically to the permanent notice after its timeout.
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
- The eight automatic-quality-control formula cards now have their own
  calculation-specific explanations in all twelve localized guides instead of
  sharing generic duplicate text. The low-loudness card also shows the
  resulting internal-target update.
- Page 5 of every localized guide now has one technical build appendix for
  Apple Silicon (arm64), Intel Mac (x86_64), and Windows (x64), with the
  correct native builder and outputs for each target.

- The Windows release identity remains synchronized with the macOS 2.1.12
  builder correction. The normalization algorithms are unchanged.
- The single `Create_Offline_Installer_Windows.cmd` entry point requires no
  preinstalled Python and no manual PowerShell command.
- The builder pins the official CPython NuGet 3.13.15 build package, verifies
  its SHA-512 and the extracted Python Software Foundation Authenticode
  signature, and extracts it only below `.build-tools`.
- The build Python is now application-local and registration-free: the builder
  neither installs nor uninstalls Python, does not read or write Python registry
  keys and is unaffected by an incomplete Python MSI registration left by an
  earlier build attempt.
- Each build recreates its isolated Python environment before installing the
  pinned build dependencies, so a partial previous environment is not reused.
- Inno Setup is also prepared automatically in the private build-tools folder;
  its Authenticode signature must be valid and identify the current official
  publisher, Pyrsys B.V. The finished setup remains offline and performs no
  end-user download.
- The same builder now also creates
  `LUFScale-2.1.12-Portable-x64.exe`, a self-contained single-file application
  that can be copied to another compatible computer and launched without
  installation, plus its SHA-256 file.
- CSV report creation and automatic start after a drop or paste are now off on
  a fresh installation. Existing saved user choices remain unchanged.
- The public source tree and archive are rebuilt from a clean staging tree.
- Local validation environments, bytecode caches, generated previews,
  incomplete download fragments and unrelated workspace metadata are excluded.
- Version records, the CycloneDX SBOM, installer definition and all twelve
  localized PDF guides use the 2.1.12 identity.
- The autonomous runtime and audio processing remain unchanged from the
  validated 2.1 series: the offline setup carries LUFScale, Python,
  PySide6/Qt, FFmpeg, codecs, guides and notices without an end-user download.

## Validation boundary

Static, translation, packaging and PDF checks are included. The final setup
must be produced and functionally validated on a real Windows x86-64 computer.
This source package does not claim that an untested installer is ready for
public deployment.
