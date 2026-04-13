# BA-Kit Usage Guide — v3.5.0

> 44 specialists, không phải 1 chatbot. Mỗi agent là expert trong một lĩnh vực.

---

## The Squad Model

BA-Kit là **Multi-Agent Expert System** — không phải một AI đơn lẻ. Mỗi trong 44 agents (33 core với anti-rationalization pattern + 11 Sprint Spine agents từ v3.4) được tối ưu hóa cho một vai trò cụ thể, với knowledge base riêng và handoff protocol rõ ràng.

**Nguyên tắc cốt lõi:**
- Gọi đúng agent cho đúng việc → kết quả tốt hơn 10x so với chatbot generic
- Agents handoff cho nhau → không cần lặp lại context
- Mọi agent đều dùng System 2 Reflection trước khi output
- Mọi skill tuân theo `docs/skill-anatomy.md` với `When to Use`, `Common Rationalizations`, `Red Flags`, `Verification`

### 1. 🧠 System 2 Cognition (The Brain)
Standard AI answers instantly (System 1). This is prone to hallucination.
**Our Agents Stop & Think.**
*   **Reflection Loop**: Before speaking, every agent critiques its own draft.
*   **Tool Mandates**: They don't guess math (they use Python). They don't guess links (they use Grep).
*   **Skill-Based**: Each agent is a self-contained "Skill" unit (`.agent/skills/`), ensuring modularity.

### 2. 🤝 Squad Collaboration (The Network)
Agents are no longer isolated. They form a **Collaborative Network (DAG)**.
*   **Old Way**: You call `@ba-writing`. It finishes. You wonder what to do next.
*   **New Way**: `@ba-writing` finishes and *advises you*: "Handover: Summon `@ba-validation` to QA this draft."

### 3. 📒 Mission Log (The Memory)
The Squad shares a "Working Brain" via `CONTINUITY.md` (derived from `.agent/templates/continuity-template.md`).
*   **Problem**: "I told `@ba-elicitation` we are an Agile team, but `@ba-nfr` thinks we are Waterfall."
*   **Solution**: You define the Context ONCE in the Mission Log. All 44 agents read it before acting.

---

## @ba-master — The Dispatcher

Không biết gọi agent nào? Gọi `@ba-master`. Nó phân tích request và route đến đúng specialist.

**Decision matrix:**

| Tình huống | @ba-master routes đến |
|-----------|----------------------|
| "Tôi có ý tưởng nhưng chưa rõ requirements" | `@ba-elicitation` |
| "Cần viết User Story từ meeting notes" | `@ba-writing` |
| "Spec này có vấn đề không?" | `@ba-validation` |
| "Backlog 50 items, cần ưu tiên" | `@ba-prioritization` |
| "Stakeholder đang conflict" | `@ba-conflict` |
| "Cần audit toàn bộ project" | `@ba-auditor` |

---

## Workflow Chains — 3 ví dụ thực tế

### Chain 1: New Feature (đầy đủ)
```
@ba-strategy     → phân tích business context, SWOT
@ba-elicitation  → phỏng vấn stakeholder, SPIN questions
@ba-writing      → viết User Stories + Gherkin ACs
@ba-validation   → review INVEST + SMART + ambiguity
@ba-test-gen     → generate test cases từ ACs
@ba-export       → compile thành DOCX/PDF cho client
```

### Chain 2: Sprint Planning
```
@ba-writing      → viết/refine Stories cho sprint
@ba-validation   → kiểm tra chất lượng từng Story
@ba-prioritization → rank theo WSJF hoặc RICE
@ba-jira         → tạo Jira tickets tự động
```

### Chain 3: Quality Audit
```
@ba-consistency  → check API spec vs User Stories
@ba-quality-gate → chấm điểm BRD theo 8 dimensions
@ba-traceability → trace impact khi requirement thay đổi
@ba-auditor      → executive health dashboard (0-100%)
```

---

## System 2 Reflection

Mọi agent đều thực hiện vòng lặp 4 bước trước khi trả lời:

```
Analysis → Draft → Reflect → Output
```

- **Analysis**: Đọc input, xác định vấn đề thực sự
- **Draft**: Tạo bản nháp đầu tiên
- **Reflect**: Tự phê bình — "Bản nháp này đã đúng chưa? Còn thiếu gì?"
- **Output**: Xuất kết quả đã được kiểm tra

Đây là lý do agents không hallucinate math (dùng Python), không đoán links (dùng Grep).

---

## Context Injection — CONTINUITY.md

Tránh lặp lại context mỗi lần đổi agent:

```bash
# Copy template
cp .agent/templates/continuity-template.md ./CONTINUITY.md

# Điền thông tin project
# Goal: MVP Release Q2 2026
# Platform: Mobile (iOS + Android)
# Team: Agile, 2-week sprints
# Constraints: GDPR compliance required
```

Mọi agent tự động đọc `CONTINUITY.md` trước khi hành động.

---

## Knowledge Engine

| Thông số | Giá trị |
|---------|--------|
| Total entries | 831 |
| Domains | 23 |
| Files | `.agent/data/*.csv` |

**Commands:**

```bash
# Tìm kiếm tổng quát
python3 .agent/scripts/ba_search.py "acceptance criteria best practices"

# Tìm trong domain
python3 .agent/scripts/ba_search.py "gherkin" --domain writing

# Liệt kê domains
python3 .agent/scripts/ba_search.py --list-domains
```

**23 domains:** writing, validation, elicitation, agile, conflict, identity, innovation, metrics, modeling, nfr, prioritization, process, solution, systems, traceability, workshop, ux-research, business-rules, integration, compliance, communication, testing, data-analytics

---

## Diagram Generation

```
@ba-diagram "Vẽ sequence diagram cho luồng checkout payment"
@ba-process  "Convert quy trình As-Is này thành BPMN To-Be"
```

Output: Mermaid syntax — copy paste vào Confluence, Notion, hoặc bất kỳ tool nào hỗ trợ Mermaid.

---

## Project Health Scan

```bash
# Scan coverage tự động
python3 .agent/scripts/coverage_checker.py outputs/<project-folder>/ --verbose

# Executive dashboard
@ba-auditor "Run full health audit — show dashboard"
```

Output: Health Score (0-100%), missing scenarios per US, ambiguous terms.

---

## Tips cho Power Users

1. **Flash switching**: `@ba-writing` → `@ba-nfr` → `@ba-solution` trong cùng một conversation — agents đọc được context của nhau.
2. **Image input**: Kéo screenshot mockup vào chat → `@ba-writing Convert this UI into Field Specifications`.
3. **Hypothesis check**: Đừng đoán ROI — `@ba-solution Calculate NPV if adoption is 5% — use Python`.
4. **Batch review**: `@ba-quality-gate Score these 5 User Stories — one table, 8 dimensions each`.
5. **Conflict resolution**: `@ba-conflict Sales vs Eng are deadlocked — apply Harvard Negotiation Method`.
