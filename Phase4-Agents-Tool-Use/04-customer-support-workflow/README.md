# Project 04 — Customer Support Workflow

LangGraph quản lý state và nhánh rõ ràng: classify → escalate hoặc lookup → draft. Refund/risk cao luôn dừng ở human escalation.

```bash
cd Phase4-Agents-Tool-Use/04-customer-support-workflow
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt && cp .env.example .env
python workflow.py "Đơn A102 ở đâu?"
python workflow.py "Hoàn tiền ngay cho đơn B205"
```

Vẽ graph, tạo 30 ticket test và đo routing accuracy. Bài tập: thêm checkpoint SQLite, retry có giới hạn và node knowledge search.
