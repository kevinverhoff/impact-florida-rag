@echo off
setlocal

:: ============================================================
:: 1_setup_and_build.bat
:: Impact Florida RAG Tool — First-Time Setup
::
:: This script:
::   1. Installs all Python dependencies from requirements.txt
::   2. Runs the pipeline to build the knowledge base (20-60 min)
::
:: Run this ONCE before using the app for the first time.
:: It is safe to run again if the build was interrupted.
:: ============================================================

echo.
echo ============================================================
echo  Impact Florida RAG Tool — Setup and Build
echo ============================================================
echo.

:: ---- Check that Python is available ----
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python was not found.
    echo Please install Python from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
)

:: ---- Move to the project root (two levels up from setup\For Windows) ----
cd /d "%~dp0..\.."

:: ---- Check that requirements.txt exists ----
if not exist requirements.txt (
    echo ERROR: requirements.txt not found.
    echo Make sure this script is located at setup\For Windows\ inside the project folder.
    echo.
    pause
    exit /b 1
)

:: ---- Check that secrets\.env exists ----
if not exist secrets\.env (
    echo ERROR: secrets\.env file not found.
    echo Please follow Part 4c of the setup guide to create it.
    echo.
    pause
    exit /b 1
)

:: ---- Check that secrets\service-account.json exists ----
if not exist secrets\service-account.json (
    echo ERROR: secrets\service-account.json not found.
    echo Please place your Google service account credentials file
    echo in the secrets\ folder before running this script.
    echo.
    pause
    exit /b 1
)

:: ---- Install dependencies ----
echo Step 1 of 2: Installing Python dependencies...
echo This may take a few minutes on the first run.
echo.
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ERROR: Dependency installation failed.
    echo Review the error messages above and reach out for help.
    echo.
    pause
    exit /b 1
)

echo.
echo Dependencies installed successfully.
echo.

:: ---- Run the pipeline ----
echo Step 2 of 2: Building the knowledge base...
echo.
echo This connects to Google Drive, downloads documents, runs AI
echo processing, and builds the searchable vector database.
echo.
echo Expected time: 20 to 60 minutes depending on corpus size.
echo The window will show progress as each step completes.
echo Do not close this window until you see "Build complete."
echo.

python pipeline/__init__.py

if errorlevel 1 (
    echo.
    echo ERROR: The pipeline did not complete successfully.
    echo Review the error messages above and reach out for help.
    echo.
    pause
    exit /b 1
)

echo.
echo ============================================================
echo  Build complete.
echo  You can now launch the app using 2_run_app.bat
echo ============================================================
echo.
pause
