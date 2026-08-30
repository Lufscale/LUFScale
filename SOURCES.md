# LUFScale 2.1.12 source code

## Repository structure

The macOS and Windows editions of LUFScale 2.1.12 are stored in two independent directories. This organization reflects the source trees that were actually used to build the distributed packages.

| Directory | Contents |
|---|---|
| `sources/macos` | LUFScale code, macOS build tools, PyInstaller definition, release metadata, licenses and notices |
| `sources/windows` | LUFScale code, Windows build tools, PyInstaller and Inno Setup definitions, licenses and notices |

Generated PDF guides and build outputs are not tracked in Git. The scripts included with each edition recreate them during the build.

## Compliance archives

Archives attached to a GitHub release remain the reference packages when third-party corresponding source code must accompany a specific distributed executable.

The macOS 2.1.12 archive includes the corresponding source code for FFmpeg 7.1.5, LAME 4.0, Opus 1.6.1, libogg 1.3.6 and libvorbis 1.3.7 used by its builder.

## Required correction before publishing the Windows package

The currently prepared Windows 2.1.12 executable contains a static FFmpeg 7.1 build configured with `--enable-gpl` and several linked third-party libraries. The current Windows archive contains the LUFScale source code, build scripts, notices and links to upstream projects, but it does not contain all corresponding source code for that specific FFmpeg binary and its linked libraries.

The Windows package must therefore not be presented as a complete compliance archive until the corresponding source code and exact build information have been added, or until FFmpeg has been rebuilt from a controlled source set archived with the release.

This requirement does not change the license of the original LUFScale code, which remains GNU GPL-3.0-or-later.
