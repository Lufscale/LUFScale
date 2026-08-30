@echo off
setlocal
cd /d "%~dp0"

echo LUFScale 2.1.12 - offline installer and portable application builder
echo.
powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File "%~dp0tools\Internal_Installer_Orchestrator_Windows.ps1"
set "BUILD_RESULT=%ERRORLEVEL%"

echo.
if not "%BUILD_RESULT%"=="0" (
  echo ERROR - The Windows packages could not be created. Review the messages above.
) else (
  echo The offline installer and portable executable are available in the dist folder.
)
echo.
pause
exit /b %BUILD_RESULT%
