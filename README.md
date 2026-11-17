# DocMind

Chat with your documents. Upload PDFs, ask questions in plain English, and get answers **with citations** (file name + page number) so every claim can be verified.

> Status: 🚧 In development. Built step by step as a learning and portfolio project.

## Why this exists

LLMs don't know your private documents, and pasting whole PDFs into a prompt doesn't scale (context limits, cost, and worse accuracy). DocMind uses **Retrieval-Augmented Generation (RAG)** to find only the relevant passages and answer strictly from them.

## How it works

**Indexing (once per document)**

```
PDF → extract text per page → split into chunks → embed each chunk → store in vector DB
```

**Querying (every question)**

```
Question → embed → retrieve top-k similar chunks → build prompt → LLM answers using only those chunks → answer + citations
```

## Tech stack

| Component | Tool |
|---|---|
| Language | Python 3.10+ |
| PDF parsing | pypdf |
| Embeddings | sentence-transformers (`all-MiniLM-L6-v2`), runs locally |
| Vector store | ChromaDB |
| LLM | Claude API (swappable) |
| Backend | FastAPI |
| UI | Streamlit |

## Project structure

```
docmind/
├── data/            # your PDFs (git-ignored)
├── src/
│   └── loader.py    # PDF loading with page-level metadata
├── .env             # API keys (git-ignored)
├── requirements.txt
└── README.md
```

## Getting started

```powershell
git clone https://github.com/YOUR_USERNAME/docmind.git
cd docmind
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Put your PDFs in `data/`, then:

```powershell
python src/loader.py
```

Create a `.env` file for the LLM step (later phase):

```
ANTHROPIC_API_KEY=your_key_here
```

## Roadmap

- [x] Project setup and PDF loader
- [ ] Chunking with overlap
- [ ] Embeddings and vector store
- [ ] Retrieval
- [ ] Answer generation with citations
- [ ] FastAPI backend and Streamlit UI
- [ ] Evaluation (retrieval hit-rate, answer faithfulness)
- [ ] Hybrid search (BM25 + vectors) and reranking
- [ ] **OCR support for scanned PDFs**

## Known limitations

- Scanned or image-only PDFs are skipped for now (no text layer). OCR is planned.
- Tables and multi-column layouts may extract imperfectly.

## Design decisions

- **No LangChain at first.** Each stage is written by hand to keep the pipeline transparent and debuggable.
- **Page-level metadata** is stored with every chunk so answers can cite source and page.
- **Local embeddings** keep indexing free and documents private.

## License

MIT