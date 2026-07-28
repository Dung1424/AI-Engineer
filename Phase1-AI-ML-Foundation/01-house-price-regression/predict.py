import argparse
import json

import joblib
import pandas as pd


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("features", help='JSON, ví dụ {"area_m2":80,...}')
    args = parser.parse_args()
    features = json.loads(args.features)
    model = joblib.load("artifacts/model.joblib")
    value = model.predict(pd.DataFrame([features]))[0]
    print(f"Giá dự đoán: {value:.2f} nghìn đơn vị")


if __name__ == "__main__":
    main()
