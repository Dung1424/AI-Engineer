from pathlib import Path
import pandas as pd

STAGE = Path(__file__).resolve().parents[1]


def main():
    df = pd.read_csv(STAGE / "data" / "scores_raw.csv", dtype=str,
                     keep_default_na=False)
    df["score"] = pd.to_numeric(df["score"], errors="coerce")
    print("Số dòng đầu vào:", len(df))
    print("Điểm thiếu hoặc không chuyển được:", int(df["score"].isna().sum()))
    clean = df.loc[df["score"].between(0, 10)].copy()
    clean = clean.drop_duplicates(subset="id", keep="first")
    print("Số dòng sạch:", len(clean))
    print("Trung bình:", float(clean["score"].mean()))
    print("Trung bình theo nhóm:", clean.groupby("group")["score"].mean().to_dict())


if __name__ == "__main__":
    main()
