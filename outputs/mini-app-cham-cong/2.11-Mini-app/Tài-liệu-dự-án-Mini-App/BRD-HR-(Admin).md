# BRD HR (Admin)

---

****************************
| Thông tin | Nội dung |
| --- | --- |
| Target release | Version 1.0 |
| Epic | STRATOS-ADMIN: Hệ thống Quản trị & Cấu hình tập trung |
| Document owner | ndthuy1 |
| Stakeholder | CEO, HR Admin, IT |
| Status | Open |

### **1. MỤC TIÊU**

- **Lý do tồn tại:** Doanh nghiệp cần công cụ quản lý nhân sự tập trung, thay thế các phương thức thủ công.
- **Bài toán:** Giải quyết việc cấu hình ca làm việc phức tạp (ca đêm, ca hành chính), quản lý thiết bị AI Camera và phê duyệt yêu cầu từ nhân viên trên một nền tảng duy nhất.
- **Giá trị mang lại:** Tự động hóa dữ liệu chấm công, tăng tính minh bạch và cung cấp báo cáo quản trị tức thời.

### **2. MÔ TẢ QUY TRÌNH NGHIỆP VỤ**

**
bottomWF Mini App HR.pnglVbbctowEP0azZAHZowNIX70BUOmhFCgpG8ZxXawBl+oLbfl77srWYqchCQdgqO193r27BoythpOa94WObFCYnmc8TwltvVQ1cfnvPoDx+8tmY2I7xHPKUHktRB9cuODROxruO6VRogaGQkc4lllBuchfLe8prxq4LTYwGXgJQUDveiOlvSQ1lcycnNk5YnWtAAVL+bsN+Nnn8bHQ121ZRJUeVWLeE4U4ucDo6pO0towsCfXzsyXBt11Gtzu0ERkMg06Z4hEp+B4u7o9g0qsSzuBFChp0upCA1HoQqEyRYyyTnJH5YE4vnYKWKKJy0EpocKwEXdGMZ4DWqQ1RQedvYcYJ0qIQMiZDoQpBEOw0REACmggq0pRuH05Wx2IBGPiWtqnU+jEbHw6VamjP/XneIGq70Y0XHvLZecL5XjUd9yZYUKFgBa0/bGJUD/MXEKDIQoNaAzSL0VJXyA5CLI0Pg4FqeSxavnVJa9LElwT32pfuOxhkIPsm4jIsKGVfsZ1PSoL10x6Gr7ilqB5n1tf7sx3wTqunkdY7i7TSNnWk0yx+q8ONZ3kj0A4vlAInw32IRjAIfJul7PwcXk/v10RSNG2fmxnm8dgM/N2s/Ainq9CfRP5eaKYMusthsG6beB2NCsoy+H/9m570esuY6rHERfU6s1hhrgdVVUOOl8dKEAXrQ6yv2poRGejeQWMi5Z6dcXZV/ixacUyXFc5i8/vNPzTNHEoBtuMPfPmSm/LucLf9ZnovubgO9Ret6VYDUtWMJPTn4U2S9WR9QD60VtKY7QFVJrQcyPb/xAtxMaByI0RWtH81YtBDL8fohu92RX9cZiZJG7xsvO4rBfPtslSF1ka0iZ7qmidoMNNSvMhZ0XaQ+BntzrfMu2jwV7tzQETt8REQte9kbnxxWyqTexO8JGiuufGOH9GLmsZAcmUwAirAdOrw5L+S8lUPTKI+kmautC26B5eS1FnoAJjhjFFEjMNOJNFdnvjneZ88D4ymmJEQlJgdqAglvjZrNcVvYqNNTRYGXr2pNeXvdRDbvffVnKPOVT0XYMkQLlYm9E9ERiSmABYPR5oIk54b0PKjOUx79aCbAN6WtNzXeW5qFN7cDGZ2d84zXWEhlenLtbYSstE/1iS138=fittrue1
**

### **3. NHU CẦU NGƯỜI DÙNG**

  

************
| Persona | Nhu cầu cụ thể | Tài liệu |
| --- | --- | --- |
| HR | Cần quản lý camera điểm danh và cài đặt quy tắc bắn thông báo login fail/muộn sớm. | Cấu hình camera & Notification |
| Quản lý | Xem báo cáo tổng hợp quân số theo phòng ban để nắm bắt tình hình đi làm thực tế. | Dashboard Admin |
| HR Admin | Thiết lập các ca làm dự kiến và giờ nghỉ để hệ thống tính công tương ứng. | Quản lý Ca làm việc |

### **4. USE CASE**

 
bottomUC Mini App HR.pngpVbbTuMwEP0aS/CAFJoW6GMuLaC9sdBFvK2MaxKraVw5Dgt/v2M7dm0Xqm1XqlxfJjNn5syMjcZJJ7GQ/bpBSYmSrKEvEo0SyWEQrKrVYskEJZLx1ohgIrmAbTQa3dzDf7ZcsxYWMMWdW8eit4sPRGEzlrurUZGifNRWsH7GIJ2cfMMtrqg49b4ctsznZtxgsoI9o2Yheq1BKm3ZaA3Tnz2anaM8Q1mqtEqhlzm6ymH1IAWWXGlWPikz6DIftCuF9rezE1jda+LGLi7VUT2spucaJxpdwFjgNRV4n33v13eU4G6wXFh9V2Xr1F1r589bT3OCijHYZFY6VZFZ4rb2Yvur+A3iRc0ZoYdAsL5PetjQNGaFUpykFzr875qPQWhOYLUwZI8N2QYtD5F855Ld9w3tDkAS0dBoI6WOOhtO8rnUJj1+XIiy251glPQVgvERhsvSz8FPM2MRWW4swnLzSWwKLzTy/aic+JSQQrl5UtSUrM5UQc55D6AK2LzrW6IkGrZm8jSMw0PNXuShXOx3vMANbZdYbCugdtIuWW2lTGGnrVyiT2OWBlVHc/TooLUuXomOl8FmWlOmFCyBMFvN8hhurpnJdlV+nZmq6JS4q585FkvnvGKK+D6DuO0cYQDUt17v/Td2hM68N1cwE2lS7wIAKctBCklreeKDyqYkRO6D+iGqR0b/HADpyaotg9K1dFRxWmQp28uNkU6MS63nRZaHULPNRvBXWnLyH3VeWuVzXUQOSB9nuOJP6gi7Mj88i55C3nLXQY1aMx2SF78L3jQwm70R2oSuz942XMhjrpvBiVr5txr28tRZ/WIafKqyuGKuKyvG4HJ0DcnHsqBi/ZWT1T4OQjKGV0VydoY+7FPxedgp4tMgY+NDP1DxWQRcj/rVs7UbXKrxWXDHBIfxHahH+wLaikUNYFcgcG33eLcAzDhOIFzuhfgXfittrue1

### **5. PHẠM VI CHỨC NĂNG**

  

************************************
| Mã | Chức năng | Mô tả | User Story |
| --- | --- | --- | --- |
| F01 | Màn hình chính | Số lượng nhân viên (On-site/WFH/Vắng). Biểu đồ chuyên cần hằng ngày. | Là Manager, tôi muốn xem nhanh danh sách nhân viên trong ngày. |
| F02 | Cơ cấu tổ chức | View danh sách NV: ID, Phòng ban, Giờ check-in cuối và trạng thái hiện tại. | Là HR, tôi muốn biết ai đang hiện diện thực tế tại VP. |
| F03 | Cấu hình Ca | Thiết lập In/Out/Break. Case: Ca đêm (Crossing 00:00). Case: Punch limit. | Là Admin, tôi muốn tạo ca làm việc linh hoạt. |
| F04 | Lịch & Ngày nghỉ | Quản lý nghỉ lễ & nghỉ chính sách (Nghỉ sinh nhật, hạn mức WFH). | Là Admin, tôi muốn quản lý lịch nghỉ lễ toàn công ty. |
| F05 | Cấu hình Camera | Chọn Device ID từ C-Cam. Gán mục đích In/Out cho từng Camera. | Là IT, tôi muốn chọn camera sảnh làm máy chấm công. |
| F06 | Cấu hình Thông báo | Cấu hình cho 36 sự kiện. Chọn Policy (Gom tin/Chống nhiễu/Lập lịch). | Là Admin, tôi muốn nhận cảnh báo security tức thời. |
| F07 | Trung tâm Phê duyệt | Xử lý tập trung đơn Nghỉ/OT/Giải trình/Đổi ca từ nhân viên. | Là Quản lý, tôi muốn duyệt đơn nhanh gọn trên mobile. |
| F08 | Báo cáo & Xuất | Kết xuất Excel: Payroll chuẩn, Báo cáo Tuân thủ, Báo cáo KPI tổng. | Là HR, tôi muốn xuất dữ liệu chuẩn để tính lương tháng. |

### **6. YÊU CẦU PHI CHỨC NĂNG**

- Giao diện web, tương thích trên cả web và mobile.
- Hỗ trợ tìm kiếm nhanh, không phân biệt hoa/thường/dấu.
- Role-based & attribute-based access (RBAC + ABAC) theo Phòng ban.
- Xuất dữ liệu định dạng Excel theo mẫu chuẩn.

### **7. ĐIỀU KIỆN GIẢ ĐỊNH**

- Người dùng đã đăng nhập vào hệ thống quản trị trung tâm.
- Thiết bị Camera AI đã hoạt động và stream được dữ liệu ID về Server.

---
