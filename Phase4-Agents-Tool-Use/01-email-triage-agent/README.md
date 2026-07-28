# Project 01 — Email Triage Agent

Đọc email JSON, phân loại, ưu tiên và tạo **draft**. Project cố ý không kết nối Gmail/Outlook và không gửi email.

```bash
cd Phase4-Agents-Tool-Use/01-email-triage-agent
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt && cp .env.example .env
python triage.py sample-email.json
```

Tạo test set 30 email. Đo category accuracy, priority accuracy và tỷ lệ billing/urgent được gắn `needs_human_review=true`.
