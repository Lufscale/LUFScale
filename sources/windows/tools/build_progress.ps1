function Set-BuildStage([int]$Completed, [string]$Label) {
    if ($env:LUFSCALE_PROGRESS_FILE) {
        $Temporary = $env:LUFSCALE_PROGRESS_FILE + '.tmp'
        [IO.File]::WriteAllText($Temporary, "$Completed|$Label")
        Move-Item -LiteralPath $Temporary -Destination $env:LUFSCALE_PROGRESS_FILE -Force
    }
}
