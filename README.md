# 🤖 AI Engineering Course - Jupyter Notebooks

<div align="center">

<img src="https://upload.wikimedia.org/wikipedia/commons/0/0f/Universit%C3%A4t_Regensburg_logo.svg" alt="University of Regensburg Logo" width="300">

**Chair of Media Informatics**  
**Faculty of Informatics and Data Science (FIDS)**  
**University of Regensburg**

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

</div>

---

A comprehensive collection of Jupyter notebooks covering fundamental concepts and advanced techniques in AI Engineering, from Python basics to building interactive AI applications.

---

## 👤 Author

**Nils Constantin Hellwig, M.Sc.**  
Research Associate at the Chair of Media Informatics  
Faculty of Informatics and Data Science (FIDS)  
University of Regensburg  
93040 Regensburg, Germany

📧 **Email:** [Nils-Constantin.Hellwig@informatik.uni-regensburg.de](mailto:Nils-Constantin.Hellwig@informatik.uni-regensburg.de)  
🌐 **Website:** [https://go.ur.de/nils-hellwig](https://go.ur.de/nils-hellwig)  
🐙 **GitHub:** [@NilsHellwig](https://github.com/NilsHellwig)  
🎓 **ORCID:** [0009-0000-7305-8797](https://orcid.org/0009-0000-7305-8797)  
📚 **Google Scholar:** [Profile](https://scholar.google.com/citations?user=VzUTKcwAAAAJ)  
💼 **LinkedIn:** [Nils Hellwig](https://www.linkedin.com/in/nils-h-748711229)  


---


## 📚 Course Contents

### **01 - Introduction to Python**
`chapter/01_python/01_intro_python.ipynb`

Foundation in Python programming essentials for AI development, from your very first `print()` statement onward.

**Topics covered:**
- Variables, basic data types, and type conversion
- Arithmetic, comparison, and logical operators
- Control flow (`if`/`elif`/`else`) and loops (`for`, `while`)
- Strings & f-strings, lists, tuples, sets, and dictionaries
- Functions with default parameters and `*args`
- Object-oriented programming: classes, inheritance, and polymorphism

**Includes:** Hands-on exercises with solutions

---

### **02 - Introduction to NLP in Python**
`chapter/02_nlp_in_python/02_intro_nlp_in_python.ipynb`

Natural Language Processing fundamentals using modern Python libraries.

**Topics covered:**
- **Tokenization** with NLTK and spaCy
- **Part-of-Speech (POS) Tagging** for English and German
- **Lemmatization and Stemming** techniques
- **Regular Expressions (RegEx)** for pattern matching and text extraction
- **Word Embeddings** and Vector Space Models with cosine similarity
- **Pandas basics** for working with text datasets (CSV files)
- **NumPy basics** for numerical computations and array operations

**Includes:** Practical exercises with real-world tweet sentiment analysis

---

### **03 - Introduction to Prompting**
`chapter/03_prompting/03_intro_prompting.ipynb`

Prompting strategies for Large Language Models (LLMs), and the Chat vs. Completions APIs underneath them.

**Topics covered:**
- **Chat Completions API** vs. the (legacy) raw **Completions API**
- **Zero-shot** and **Few-shot Prompting**
- **Chain of Thought (CoT)** - the classic trigger-phrase technique, and how native "thinking" models make it largely unnecessary
- **Self-Consistency** - majority voting for improved accuracy
- A from-scratch look at Gemma 4's raw chat template (tokens, turns, thinking)

**Includes:** Named Entity Recognition exercise with evaluation

---

### **04 - LLM Parameters & Structured Outputs**
`chapter/04_llm_parameters_structured_outputs/`

`04_intro_llm_parameters_structured_outputs.ipynb` - the five LLM inference parameters (context size, `temperature`, `top_p`/`top_k`, `max_tokens`, `stop`), then Pydantic basics (models, validation, `Field()`, `Literal`, nested models, JSON Schema), then structured LLM output via `response_format` and regex-constrained output.

**Includes:** Classification and information extraction from text

---

### **05 - Agents & Model Context Protocol (MCP)**
`chapter/05_agents/`

Four notebooks, meant to be read in order:

- **Part 1:** `05_1_agents.ipynb` - tool calling with the `ollama` package (single and multiple tools, the agent loop), the same with LangChain's `create_agent`, and the ReAct pattern
- **Part 2:** `05_2_mcp.ipynb` - what MCP is, building an MCP server with FastMCP (tools, resources, prompts), connecting a client to it, and using its tools in a LangChain agent
- **Part 3:** `05_3_context_memory.ipynb` - context compression (summarization, clearing old tool outputs), short-term vs. long-term memory, and LLM call caching
- **Part 4:** `05_4_subagents.ipynb` - multi-agent delegation: wrapping an agent as a tool for another agent to call, context quarantine, and choosing between several specialist subagents

**Includes:** Exercises with a real, free exchange-rate API (Frankfurter) and a small custom MCP server (`mcp_server.py`) with a university library catalog example

---

### **06 - Retrieval-Augmented Generation (RAG)**
`chapter/06_rag/`

Three notebooks, one per RAG architecture, meant to be read in order:

- **Part 1:** `06_1_two_step_rag.ipynb` - RAG fundamentals (`Document`s, loaders, text splitting, embeddings, vector stores), keyword search (BM25) vs. semantic search, and the simplest architecture: always retrieve, then generate
- **Part 2:** `06_2_agentic_rag.ipynb` - wrapping retrieval as a tool and letting an LLM agent (`create_agent`) decide if, when, and how many times to retrieve
- **Part 3:** `06_3_hybrid_rag.ipynb` - Corrective RAG as an explicit `StateGraph`: query rewriting, document relevance grading, and answer validation with a self-correcting retry loop

**Includes:** A real knowledge base of 500 customer tweets about airlines (with cached embeddings), reused and rebuilt across all three notebooks

---

### **07 - Introduction to Gradio**
`chapter/07_gradio/07_intro_gradio.ipynb`

Building interactive web interfaces for AI applications.

**Topics covered:**
- **Gradio components**, layouts, and events
- **Blocks**, tabs, and connecting layouts
- **Chatbot interfaces** for conversational AI
- **Structured output in a real UI** (Aspect-Based Sentiment Analysis)

**Includes:** Complete examples from simple UIs to chatbots

---

### **08 - Deep Agents**
`chapter/08_deep_agents/08_intro_deep_agents.ipynb`

The `deepagents` "agent harness": `create_deep_agent`, the built-in virtual filesystem (`ls`, `read_file`, `write_file`, `edit_file`), swapping in a real-disk backend, and task planning with `write_todos`. Delegation (covered by hand first in `05_4_subagents.ipynb`) and human-in-the-loop approval are also built into `deepagents`.

**Topics covered:**
- The **agent harness** concept: `create_agent` plus built-in scaffolding for real, longer-running tasks
- A **virtual filesystem** (state-backed by default, swappable to real disk)
- **Task planning** with `write_todos`

**Includes:** A note-taking agent exercise that plans, writes, edits, and reads back multiple files

---

### **09 - Testing & Observability** ⚠️ *Advanced, optional — not part of the core course scope*
`chapter/09_observability/`

Three notebooks: a general-purpose testing notebook that needs nothing beyond the standard install, plus two notebooks covering the same observability concepts (traces, runs/observations, metadata, feedback/scores) on a different tool, each needing its own extra setup — see the note at the end of [setup.md](setup.md).

- **Part 1:** `09_1_pytest.ipynb` - fixtures, parametrize, marks (skip/xfail), exception testing (`pytest.raises`), `tmp_path`, `monkeypatch`, `capsys`, assertion introspection, `conftest.py`, and selecting/rerunning tests (`-k`/`-m`/`-x`/`--lf`) — using [pytest](https://docs.pytest.org/) (just a pip package, no extra setup)
- **Part 2:** `09_2_langsmith.ipynb` - observability concepts (projects, traces, runs, threads), manual instrumentation (`wrap_openai`, `@traceable`) against our own Ollama endpoint, automatic zero-code tracing for LangChain/LangGraph agents, metadata, and feedback — using [LangSmith](https://smith.langchain.com/) (hosted, free tier)
- **Part 3:** `09_3_langfuse.ipynb` - the same ideas on [Langfuse](https://langfuse.com/) (open-source, self-hosted via Docker Compose) — includes step-by-step container setup with headless auto-provisioning, since LangSmith's self-hosting option is Enterprise-only

**Includes:** A real pytest test suite (`content/tests/`) covering a library-management module end to end, plus a real self-hosted Langfuse stack (Postgres, ClickHouse, Redis, MinIO) via Docker Compose, with a ready-to-use `docker-compose.yml`

---

## 🚀 Getting Started

See **[setup.md](setup.md)** for full step-by-step installation instructions (installing `uv`, setting up your project folder, installing the pinned Python packages, and connecting to the course's LLM server via a `.env` file) — separately for macOS, Windows, and Linux. You don't clone this repository as a student; chapter folders are downloaded individually from the learning platform.

---

## 📖 How to Use These Notebooks

1. **Sequential Learning:** Start with chapter 01 and progress through the series. Within a chapter folder that has multiple notebooks (e.g. 05, 06, 09), they're numbered `NN_1_...`, `NN_2_...`, etc. — work through them in that order.
2. **Interactive Execution:** Run code cells to see results and experiment with modifications.
3. **Practice Exercises:** Complete the exercises at the end of each notebook.
4. **Solutions Provided:** Expand the solution sections to check your work.

---


## 📝 Resources

- [Stanford NLP Book (Jurafsky & Martin)](https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf)
- [Prompting Guide](https://www.promptingguide.ai/techniques)
- [OpenAI Function Calling API](https://platform.openai.com/docs/guides/function-calling)
- [OpenAI Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)
- [Pydantic Documentation](https://pydantic.dev/)
- [Ollama Documentation](https://ollama.com/) & [Ollama: Tool Calling](https://docs.ollama.com/capabilities/tool-calling)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/) & [FastMCP Documentation](https://gofastmcp.com/)
- [LangChain: Agents](https://docs.langchain.com/oss/python/langchain/agents)
- [LangChain: Retrieval](https://docs.langchain.com/oss/python/langchain/retrieval)
- [LangChain: Multi-agent](https://docs.langchain.com/oss/python/langchain/multi-agent)
- [LangChain: Human-in-the-loop](https://docs.langchain.com/oss/python/langchain/human-in-the-loop)
- [LangChain: Deep Agents Overview](https://docs.langchain.com/oss/python/deepagents/overview)
- [pytest Documentation](https://docs.pytest.org/)
- [LangSmith: Observability concepts](https://docs.langchain.com/langsmith/observability-concepts)
- [Langfuse: Docker Compose self-hosting guide](https://langfuse.com/self-hosting/deployment/docker-compose)
- [Hugging Face: `iecjsu/airlineSFT_All` dataset](https://huggingface.co/datasets/iecjsu/airlineSFT_All)
- Yao et al. (2022), [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/pdf/2210.03629)
- [Gradio Documentation](https://www.gradio.app/docs/)
- [spaCy Documentation](https://spacy.io/)
- [NLTK Documentation](https://www.nltk.org/)
- [RegExr - Regular Expression Tester](https://regexr.com/)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/NilsHellwig/ai-engineering-notebooks/issues).

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⭐ Acknowledgments

- Thanks to all students and contributors who helped improve these materials.

---

<div align="center">

[⬆ Back to Top](#-ai-engineering-course---jupyter-notebooks)

</div>
