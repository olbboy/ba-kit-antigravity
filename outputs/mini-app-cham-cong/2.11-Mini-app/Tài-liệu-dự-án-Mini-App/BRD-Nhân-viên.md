# BRD Nhân viên

---

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
    A([Nhan vien mo Mini App]) --> B[Dashboard Ca nhan<br/>Gio vao + Progress bar 8h]

    subgraph Features["6 chuc nang ESS"]
        C[Nhat ky Cham cong<br/>In/Out + Anh Face ID]
        D[Trung tam Dang ky<br/>Nghi phep / Doi ca / OT]
        E[Giai trinh cong<br/>Muon/Som + Minh chung]
        F[Bao cao ca nhan<br/>KPI + Score chuyen can]
        G[Setup Ho so<br/>Thong tin + Face ID]
    end

    B --> C & D & E & F & G

    subgraph Approval["Luong phe duyet"]
        D & E --> H[Gui don - PENDING]
        H --> I{Manager/HR<br/>phe duyet}
        I -->|Duyet| J[Cap nhat du lieu]
        I -->|Tu choi| K[/Phan hoi ly do/]
    end

    subgraph Setup["Dang ky Face ID"]
        G -->|Buoc 1| G1[Thong tin ca nhan]
        G1 -->|Buoc 2| G2[Dinh danh Face AI]
        G2 -->|Buoc 3| G3[Hoan tat]
    end

    classDef start fill:#4CAF50,color:#fff,stroke-width:2px
    classDef dashboard fill:#1976D2,color:#fff,stroke-width:2px
    classDef feature fill:#E3F2FD,stroke:#1565C0,color:#0D47A1
    classDef success fill:#66BB6A,color:#fff,stroke-width:2px
    classDef fail fill:#EF5350,color:#fff,stroke-width:2px

    class A start
    class B dashboard
    class C,D,E,F,G feature
    class J,G3 success
    class K fail
```

### **3. NHU CẦU NGƯỜI DÙNG**

| Persona | Nhu cầu cụ thể | Tài liệu |
| --- | --- | --- |
| Nhân viên | Muốn biết hôm nay mình đã làm được bao nhiêu tiếng (Progress) và bao giờ thì đủ 8 tiếng. | Dashboard Cá nhân |
| Nhân viên | Cần tự cập nhật ảnh quét khuôn mặt Face ID để không phải nhờ IT hỗ trợ. | Setup cá nhân |
| Nhân viên | Muốn xem báo cáo hiệu suất cá nhân (KPI) để biết mình có được thưởng năng suất. | Báo cáo hiệu suất cá nhân |

### **4. USE CASE**

```mermaid
graph LR
    subgraph Actor
        NV([Nhan vien])
    end

    subgraph View["Xem thong tin"]
        F01[F01: Dashboard Ca nhan<br/>Gio vao + Progress 8h]
        F02[F02: Nhat ky Cham cong<br/>In/Out + Tag trang thai]
        F05[F05: Bao cao ca nhan<br/>Score + KPI Highlights]
    end

    subgraph Action["Thao tac"]
        F03[F03: Trung tam Dang ky<br/>Nghi phep / Doi ca / OT]
        F04[F04: Giai trinh<br/>Muon/Som + Anh]
        F06[F06: Setup Ho so<br/>Thong tin + Face ID]
    end

    NV --> F01 & F02 & F05
    NV --> F03 & F04 & F06

    classDef actor fill:#37474F,color:#fff,stroke-width:2px
    classDef view fill:#E3F2FD,stroke:#1565C0,color:#0D47A1
    classDef action fill:#FFF3E0,stroke:#E65100,color:#BF360C

    class NV actor
    class F01,F02,F05 view
    class F03,F04,F06 action
```

### **5. PHẠM VI CHỨC NĂNG**

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
