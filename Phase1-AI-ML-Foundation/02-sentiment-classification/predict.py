import argparse

import joblib


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("review")
    args = parser.parse_args()
    model = joblib.load("artifacts/model.joblib")
    probabilities = model.predict_proba([args.review])[0]
    print(dict(zip(model.classes_, probabilities.round(4))))
