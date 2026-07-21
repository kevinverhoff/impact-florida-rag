#!/bin/bash
#
# ============================================================
# 1_setup_and_build.sh
# Impact Florida RAG Tool — First-Time Setup
#
# This script:
#   1. Installs all Python dependencies from requirements.txt
#   2. Runs the pipeline to build the knowledge base (20-60 min)
#
# Run this ONCE before using the app for the first time.
# It is safe to run again if the build was interrupted.
# ============================================================

echo ""
echo "============================================================"
echo " Impact Florida RAG Tool — Setup and Build"
echo "============================================================"
echo ""

# ---- Check that Python is available ----
if command -v python3 >/dev/null 2>&1; then
    PYTHON=python3
elif command -v python >/dev/null 2>&1; then
    PYTHON=python
else
    echo "ERROR: Python was not found."
    echo "Please install Python from https://www.python.org/downloads/"
    echo "or via Homebrew: brew install python"
    echo ""
    read -p "Press Enter to exit..."
    exit 1
fi

# ---- Move to the project root (two levels up from setup/For Mac) ----
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/../.." || exit 1

# ---- Check that requirements.txt exists ----
if [ ! -f requirements.txt ]; then
    echo "ERROR: requirements.txt not found."
    echo "Make sure this script is located at setup/For Mac/ inside the project folder."
    echo ""
    read -p "Press Enter to exit..."
    exit 1
fi

# ---- Check that secrets/.env exists ----
if [ ! -f secrets/.env ]; then
    echo "ERROR: secrets/.env file not found."
    echo "Please follow Part 4c of the setup guide to create it."
    echo ""
    read -p "Press Enter to exit..."
    exit 1
fi

# ---- Check that secrets/service-account.json exists ----
if [ ! -f secrets/service-account.json ]; then
    echo "ERROR: secrets/service-account.json not found."
    echo "Please place your Google service account credentials file"
    echo "in the secrets/ folder before running this script."
    echo ""
    read -p "Press Enter to exit..."
    exit 1
fi

# ---- Install dependencies ----
echo "Step 1 of 2: Installing Python dependencies..."
echo "This may take a few minutes on the first run."
echo ""
"$PYTHON" -m pip install --upgrade pip
"$PYTHON" -m pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo ""
    echo "ERROR: Dependency installation failed."
    echo "Review the error messages above and reach out for help."
    echo ""
    read -p "Press Enter to exit..."
    exit 1
fi

echo ""
echo "Dependencies installed successfully."
echo ""

# ---- Run the pipeline ----
echo "Step 2 of 2: Building the knowledge base..."
echo ""
echo "This connects to Google Drive, downloads documents, runs AI"
echo "processing, and builds the searchable vector database."
echo ""
echo "Expected time: 20 to 60 minutes depending on corpus size."
echo "The window will show progress as each step completes."
echo "Do not close this window until you see \"Build complete.\""
echo ""

"$PYTHON" pipeline/__init__.py

if [ $? -ne 0 ]; then
    echo ""
    echo "ERROR: The pipeline did not complete successfully."
    echo "Review the error messages above and reach out for help."
    echo ""
    read -p "Press Enter to exit..."
    exit 1
fi

echo ""
echo "============================================================"
echo " Build complete."
echo " You can now launch the app using 2_run_app.sh"
echo "============================================================"
echo ""
read -p "Press Enter to close..."
