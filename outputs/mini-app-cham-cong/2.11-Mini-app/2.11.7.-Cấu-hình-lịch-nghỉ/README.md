# 2.11.7. Cấu hình lịch nghỉ

---

****************************
| Thông tin | Nội dung |
| --- | --- |
| Target release | Version 1.0 (Sprint 8) |
| Epic | STRATOS-ADMIN: Hệ thống Quản trị & Cấu hình tập trung |
| Document owner | Business Analyst Team |
| Stakeholder | HR Admin, Toàn bộ Nhân viên |
| Status | Open |

  

---

### **1. MỤC TIÊU**

- **Lý do tồn tại:** Chuẩn hóa lịch trình nghỉ lễ của công ty và tự động hóa các chính sách đãi ngộ đặc thù (Sinh nhật, Bão lũ, WFH).
- **Bài toán:** Tránh việc nhân viên phải quẹt thẻ vào các ngày lễ quốc gia; Quản lý hạn mức làm việc từ xa (WFH) một cách công bằng.
- **Giá trị mang lại:** Giảm 90% khiếu nại về chấm công trong các ngày nghỉ lễ; Tự động hóa việc cộng ngày nghỉ sinh nhật cho nhân sự.

---

### **2. MÔ TẢ QUY TRÌNH NGHIỆP VỤ**

```mermaid
graph TD
    A["📋 HR Admin cấu hình"] --> B["📅 CRUD Danh mục ngày nghỉ<br/>Lễ quốc gia / Nội bộ"]
    A --> C["⚙️ Cấu hình Policy & Rules<br/>Sinh nhật / WFH / Thiên tai"]
    
    B --> D["🔄 Batch Job 00:01 hằng ngày<br/>Quét toàn bộ NV"]
    C --> D
    
    D --> E{"Ngày hôm nay<br/>là ngày nghỉ?"}
    E -->|"Có"| F["✅ Gán trạng thái<br/>HỢP LỆ / HƯỞNG LƯƠNG"]
    E -->|"Không"| G{"NV có sinh nhật<br/>trong tháng?"}
    G -->|"Có + NV chính thức"| H["🎂 Cộng 1 ngày phép<br/>vào quỹ phép cá nhân"]
    G -->|"Không"| I["➡️ Bỏ qua"]
    
    F --> J["📱 App NV hiển thị<br/>Calendar màu sắc + Thông báo"]
    H --> J
    
    C --> K{"Kích hoạt<br/>Nghỉ thiên tai?"}
    K -->|"Có"| L["🌊 Chọn vùng ảnh hưởng<br/>→ Gán nghỉ khẩn cấp<br/>cho NV thuộc khu vực"]

    style A fill:#FF9800,color:#fff
    style F fill:#4CAF50,color:#fff
    style H fill:#E91E63,color:#fff
    style L fill:#F44336,color:#fff
```

### **3. NHU CẦU NGƯỜI DÙNG**

************
| Persona | Nhu cầu cụ thể | Tài liệu / Căn cứ |
| --- | --- | --- |
| HR Admin | Muốn gán các ngày Lễ quốc gia (Tết, 30/4) để hệ thống tự động tính đủ công cho nhân viên mà họ không cần chấm công. | Holiday Catalog |
| Nhân viên | Muốn biết được trong năm có bao nhiêu ngày nghỉ Lễ chính thức và chính sách WFH của công ty như thế nào. | Personal Dashboard |
| Ban Lãnh đạo | Muốn kích hoạt nhanh chế độ "Nghỉ thiên tai" cho một khu vực/văn phòng cụ thể khi có sự cố khẩn cấp. | Disaster Recovery Policy |

---

### **4. USE CASE DIAGRAM**

```mermaid
graph LR
    HR["📋 HR Admin"]
    NV["👤 Nhân viên"]
    BGD["🏢 Ban Lãnh đạo"]
    SYS["⚙️ Hệ thống"]

    UC1["CRUD Danh mục ngày nghỉ<br/>Lễ quốc gia / Nội bộ"]
    UC2["Cấu hình Policy<br/>Sinh nhật / WFH"]
    UC3["Kích hoạt Nghỉ thiên tai<br/>Chọn vùng ảnh hưởng"]
    UC4["Clone lịch nghỉ<br/>sang năm mới"]
    UC5["Xem Calendar cá nhân<br/>Mã màu Đỏ/Xanh"]
    UC6["Xem chi tiết ngày nghỉ<br/>Loại + Đãi ngộ"]
    UC7["Batch Job tự động<br/>Gán công 00:01"]
    UC8["Gửi thông báo<br/>trước 3 ngày nghỉ lễ"]

    HR --> UC1 & UC2 & UC4
    BGD --> UC3
    NV --> UC5 & UC6
    SYS --> UC7 & UC8

    style HR fill:#FF9800,color:#fff
    style NV fill:#4CAF50,color:#fff
    style BGD fill:#F44336,color:#fff
    style SYS fill:#607D8B,color:#fff
```

### **5. PHẠM VI CHỨC NĂNG**

************************************************
| Mã | Chức năng | Mô tả chi tiết | User Story |
| --- | --- | --- | --- |
| F07.1 | Quản trị Danh mục ngày nghỉ | Giao diện CRUD quản lý danh sách ngày nghỉ (Lễ quốc gia/Nội bộ). Hỗ trợ chọn ngày trên Calendar và gán loại hình nghỉ hưởng lương/không lương. | Là Admin, tôi muốn tự thiết lập danh mục ngày nghỉ để hệ thống có căn cứ tính công tự động cho toàn công ty. |
| F07.2 | Cấu hình Policy & Rules | Quản lý tham số: Bật/Tắt nghỉ sinh nhật; Hạn mức WFH tối đa/tuần; Kích hoạt Chế độ khẩn cấp (Thiên tai) cho từng khu vực/văn phòng. | Là Admin, tôi muốn cấu hình các tham số luật (Rules) để hệ thống tự động hóa các chế độ đãi ngộ mà không cần can thiệp thủ công. |
| F07.3 | Logic Sync & Batch Job | Tự động quét dữ liệu Ngày nghỉ/Sinh nhật để gán trạng thái "Hợp lệ" trên Nhật ký nhân viên. Đồng bộ Real-time mốc WFH/Công tác lên Dashboard. | Hệ thống tự động đồng bộ và tính công dựa trên lịch nghỉ/chính sách đã cấu hình để đảm bảo quyền lợi nhân viên chính xác 100%. |
| F07.4 | API & Mini App View | Xây dựng bộ API truy vấn lịch trình cá nhân. Hiển thị Calendar màu sắc (Đỏ/Xanh) và các thông báo nhắc nhở ngày nghỉ lễ trên App nhân viên. | Là Nhân viên, tôi muốn tra cứu lịch trình nghỉ lễ và hạn mức vắng mặt qua App để chủ động sắp xếp kế hoạch làm việc. |

### **6. YÊU CẦU PHI CHỨC NĂNG**

- **Tính kế thừa:** Lịch nghỉ lễ của năm nay có thể Clone sang năm sau để Admin chỉ cần chỉnh sửa ngày lẻ.
- **Thông báo:** Tự động gửi thông báo cho toàn thể nhân viên trước 03 ngày diễn ra nghỉ lễ chính thức.
- **Ràng buộc:** Không được gán 2 loại lễ trùng ngày nhau trên cùng một lịch làm việc.

---

### **7. ĐIỀU KIỆN GIẢ ĐỊNH**

1. Hệ thống đã có danh sách nhân sự kèm Ngày sinh chính xác.
2. Quy hoạch location đã được gán để phục vụ việc bật "Nghỉ thiên tai" theo vùng.
