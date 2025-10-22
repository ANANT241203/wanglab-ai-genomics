# AI-Driven Genomic Data Curation for Alzheimer’s Research

[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)](LICENSE)

This repository implements a working prototype of an intelligent system for automated extraction, harmonization, and semantic linking of genetic association findings. It mirrors the goals described by the Wang Lab: connecting genetic association signals with functional genomics knowledge to enable data-driven hypothesis generation in neurodegenerative disease research.

## Overview

* Construct a machine-readable knowledge base integrating GWAS-like association data with gene-level functional annotations.
* Core capabilities:

  1. Ingest and preprocess genetic association data.
  2. Harmonize variant identifiers and gene annotations.
  3. Embed textual descriptions and perform semantic similarity linking between variants and biological processes.
  4. Serve a lightweight REST API for programmatic access and exploration.

## Stack

Python 3.10+, pandas, numpy (<2), sentence-transformers, scikit-learn, FastAPI, uvicorn

FAISS can optionally accelerate similarity search when compatible, but the default backend uses scikit-learn’s cosine similarity for cross-platform reliability.

## Quickstart

```bash
pip install -r requirements.txt
python src/ingest_gwas.py
python src/harmonize_data.py
python src/semantic_linker.py
python -m uvicorn src.api_server:app --reload
```

Open in browser:

* Variant lookup: [http://127.0.0.1:8000/variant/rs429358](http://127.0.0.1:8000/variant/rs429358)
* Gene search: [http://127.0.0.1:8000/search_gene/APOE](http://127.0.0.1:8000/search_gene/APOE)

**Windows note:** If FAISS fails due to NumPy versioning, the pipeline automatically falls back to scikit-learn cosine similarity. Requirements pin `numpy<2` for compatibility.

## Data

The repository includes a small demonstration dataset in `data/`:

* `gwas_sample.csv`: rsID-level associations for Alzheimer’s disease
* `gene_annotations.csv`: biological process annotations for key genes

These can be replaced with larger public resources (e.g., the GWAS Catalog and GO annotations) to scale the analysis.

## Notes

* `semantic_linker.py` generates text embeddings and performs semantic matching between variants and gene functions.
* The framework is designed for easy extension to include eQTLs, epigenomic features, and regulatory network data.
