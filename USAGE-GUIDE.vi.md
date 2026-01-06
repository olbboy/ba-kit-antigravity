# 📘 Hướng Dẫn Sử Dụng BA-Kit (Antigravity Native)

**Chào mừng đến với "Bầy Đàn Nhận Thức" (Cognitive Swarm).**
Hướng dẫn này giải thích cách điều khiển 15 Agent của BA-Kit để đạt được kết quả "World Class".

---

## 🏗️ Kiến Trúc: Sự Khác Biệt Của "System 2"

Không giống như các workflow "Chat với AI" thông thường, các agent của BA-Kit hoạt động dựa trên một **Vòng Lặp Nhận Thức (Cognitive Loop)**:

1.  **Kích Thích (Stimulus)**: Input của người dùng.
2.  **Hệ Thống 1 (Nhanh)**: Agent phác thảo câu trả lời ngay lập tức dựa trên khớp mẫu (pattern matching).
3.  **Hệ Thống 2 (Chậm)**: Agent **Suy Ngẫm (Reflect)**.
    *   Nó tự phê bình bản nháp của mình ("Cái này có quá mơ hồ không?").
    *   Nó kiểm tra ảo giác ("Mình có bịa ra dependency này không nhỉ?").
    *   Nó xác minh sự thật ("Để mình grep lại codebase cho chắc").
4.  **Phản Hồi**: Kết quả đã được trau chuốt và xác minh.

**Lợi ích**: Bạn nhận được ít lỗi hơn, toán học chính xác, và trích dẫn thực tế.

---

## 🚦 15 Agent: Khi Nào Dùng Ai?

### 🔴 The Boss (Sếp)
*   **`@ba-master`**: Dùng khi bạn không biết phải dùng ai. "Tôi có vấn đề này, cứu với."

### 🔵 Giai Đoạn Sáng Tạo (Khởi Đầu Vòng Đời)
1.  **`@ba-identity`**: Bắt đầu tại đây. Xác định *Ai* là stakeholders? Ai là Nhà tài trợ?
2.  **`@ba-elicitation`**: Dùng để phỏng vấn người dùng. "Bạn cần gì?" (Funnel Questioning).
3.  **`@ba-writing`**: Dùng để soạn thảo Yêu cầu (User Stories / GHERKIN).

### 🟡 Giai Đoạn Kỹ Thuật (Giữa Vòng Đời)
4.  **`@ba-nfr`**: Định nghĩa *Ràng buộc*. "Nhanh thế nào? Bảo mật ra sao?" (ISO 25010).
5.  **`@ba-process`**: Vẽ luồng. "Trực quan hóa quy trình thanh toán." (BPMN).
6.  **`@ba-traceability`**: Map các liên kết. "Cái gì sẽ hỏng nếu tôi đổi X?" (Lý thuyết đồ thị).
7.  **`@ba-conflict`**: Giải quyết tranh cãi. "Sales muốn A, Dev muốn B." (Đàm phán Harvard).

### 🟣 Giai Đoạn Tối Ưu Hóa (Cuối Vòng Đời)
8.  **`@ba-validation`**: Kiểm tra chất lượng. "Tìm lỗi trong spec này." (Visual QA).
9.  **`@ba-prioritization`**: Quyết định thứ tự. "Xây cái gì trước?" (WSJF).
10. **`@ba-solution`**: Kiểm tra tiền bạc. "Cái này có lãi không?" (ROI/NPV).
11. **`@ba-export`**: Xuất bản. "Biến nó thành PDF." (Compliance).

### ⚫ Giai Đoạn "Level 5" (Tối Ưu Hóa Sâu)
12. **`@ba-metrics`**: Kiểm toán *Quy trình*. "Chúng ta đang nhanh hơn hay ẩu hơn?" (SPC).
13. **`@ba-root-cause`**: Sửa *Hệ thống*. "Tại sao chúng ta cứ gặp lỗi này mãi?" (5 Whys).
14. **`@ba-innovation`**: Thiết kế *Thử nghiệm*. "AI có giúp ích không?" (A/B Testing).

---

## 🛠️ Tool Mandates (Tại Sao Agent Chạy Lệnh?)

Bạn sẽ thấy các Agent chạy lệnh `run_command` hoặc `grep_search`. **Đừng ngăn cản họ.**

*   **Python**: Được dùng bởi `@ba-solution`, `@ba-innovation`, `@ba-metrics` để đảm bảo **Tính Toàn Vẹn Của Toán Học**. LLM không biết, Python biết.
*   **Grep**: Được dùng bởi `@ba-traceability` để đảm bảo **Tính Toàn Vẹn Của Liên Kết**. Agent phải "nhìn thấy" file thì mới link được.
*   **Web Search**: Được dùng bởi `@ba-nfr` để đảm bảo **Tính Toàn Vẹn Của Tiêu Chuẩn**. Nó kiểm tra web thực tế để cập nhật GDPR/ISO.

---

## 🎓 Mẹo Chuyên Gia (Pro-Tips)

### 1. "Bàn Giao Persona" (The Persona Handover)
Bạn có thể chuỗi các agent thủ công để tạo workflow mạnh mẽ:
> *User*: `@ba-elicitation Phỏng vấn tôi về tính năng Đăng nhập.`
> *(Hội thoại diễn ra...)*
> *User*: `Tuyệt. Giờ thì @ba-writing hãy biến cuộc phỏng vấn đó thành Gherkin scenarios.`

### 2. "Kiểm Tra Thiên Kiến" (The Bias Check)
Nếu thấy Agent quá hiền, hãy yêu cầu nó dùng Chế độ Phê bình (Critic Mode):
> *User*: `@ba-validation Roast (chửi) yêu cầu này đi. Hãy cực kỳ khắc nghiệt.`

### 3. "Quét Hình Ảnh" (The Visual Scan)
Bạn có thể đưa ảnh cho Agent (Drag & Drop):
> *User*: `@[image.png] @ba-writing Viết yêu cầu UI dựa trên mockup này.`

---

**Kết Thúc Hướng Dẫn**
*Đi và Kiến tạo đi.*
