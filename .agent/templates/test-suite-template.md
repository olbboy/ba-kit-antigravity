# Template: Test Suite
Tập hợp test cases cho 1 User Story — đảm bảo coverage toàn diện theo 7 loại kịch bản.

## How to Use
- 1 file = 1 user story's full test coverage. Đặt tên: `TS-{US_ID}.md`.
- Coverage Matrix giúp phát hiện loại test bị thiếu trước khi sprint review.
- Coverage Score = (TC Pass) / (Total TC) × 100%.

---

## Tham chiếu

| Trường | Giá trị |
|--------|---------|
| **TS ID** | TS-{US_ID} |
| **US tham chiếu** | US-{num}: {story_title} |
| **Số AC** | {total_ac} |
| **Tổng TC** | {total_tc} |
| **Ngày cập nhật** | {date} |
| **QA phụ trách** | {qa_name} |

---

## Coverage Matrix

| AC | Happy Path | Edge Case | Error | Security | Performance | Boundary | Concurrency |
|----|-----------|-----------|-------|----------|------------|----------|-------------|
| AC-01 | TC-{n} | TC-{n} | TC-{n} | — | — | — | — |
| AC-02 | TC-{n} | TC-{n} | TC-{n} | TC-{n} | — | — | — |
| AC-{N} | TC-{n} | — | TC-{n} | — | — | TC-{n} | — |

> ✓ = có TC | — = không áp dụng | ✗ = còn thiếu (cần bổ sung)

---

## Danh sách Test Cases

| TC ID | Loại | Mô tả | AC | Priority | Trạng thái |
|-------|------|-------|-----|---------|-----------|
| TC-{US}-01 | Happy Path | {description} | AC-01 | P1 | Not Run |
| TC-{US}-02 | Edge Case | {description} | AC-01 | P2 | Not Run |
| TC-{US}-03 | Error | {description} | AC-02 | P2 | Not Run |
| TC-{US}-04 | Security | {description} | AC-{N} | P1 | Not Run |
| TC-{US}-05 | Boundary | {description} | AC-{N} | P3 | Not Run |

---

## Coverage Score

| Chỉ số | Giá trị |
|--------|--------|
| Tổng TC | {total} |
| TC Pass | {pass} |
| TC Fail | {fail} |
| TC Not Run | {not_run} |
| **Coverage %** | **{score}%** |
| **Mục tiêu** | ≥ 95% |

---

## Kết luận & Rủi ro chưa cover

> {Mô tả các kịch bản chưa được test và lý do (không áp dụng, thiếu data, thiếu môi trường...)}

**Ngưỡng Go/No-Go:** Tất cả P1 Pass + không có P2 Fail chưa được giải thích.
