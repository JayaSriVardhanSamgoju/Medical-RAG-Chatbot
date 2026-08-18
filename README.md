# 🏥 Medical RAG Chatbot (MediMind AI)

An intelligent, full-stack **Retrieval-Augmented Generation (RAG)** Medical Chatbot built using **Flask**, **LangChain**, **FAISS**, and **Hugging Face Inference**. The system ingests medical documents/PDFs, constructs a vector knowledge database, and retrieves precise context-based answers using LLMs.

---

## 🌟 Key Features

- **Context-Aware Medical Q&A**: Uses RAG to answer queries grounded exclusively in verified medical documentation.
- **Fast FAISS Vector Database**: Employs `sentence-transformers/all-MiniLM-L6-v2` embeddings for semantic retrieval.
- **Hugging Face LLM Integration**: Integrates modern open-weights LLMs (such as `Qwen/Qwen2.5-7B-Instruct` or `Mistral`) via `ChatHuggingFace` & `HuggingFaceEndpoint`.
- **Modern Glassmorphic Web UI**: A sleek, dark-themed UI built with Flask, Vanilla CSS, FontAwesome, and interactive JavaScript with session memory and quick prompt suggestions.
- **Automated PDF Ingestion**: Load, parse, chunk, and index medical textbooks or clinical guides.
- **Modular Enterprise Architecture**: Organized into clean components with custom logging, error handling, and configuration management.

---

## 📁 Repository Structure

```
Medical RAG Chatbot/
│
├── app/
│   ├── application.py          # Flask app entry point & routes
│   ├── common/
│   │   ├── custom_exception.py # Centralized Custom Exception Handler
│   │   └── logger.py           # Custom Logging utility
│   ├── components/
│   │   ├── data_loader.py      # Data loading pipeline
│   │   ├── pdf_loader.py       # PDF document loader & text splitter
│   │   ├── embeddings.py       # SentenceTransformers embedding loader
│   │   ├── vector_store.py     # FAISS vector database builder/loader
│   │   ├── llm.py              # HuggingFace LLM initialization
│   │   └── retriever.py        # Prompt templates & QA chain construction
│   ├── config/
│   │   └── config.py           # Application constants & parameters
│   └── templates/
│       └── index.html          # Web UI interface
│
├── data/                       # Directory for medical PDF/text documents
├── vectorstore/                # Saved FAISS index (db_faiss)
├── logs/                       # Application execution logs
├── .env                        # Environment variables (API tokens)
├── requirements.txt            # Python dependencies
└── setup.py                    # Package configuration
```

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Backend Framework** | Flask |
| **RAG Framework** | LangChain Core / LangChain HuggingFace |
| **Vector Database** | FAISS (`faiss-cpu`) |
| **Embeddings** | `sentence-transformers/all-MiniLM-L6-v2` |
| **LLM Provider** | Hugging Face Serverless Inference (`Qwen/Qwen2.5-7B-Instruct`) |
| **Frontend** | HTML5, Vanilla CSS3 (Glassmorphism), JavaScript |
| **PDF Parsing** | `pypdf` / `PyPDFDirectoryLoader` |

---

## 🚀 Getting Started

### 1. Prerequisites
- Python **3.10+** installed
- A Hugging Face account and API Token ([Get Access Token](https://huggingface.co/settings/tokens))

### 2. Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/medical-rag-chatbot.git
   cd "medical-rag-chatbot"
   ```

2. **Create and activate a virtual environment**:
   - **Windows (PowerShell)**:
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   - **Linux / macOS**:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the project root:
   ```env
   HF_TOKEN="your_huggingface_api_token_here"
   ```

---

## 📥 Document Ingestion & VectorStore Build

Place your medical PDFs into the `data/` directory, then run the vector store component to create or update your FAISS database:

```bash
python -m app.components.vector_store
```

This will chunk the documents using `RecursiveCharacterTextSplitter` (chunk size: `500`, overlap: `50`) and save the index to `vectorstore/db_faiss`.

---

## 🖥️ Running the Application

Launch the Flask development server:

```bash
python app/application.py
```

Open your browser and navigate to:
```
http://127.0.0.1:5000
```

---

## ⚙️ Configuration Parameters

Key settings can be modified in `app/config/config.py`:

```python
HF_TOKEN = os.environ.get("HF_TOKEN")
HUGGINGFACE_REPO_ID = "Qwen/Qwen2.5-7B-Instruct"  # HuggingFace Model Repo ID
DB_FAISS_PATH = "vectorstore/db_faiss"            # Vector database location
DATA_PATH = "data/"                               # PDF source folder
CHUNK_SIZE = 500                                  # Text chunk size
CHUNK_OVERLAP = 50                                # Text chunk overlap
```

---

## ⚠️ Disclaimer

> **Medical Disclaimer**: This application is built for informational and research purposes only. It is not intended to be a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of a qualified physician or healthcare provider with any health questions.
