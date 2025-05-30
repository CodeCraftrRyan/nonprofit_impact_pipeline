from extract import extract_data
from transform import clean_data

def save_data(df):
    df.to_csv("data/processed/cleaned_marketing_data.csv", index=False)
    print("✅ Cleaned data saved!")

if __name__ == "__main__":
    df = extract_data()
    df_clean = clean_data(df)
    save_data(df_clean)