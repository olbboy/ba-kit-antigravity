# US-SHIFT-03: Giới hạn thời gian chấm công (punch limit)

---

**AS A** HR,  
**I WANT TO** giới hạn khung giờ cho phép Check-in sớm và Check-out muộn so với giờ ca chính thức,  
**SO THAT** hệ thống không ghi nhận dữ liệu "ngoại lai" (quẹt thẻ quá sớm hoặc quá muộn vô ích), giúp bảo vệ tính chính xác của dữ liệu báo cáo chuyên cần.

---

### **1. BUSINESS FLOW**

1. Thiết lập: HR nhập tham số số giờ giới hạn (vd: 3 giờ).
2. Giới hạn In: Hệ thống chỉ chấp nhận mốc quẹt nếu Check_in >= (Giờ Vào Ca - 3h).
3. Giới hạn Out: Hệ thống chỉ cập nhật mốc quẹt cuối cùng nếu Check_out <= (Giờ Tan Ca + 3h).

---

### **2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA)**

#### **AC1. Cấu hình Tham số Giới hạn**

- Tham số 1: "Cho phép Check-In sớm tối đa (giờ)".
- Tham số 2: "Cho phép Check-out muộn tối đa (giờ)".
- Kiểu dữ liệu: Số nguyên (vd: 2, 3, 5...).
- Check validate

#### **AC2. Logic xác thực mốc quẹt (Validation Logic)**

- **Trường hợp quẹt sớm quá mức**: NV quẹt lúc 04:00 AM cho ca làm 08:00 AM (Giới hạn là 3h) ➔ Backend bỏ qua mốc quẹt này, không hiển thị Badge "Đã chấm công".
- **Trường hợp làm thêm giờ (OT)**: Nếu ca làm việc kết thúc lúc 17:30 (Giới hạn ra 3h là đến 20:30), nhưng nhân viên có **Đơn OT** được duyệt đến 22:00 ➔ Hệ thống tự động mở khung giới hạn Check-out ra đến 22:30 để ghi nhận dữ liệu.

---

### **3. DEFINITION OF DONE (DOD)**

1. **Dữ liệu rác**: Kiểm thử với mốc quẹt nằm ngoài khung giới hạn ➔ Đảm bảo không làm sai lệch mốc giờ "Vào/Ra" trên Dashboard của nhân viên.
2. **Thông báo**: Khi NV quẹt ngoài khung, Camera vẫn báo thành công, nhưng App sẽ không hiển thị cập nhật trạng thái làm việc.
