[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"
Set-StrictMode -Version 2.0

$ScriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Split-Path -Parent $ScriptDirectory
Set-Location $ProjectRoot
. (Join-Path $PSScriptRoot "build_progress.ps1")
if ($env:LUFSCALE_PROGRESS_FILE) { $ProgressPreference = "SilentlyContinue" }

$PythonVersion = "3.13.15"
$PythonUrl = "https://www.nuget.org/api/v2/package/python/$PythonVersion"
$PythonSha512 = "0ad3164e412912412d89ee9e8a9d8292893427812a67b9e43d8ef6766871faa7f10dc15899e3691c14e0336fd79da3d39eaa843eac1e3e056a9151ad336bac04"
$InnoVersion = "6.7.3"
$InnoUrl = "https://github.com/jrsoftware/issrc/releases/download/is-6_7_3/innosetup-$InnoVersion.exe"
$InnoPublisherPattern = '(?i)^CN=Pyrsys B\.V\.,\s*O=Pyrsys B\.V\.(?:,|$)'
$ToolsDirectory = Join-Path $ProjectRoot ".build-tools"
$DownloadDirectory = Join-Path $ToolsDirectory "downloads"
$PythonDirectory = Join-Path $ToolsDirectory "python-$PythonVersion"
$InnoDirectory = Join-Path $ToolsDirectory "inno-setup-$InnoVersion"

function Fail([string]$Message) {
    throw "ERROR - $Message"
}

function Assert-WindowsSignature(
    [string]$Path,
    [string]$ExpectedPublisher
) {
    $Signature = Get-AuthenticodeSignature -FilePath $Path
    if ($Signature.Status -ne [System.Management.Automation.SignatureStatus]::Valid) {
        Fail "Invalid or unverifiable digital signature for $Path ($($Signature.Status))."
    }
    if (-not $Signature.SignerCertificate -or $Signature.SignerCertificate.Subject -notmatch $ExpectedPublisher) {
        Fail "Unexpected publisher for ${Path}: $($Signature.SignerCertificate.Subject)"
    }
}

function Test-ExpectedPythonRuntime([string]$Path) {
    if (-not $Path -or -not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        return $false
    }
    $Signature = Get-AuthenticodeSignature -FilePath $Path
    if (-not (
        $Signature.Status -eq [System.Management.Automation.SignatureStatus]::Valid -and
        $Signature.SignerCertificate -and
        $Signature.SignerCertificate.Subject -match "Python Software Foundation"
    )) {
        return $false
    }
    & $Path -c "import platform, sys; assert sys.version_info[:3] == (3, 13, 15) and platform.machine().lower() in ('amd64', 'x86_64')" 2>$null
    return ($LASTEXITCODE -eq 0)
}

function Download-VerifiedArchive(
    [string]$Url,
    [string]$Destination,
    [string]$ExpectedSha512
) {
    if (Test-Path -LiteralPath $Destination -PathType Leaf) {
        $CachedSha512 = (Get-FileHash -Algorithm SHA512 $Destination).Hash.ToLowerInvariant()
        if ($CachedSha512 -eq $ExpectedSha512.ToLowerInvariant()) {
            return
        }
        Remove-Item -LiteralPath $Destination -Force
    }
    $PartialDestination = "$Destination.partial"
    Remove-Item -LiteralPath $PartialDestination -Force -ErrorAction SilentlyContinue
    try {
        Write-Host "Downloading the official portable Python build prerequisite..."
        [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
        Invoke-WebRequest -UseBasicParsing -Uri $Url -OutFile $PartialDestination
        $ActualSha512 = (Get-FileHash -Algorithm SHA512 $PartialDestination).Hash.ToLowerInvariant()
        if ($ActualSha512 -ne $ExpectedSha512.ToLowerInvariant()) {
            Fail "SHA-512 verification failed for the downloaded Python package."
        }
        Move-Item -LiteralPath $PartialDestination -Destination $Destination
    } finally {
        Remove-Item -LiteralPath $PartialDestination -Force -ErrorAction SilentlyContinue
    }
}

function Download-VerifiedInstaller(
    [string]$Url,
    [string]$Destination,
    [string]$ExpectedPublisher,
    [string]$ExpectedSha256 = ""
) {
    if (-not (Test-Path $Destination)) {
        Write-Host "Downloading the official build prerequisite..."
        [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
        Invoke-WebRequest -UseBasicParsing -Uri $Url -OutFile $Destination
    }
    if ($ExpectedSha256) {
        $ActualSha256 = (Get-FileHash -Algorithm SHA256 $Destination).Hash.ToLowerInvariant()
        if ($ActualSha256 -ne $ExpectedSha256.ToLowerInvariant()) {
            Remove-Item -Force $Destination -ErrorAction SilentlyContinue
            Fail "SHA-256 verification failed for the downloaded prerequisite."
        }
    }
    Assert-WindowsSignature $Destination $ExpectedPublisher
}


function Find-InnoCompiler {
    $Candidates = @(
        (Join-Path $InnoDirectory "ISCC.exe"),
        (Join-Path ${env:ProgramFiles(x86)} "Inno Setup 6\ISCC.exe"),
        (Join-Path $env:ProgramFiles "Inno Setup 6\ISCC.exe")
    )
    foreach ($Candidate in $Candidates) {
        if ($Candidate -and (Test-Path $Candidate)) { return $Candidate }
    }
    $Command = Get-Command ISCC.exe -ErrorAction SilentlyContinue
    if ($Command) { return $Command.Source }
    return $null
}

if ([Environment]::OSVersion.Platform -ne [PlatformID]::Win32NT) {
    Fail "The Windows installer must be built on Windows."
}
if (-not [Environment]::Is64BitOperatingSystem -or -not [Environment]::Is64BitProcess) {
    Fail "Use 64-bit Windows and a 64-bit command environment."
}

New-Item -ItemType Directory -Force -Path $DownloadDirectory | Out-Null

Set-BuildStage 0 "Preparing Python"
$Python = Join-Path $PythonDirectory "python.exe"
$PrivatePythonIsValid = Test-ExpectedPythonRuntime $Python
if (-not $PrivatePythonIsValid) {
    Write-Host "Preparing the verified private Python $PythonVersion build copy without Windows installation or registry changes..."
    $PythonArchive = Join-Path $DownloadDirectory "python-$PythonVersion-nuget.zip"
    $PythonExtractionDirectory = Join-Path $ToolsDirectory "python-$PythonVersion-extracting"
    Download-VerifiedArchive $PythonUrl $PythonArchive $PythonSha512
    if (Test-Path -LiteralPath $PythonExtractionDirectory) {
        Remove-Item -LiteralPath $PythonExtractionDirectory -Recurse -Force
    }
    if (Test-Path -LiteralPath $PythonDirectory) {
        Remove-Item -LiteralPath $PythonDirectory -Recurse -Force
    }
    New-Item -ItemType Directory -Force -Path $PythonExtractionDirectory | Out-Null
    try {
        Expand-Archive -LiteralPath $PythonArchive -DestinationPath $PythonExtractionDirectory -Force
        $ExtractedPythonDirectory = Join-Path $PythonExtractionDirectory "tools"
        $ExtractedPython = Join-Path $ExtractedPythonDirectory "python.exe"
        if (-not (Test-ExpectedPythonRuntime $ExtractedPython)) {
            Fail "The extracted Python package failed signature, version or x86-64 validation."
        }
        Move-Item -LiteralPath $ExtractedPythonDirectory -Destination $PythonDirectory
    } finally {
        Remove-Item -LiteralPath $PythonExtractionDirectory -Recurse -Force -ErrorAction SilentlyContinue
    }
}
if (-not (Test-ExpectedPythonRuntime $Python)) {
    Fail "The private Python executable could not be prepared at $Python. Delete .build-tools and run the builder again."
}

Write-Host "Building the autonomous LUFScale application..."
& (Join-Path $ScriptDirectory "Internal_Application_Builder_Windows.ps1") -PythonExecutable $Python

Set-BuildStage 6 "Preparing the installer"
$InnoCompiler = Find-InnoCompiler
if (-not $InnoCompiler) {
    Write-Host "Inno Setup was not found. Installing a private compiler automatically..."
    $InnoInstaller = Join-Path $DownloadDirectory "innosetup-$InnoVersion.exe"
    $InnoInstallLog = Join-Path $DownloadDirectory "innosetup-$InnoVersion-install.log"
    Download-VerifiedInstaller $InnoUrl $InnoInstaller $InnoPublisherPattern
    $InnoArgumentLine = @(
        "/VERYSILENT"
        "/SUPPRESSMSGBOXES"
        "/NORESTART"
        "/CURRENTUSER"
        "/DIR=`"$InnoDirectory`""
        "/LOG=`"$InnoInstallLog`""
    ) -join " "
    $Process = Start-Process -FilePath $InnoInstaller -ArgumentList $InnoArgumentLine -Wait -PassThru
    if ($Process.ExitCode -ne 0) {
        Fail "The private Inno Setup installation failed with exit code $($Process.ExitCode). Installer log: $InnoInstallLog"
    }
    $InnoCompiler = Join-Path $InnoDirectory "ISCC.exe"
}
if (-not (Test-Path $InnoCompiler)) { Fail "ISCC.exe could not be prepared." }

Set-BuildStage 7 "Creating Setup and final checks"
$InstallerScript = Join-Path $ProjectRoot "packaging\windows\LUFScale.iss"
Write-Host "Creating the single-file offline installer..."
& $InnoCompiler $InstallerScript
if ($LASTEXITCODE -ne 0) { Fail "Inno Setup compilation failed with exit code $LASTEXITCODE." }

$Installer = Join-Path $ProjectRoot "dist\LUFScale-2.2.3-Setup-x64.exe"
$Portable = Join-Path $ProjectRoot "dist\LUFScale-2.2.3-Portable-x64.exe"
$InstallerChecksum = "$Installer.sha256"
$PortableChecksum = "$Portable.sha256"
if (-not (Test-Path $Installer)) { Fail "The expected offline installer was not created: $Installer" }
if ((Get-Item $Installer).Length -lt 10MB) { Fail "The generated installer is unexpectedly small." }
if (-not (Test-Path $Portable)) { Fail "The expected portable executable was not created: $Portable" }
if ((Get-Item $Portable).Length -lt 10MB) { Fail "The portable executable is unexpectedly small." }

$IconCheckPython = Join-Path $ProjectRoot ".build-windows\Scripts\python.exe"
& $IconCheckPython tools\verify_application_icon.py windows $Installer assets\branding\LUFScale.ico
if ($LASTEXITCODE -ne 0) { Fail "The installer icon is missing or invalid." }

$InstallerHash = (Get-FileHash -Algorithm SHA256 $Installer).Hash.ToLowerInvariant()
Set-Content -Path $InstallerChecksum -Value "$InstallerHash  LUFScale-2.2.3-Setup-x64.exe" -Encoding Ascii
$PortableHash = (Get-FileHash -Algorithm SHA256 $Portable).Hash.ToLowerInvariant()
Set-Content -Path $PortableChecksum -Value "$PortableHash  LUFScale-2.2.3-Portable-x64.exe" -Encoding Ascii
foreach ($Checksum in @($InstallerChecksum, $PortableChecksum)) {
    if ((Get-Item $Checksum).Length -le 0) { Fail "The SHA-256 file is empty: $Checksum" }
}

Write-Host ""
Write-Host "LUFScale 2.2.3 offline installer created successfully:"
Write-Host $Installer
Write-Host "SHA-256: $InstallerChecksum"
Write-Host ""
Write-Host "LUFScale 2.2.3 portable single-file application created successfully:"
Write-Host $Portable
Write-Host "SHA-256: $PortableChecksum"
Write-Host ""
Write-Host "Both files contain LUFScale, Python runtime, Qt, FFmpeg, guides and notices."
Write-Host "They download nothing and launch no PowerShell script on the end user's computer."
Write-Host "A final install, portable launch, audio and SmartScreen test is still required on Windows 10/11 x86-64."

Set-BuildStage 8 "Complete"
