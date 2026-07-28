# Giai đoạn 4 — Agents và Tool Use

| Project | Trọng tâm |
|---|---|
| [01 Email Triage Agent](./01-email-triage-agent/README.md) | Structured classification và draft, không tự gửi |
| [02 Web Research Agent](./02-web-research-agent/README.md) | Hosted web search và báo cáo có nguồn |
| [03 Business DB Agent](./03-business-database-agent/README.md) | Tool calling tới SQLite read-only |
| [04 Customer Support Workflow](./04-customer-support-workflow/README.md) | LangGraph state, routing và human escalation |

## Quy tắc an toàn chung

- Tool mặc định read-only; không gửi email hay cập nhật order thật.
- Validate arguments, allowlist tool, giới hạn vòng lặp và số dòng kết quả.
- Tool có side effect phải thêm bước human approval trước khi thực thi.
- Lưu trace đầu vào/tool/output đã che dữ liệu nhạy cảm khi tự mở rộng project.
