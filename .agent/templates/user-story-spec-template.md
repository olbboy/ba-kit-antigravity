# Template: User Story Specification
Đặc tả user story chi tiết — đủ thông tin để dev + QA làm việc không cần hỏi lại.

## How to Use
- 1 file = 1 user story. Đặt tên file: `US-{ID}-{slug}.md`.
- Acceptance Criteria phải viết theo Gherkin (Given/When/Then) hoặc checklist rõ ràng.
- Definition of Done phải được team đồng ý trước sprint.

---

## Định danh

| Trường | Giá trị |
|--------|---------|
| **US ID** | US-{module}-{num} |
| **Tên** | {story_title} |
| **Feature** | F-{num}: {feature_name} |
| **Sprint** | {sprint_number} |
| **Story Points** | {points} |
| **Độ ưu tiên** | Must / Should / Could / Won't |
| **Trạng thái** | Draft / Ready / In Dev / Done |

---

## User Story

> **AS A** {actor/role}
> **I WANT TO** {action/capability}
> **SO THAT** {benefit/business_value}

---

## Business Flow (Luồng nghiệp vụ)

1. {step_1}
2. {step_2}
3. {step_3}

**Trigger:** {what_initiates_this_flow}
**End State:** {what_success_looks_like}

---

## Phân quyền (RBAC)

| Role | Có thể thực hiện | Ghi chú |
|------|-----------------|--------|
| {role_1} | Yes | {note} |
| {role_2} | No | {reason} |

---

## Acceptance Criteria

### AC-01: {happy_path_title}
```
Given {precondition}
When  {action}
Then  {expected_result}
```

### AC-02: {edge_case_title}
```
Given {precondition}
When  {action}
Then  {expected_result}
```

### AC-03: {error_case_title}
```
Given {precondition}
When  {invalid_action}
Then  {error_behavior}
```

---

## Edge Cases

| Tình huống | Input | Expected Behavior |
|-----------|-------|------------------|
| {scenario} | {input_data} | {expected} |

---

## Definition of Done

- [ ] Code reviewed và merged vào nhánh dev
- [ ] Unit tests passed (coverage ≥ {N}%)
- [ ] AC-01 đến AC-{N} đều passed (manual/auto test)
- [ ] Không có P1/P2 bug còn mở
- [ ] {custom_dod_item}

---

## Ghi chú kỹ thuật

> {Technical notes cho dev — API deps, DB changes, migration needs, etc.}

**Phụ thuộc:** {US-ID hoặc task liên quan}
