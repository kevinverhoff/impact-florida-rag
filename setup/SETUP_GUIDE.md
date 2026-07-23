# Impact Florida RAG Tool — Setup Guide

Follow these steps in order. Each section builds on the previous one. Steps are split into **Windows** and **Mac** — just follow the column that matches your computer. If anything goes wrong, note the error message and reach out for help.

You will need the following items, which will be provided to you separately:

- **service-account.json** — a credential file for accessing Google Drive
- A **.env** file (which we will share) that has:
  - The **Shared Drive ID** — a string of letters and numbers from the Google Drive URL
  - An **OpenAI API key** — starts with `sk-`

Put these files in a folder named `secrets` and keep these somewhere easy to find (like your Desktop) while you work through setup.

---

## Part 1: Install Python

Python is the programming language that runs this tool.

**On Windows:**

1. Open your web browser and go to: https://www.python.org/downloads/
2. Click the large yellow "Download Python 3.x.x" button (the exact version number doesn't matter — any 3.11 or 3.12 version is fine).
3. Run the downloaded installer.
4. **Important:** On the first screen of the installer, check the box that says "Add Python to PATH" before clicking Install Now.

   *(Screenshot: check "Add Python to PATH" at the bottom of the first installer screen)*

5. Click Install Now and wait for the installation to finish.
6. Click Close when done.

To verify Python installed correctly:

1. Press `Windows key + R`, type `cmd`, and press Enter to open a Command Prompt window.
2. Type `python --version` and press Enter.
3. You should see something like `Python 3.12.3`. If you see an error, reach out for help.

**On Mac:**

1. Open your web browser and go to: https://www.python.org/downloads/
2. Click the large yellow "Download Python 3.x.x" button (any 3.11 or 3.12 version is fine).
3. Open the downloaded `.pkg` file and click through the installer (Continue → Continue → Agree → Install).
4. Enter your Mac password if prompted, and wait for the installation to finish.
5. Click Close when done.

To verify Python installed correctly:

1. Open Terminal (press `Cmd + Space`, type `Terminal`, press Enter).
2. Type `python3 --version` and press Enter.
3. You should see something like `Python 3.12.3`. If you see an error, reach out for help.

---

## Part 2: Install Git

Git is a tool for downloading code from the internet.

**On Windows:**

1. Go to: https://git-scm.com/download/win
2. The download should start automatically. If not, click the link for the 64-bit Windows installer.
3. Run the installer. You can accept all the default settings by clicking Next through each screen, then Install.
4. Click Finish when done.

To verify Git installed correctly:

1. Open a new Command Prompt window (close and reopen if you already had one open).
2. Type `git --version` and press Enter.
3. You should see something like `git version 2.x.x`. If you see an error, reach out for help.

**On Mac:**

1. Open Terminal (press `Cmd + Space`, type `Terminal`, press Enter).
2. Type `git --version` and press Enter.
3. If Git isn't installed yet, macOS will pop up a prompt offering to install the "Command Line Developer Tools." Click **Install**, accept the license agreement, and wait for it to finish — this installs Git for you.
4. Once it's done, run `git --version` again.
5. You should see something like `git version 2.x.x`. If you see an error, reach out for help.

---

## Part 3: Clone the Repository

"Cloning" downloads all the project files to your computer.

**On Windows:**

1. Decide where you want to put the project folder. Your Desktop or Documents folder works well.
2. Open a Command Prompt window.
3. Navigate to that location. For example, to go to your Desktop:

   ```
   cd %USERPROFILE%\Desktop
   ```

4. Run this command to download the project:

   ```
   git clone https://github.com/kevinverhoff/impact-florida-rag.git
   ```

5. Wait for it to finish. You will see a new folder called `impact-florida-rag` appear in the chosen location.
6. Close the Command Prompt window.

**On Mac:**

1. Decide where you want to put the project folder. Your Desktop or Documents folder works well.
2. Open Terminal.
3. Navigate to that location. For example, to go to your Desktop:

   ```
   cd ~/Desktop
   ```

4. Run this command to download the project:

   ```
   git clone https://github.com/kevinverhoff/impact-florida-rag.git
   ```

5. Wait for it to finish. You will see a new folder called `impact-florida-rag` appear in the chosen location.
6. Close the Terminal window.

---

## Part 4: Add Your Credential Files

If you already have the secrets saved somewhere, now you can move them into the folder where the repository was just created. If not, follow the steps below.

### 4a. Create the secrets folder

**On Windows:**

1. Open the `impact-florida-rag` folder on your computer.
2. Inside it, create a new folder called exactly `secrets` (all lowercase).

**On Mac:**

1. Open the `impact-florida-rag` folder in Finder.
2. Inside it, create a new folder called exactly `secrets` (all lowercase) — right-click in the window and choose New Folder.

### 4b. Add the service account JSON

**On Windows:**

1. Take the `service-account.json` file you were given and copy it into the `secrets` folder.
2. Make sure the file is named exactly `service-account.json`.

**On Mac:**

1. Take the `service-account.json` file you were given and copy it into the `secrets` folder.
2. Make sure the file is named exactly `service-account.json` (Finder hides file extensions by default, so double-check under Get Info if you're not sure).

### 4c. Create the .env file

The `.env` file holds your configuration settings.

**On Windows:** You will create it using Notepad.

1. Open Notepad (search for it in the Start menu).
2. Copy and paste the following three lines into Notepad, replacing the placeholder values with your actual information:

   ```
   SERVICE_ACCOUNT_FILE=secrets/service-account.json

   SHARED_DRIVE_ID=your-drive-id-here

   OPENAI_API_KEY=sk-your-key-here
   ```

3. Replace `your-drive-id-here` with the Shared Drive ID you were given. It is the string of characters at the end of the Google Drive URL (e.g., `https://drive.google.com/drive/folders/1ABC...XYZ` — the part after `folders/`).
4. Replace `sk-your-key-here` with your OpenAI API key.
5. In Notepad, go to **File → Save As**.
6. Navigate to the `secrets` folder inside `impact-florida-rag`.
7. In the "File name" box, type: `.env` (just a dot, then "env" — no other characters).
8. In the "Save as type" dropdown, select **"All Files (*.*)"** — this is important, otherwise Windows will save it as `.env.txt`.
9. Click Save.

**On Mac:** Don't use TextEdit or Finder to create this file — two things about how Mac handles it by default will trip you up:

1. **Finder hides the file after you create it.** Files that start with a dot (like `.env`) are treated as hidden by macOS. If you don't see it in the `secrets` folder afterward, that's expected — it's there, just hidden. (To check, in Finder press `Cmd + Shift + .` to toggle showing hidden files.)
2. **TextEdit silently appends `.txt`.** If you create the file in TextEdit and type `.env` as the file name, macOS will often save it as `.env.txt` instead — and because extensions are hidden by default, it *looks* like `.env` in Finder even though it isn't. This is the Mac equivalent of the Windows "Save as type: All Files" problem above.

The reliable way around both problems is to create the file from Terminal instead:

1. Open Terminal and navigate to the `secrets` folder, for example:

   ```
   cd ~/Desktop/impact-florida-rag/secrets
   ```

2. Create the file and open it for editing:

   ```
   touch .env
   open -e .env
   ```

3. This opens an empty file named exactly `.env` in TextEdit. Paste in the three lines below, replacing the placeholder values with your actual information:

   ```
   SERVICE_ACCOUNT_FILE=secrets/service-account.json

   SHARED_DRIVE_ID=your-drive-id-here

   OPENAI_API_KEY=sk-your-key-here
   ```

4. Replace `your-drive-id-here` with the Shared Drive ID you were given. It is the string of characters at the end of the Google Drive URL (e.g., `https://drive.google.com/drive/folders/1ABC...XYZ` — the part after `folders/`).
5. Replace `sk-your-key-here` with your OpenAI API key.
6. Save with `Cmd + S`. Since the file already exists as `.env`, saving won't rename or add an extension to it.
7. To double-check you got it right, go back to Terminal and run `ls -a` in the `secrets` folder — you should see `.env` listed (not `.env.txt`).

Your repo (`impact-florida-rag`) should now look like:

```
impact-florida-rag/
    secrets/
        service-account.json
        .env
    app/
    pipeline/
    ...
```

---

## Part 5: Install Requirements and Build the Knowledge Base

This step downloads all the software the tool needs and then builds the searchable document database. This will take 20–60 minutes the first time — it downloads documents from Google Drive and runs AI processing on them. You can let it run in the background.

**On Windows:**

1. Inside the `impact-florida-rag` folder, open the `setup\For Windows` folder and find the file called `1_setup_and_build.bat`.
2. Double-click it.
3. A black Command Prompt window will open and you will see text scrolling by. This is normal.
4. Wait until you see a line that says `Build complete.` or the window stops scrolling and shows a final message.
5. If you see any red error text, do not close the window — take a screenshot and reach out for help.

**Note:** If Windows asks "Do you want to allow this app to make changes?" click Yes.

**On Mac:**

1. Open Terminal and navigate to the setup folder inside the project:

   ```
   cd ~/Desktop/impact-florida-rag/setup/"For Mac"
   ```

2. The first time only, make the script runnable:

   ```
   chmod +x 1_setup_and_build.sh 2_run_app.sh
   ```

3. Run the setup script:

   ```
   ./1_setup_and_build.sh
   ```

4. You will see text scrolling by in the Terminal window. This is normal.
5. Wait until you see a line that says `Build complete.` or the window stops scrolling and shows a final message.
6. If you see any red `ERROR:` text, don't close the window — take a screenshot and reach out for help.

**Note:** If Terminal shows `permission denied` when you try to run `./1_setup_and_build.sh`, it means step 2 (the `chmod +x` command) was skipped or didn't run — go back and run it.

**Either way:** This will take some time, and you may notice your computer running a little more slowly. This is not an operation you will run very often.

---

## Part 6: Launch the App

Once the build is complete (Part 5 finished successfully), you can launch the tool any time.

**Note:** The launch script automatically figures out how to start the app — it tries `python`, then `python3`, and if neither is found on your PATH it falls back to running `streamlit` directly. You shouldn't need to think about which one is installed; if all three are missing, the script will tell you.

**On Windows:**

1. Inside the `impact-florida-rag` folder, open the `setup\For Windows` folder and find the file called `2_run_app.bat`.
2. Double-click it.
3. A black Command Prompt window will open and you will see a message like:

   ```
   You can now view your Streamlit app in your browser.
   Local URL: http://localhost:8501
   ```

4. Your web browser should open automatically to the app. If it doesn't, open your browser and go to: http://localhost:8501
5. The app is now running. Use it like a normal website — type questions in the chat box and use the sidebar filters to narrow results.

**To stop the app:** Click on the black Command Prompt window and press `Ctrl + C`, then close the window.

**On Mac:**

1. Open Terminal and navigate to the setup folder inside the project:

   ```
   cd ~/Desktop/impact-florida-rag/setup/"For Mac"
   ```

2. Run:

   ```
   ./2_run_app.sh
   ```

3. You will see a message like:

   ```
   You can now view your Streamlit app in your browser.
   Local URL: http://localhost:8501
   ```

4. Your web browser should open automatically to the app. If it doesn't, open your browser and go to: http://localhost:8501
5. The app is now running. Use it like a normal website — type questions in the chat box and use the sidebar filters to narrow results.

**To stop the app:** Click on the Terminal window and press `Ctrl + C`.

---

## Part 7: Running the App in the Future

After the initial setup is complete, you only need Part 6 going forward:

**On Windows:**

1. Double-click `2_run_app.bat` in `setup\For Windows`
2. Open your browser to http://localhost:8501

**On Mac:**

1. Open Terminal, `cd` into `setup/For Mac`, and run `./2_run_app.sh`
2. Open your browser to http://localhost:8501

The knowledge base (built in Part 5) is saved on your computer and does not need to be rebuilt unless the documents in Google Drive change significantly.

---

## Appendix: Running the Commands Manually

The `.bat` and `.sh` files in Parts 5 and 6 just run a couple of commands for you. If you'd rather type the commands yourself (or the scripts aren't working for some reason), here's what they do under the hood.

For all of the commands below, first open Command Prompt (Windows) or Terminal (Mac) and navigate to the project folder:

**On Windows:**

```
cd %USERPROFILE%\Desktop\impact-florida-rag
```

**On Mac:**

```
cd ~/Desktop/impact-florida-rag
```

*(Adjust the path if you put the `impact-florida-rag` folder somewhere other than your Desktop.)*

### Manual equivalent of Part 5 (install requirements + build the knowledge base)

Run these two commands in order, one at a time, waiting for each to finish:

```
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

```
python pipeline/__init__.py
```

If `python` isn't recognized, try `python3` instead of `python` in both commands above. The pipeline step is the one that takes 20–60 minutes — wait until it finishes and returns you to the command prompt before moving on.

### Manual equivalent of Part 6 (launch the app)

```
python -m streamlit run app/app.py
```

If `python` isn't recognized, try one of these instead:

```
python3 -m streamlit run app/app.py
```

```
streamlit run app/app.py
```

Once you see `Local URL: http://localhost:8501` in the output, open that address in your browser. To stop the app, press `Ctrl + C` in the same window.

---

## Troubleshooting

| Symptom | Likely cause | What to do |
|---|---|---|
| `python` is not recognized (Windows) | Python not installed or PATH not set | Reinstall Python, make sure "Add to PATH" is checked |
| `python3: command not found` (Mac) | Python not installed | Reinstall Python from python.org |
| `git` is not recognized (Windows) | Git not installed | Reinstall Git; close and reopen Command Prompt after |
| `git` prompts to install Command Line Tools (Mac) | Git not installed yet | Click Install and wait; this is expected the first time |
| `permission denied` running `./1_setup_and_build.sh` or `./2_run_app.sh` (Mac) | Script isn't marked executable | Run `chmod +x 1_setup_and_build.sh 2_run_app.sh` in that folder, then try again |
| `ERROR: Could not find "python", "python3", or "streamlit"` | None of the three are installed or on PATH | Reinstall Python from python.org (Windows: check "Add to PATH") and re-run Part 5 |
| Red error about `secrets/.env` | `.env` file missing or saved as `.env.txt` | Check the file name in the `secrets` folder; re-create using the steps in Part 4c |
| Red error about `service-account.json` | File missing or misnamed | Confirm the file is in the `secrets` folder with that exact name |
| App opens but returns no results | Knowledge base not built yet | Make sure Part 5 finished without errors before launching the app |
| Browser does not open automatically | Streamlit didn't auto-launch | Manually go to http://localhost:8501 in your browser |

If you encounter an error not listed here, copy the full error message (or take a screenshot) and send it over — it will make diagnosing the issue much faster.
