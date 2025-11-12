```markdown
# rag_app_with_ingest

A Retrieval Augmented Generation (RAG) app for ingesting PDF documents, embedding them using local LLMs, and enabling fast semantic search and question-answering on your private document corpus.

## 🚀 What is this project about?

This project builds an end-to-end RAG pipeline using:
- **FastAPI** for serving the API
- **Ollama** (embeddinggemma) for local text embeddings
- **Qdrant** as the vector database
- **LlamaIndex** to convert text into chunks
- **ollama** (gemma3:1b)
It lets users upload PDFs, chunk and embed their content, store embeddings, and run queries with source-accurate semantic results.

## 🛠️ Problems Solved

- **Easy document ingestion and chunking** (PDF, etc.)
- **Local embeddings for privacy and speed**
- **Efficient semantic search with Qdrant**
- **Retrieval-based answers with references**

Most RAG solutions are cloud-dependent or paid; this is free, fast, private, and open-source.

## 🗂️ Project Structure

- `main.py` — FastAPI API server
- `data_loader.py` — Document loader & chunking logic
- `vector_db.py` — Qdrant vector DB handler
- `custom_types.py` — Pydantic model definitions
- `pyproject.toml` — Dependency management
- `README.md` — Project documentation

## 🔧 How To Clone and Run

### 1. Clone the repository
```
git clone https://github.com/sorabhlahoti/rag_app_with_ingest.git
cd rag_app_with_ingest
```

### 2. Install dependencies (Python ≥3.13, Ollama installed)
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Or using [uv](https://github.com/astral-sh/uv):
```
uv pip install -r requirements.txt
```

### 3. Start Qdrant vector DB locally
```
docker run -p 6333:6333 qdrant/qdrant
```

### 4. Launch FastAPI server
```
uv run --env-file .env -- uvicorn main:app --reload
```

### 5. Run Ingest Dev Server Locally!
uv run --env-file .env -- uvicorn main:app --reload

### 6. Invoke the function from ingest:


to invoke rag_ingest_pdf:
{
  data:{
    "pdf_path":".......",
    "source_id":"sdfsdfsd"
  }
}

to invoke rag_query_pdf_ai:
{
  data:{
    "question":"xyz......"
  }
}


## ⚙️ Setup & Requirements

- Python ≥3.13
- Ollama (see [Ollama docs](https://ollama.com/))
- Qdrant (see [Qdrant docs](https://qdrant.tech/))
- See `pyproject.toml` for all dependencies

## 💡 Example Workflow

1. Invoke function by giving pdf path 
2. App splits and embeds content using embeddinggemma
3. Stores content in Qdrant DB
4. Search and query with natural language to retrieve semantically matching responses

## 🤝 Contributing

Open for PRs, issues, and feature suggestions! Fork and improve freely.

## ✨ License

MIT

---

**Build your own private document search, semantic retrieval, and RAG-powered Q&A using only open-source, locally running tools.**

```
