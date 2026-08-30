[CmdletBinding()]
param(
    [string]$PythonExecutable = ""
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version 2.0

$ScriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Split-Path -Parent $ScriptDirectory
Set-Location $ProjectRoot

function Fail([string]$Message) {
    throw "ERROR - $Message"
}

if ([Environment]::OSVersion.Platform -ne [PlatformID]::Win32NT) {
    Fail "The Windows application must be built on Windows."
}
if (-not [Environment]::Is64BitOperatingSystem -or -not [Environment]::Is64BitProcess) {
    Fail "Use 64-bit Windows and 64-bit PowerShell to build LUFScale x86-64."
}

Write-Host "Locating Python 3.10 through 3.13..."
$Python = $null
if ($PythonExecutable) {
    if (-not (Test-Path $PythonExecutable)) {
        Fail "The requested Python executable does not exist: $PythonExecutable"
    }
    $Python = (Resolve-Path $PythonExecutable).Path
}
if (-not $Python -and (Get-Command py.exe -ErrorAction SilentlyContinue)) {
    foreach ($Version in @("3.13", "3.12", "3.11", "3.10")) {
        & py.exe "-$Version-64" -c "import sys; assert (3,10) <= sys.version_info[:2] <= (3,13); print(sys.executable)" 2>$null | ForEach-Object {
            if (-not $Python) { $Python = $_.Trim() }
        }
        if ($Python) { break }
    }
}
if (-not $Python -and (Get-Command python.exe -ErrorAction SilentlyContinue)) {
    $Candidate = (& python.exe -c "import sys; assert (3,10) <= sys.version_info[:2] <= (3,13) and sys.maxsize > 2**32; print(sys.executable)" 2>$null)
    if ($LASTEXITCODE -eq 0 -and $Candidate) { $Python = $Candidate.Trim() }
}
if (-not $Python) {
    Fail "No build Python was supplied. Run Create_Offline_Installer_Windows.cmd so the private runtime is prepared automatically."
}
if ($Python -match "WindowsApps") {
    Fail "The Microsoft Store execution alias is not a complete build runtime. Run Create_Offline_Installer_Windows.cmd."
}

$BuildEnvironment = Join-Path $ProjectRoot ".construction-windows"
$EnvironmentPython = Join-Path $BuildEnvironment "Scripts\python.exe"
if (Test-Path -LiteralPath $BuildEnvironment) {
    Write-Host "Removing the previous isolated build environment..."
    Remove-Item -LiteralPath $BuildEnvironment -Recurse -Force
}
Write-Host "Creating a clean isolated build environment..."
& $Python -m venv $BuildEnvironment
if ($LASTEXITCODE -ne 0 -or -not (Test-Path -LiteralPath $EnvironmentPython -PathType Leaf)) {
    Fail "The isolated Python build environment could not be created."
}
& $EnvironmentPython -m pip install --disable-pip-version-check --upgrade "pip==26.2.1"
if ($LASTEXITCODE -ne 0) { Fail "The pinned pip build dependency could not be prepared." }
& $EnvironmentPython -m pip install --disable-pip-version-check "pyinstaller==6.21.0" "reportlab==4.4.3" -r requirements.txt
if ($LASTEXITCODE -ne 0) { Fail "The pinned Windows build dependencies could not be installed." }

$Version = (& $EnvironmentPython -c "import sys; sys.path.insert(0, 'src'); from lufscale.version import APP_VERSION; print(APP_VERSION)").Trim()
if ($Version -ne "2.1.12") { Fail "Unexpected application version: $Version" }

$GuideDirectory = Join-Path $ProjectRoot "output\pdf"
if (Test-Path $GuideDirectory) { Remove-Item -Recurse -Force $GuideDirectory }
New-Item -ItemType Directory -Force -Path $GuideDirectory | Out-Null
Write-Host "Generating the twelve Windows PDF guides..."
& $EnvironmentPython tools\generate_guides.py --output-dir $GuideDirectory
if ($LASTEXITCODE -ne 0) {
    Fail "PDF guide generation failed. Review the Python error shown above."
}
if (-not (Test-Path $GuideDirectory)) {
    Fail "PDF guide generation did not create output\pdf."
}
if (@(Get-ChildItem $GuideDirectory -Filter *.pdf -File).Count -ne 12) {
    Fail "The Windows build requires exactly twelve PDF guides."
}

Write-Host "Preparing and validating the bundled Windows FFmpeg engine..."
& $EnvironmentPython tools\prepare_bundled_ffmpeg_windows.py
$BundledFFmpeg = Join-Path $ProjectRoot "packaging\generated\windows-x86_64\ffmpeg.exe"
if (-not (Test-Path $BundledFFmpeg)) { Fail "The validated FFmpeg executable is missing." }

$env:LUFSCALE_BUNDLED_FFMPEG = $BundledFFmpeg
$env:LUFSCALE_GUIDES_DIR = $GuideDirectory
if (Test-Path "build\LUFScale") { Remove-Item -Recurse -Force "build\LUFScale" }
if (Test-Path "dist\LUFScale") { Remove-Item -Recurse -Force "dist\LUFScale" }

Write-Host "Building the Windows application tree for the offline installer..."
& $EnvironmentPython -m PyInstaller --clean --noconfirm packaging\windows\LUFScale.spec

$ApplicationDirectory = Join-Path $ProjectRoot "dist\LUFScale"
$Application = Join-Path $ApplicationDirectory "LUFScale.exe"
$PackagedFFmpeg = Join-Path $ApplicationDirectory "ffmpeg.exe"
if (-not (Test-Path $Application)) { Fail "PyInstaller did not create dist\LUFScale\LUFScale.exe." }
if (-not (Test-Path $PackagedFFmpeg)) { Fail "The packaged application does not contain ffmpeg.exe." }
if (@(Get-ChildItem $ApplicationDirectory -Filter ffmpeg.exe -File -Recurse).Count -ne 1) {
    Fail "The application must contain exactly one ffmpeg.exe."
}

$Filters = & $PackagedFFmpeg -hide_banner -filters 2>&1 | Out-String
if ($LASTEXITCODE -ne 0 -or $Filters -notmatch "\bloudnorm\b") {
    Fail "The packaged FFmpeg does not provide loudnorm."
}
$Encoders = & $PackagedFFmpeg -hide_banner -encoders 2>&1 | Out-String
foreach ($Encoder in @("libmp3lame", "flac", "pcm_s16le", "pcm_s16be", "pcm_s24le", "pcm_s24be", "pcm_s32le", "pcm_s32be", "pcm_f32le", "aac", "libvorbis", "libopus")) {
    if ($Encoders -notmatch "\b$Encoder\b") { Fail "Missing packaged FFmpeg encoder: $Encoder" }
}

foreach ($Required in @(
    "LICENSE", "COPYRIGHT", "README.md", "OPEN_LUFSCALE_ON_WINDOWS.md",
    "THIRD_PARTY_NOTICES.md", "SBOM.cdx.json", "RELEASE_2.1.12.md",
    "VALIDATION_2.1.12.md", "FFMPEG_WINDOWS_BUILD_MANIFEST.json",
    "FFMPEG_WINDOWS_DISTRIBUTION_NOTICE.txt"
)) {
    if (-not (Test-Path (Join-Path $ApplicationDirectory $Required))) {
        Fail "Required packaged file is missing: $Required"
    }
}
if (@(Get-ChildItem (Join-Path $ApplicationDirectory "output\pdf") -Filter *.pdf -File).Count -ne 12) {
    Fail "The packaged application does not contain the twelve PDF guides."
}

if (Test-Path "build\LUFScale-Portable") { Remove-Item -Recurse -Force "build\LUFScale-Portable" }
$PortableApplication = Join-Path $ProjectRoot "dist\LUFScale-2.1.12-Portable-x64.exe"
if (Test-Path $PortableApplication) { Remove-Item -Force $PortableApplication }

Write-Host "Building the self-contained single-file portable application..."
& $EnvironmentPython -m PyInstaller --clean --noconfirm packaging\windows\LUFScale-Portable.spec
if ($LASTEXITCODE -ne 0) { Fail "The portable PyInstaller build failed." }
if (-not (Test-Path $PortableApplication)) {
    Fail "PyInstaller did not create dist\LUFScale-2.1.12-Portable-x64.exe."
}
if ((Get-Item $PortableApplication).Length -lt 10MB) {
    Fail "The portable executable is unexpectedly small."
}

$ArchiveViewer = Join-Path $BuildEnvironment "Scripts\pyi-archive_viewer.exe"
if (-not (Test-Path $ArchiveViewer)) {
    Fail "The PyInstaller archive inspection tool is missing."
}
$PortableListing = (& $ArchiveViewer -l $PortableApplication 2>&1 | Out-String)
if ($LASTEXITCODE -ne 0) { Fail "The portable executable archive could not be inspected." }
foreach ($RequiredPortableEntry in @(
    "ffmpeg.exe", "Guide_LUFScale_EN.pdf", "LICENSE",
    "FFMPEG_WINDOWS_BUILD_MANIFEST.json"
)) {
    if ($PortableListing -notmatch ([Regex]::Escape($RequiredPortableEntry))) {
        Fail "Required portable executable entry is missing: $RequiredPortableEntry"
    }
}
if ([Regex]::Matches($PortableListing, "(?i)ffmpeg\.exe").Count -ne 1) {
    Fail "The portable executable must contain exactly one ffmpeg.exe."
}

Write-Host "Windows application builds completed successfully:"
Write-Host $Application
Write-Host $PortableApplication
Write-Host "A final launch, audio-format and SmartScreen test is still required on Windows 10/11."
