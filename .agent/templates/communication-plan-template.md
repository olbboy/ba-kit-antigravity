# Template: Stakeholder Communication Plan
Kế hoạch truyền thông với stakeholders — ai cần biết gì, khi nào, qua kênh nào.

## How to Use
- Điền Stakeholder Register trước khi lập Communication Matrix.
- Influence/Interest dùng thang H/M/L — dùng để ưu tiên effort truyền thông.
- Review lại plan khi có stakeholder mới hoặc thay đổi phase dự án.

---

## Thông tin tài liệu

| Trường | Giá trị |
|--------|---------|
| **Dự án** | {project_name} |
| **Phiên bản** | {version} |
| **Ngày tạo** | {date} |
| **BA phụ trách** | {ba_name} |

---

## Stakeholder Register

| Tên | Vai trò | Phòng ban | Mức độ quan tâm | Mức độ ảnh hưởng | Kênh ưa thích | Ghi chú |
|-----|---------|-----------|----------------|-----------------|--------------|--------|
| {name} | {role} | {dept} | H/M/L | H/M/L | Email/Slack/Meeting | {notes} |
| {name} | {role} | {dept} | H/M/L | H/M/L | {channel} | {notes} |

**Phân loại (Power/Interest Grid):**
- **Manage Closely** (H Power, H Interest): {stakeholders}
- **Keep Satisfied** (H Power, L Interest): {stakeholders}
- **Keep Informed** (L Power, H Interest): {stakeholders}
- **Monitor** (L Power, L Interest): {stakeholders}

---

## Communication Matrix

| Artifact / Sự kiện | Đối tượng | Tần suất | Kênh | Owner | Mục đích |
|-------------------|-----------|---------|------|-------|---------|
| Project Status Update | {audience} | Weekly | {channel} | BA | Cập nhật tiến độ |
| Sprint Review | {audience} | Bi-weekly | Meeting | PM | Demo & feedback |
| Requirements Sign-off | {audience} | Per milestone | Email + Meeting | BA | Phê duyệt chính thức |
| Risk Escalation | {audience} | Ad-hoc | {channel} | {owner} | Báo cáo rủi ro |
| {artifact} | {audience} | {frequency} | {channel} | {owner} | {purpose} |

---

## Escalation Path

```
Level 1: BA → {direct_contact} (response SLA: {N} giờ)
Level 2: PM → {manager} (response SLA: {N} ngày)
Level 3: Steering Committee (blocker không giải quyết được ở L2)
```

---

## Meeting Cadence

| Loại meeting | Tần suất | Thời lượng | Participants | Agenda template |
|-------------|---------|-----------|-------------|----------------|
| Daily standup | Daily | 15 min | Dev team | Yesterday / Today / Blockers |
| Sprint planning | Bi-weekly | 2h | Team + PO | Backlog refinement + commitment |
| Stakeholder review | {frequency} | {duration} | {participants} | Demo + decisions needed |
| {meeting_type} | {frequency} | {duration} | {participants} | {agenda} |

---

## Templates thông báo chuẩn

### Status Update (Weekly)
```
Tuần {N} — {project_name}
✅ Hoàn thành: {completed_items}
🔄 Đang làm: {in_progress_items}
⚠️ Rủi ro / Blockers: {risks}
📅 Tuần tới: {next_week_plan}
```
