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

**
bottomWF Cấu hình lịch nghỉ.pnglVVtb9pADP41J7XfAkca8vEuaYa0Dmkbavs1TRg5Ee5QuHTqv599bxxQqCZVNA62H/t5bENmyUHXgx53PUlKkjAtdL8m0+RFDds/vfoLjz9H8jghnBFGJZg9KSjhJTw9mfeczHnTgUmmD/C53OD3LPmAZ7npvEsO5t0P1Y4me5LdW7jDVsh9PdQ7eMkaLd6F/uB1s90MapRtoXo1mMy0mlesKm4EqaFdD1HANH2gj9wGuM+sWPzCkHYnJBguGbbvHChbDSMW3viOyz1YhbfSEazO9FfI7r8ZoK4cqB1oFkqakOmqEw6AV9oQHIOfQQQzhUiMz3yPmMv/UVYE3FKe1lStbAcTuYEv9GAMhk5F3a9lWw+h0LOc31wc1qh8kRNxKXQfFZncufnhJJ80YG9EDUUs/bsc49+CdX8N/IkUD4QnqEBbG/IPthygJYRkZSz4Gc/fjX9paOyO9SPlji1UAH2LGdQaSjp9Az4ZtvEmfJOZvi0FD3pqZN9bRmuS8uUpd7+FaU52UVRaXmPl9uwsQpNIwc7BsLyxyKYr09ucmmHYhtV+qRaICuo9AzaiYodvQckUVKt0OAyZvKrb7QqfDWJu0I9XprNrhnp7wMq6XNCF6cMA61q4qmXAHM06Iwq9vzYocAyWdimmmOY9pPRHAvp4Xe8ut/Fs7hubpDQN6O6E73jR2H5/LIWy5VFraZJevaDaGXxyOaZunZX9H+/44ZORiuC/GINpZR1EIHJmIdz6GbS1MpLdGDdbLIbQ+MCenVR6cbHDlsWU5thYJM7qS14iYeImYHM9AqP7+HRldqmbDjtbPuNYWFmUT2F7j9WKjvMlv67hHB1bj4nnpj9eEiTjUJvKuIWI0FT4hXkNi5celTxotXeYswTuePhJ/wc=fittrue1
**

### **3. NHU CẦU NGƯỜI DÙNG**

************
| Persona | Nhu cầu cụ thể | Tài liệu / Căn cứ |
| --- | --- | --- |
| HR Admin | Muốn gán các ngày Lễ quốc gia (Tết, 30/4) để hệ thống tự động tính đủ công cho nhân viên mà họ không cần chấm công. | Holiday Catalog |
| Nhân viên | Muốn biết được trong năm có bao nhiêu ngày nghỉ Lễ chính thức và chính sách WFH của công ty như thế nào. | Personal Dashboard |
| Ban Lãnh đạo | Muốn kích hoạt nhanh chế độ "Nghỉ thiên tai" cho một khu vực/văn phòng cụ thể khi có sự cố khẩn cấp. | Disaster Recovery Policy |

---

### **4. USE CASE DIAGRAM**

**
bottomUC Cấu hình ngày nghỉ.pngpVTJboMwEP2akdpDKrOV5migUaS2kbqpvTpAwCpLBKbf3/FGgCjKoRIy857HfjPPBvBJL1gnhroCkgChVX4Q4BLR4tDxopQg412eCt42OoWlou2QBtfdvuGbZjVvEGDI+hEvU3clxB5QFzPJL1cxna56F+xw0Kv0eGTpDytyvfqlzYZKxiQEj+L7dYBHByIK1JM7VnLDKMHoWfERPERpqdbe47grSkuvtSaEkRGTOeYZ+jxlvZH8KLmRiDZCSRjB5Iiome1oJhEECG5McRGsnRRxwRm4m53l1hy5/YhuJyZ8xuGdc6Wu2NYRDEhoV+NG9hprkCjQq9hRJszbJxD7WJltLpQl7rlNCMWiHvdfPm0tcuQx1UaFrqXo12a70PKuaH3n9fkRL44i1Y3LidOVm6n4V1SetI1q87IdGxDaYtvr3Eh5kudOi/J004lgfFFIYAoJk+nFN98TWa3mN+KMdy/w3gU+mKro720ya13xSd5k4//gDw==fittrue1
**

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
