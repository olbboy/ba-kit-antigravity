# Template: Data Dictionary & Glossary
Từ điển dữ liệu và thuật ngữ dự án — nguồn sự thật duy nhất cho tên gọi và định nghĩa.

## How to Use
- Thêm term mới ngay khi xuất hiện trong requirements — không để sau mới bổ sung.
- "Owner module" trong Entity table = team/service chịu trách nhiệm CRUD entity đó.
- Field table điền đầy đủ Constraints để dev không tự suy đoán DB schema.

---

## Thông tin tài liệu

| Trường | Giá trị |
|--------|---------|
| **Dự án** | {project_name} |
| **Phiên bản** | {version} |
| **Ngày cập nhật** | {date} |
| **Owner** | {ba_or_architect_name} |

---

## Bảng thuật ngữ (Glossary)

| Thuật ngữ | Tiếng Việt | Tiếng Anh | Định nghĩa | Nguồn |
|-----------|-----------|-----------|-----------|-------|
| {term} | {vi_term} | {en_term} | {definition} | BRD / Domain / Luật |
| {term} | {vi_term} | {en_term} | {definition} | {source} |

> Quy tắc: Khi thuật ngữ xuất hiện trong requirements, phải dùng đúng tên trong cột "Thuật ngữ" — không dùng synonym.

---

## Bảng Entity

| Entity | Tên hiển thị | Mô tả nghiệp vụ | Owner Module | DB Table |
|--------|-------------|----------------|-------------|---------|
| {EntityName} | {display_name} | {business_description} | {module} | `{table_name}` |

---

## Bảng Field (Data Dictionary)

### Entity: {EntityName}

| Field | Kiểu dữ liệu | Nullable | Constraints | Mô tả nghiệp vụ |
|-------|-------------|---------|------------|----------------|
| `id` | UUID | No | PK, auto-generated | Định danh duy nhất |
| `{field_name}` | {VARCHAR/INT/BOOL/...} | Yes/No | {UNIQUE/FK/CHECK/...} | {business_meaning} |
| `{field_name}` | {type} | Yes | Max: {N} chars | {description} |
| `created_at` | TIMESTAMP | No | Default: NOW() | Thời điểm tạo record |
| `updated_at` | TIMESTAMP | No | Auto-update | Thời điểm cập nhật cuối |

**Indexes:**
- `idx_{table}_{field}` on `{field}` — {reason}

**Enum values cho `{field_name}`:**
| Value | Nhãn hiển thị | Mô tả |
|-------|--------------|-------|
| `{VALUE}` | {label} | {description} |

---

## Quy tắc đặt tên (Naming Conventions)

| Loại | Convention | Ví dụ |
|------|-----------|-------|
| DB Table | snake_case, số nhiều | `user_profiles` |
| DB Column | snake_case | `first_name` |
| API field | camelCase | `firstName` |
| Enum | UPPER_SNAKE_CASE | `PENDING_APPROVAL` |
