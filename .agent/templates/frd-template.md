# Template: Functional Requirements Document (FRD)
Đặc tả chức năng chi tiết — cầu nối giữa BRD (nghiệp vụ) và dev team (kỹ thuật).

## How to Use
- Mỗi feature trong BRD được mở rộng thành 1 section chi tiết ở đây.
- Điền đầy đủ RBAC và Validation rules — dev không nên tự suy đoán.
- Data Flow dùng để đặc tả luồng dữ liệu qua các components.

---

## Thông tin tài liệu

| Trường | Giá trị |
|--------|---------|
| **Dự án** | {project_name} |
| **Phiên bản** | {version} |
| **Ngày** | {date} |
| **Tham chiếu BRD** | {brd_ref} |

---

## Feature Summary

| Mã | Tên feature | Module | Độ ưu tiên | Trạng thái |
|----|-------------|--------|-----------|-----------|
| F-01 | {feature_name} | {module} | Must/Should/Could | Draft/Ready/Done |

---

## Chi tiết chức năng

### F-01: {feature_name}

**Mô tả:** {brief_description}

**Mục tiêu nghiệp vụ:** {business_goal}

#### Business Rules
| Mã quy tắc | Mô tả | Nguồn |
|-----------|-------|-------|
| BR-01 | {rule_description} | BRD / Domain Expert |

#### Phân quyền (RBAC)
| Hành động | {Role_1} | {Role_2} | {Role_3} |
|-----------|---------|---------|---------|
| Xem | ✓ | ✓ | ✗ |
| Tạo mới | ✓ | ✗ | ✗ |
| Chỉnh sửa | ✓ | ✗ | ✗ |
| Xóa | ✓ | ✗ | ✗ |

#### Validation Rules
| Trường | Kiểu | Bắt buộc | Quy tắc | Thông báo lỗi |
|--------|------|---------|--------|--------------|
| {field_name} | {type} | Yes/No | {rule} | {error_message} |

#### UI Specifications
- **Màn hình:** {screen_name}
- **Components:** {component_list}
- **Trạng thái loading/empty/error:** {ux_states}
- **Responsive:** {responsive_notes}

#### API Endpoints liên quan
| Method | Path | Mô tả |
|--------|------|-------|
| {GET/POST} | `/api/{path}` | {description} |

---

## Data Flow

```
{Actor} → [{Screen}] → [API: {endpoint}] → [Service] → [DB: {table}]
                                ↓
                         [Response: {data}]
```

**Luồng chính:**
1. {step_1}
2. {step_2}
3. {step_3}

**Luồng ngoại lệ:**
- {exception_flow}

---

## Phụ lục: Mockup / Wireframe

> {Link đến Figma / ảnh mockup hoặc mô tả text}
