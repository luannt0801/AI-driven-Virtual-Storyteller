# How to deploy an LLM model

## Mô hình LLM

Mô hình LLM dựa trên kiến trúc transformer (GPT, BERT, LLAMMA, ...) cấu hình các tham số đầu vào của model gọi là tolken tương đương với không gian
vector chứa số lượng dữ liệu (từ có nghĩa) tức số lượng tham số tối đa mà mô hình đó có. Ví dụ mô hình có 3B tham số có nghĩa các mạng của mô hình đó có 3 tỉ tham số tức là nó có khả năng học hiểu ngữ cảnh, nội dung liên kết giữa 3 tỉ từ trong tài liệu.


Mô hình càng có nhiều tham số tính toán thì càng có khả năng hiểu rõ ngữ cảnh, cấu trúc của tài liệu hơn.

Việc có nhiều tham số tính toán dẫn đến tài nguyên để huấn luyện mô hình là rất lớn. 

## Deploy model

Huấn luyện model với dữ liệu được chuẩn hóa tokenization từ các dạng (pdf, doc, ...) từ nhiều nguồn như internet, tài liệu nội bộ, ...

Nếu huấn luyện mô hình từ đầu, từ những tham số khởi tạo ngẫu nhiên và huấn luyện với dữ liệu để lấy ra được bộ tham số mô hình tốt thì sẽ rất tốn kém, cỡ google, openai, microsoft mới làm được.

Ta cần finetune các mô hình mã nguồn mở được trainning các bộ tham số khá tốt trước trên hugging face, ... như Llama, bert, falcom, gpt, ...

Sau đó huấn luyện mô hình lại với các dữ liệu local để mô hình hiểu rõ hơn các dữ liệu riêng biệt của mình.

## Optimize model

Quantization: nén mô hình (ví dụ FP16 → INT8) để chạy nhanh hơn.

LoRA / PEFT: fine-tune hiệu quả hơn với ít tài nguyên.

Distillation: rút gọn mô hình nhỏ hơn nhưng giữ chất lượng.

Triển khai trên nền tảng:

- On-premise: máy chủ nội bộ (đảm bảo bảo mật)

- Cloud: dùng dịch vụ từ AWS, GCP, Azure...