# Template: Requirements Traceability Matrix (RTM)
Ma trận truy vết yêu cầu — chứng minh mọi requirement đều có nguồn gốc, được implement và được test.

## How to Use
- Cập nhật RTM mỗi khi thêm US mới, viết AC, hoặc tạo TC.
- Coverage Dashboard tính tự động từ bảng RTM — điền đầy đủ các cột trước.
- Orphan = có code/test không có US | Untested = US không có TC | Gold-plating = feature không trong BRD.

---

## Thông tin tài liệu

| Trường | Giá trị |
|--------|---------|
| **Dự án** | {project_name} |
| **Phiên bản** | {version} |
| **Ngày cập nhật** | {date} |
| **Owner** | {ba_name} |

---

## RTM Table

| REQ ID | Mô tả yêu cầu | Priority | BRD Source | US ID | AC # | TC # | API Endpoint | DB Table | Trạng thái | Owner |
|--------|--------------|---------|-----------|-------|------|------|-------------|---------|-----------|-------|
| REQ-01 | {requirement} | Must | F-{num} | US-{num} | AC-01,02 | TC-{n},TC-{n} | `POST /api/{path}` | `{table}` | Traced / Partial / Orphan | {name} |
| REQ-02 | {requirement} | Should | F-{num} | US-{num} | AC-01 | — | — | `{table}` | Untested | {name} |
| REQ-{N} | {requirement} | {priority} | {brd_ref} | {us_id} | {ac_list} | {tc_list} | {api} | {db} | {status} | {owner} |

**Trạng thái legend:**
- `Traced` — có đầy đủ chuỗi BRD → US → AC → TC
- `Partial` — thiếu 1 hoặc nhiều link trong chuỗi
- `Orphan` — không tìm thấy BRD source (scope risk)
- `Untested` — có US/AC nhưng chưa có TC
- `Gold-plating` — có code/TC nhưng không có REQ tương ứng

---

## Coverage Dashboard

| Chỉ số | Giá trị | Mục tiêu | Trạng thái |
|--------|--------|---------|-----------|
| Tổng requirements | {total_req} | — | — |
| Fully Traced (BRD→TC) | {traced} / {total_req} | 100% | ✅ / ⚠️ / ❌ |
| Requirements có US | {with_us} / {total_req} | 100% | ✅ / ⚠️ / ❌ |
| US có AC | {with_ac} / {total_us} | 100% | ✅ / ⚠️ / ❌ |
| AC có TC | {with_tc} / {total_ac} | ≥ 95% | ✅ / ⚠️ / ❌ |
| TC Pass rate | {pass} / {total_tc} | ≥ 95% | ✅ / ⚠️ / ❌ |

---

## Phân tích Gap

### Orphan Requirements (có code/test, không có US)
| Artifact | Mô tả | Hành động |
|---------|-------|---------|
| {artifact_id} | {description} | Thêm US hoặc xóa code |

### Untested Requirements (có US/AC, chưa có TC)
| US ID | AC chưa có TC | Owner | Deadline |
|-------|-------------|-------|---------|
| US-{num} | AC-{num} | {qa_name} | {date} |

### Gold-plating (feature không trong BRD)
| Feature | Lý do tồn tại | Quyết định |
|---------|-------------|-----------|
| {feature} | {reason} | Giữ / Xóa / Thêm vào BRD |

---

## Impact Analysis Template

Khi thay đổi **{REQ ID}**, các artifact bị ảnh hưởng:

```
REQ-{N} → US-{num} → AC-{list} → TC-{list}
                              → API: {endpoints}
                              → DB: {tables}
Blast radius: {N} TC cần retest, {N} API cần update
```
