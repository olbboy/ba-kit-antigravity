# Template: Squad Shared Memory (Continuity)
Tài liệu bàn giao context cho agent mới hoặc team member tiếp theo — không mất context giữa sessions.

## How to Use
- Cập nhật file này sau mỗi session làm việc quan trọng.
- Section "Key Decisions" là bắt buộc — lý do quyết định quan trọng hơn bản thân quyết định.
- Agent mới đọc file này TRƯỚC KHI làm bất cứ điều gì.

---

## Thông tin dự án

| Trường | Giá trị |
|--------|---------|
| **Tên dự án** | {project_name} |
| **Repository** | {repo_url} |
| **Phase hiện tại** | {current_phase} |
| **Sprint** | {sprint_number} |
| **Cập nhật lần cuối** | {date} bởi {author} |

---

## Tóm tắt dự án

> {2-3 câu mô tả dự án — đủ để agent mới hiểu ngay không cần đọc thêm tài liệu khác}

**Stack kỹ thuật:** {tech_stack}
**Môi trường:** Dev: `{dev_url}` | Staging: `{staging_url}` | Prod: `{prod_url}`

---

## Phase & Trạng thái

| Phase | Tên | Trạng thái | Ghi chú |
|-------|-----|-----------|--------|
| P1 | {phase_name} | Done / In Progress / Pending | {note} |
| P2 | {phase_name} | Pending | Bắt đầu sau khi P1 xong |

---

## Key Decisions (Quyết định quan trọng)

| Ngày | Quyết định | Lý do | Người quyết định |
|------|-----------|-------|-----------------|
| {date} | {decision} | {rationale} | {decider} |

---

## Open Questions (Câu hỏi chưa có đáp án)

| # | Câu hỏi | Owner | Deadline | Trạng thái |
|---|---------|-------|---------|-----------|
| 1 | {question} | {owner} | {date} | Open / Resolved |

---

## Blockers

| # | Blocker | Impact | Owner | Giải pháp tạm thời |
|---|---------|--------|-------|------------------|
| 1 | {blocker} | High/Medium/Low | {owner} | {workaround} |

---

## Next Actions

- [ ] {action_1} — Owner: {owner} — Due: {date}
- [ ] {action_2} — Owner: {owner} — Due: {date}

---

## Knowledge Transfer Notes

> {Những điều "không có trong docs" mà agent/dev tiếp theo cần biết — gotchas, quirks, tribal knowledge}

**Files quan trọng cần đọc đầu tiên:**
1. `{file_path}` — {why_important}
2. `{file_path}` — {why_important}

**Liên hệ khi bị blocked:**
- {topic}: {contact_name} ({channel})
