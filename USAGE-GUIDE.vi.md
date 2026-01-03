# 📘 BA-Kit Antigravity Workflows - Hướng dẫn Sử dụng Toàn diện

<p align="center">
  <img src="assets/logo.png" alt="BA-Kit Logo" width="150">
</p>

<div align="center">

[**🇬🇧 English**](USAGE-GUIDE.md) | [**🇻🇳 Tiếng Việt**](USAGE-GUIDE.vi.md)

</div>

## 🧠 Triết lý & Hiểu biết Chuyên sâu

### Nguyên tắc Cốt lõi: Năng lực Phân lớp (Layered Competency)

BA-Kit được xây dựng trên một **mô hình năng lực phân lớp** nơi các kỹ năng xây dựng dựa trên nhau:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     KIM TỰ THÁP NĂNG LỰC BA-KIT                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│                           ┌───────────────┐                             │
│                           │   TEMPLATES   │  ← LỚP OUTPUT               │
│                           │   (09-12)     │    Sản phẩm đầu ra          │
│                           └───────┬───────┘                             │
│                                   │                                     │
│                    ┌──────────────┴──────────────┐                      │
│                    │      KỸ NĂNG CHUYÊN SÂU     │  ← LỚP NGỮ CẢNH      │
│                    │         (04-08)             │    Áp dụng khi cần   │
│                    └──────────────┬──────────────┘                      │
│                                   │                                     │
│         ┌─────────────────────────┴─────────────────────────┐          │
│         │              KỸ NĂNG CỐT LÕI (01-03)               │  ← LỚP   │
│         │   Identity → Elicitation → Writing Quality         │    NỀN   │
│         └───────────────────────────────────────────────────┘          │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

**Insight Quan trọng**: Bạn không thể sử dụng hiệu quả các kỹ năng chuyên sâu nếu không thiết lập các kỹ năng cốt lõi trước. Hãy nghĩ về nó như một ngôi nhà:
- **Móng** (SKILL-01 Identity): Bạn là AI, bạn tư duy NHƯ THẾ NÀO
- **Tường** (SKILL-02 Elicitation): CÁCH bạn thu thập thông tin
- **Mái** (SKILL-03 Writing): CÁCH bạn diễn đạt yêu cầu
- **Nội thất** (SKILL 04-08): Kỹ thuật CỤ THỂ nào bạn áp dụng
- **Đồ đạc** (SKILL 09-12): Tài liệu GÌ bạn tạo ra

---

## 🎯 Kịch bản Sử dụng & Cây Quyết định

### Kịch bản 1: Bắt đầu Dự án Mới từ Đầu

```
USER: "Tôi cần phân tích yêu cầu cho một ứng dụng ngân hàng di động mới"

ĐƯỜNG DẪN WORKFLOW:
┌─────────────────────────────────────────────────────────────────────────┐
│ Bước 1: /ba-identity                                                    │
│ ─────────────────────────────────────────────────────────────────────── │
│ • Kích hoạt BA Expert persona                                           │
│ • Lập bản đồ stakeholders (Lãnh đạo NH, Team Product, End users, IT)    │
│ • Xác định lưới quyền lực/lợi ích (power/interest grid)                 │
│ • Thiết lập phong cách giao tiếp cho từng loại stakeholder              │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Bước 2: /ba-elicitation                                                 │
│ ─────────────────────────────────────────────────────────────────────── │
│ • Bắt đầu với câu hỏi KHÁM PHÁ (EXPLORATORY):                           │
│   - "Mục tiêu kinh doanh chính của ứng dụng mobile banking?"            │
│   - "Ai là đối tượng khách hàng mục tiêu?"                              │
│   - "Pain points lớn nhất của quy trình hiện tại?"                      │
│                                                                         │
│ • Tiến tới câu hỏi LÀM RÕ (CLARIFYING):                                 │
│   - "Khi nói 'giao dịch nhanh', bạn đề cập đến bao nhiêu giây?"        │
│   - "'Khách hàng VIP' được định nghĩa như thế nào?"                    │
│                                                                         │
│ • Đi sâu với câu hỏi THĂM DÒ (PROBING):                                 │
│   - "Điều gì xảy ra nếu mất kết nối giữa giao dịch?"                   │
│   - "Có ngoại lệ nào cho quy tắc xác thực 2 bước không?"               │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Bước 3: /ba-prioritization (Áp dụng khi đã thu thập yêu cầu)            │
│ ─────────────────────────────────────────────────────────────────────── │
│ • Sử dụng MoSCoW để phân loại nhanh:                                    │
│   MUST: Đăng nhập, Chuyển tiền, Xem số dư                               │
│   SHOULD: Thanh toán hóa đơn, Lịch sử giao dịch                         │
│   COULD: Sản phẩm đầu tư, Chatbot                                       │
│   WON'T: Giao dịch tiền ảo (Phase 2)                                    │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Bước 4: /ba-writing + /ba-nfr                                           │
│ ─────────────────────────────────────────────────────────────────────── │
│ • Viết FR sử dụng template chuẩn:                                       │
│   "Hệ thống PHẢI (SHALL) cho phép người dùng đã xác thực chuyển tiền    │
│    KHI họ cung cấp tài khoản người nhận và số tiền                      │
│    ĐỂ họ có thể hoàn thành giao dịch tài chính từ xa."                  │
│                                                                         │
│ • Định nghĩa NFRs sử dụng ISO 25010:                                    │
│   NFR-PERF-001: Thời gian phản hồi < 2 giây cho chuyển tiền             │
│   NFR-SEC-001: Mã hóa TLS 1.3, xác thực sinh trắc học                   │
│   NFR-REL-001: Độ sẵn sàng 99.99%                                       │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Bước 5: Tạo sản phẩm sử dụng template                                   │
│ ─────────────────────────────────────────────────────────────────────── │
│ • Tham chiếu: templates/SKILL-09-brd-template.md (cho business case)    │
│ • Tham chiếu: templates/SKILL-10-srs-template.md (cho đặc tả chi tiết)  │
│ • Tham chiếu: templates/SKILL-12-agile-artifacts.md (cho user stories)  │
└─────────────────────────────────────────────────────────────────────────┘
```

---

### Kịch bản 2: Các Stakeholder đang Xung đột

```
USER: "Team Sales muốn báo cáo thời gian thực nhưng IT nói xử lý batch khả thi hơn"

ĐƯỜNG DẪN WORKFLOW:
┌─────────────────────────────────────────────────────────────────────────┐
│ Bước 1: /ba-identity (Refresh nhanh)                                    │
│ ─────────────────────────────────────────────────────────────────────── │
│ • Hãy nhớ: Giữ TRUNG LẬP - bạn là người điều phối, không phải ra q.định │
│ • Map cả hai stakeholders:                                              │
│   Sales = Lợi ích Cao, Quyền lực Trung bình                             │
│   IT = Lợi ích Trung bình, Quyền lực Cao (thẩm quyền kỹ thuật)          │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Bước 2: /ba-conflict (WORKFLOW CHÍNH)                                   │
│ ─────────────────────────────────────────────────────────────────────── │
│ Áp dụng Phương pháp Harvard - Tập trung vào LỢI ÍCH, không phải VỊ THẾ: │
│                                                                         │
│ VỊ THẾ SALES: "Chúng tôi cần báo cáo realtime"                          │
│ LỢI ÍCH SALES: Cần dữ liệu HIỆN TẠI để ra quyết định nhanh              │
│                                                                         │
│ VỊ THẾ IT: "Xử lý batch là đủ rồi"                                      │
│ LỢI ÍCH IT: Lo ngại về HIỆU NĂNG hệ thống và độ PHỨC TẠP                │
│                                                                         │
│ TẠO CÁC LỰA CHỌN (OPTIONS):                                             │
│ 1. Real-time chỉ cho các KPI quan trọng, batch cho báo cáo chi tiết     │
│ 2. Gần real-time (làm mới mỗi 5 phút) như một thỏa hiệp                 │
│ 3. Real-time với chiến lược caching được IT chấp thuận                  │
│                                                                         │
│ SỬ DỤNG TIÊU CHÍ KHÁCH QUAN:                                            │
│ • Đối thủ cạnh tranh cung cấp độ trễ bao nhiêu?                         │
│ • Tác động kinh doanh thực tế của độ trễ 5 phút là gì?                  │
│ • Chênh lệch chi phí hạ tầng là bao nhiêu?                              │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Bước 3: /ba-traceability                                                │
│ ─────────────────────────────────────────────────────────────────────── │
│ Tài liệu hóa quyết định:                                                │
│ • Xung đột ban đầu                                                      │
│ • Các lựa chọn đã xem xét                                               │
│ • Quyết định cuối cùng + lý do                                          │
│ • Ai đã phê duyệt                                                       │
│ • Cập nhật RTM với yêu cầu đã giải quyết                                │
└─────────────────────────────────────────────────────────────────────────┘
```

---

### Kịch bản 3: Review Tài liệu Yêu cầu Hiện có

```
USER: "Vui lòng review SRS này để tìm lỗi chất lượng"

ĐƯỜNG DẪN WORKFLOW:
┌─────────────────────────────────────────────────────────────────────────┐
│ Bước 1: /ba-writing (Sử dụng như checklist tham chiếu)                  │
│ ─────────────────────────────────────────────────────────────────────── │
│ Kiểm tra từng yêu cầu dựa trên tiêu chí chất lượng:                     │
│                                                                         │
│ ☐ Sử dụng đúng SHALL/SHOULD/MAY không?                                  │
│ ☐ Có nguyên tử (atomic - một yêu cầu trên một câu) không?               │
│ ☐ Có không mơ hồ (không dùng "nhanh", "thân thiện", "v.v.")?            │
│ ☐ Có thể kiểm thử (có tiêu chí nghiệm thu đo lường được)?               │
│ ☐ Có đầy đủ (không có TBDs)?                                            │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Bước 2: /ba-validation (WORKFLOW CHÍNH)                                 │
│ ─────────────────────────────────────────────────────────────────────── │
│ Áp dụng checklist xác minh:                                             │
│                                                                         │
│ KIỂM TRA YÊU CẦU CÁ NHÂN:                                               │
│ ☐ Có ID duy nhất                                                        │
│ ☐ Có tiêu đề rõ ràng                                                    │
│ ☐ Sử dụng từ khóa chính xác                                             │
│ ☐ Có tiêu chí nghiệm thu                                                │
│ ☐ Có tính khả thi                                                       │
│ ☐ Truy vết được về nhu cầu kinh doanh                                   │
│                                                                         │
│ KIỂM TRA BỘ YÊU CẦU:                                                    │
│ ☐ Đầy đủ - tất cả nhu cầu đã được nắm bắt                               │
│ ☐ Nhất quán - không mâu thuẫn                                           │
│ ☐ Không trùng lặp                                                       │
│ ☐ Không có lỗ hổng                                                      │
│                                                                         │
│ Ghi log lỗi tìm thấy:                                                   │
│ DEF-001: FR-003 dùng "nhanh" - MƠ HỒ - Major                            │
│ DEF-002: FR-007 không có tiêu chí nghiệm thu - KHÔNG ĐẦY ĐỦ - Major     │
│ DEF-003: FR-012 và FR-015 mâu thuẫn - KHÔNG NHẤT QUÁN - Critical        │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Bước 3: /ba-traceability                                                │
│ ─────────────────────────────────────────────────────────────────────── │
│ • Chạy kiểm tra sức khỏe RTM                                            │
│ • Xác định yêu cầu mồ côi (orphan requirements)                         │
│ • Xác định yêu cầu chưa được kiểm thử                                   │
│ • Cập nhật RTM với kết quả review                                       │
└─────────────────────────────────────────────────────────────────────────┘
```

---

### Kịch bản 4: Lên kế hoạch Agile Sprint

```
USER: "Giúp tôi tạo user stories cho tính năng thanh toán (checkout)"

ĐƯỜNG DẪN WORKFLOW:
┌─────────────────────────────────────────────────────────────────────────┐
│ Bước 1: /ba-elicitation (Khám phá nhanh)                                │
│ ─────────────────────────────────────────────────────────────────────── │
│ Đặt câu hỏi 5W1H:                                                       │
│ • WHO: Ai thanh toán? (Khách vãng lai, Thành viên, VIP)                 │
│ • WHAT: Hành động gì? (Thêm vào giỏ, Áp mã, Trả tiền, Xác nhận)         │
│ • WHEN: Ràng buộc thời gian? (Hết phiên, Flash sale)                    │
│ • WHERE: Web hay mobile?                                                │
│ • WHY: Mục tiêu? (Tăng chuyển đổi, Giảm bỏ giỏ hàng)                    │
│ • HOW: Phương thức? (Thẻ, Ví điện tử, COD)                              │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Bước 2: /ba-writing (Cấu trúc user stories)                             │
│ ─────────────────────────────────────────────────────────────────────── │
│ Sử dụng định dạng chuẩn + tiêu chí INVEST:                              │
│                                                                         │
│ ✅ USER STORY TỐT:                                                      │
│ "Là một khách hàng quay lại,                                            │
│  Tôi muốn lưu phương thức thanh toán của mình,                          │
│  Để tôi có thể thanh toán nhanh hơn trong các lần mua sau."             │
│                                                                         │
│ Tiêu chí Nghiệm thu (Gherkin):                                          │
│ Given tôi đã đăng nhập và đang ở trang thanh toán                       │
│ When tôi tích vào "Lưu thẻ này cho lần sau"                             │
│ Then thẻ của tôi được lưu trữ an toàn                                   │
│ And tôi thấy nó được chọn sẵn ở lần thanh toán tới                      │
│                                                                         │
│ Kiểm tra INVEST:                                                        │
│ ☑ Independent - Có thể phát triển độc lập                               │
│ ☑ Negotiable - Chi tiết có thể thương lượng                             │
│ ☑ Valuable - Lợi ích người dùng rõ ràng                                 │
│ ☑ Estimable - Team có thể ước lượng                                     │
│ ☑ Small - Vừa vặn trong một sprint                                      │
│ ☑ Testable - Tiêu chí nghiệm thu rõ ràng                                │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Bước 3: /ba-prioritization                                              │
│ ─────────────────────────────────────────────────────────────────────── │
│ Áp dụng WSJF để sắp xếp backlog:                                        │
│                                                                         │
│ ┌────────────────────┬───────┬───────┬───────┬───────┬────────┐        │
│ │ Story              │ Value │ Time  │ Risk  │ Size  │ WSJF   │        │
│ ├────────────────────┼───────┼───────┼───────┼───────┼────────┤        │
│ │ Checkout cơ bản    │   13  │   8   │   5   │   5   │  5.2   │        │
│ │ Lưu thanh toán     │    5  │   3   │   2   │   2   │  5.0   │        │
│ │ Áp dụng coupon     │    8  │   5   │   1   │   3   │  4.7   │        │
│ │ Checkout vãng lai  │    8  │   8   │   3   │   5   │  3.8   │        │
│ └────────────────────┴───────┴───────┴───────┴───────┴────────┘        │
│                                                                         │
│ Sprint 1: Checkout cơ bản (WSJF cao nhất)                               │
│ Sprint 2: Lưu thanh toán, Áp dụng coupon                                │
│ Sprint 3: Checkout vãng lai                                             │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Tham khảo Lệnh Nhanh

### Khi nào dùng Workflow nào

| Bạn Muốn... | Dùng Lệnh Này | Nó Làm Gì |
|-------------|---------------|-----------|
| **Bắt đầu mọi task BA** | `/ba-identity` | Kích hoạt persona chuyên gia, map stakeholder |
| **Phỏng vấn stakeholder** | `/ba-elicitation` | Lấy khung câu hỏi, kỹ thuật phễu |
| **Viết yêu cầu chất lượng** | `/ba-writing` | Lấy template, checklist chất lượng |
| **Đặc tả NFRs** | `/ba-nfr` | Lấy template ISO 25010 (Hiệu năng, Bảo mật...) |
| **Ưu tiên tính năng** | `/ba-prioritization` | Lấy kỹ thuật MoSCoW, Kano, WSJF |
| **Giải quyết xung đột** | `/ba-conflict` | Lấy phương pháp Harvard, ma trận leo thang |
| **Theo dõi yêu cầu** | `/ba-traceability` | Lấy template RTM, kiểm soát thay đổi |
| **Review yêu cầu** | `/ba-validation` | Lấy checklist V&V, quy trình ký duyệt |

---

## 🎓 Mẹo Làm chủ (Mastery Tips)

### Tip 1: Chuỗi Workflow Tự nhiên
Đừng nghĩ các workflow là công cụ rời rạc. Chúng chảy tự nhiên:

```
/ba-identity → /ba-elicitation → /ba-writing → /ba-validation
     ↓              ↓                ↓               ↓
   AI LÀ?        THU THẬP          TÀI LIỆU        XÁC MINH
```

### Tip 2: Luôn Bắt đầu với Core Skills
Dù là task "nhanh", hãy kích hoạt tư duy:
1. **Identity** - Tôi có giữ trung lập không? Stakeholder của tôi là ai?
2. **Elicitation** - Tôi có đang hỏi đúng câu hỏi không?
3. **Writing** - Tôi có đang tài liệu hóa rõ ràng không?

### Tip 3: Dùng Template làm Điểm Khởi đầu
Các template (SKILL-09 đến SKILL-12) sinh ra để được tùy chỉnh. Đừng điền mọi trường nếu không áp dụng.

### Tip 4: Tài liệu hóa Quyết định, Không chỉ Yêu cầu
Dùng `/ba-traceability` và `/ba-conflict` để ghi lại TẠI SAO quyết định được đưa ra, không chỉ CÁI GÌ được quyết định.

### Tip 5: Lặp lại, Đừng Hoàn hảo ngay
Yêu cầu luôn tiến hóa. Sử dụng tiếp cận lặp:
- Nháp → Review → Tinh chỉnh → Baseline
- Baseline → Yêu cầu thay đổi → Phân tích tác động → Cập nhật

---

## 📋 Lệnh Khởi động Nhanh cho Task Phổ biến

```
┌─────────────────────────────────────────────────────────────────────────┐
│ TASK                              │ COMMAND SEQUENCE                    │
├───────────────────────────────────┼─────────────────────────────────────┤
│ Khởi động dự án mới               │ /ba-identity → /ba-elicitation      │
│                                   │ → /ba-prioritization                │
├───────────────────────────────────┼─────────────────────────────────────┤
│ Viết SRS                          │ /ba-writing → /ba-nfr               │
│                                   │ + templates/SKILL-10                │
├───────────────────────────────────┼─────────────────────────────────────┤
│ Tạo user stories                  │ /ba-elicitation → /ba-writing       │
│                                   │ + templates/SKILL-12                │
├───────────────────────────────────┼─────────────────────────────────────┤
│ Giải quyết bất đồng stakeholder   │ /ba-conflict                        │
├───────────────────────────────────┼─────────────────────────────────────┤
│ Review chất lượng yêu cầu         │ /ba-validation → /ba-writing        │
├───────────────────────────────────┼─────────────────────────────────────┤
│ Xử lý yêu cầu thay đổi            │ /ba-traceability                    │
├───────────────────────────────────┼─────────────────────────────────────┤
│ Định nghĩa yêu cầu hiệu năng      │ /ba-nfr                             │
└───────────────────────────────────┴─────────────────────────────────────┘
```

---

## 🚀 Bắt đầu Ngay Bây giờ

**Bước 1**: Mở bất kỳ hội thoại nào liên quan đến BA

**Bước 2**: Gõ `/ba-master` để xem bản đồ workflow đầy đủ

**Bước 3**: Chọn workflow phù hợp dựa trên task của bạn

**Bước 4**: Làm theo hướng dẫn từng bước trong workflow đó

**Ví dụ Prompt**:
```
Tôi cần thu thập yêu cầu cho một hệ thống nhận diện khách hàng VIP mới 
tại chi nhánh ngân hàng. Bắt đầu với workflow /ba-identity và /ba-elicitation.
```

AI sẽ:
1. Kích hoạt persona BA Expert
2. Giúp bạn map stakeholders
3. Hướng dẫn bạn qua các câu hỏi có cấu trúc
4. Tài liệu hóa yêu cầu theo định dạng chuẩn
