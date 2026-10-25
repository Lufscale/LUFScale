# LUFScale 2.2.2

- Error list: all three columns can be resized independently, with horizontal scrolling for wide content.
- MP3 artwork: detect the actual embedded image format. Correct mislabeled JPEG/PNG images; convert other readable image formats, including WebP, to PNG on a private working copy. Preserve originals and all attached pictures. Unreadable artwork produces a clear error rather than silently removing it.
- Reject out-of-range/non-finite loudness measurements before normalization, including cached measurements. Silent audio remains supported. Damaged audio is not claimed to be repaired.
- Build outputs in a local per-track recovery directory, then copy, flush and atomically replace at the destination. A delivery failure stops the batch. Completed undelivered outputs are retained; the error log gives their exact recovery path and each directory contains destination.json.
- A missing macOS /Volumes mount is not recreated on the internal disk. No automatic retry or automatic overwrite of recovered output is attempted.
- Existing language choices, AppleDouble filtering, PNG support, build progress bars and executable icon checks are retained. English remains the default for new installations.

Local staging requires enough free space for concurrent outputs and any artwork-repaired source copies. Incomplete outputs are removed; completed outputs retained after failure remain until the user retrieves or deletes them. Cancellation may retain completed but undelivered output as well.

These are source/build packages. Native macOS and Windows compilation and visual validation must be performed on the target operating systems.

## Distribution language

Installation, build messages and release documentation use English. Windows Setup uses English only. The twelve interface languages remain available inside the application; each language opens its dedicated translated PDF guide. Superseded release documents are excluded from this package.

## Build correction

The macOS PyInstaller definition now accepts the complete multilingual PDF guide set instead of requiring a single English guide. The macOS and both Windows definitions validate guide names and reject missing, empty or unexpected PDFs before packaging. Interface translations, PDF contents and audio processing are unchanged.
