# Kế hoạch triển khai đã chốt

## Phạm vi

- Giai đoạn 0: bỏ qua, giữ nguyên mã nguồn hiện có.
- Giai đoạn 1: triển khai 3 project AI/ML.
- Giai đoạn 2: triển khai 4 project LLM.
- Giai đoạn 3: triển khai 3 project RAG.
- Giai đoạn 4: triển khai 4 project Agents/Tool Use.
- Giai đoạn 5: bỏ qua toàn bộ LLMOps, cloud deployment và production hardening.
- Giai đoạn 6: triển khai 3 project open-source/fine-tuning chạy local.

Danh sách chi tiết nằm tại [PROJECTS.md](./PROJECTS.md).

## Thứ tự thực hiện

1. Giai đoạn 1: train/evaluate ba project, viết error analysis.
2. Giai đoạn 2: cấu hình API key, chạy structured output, streaming và tool calling.
3. Giai đoạn 3: tạo bộ tài liệu và tối thiểu 30 câu hỏi retrieval evaluation.
4. Giai đoạn 4: tạo test set cho routing/tool accuracy và adversarial inputs.
5. Giai đoạn 6: benchmark baseline, fine-tune, local serving rồi so sánh API/local.

## Definition of Done chung

- Mỗi project dùng virtual environment và dependency riêng.
- README chạy được theo thứ tự từ môi trường sạch.
- API key chỉ nằm trong `.env` đã bị Git ignore.
- Có input mẫu, metric hoặc tiêu chí đánh giá và phần giới hạn.
- Không kết nối dữ liệu/tài khoản thật trong agent project.
- Không triển khai Docker/cloud/CI/CD/monitoring production theo yêu cầu.
