from fastapi import FastAPI
import pandas as pd

app = FastAPI(title="Genomic Curation API", version="0.1.0")

def _load():
    return pd.read_csv("data/semantic_links.csv") if (True) else None

@app.get("/variant/{rsid}")
def get_variant(rsid: str):
    data = _load()
    record = data[data["rsid"].astype(str).str.lower() == rsid.lower()]
    if record.empty:
        return {"error": "Variant not found"}
    return record.to_dict(orient="records")[0]

@app.get("/search_gene/{gene}")
def search_gene(gene: str):
    data = _load()
    subset = data[data["gene"].astype(str).str.contains(gene, case=False, na=False)]
    return subset.to_dict(orient="records")
