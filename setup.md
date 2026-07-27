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
├── pyproject.toml
├── uv.lock
└── chapter/
    ├── 01_python/
    ├── 02_nlp_in_python/
    └── ...
```

---

## 3. Download the project files

Two files together describe every package this course needs, with exact versions pinned so everyone's setup matches: [`pyproject.toml`](pyproject.toml) (the package list) and [`uv.lock`](uv.lock) (the exact resolved versions of those packages, and everything they depend on). Download both directly from GitHub into your `ai-engineering-course` folder (do **not** clone the repository). Make sure your terminal is still inside `ai-engineering-course`.

### macOS

```bash
curl -L -o pyproject.toml https://raw.githubusercontent.com/NilsHellwig/ai-engineering-notebooks/main/pyproject.toml
curl -L -o uv.lock https://raw.githubusercontent.com/NilsHellwig/ai-engineering-notebooks/main/uv.lock
```

### Windows (PowerShell)

```powershell
Invoke-WebRequest -Uri https://raw.githubusercontent.com/NilsHellwig/ai-engineering-notebooks/main/pyproject.toml -OutFile pyproject.toml
Invoke-WebRequest -Uri https://raw.githubusercontent.com/NilsHellwig/ai-engineering-notebooks/main/uv.lock -OutFile uv.lock
```

### Linux

```bash
curl -L -o pyproject.toml https://raw.githubusercontent.com/NilsHellwig/ai-engineering-notebooks/main/pyproject.toml
curl -L -o uv.lock https://raw.githubusercontent.com/NilsHellwig/ai-engineering-notebooks/main/uv.lock
```

If none of these work, simply open both links in your browser and save each page under the exact file name shown (`pyproject.toml` and `uv.lock`) into your `ai-engineering-course` folder.

---

## 4. Create the virtual environment and install all packages

Make sure your terminal is still inside `ai-engineering-course`, then run this one command — it's the same on macOS, Windows and Linux:

```bash
uv sync
```

`uv sync` reads `pyproject.toml`/`uv.lock`, creates an isolated virtual environment for this course in a new `.venv` folder (so these packages don't interfere with anything else on your computer), and installs Jupyter Lab plus every package needed for chapters 01–09 at the exact pinned version (this may take a few minutes) — including `pytest` for chapter 10's testing notebook. Chapter 10's LangSmith/Langfuse notebooks are optional and advanced — see the note at the end of this guide.

Now activate the environment — you'll need to repeat this "activate" step every time you open a new terminal to work on the course.

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

Two small language models are also required for chapter 02 (NLP) — again, the same command on all systems:

```bash
uv run python -m spacy download en_core_web_sm
uv run python -m spacy download de_core_news_sm
```

---

## 5. Create your `.env` file

From chapter 03 onward, notebooks connect to an LLM server. Its address is kept out of the notebooks (and out of the public GitHub repo) and instead read from a file named `.env`, which you create yourself, once, in your `ai-engineering-course` folder.

- **Taking this as part of the course?** You'll get the IP address in the lecture.
- **Studying on your own with your own local Ollama install instead?** Use `localhost`.

Create the file with a single command — this creates `.env` with one line in it. Replace the value with the address you got in the lecture (or `localhost`):

### macOS / Linux

```bash
echo "LLM_HOST=<the IP address from the lecture, or localhost>" > .env
```

### Windows (PowerShell)

```powershell
echo "LLM_HOST=<the IP address from the lecture, or localhost>" > .env
```

For example, if you were given `203.0.113.42`, the command would be `echo "LLM_HOST=203.0.113.42" > .env`. This only needs to be done once — `.env` stays in your `ai-engineering-course` folder for every future session, and (like `.venv`) it's excluded from git via `.gitignore`, so it's safe to keep secrets like this in it.

---

## 6. Launch Jupyter Lab

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

---

## ⚠️ Optional: Chapter 10 (Advanced) — Testing & Observability

Two of chapter 10's three notebooks are **not part of the course scope**. `10_1_pytest.ipynb` needs nothing beyond the standard install above - it's just the `pytest` package. The other two notebooks use external observability tools, each needing its own extra setup beyond anything else in this course:

- **`10_2_langsmith.ipynb`** needs a free [smith.langchain.com](https://smith.langchain.com/) account and API key (no credit card required) — see the notebook itself for the exact steps.
- **`10_3_langfuse.ipynb`** needs [Docker](https://www.docker.com/products/docker-desktop/) installed and running on your machine, since it self-hosts an open-source observability stack locally — again, the notebook walks through this step by step.

Only work through the LangSmith/Langfuse notebooks if you're specifically interested in observability tooling for LLM applications - everything through chapter 09, and `10_1_pytest.ipynb`, works without either of them.
