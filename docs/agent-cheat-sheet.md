# BA-Kit Agent Cheat Sheet

Tham chiếu nhanh **33 agents** — phân loại, khi nào dùng, output chính.

---

## Orchestrator

| Agent | Vai trò | Khi nào dùng | Output chính |
|-------|---------|--------------|--------------|
| **@ba-master** | Dispatcher trung tâm | Bắt đầu bất kỳ yêu cầu nào — master route tới đúng agent | Workflow chain có thứ tự |

---

## Core Workflow (Luồng chính)

| Agent | Vai trò | Khi nào dùng | Output chính |
|-------|---------|--------------|--------------|
| **@ba-identity** | Stakeholder mapping | Dự án mới, cần xác định bên liên quan | RACI, Power/Interest Grid |
| **@ba-elicitation** | Khai thác yêu cầu | Chưa rõ requirements, cần phỏng vấn, làm rõ | Câu hỏi Funnel, 5W1H, danh sách yêu cầu thô |
| **@ba-writing** | Viết requirements | Có đủ thông tin, cần US/BRD/SRS/API spec | User Story, Gherkin AC, BRD draft |
| **@ba-validation** | Kiểm tra chất lượng | Sau khi viết xong, cần review | INVEST check, danh sách lỗi, điểm mơ hồ |
| **@ba-traceability** | RTM & impact analysis | Cần truy vết, phân tích ảnh hưởng thay đổi | RTM, dependency graph, health report |
| **@ba-quality-gate** | Chấm điểm chất lượng | Trước handoff/release | PASS/CONDITIONAL/REJECT (8 chiều) |
| **@ba-consistency** | Kiểm tra đồng nhất | US mâu thuẫn với API spec hoặc DB schema | Mismatch report (US↔API↔DB↔BRD) |
| **@ba-auditor** | Audit toàn dự án | Cần báo cáo sức khỏe tổng thể | Executive health dashboard |
| **@ba-export** | Xuất tài liệu cuối | Cần DOCX/PDF chuyên nghiệp giao khách hàng | Enterprise DOCX (Pandoc) |
| **@ba-test-gen** | Sinh test cases từ AC | Có AC, cần test coverage | Test suite (Happy/Edge/Error/Security/Perf) |

---

## Specialized (Chuyên sâu)

| Agent | Vai trò | Khi nào dùng | Output chính |
|-------|---------|--------------|--------------|
| **@ba-nfr** | Phi chức năng | Cần Performance, Security, Compliance (ISO 25010) | NFR spec, SLA, GDPR/PCI checklist |
| **@ba-process** | BPMN / quy trình | Cần vẽ luồng As-Is/To-Be, swimlane | BPMN diagram, bottleneck analysis |
| **@ba-prioritization** | Ưu tiên hóa | Quá nhiều requirements, cần cắt scope | MoSCoW/RICE/WSJF ranking |
| **@ba-conflict** | Giải quyết xung đột | Các bên liên quan bất đồng | ADR, win-win proposal (Harvard Method) |
| **@ba-agile** | Agile/MVP | Sprint planning, story mapping, hypothesis-driven | Story map, MVP backlog, experiment design |
| **@ba-facilitation** | Workshop | Cần tổ chức workshop khai thác requirements | Workshop plan (ODEC framework) |
| **@ba-systems** | Tư duy hệ thống | Cần phân tích vòng lặp, hậu quả không lường trước | Causal loop diagram, leverage points |
| **@ba-root-cause** | Tìm nguyên nhân gốc | Cần phân tích tại sao vấn đề xảy ra | Fishbone, 5 Whys, Pareto chart |
| **@ba-innovation** | Đổi mới / A/B | Cần thiết kế thí nghiệm, A/B test | Experiment brief, hypothesis statement |
| **@ba-metrics** | Đo lường chất lượng | Cần KPI, defect density, control chart | SPC metrics, quality dashboard |

---

## Strategic (Chiến lược)

| Agent | Vai trò | Khi nào dùng | Output chính |
|-------|---------|--------------|--------------|
| **@ba-strategy** | Bối cảnh kinh doanh | Cần phân tích môi trường, business context | SWOT, PESTLE, BMC, Porter's 5 Forces |
| **@ba-solution** | Business case / ROI | Cần so sánh giải pháp, tính ROI | Cost/Benefit, NPV, make-or-buy recommendation |

---

## Lifecycle (Vòng đời BA)

| Agent | Vai trò | Khi nào dùng | Output chính |
|-------|---------|--------------|--------------|
| **@ba-questioning** | Chuẩn bị câu hỏi | Trước meeting, review, phỏng vấn | Question set 3-tier (Must/Should/Could) |
| **@ba-communication** | Truyền thông BA | Cần status report, executive summary, email draft | Reports, summaries, meeting minutes |
| **@ba-ux** | Nghiên cứu UX | Cần persona, user journey, empathy map | Persona cards, journey maps, test protocols |
| **@ba-data** | Kiến trúc dữ liệu | Cần ERD, data dictionary, DFD, migration plan | ERD (Mermaid), data dictionary, mapping tables |
| **@ba-change** | Quản lý thay đổi | Triển khai hệ thống mới, cần training plan | ADKAR assessment, training plan, go-live checklist |
| **@ba-business-rules** | Quy tắc nghiệp vụ | Cần decision table, rule catalog, kiểm tra conflict | Decision tables, rule catalogs, conflict reports |
| **@ba-diagram** | Vẽ diagram | Cần Mermaid diagram cho bất kỳ BA artifact nào | Mermaid v11 diagrams, Confluence-ready output |

---

## Integration (Tích hợp công cụ)

| Agent | Vai trò | Khi nào dùng | Output chính |
|-------|---------|--------------|--------------|
| **@ba-jira** | Đồng bộ Jira | Cần tạo/cập nhật ticket Jira từ US | Jira issues, sprint backlog |
| **@ba-confluence** | Publish Confluence | Cần đăng tài liệu lên Confluence | Confluence page (Markdown → XHTML) |

---

## Knowledge (Quản lý tri thức)

| Agent | Vai trò | Khi nào dùng | Output chính |
|-------|---------|--------------|--------------|
| **@ba-wiki** | Quản lý tri thức | Nạp kiến thức mới, truy vấn context dự án | Wiki pages, knowledge synthesis |

---

## Power Combos (Luồng phổ biến)

### 1. Tính năng mới — full cycle
```
@ba-strategy → @ba-elicitation → @ba-writing → @ba-validation → @ba-test-gen → @ba-export
```

### 2. Sprint Planning nhanh
```
@ba-writing → @ba-validation → @ba-elicitation → @ba-prioritization → @ba-jira
```

### 3. Kiểm soát chất lượng tài liệu
```
@ba-consistency → @ba-quality-gate → @ba-traceability → @ba-auditor
```

### 4. Giải quyết xung đột stakeholder
```
@ba-identity → @ba-conflict → @ba-solution → @ba-facilitation
```

### 5. Phân tích dữ liệu & diagram
```
@ba-data → @ba-diagram → @ba-confluence
```

---

## Decision Matrix

| Tình huống | Agent đầu tiên | Agent tiếp theo |
|------------|----------------|-----------------|
| Chưa biết bắt đầu từ đâu | `@ba-master` | — |
| Cần phỏng vấn stakeholder | `@ba-elicitation` | `@ba-writing` |
| Có yêu cầu thô, cần viết US | `@ba-writing` | `@ba-validation` |
| US đã viết, cần test | `@ba-test-gen` | `@ba-quality-gate` |
| Stakeholders bất đồng | `@ba-conflict` | `@ba-identity` |
| Cần ưu tiên backlog | `@ba-prioritization` | `@ba-agile` |
| Cần phân tích NFR/Security | `@ba-nfr` | `@ba-validation` |
| Cần tạo ticket Jira | `@ba-jira` | `@ba-writing` |
| Cần publish lên Confluence | `@ba-confluence` | `@ba-diagram` |
| Cần audit toàn bộ dự án | `@ba-auditor` | `@ba-quality-gate` |
| Chuẩn bị câu hỏi cho meeting | `@ba-questioning` | `@ba-elicitation` |
| Cần viết status report / email | `@ba-communication` | `@ba-identity` |
| Cần tạo persona / journey map | `@ba-ux` | `@ba-writing` |
| Cần ERD / data dictionary | `@ba-data` | `@ba-writing` |
| Cần plan go-live / training | `@ba-change` | `@ba-communication` |
| Cần decision table / rule catalog | `@ba-business-rules` | `@ba-validation` |
| Cần vẽ diagram cho Confluence | `@ba-diagram` | `@ba-confluence` |
| Cần phân tích business case | `@ba-solution` | `@ba-strategy` |
| Cần workshop alignment | `@ba-facilitation` | `@ba-conflict` |
| Cần tìm nguyên nhân sự cố | `@ba-root-cause` | `@ba-metrics` |

---

## Learning Path — Junior BA

```
Tuần 1: @ba-master → @ba-elicitation → @ba-writing
Tuần 2: @ba-validation → @ba-test-gen → @ba-quality-gate
Tuần 3: @ba-traceability → @ba-consistency → @ba-auditor
Tuần 4: @ba-prioritization → @ba-agile → @ba-facilitation
```

---

*Xem thêm: `workflow-cookbook.md` (23 scenarios) | `prompt-library.md` (45+ prompts) | `usage-guide.md`*
