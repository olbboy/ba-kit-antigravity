# 2.11 Mini app

---

### **1. MỤC TIÊU**

Hệ thống ra đời nhằm giải quyết bài toán chấm công thủ công thiếu minh bạch và chậm trễ trong việc cập nhật dữ liệu cho nhân viên.

- **Lý do tồn tại:** Tự động hóa việc ghi nhận công sức thông qua công nghệ AI Vision, giúp minh bạch hóa quyền lợi giữa NV và công ty.
- **Bài toán:** Loại bỏ việc "quên chấm công", giảm sai sót khi tính lương và tối ưu luồng đơn từ phê duyệt (Nghiệp phép, OT, Công tác).
- **Giá trị mang lại:** Giảm 70% khối lượng công việc đối soát cho HR, tăng 100% tính minh bạch dữ liệu cho nhân viên.** **

### **2.**** DANH SÁCH TÍNH NĂNG**

**Module 01: Chấm công & Nhật ký**

- Dashboard Trạng thái: Hiển thị mốc giờ Vào/Ra thực tế; Badge [Đã chấm công/Chưa chấm công].
- Thanh Tiến độ làm việc: Tính toán % dựa trên Giờ hiện tại so với Giờ vào của ca.
- Nhật ký Accordion: Tra cứu mốc quẹt kèm ảnh Face ID của 30 ngày gần nhất.
- Logic Ca Đêm (20h - 06h):    - Mốc quẹt từ 20:00 (Ngày T) đến 06:00 (Ngày T+1) được gán vào Nhật ký của Ngày T.
    - Thanh tiến độ tiếp tục chạy xuyên đêm (không bị reset tại mốc 24:00).

**Module 02: Trung tâm Đăng ký**

- Đăng ký nghỉ: Nghỉ phép (trừ quỹ phép), Nghỉ không lương, Nghỉ ốm/thực tế.
- Đổi ca & OT: Cho phép NV chọn ngày và ca cần đổi; Đăng ký làm thêm giờ (OT) kèm mốc thời gian cụ thể (Ví dụ: 18:00 - 20:00).
- Ràng buộc: Chặn đăng ký trùng ngày/giờ; Chặn xóa đơn đã được Duyệt.

**Module 03: Giải trình công**

- Tạo đơn giải trình: Bổ sung mốc giờ In/Out còn thiếu do lỗi thiết bị hoặc quên quẹt.
- Logic: Sau khi HR duyệt đơn ➔ Hệ thống tự động cập nhật giờ giải trình vào Nhật ký (Module 01) và tính lại trạng thái "Đủ công".

**Module 04: Báo cáo cá nhân**

- Thống kê hiệu suất: Tỷ lệ đi làm đúng giờ (%); Số ngày nghỉ trong tháng; Tổng giờ OT lũy kế.
- Cập nhật dữ liệu: Real-time ngay khi có mốc quét camera hoặc đơn từ được Phê duyệt.

**Module 05: Quản lý Nhân sự & Cơ cấu tổ chức**

- Danh bạ NV: Quản lý họ tên, Email, ID, Phòng ban, Trạng thái (Active/Inactive).
- Theo dõi hiện diện: Dashboard hiển thị ai đang có mặt, ai đang vắng mặt hoặc đang làm Work From Home.
- Bulk Import: Nhập danh sách NV mới từ Excel mẫu (.xlsx). Hệ thống Validate Mã nhân viên và Email duy nhất.

**Module 06: Quản lý Ca làm việc & Phân ca**

- Thư viện Ca: Cấu hình Ca Sáng, Ca Chiều, Ca Đêm (Bắt đầu T -> Kết thúc T+1).
- Import Phân ca: HR Import file Excel gán ca cho từng NV theo ngày trong tuần/tháng.

**Module 07: Cấu hình Lịch & Ngày nghỉ đặc biệt**

- Lịch Lễ: Tính công mặc định (Hợp lệ) cho toàn bộ NV vào các ngày lễ quốc gia.
- Chế độ đặc biệt: Đưa ra quy tắc cho phép đăng ký WFH (Làm việc tại nhà), Đi công tác, Nghỉ sinh nhật (được hưởng lương).

**Module 8: Quản lý & Cấu hình Camera AI**

- 
Định danh thiết bị: Mỗi Camera gắn với một Location ID (Văn phòng, Cổng ra vào, Tầng). Khi camera quét mặt, dữ liệu gửi về server sẽ kèm theo ID này để xác định vị trí chấm công trong Nhật ký (Module 01).

- 
Xử lý trùng lặp (De-duplication): Nếu một nhân viên đứng trong vùng quét và bị Camera ghi nhận nhiều lần trong 1 khoảng thời gian ngắn (ví dụ < 30 giây), hệ thống chỉ lấy mốc thời gian sớm nhất để đẩy lên App.

- 
Health Check: Hệ thống tự động kiểm tra tín hiệu (Heartbeat) của camera mỗi 5 phút. Nếu mất tín hiệu, gửi cảnh báo ngay cho bộ phận IT/Admin.

**Module 09: Cấu hình Thông báo**

- 
Kênh thông báo (Channels): Hỗ trợ đa kênh gồm App Push Notification (ưu tiên), Email (cho các đơn từ cần lưu trữ) và Popup Dashboard.

- 
Điều kiện kích hoạt (Triggers):
    - 
Sự kiện chấm công: Thông báo thành công ngay khi Camera nhận diện xong (< 60s).

    - 
Sự kiện đơn từ: Trạng thái đơn thay đổi (Chờ duyệt -> Đã duyệt/Từ chối).

    - 
Sự kiện định kỳ: Nhắc nhở chấm công đầu/cuối ca hoặc thông báo lịch nghỉ lễ/tết diện rộng.

- 
Ràng buộc: Cho phép nhân viên tắt/mở thông báo nhắc nhở cá nhân, nhưng không được tắt các thông báo quan trọng liên quan đến kết quả phê duyệt đơn từ và kỷ luật lao động.

**Module 10: Trung tâm Phê duyệt**

- Luồng Duyệt: Manager Duyệt đơn của NV thuộc team ➔ HR Duyệt cuối hoặc Duyệt đơn nhạy cảm (Giải trình/Hủy công).
- Phản hồi: Lưu trữ lý do từ chối (Rejection Reason) gửi về App cho nhân viên.

**Module 11: Báo cáo tổng & Xuất dữ liệu**

- Manager Dashboard: Biểu đồ tỷ lệ chuyên cần theo phòng ban; Danh sách NV đi muộn/về sớm nhiều nhất.
- Excel Export: Xuất bảng công tổng hợp (Attendance Report) có cấu trúc phù hợp để tính lương.

### **3. USE CASE DIAGRAM**

**
bottomChấm công C Vision.pngpVZbb5swFP411raHRASSEh65pO2kttt6015dQsAqGAZO1fz7+djYsRNSolaKHNvY33fux2judAy3bFuVyEmQEzLCygy5zlMHY4zFX0Jw3uKKzyawOXkmHakpn4aMZXSNaQqnbgklsNc0EqrMNoyvWc2HluQFLNakzVIGl8UROeKU1S3/iFz3rkCxh0IXwN+ImId87vIl7vjwwPBmc3TrzxatZigKUejBxRLuRYn4dsnH63sDIVxXhB4hXAuACC19kLjoV8GM5pbCezl2MCIvhp9YsqwSOyv4Gco1OH3FeSZpVlVT1rsMVg9Z+0bSDGC+S60jDxDunn9IHuRHPQ5c7X/bLkulT/ihv4KStUp5KS2TJpwRcegCIAt1IgEfvCrzaG2e4tl5VKQHii7BziiecxMpWwXK8qFTSe8pk6Y21XSMTOAK9KUnVNISO3e58s0S+Bqpa9BoX8u7oHu11ZJRSwD38/T9px53ATQp1ty/Hm2eUUWveqQwAaSc6Cgm0q+gW0wLYBEizIU4peL3icXnneXDFxkdtQK1pnxG9xloYM97bD85GdsysVTMQc45t5jyz1VG2WGU/xvM2LMj/2TCG9I7XW+naKal+lk1dQvCrN7TrLQ0XIz5SlajWSWQxRSAin2YU1HfrOV9hssJI1VmU40GRqzUW2yBwwiEGGtlfhu6QhQaDBej+CJPiZ3EPK990OlG6RClQEntnOv9W5dkjaEKGrT+WRGY4K54qXG7ts0HmnbarwvROnSmQeAbRMsxIhtnQ0RPe9kHTX6QU8fxsBx1Um9/OLDe7rQebF8nuB94UTYUCSNdLK5OZ7shRTCYd98gt3SPIiKfMBWRYrSxVJH6EDPDnVXAyabKm/sEGb3gcHc6vO8O75447Q3uzr+q3AftW/KJdq31gz4t/eoaFZ27ItiBMxU0uKm0AtQdgINsNgB16iaNrEdm6/2gV7tftgGvuJcnCqMAVQVayT28qxx3sH8xuOsP7i6Hd08gB4eK3+zffbz1qgcHmC8n2jUY6aaVwlQZJgxgSXX3FqhA4jrTKTzNZMyaESAece+6FRtmk4855ZpDFO+TKEsRMHuc2TGOXfi010Ov+TA+baZ+nDv8ib6t5Oo/fittrue1
**
