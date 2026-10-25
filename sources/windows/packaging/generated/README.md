# Generated Windows release records

The Windows builder validates the pinned imageio-ffmpeg x86-64 executable and
stores its hash, reported version, configuration and distribution notice in
`windows-x86_64`.

These generated files are embedded in the autonomous Windows application,
which is then carried unchanged by the single-file offline installer.

## Documentation update in 2.2.3

This release integrates the approved twelve-language PDF guides. Audio processing, application controls, language choices and dependency pins are unchanged from 2.2.2. The build verifies the bundled PDFs against `packaging/approved-guides.json` and embeds them without regenerating them. The generator sources remain available for future documentation edits. Native validation of 2.2.3 is pending.
