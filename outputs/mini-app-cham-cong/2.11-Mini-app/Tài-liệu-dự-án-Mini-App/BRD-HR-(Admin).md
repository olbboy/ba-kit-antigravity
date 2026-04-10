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

```mermaid
graph TD
    A["👔 HR Admin đăng nhập<br/>Hệ thống Quản trị"] --> B["📊 Dashboard Admin<br/>On-site / WFH / Vắng"]
    
    B --> C["🏢 Cơ cấu tổ chức<br/>Sơ đồ cây + Import NV"]
    B --> D["⏰ Cấu hình Ca<br/>In/Out/Break + Punch Limit"]
    B --> E["📅 Lịch & Ngày nghỉ<br/>Lễ tết + Policy"]
    B --> F["📷 Camera AI<br/>Device + Mapping + Health"]
    B --> G["🔔 Thông báo<br/>36 events × 3 channels"]
    B --> H["✅ Phê duyệt<br/>Nghỉ/OT/Giải trình/Đổi ca"]
    B --> I["📈 Báo cáo & Xuất<br/>Payroll Excel + KPI"]

    C -->|"Import Excel"| J["💾 Master Data NV"]
    D -->|"Áp dụng"| K["⚙️ Engine tính công"]
    E -->|"Batch Job"| K
    F -->|"Webhook"| K
    K --> I

    style A fill:#FF9800,color:#fff
    style B fill:#1976D2,color:#fff
```

### **3. NHU CẦU NGƯỜI DÙNG**

  

************
| Persona | Nhu cầu cụ thể | Tài liệu |
| --- | --- | --- |
| HR | Cần quản lý camera điểm danh và cài đặt quy tắc bắn thông báo login fail/muộn sớm. | Cấu hình camera & Notification |
| Quản lý | Xem báo cáo tổng hợp quân số theo phòng ban để nắm bắt tình hình đi làm thực tế. | Dashboard Admin |
| HR Admin | Thiết lập các ca làm dự kiến và giờ nghỉ để hệ thống tính công tương ứng. | Quản lý Ca làm việc |

### **4. USE CASE**

 
```mermaid
graph LR
    HR["📋 HR Admin"]
    MGR["👔 Quản lý"]
    IT["🔧 IT Admin"]

    F01["F01: Dashboard<br/>Quân số + Biểu đồ"]
    F02["F02: Cơ cấu tổ chức<br/>NV + Phòng ban"]
    F03["F03: Cấu hình Ca<br/>In/Out/Break"]
    F04["F04: Lịch & Ngày nghỉ<br/>Lễ + Policy"]
    F05["F05: Camera AI<br/>Device + Mapping"]
    F06["F06: Thông báo<br/>36 events + Policy"]
    F07["F07: Phê duyệt<br/>Nghỉ/OT/Giải trình"]
    F08["F08: Báo cáo & Xuất<br/>Payroll + KPI"]

    HR --> F01 & F02 & F03 & F04 & F07 & F08
    MGR --> F01 & F07 & F08
    IT --> F05 & F06

    style HR fill:#FF9800,color:#fff
    style MGR fill:#2196F3,color:#fff
    style IT fill:#9C27B0,color:#fff
```

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
