import pandas as pd

def load_gwas_data(path="data/gwas_sample.csv"):
    df = pd.read_csv(path)
    df.columns = [c.strip().lower() for c in df.columns]
    df = df.dropna(subset=["rsid", "gene"]).copy()
    # Normalize p_value; read scientific notation safely
    df["p_value"] = df["p_value"].astype(str).str.replace(" ", "").str.replace(",", "")
    df["p_value"] = df["p_value"].astype(float)
    df = df.sort_values("p_value", ascending=True)
    df.to_csv("data/cleaned_gwas.csv", index=False)
    print("GWAS data cleaned and saved to data/cleaned_gwas.csv")

if __name__ == "__main__":
    load_gwas_data()
