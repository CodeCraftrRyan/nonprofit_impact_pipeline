import pandas as pd
def clean_data(df):
    # Standardize column names
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    # Drop duplicates and nulls
    df = df.drop_duplicates()
    df = df.dropna()

    # Create age
    df["age"] = 2025 - df["year_birth"]

    # Segment income into 4 bins
    df["income_segment"] = pd.qcut(df["income"], 4, labels=["Low", "Mid-Low", "Mid-High", "High"])

    # Total spending
    spend_cols = [
        "mntwines", "mntfruits", "mntmeatproducts",
        "mntfishproducts", "mntsweetproducts", "mntgoldprods"
    ]
    df["total_spent"] = df[spend_cols].sum(axis=1)

    return df