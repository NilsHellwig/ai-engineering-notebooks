# 🤖 AI Engineering Course - Jupyter Notebooks

<div align="center">

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Universit%C3%A4t_Regensburg_logo.svg/2560px-Universit%C3%A4t_Regensburg_logo.svg.png" alt="University of Regensburg Logo" width="300">

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
`Notebooks/01_intro_python.ipynb`

Foundation in Python programming essentials for AI development.

**Topics covered:**
- Variables and data types (strings, integers, floats, booleans, lists, dictionaries)
- String operations and F-String formatting
- List operations and comprehensions
- Dictionary operations for text processing
- Functions with default parameters and `*args`
- Object-oriented programming: classes, inheritance, and polymorphism

**Includes:** Hands-on exercises with solutions

---

### **02 - Introduction to NLP in Python**
`Notebooks/02_intro_nlp_in_python.ipynb`

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
`Notebooks/03_intro_prompting.ipynb`

Advanced prompting strategies for Large Language Models (LLMs).

**Topics covered:**
- **Zero-shot Prompting** - Direct task execution without examples
- **Few-shot Prompting** - Learning from examples for better performance
- **Chain of Thought (CoT)** - Step-by-step reasoning for complex tasks
- **Self-Consistency** - Majority voting for improved accuracy
- **Generated Knowledge Prompting** - Leveraging model knowledge

**Includes:** Named Entity Recognition exercise with evaluation

---

### **04 - Introduction to Structured Outputs**
`Notebooks/04_intro_structured_outputs.ipynb`

Generating and validating structured outputs from LLMs using JSON schemas.

**Topics covered:**
- **JSON fundamentals** and data structures
- **Pydantic models** for data validation
- **Structured extraction** from text and images
- **Document analysis** and information extraction
- **Schema definition** with Field validations

**Includes:** Invoice processing and multi-modal document extraction

---

### **05 - Introduction to Function Calling**
`Notebooks/05_intro_function_calling.ipynb`

Implementing function calling to extend LLM capabilities.

**Topics covered:**
- **Tool definition** with JSON schemas
- **Function execution** workflows
- **API integration** with real-world services
- **Tool calling patterns** for LLMs
- **Building interactive pipelines**

**Includes:** Stock price and country information API examples

---

### **06 - Agents & Model Context Protocol (MCP)**
`chapter/06_agents/06_mcp.ipynb`

Connecting LLMs to tools exposed by a standalone MCP server, and an introduction to agents.

**Topics covered:**
- **Model Context Protocol (MCP)** fundamentals
- **Building an MCP server** with FastMCP
- **Calling MCP tools** from a Python client
- **Combining MCP tools with LLM tool calling**

**Includes:** A small custom MCP server (`mcp_server.py`) with a university library catalog example

---

### **07 - Introduction to RAG**
`chapter/07_rag/07_intro_rag.ipynb`

Retrieval Augmented Generation for knowledge-enhanced AI responses.

**Topics covered:**
- **Embeddings** and vector representations
- **Semantic search** with similarity metrics
- **Vector databases** and indexing
- **RAG pipeline architecture**
- **Document retrieval** strategies

**Includes:** Building a complete RAG system from scratch

---

### **08 - Introduction to Gradio**
`chapter/08_gradio/08_intro_gradio.ipynb`

Building interactive web interfaces for AI applications.

**Topics covered:**
- **Gradio components** and layouts
- **Event handling** and interactivity
- **Chatbot interfaces** for conversational AI
- **Multi-modal inputs** (text, images, audio)
- **Deployment** and sharing

**Includes:** Complete examples from simple UIs to chatbots

---

## 🚀 Getting Started

### Prerequisites

- Python 3.12 or higher
- Jupyter Notebook or JupyterLab

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/NilsHellwig/ai-engineering-notebooks.git
   cd ai-engineering-notebooks
   ```

2. **Install Ollama:**

   Ollama is required for running local Large Language Models (LLMs) used throughout the notebooks. It provides a simple API interface for interacting with various open-source models.

   **macOS:**
   ```bash
   brew install ollama
   ```

   **Linux:**
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```

   **Windows:**
   Download the installer from [ollama.com](https://ollama.com/download/windows)

   **Start Ollama server:**
   ```bash
   ollama serve
   ```

   **Pull required models** (examples used in notebooks):
   ```bash
   ollama pull gemma3:4b
   ollama pull gpt-oss:20b
   ```

   For more information, visit the [Ollama documentation](https://ollama.com/docs).

3. **Install Python dependencies:**

   Each notebook specifies its required packages. Common dependencies include:
   ```bash
   pip install jupyterlab
   ```

4. **Launch Jupyter:**
   ```bash
   jupyter lab
   ```

---

## 📖 How to Use These Notebooks

1. **Sequential Learning:** Start with notebook 01 and progress through the series
2. **Interactive Execution:** Run code cells to see results and experiment with modifications
3. **Practice Exercises:** Complete the exercises at the end of each notebook
4. **Solutions Provided:** Expand the solution sections to check your work

---


## 📝 Resources

- [Stanford NLP Book (Jurafsky & Martin)](https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf)
- [Prompting Guide](https://www.promptingguide.ai/techniques)
- [OpenAI Function Calling API](https://platform.openai.com/docs/guides/function-calling)
- [OpenAI Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)
- [Pydantic Documentation](https://pydantic.dev/)
- [Ollama Documentation](https://ollama.com/)
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

**Made with ❤️ for NLP Community**

[⬆ Back to Top](#-ai-engineering-course---jupyter-notebooks)

</div>
