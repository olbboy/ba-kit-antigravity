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

**
bottomBRD Giải trình công.pngrVVNj5swEP01ljaHSnwkm3C0Id4edqNWqra9UqCxFT4icKLm33c8xgZvSdRDowiN8fjNmzczhqyDQeW9ujQ1CTISUCVVXZEo+Hq5wVP1JI0JTVsBixdJ9iFhlNBYftwrtM3W7dGgmOdwku057/MGHGih5FUqDUq2bPQC2/5ZXpyOfXdpy7Srux7efBdSVQuOXV9WvXUiURxtnuO9RdxmcwJkm4ID33HKU7A/I39GdltNX4yrJATWUZB+epeD7Fp9xrDXuow4Mf0iMNtQgauQDqiFZW2BtlqWQliVNo0nTMwcGEnXJAmsX3JDP6st6vnTROvAvKIZaLPMcXMwm4VAAaJXP74FQm7H+zWLJkYzsfacP3MO9sEkHGmUq0SbTuJAEj+qZpmSr4eyBEK9akwyGlT8U2vNVEttxXbZguxe2r/HPZqhoy6Btsg+IsmeJGuw3+xxDgve9c1DtWY0Dq7A2RmcXh162WE9GDwPFjzROOUFO6wQCGpjMK4WekIHzFCTE9o7zetNmiGzAtAEAZ8skUhvcy7rarXMdKNFIRv24nSRD9PdZIvNwfEH9sLtMA4IxXxvbkDUvGX88Eq42fAavhAdXkDTRHhFhKgGhYWFr+fZkZa/tDx3ITKPYMxXyKZqUdNpNqF+MZIzB1d/X0a6K71uaKfmUBNX3f0IpMZbRJrJndU8hjfnexLOZ9WP/s1pgTQBLnSthxEHJ3mO42fvvGKqPyyNrh2eOPgpnEbVLIGqHvT34clGpmzemUko/79Md0M9EuZhcx3e/QGr/SFWdwM6FdoSemz+rVPdeVyvA9h1H9Q/fittrue1
**

### **3. NHU CẦU NGƯỜI DÙNG**

************
| Persona | Nhu cầu cụ thể | Tài liệu / Căn cứ |
| --- | --- | --- |
| Nhân viên | Biết rõ mình đang bị lỗi ngày nào, giờ nào ngay tại màn hình "Lỗi chấm công cần giải trình". | List Anomaly |
| Nhân viên | Dễ dàng tải ảnh minh chứng để tăng tính thuyết phục cho đơn. | Upload Evidence |
| Quản lý | Theo dõi trạng thái của các đơn (Đang chờ/Đã duyệt/Từ chối) để không bỏ lỡ yêu cầu của cấp dưới. | Request Status |

---

### **4. USE CASE DIAGRAM**

**
bottomUC Giải trình công.pnglVRta4MwEP41ge5DR3yb7Udf1g3KBmMt7GtQa8I0Fo0D//3uEnW2xcqgjXdn7p7nnlwkLm0Uq1VbFoTGhAZKqCIjNj02uEZMP2LB8pqVYK3h/yLIs0XCgASOAFfVJHJIEEkOToJ26MrcVCuyk8ItFSy1yDk6qaizRIlKmi1mZYmqanhJbPud63q2BPdHaDsA2waXNbB8KnY63WR9tCMpTCw0j3iS9sYky7N6CnpmyTfETIFXnR+SjY+Eee9tLWjlbssIQPywr4ul+l/bZImRDzZ9ZaheyrRIjc62Eq6J9kA+Fk74gOOVF2r+9XGMnEdrAW0/0t9pukNRC8+BRC60RaIn8FGq/M5xSs6GHkdwewH8eC4qloJdCjMSA5lgq7VcDXA2vt4dNBxF6EKMZ9A+XKE6C6gHnmFzqVbMExNlN2FiRO9ZwFDQzoxVqzXu6fjo5aMnJ1LhOHZXhNwFQsM8BX73T9FXe97PAmwPKcO22m6URl1L4/VM/Hg63OaawI1dXw7NTdyeiTszcXcm7k3Rh9t2kQcyOMHccYEEw5TqMVHmM2AJ7NZUdmkm0/FL9Qs=fittrue1
**

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
