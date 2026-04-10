# 2.11.3. Giải trình công

---

************************
| Thông tin | Nội dung |
| --- | --- |
| Target release | Release 1.0 |
| Epic | EPIC-03 – Quản lý sai lệch công |
| Document owner | ndthuy1 |
| Stakeholder | Nhân viên, Quản lý trực tiếp, HR |
| Status | Open |

  

---

### **1. MỤC TIÊU**

- **Lý do tồn tại:** Trong thực tế vận hành, việc chấm công bằng AI/Camera có thể phát sinh sai sót (Lỗi nhận diện, Quên quẹt thẻ, Đi muộn vì lý do khách quan).
- **Bài toán:** Cung cấp kênh chính thống để nhân viên tự đính chính dữ liệu giờ công kèm minh chứng (ảnh/tài liệu).
- **Giá trị mang lại:**    - Giảm 80% khối lượng công việc phản hồi thủ công của HR vào cuối tháng.
    - Tăng tính tương tác và hài lòng của nhân viên thông qua quy trình phê duyệt minh bạch.

### **2. MÔ TẢ QUY TRÌNH NGHIỆP VỤ (WORKFLOW)**

```mermaid
graph TD
    A["⚙️ Hệ thống AI quét<br/>So khớp dữ liệu chấm công vs Lịch phân ca"] --> B{"Phát hiện<br/>sai lệch?"}
    B -->|"Không"| C["✅ Dữ liệu hợp lệ"]
    B -->|"Có"| D["⚠️ Tạo Anomaly<br/>Quên quẹt / Muộn / Sớm / Vắng"]
    D --> E["📱 Hiển thị danh sách lỗi<br/>trên App nhân viên"]
    E --> F{"Trước ngày<br/>chốt công?"}
    F -->|"Có"| G["🔴 Badge: CHỜ GIẢI TRÌNH<br/>NV nhấn tạo đơn"]
    F -->|"Không"| H["⛔ Badge: VI PHẠM QUY CHẾ<br/>Nút bị vô hiệu hóa"]
    G --> I["📝 NV nhập Form giải trình<br/>Lý do + Upload minh chứng"]
    I --> J["📤 Gửi đơn → PENDING"]
    J --> K["👔 Manager/HR phê duyệt"]
    K -->|"Duyệt"| L["✅ Cập nhật Nhật ký<br/>Tính lại trạng thái Đủ công"]
    K -->|"Từ chối"| M["❌ Giữ nguyên lỗi<br/>+ Lý do từ chối"]

    style D fill:#FF9800,color:#fff
    style H fill:#D32F2F,color:#fff
    style L fill:#4CAF50,color:#fff
```

### **3. NHU CẦU NGƯỜI DÙNG**

************
| Persona | Nhu cầu cụ thể | Tài liệu / Căn cứ |
| --- | --- | --- |
| Nhân viên | Biết rõ mình đang bị lỗi ngày nào, giờ nào ngay tại màn hình "Lỗi chấm công cần giải trình". | List Anomaly |
| Nhân viên | Dễ dàng tải ảnh minh chứng để tăng tính thuyết phục cho đơn. | Upload Evidence |
| Quản lý | Theo dõi trạng thái của các đơn (Đang chờ/Đã duyệt/Từ chối) để không bỏ lỡ yêu cầu của cấp dưới. | Request Status |

---

### **4. USE CASE DIAGRAM**

```mermaid
graph LR
    NV["👤 Nhân viên"]
    MGR["👔 Quản lý"]
    SYS["⚙️ Hệ thống"]

    UC1["Xem danh sách lỗi<br/>cần giải trình"]
    UC2["Tạo đơn giải trình<br/>Chọn ngày + Lý do"]
    UC3["Đính kèm minh chứng<br/>Ảnh / PDF ≤ 5MB"]
    UC4["Theo dõi trạng thái<br/>Pending / Approved / Rejected"]
    UC5["Xem lịch sử giải trình"]
    UC6["Phê duyệt / Từ chối<br/>đơn giải trình"]
    UC7["Quét phát hiện Anomaly<br/>tự động cuối ngày"]
    UC8["Khóa giải trình<br/>sau ngày chốt công"]

    NV --> UC1 & UC2 & UC3 & UC4 & UC5
    MGR --> UC6
    SYS --> UC7 & UC8

    style NV fill:#4CAF50,color:#fff
    style MGR fill:#2196F3,color:#fff
    style SYS fill:#607D8B,color:#fff
```

### **5. PHẠM VI CHỨC NĂNG**

** **

********************
| Mã | Chức năng | Mô tả chi tiết | User Story |
| --- | --- | --- | --- |
| F03.1 | List Lỗi cần giải trình | Hiển thị các block lỗi (Quên check-out, Vào muộn) được hệ thống AI tự động phát hiện. | Là NV, tôi muốn thấy lỗi của mình để giải trình kịp lúc. |
| F03.2 | Form Giải trình | Cho phép chọn Ngày, Lý do (Dropdown), nhập Nội dung văn bản. | Là NV, tôi muốn nhập lý do để giải thích rõ sự việc. |
| F03.3 | Đính kèm minh chứng | Vùng kéo thả file để upload bằng chứng thực tế. | Là NV, tôi muốn đính kèm ảnh để tăng độ tin cậy của đơn. |
| F03.4 | Trạng thái yêu cầu | Các Badge (Đã duyệt, Đang chờ, Từ chối) hiển thị tại cụm "Yêu cầu gần đây". | Là NV, tôi muốn theo dõi tiến độ duyệt đơn để yên tâm về ngày công. |
| F03.5 | Xem tất cả | Link chuyển hướng xem toàn bộ lịch sử giải trình trong quá khứ. | Là NV, tôi muốn xem lại các đơn cũ để đối soát lương cuối tháng. |

---

### **6. YÊU CẦU PHI CHỨC NĂNG**

1. **Dung lượng File**: Hỗ trợ upload ảnh (.jpg, .png) và tài liệu (.pdf) không quá 5MB.
2. **Tính tích hợp**: Sau khi đơn được duyệt, dữ liệu mốc giờ công màn Nhật ký phải được cập nhật **Real-time**.
3. **Bảo mật**: Chỉ có Quản lý của phòng ban đó mới thấy được nội dung giải trình và minh chứng của nhân viên cấp dưới.

---

### **7. ĐIỀU KIỆN GIẢ ĐỊNH (PRE-CONDITION)**

1. Nhân viên đã được định danh và gán Ca làm việc.
2. Hệ thống AI đã ghi nhận dữ liệu chấm công thực tế để làm căn cứ so sánh lỗi.
