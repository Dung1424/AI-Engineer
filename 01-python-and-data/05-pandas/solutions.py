import pandas as pd


def clean_data(df):
    clean = df.copy()
    clean["score"] = pd.to_numeric(clean["score"], errors="coerce")
    clean = clean.loc[clean["score"].between(0, 10)].copy()
    return clean.drop_duplicates(subset="id", keep="first").reset_index(drop=True)


def mean_by_group(clean_df):
    return clean_df.groupby("group")["score"].mean().to_dict()
