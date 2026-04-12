<p align="center">
  <img src="docs/assets/logo.png?v=3.1.0" alt="BA-Kit Logo" width="200">
</p>

<div align="center">

[**🇬🇧 English**](README.md) | [**🇻🇳 Tiếng Việt**](README.vi.md)

</div>

<p align="center">
  <img src="https://img.shields.io/badge/Phiên%20bản-3.1.0-blue?style=for-the-badge" alt="Phiên bản 3.1.0">
  <img src="https://img.shields.io/badge/Agents-33-green?style=for-the-badge" alt="33 Agents">
  <img src="https://img.shields.io/badge/Nền%20tảng-Antigravity%20%7C%20Claude%20Code%20%7C%20CoWork-orange?style=for-the-badge" alt="3 Nền tảng">
  <img src="https://img.shields.io/badge/Năng%20lực-CMMI%20Level%205%20Enabler-purple?style=for-the-badge" alt="CMMI Level 5 Enabler">
  <img src="https://img.shields.io/badge/Tri%20thức-831%20Entries%20%7C%2023%20Domains-teal?style=for-the-badge" alt="831 Entries">
  <img src="https://img.shields.io/badge/Tích%20hợp-Jira%20%2B%20Confluence-blue?style=for-the-badge" alt="Jira + Confluence">
  <img src="https://img.shields.io/badge/Templates-14-gray?style=for-the-badge" alt="14 Templates">
  <img src="https://img.shields.io/badge/Prompts-48-yellow?style=for-the-badge" alt="48 Prompts">
</p>

<h1 align="center">BA-Kit</h1>
<h3 align="center">Biệt Đội Chuyên Gia Phân Tích Nghiệp Vụ</h3>

---

## BA-Kit là gì?

BA-Kit **không phải là kho prompt**. Đây là một **biệt đội agent** dành cho các nền tảng agentic AI.

Nó thay thế mô hình "một chatbot duy nhất" bằng **33 chuyên gia** — mỗi người có vai trò riêng, bộ công cụ riêng, và Vòng Lặp Phản Tư Hệ thống 2 — chạy trên ba nền tảng:

| Nền tảng | Runtime | Phù hợp nhất cho |
| :--- | :--- | :--- |
| **Antigravity IDE** (Google DeepMind) | Agent Skills + MCP | Power user, đầy đủ toolchain |
| **Claude Code** (Anthropic) | CLI, Git, CI/CD | Kỹ sư, suy luận cấp dự án |
| **Claude CoWork** (Anthropic) | Desktop | BA không kỹ thuật, tổng hợp tài liệu |

---

## Cách Hoạt Động

```
Yêu cầu từ người dùng
         │
         ▼
@ba-master ──── Phân loại + Điều phối ────────────────────────┐
         │                                                       │
         ▼                                                       ▼
Agent Chuyên Gia                                      Chuyển giao ngữ cảnh
  (vd: @ba-writing)                                 (continuity dùng chung)
         │
         ├── Hệ thống 1: Phác thảo kết quả
         │
         ├── Hệ thống 2: DỪNG & PHẢN TƯ
         │     ├── Tôi có đang ảo giác không?
         │     └── Xác minh bằng grep / python / web
         │
         └── Kết quả đã xác minh → Chuyển sang agent tiếp theo
```

---

## Biệt Đội Chuyên Gia (33 Agents)

<details>
<summary><strong>Tổng Chỉ Huy (1)</strong></summary>

| Agent | Vai trò | Năng lực |
| :--- | :--- | :--- |
| **`@ba-master`** | Điều Phối Viên | Chiến lược, Định tuyến, Quản lý Ngữ cảnh |

</details>

<details>
<summary><strong>Core (3) — Nền Tảng</strong></summary>

| Agent | Vai trò | Năng lực |
| :--- | :--- | :--- |
| **`@ba-identity`** | Tham Mưu Trưởng | Ánh xạ Stakeholder, RACI, Bảng Năng lực |
| **`@ba-elicitation`** | Nhà Báo | Kỹ thuật Phỏng vấn Phễu, Colombo Method |
| **`@ba-writing`** | Kiến Trúc Sư | Quét UI Thị giác, Soạn Gherkin (BDD) |

</details>

<details>
<summary><strong>Chuyên Biệt (8) — Các Chuyên Gia</strong></summary>

| Agent | Vai trò | Năng lực |
| :--- | :--- | :--- |
| **`@ba-validation`** | Trưởng QA | QA Thị giác, Phát hiện Edge Case |
| **`@ba-traceability`** | Thư ký CCB | Xác minh bằng Grep, Không ảo giác |
| **`@ba-nfr`** | Kiến Trúc Sư SRE | Tiêu chuẩn ISO 25010 có xác minh web |
| **`@ba-process`** | Bậc Thầy Lean | Thị giác Bảng trắng, Phân tích Lãng phí BPMN |
| **`@ba-prioritization`** | Product Manager | Khung MoSCoW, RICE, WSJF |
| **`@ba-solution`** | Nhà Đầu Tư | ROI & NPV có xác minh Python |
| **`@ba-conflict`** | Nhà Ngoại Giao | Đàm phán Harvard, Soạn ADR |
| **`@ba-export`** | Nhà Xuất Bản | Kiểm tra Compliance, Định dạng Pandoc |

</details>

<details>
<summary><strong>Nâng Cao (3)</strong></summary>

| Agent | Vai trò | Năng lực |
| :--- | :--- | :--- |
| **`@ba-metrics`** | Nhà Khoa học Dữ liệu | Biểu đồ SPC, Mật độ Lỗi, Cpk |
| **`@ba-root-cause`** | Thám Tử | 5 Whys, Fishbone, Phân tích Pareto |
| **`@ba-innovation`** | Nhà Khoa học R&D | A/B Testing, Thiết kế Giả thuyết |

</details>

<details>
<summary><strong>Chiến Lược (4)</strong></summary>

| Agent | Vai trò | Năng lực |
| :--- | :--- | :--- |
| **`@ba-strategy`** | Chiến Lược Gia | PESTLE, SWOT, Business Model Canvas, Porter's 5 Forces |
| **`@ba-facilitation`** | Điều Phối Viên | Thiết kế Workshop, ODEC Framework, Group Dynamics |
| **`@ba-systems`** | Phân Tích Hệ Thống | Stocks & Flows, Điểm Đòn Bẩy, System Archetypes |
| **`@ba-agile`** | Phân Tích Agile | User Story Mapping, MVP Definition, Hypothesis-Driven |

</details>

<details>
<summary><strong>Chất Lượng & Kiểm Toán (4)</strong></summary>

| Agent | Vai trò | Năng lực |
| :--- | :--- | :--- |
| **`@ba-test-gen`** | Kiến Trúc Sư QA | AC → Test Cases 7 loại (BVA, Decision Tables, State Transitions) |
| **`@ba-quality-gate`** | Giám Đốc Chất Lượng | Chấm điểm 8 chiều, 5 cổng: PASS / CONDITIONAL / REJECT |
| **`@ba-consistency`** | Kiểm Toán Tích hợp | Đồng bộ chéo: US ↔ API ↔ DB ↔ BRD |
| **`@ba-auditor`** | Tổng Kiểm Toán | Dashboard sức khỏe dự án + kế hoạch hành động |

</details>

<details>
<summary><strong>Vòng Đời (7)</strong></summary>

| Agent | Vai trò | Năng lực |
| :--- | :--- | :--- |
| **`@ba-questioning`** | Chuyên Gia Phỏng Vấn | Câu hỏi Context-Free, chuẩn bị phỏng vấn, phát hiện giả định |
| **`@ba-communication`** | Chuyên Gia Truyền Thông | Báo cáo trạng thái, tóm tắt điều hành, biên bản họp |
| **`@ba-ux`** | Nghiên Cứu Viên UX | Persona, Journey Map, Empathy Map, JTBD, kiểm thử khả dụng |
| **`@ba-data`** | Kiến Trúc Sư Dữ Liệu | ERD, Data Dictionary, DFD, Data Mapping, Migration |
| **`@ba-change`** | Chuyên Gia Thay Đổi | ADKAR, đánh giá sẵn sàng, kế hoạch đào tạo, Go-Live |
| **`@ba-business-rules`** | Quản Lý Quy Tắc | Decision Table, Decision Tree, Rule Catalog, phát hiện xung đột |
| **`@ba-diagram`** | Visualizer | Mermaid v11 (24+ loại), BA artifact→diagram, Confluence export |

</details>

<details>
<summary><strong>Tích Hợp (2) + Tri Thức (1)</strong></summary>

| Agent | Vai trò | Năng lực |
| :--- | :--- | :--- |
| **`@ba-jira`** | Cầu Nối Jira | Story→Ticket, Sprint Planning, Transport Gate Reflection |
| **`@ba-confluence`** | Cầu Nối Confluence | Markdown→XHTML, Document Import, Version Tracking |
| **`@ba-wiki`** | Quản Lý Tri Thức | Nạp kiến thức 2 tầng, truy vấn wiki, tài liệu sống, quản lý glossary |

</details>

---

## Bắt Đầu Nhanh

**Antigravity IDE**
```bash
cp -r ba-kit/.agent/skills/* ~/.gemini/antigravity/skills/
```

**Claude Code**
```bash
cp -r ba-kit/.agent/skills/* ~/.claude/skills/
```

**Claude CoWork**
```bash
cp -r ba-kit/.agent/skills/* ~/Library/Application\ Support/Claude/skills/
```

Sau đó triệu hồi chuyên gia bất kỳ:
```
@ba-writing Tôi cần spec cho tính năng đăng nhập.
@ba-solution Kiểm tra ROI cho sáng kiến này.
@ba-master Định tuyến yêu cầu này đến đúng chuyên gia.
```

---

## Trí Tuệ Hệ Thống 2

Mọi agent đều chạy **Vòng Lặp Nhận Thức Phản Tư** trước khi trả lời:

1. **Phân tích (Hệ thống 1)** — khớp mẫu nhanh
2. **Phác thảo (Hệ thống 1)** — tạo kết quả ban đầu
3. **Phản tư (Hệ thống 2)** — DỪNG. Tôi có đang ảo giác không? Xác minh bằng `grep` / `python` / web
4. **Kết quả** — câu trả lời đã xác minh, độ chính xác cao

Vòng lặp này tự động giảm ảo giác và phát hiện các giả định ẩn.

---

## Công Cụ Tìm Kiếm Tri Thức

**831 entries** được lập chỉ mục trên **23 domain**, sử dụng BM25+.

```bash
python3 .agent/scripts/ba_search.py "acceptance criteria gherkin"
python3 .agent/scripts/ba_search.py "GDPR compliance" --domain compliance
python3 .agent/scripts/ba_search.py "stakeholder analysis" --multi-domain
python3 .agent/scripts/ba_search.py --stats
```

Domains: `writing` `elicitation` `validation` `nfr` `process` `prioritization` `traceability` `conflict` `solution` `systems` `agile` `identity` `workshop` `innovation` `metrics` `modeling` `ux-research` `business-rules` `integration` `compliance` `communication` `testing` `data-analytics`

---

## Cấu Trúc Repository

```
ba-kit/
├── .agent/skills/          # 33 Agent Skills + 2 Connectors
├── .agent/scripts/         # BM25+ Knowledge Search Engine
├── .agent/data/            # 831 Entries được lập chỉ mục (23 domain)
├── .agent/templates/       # 14 Document Templates (BRD, SRS, FRD, PRD, ...)
├── .agent/wiki/            # Wiki tri thức sống
├── docs/                   # Tài liệu & Hướng dẫn
│   ├── agent-cheat-sheet.md
│   ├── prompt-library.md   # 48 prompt theo workflow phase
│   └── knowledge_base/
├── ebooks/                 # Tri thức từ sách tổng hợp (9 files)
├── README.md
└── README.vi.md
```

---

## Giấy Phép

MIT License. Miễn phí sử dụng cho dự án cá nhân và doanh nghiệp.

---

<p align="center">
  <strong>Antigravity • Claude Code • Claude CoWork</strong><br>
  <em>Code Ít Hơn. Tư Duy Nhiều Hơn.</em>
</p>
