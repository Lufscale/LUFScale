# Open the LUFScale 2.1.12 community distribution on macOS

## No additional runtime installation

The published `LUFScale.app` is self-contained. It includes Python,
PySide6/Qt, FFmpeg, the required audio codecs, guides, fonts and licence
notices. End users must not install Python, FFmpeg, Homebrew, MacPorts or any
other runtime for LUFScale.

The published community application targets **Apple Silicon Macs** running
macOS 12 or later. A native Intel `x86_64` build and first launch have also
succeeded on an Intel Mac. Complete functional validation is still required
before either architecture is published.

## Open the unsigned community application

The community distribution has no Apple Developer ID identity and is not
notarized. macOS can therefore report that the developer cannot be verified or
that Apple cannot check the application for malicious software.

If the download came from the official project page:

1. verify the published SHA-256 checksum against the downloaded ZIP;
2. extract the ZIP and move `LUFScale.app` to Applications;
3. try to open `LUFScale.app` once;
4. open **System Settings** and select **Privacy & Security**;
5. in the Security section, click **Open Anyway** for LUFScale;
6. confirm by clicking **Open**.

macOS then stores LUFScale as an exception. The option may be unavailable on a
Mac managed by a company, school or other administrator. Do not disable
Gatekeeper globally and do not remove macOS security attributes system-wide.

## Build the Intel variant

On an Intel Mac running macOS 12 or later:

1. extract the complete source package;
2. connect the Mac to the Internet;
3. open Terminal in the extracted directory and run
   `./Create_Community_Distribution_macOS.command`;
4. if macOS requests the Xcode Command Line Tools, finish that installation
   while leaving Terminal open; the builder waits and resumes automatically;
5. verify the two native executables with:

```zsh
file "dist/LUFScale.app/Contents/MacOS/LUFScale"
file "dist/LUFScale.app/Contents/Frameworks/ffmpeg"
```

Both results must contain `x86_64`. The script rejects a target architecture
different from the build Mac. It downloads the pinned uv 0.12.5 bootstrap,
verifies its published SHA-256, and uses it to place a portable CPython 3.13.15
only below the private `.build-tools` directory. It neither invokes `sudo` nor
modifies `/Library` or the shell `PATH`. It then uses its own `pkg-config`
helper, compiles the verified FFmpeg engine and packages the compatible Python
and PySide6/Qt runtimes. The successful native Intel build and first launch do
not replace the complete functional tests on Intel hardware.

`Create_Community_Distribution_macOS.command` is the only launcher intended
for the publisher. Do not run the internal worker stored in `tools` directly.

Official Apple security guidance: <https://support.apple.com/en-us/102445>.
