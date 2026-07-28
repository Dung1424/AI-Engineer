# Giai đoạn 1 — Nền tảng AI/ML

| Project | Bài toán | Metric chính |
|---|---|---|
| [01 House Price Regression](./01-house-price-regression/README.md) | Regression, preprocessing, feature engineering | MAE, RMSE, R² |
| [02 Sentiment Classification](./02-sentiment-classification/README.md) | TF-IDF + Logistic Regression | Precision, Recall, F1 |
| [03 Embedding Search](./03-embedding-semantic-search/README.md) | Embedding + cosine similarity | Recall@k thủ công |

## Lý thuyết phải hiểu

- Vector, matrix, dot product và cosine similarity.
- Mean, variance, correlation, sampling và xác suất có điều kiện.
- Gradient ở mức “hướng thay đổi làm loss tăng/giảm”.
- Supervised/unsupervised, train/validation/test và data leakage.
- Overfitting/underfitting, feature engineering và baseline.
- Neural network, embedding, attention và Transformer ở mức khái niệm.

## Cổng hoàn thành

Không chỉ chạy code: phải giải thích vì sao chọn metric, so với baseline, phân tích ít nhất năm lỗi và chỉ ra feature có nguy cơ leakage.

Tham khảo [scikit-learn Pipeline](https://scikit-learn.org/stable/modules/compose.html), giúp gom preprocessing và model vào cùng quy trình để giảm nguy cơ leakage.
