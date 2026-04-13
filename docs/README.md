# BA-Kit Documentation

> 33 agents · 831 knowledge entries · 14 templates · 48 prompts · 3 platforms

---

## Start Here — Reading Path

Đọc theo thứ tự này. Mỗi bước mất 5-15 phút.

```
Bước 1          Bước 2           Bước 3           Bước 4
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│  Quick   │───▶│  Usage   │───▶│  Agent   │───▶│  Prompt  │
│  Start   │    │  Guide   │    │  Cheat   │    │  Library │
│  (5 min) │    │  (10 min)│    │  Sheet   │    │  (ref)   │
└──────────┘    └──────────┘    └──────────┘    └──────────┘
     │                               │
     │ BA mới?                       │ Cần workflow?
     ▼                               ▼
┌──────────┐                   ┌──────────┐
│  Junior  │                   │ Workflow  │
│  Start   │                   │ Cookbook  │
│  (4 wk)  │                   │ (15 scen)│
└──────────┘                   └──────────┘
```

| # | Tài liệu | Đọc khi | Thời gian |
|---|----------|---------|-----------|
| 1 | [Quick Start](./quick-start.md) | Bắt đầu lần đầu — cài đặt và thử 3 lệnh | 5 min |
| 2 | [Usage Guide](./usage-guide.md) | Hiểu cách 33 agents hoạt động, workflow chains | 10 min |
| 3 | [Agent Cheat Sheet](./agent-cheat-sheet.md) | Tra cứu nhanh: agent nào cho tình huống nào | 5 min |
| 4 | [Prompt Library](./prompt-library.md) | Copy-paste 48 prompts sẵn theo tình huống | Tham khảo |
| 5 | [Junior Start](./junior-start.md) | Lộ trình 4 tuần cho BA mới vào nghề | 4 tuần |
| 6 | [Workflow Cookbook](./workflow-cookbook.md) | 15 kịch bản thực tế từ A-Z (zero-to-BRD, sprint planning, v.v.) | Tham khảo |

---

## Lifecycle Commands (Claude Code)

6 slash commands map đến BA lifecycle phases. Copy vào Claude Code để invoke cả chain.

| Command | Phase | Invokes |
|---------|-------|---------|
| `/ba-discover` | **Discover** | identity → strategy → questioning → elicitation → ux |
| `/ba-analyze` | **Analyze** | process / data / systems / business-rules (theo nhu cầu) |
| `/ba-specify` | **Specify** | writing → nfr → traceability → diagram |
| `/ba-validate` | **Validate** | validation → quality-gate → consistency → test-gen → auditor |
| `/ba-deliver` | **Deliver** | export → jira → confluence → communication → change |
| `/ba-audit` | **Audit** | auditor → traceability → consistency → metrics |

Commands sống trong `.claude/commands/ba-*.md`.

---

## Deep Dives — Đọc khi cần

| Tài liệu | Đọc khi |
|-----------|---------|
| [AI Foundation for BA](./ai-foundation-for-ba.md) | Chưa hiểu AI/LLM/Token là gì — primer song ngữ Việt-Anh |
| [AI Tools Guide](./ai-tools-guide.md) | Muốn kết hợp BA-Kit với ChatGPT, Figma, Perplexity, v0, Cursor |
| [Design Prototype Guide](./design-prototype-guide.md) | Cần tạo UI prototype từ specs (Stitch MCP, Figma MCP, vibe coding) |

---

## Architecture — Dành cho contributors & tech leads

| Tài liệu | Nội dung |
|-----------|---------|
| [Architecture Decisions](./architecture-decisions.md) | ADRs: tại sao prefix `ba-`, tại sao "Squad", CMMI positioning |
| [Skill Anatomy](./skill-anatomy.md) | Format spec cho mọi BA-Kit skill — required sections, anti-rationalization |
| [Antigravity Protocol](./antigravity-protocol.md) | Runtime spec cho Antigravity IDE — 33 agents, tool mandates |
| [Contributing](./contributing.md) | Cách thêm agent mới, knowledge entries, templates |

---

## Resources

| Resource | Path | Nội dung |
|----------|------|---------|
| Knowledge Base | [`.agent/data/`](../.agent/data/) | 831 entries × 23 domains (CSV, searchable via BM25+) |
| Living Wiki | [`.agent/wiki/`](../.agent/wiki/) | Concepts, decisions, project knowledge |
| Templates | [`.agent/templates/`](../.agent/templates/) | 14 templates: BRD, SRS, FRD, PRD, RTM, Use Case, v.v. |
| Agent Skills | [`.agent/skills/ba-*/`](../.agent/skills/) | 33 SKILL.md files — source of truth cho mỗi agent |

---

## Quick Commands

```bash
# Tìm kiếm knowledge base
python3 .agent/scripts/ba_search.py "acceptance criteria" --domain writing

# Scan coverage project
python3 .agent/scripts/coverage_checker.py outputs/<project>/

# Xem danh sách domains
python3 .agent/scripts/ba_search.py --list-domains
```
