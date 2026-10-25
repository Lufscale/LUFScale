# LUFScale 2.2.3 for macOS - validation

Prepared on 2026-10-25. Native test results reported by the maintainer are recorded below.

## Completed source checks

- 72 automated tests passed on Linux with Python 3.12 and Qt 6.8.3, including the existing regression suite and six approved-guide integrity tests.
- Runtime source compared against 2.2.2: only application version and version references in guide/build translations changed. Audio processing and UI behavior code remain byte-for-byte identical.
- Dependency requirements and native build dependency pins remain unchanged.
- All twelve PDFs have the same page counts and extracted text as the approved documentation, except that 2.2.2 references become 2.2.3. French opening, technical and formula pages were rendered and visually checked.
- The builder verifies each PDF against SHA-256 hashes before packaging. Missing, extra, changed and wrong-version guide sets are rejected.
- Application resource mappings and PyInstaller definitions include one guide per supported language.
- Release version, output names and package metadata are 2.2.3.
- macOS launcher and worker shell syntax checked with zsh.

## Native test checklist for future builds

Build this kit on macOS. Confirm that the resulting application displays 2.2.3, opens the updated local PDF through Help in each language, preserves saved settings and processes representative supported audio files. Exercise Normalize, Analyze only and ReplayGain on formats supported by those operations.
Build and test separately on Apple Silicon and Intel. Check the application inside the generated community ZIP, not only the local build directory.

The checklist describes recommended checks for future builds. The maintainer has reported successful native tests for the supplied release executables; the exact test coverage and signatures were not independently audited on this preparation host. No release or website publication has been performed during preparation.

## Native validation reported by the maintainer

On 2026-10-25, the maintainer reported successful tests on Windows 10, Windows 11, Intel Mac and Apple Silicon Mac and supplied the resulting executables and SHA-256 files. The publication preparation checked archive integrity, the supplied SHA-256 values and all twelve embedded PDF guides per platform against the approved guide manifest. The native test report is supplied by the maintainer, not a native execution performed on the preparation host.
