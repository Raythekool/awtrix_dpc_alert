@echo off
REM Batch script wrapper for upload_icons.py
REM Makes it easier to upload icons to AWTRIX device on Windows

setlocal

set "SCRIPT_DIR=%~dp0"
set "PYTHON_SCRIPT=%SCRIPT_DIR%upload_icons.py"

REM Check if Python is available
where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Error: python is not installed or not in PATH
    echo Please install Python 3.6 or higher from https://www.python.org/
    exit /b 1
)

REM If no arguments provided, use --default-icons
if "%~1"=="" (
    python "%PYTHON_SCRIPT%" --default-icons
) else (
    REM Run the Python script with all arguments
    python "%PYTHON_SCRIPT%" %*
)
