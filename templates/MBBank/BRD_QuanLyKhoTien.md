Gán vai trò – phân quyền - Ủy quyền: Hệ thống Quản lý Kho tiền tập trung
================================================================
* Áp dụng từ 06 Nov 2025
* Các mục có dấu \* là bắt buộc

****TÀI LIỆU ĐẶC TẢ PHÂN TÍCH YÊU CẦU NGƯỜI DÙNG (BRD)****
----------------------------------------------------

****I. THÔNG TIN YÊU CẦU****
----------------------------

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Tên yêu cầu \*** | **Hệ thống Quản lý Kho tiền tập trung (Camera AI & Smart Management)** | | | | | |
| **Loại yêu cầu \*** | * Yêu cầu **PHÁT TRIỂN MỚI** tính năng/sản phẩm | | **Đề xuất ngày hoàn thành \*** | 06 Dec 2025 | | |
| **Độ ưu tiên \*** | * CAO | * TRUNG BÌNH | * THẤP |
| **Cán bộ soạn thảo - Phòng thuộc Đơn vị yêu cầu** | | | **Cán bộ soạn thảo - Phòng thuộc CNTT** | | | |
| **Người yêu cầu \*** | Họ tên & Chức danh | Ngô Tiến Dũng | **Business Analysis (BA) \*** | Nguyễn Hữu Hồng Sơn | Phòng BA TTTM&SQ | |
| Email & Điện thoại | dungnt.sgd@mbbank.com.vn | | **SA/DEV Lead** | | | |
| **Phòng/TT/Khối \*** | SME.TRADE FINANCE | | **Designer** | | | |

****II. MỤC TIÊU THỰC HIỆN VÀ ĐO LƯỜNG****
------------------------------------------

### 2.1. ****Mục tiêu thực hiện (CARD) \*****

**(1) Hiện trạng:**
*   Quản lý thủ công: Việc giám sát vào/ra kho tiền tại CN/PGD dựa hoàn toàn vào con người và sổ sách ghi chép.
*   Rủi ro vận hành: Khó kiểm soát việc tuân thủ quy tắc "tam tắc" (3 chìa khóa) và quy định người lạ vào kho.
*   Quy trình ủy quyền rời rạc: Thực hiện qua giấy tờ, khó tra cứu lịch sử và xác định trách nhiệm tức thời.

**(2) Vướng mắc/bất cập:**
*   Không có cảnh báo tức thời khi xảy ra vi phạm (VD: vào sai giờ, thiếu người quản lý).
*   Khó khăn trong việc hậu kiểm, trích xuất dữ liệu camera khi có sự cố.
*   Phụ thuộc vào ý thức tuân thủ của nhân sự tại chỗ.

**(3) Mong muốn (Giải pháp đề xuất):**
*   **Số hóa toàn trình:** Quản lý User, Phân quyền, Uy quyền trên hệ thống phần mềm tập trung.
*   **Giám sát thông minh:** Sử dụng Camera AI nhận diện khuôn mặt để tự động điểm danh, kiểm soát số lượng và danh tính người trong kho.
*   **Cảnh báo thời gian thực:** Phát hiện và gửi cảnh báo ngay lập tức các hành vi vi phạm (người lạ, sai giờ, sai quy trình bàn giao).
*   **Quy trình Bàn giao chặt chẽ:** Hỗ trợ quy trình bàn giao có sự hiện diện của cả bên giao và bên nhận mà không báo lỗi vi phạm, đảm bảo tính liên tục của an ninh.

### ****2.2. Tiêu chí đo lường về hiệu quả kinh doanh/nghiệp vụ \*****

| STT | Tiêu chí đo lường | Cách thức đo lường | Thời gian đo | Kết quả đăng ký |
| --- | --- | --- | --- | --- |
| 1 | Mức độ tuân thủ an toàn kho quỹ | Số lượng vi phạm được phát hiện và xử lý / Tổng số phiên vào kho | Hàng tháng | 100% |
| 2 | Thời gian truy vết sự cố | Thời gian trung bình để trích xuất video/nhật ký của 1 phiên giao dịch | Khi có yêu cầu | < 5 phút |
| 3 | Hiệu quả vận hành | Giảm thời gian làm thủ tục giấy tờ cho việc ủy quyền/bàn giao | Đánh giá định kỳ | Giảm 50% |

****III. XÁC ĐỊNH VẤN ĐỀ****
--------------------

### 3.1. Phân tích bài toán Bàn giao (Deep Dive)

Một trong những vấn đề phức tạp nhất là xử lý tình huống "Bàn giao" (Handover) nhiệm vụ quản lý kho giữa hai nhân sự. 
*   **Thực tế:** Cần có khoảng thời gian *giao thoa* (Overlap) khi cả Người giao (Giver) và Người nhận (Receiver) cùng ở trong kho để kiểm đếm, bàn giao chìa khóa.
*   **Xung đột hệ thống cũ:** Hệ thống giám sát thông thường sẽ báo lỗi "Dư người" hoặc "Người lạ" (nếu Giver đã hết ca).
*   **Giải pháp nâng cao:** Hệ thống cần trạng thái "Phiên bàn giao" đặc biệt, cho phép sự hiện diện hợp lệ của cả hai bên trong một khoảng thời gian giới hạn (Timeout), với sự chuyển giao trách nhiệm rõ ràng.

****IV. MÔ TẢ YÊU CẦU CHI TIẾT****
----------------------------------

### ****4.1. Quy tắc chung (General Rules)****

| Mã quy tắc | Tên quy tắc | Mô tả chi tiết |
| --- | --- | --- |
| **BR-GEN-01** | **Nguyên tắc Tam tắc** | Mọi phiên làm việc trong kho phải đảm bảo tối thiểu 3 bộ phận quản lý (Quản lý 1, 2, 3) hiện diện cùng lúc khi mở/đóng kho. |
| **BR-GEN-02** | **Định danh duy nhất** | Mỗi cá nhân ra vào kho phải được định danh duy nhất (FaceID + Mã nhân viên). Không chấp nhận "khách" không định danh trong kho tiền. |
| **BR-GEN-03** | **Phiên làm việc** | Một "Phiên" bắt đầu khi người đầu tiên check-in và kết thúc khi người cuối cùng check-out. |

### ****4.2. Tính năng Quản lý User & Phân quyền (US1 & US2)****

**Mục đích:** Thiết lập danh sách "White-list" những người được phép vào kho tại từng thời điểm.

**Quy tắc nghiệp vụ:**
1.  **Phân loại User:**
    *   *Nhân sự MB:* Đồng bộ từ HRMS.
    *   *Khách/Đối tác:* Đăng ký thủ công, duyệt 2 cấp (Inputter/Authoriser), có thời hạn hiệu lực cụ thể.
2.  **Gán Role Quản lý:**
    *   Hệ thống cho phép gán User vào các Slot quản lý (QL1, QL2, QL3).
    *   Kiểm tra chéo chức danh (VD: Giám đốc không thể giữ chìa của Thủ quỹ).

**Quy trình:**
*   Inputter chọn User -> Gán Role/Thời gian cho phép -> Gửi duyệt -> Authoriser phê duyệt -> Kích hoạt quyền vào kho.

### ****4.3. Tính năng Ủy quyền & Bàn giao (US3 - Enhanced)****

**Mục đích:** Quản lý việc chuyển giao quyền hạn, đảm bảo luôn xác định được *ai là người chịu trách nhiệm chính* tại mọi thời điểm.

**Quy tắc Bàn giao (Handover Rules) - QUAN TRỌNG:**

*   **Rule 1 (Trạng thái Bàn giao):** Hệ thống ghi nhận trạng thái "Bàn giao" (Handover Mode) khi có yêu cầu chuyển giao quyền lực từ User A (Giver) sang User B (Receiver).
*   **Rule 2 (Quyền hiện diện):** Trong trạng thái Bàn giao, User A (Giver) vẫn được coi là hợp lệ trong kho, dù ca làm việc có thể đã kết thúc, cho đến khi hoàn tất bàn giao.
*   **Rule 3 (Chuyển giao trách nhiệm):**
    *   Ngay khi User B (Receiver) check-in và xác nhận "Nhận bàn giao", User B trở thành **Quản lý chính** (Main Manager) trên hệ thống.
    *   User A (Giver) trở thành "Nhân sự hỗ trợ/bàn giao".
*   **Rule 4 (Giới hạn thời gian - Timeout):**
    *   Hệ thống quy định "Thời gian bàn giao tối đa" (Configurable, VD: 30 phút).
    *   Nếu quá thời gian này mà User A chưa check-out, hệ thống sẽ phát cảnh báo "Quá giờ bàn giao".

**Kịch bản Bàn giao (Happy Path):**
1.  **Giver** đang trong kho.
2.  **Receiver** đến, check-in FaceID.
3.  Hệ thống hỏi Receiver: "Bạn vào để nhận bàn giao?". Receiver xác nhận "Có".
4.  Hệ thống kích hoạt **Handover Mode**. (Cho phép hiện diện cả Giver và Receiver).
5.  Hai bên thực hiện kiểm đếm/bàn giao.
6.  **Giver** check-out rời khỏi kho.
7.  Hệ thống kết thúc **Handover Mode**.

### ****4.4. Tính năng Cảnh báo & Giám sát (US4 - Deep Analysis)****

**Mục đích:** Phát hiện các bất thường dựa trên dữ liệu AI và Quy tắc nghiệp vụ.

**Ma trận vi phạm (Violation Matrix):**

| Tình huống | Điều kiện Logic | Kết luận | Hành động |
| --- | --- | --- | --- |
| **Người lạ** | Có mặt người không thuộc White-list | **VI PHẠM** | Báo động ngay lập tức |
| **Dư người** | Số người thực tế > 3 (và KHÔNG trong Handover Mode) | **VI PHẠM** | Cảnh báo |
| **Bàn giao hợp lệ** | Số người thực tế = 4 (3 QL + 1 Giver) VÀ (Trong Handover Mode) VÀ (Thời gian < Timeout) | **HỢP LỆ** | Ghi log "Bàn giao" |
| **Quá giờ bàn giao** | Số người thực tế = 4 VÀ (Trong Handover Mode) VÀ (Thời gian > Timeout) | **VI PHẠM** | Cảnh báo "Quá giờ bàn giao" |
| **Thiếu tam tắc** | Số lượng Role quản lý < 3 | **VI PHẠM** | Cảnh báo |

**Cơ chế gửi cảnh báo:**
*   Notification tới App của Giám đốc/Kiểm soát viên.
*   Email tới Hộp thư chung của Phòng An ninh/Vận hành.
*   Loa cảnh báo tại chỗ (nếu tích hợp).

### ****4.5. Tính năng Báo cáo (US5)****

*   **Báo cáo Bàn giao:** Liệt kê các phiên bàn giao, thời gian overlap, người giao/nhận.
*   **Nhật ký Vi phạm:** Chi tiết từng vi phạm, kèm link/snapshot video tại thời điểm đó.

****V. NỘI DUNG KHÁC****
------------------------
(Để trống - bổ sung theo yêu cầu cụ thể của đơn vị)

****VI. YÊU CẦU PHI CHỨC NĂNG****
---------------------------------

### 6.1. Hiệu năng & Độ trễ
*   Độ trễ nhận diện khuôn mặt: < 1 giây.
*   Độ trễ xử lý logic cảnh báo: < 3 giây (từ lúc AI nhận diện đến khi bắn cảnh báo).

### 6.2. Bảo mật
*   Dữ liệu khuôn mặt phải được mã hóa (Vector hóa), không lưu ảnh thô nếu không cần thiết.
*   Logs hệ thống là bất biến (Immutable), không cho phép sửa xóa lịch sử ra vào.

### 6.3. Khả dụng
*   Hệ thống hoạt động 24/7.
*   Có cơ chế Offline Mode: Camera vẫn ghi hình và AI Box vẫn xử lý tại biên (Edge) khi mất kết nối Internet, đồng bộ dữ liệu khi có mạng lại.
