# Project 01 — Intent Fine-tuning

Fine-tune model multilingual nhỏ cho bốn intent bằng Hugging Face Trainer.

```bash
cd Phase6-Open-Source-Fine-Tuning/01-intent-finetuning
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python train.py --epochs 3
```

Dataset đi kèm quá nhỏ để kết luận chất lượng. Trước khi dùng thật: tối thiểu hàng trăm mẫu/intent, deduplicate, giữ test set riêng, thêm baseline TF-IDF, confusion matrix và error analysis. Sau khi hiểu full-head fine-tuning, bài tập tiếp theo là áp dụng PEFT/LoRA cho model phù hợp.
