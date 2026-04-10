# 2.11.2. Cấu hình ca làm việc

---

| Thông tin | Nội dung |
| --- | --- |
| Target release | Version 1.0 (Sprint 8) |
| Epic | STRATOS-ADMIN: Hệ thống Quản trị & Cấu hình tập trung |
| Document owner | BA Team |
| Stakeholder | HR Admin, Quản lý |
| Status | Open |
| Tham chiếu | EAMS v2.0 §4 (Quản lý ca làm việc) |

---

### **1. MỤC TIÊU**

- **Lý do tồn tại:** Doanh nghiệp có nhiều loại ca làm việc phức tạp (ca hành chính, ca đêm, ca xoay) cần được cấu hình linh hoạt và chính xác để hệ thống tự động tính công.
- **Bài toán:** Cung cấp công cụ cho HR thiết lập khung giờ In/Out, giờ nghỉ, giới hạn chấm công (Punch Limit) và gán nhân viên vào ca hàng loạt.
- **Giá trị mang lại:** Giảm 90% thời gian phân ca thủ công; đảm bảo tính chính xác khi tính giờ công, OT và trạng thái chuyên cần.

---

### **2. MÔ TẢ QUY TRÌNH NGHIỆP VỤ**

```
HR truy cập "Cấu hình ca làm việc"
        ↓
Xem danh sách ca hiện có (Thẻ ca bên trái)
        ↓
  ├─ Tạo ca mới: Nhập tên, chọn ngày, giờ In/Out, Break, Punch Limit
  ├─ Chỉnh sửa ca: Chọn thẻ ca → Cập nhật thông số
  └─ Import NV: Tải file Excel mẫu → Điền mã NV → Upload → Validate → Gán ca
        ↓
Hệ thống áp dụng cấu hình mới cho chấm công
```

---

### **3. NHU CẦU NGƯỜI DÙNG**

| Persona | Nhu cầu cụ thể | Tài liệu / Căn cứ |
| --- | --- | --- |
| HR Admin | Muốn tạo ca đêm xuyên ngày (20h-06h) mà hệ thống vẫn gán công đúng vào Ngày T. | Cấu hình giờ & ngày |
| HR Admin | Muốn giới hạn khung giờ check-in/out để loại bỏ dữ liệu quẹt thẻ "rác". | Punch Limit |
| HR Admin | Muốn gán ca cho 500+ nhân viên cùng lúc thay vì nhập từng người. | Import NV vào ca |

---

### **4. PHẠM VI CHỨC NĂNG**

| Mã | Chức năng | Mô tả chi tiết | User Story |
| --- | --- | --- | --- |
| F02.1 | Danh sách ca làm việc | Hiển thị các Thẻ ca kèm tên, giờ, số NV. Phân loại Active/Inactive. Sắp xếp theo giờ bắt đầu. | [US-SHIFT-01](./US-SHIFT-01-Danh-sách-ca-làm-việc.md) |
| F02.2 | Cấu hình giờ và ngày làm việc | Thiết lập tên ca, chọn ngày T2-CN, mốc giờ In/Out, ngày hiệu lực. Xử lý ca đêm tự động. | [US-SHIFT-02](./US-SHIFT-02-Cấu-hình-giờ-và-ngày-làm-việc.md) |
| F02.3 | Giới hạn thời gian chấm công | Thiết lập Punch Limit: số giờ check-in sớm / check-out muộn tối đa. Mốc quẹt ngoài khung bị bỏ qua. | [US-SHIFT-03](./US-SHIFT-03-Giới-hạn-thời-gian-chấm-công-(punch-limit).md) |
| F02.4 | Cấu hình giờ nghỉ | Thiết lập khung giờ nghỉ (Break) cho ca. Hệ thống tự trừ khi tính giờ làm thực tế. | [US-SHIFT-04](./US-SHIFT-04-Cấu-hình-giờ-nghỉ.md) |
| F02.5 | Import nhân viên vào ca | Tải file mẫu Excel, nhập Mã NV, upload và validate hàng loạt. Trả kết quả thành công/thất bại. | [US-SHIFT-05](./US-SHIFT-05-Import-nhân-viên-vào-ca.md) |

---

### **5. LOẠI CA HỖ TRỢ** *(Nguồn: EAMS v2.0 §4.1)*

| Loại ca | Mô tả | Ví dụ |
| --- | --- | --- |
| FIXED | Ca cố định | 08:00 - 17:00 |
| FLEXIBLE | Ca linh hoạt (core hours) | 10:00-15:00 core, ±2h |
| ROTATING | Ca xoay | Sáng/Chiều/Đêm luân phiên |
| SPLIT | Ca chia (2 buổi) | 08:00-12:00, 14:00-18:00 |
| FREE | Tự do | Chỉ cần đủ giờ/ngày |

---

### **6. YÊU CẦU PHI CHỨC NĂNG**

- **Hiệu năng:** Tải danh sách ca ≤ 1.5 giây; Import ≤ 5,000 NV/lần trong ≤ 30 giây.
- **Tính nhất quán:** Thay đổi cấu hình ca phải đồng bộ ngay xuống Dashboard NV.
- **Bảo mật:** Chỉ HR Admin mới có quyền CRUD ca và import nhân viên.

---

### **7. ĐIỀU KIỆN GIẢ ĐỊNH**

1. Người dùng đã đăng nhập với role HR Admin hoặc cao hơn.
2. Hệ thống đã khởi tạo tenant, site và danh sách nhân sự (Module 05).
3. Danh mục ngày nghỉ đã được cấu hình (Module 07) để xử lý ca đúng ngày lễ.
