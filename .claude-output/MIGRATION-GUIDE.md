# BA-Kit Migration Guide: Antigravity to Claude Code

## Installation

1. Copy `.claude-output/CLAUDE.md` to project root `CLAUDE.md`
2. Copy `.claude-output/skills/` to `.claude/skills/`
3. Copy `.claude-output/.mcp.json` to project root `.mcp.json`
4. Copy `.claude-output/settings.json` to `.claude/settings.json`
5. Keep `templates/`, `docs/`, `ebooks/` as-is (no changes needed)

## Verify

```bash
# Check all skills registered
ls .claude/skills/ba-*/SKILL.md | wc -l  # expect: 20 (19 agents + 1 search)

# Test knowledge search
python3 .claude/skills/ba-kit-search/scripts/ba_search.py --stats

# Test a skill (in Claude Code CLI)
/ba-writing "Write a user story for login"
```

## Key Differences: Antigravity vs Claude Code

| Feature | Antigravity | Claude Code |
|---------|-------------|-------------|
| Invoke agent | `@ba-writing` | `/ba-writing` |
| Tool: Python | `run_command(python)` | Bash tool: `python3 -c "..."` |
| Tool: Search | `grep_search` | Grep tool |
| Tool: Web | `search_web` | WebSearch tool |
| Tool: Files | `write_to_file` | Write tool |
| MCP | SSE bridge (index.js) | Direct stdio (.mcp.json) |
| Knowledge | `python3 .agent/scripts/ba_search.py` | `python3 .claude/skills/ba-kit-search/scripts/ba_search.py` |

## Gotchas

1. Claude Code loads CLAUDE.md automatically — no need for CONTINUITY.md (use CLAUDE.md instead)
2. Skills are auto-discovered from `.claude/skills/` — no registration needed
3. MCP bridge is unnecessary — Claude Code connects to MCP servers directly via stdio
4. Settings.json permissions pre-approve common tools to reduce confirmation prompts
