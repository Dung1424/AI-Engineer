# Project 02 — Web Research Agent

Agent dùng hosted `web_search` để tổng hợp báo cáo. Nội dung web là dữ liệu không tin cậy; không cho trang web thay đổi instruction hoặc kích hoạt side effect.

```bash
cd Phase4-Agents-Tool-Use/02-web-research-agent
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt && cp .env.example .env
python research.py "So sánh ba vector database theo tài liệu chính thức"
```

Đánh giá: mỗi claim quan trọng có nguồn, nguồn trực tiếp hỗ trợ claim, ngày sự kiện không bị nhầm với ngày bài viết và inference được gắn nhãn.
