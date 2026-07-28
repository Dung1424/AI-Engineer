import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


def main() -> None:
    data = pd.read_csv("data/reviews.csv")
    x_train, x_test, y_train, y_test = train_test_split(
        data["text"], data["label"], test_size=0.3, random_state=42, stratify=data["label"]
    )
    model = Pipeline([
        (
            "tfidf",
            TfidfVectorizer(
                analyzer="char_wb", ngram_range=(3, 5), min_df=1, sublinear_tf=True
            ),
        ),
        (
            "classifier",
            LogisticRegression(C=3.0, max_iter=1000, class_weight="balanced"),
        ),
    ])
    baseline = DummyClassifier(strategy="most_frequent").fit([[0]] * len(y_train), y_train)
    model.fit(x_train, y_train)
    prediction = model.predict(x_test)
    report = {
        "baseline_accuracy": float((baseline.predict([[0]] * len(y_test)) == y_test).mean()),
        "classification_report": classification_report(y_test, prediction, output_dict=True),
        "confusion_matrix_labels": ["negative", "positive"],
        "confusion_matrix": confusion_matrix(y_test, prediction, labels=["negative", "positive"]).tolist(),
    }
    Path("artifacts").mkdir(exist_ok=True)
    joblib.dump(model, "artifacts/model.joblib")
    Path("artifacts/metrics.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(classification_report(y_test, prediction))


if __name__ == "__main__":
    main()
