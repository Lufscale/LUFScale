# Generated macOS release records

The native macOS builder generates verified records in this directory.

- `FFMPEG_BUILD_MANIFEST.json` records the native engine and build options.
- `FFMPEG_DISTRIBUTION_NOTICE.txt`, corresponding-source archives and licence
  copies accompany the redistributable FFmpeg build.
- `LUFSCALE_RUNTIME_MANIFEST.json` records the exact Python, PySide6/Qt,
  psutil, PyInstaller and FFmpeg components embedded in `LUFScale.app`.

These generated files are embedded in the application and copied beside it in
the publishable community ZIP.

## Documentation update in 2.2.3

This release integrates the approved twelve-language PDF guides. Audio processing, application controls, language choices and dependency pins are unchanged from 2.2.2. The build verifies the bundled PDFs against `packaging/approved-guides.json` and embeds them without regenerating them. The generator sources remain available for future documentation edits. Native validation of 2.2.3 is pending.
