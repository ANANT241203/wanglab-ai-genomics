import pandas as pd

def harmonize_data(gwas_path="data/cleaned_gwas.csv", gene_path="data/gene_annotations.csv"):
    gwas = pd.read_csv(gwas_path)
    gene_annot = pd.read_csv(gene_path)
    # Basic left join to attach process text where available
    merged = gwas.merge(gene_annot, on="gene", how="left")
    merged.to_csv("data/harmonized_data.csv", index=False)
    print("Harmonized data saved to data/harmonized_data.csv")

if __name__ == "__main__":
    harmonize_data()
