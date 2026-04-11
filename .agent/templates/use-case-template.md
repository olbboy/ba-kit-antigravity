# Template: Use Case Specification
Đặc tả use case theo chuẩn UML/Cockburn — mô tả tương tác actor-system đầy đủ.

## How to Use
- 1 file = 1 use case. Đặt tên: `UC-{ID}-{slug}.md`.
- Main Flow phải là luồng thành công (happy path) — không trộn exception vào.
- Mỗi Alternative/Exception Flow phải ghi rõ tại bước nào của Main Flow nó tách ra.

---

## Định danh

| Trường | Giá trị |
|--------|---------|
| **UC ID** | UC-{module}-{num} |
| **Tên** | {use_case_name} |
| **Actor chính** | {primary_actor} |
| **Actor phụ** | {secondary_actors} |
| **Feature liên quan** | F-{num} |
| **US liên quan** | US-{num} |
| **Phiên bản** | {version} |

---

## Mô tả ngắn

> {1-2 câu mô tả mục đích của use case này}

---

## Điều kiện tiên quyết (Preconditions)

- {precondition_1}
- {precondition_2}

---

## Luồng chính (Main Flow)

| Bước | Actor | Hành động | Phản hồi hệ thống |
|------|-------|-----------|------------------|
| 1 | {actor} | {action} | {system_response} |
| 2 | System | — | {system_action} |
| 3 | {actor} | {action} | {system_response} |

---

## Luồng thay thế (Alternative Flows)

### AF-01: {alternative_name} *(rẽ tại bước {N})*
1. {step}
2. {step}
3. Quay lại bước {N} của Main Flow.

---

## Luồng ngoại lệ (Exception Flows)

### EF-01: {exception_name} *(rẽ tại bước {N})*
1. {trigger_condition}
2. Hệ thống hiển thị: `"{error_message}"`
3. Use case kết thúc / Quay lại bước {N}.

---

## Điều kiện kết thúc (Postconditions)

**Thành công:** {success_state}
**Thất bại:** {failure_state}

---

## Business Rules

| Mã | Quy tắc |
|----|--------|
| BR-{num} | {rule_description} |

---

## Ghi chú

> {additional_notes — UI constraints, performance notes, security considerations}
