import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

TARGET = "price_thousand"
NUMERIC = ["area_m2", "bedrooms", "age_years", "distance_km"]
CATEGORICAL = ["district"]


def metrics(y_true, prediction) -> dict[str, float]:
    return {
        "mae": float(mean_absolute_error(y_true, prediction)),
        "rmse": float(mean_squared_error(y_true, prediction) ** 0.5),
        "r2": float(r2_score(y_true, prediction)),
    }


def main() -> None:
    data = pd.read_csv("data/houses.csv")
    train, test = train_test_split(data, test_size=0.2, random_state=42)
    preprocessor = ColumnTransformer([
        ("numeric", StandardScaler(), NUMERIC),
        ("category", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL),
    ])
    model = Pipeline([
        ("preprocess", preprocessor),
        ("model", RandomForestRegressor(n_estimators=250, min_samples_leaf=2, random_state=42, n_jobs=-1)),
    ])
    baseline = DummyRegressor(strategy="median").fit(train[NUMERIC + CATEGORICAL], train[TARGET])
    model.fit(train[NUMERIC + CATEGORICAL], train[TARGET])
    result = {
        "baseline": metrics(test[TARGET], baseline.predict(test[NUMERIC + CATEGORICAL])),
        "model": metrics(test[TARGET], model.predict(test[NUMERIC + CATEGORICAL])),
        "train_rows": len(train),
        "test_rows": len(test),
    }
    Path("artifacts").mkdir(exist_ok=True)
    joblib.dump(model, "artifacts/model.joblib")
    Path("artifacts/metrics.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
