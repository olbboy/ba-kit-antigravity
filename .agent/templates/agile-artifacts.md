# Template: Agile Artifacts — Theme / Epic / Story Hierarchy
Cấu trúc phân cấp backlog từ Theme → Epic → User Story theo chuẩn SAFe/Scrum.

## How to Use
- Điền từ trên xuống: Theme → Epic → Stories. Không bắt đầu từ Story.
- Dùng INVEST checklist để validate mỗi User Story trước khi đưa vào sprint.
- Story Points guide ở cuối file — team phải thống nhất trước sprint planning đầu tiên.

---

## Theme

> **Theme:** {theme_name}
> **Mục tiêu chiến lược:** {strategic_objective}
> **OKR liên quan:** {okr_reference}
> **Horizon:** {Q_or_release_target}

---

## Epic

> **Epic ID:** EP-{num}
> **Tên:** {epic_name}
> **Theme:** {theme_name}
> **Hypothesis:** Nếu chúng ta {build_this}, thì {user_segment} sẽ {achieve_outcome}, điều này sẽ {business_impact}.
> **MVP Scope:** {minimum_to_validate_hypothesis}
> **KPI đo lường:** {metric} tăng/giảm {N}% trong {timeframe}

---

## User Story

**US ID:** US-{num}
**Epic:** EP-{num}

> As a **{role}**,
> I want to **{action}**,
> so that **{benefit}**.

### INVEST Checklist
- [ ] **I**ndependent — Story không phụ thuộc vào story khác cùng sprint
- [ ] **N**egotiable — Scope có thể thương lượng, không phải hợp đồng cứng
- [ ] **V**aluable — Deliverable value ngay cả khi deliver một mình
- [ ] **E**stimable — Team có thể estimate được (đủ rõ)
- [ ] **S**mall — Hoàn thành trong 1 sprint (≤ {sprint_days} ngày)
- [ ] **T**estable — AC có thể viết test case được

---

## Acceptance Criteria (Gherkin)

### Scenario 1: {happy_path_name}
```gherkin
Given {initial_context}
  And {additional_context}
When  {trigger_action}
Then  {observable_outcome}
  And {additional_assertion}
```

### Scenario 2: {edge_case_name}
```gherkin
Given {initial_context}
When  {edge_trigger}
Then  {edge_outcome}
```

### Scenario 3: {error_case_name}
```gherkin
Given {initial_context}
When  {invalid_action}
Then  {error_message_displayed}
  And {system_state_unchanged}
```

---

## Story Points Guide (Team Reference)

| Points | Độ phức tạp | Ví dụ |
|--------|------------|-------|
| 1 | Trivial — thay đổi text, config | Đổi label button |
| 2 | Simple — 1 field, 1 endpoint rõ ràng | Thêm field optional vào form |
| 3 | Medium — logic nghiệp vụ nhỏ | Form validation + API call |
| 5 | Complex — nhiều components + rules | Màn hình CRUD đầy đủ |
| 8 | Very Complex — integration + edge cases | Auth flow + RBAC |
| 13 | Cần split — quá lớn cho 1 sprint | → Tách thành 2–3 stories |
