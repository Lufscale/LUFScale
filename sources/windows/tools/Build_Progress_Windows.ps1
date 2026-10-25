[CmdletBinding()]
param()
$ErrorActionPreference = 'Stop'
$ProjectRoot = Split-Path -Parent $PSScriptRoot
$Logs = Join-Path $ProjectRoot 'build-logs'
New-Item -ItemType Directory -Force -Path $Logs | Out-Null
$RunName = 'build-' + (Get-Date -Format 'yyyyMMdd-HHmmss') + '-' + $PID
$OutputLog = Join-Path $Logs ($RunName + '.log')
$ErrorLog = Join-Path $Logs ($RunName + '-errors.log')
$env:LUFSCALE_PROGRESS_FILE = Join-Path $Logs ($RunName + '.progress')
[IO.File]::WriteAllText($env:LUFSCALE_PROGRESS_FILE, '0|Preparing')
$env:PYTHONUNBUFFERED = '1'
$Titles = @('Preparing Python', 'Dependencies', 'PDF guides', 'FFmpeg validation', 'Building the application', 'Portable executable', 'Preparing the installer', 'Setup and final checks')
$Shown = -1
$LastBytes = 0L
$LastOutput = 0.0
$StageStarted = 0.0
function Write-LiveLine([string]$Text) {
    $Width = 100
    try { $Width = [Math]::Max(20, [Console]::WindowWidth - 1) } catch { }
    if ($Text.Length -gt $Width) { $Text = $Text.Substring(0, $Width) }
    [Console]::Write("`r" + $Text.PadRight($Width))
}
$Worker = $null
$Result = 1
$Watch = [Diagnostics.Stopwatch]::StartNew()
Write-Host 'LUFScale 2.2.2 - Windows build'
Write-Host 'One progress bar per stage; animation indicates recent build activity.'
Write-Host 'No new messages does not necessarily mean the build is stalled.'
Write-Host "Logs: $OutputLog and $ErrorLog"
try {
    $Script = Join-Path $PSScriptRoot 'Internal_Installer_Orchestrator_Windows.ps1'
    $Arguments = '-NoLogo -NoProfile -NonInteractive -ExecutionPolicy Bypass -File "' + $Script + '"'
    $Worker = Start-Process -FilePath (Join-Path $PSHOME 'powershell.exe') `
        -ArgumentList $Arguments -WorkingDirectory $ProjectRoot -NoNewWindow `
        -RedirectStandardOutput $OutputLog -RedirectStandardError $ErrorLog -PassThru
    while (-not $Worker.HasExited) {
        $Step = 0
        $Label = 'Preparing'
        try {
            $Parts = ([IO.File]::ReadAllText($env:LUFSCALE_PROGRESS_FILE)).Trim().Split('|', 2)
            if ($Parts.Length -eq 2 -and $Parts[0] -match '^[0-8]$') {
                $Step = [int]$Parts[0]
                $Label = $Parts[1]
            }
        } catch { }
        $Target = [Math]::Min(7, $Step)
        while ($Shown -lt $Target) {
            if ($Shown -ge 0) {
                Write-LiveLine '[====================] Complete'
                [Console]::WriteLine()
            }
            $Shown++
            Write-Host "`nStage $($Shown + 1)/8 - $($Titles[$Shown])"
            $StageStarted = $Watch.Elapsed.TotalSeconds
        }
        $Bytes = 0L
        foreach ($Path in @($OutputLog, $ErrorLog)) {
            if (Test-Path -LiteralPath $Path) { $Bytes += (Get-Item -LiteralPath $Path).Length }
        }
        $Now = $Watch.Elapsed.TotalSeconds
        if ($Bytes -ne $LastBytes) { $LastOutput = $Now; $LastBytes = $Bytes }
        $Quiet = [int]($Now - $LastOutput)
        $Detail = $Label
        # Show just the latest useful activity, with the full output in the logs.
        try {
            $LatestLog = @($OutputLog, $ErrorLog) | Get-Item | Sort-Object LastWriteTimeUtc -Descending | Select-Object -First 1
            $Recent = @(Get-Content -LiteralPath $LatestLog.FullName -Tail 4 | Where-Object { $_.Trim() })
            if ($Recent.Count -gt 0) { $Detail = $Recent[-1].Trim() }
        } catch { }
        $Detail = $Detail -replace '[\x00-\x1f]', ' '
        $Bar = '....................'.ToCharArray()
        if ($Quiet -le 2) {
            $Bar[([int]$Now % 20)] = '='
            $Activity = 'Activity detected'
        } else { $Activity = "No new messages for ${Quiet}s" }
        $Elapsed = [int]($Now - $StageStarted)
        Write-LiveLine ("[" + (-join $Bar) + "] ${Elapsed}s - $Activity - $Detail")
        Start-Sleep -Milliseconds 500
        $Worker.Refresh()
    }
    $Worker.WaitForExit()
    $Result = $Worker.ExitCode
    if ($Result -eq 0) {
        while ($Shown -lt 7) {
            if ($Shown -ge 0) { Write-LiveLine '[====================] Complete'; [Console]::WriteLine() }
            $Shown++
            Write-Host "`nStage $($Shown + 1)/8 - $($Titles[$Shown])"
        }
        Write-LiveLine '[====================] Complete'
        [Console]::WriteLine()
        Write-Host '8/8 - Build complete. Executables are in dist.' 
    } else {
        [Console]::WriteLine()
        Write-Host "FAILED (code $Result). Logs: $OutputLog and $ErrorLog"
        Get-Content -LiteralPath $OutputLog -Tail 8
        Get-Content -LiteralPath $ErrorLog -Tail 12
    }
} catch {
    [Console]::WriteLine()
    Write-Host "FAILED : $($_.Exception.Message)"
    Write-Host "Logs: $OutputLog and $ErrorLog"
    $Result = 1
} finally {
    if ($null -ne $Worker -and -not $Worker.HasExited) {
        & taskkill.exe /PID $Worker.Id /T /F 2>&1 | Out-Null
    }
    Remove-Item Env:PYTHONUNBUFFERED -ErrorAction SilentlyContinue
    Remove-Item Env:LUFSCALE_PROGRESS_FILE -ErrorAction SilentlyContinue
}
exit $Result
