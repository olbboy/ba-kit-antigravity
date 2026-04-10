# US-REG-01: Đăng ký nghỉ phép

---

**AS A** Nhân viên,  
**I WANT TO** tạo đơn xin nghỉ phép trực tiếp trên Mini App với đầy đủ loại phép và kiểm tra hạn mức tự động,  
**SO THAT** tôi không cần gửi đơn giấy hoặc email, đồng thời biết ngay số ngày phép còn lại để chủ động sắp xếp.

---

### **1. BUSINESS FLOW**

1. **Khởi tạo:** NV nhấn "Đăng ký nghỉ phép" tại Trung tâm đăng ký.
2. **Chọn loại phép:** Hệ thống hiển thị 8 loại: Phép năm, Ốm, Thai sản, Cha, Kết hôn, Tang, Không lương, Bù.
3. **Nhập thông tin:** Chọn ngày bắt đầu/kết thúc, nửa ngày (AM/PM nếu nghỉ nửa buổi), lý do, đính kèm file (nếu bắt buộc).
4. **Validate:**
   - Hệ thống tính số ngày làm việc thực tế (trừ T7/CN và ngày lễ).
   - Kiểm tra số dư phép (pessimistic lock tránh race condition).
   - Kiểm tra trùng ngày nghỉ (DB exclusion constraint).
   - Kiểm tra báo trước (VD: Phép năm cần báo trước 3 ngày).
5. **Gửi đơn:** Tạo LeaveRequest (status: PENDING), cập nhật balance.pending += workingDays.
6. **Phê duyệt:** Đơn được chuyển vào Trung tâm phê duyệt (Module 10).

---

### **2. ACCESS CONTROL (RBAC/ABAC)**

| Thông tin (Data Field) | Role (Access Right) | Ghi chú |
| --- | --- | --- |
| Form đăng ký nghỉ phép | Nhân viên, HR, Quản lý | Mọi role đều có thể tạo đơn cho chính mình. |
| Hạn mức phép còn lại | Nhân viên | ABAC: Chỉ xem hạn mức của chính mình. |
| Tạo đơn cho NV khác | HR Admin | HR có thể tạo đơn thay cho NV (trường hợp đặc biệt). |

---

### **3. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA)**

#### **AC1. Hiển thị hạn mức phép**

- Trước khi nhập form, hiển thị tóm tắt: Phép năm (Đã dùng / Tổng), Phép chuyển tiếp (Carryover), Ngày hết hạn carryover.
- Công thức phép năm: 12 ngày cơ bản + 1 ngày / 5 năm thâm niên.
- NV mới (< 12 tháng): Phép = (entitlement × số_tháng_làm) / 12.

#### **AC2. Chọn loại phép & Validation**

- Mỗi loại phép hiển thị: tên, hạn mức, yêu cầu đính kèm (Có/Không), thời hạn báo trước.
- **Đính kèm bắt buộc:** Ốm (giấy khám), Thai sản (giấy chứng nhận), Cha (giấy khai sinh).
- **File:** Hỗ trợ .jpg, .png, .pdf; tối đa 5MB/file.
- **Trùng ngày:** Nếu đã có đơn nghỉ (PENDING hoặc APPROVED) trùng ngày → Hiển thị lỗi cụ thể.

#### **AC3. Tính số ngày nghỉ thực tế**

- Hệ thống tự động trừ T7/CN và ngày lễ (từ Module 07) khỏi khoảng ngày chọn.
- Hỗ trợ nghỉ nửa ngày (0.5): chọn AM hoặc PM.
- Hiển thị: "Bạn sẽ nghỉ X ngày làm việc (từ dd/MM đến dd/MM)".

#### **AC4. Xác nhận & Gửi đơn**

- Màn hình xác nhận hiển thị tóm tắt: Loại phép, khoảng ngày, số ngày, phép còn lại sau khi trừ.
- Sau khi gửi → Hiển thị thông báo "Đơn đã gửi thành công" kèm mã đơn.
- Hạn mức phép hiển thị cập nhật ngay (pending balance).

---

### **4. DEFINITION OF DONE (DOD)**

1. **Race condition:** Kiểm thử 2 request đồng thời cho cùng NV → Chỉ 1 request thành công (pessimistic lock).
2. **Exclusion constraint:** Tạo đơn trùng ngày → DB reject (PostgreSQL exclusion constraint với GiST index).
3. **Giao diện:** Form responsive, hiển thị tốt trên mobile và web.
4. **QA:** Kiểm thử tất cả 8 loại phép với các case: đủ phép, hết phép, carryover, nửa ngày.
