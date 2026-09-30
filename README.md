# rag-knowledge-assistant

A local question-answering assistant over scattered product documentation, using retrieval-augmented generation (RAG).

## Problem

In many companies, product and process knowledge is spread across PDFs, help pages and specifications — and often lives in the heads of a few people. Finding the right answer means knowing where to look. This project explores whether a small, locally hosted RAG system can answer plain-language questions from that documentation and point to its sources.

## Approach

1. Load documents (PDF first) and extract their text
2. Split the text into overlapping chunks
3. Embed the chunks with `nomic-embed-text` via Ollama
4. Store the vectors in ChromaDB
5. For a question, retrieve the most similar chunks and pass them to a local language model (Ollama) to generate an answer with source references

Everything runs locally — no documents leave the machine.

## Data Sources

Publicly available documents only: HR software product descriptions and SAP help pages on personnel administration. No internal or confidential company data is used.

## Status

- [x] Project structure
- [x] PDF loader (`src/loader.py`)
- [ ] Chunking
- [ ] Embeddings and vector store
- [ ] Retrieval and answer generation
- [ ] Evaluation

## Usage

```bash
conda create -n rag python=3.11
conda activate rag
pip install pypdf
# place PDF files in data/docs/
python src/loader.py
```

## Evaluation

Planned: a set of test questions with verified answers, to measure whether the retrieved chunks contain the answer and whether the generated answer is correct and grounded in its sources.

## Limitations

Outdated documents are a core problem for RAG: the model cannot tell whether a document is still valid and will answer confidently from obsolete content. Document selection and versioning matter as much as the model.
