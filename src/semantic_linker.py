import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np

try:
    import faiss
    _HAS_FAISS = True
except Exception:
    _HAS_FAISS = False

from sklearn.neighbors import NearestNeighbors

def create_embeddings(texts, model):
    emb = model.encode(texts, convert_to_numpy=True, show_progress_bar=False, normalize_embeddings=True)
    return emb

def _faiss_top1(query_emb: np.ndarray, base_emb: np.ndarray):
    dim = base_emb.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(base_emb.astype(np.float32))
    sims, idxs = index.search(query_emb.astype(np.float32), k=1)
    return sims, idxs

def _sklearn_top1(query_emb: np.ndarray, base_emb: np.ndarray):
    nn = NearestNeighbors(n_neighbors=1, metric='cosine')
    nn.fit(base_emb)
    distances, indices = nn.kneighbors(query_emb, n_neighbors=1)
    sims = 1.0 - distances
    return sims, indices

def build_semantic_links():
    df = pd.read_csv("data/harmonized_data.csv")
    variant_texts = df["description"].fillna("").astype(str).tolist()
    gene_texts = df["biological_process"].fillna("").astype(str).tolist()
    gene_names = df["gene"].fillna("").astype(str).tolist()

    model = SentenceTransformer("all-MiniLM-L6-v2")
    v_emb = create_embeddings(variant_texts, model)
    g_emb = create_embeddings(gene_texts, model)

    if _HAS_FAISS:
        sims, idxs = _faiss_top1(v_emb, g_emb)
    else:
        sims, idxs = _sklearn_top1(v_emb, g_emb)

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
