# Project 02 — Sentiment Classification

## Mục tiêu

Biểu diễn văn bản bằng TF-IDF, phân loại bằng Logistic Regression và đọc precision/recall/F1/confusion matrix.

## Chạy

```bash
cd Phase1-AI-ML-Foundation/02-sentiment-classification
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python train.py
python predict.py "Dùng ổn nhưng pin hơi yếu"
```

Dataset nhỏ chỉ để học pipeline, không đại diện ngôn ngữ thật. Hãy mở rộng tối thiểu 500 review, giữ một test set không chỉnh sửa và phân tích câu mỉa mai/câu có cả khen lẫn chê.

Tham khảo [scikit-learn text feature extraction](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction).
