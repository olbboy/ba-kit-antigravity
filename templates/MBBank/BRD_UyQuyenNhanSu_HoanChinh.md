# TÀI LIỆU ĐẶC TẢ YÊU CẦU NGƯỜI DÙNG (BRD)
# DỰ ÁN: QUẢN LÝ KHO TIỀN (SME.TRADE FINANCE)
## Tên yêu cầu: Gán vai trò – Phân quyền – Ủy quyền nhân sự ra vào kho

---

## I. THÔNG TIN YÊU CẦU

| Mục | Nội dung |
| --- | --- |
| **Tên yêu cầu** | Gán Role, Phân quyền và Ủy quyền nhân sự ra vào kho tiền |
| **Loại yêu cầu** | Phát triển mới |
| **Độ ưu tiên** | CAO |
| **Đơn vị yêu cầu** | Phòng BA TTTM&SQ |
| **Người yêu cầu** | Ngô Tiến Dũng |
| **Ngày đề xuất** | 06/11/2025 |
| **Ngày hoàn thành** | 09/08/2024 (Theo US gốc) |

---

## II. MỤC TIÊU THỰC HIỆN VÀ ĐO LƯỜNG

### 2.1. Mục tiêu kinh doanh
*   **Số hóa quy trình:** Chuyển đổi quy trình gán quyền, ủy quyền ra vào kho tiền từ thủ công sang tự động hóa trên hệ thống.
*   **Tăng cường kiểm soát:** Đảm bảo tuân thủ chặt chẽ các quy định về an toàn kho quỹ (Rule 3 quản lý, Rule ủy quyền).
*   **Linh hoạt vận hành:** Hỗ trợ cơ chế ủy quyền linh hoạt khi nhân sự vắng mặt, đảm bảo hoạt động kho quỹ không bị gián đoạn.

### 2.2. Tiêu chí đo lường
| STT | Tiêu chí | Công thức/Cách đo | Kỳ vọng |
| --- | --- | --- | --- |
| 1 | Thời gian xử lý yêu cầu ủy quyền | Thời gian từ lúc tạo request đến lúc duyệt xong | < 30 phút |
| 2 | Tỷ lệ tuân thủ quy trình | % giao dịch có đủ phê duyệt đúng role | 100% |

---

## III. PHẠM VI VÀ QUY ĐỊNH NGHIỆP VỤ

### 3.1. Bảng quy định chức danh (Role Matrix)

Hệ thống phải tuân thủ nghiêm ngặt bảng phân vai sau cho 3 vị trí quản lý kho:

| Vị trí | Tại Chi Nhánh (CN) | Tại PGD |
| --- | --- | --- |
| **Quản lý 1** | Giám đốc CN, Phó GĐ CN | Giám đốc PGD, Phó GĐ PGD |
| **Quản lý 2** | Giám đốc DV, Trưởng/Phó phòng DVKH, KSV | Trưởng/Phó phòng DVKH, KSV (hoặc nhân sự CN hỗ trợ) |
| **Quản lý 3** | Trưởng Quỹ, Thủ kho, Kiểm ngân, GDV | Thủ kho, Kiểm ngân, GDV |

### 3.2. Quy tắc nghiệp vụ (Business Rules)
*   **Rule 1 (Phê duyệt MO):** Mọi thao tác gán quyền, ủy quyền đều phải sinh bản ghi trình ký lên hệ thống MO (Middle Office).
*   **Rule 2 (Phân quyền):** User gốc của Role Quản lý 1 luôn có quyền vào kho.
*   **Rule 3 (Độ ưu tiên ủy quyền):** Nếu một Role được ủy quyền cho nhiều người, hệ thống ưu tiên theo "Độ ưu tiên" (Priority) hoặc "Thời gian ủy quyền mới nhất".
*   **Rule 4 (Bàn giao):** Khi người được ủy quyền (A) bận và bàn giao lại cho người khác (B), thì B sẽ có quyền, A tạm mất quyền trong thời gian bàn giao (tùy cấu hình scenario).

---

## IV. MÔ TẢ YÊU CẦU CHI TIẾT

### 4.1. Tính năng 1: Gán Role Quản Lý Kho (US2)
**Mô tả:** Cho phép Inputter tại CN/PGD thiết lập 3 nhân sự chịu trách nhiệm quản lý kho (Quản lý 1, 2, 3).

**Luồng nghiệp vụ:**
1.  **Inputter** chọn nhân sự cho 3 vị trí từ danh sách user hệ thống.
2.  **Hệ thống** validate chức danh user dựa trên *Bảng quy định chức danh* (Mục 3.1).
    *   *Hợp lệ:* Cho phép gửi duyệt.
    *   *Không hợp lệ:* Cảnh báo, nhưng vẫn cho phép gửi (với luồng duyệt ngoại lệ - Exception Flow).
3.  **Inputter** gửi yêu cầu. Hệ thống tạo bản ghi trên MO.
4.  **Cấp phê duyệt (CPD)** trên MO xem xét.
    *   Nếu đúng quy định: Duyệt -> Áp dụng ngay.
    *   Nếu sai quy định (Ngoại lệ): Duyệt -> Hệ thống gửi email cho HO (Hội sở) để tái thẩm định.
5.  **HO** phản hồi qua Email (Duyệt/Từ chối). Hệ thống cập nhật trạng thái cuối cùng.

### 4.2. Tính năng 2: Phân quyền Vào Kho (US2)
**Mô tả:** Cấp quyền ra/vào kho cho các nhân sự vận hành khác (ngoài 3 quản lý).

**Luồng nghiệp vụ:**
1.  **Inputter** chọn danh sách User cần vào kho.
2.  **Inputter** thiết lập thời gian hiệu lực (Thời gian ra/vào).
3.  **Inputter** chọn CPD trên MO.
4.  Gửi duyệt -> MO phê duyệt -> Hệ thống cập nhật quyền.

### 4.3. Tính năng 3: Ủy Quyền (US3)
**Mô tả:** Cho phép quản lý ủy quyền vai trò của mình cho người khác khi vắng mặt.

**Luồng nghiệp vụ:**
1.  **Inputter** chọn Role cần ủy quyền (VD: Quản lý 1).
2.  Click icon "Ủy quyền".
3.  Chọn danh sách người nhận ủy quyền (người thay thế).
    *   Thiết lập **Thứ tự ưu tiên** (1, 2, 3...).
    *   Thiết lập **Thời gian ủy quyền**.
4.  Chọn CPD trên MO.
5.  Hệ thống sinh biểu mẫu trình ký tương ứng:
    *   *Quản lý 1/2:* Mẫu Giấy ủy quyền TV quản lý kho.
    *   *Quản lý 3:* Mẫu Giấy đề nghị cử người thay thế.
6.  Gửi duyệt -> MO phê duyệt -> Hệ thống cập nhật quyền cho người được ủy quyền theo quy tắc ưu tiên.

---

## V. YÊU CẦU PHI CHỨC NĂNG (NFR)

### 5.1. Bảo mật & An toàn dữ liệu
*   **Mã hóa:** Dữ liệu nhạy cảm (thông tin cá nhân, chức danh) phải được mã hóa khi truyền tải và lưu trữ (tuân thủ Nghị định 13/2023).
*   **Phân quyền:** Chỉ user có role `Inputter_Kho` mới được tạo yêu cầu. Chỉ user có role `Approver_MO` mới được phê duyệt.

### 5.2. Audit Log (Lưu vết)
*   Hệ thống phải ghi log toàn bộ thao tác: Người tạo, Người duyệt, Thời gian, Nội dung thay đổi (Before/After).
*   Log phải được lưu trữ tối thiểu 10 năm theo quy định an toàn kho quỹ.

### 5.3. Hiệu năng
*   Hệ thống phải xử lý đồng thời tối thiểu **200 CCU** (Concurrent Users) trong giờ cao điểm sáng/chiều (giờ mở/đóng kho).
*   Thời gian phản hồi thao tác < 2 giây.

---

## VI. TÀI LIỆU THAM CHIẾU
*   [QCĐH.B4.TT.MB.01] Mẫu QĐ giao nhiệm vụ TV quản lý kho.
*   [QCĐH.B4.TT.MB.02] Mẫu Giấy ủy quyền TV quản lý kho.
*   [QCĐH.B4.TT.MB.04] Mẫu Biên bản bàn giao công tác kho quỹ.

---
**Trạng thái tài liệu:** DRAFT
**Người soạn thảo:** AI Agent (Antigravity)
