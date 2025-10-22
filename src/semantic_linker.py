import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

def create_embeddings(texts, model):
    emb = model.encode(texts, convert_to_numpy=True, show_progress_bar=False, normalize_embeddings=True)
    return emb

def build_semantic_links():
    df = pd.read_csv("data/harmonized_data.csv")
    # Fallback texts when annotations are missing
    variant_texts = df["description"].fillna("").astype(str).tolist()
    gene_texts = df["biological_process"].fillna("").astype(str).tolist()
    gene_names = df["gene"].fillna("").astype(str).tolist()

    model = SentenceTransformer("all-MiniLM-L6-v2")
    v_emb = create_embeddings(variant_texts, model)
    g_emb = create_embeddings(gene_texts, model)

    dim = g_emb.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(g_emb)
    sims, idxs = index.search(v_emb, k=1)

    matched_genes = []
    sim_scores = []
    for i in range(len(df)):
        j = int(idxs[i][0])
        matched_genes.append(gene_names[j] if j < len(gene_names) else None)
        sim_scores.append(float(sims[i][0]))

    out = df.copy()
    out["semantic_match_gene"] = matched_genes
    out["similarity_score"] = sim_scores

    out.to_csv("data/semantic_links.csv", index=False)
    print("Semantic linking complete. Saved to data/semantic_links.csv")

if __name__ == "__main__":
    build_semantic_links()
