# Install and open LUFScale on Windows

## Requirements

The published installer targets **64-bit Windows on x86-64**. Windows 11 is recommended.
Windows 10 version 1809 or later remains a technical compatibility
target, although Microsoft standard support for Windows 10 has ended.

## Install the application

The single `LUFScale-2.1.12-Setup-x64.exe` file already contains LUFScale,
the Python runtime, PySide6/Qt, FFmpeg, the required audio codecs, PDF guides
and licence notices. Installation requires no separate download, Python setup,
FFmpeg setup or PowerShell command.

1. Verify the installer against the adjacent `.sha256` file.
2. Double-click `LUFScale-2.1.12-Setup-x64.exe`.
3. Read and accept the GNU GPL licence.
4. Follow the setup wizard. The desktop shortcut is optional.
5. Open LUFScale from the Windows Start menu.

The default per-user installation location does not require administrator
rights. To remove LUFScale, use Windows **Settings > Apps > Installed apps** or
the uninstall shortcut in the LUFScale Start menu folder.

## Run the portable application without installation

`LUFScale-2.1.12-Portable-x64.exe` contains the same application, Python/Qt
runtime, FFmpeg engine, codecs, guides and notices in one file. Verify its
adjacent `.sha256` file, copy the executable to any compatible x86-64 Windows
10/11 computer and double-click it. No installation, Python, FFmpeg or
PowerShell command is required.

At each launch, Windows extracts the private runtime to a temporary directory.
The first opening can therefore take longer and antivirus software can inspect
the extracted files. A normal application close removes the temporary runtime;
audio outputs and user settings are not stored inside it.

## SmartScreen

The free community build is not signed with a commercial Windows code-signing
certificate. SmartScreen can display **Windows protected your PC** for either
executable even when the checksum is correct. After checking the source and
SHA-256 file, select
**More info**, verify that the application is LUFScale, then choose
**Run anyway** if you trust the package.

Do not disable SmartScreen or antivirus protection globally. An administrator
can block unsigned software by policy; in that case, ask the administrator to
review the source, checksum and build records.

## Build the offline installer from source

Extract the source package completely on a real x86-64 Windows 10/11 computer,
then double-click `Create_Offline_Installer_Windows.cmd`. The builder prepares
its own compatible Python and Inno Setup compiler if required; no manual Python
download, PATH change or PowerShell command is needed.

This `.cmd` file is the only launcher intended for the publisher. The
PowerShell files stored in `tools` are internal workers and must not be opened
separately.

The build computer needs Internet access to obtain verified official build
prerequisites and pinned Python packages. The resulting setup and portable
executable are nevertheless fully offline and download nothing on the end
user's computer.

## Verification before redistribution

Test install, launch, upgrade and uninstall on clean Windows 10/11 x86-64
profiles. Also copy the portable executable to a second clean computer and run
it directly. Test Normalize, ReplayGain and Analyze only with every supported
format, Unicode and long paths, pause/cancel, optional CSV creation,
application closure and relaunch. Confirm that CSV creation and automatic start
are off on a fresh profile and that both packages run while Python and FFmpeg
are absent from the system PATH. The absence of a build error does not replace
this functional validation.
