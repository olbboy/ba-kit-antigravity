# Template: API Integration Contract
Đặc tả hợp đồng API giữa các team/service — nguồn sự thật duy nhất cho tích hợp.

## How to Use
- 1 file = 1 service/module API. Đặt tên: `api-contract-{service}.md`.
- Request/Response samples phải là JSON thực — không dùng pseudo-code.
- Cập nhật ngay khi có breaking change; ghi rõ version và deprecation notice.

---

## Thông tin chung

| Trường | Giá trị |
|--------|---------|
| **Service** | {service_name} |
| **Phiên bản API** | v{N} |
| **Base URL (Prod)** | `{base_url_prod}` |
| **Base URL (Dev)** | `{base_url_dev}` |
| **Ngày cập nhật** | {date} |
| **Owner** | {team_or_person} |

---

## Authentication

| Phương thức | Mô tả |
|------------|-------|
| **Type** | Bearer JWT / API Key / OAuth2 |
| **Header** | `Authorization: Bearer {token}` |
| **Token URL** | `{token_endpoint}` |
| **Scope** | `{required_scopes}` |
| **Expiry** | {N} minutes |

---

## Endpoints

| Method | Path | Mô tả | Auth | US liên quan |
|--------|------|-------|------|-------------|
| GET | `/api/v{N}/{resource}` | {description} | Required | US-{num} |
| POST | `/api/v{N}/{resource}` | {description} | Required | US-{num} |
| PUT | `/api/v{N}/{resource}/{id}` | {description} | Required | US-{num} |
| DELETE | `/api/v{N}/{resource}/{id}` | {description} | Required | US-{num} |

---

## Request / Response Samples

### POST `/api/v{N}/{resource}`

**Request:**
```json
{
  "{field_1}": "{value_1}",
  "{field_2}": {value_2}
}
```

**Response 201:**
```json
{
  "id": "{uuid}",
  "{field_1}": "{value_1}",
  "createdAt": "2025-01-01T00:00:00Z"
}
```

---

## Error Codes

| HTTP Status | Code | Mô tả | Cách xử lý |
|-------------|------|-------|-----------|
| 400 | `VALIDATION_ERROR` | Input không hợp lệ | Hiển thị lỗi từng field |
| 401 | `UNAUTHORIZED` | Token hết hạn / thiếu | Redirect login |
| 403 | `FORBIDDEN` | Không có quyền | Hiển thị permission error |
| 404 | `NOT_FOUND` | Resource không tồn tại | Hiển thị 404 page |
| 409 | `CONFLICT` | Duplicate resource | Thông báo đã tồn tại |
| 422 | `BUSINESS_RULE_VIOLATION` | Vi phạm quy tắc nghiệp vụ | {specific_handling} |
| 500 | `INTERNAL_ERROR` | Lỗi server | Retry + alert team |

---

## Rate Limits

| Endpoint nhóm | Giới hạn | Window | Header trả về |
|--------------|---------|--------|--------------|
| /api/* | {N} req | 1 phút | `X-RateLimit-Remaining` |
| /api/export/* | {N} req | 1 giờ | `X-RateLimit-Remaining` |

---

## Versioning Policy

- **Current:** v{N} (supported đến {date})
- **Deprecated:** v{N-1} (sunset {date} — migration guide: {link})
- **Strategy:** URI versioning `/api/v{N}/`
- **Breaking changes:** Thông báo trước {N} ngày qua {channel}
