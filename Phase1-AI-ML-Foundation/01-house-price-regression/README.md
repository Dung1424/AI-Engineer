# Project 01 — House Price Regression

## Mục tiêu

Học một ML workflow tái lập được: tạo dữ liệu, split trước preprocessing, dùng `ColumnTransformer` + `Pipeline`, so với baseline và lưu metric/model.

## Chạy

```bash
cd Phase1-AI-ML-Foundation/01-house-price-regression
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python generate_data.py
python train.py
python predict.py '{"area_m2":90,"bedrooms":3,"age_years":5,"distance_km":4.2,"district":"east"}'
```

## Đọc kết quả

- MAE: sai lệch tuyệt đối trung bình, cùng đơn vị với giá.
- RMSE: phạt lỗi lớn mạnh hơn MAE.
- R²: mức biến thiên target được model giải thích; không dùng một mình.

## Bài tập

Thêm missing values, thử Linear Regression/Gradient Boosting, cross-validation và phân tích residual. Không được dùng `price_thousand` hoặc feature phát sinh sau giao dịch làm input.
