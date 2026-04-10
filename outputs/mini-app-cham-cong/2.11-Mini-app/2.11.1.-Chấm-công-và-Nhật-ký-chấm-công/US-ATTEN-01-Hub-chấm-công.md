# US-ATTEN-01: Hub chấm công

---

**AS A** Nhân viên,  
**I WANT TO** xem trạng thái chấm công, mốc giờ In/Out và thanh tiến độ thực tế ngay tại cụm trung tâm Trang chủ,  
**SO THAT** tôi có thể xác định ngay lập tức tình trạng công của mình và chủ động điều phối thời gian làm việc để hoàn thành ca làm.

---

### **1. BUSINESS FLOW**

1. **Hành động**: Nhân viên quét khuôn mặt thành công tại Camera AI C-Vision.
2. **Xử lý hệ thống**: Camera gửi mốc thời gian về hệ thống ➔ hệ thống đối soát lịch phân ca ➔ Lưu mốc giờ vào Database.
3. **Cập nhật giao diện**: Backend đẩy dữ liệu Real-time ➔ Mini App cập nhật lại các trường thông tin trong Hub Chấm công ngay lập tức.
4. **Kiểm tra**: Nhân viên mở App và thấy các mốc giờ, Badge và thanh tiến độ đã thay đổi.

---

### **2. ACCESS CONTROL (RBAC/ABAC)**

| Thông tin (Data Field) | Role (Access Right) | Ghi chú |
| --- | --- | --- |
| Trạng thái của NV hiện tại | Nhân viên, HR, Quản lý | ABAC: NV chỉ xem được của chính mình. |
| Mốc giờ In/Out cá nhân | Nhân viên, HR, Quản lý | ABAC: Lọc theo User_ID đang đăng nhập App. |
| Thời gian cập nhật | Toàn bộ các Role | Hiển thị mốc đồng bộ từ Device Camera AI. |

---

### **3. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA)**

#### **3.1. Hiển thị Badge Trạng thái & Mốc giờ (In/Out)**

- Trạng thái 1 (Chưa chấm công): Khi hệ thống chưa nhận bất kỳ mốc quẹt nào trong ngày ➔ Badge hiển thị CHƯA CHẤM CÔNG (Xám), Giờ Vào/Ra hiển thị --:--.
- Trạng thái 2 (Đã chấm công): Khi hệ thống ghi nhận ít nhất 01 mốc quẹt thành công ➔ Badge hiển thị ĐÃ CHẤM CÔNG (Xanh lá).
- Logic gán mốc giờ:    - Giờ Vào: Là mốc quẹt khuôn mặt Sớm nhất ghi nhận được trong ca làm việc.
    - Giờ Ra: Là mốc quẹt khuôn mặt Mới nhất/Muộn nhất ghi nhận được sau mốc Giờ Vào.
    - Logic Ca Đêm (VD: 20h - 06h):        - Mốc quẹt từ 20:00 (Ngày T) đến 06:00 (Ngày T+1) được gán vào Nhật ký của Ngày T.
        - Thanh tiến độ tiếp tục chạy xuyên đêm (không bị reset tại mốc 24:00).
- **Grace Period (Thời gian ân hạn):**    - Hệ thống cho phép nhân viên đến muộn tối đa **15 phút** (giá trị mặc định, cấu hình được bởi HR tại Module Ca làm việc) mà không bị tính là "Đi muộn".
    - Công thức: Đi muộn (phút) = MAX(0, Giờ Vào thực tế - Giờ bắt đầu ca - Grace Period).
    - VD: Ca 08:00, Grace = 15 phút → Quẹt lúc 08:12 = Đúng giờ; Quẹt lúc 08:20 = Trễ 5 phút.
    - *(Tham chiếu: EAMS v2.0 §4.2 `gracePeriodMinutes`)*

#### **3.2. Logic Thanh Tiến độ**

- **Công thức tính phần số:** Tổng thời gian = [Current_Time] - [Check_In_Time] (Trừ đi thời gian nghỉ trưa do HR đã set up ở module Shift).
- **Công thức tính phần thanh (%)**: Progress (%) = (Tổng thời gian / Tổng giờ làm theo quy định) * 100.
- **Giới hạn hiển thị:**    - Nếu chưa có Giờ Vào ➔ Thanh tiến độ ở mức 0% và hiển thị 00h 00m / Tổng giờ làm theo quy định
    - Nếu làm việc quá 8 tiếng (OT) ➔ Thanh sẽ đầy 100% nhưng mốc thời gian thực hiện vẫn cộng dồn (VD: 09h 15m / 08h 00m).

- **Trường hợp đặc biệt:** Nếu Current_Time nằm ngoài ca làm việc hoặc NV đang trong đơn nghỉ được duyệt ➔ Vẫn giữ mốc thời gian tại lần quẹt cuối cùng.

#### **3.3. Hiển thị mốc "Cập nhật lúc"**

- Hiển thị đúng mốc thời gian hệ thống Backend nhận dữ liệu từ Camera AI.
- **Ví dụ:** Nếu NV quẹt lúc 12:35 và Backend đồng bộ lúc 12:37 ➔ App hiển thị "* Cập nhật lúc 12:37 PM".

---

### **4. DEFINITION OF DONE (DOD)**

1. **Phần quyền**: Phân quyền RBAC (NV xem của mình) và ABAC (Lọc theo Team_ID đối với Manager) được áp dụng đúng.
2. **Độ chính xác**: Tất cả field hiển thị đúng dữ liệu thực từ Camera AI. Sai số ±1 phút do độ trễ mạng.
3. **Kiểm thử**: Logic thanh tiến độ được Unit Test với các case: Bình thường, Đi muộn, Về sớm, Tăng ca xuyên đêm.
4. **Báo cáo**: QA xác nhận đầy đủ test case pass (> 90%).
5. **Giao diện**: Responsive đúng Figma, không vỡ layout
