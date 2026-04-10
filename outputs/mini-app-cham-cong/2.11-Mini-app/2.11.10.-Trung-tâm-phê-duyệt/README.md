# 2.11.10. Trung tâm phê duyệt

---

| Thông tin | Nội dung |
| --- | --- |
| Target release | Version 1.0 (Sprint 9) |
| Epic | STRATOS-ADMIN: Hệ thống Quản trị & Cấu hình tập trung |
| Document owner | BA Team |
| Stakeholder | Quản lý, HR Admin, Nhân viên |
| Status | Draft |
| Tham chiếu | EAMS v2.0 §7 (Quy trình phê duyệt) |

---

### **1. MỤC TIÊU**

- **Lý do tồn tại:** Tất cả đơn từ (nghỉ phép, OT, giải trình, đổi ca) cần quy trình phê duyệt đa cấp minh bạch và có thể truy vết.
- **Bài toán:** Cung cấp giao diện tập trung cho Manager/HR duyệt đơn nhanh, cấu hình chuỗi phê duyệt theo chi nhánh, và hỗ trợ duyệt hàng loạt.
- **Giá trị mang lại:** Giảm 60% thời gian phê duyệt; đảm bảo không bỏ sót đơn; lưu trữ lý do từ chối minh bạch.

---

### **2. MÔ TẢ QUY TRÌNH NGHIỆP VỤ**

```
NV gửi đơn → Hệ thống tạo Approval workflow
        ↓
Xác định chuỗi phê duyệt theo cấu hình site:
  Level 1: DIRECT_MANAGER
  Level 2: DEPT_HEAD (nếu > N ngày/giờ)
  Level 3: SITE_HR (nếu nhạy cảm)
        ↓
Đơn xuất hiện trong Inbox phê duyệt của approver
        ↓
Approver xem chi tiết → Duyệt / Từ chối (kèm lý do)
        ↓
  ├─ APPROVED → Chuyển level tiếp (nếu multi-level)
  │              hoặc Final APPROVED → Áp dụng
  ├─ REJECTED → Phản hồi lý do về NV
  └─ Fallback: Nếu approver không có quyền tại site
               → SITE_MANAGER → SITE_HR → GLOBAL_HR
```

---

### **3. NHU CẦU NGƯỜI DÙNG**

| Persona | Nhu cầu cụ thể | Tài liệu / Căn cứ |
| --- | --- | --- |
| Quản lý | Muốn duyệt đơn của team nhanh gọn trên mobile, không bỏ sót. | Inbox phê duyệt |
| HR Admin | Muốn cấu hình chuỗi phê duyệt khác nhau cho từng chi nhánh. | Approval Chain config |
| Nhân viên | Muốn biết lý do bị từ chối và ai đã duyệt/từ chối đơn. | Rejection feedback |

---

### **4. PHẠM VI CHỨC NĂNG**

| Mã | Chức năng | Mô tả chi tiết | User Story |
| --- | --- | --- | --- |
| F10.1 | Inbox phê duyệt | Danh sách đơn chờ duyệt, lọc theo loại (Leave/OT/Correction). Xem chi tiết đơn, file đính kèm. Nút Duyệt/Từ chối kèm lý do. Badge số đơn chưa duyệt. | [US-APPR-01](./US-APPR-01-Inbox-phê-duyệt.md) |
| F10.2 | Cấu hình chuỗi phê duyệt | Thiết lập approval chain theo loại đơn × site. Thêm/bớt level. Điều kiện kích hoạt level (> N ngày, > N giờ). Cấu hình fallback. | [US-APPR-02](./US-APPR-02-Cấu-hình-chuỗi-phê-duyệt.md) |
| F10.3 | Phê duyệt hàng loạt | Chọn nhiều đơn cùng loại → Duyệt/Từ chối batch. Hiển thị kết quả xử lý cho từng đơn. Hỗ trợ cấu hình ngày chốt công. | [US-APPR-03](./US-APPR-03-Phê-duyệt-hàng-loạt.md) |

---

### **5. CHUỖI PHÊ DUYỆT MẪU** *(Nguồn: EAMS v2.0 §7.2)*

| Loại đơn | Level 1 | Level 2 | Level 3 |
| --- | --- | --- | --- |
| Leave (≤ 3 ngày) | DIRECT_MANAGER | — | — |
| Leave (> 3 ngày) | DIRECT_MANAGER | DEPT_HEAD | — |
| Leave (> 5 ngày) | DIRECT_MANAGER | DEPT_HEAD | SITE_HR |
| OT Request | DIRECT_MANAGER | — | — |
| OT (> 8 giờ) | DIRECT_MANAGER | SITE_MANAGER | — |
| Correction | DIRECT_MANAGER | SITE_HR | — |
| Manual Entry | SITE_HR | — | — |

---

### **6. YÊU CẦU PHI CHỨC NĂNG**

- **Hiệu năng:** Tải inbox ≤ 1 giây; batch approve ≤ 3 giây cho 50 đơn.
- **Thông báo:** Push notification cho approver khi có đơn mới; cho NV khi đơn thay đổi trạng thái.
- **Audit trail:** Ghi vết toàn bộ: ai duyệt, thời điểm, lý do.
- **Ngày chốt công:** Sau ngày chốt, đơn tháng cũ không thể duyệt (ngoại trừ Exception Approval).

---

### **7. ĐIỀU KIỆN GIẢ ĐỊNH**

1. Cấu hình tổ chức đã được thiết lập (Manager → NV relationship).
2. Người dùng đã đăng nhập với role Manager, DEPT_HEAD, SITE_HR hoặc cao hơn.
3. Đơn từ đã được tạo qua Module 04 (Trung tâm đăng ký) hoặc Module 03 (Giải trình).
