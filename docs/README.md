# BA-Kit Documentation

Tài liệu hướng dẫn cho BA-Kit v3.1.0 — 33 agents, 831 knowledge entries, 3 platforms.

---

## Getting Started

| Tài liệu | Mô tả | Đối tượng |
|-----------|-------|-----------|
| [Quick Start](./quick-start.md) | Setup BA-Kit trong 2 phút | Tất cả |
| [Junior Start](./junior-start.md) | Onboarding cho Junior BA | Junior BA |
| [Usage Guide](./usage-guide.md) | Cách sử dụng BA squad đầy đủ | Tất cả |

## Core References

| Tài liệu | Mô tả | Đối tượng |
|-----------|-------|-----------|
| [Agent Cheat Sheet](./agent-cheat-sheet.md) | Bảng tham chiếu nhanh 33 agents | Tất cả |
| [Prompt Library](./prompt-library.md) | 45+ prompts copy-paste sẵn | BA thực hành |
| [Workflow Cookbook](./workflow-cookbook.md) | 23 kịch bản thực tế theo ngành | BA có kinh nghiệm |

## Guides

| Tài liệu | Mô tả | Đối tượng |
|-----------|-------|-----------|
| [AI Foundation for BA](./ai-foundation-for-ba.md) | Nền tảng AI cho Business Analysis | BA mới bắt đầu với AI |
| [AI Tools Guide](./ai-tools-guide.md) | Tích hợp AI tools vào BA workflow | BA muốn dùng AI |
| [Design Prototype Guide](./design-prototype-guide.md) | Tạo prototype UI/UX cho BA | BA + Designer |

## Architecture

| Tài liệu | Mô tả | Đối tượng |
|-----------|-------|-----------|
| [Architecture Decisions](./architecture-decisions.md) | ADRs — quyết định kiến trúc hệ thống | Tech Lead |
| [Antigravity Protocol](./antigravity-protocol.md) | Protocol giao tiếp giữa 33 agents | Developers |
| [Contributing](./contributing.md) | Hướng dẫn đóng góp cho dự án | Contributors |

## Knowledge Base

| Resource | Mô tả |
|----------|-------|
| [`../.agent/data/`](../.agent/data/) | 23 CSV files, 831 knowledge entries |
| [`../.agent/wiki/`](../.agent/wiki/) | Living wiki 2-tier (concepts + decisions) |

## Templates

| Resource | Mô tả |
|----------|-------|
| [`../.agent/templates/`](../.agent/templates/) | 14 BA document templates (BRD, SRS, FRD, etc.) |

---

## Cấu trúc BA-Kit

```
ba-kit-antigravity/
├── .agent/
│   ├── skills/         33 BA agents + connectors (.../SKILL.md)
│   ├── scripts/        Python utilities (search, coverage, docx)
│   ├── data/           23 CSV knowledge base files (831 entries)
│   ├── templates/      14 BA document templates
│   └── wiki/           Living knowledge wiki (2-tier)
├── docs/               Tài liệu hướng dẫn (folder này)
├── ebooks/             BA reference ebooks
└── outputs/            Project outputs
```

## Quick Commands

```bash
# Knowledge search
python3 .agent/scripts/ba_search.py "topic" --domain elicitation
python3 .agent/scripts/ba_search.py "query" --multi-domain

# Coverage checker
python3 .agent/scripts/coverage_checker.py outputs/project-name/
```
