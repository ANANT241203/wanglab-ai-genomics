# AI-Driven Genomic Data Curation for Alzheimer's Research
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green.svg)](https://fastapi.tiangolo.com/)
[![FAISS](https://img.shields.io/badge/FAISS-Semantic_Search-orange.svg)](https://github.com/facebookresearch/faiss)
[![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)](LICENSE)

This repository is a working prototype of an intelligent system for automated extraction, harmonization, and semantic linking of genetic association findings. It mirrors the goals described by the Wang Lab: connecting association signals with functional genomics knowledge to enable data-driven hypothesis generation in neurodegenerative disease genetics.

## Overview
- Build a machine-readable knowledge base that integrates GWAS-like association records with gene-level functional annotations.
- Core capabilities:
  1. Ingest and preprocess genetic association data
  2. Harmonize variant identifiers and gene annotations
  3. Embed textual descriptions and perform semantic similarity search to connect variants with relevant gene functions
  4. Expose a lightweight API for interactive querying

## Stack
Python 3.10+, pandas, numpy, sentence-transformers, faiss-cpu, FastAPI, uvicorn

## Quickstart
```bash
pip install -r requirements.txt
python src/ingest_gwas.py
python src/harmonize_data.py
python src/semantic_linker.py
uvicorn src.api_server:app --reload
```

Open:
- Variant lookup: http://127.0.0.1:8000/variant/rs429358
- Gene search: http://127.0.0.1:8000/search_gene/APOE

## Data
The repository ships with a small, illustrative dataset in `data/`:
- `gwas_sample.csv`: rsID-level associations for Alzheimer's disease
- `gene_annotations.csv`: coarse functional process annotations

Replace these files with larger public resources, for example the GWAS Catalog summary stats and gene process annotations from public ontologies, to scale the pipeline.

## Notes
- `semantic_linker.py` uses `sentence-transformers` to create embeddings and FAISS for nearest neighbor search.
- This prototype is intentionally concise and ready to extend with additional modalities such as eQTLs, epigenomic marks, and regulatory annotations.
