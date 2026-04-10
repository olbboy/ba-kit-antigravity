# BRD Nhân viên

---

****************************
| Thông tin | Nội dung |
| --- | --- |
| Target release | Version 1.0 |
| Epic | STRATOS-ESS: Trải nghiệm dành cho Nhân viên |
| Document owner | ndthuy1 |
| Stakeholder | Toàn bộ Nhân viên |
| Status | Open |

  

### **1. MỤC TIÊU**

- **Lý do tồn tại:** Nhân viên cần quyền truy cập thông tin công việc, chấm công và hiệu suất cá nhân chủ động.
- **Bài toán:** Loại bỏ việc hỏi đáp thủ công về giờ công, gửi đơn giấy và giúp nhân viên tự định danh khuôn mặt chấm công.
- **Giá trị mang lại:** Nâng cao sự hài lòng của nhân viên thông qua sự minh bạch về dữ liệu giờ công và KPIs.

### **2. MÔ TẢ QUY TRÌNH NGHIỆP VỤ**

```mermaid
graph TD
    A["👤 Nhân viên mở Mini App"] --> B["📊 Dashboard Cá nhân<br/>Giờ vào + Progress bar 8h"]
    
    B --> C["📒 Nhật ký Chấm công<br/>In/Out + Ảnh Face ID"]
    B --> D["📝 Trung tâm Đăng ký<br/>Nghỉ phép / Đổi ca / OT"]
    B --> E["⚠️ Giải trình công<br/>Muộn/Sớm + Minh chứng"]
    B --> F["📈 Báo cáo cá nhân<br/>KPI + Score chuyên cần"]
    B --> G["⚙️ Setup Hồ sơ<br/>Thông tin + Face ID"]

    D --> H["📤 Gửi đơn → PENDING"]
    E --> H
    H --> I["👔 Manager/HR phê duyệt"]
    I -->|"Duyệt"| J["✅ Cập nhật dữ liệu"]
    I -->|"Từ chối"| K["❌ Phản hồi lý do"]
    J --> B
    K --> B

    G -->|"Bước 1"| G1["Thông tin cá nhân"]
    G1 -->|"Bước 2"| G2["📷 Định danh Face AI"]
    G2 -->|"Bước 3"| G3["✅ Hoàn tất"]

    style A fill:#4CAF50,color:#fff
    style B fill:#1976D2,color:#fff
```

### **3. NHU CẦU NGƯỜI DÙNG**

  

************
| Persona | Nhu cầu cụ thể | Tài liệu |
| --- | --- | --- |
| Nhân viên | Muốn biết hôm nay mình đã làm được bao nhiêu tiếng (Progress) và bao giờ thì đủ 8 tiếng. | Dashboard Cá nhân |
| Nhân viên | Cần tự cập nhật ảnh quét khuôn mặt Face ID để không phải nhờ IT hỗ trợ. | Setup cá nhân |
| Nhân viên | Muốn xem báo cáo hiệu suất cá nhân (KPI) để biết mình có được thưởng năng suất. | Báo cáo hiệu suất cá nhân |

### **4. USE CASE**

```mermaid
graph LR
    NV["👤 Nhân viên"]

    F01["F01: Dashboard Cá nhân<br/>Giờ vào + Progress 8h"]
    F02["F02: Nhật ký Chấm công<br/>In/Out + Tag trạng thái"]
    F03["F03: Trung tâm Đăng ký<br/>Nghỉ phép / Đổi ca / OT"]
    F04["F04: Giải trình<br/>Muộn/Sớm + Ảnh"]
    F05["F05: Báo cáo cá nhân<br/>Score + KPI Highlights"]
    F06["F06: Setup Hồ sơ<br/>Thông tin + Face ID"]

    NV --> F01 & F02 & F03 & F04 & F05 & F06

    style NV fill:#4CAF50,color:#fff
    style F01 fill:#E3F2FD
    style F02 fill:#E3F2FD
    style F03 fill:#FFF3E0
    style F04 fill:#FFEBEE
    style F05 fill:#E8F5E9
    style F06 fill:#F3E5F5
```

### **5. PHẠM VI CHỨC NĂNG**

  

****************************************
| Mã | Chức năng | Mô tả | User Story |
| --- | --- | --- | --- |
| F01 | Dashboard Cá nhân | Xem giờ vào, Thanh tiến độ 8h (Progress bar) nhảy real-time. % Đúng giờ. | Là NV, tôi muốn xem mình đã làm đủ ca hôm nay chưa. |
| F02 | Nhật ký Chấm công | Danh sách ngày vào/ra kèm tag trạng thái (Đúng giờ/Vào trễ). | Là NV, tôi muốn đối soát lại giờ quẹt mặt tuần qua. |
| F03 | Trung tâm đăng ký | Form: Nghỉ phép, Đổi ca, OT, Nghỉ ko lương. Theo dõi hạn mức phép năm. | Là NV, tôi muốn gửi đơn xin nghỉ ngay trên điện thoại. |
| F04 | Giải trình cá nhân | Case: Giải trình muộn/sớm kèm ảnh. Case: Tự động khóa nút giải trình sau ngày chốt công. | Là NV, tôi muốn giải trình lỗi công để giữ chuyên cần. |
| F05 | Báo cáo cá nhân | Score chuyên cần, Tổng giờ làm tháng, Bảng KPI Highlights. | Là NV, tôi muốn theo dõi KPI năng lực quý của mình. |
| F06 | Setup Hồ sơ | Quy trình 3 bước: Thông tin cá nhân ➔ Định danh khuôn mặt AI ➔ Hoàn tất. | Là NV mới, tôi muốn tự đăng ký khuôn mặt để điểm danh. |

### **6. YÊU CẦU PHI CHỨC NĂNG**

- Giao diện  Web/Mobile Mini App, hỗ trợ đa nền tảng (iOS/Android).
- Đồng bộ dữ liệu khuôn mặt sang Camera AI thành công trong vòng < 60 giây.
- Thông báo Push Notification ngay khi trạng thái đơn phê duyệt thay đổi.
- Bảo mật thông tin khuôn mặt chỉ dùng cho định danh chấm công.

### **7. ĐIỀU KIỆN GIẢ ĐỊNH**

- Nhân viên đã được cấp tài khoản định danh trên hệ thống Stratos.
- Smartphone của nhân viên có camera hoạt động để thực hiện định danh (Enrollment).
