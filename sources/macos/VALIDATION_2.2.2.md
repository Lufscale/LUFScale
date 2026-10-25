# LUFScale 2.2.2 validation

Validation performed on a Linux host with Python 3.12, Qt 6.8.3 and FFmpeg 6.1.1.

- 62 automated tests passed for the macOS source package, including independent resizing of all error columns, mislabeled WebP repair, unchanged original/audio payload, invalid loudness rejection, and failure-safe delivery/recovery. Missing macOS volumes are rejected.
- The actual macOS worker was exercised on 14 supplied MP3s: all seven affected Clan Destine tracks, the three abnormal Rhapsody in White tracks, and one previously failing track from each of Songstress, Rhythm Of Love, Rapture and Kryptos.
- Eleven conversions succeeded and passed loudness/true-peak QC at a -14 LUFS target. All seven repaired covers were retained as PNG. Original file SHA-256 values were unchanged.
- The three Rhapsody in White tracks were rejected with explicit invalid-measurement errors and no output written. Their damaged audio was not repaired.
- A simulated delivery I/O failure preserved the completed local result and the pre-existing destination, and stopped the worker.
- macOS launcher shell syntax checked. The twelve guides were regenerated for this version on each platform.

Limitations: these are source-level tests, not native macOS/Windows builds. Physical unplugging, Finder/Explorer icon display and native executable packaging were not tested here. Linux FFmpeg was used for the audio corpus on both editions. Storage failures must still be diagnosed on the user's machine.

## Distribution audit

The build and installation documentation is in English. Each of the twelve application languages retains its dedicated PDF guide. Application source files and the twelve PDFs match the previously delivered 2.2.2 package byte for byte. Windows Setup uses English only. Superseded release notes have been removed. Dependency versions and licence notices are preserved.

The distribution audit passed 62 macOS tests and 50 Windows tests on Linux. PDF text was checked for the 2.2.2 release reference. Native builds remain to be validated on their target systems.

## Build correction validation

The original macOS PyInstaller input validation was reproduced failing with twelve guides. The corrected definitions accept the complete guide set and reject missing, empty or unexpected PDFs. The macOS suite passes 66 tests and the Windows suite passes 54 tests on Linux. The three PyInstaller definitions and macOS shell syntax were checked. Native executable compilation remains to be verified on macOS and Windows.
