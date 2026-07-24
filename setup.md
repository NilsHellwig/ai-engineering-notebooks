# Setup Guide

This guide walks you through setting up your computer for this course, step by step. No prior programming experience needed — just copy and paste the commands into a **terminal**.

- **macOS:** Open the app "Terminal" (search for it with Spotlight, `Cmd + Space`).
- **Windows:** Open "PowerShell" (search for it in the Start menu).
- **Linux:** Open your terminal application.

---

## 1. Install `uv`

`uv` is a tool that installs Python and manages the packages (add-on libraries) used in the notebooks for you.

**macOS / Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

After installation, close and reopen your terminal, then check that it worked:
```bash
uv --version
```
You should see a version number printed (e.g. `uv 0.9.x`).

---

## 2. Create your course folder

When you open your terminal, it always starts in your personal home folder — the same one that contains your `Desktop`, `Documents`, etc. We'll create the course folder on your Desktop, so it's easy to find later. Type each command below one at a time and press Enter after each. `cd` means "go to this folder", `mkdir` means "create a folder".

### macOS

```bash
cd Desktop
mkdir ai-engineering-course
cd ai-engineering-course
mkdir chapter
```

### Windows (PowerShell)

```powershell
cd Desktop
mkdir ai-engineering-course
cd ai-engineering-course
mkdir chapter
```

### Linux

```bash
cd ~/Desktop
mkdir ai-engineering-course
cd ai-engineering-course
mkdir chapter
```

You should now see a new `ai-engineering-course` folder on your Desktop — take a look in Finder/File Explorer. Tip: if you ever get lost in the terminal, `pwd` prints the folder you're currently in.

You do **not** need to clone the GitHub repository. Whenever a new chapter is released on the learning platform, download its folder (e.g. `01_intro_python`) and place it inside your `chapter` folder — either by dragging it there in Finder/File Explorer, or by moving the download into `ai-engineering-course/chapter/` — so you end up with:

```
ai-engineering-course/
├── requirements.txt
└── chapter/
    ├── 01_python/
    ├── 02_nlp_in_python/
    └── ...
```

---

## 3. Create a virtual environment

A virtual environment is an isolated space for this course's Python packages, so they don't interfere with anything else on your computer. Make sure your terminal is still inside `ai-engineering-course`, then create it:

```bash
uv venv
```

Now activate it — you'll need to repeat this "activate" step every time you open a new terminal to work on the course.

### macOS

```bash
source .venv/bin/activate
```

### Windows (PowerShell)

```powershell
.venv\Scripts\activate
```

### Linux

```bash
source .venv/bin/activate
```

If it worked, you should see `(.venv)` appear at the start of your terminal prompt.

---

## 4. Install all required packages

All packages needed across every notebook are listed with fixed (pinned) versions in one file: [`requirements.txt`](requirements.txt). Download it directly from GitHub into your `ai-engineering-course` folder (do **not** clone the repository). Make sure your terminal is still inside `ai-engineering-course`.

### macOS

```bash
curl -L -o requirements.txt https://raw.githubusercontent.com/NilsHellwig/ai-engineering-notebooks/main/requirements.txt
```

### Windows (PowerShell)

```powershell
Invoke-WebRequest -Uri https://raw.githubusercontent.com/NilsHellwig/ai-engineering-notebooks/main/requirements.txt -OutFile requirements.txt
```

### Linux

```bash
curl -L -o requirements.txt https://raw.githubusercontent.com/NilsHellwig/ai-engineering-notebooks/main/requirements.txt
```

If none of these work, simply open that link in your browser and save the page as `requirements.txt` in your `ai-engineering-course` folder.

Now install everything with one command — this is the same on macOS, Windows and Linux:

```bash
uv pip install -r requirements.txt
```

This installs Jupyter Lab and all packages needed for chapters 01–07 (this may take a few minutes).

Two small language models are also required for chapter 02 (NLP) — again, the same command on all systems:

```bash
uv run python -m spacy download en_core_web_sm
uv run python -m spacy download de_core_news_sm
```

---

## 5. Launch Jupyter Lab

From inside your `ai-engineering-course` folder (with the virtual environment activated). This command is identical on all systems:

### macOS

```bash
uv run jupyter lab
```

### Windows (PowerShell)

```powershell
uv run jupyter lab
```

### Linux

```bash
uv run jupyter lab
```

This opens Jupyter Lab in your browser. Navigate into the `chapter` folder and open the notebook for the current chapter.

---

# Starting Work Next Time (Do This Every Time!)

Steps 1–4 above are a **one-time setup**. Once they're done, you do **not** need to repeat them. But every time you come back to work on the course — a new day, after restarting your computer, after closing the terminal — you need to redo these three quick steps to get going again.

### macOS

```bash
cd Desktop/ai-engineering-course
source .venv/bin/activate
uv run jupyter lab
```

### Windows (PowerShell)

```powershell
cd Desktop\ai-engineering-course
.venv\Scripts\activate
uv run jupyter lab
```

### Linux

```bash
cd ~/Desktop/ai-engineering-course
source .venv/bin/activate
uv run jupyter lab
```

That's it — Jupyter Lab opens in your browser, ready to go.
