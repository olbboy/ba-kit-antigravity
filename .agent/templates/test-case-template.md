# Template: Test Case Specification
Đặc tả test case đơn lẻ — đủ chi tiết để QA thực thi mà không cần hỏi thêm.

## How to Use
- 1 file = 1 test case. Thường được nhóm trong Test Suite.
- Điền Test Data cụ thể — không để "any valid data".
- Priority: P1=Blocker, P2=Critical, P3=Major, P4=Minor.

---

## Định danh

| Trường | Giá trị |
|--------|---------|
| **TC ID** | TC-{US_ID}-{num} |
| **Tên** | {test_case_title} |
| **US liên quan** | US-{num} |
| **AC liên quan** | AC-{num} |
| **Loại** | Happy Path / Edge Case / Error / Security / Performance |
| **Priority** | P1 / P2 / P3 / P4 |
| **Trạng thái** | Not Run / Pass / Fail / Blocked / N/A |
| **Người tạo** | {author} |
| **Ngày tạo** | {date} |

---

## Điều kiện tiên quyết (Preconditions)

- {precondition_1} *(vd: User đã login với role {role})*
- {precondition_2}

---

## Test Data

| Trường | Giá trị test |
|--------|-------------|
| {field_1} | `{value_1}` |
| {field_2} | `{value_2}` |

---

## Các bước thực thi

| Bước | Hành động | Kết quả mong đợi |
|------|-----------|-----------------|
| 1 | {action} | {expected_result} |
| 2 | {action} | {expected_result} |
| 3 | {action} | {expected_result} |

---

## Kết quả mong đợi cuối cùng

> {Overall expected outcome — trạng thái hệ thống sau khi test hoàn tất}

---

## Điều kiện kết thúc (Postconditions)

- {postcondition_1} *(vd: Record được tạo trong DB với status = {value})*

---

## Ghi chú

> {Notes về môi trường test, data cleanup, known limitations}

**Thực thi lần cuối:** {date} | **Kết quả:** {Pass/Fail} | **Người thực thi:** {tester}
