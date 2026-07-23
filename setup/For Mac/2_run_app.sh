#!/bin/bash
#
# ============================================================
# 2_run_app.sh
# Impact Florida RAG Tool — Launch the App
#
# Run this any time you want to use the tool.
# The app will open in your web browser at http://localhost:8501
#
# To stop the app: press Ctrl+C in this window.
# ============================================================

echo ""
echo "============================================================"
echo " Impact Florida RAG Tool — Launching App"
echo "============================================================"
echo ""

# ---- Find a way to run Streamlit: try "python3", then "python", ----
# ---- then fall back to a bare "streamlit" command on PATH.      ----
PYTHON=""
if command -v python3 >/dev/null 2>&1; then
    PYTHON=python3
elif command -v python >/dev/null 2>&1; then
    PYTHON=python
elif ! command -v streamlit >/dev/null 2>&1; then
    echo "ERROR: Could not find \"python3\", \"python\", or \"streamlit\"."
    echo "Please install Python from https://www.python.org/downloads/"
    echo "or via Homebrew: brew install python"
    echo ""
    read -p "Press Enter to exit..."
    exit 1
fi

# ---- Move to the project root (two levels up from setup/For Mac) ----
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/../.." || exit 1

# ---- Check that the knowledge base exists ----
if [ ! -d data/chroma_db ]; then
    echo "ERROR: The knowledge base has not been built yet."
    echo "Please run 1_setup_and_build.sh first and wait for it"
    echo "to complete before launching the app."
    echo ""
    read -p "Press Enter to exit..."
    exit 1
fi

# ---- Check that the app file exists ----
if [ ! -f app/app.py ]; then
    echo "ERROR: app/app.py not found."
    echo "Make sure this script is located at setup/For Mac/ inside the project folder."
    echo ""
    read -p "Press Enter to exit..."
    exit 1
fi

echo "Starting the app..."
echo ""
echo "Once you see \"Local URL: http://localhost:8501\" below,"
echo "open your browser and go to:"
echo ""
echo "    http://localhost:8501"
echo ""
echo "(Your browser may open automatically.)"
echo ""
echo "To stop the app, press Ctrl+C in this window."
echo "============================================================"
echo ""

if [ -n "$PYTHON" ]; then
    "$PYTHON" -m streamlit run app/app.py
else
    streamlit run app/app.py
fi

echo ""
echo "App stopped."
read -p "Press Enter to close..."
