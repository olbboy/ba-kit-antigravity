# Template: Business Requirements Document (BRD)
Tài liệu yêu cầu nghiệp vụ — mô tả WHY và WHAT của dự án, không đi vào HOW.

## How to Use
- Điền tất cả `{placeholder}` trước khi chia sẻ với stakeholders.
- Mỗi chức năng trong bảng Feature phải có ít nhất 1 US tương ứng.
- Review lại mục Giả định & Ràng buộc trước mỗi sprint planning.

---

## Thông tin dự án

| Trường | Giá trị |
|--------|---------|
| **Tên dự án** | {project_name} |
| **Phiên bản** | {version} |
| **Ngày tạo** | {date} |
| **BA phụ trách** | {ba_name} |
| **Product Owner** | {po_name} |
| **Trạng thái** | Draft / In Review / Approved |

---

## Mục tiêu nghiệp vụ

> {Mô tả vấn đề đang giải quyết và giá trị kỳ vọng — 2-4 câu}

**Mục tiêu đo lường được (SMART):**
- {objective_1}
- {objective_2}

---

## Phạm vi (Scope)

### Trong phạm vi (In Scope)
- {in_scope_item_1}
- {in_scope_item_2}

### Ngoài phạm vi (Out of Scope)
- {out_of_scope_item_1}
- {out_of_scope_item_2}

---

## Stakeholders

| Vai trò | Tên | Phòng ban | Mức độ ảnh hưởng | Kỳ vọng chính |
|---------|-----|-----------|-----------------|---------------|
| {role} | {name} | {dept} | H/M/L | {expectation} |

---

## Chức năng (Features)

| Mã | Tên chức năng | Mô tả nghiệp vụ | US liên quan | Độ ưu tiên |
|----|---------------|-----------------|--------------|-----------|
| F-01 | {feature_name} | {description} | US-{num} | Must/Should/Could |

---

## Yêu cầu phi chức năng (NFRs)

| Loại | Yêu cầu | Chỉ tiêu |
|------|---------|---------|
| Performance | {requirement} | {metric} |
| Security | {requirement} | {standard} |
| Availability | {requirement} | {uptime_sla} |

---

## Giả định

- {assumption_1}
- {assumption_2}

---

## Ràng buộc

- {constraint_1} *(loại: kỹ thuật / nghiệp vụ / pháp lý / ngân sách)*
- {constraint_2}

---

## Lịch sử thay đổi

| Phiên bản | Ngày | Người thay đổi | Mô tả |
|-----------|------|----------------|-------|
| {version} | {date} | {author} | {change} |
