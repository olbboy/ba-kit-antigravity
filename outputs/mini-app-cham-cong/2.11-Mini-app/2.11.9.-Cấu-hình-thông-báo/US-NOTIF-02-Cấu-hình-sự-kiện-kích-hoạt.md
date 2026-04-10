# US-NOTIF-02: Cấu hình sự kiện kích hoạt

---

**AS A** HR Admin,  
**I WANT TO** cấu hình danh sách sự kiện kích hoạt thông báo và tùy chỉnh nội dung template cho từng event,  
**SO THAT** hệ thống gửi đúng thông báo, đúng nội dung cho đúng đối tượng khi có sự kiện xảy ra.

---

### **1. BUSINESS FLOW**

1. **Xem danh sách event:** Admin thấy danh sách 36 loại sự kiện, phân theo nhóm.
2. **Bật/tắt trigger:** Toggle cho từng event — tắt nghĩa là không gửi thông báo khi event xảy ra.
3. **Cấu hình template:** Chỉnh sửa tiêu đề và nội dung thông báo cho từng event. Hỗ trợ biến động (VD: `{{employee_name}}`, `{{date}}`).
4. **Preview:** Xem trước thông báo mẫu trước khi lưu.

---

### **2. ACCESS CONTROL (RBAC/ABAC)**

| Thông tin (Data Field) | Role (Access Right) | Ghi chú |
| --- | --- | --- |
| Bật/tắt trigger | HR Admin, SYS_ADMIN | Chỉ Admin cấu hình. |
| Chỉnh sửa template | HR Admin | Tùy chỉnh nội dung thông báo. |
| Xem cấu hình | HR, IT Admin | Read-only. |

---

### **3. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA)**

#### **AC1. Danh sách sự kiện theo nhóm**

| Nhóm | Sự kiện mẫu | Mặc định |
| --- | --- | --- |
| Chấm công | Check-in thành công, Check-out thành công, Nhận diện thất bại | Bật |
| Đơn từ | Đơn mới cần duyệt, Đơn được duyệt, Đơn bị từ chối | Bật |
| Cảnh báo | Đi muộn, Về sớm, Vắng mặt, Thiếu mốc quẹt, Gần hạn chốt công | Bật |
| Nhắc nhở | Nhắc chấm công đầu ca, Nhắc chấm công cuối ca, Lịch nghỉ lễ | Bật |
| Hệ thống | Camera offline, Batch job lỗi, OT vượt ngưỡng | Bật |

- Mỗi event có: Tên, Mô tả, Toggle Bật/Tắt, Kênh gửi, Template.
- Event bắt buộc (kết quả phê duyệt, kỷ luật): Không cho phép tắt → Toggle disabled.

#### **AC2. Template thông báo**

- Mỗi event có template mặc định (tiếng Việt).
- Biến động hỗ trợ: `{{employee_name}}`, `{{date}}`, `{{time}}`, `{{shift_name}}`, `{{request_type}}`, `{{approver_name}}`, `{{reason}}`.
- Giới hạn: Tiêu đề ≤ 100 ký tự; Nội dung ≤ 500 ký tự.

#### **AC3. Preview**

- Nút "Xem trước" hiển thị thông báo mẫu với dữ liệu giả.
- Hiển thị cả Push notification view và Email view.

---

### **4. DEFINITION OF DONE (DOD)**

1. **36 events:** Tất cả event được seed mặc định khi khởi tạo tenant.
2. **Bắt buộc:** Event bắt buộc không thể tắt (UI disabled + backend reject).
3. **Template:** Biến động được thay thế đúng khi gửi thông báo thực.
4. **QA:** Kiểm thử bật/tắt event → Trigger xảy ra → Thông báo gửi/không gửi đúng.
