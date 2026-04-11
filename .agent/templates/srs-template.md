# Template: Software Requirements Specification (SRS)
Đặc tả yêu cầu phần mềm theo chuẩn IEEE 29148 — tài liệu kỹ thuật cho dev team.

## How to Use
- Dùng sau khi BRD đã được approved — SRS đi sâu hơn vào chi tiết kỹ thuật.
- Mỗi FR phải có ID duy nhất để link vào RTM.
- NFR section dùng chuẩn ISO 25010 (Functionality, Performance, Security, Maintainability...).

---

## 1. Phạm vi hệ thống

**Tên hệ thống:** {system_name}
**Phiên bản:** {version} | **Ngày:** {date}

> {Mô tả ngắn hệ thống — mục đích, người dùng chính, môi trường triển khai}

---

## 2. Định nghĩa & Thuật ngữ

| Thuật ngữ | Định nghĩa | Nguồn |
|-----------|-----------|-------|
| {term} | {definition} | BRD / Domain |

---

## 3. Tổng quan hệ thống

**Kiến trúc tổng thể:** {architecture_description}

**Người dùng chính:**
- {actor_1}: {description}
- {actor_2}: {description}

**Hệ thống tích hợp:**
- {external_system_1}: {integration_type}

---

## 4. Yêu cầu chức năng (FR)

### Module: {module_name}

| FR ID | Tên yêu cầu | Mô tả | Độ ưu tiên | US liên quan |
|-------|-------------|-------|-----------|--------------|
| FR-{MOD}-01 | {requirement_name} | {description} | Must/Should/Could | US-{num} |

**Chi tiết FR-{MOD}-01:**
- **Điều kiện tiên quyết:** {precondition}
- **Quy tắc nghiệp vụ:** {business_rule}
- **Ngoại lệ:** {exception_handling}

---

## 5. Yêu cầu phi chức năng (NFR — ISO 25010)

| Đặc tính | Tiêu chí | Chỉ tiêu | Phương pháp đo |
|---------|---------|---------|----------------|
| Performance Efficiency | Response time | ≤ {N}ms (p95) | Load test |
| Security | Authentication | {standard} | Pentest |
| Reliability | Uptime | ≥ {N}% | Monitoring |
| Maintainability | Code coverage | ≥ {N}% | CI pipeline |

---

## 6. Yêu cầu giao diện (Interface Requirements)

### 6.1 UI
- {ui_requirement}

### 6.2 API
- Protocol: {REST/GraphQL/gRPC}
- Auth: {OAuth2/JWT/API Key}
- Base URL: `{base_url}`

### 6.3 Tích hợp bên ngoài
- {external_interface_description}

---

## 7. Yêu cầu dữ liệu

| Entity | Mô tả | Volume ước tính | Retention |
|--------|-------|----------------|-----------|
| {entity_name} | {description} | {N} records/day | {N} years |

**Yêu cầu bảo mật dữ liệu:** {data_security_requirements}

---

## 8. Ràng buộc thiết kế

- **Platform:** {platform}
- **Tech stack:** {stack}
- **Tiêu chuẩn tuân thủ:** {compliance_standard}
