# LUFScale release history

## 2.2.2 — Artwork, errors and result protection

- File, Path and Details error columns can be resized independently.
- MP3 artwork is identified by its actual format; WebP images mislabeled as JPEG are repaired on a working copy, preserving the originals.
- Abnormal audio measurements are rejected before normalization; unreadable artwork produces an explicit error instead of being silently removed.
- Completed results are created locally before transfer. A failed transfer stops processing and retains completed, undelivered files with their recovery paths in the log.
- A missing Mac volume no longer causes its folder to be recreated under /Volumes.

## 2.2.1 — Build progress and package presentation

- Version 2.1.13 was renamed 2.2.1.
- Each build stage has its own progress bar; completed stages remain visible, with elapsed time and activity details, especially during FFmpeg compilation.
- “Activity detected” and “No new messages for Xs” indicate activity. Full logs are retained, with a short diagnostic on failure.

## 2.1.13 — Initial audio corrections

- AppleDouble files beginning with ._ and the contents of __MACOSX are ignored without being reported as audio errors; processing continues.
- The macOS FFmpeg build supports PNG artwork, resolving the investigated -22 error. Both Mac and Windows builds check artwork support.

Earlier releases remain available in [GitHub Releases](https://github.com/Lufscale/LUFScale/releases).
