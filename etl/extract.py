import pandas as pd

def extract_data():
    # The original file from Kaggle uses semicolons
    df = pd.read_csv("data/raw/marketing_campaign.csv", sep="\t")
    print(f"✅ Loaded {df.shape[0]} rows and {df.shape[1]} columns.")
    return df

if __name__ == "__main__":
    df = extract_data()
    print(df.head())