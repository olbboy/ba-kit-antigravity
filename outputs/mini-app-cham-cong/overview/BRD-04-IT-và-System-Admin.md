# BRD IT Admin & System Admin

---

| Thông tin | Nội dung |
| --- | --- |
| Target release | Version 1.0 |
| Epic | STRATOS-SYS: Hạ tầng kỹ thuật & Quản trị hệ thống |
| Document owner | BA Team |
| Stakeholder | IT Admin, System Admin, Super Admin |
| Status | Open |

---

### **1. MỤC TIÊU**

- **Lý do tồn tại:** Hệ thống EAMS cần vai trò kỹ thuật quản lý camera AI, cấu hình thông báo, quản trị chi nhánh và giám sát hoạt động hệ thống.
- **Bài toán:** Cung cấp công cụ cho IT quản lý thiết bị, cho System Admin quản trị site/audit, và quy trình offboarding tự động khi NV nghỉ việc.
- **Giá trị mang lại:** Giảm 90% lỗi chấm công do camera; truy vết 100% thay đổi hệ thống; xử lý nghỉ việc trong 5 phút thay vì 2 ngày.

---

### **2. PHẠM VI VAI TRÒ**

| Vai trò | Scope | Trách nhiệm chính |
| --- | --- | --- |
| IT_ADMIN | Camera + Thông báo tại site | Quản lý thiết bị camera, cấu hình thông báo |
| SYSTEM_ADMIN | Toàn hệ thống | Quản lý site, audit log, circuit breaker |
| SUPER_ADMIN | Toàn quyền không giới hạn | Offboarding, cấu hình tenant-level |

---

### **3. PHẠM VI CHỨC NĂNG**

| Mã | Chức năng | Mô tả | Module | User Story |
| --- | --- | --- | --- | --- |
| SF01 | Quản lý thiết bị Camera | CRUD camera: deviceId, site, hướng In/Out, ngưỡng confidence. Toggle Active/Inactive. | m08 | US-CAM-01 |
| SF02 | Mapping nhân viên - Camera | Quản lý CVisionPersonMapping. Bulk-create từ Excel. Xử lý mapping thất bại. | m08 | US-CAM-02 |
| SF03 | Health check Camera | Dashboard trạng thái camera real-time. Heartbeat 5 phút. Cảnh báo IT khi offline. | m08 | US-CAM-03 |
| SF04 | Face ID Enrollment | Hỗ trợ NV đăng ký khuôn mặt. Re-enrollment khi thay đổi ngoại hình. | m08 | US-CAM-04 |
| SF05 | Cấu hình kênh thông báo | Bật/tắt Push, Email, Popup. Thiết lập fallback chain. | m09 | US-NOTIF-01 |
| SF06 | Cấu hình sự kiện kích hoạt | Quản lý 36 loại sự kiện. Bật/tắt trigger. Template nội dung. | m09 | US-NOTIF-02 |
| SF07 | Quản lý policy thông báo | Batching, Throttle, Schedule. NV preference cá nhân. | m09 | US-NOTIF-03 |
| SF08 | Quản lý chi nhánh | CRUD site: Tên, Mã, Timezone, Ngày chốt công. Deactivate khi thu hẹp. | m12 | US-SYS-01 |
| SF09 | Audit Log Viewer | Xem toàn bộ log hệ thống. Filter theo user, module, action, time. Export CSV. | m12 | US-SYS-02 |
| SF10 | Employee Offboarding | Quy trình tự động: hủy đơn, freeze phép, deactivate camera, re-route approval. | m12 | US-SYS-03 |

---

### **4. YÊU CẦU PHI CHỨC NĂNG**

- Camera health check: phát hiện offline trong 5 phút.
- Audit log: retention 3 năm, immutable (không sửa/xóa).
- Webhook C-Vision: xác thực HMAC-SHA256, idempotency check.
- Offboarding: hoàn thành tất cả bước trong 5 phút, ghi audit trail.

---

### **5. ĐIỀU KIỆN GIẢ ĐỊNH**

1. Camera AI (C-Vision) đã lắp đặt và kết nối internet.
2. Hệ thống Push Notification (Firebase/APNs) và Email (SMTP) đã tích hợp.
3. Tenant và ít nhất 1 site đã được khởi tạo.
