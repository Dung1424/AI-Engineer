# Project 03 — Business Database Agent

Agent chuyển câu hỏi kinh doanh thành SQL, nhưng tool chỉ mở SQLite ở chế độ read-only, chặn statement nguy hiểm và giới hạn 100 dòng.

```bash
cd Phase4-Agents-Tool-Use/03-business-database-agent
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt && cp .env.example .env
python agent.py "Doanh thu theo region trong tháng 7 là bao nhiêu?"
```

Regex không phải SQL sandbox hoàn chỉnh. Project học tập chỉ dùng database giả; không nối production DB. Bài tập: thay raw SQL bằng metric/dimension tool có allowlist chặt hơn.
