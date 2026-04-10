# US-SHIFT-04: Cấu hình giờ nghỉ

---

**AS A** HR,  
**I WANT TO** thiết lập khung giờ nghỉ (Bắt đầu nghỉ - Kết thúc nghỉ) cho từng ca làm việc,  
**SO THAT** hệ thống có thể tự động trừ đi thời gian này khi tính toán "Tổng giờ làm việc thực tế" của nhân viên, giúp bảng công chính xác và minh bạch.

---

### **1. BUSINESS FLOW**

1. Hành động: Tại màn hình Cấu hình ca, HR điền mốc giờ Bắt đầu nghỉ và Kết thúc nghỉ.
2. Tính toán thời gian nghỉ: Hệ thống tự động tính ra số phút nghỉ (vd: 12:00 - 13:30 = 90 phút).
3. Áp dụng: Khi nhân viên hoàn thành ca làm, hệ thống tự động trừ đi số phút nghỉ này khỏi tổng thời gian từ mốc Check-in đến Check-out.

---

### **2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA)**

#### **AC1. Cấu hình mốc giờ Nghỉ**

- Trường dữ liệu: Bắt đầu nghỉ (Start_Break), Kết thúc nghỉ (End_Break).
- Ràng buộc thời gian:    - Start_Break và End_Break phải nằm trong khung giờ làm việc chính thức của ca.
    - Không cho phép End_Break nhỏ hơn Start_Break (ngoại trừ ca đêm đặc biệt).

- Hiển thị: Tóm tắt "Mandatory Break" (vd: 60 Minutes) phải hiển thị ngay trên Thẻ ca ở cột bên trái.

#### **AC2. Logic tính toán Giờ làm thực tế (Work Hours Calculation)**

- Công thức: Tổng giờ làm = (Check_out - Check_in) - (End_Break - Start_Break).

---

### **3. DEFINITION OF DONE (DOD)**

1. **Dữ liệu chính xác**: Kiểm thử với ca hành chính (8h-17h30, nghỉ 1h30m) ➔ Tổng công hiển thị đúng giờ làm.
2. **Thông báo**: Nếu HR thiết lập giờ nghỉ chồng chéo hoặc sai lệch, hệ thống phải báo lỗi ngay khi lưu.
