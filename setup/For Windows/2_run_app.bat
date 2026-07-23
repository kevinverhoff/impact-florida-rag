@echo off
setlocal

:: ============================================================
:: 2_run_app.bat
:: Impact Florida RAG Tool — Launch the App
::
:: Run this any time you want to use the tool.
:: The app will open in your web browser at http://localhost:8501
::
:: To stop the app: press Ctrl+C in this window, then close it.
:: ============================================================

echo.
echo ============================================================
echo  Impact Florida RAG Tool — Launching App
echo ============================================================
echo.

:: ---- Find a way to run Streamlit: try "python", then "python3", ----
:: ---- then fall back to a bare "streamlit" command on PATH.       ----
set "PY_CMD="
python --version >nul 2>&1
if not errorlevel 1 set "PY_CMD=python"

if not defined PY_CMD (
    python3 --version >nul 2>&1
    if not errorlevel 1 set "PY_CMD=python3"
)

if not defined PY_CMD (
    streamlit --version >nul 2>&1
    if errorlevel 1 (
        echo ERROR: Could not find "python", "python3", or "streamlit".
        echo Please install Python from https://www.python.org/downloads/
        echo Make sure to check "Add Python to PATH" during installation.
        echo.
        pause
        exit /b 1
    )
)

:: ---- Move to the project root (two levels up from setup\For Windows) ----
cd /d "%~dp0..\.."

:: ---- Check that the knowledge base exists ----
if not exist data\chroma_db (
    echo ERROR: The knowledge base has not been built yet.
    echo Please run 1_setup_and_build.bat first and wait for it
    echo to complete before launching the app.
    echo.
    pause
    exit /b 1
)

:: ---- Check that the app file exists ----
if not exist app\app.py (
    echo ERROR: app\app.py not found.
    echo Make sure this script is located at setup\For Windows\ inside the project folder.
    echo.
    pause
    exit /b 1
)

echo Starting the app...
echo.
echo Once you see "Local URL: http://localhost:8501" below,
echo open your browser and go to:
echo.
echo     http://localhost:8501
echo.
echo (Your browser may open automatically.)
echo.
echo To stop the app, press Ctrl+C in this window.
echo ============================================================
echo.

if defined PY_CMD (
    %PY_CMD% -m streamlit run app/app.py
) else (
    streamlit run app/app.py
)

echo.
echo App stopped.
pause
