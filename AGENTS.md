# BA-Kit Antigravity — Agent Rules

## Project Overview

BA-Kit is a squad of **33 BA Specialists** for Requirements Engineering.
Knowledge engine: BM25+ over 831 entries across 23 domains.
Templates: 14 BA document templates in `.agent/templates/`.

## Agent Squad (invoke via /ba-*)

| Agent | Role |
| :--- | :--- |
| `/ba-master` | Dispatcher — routing & squad planning |
| `/ba-identity` | Chief of Staff — persona & stakeholder mapping |
| `/ba-elicitation` | Journalist — funnel questioning |
| `/ba-writing` | Architect — user stories, Gherkin |
| `/ba-validation` | QA Lead — visual QA, edge cases |
| `/ba-traceability` | CCB Secretary — RTM, impact analysis |
| `/ba-nfr` | SRE Architect — ISO-validated NFRs |
| `/ba-process` | Lean Master — process mapping, waste analysis |
| `/ba-prioritization` | Product Manager — MoSCoW, RICE, WSJF |
| `/ba-solution` | Investor — ROI/NPV analysis |
| `/ba-conflict` | Mediator — Harvard negotiation, ADR |
| `/ba-export` | Publisher — compliance, formatting |
| `/ba-metrics` | Data Scientist — SPC charts, Cpk stats |
| `/ba-root-cause` | Investigator — 5 Whys, Fishbone, Pareto |
| `/ba-innovation` | R&D Scientist — A/B testing, hypothesis design |
| `/ba-strategy` | Strategist — PESTLE, SWOT, BMC |
| `/ba-facilitation` | Facilitator — workshop design, ODEC |
| `/ba-systems` | Systems Analyst — stocks & flows, leverage points |
| `/ba-agile` | Agile Analyst — story mapping, MVP, estimation |
| `/ba-jira` | Jira Bridge — story→ticket transport |
| `/ba-confluence` | Confluence Bridge — markdown→XHTML publishing |
| `/ba-test-gen` | QA Architect — AC → 7-category test cases |
| `/ba-quality-gate` | Quality Officer — 8-dimension quality scoring |
| `/ba-consistency` | Integration Auditor — cross-artifact alignment |
| `/ba-auditor` | Chief Auditor — project health dashboard |
| `/ba-questioning` | Critical Thinker — Paul-Elder framework, assumption surfacing |
| `/ba-communication` | Communicator — status reports, executive summaries |
| `/ba-ux` | UX Analyst — persona, journey mapping, usability testing |
| `/ba-data` | Data Analyst — ERD, data dictionary, DFD, migration |
| `/ba-change` | Change Manager — ADKAR, training needs, go-live |
| `/ba-business-rules` | Rules Engineer — decision tables, rule catalog |
| `/ba-diagram` | Visual Architect — Mermaid v11 (24+ types) |
| `/ba-wiki` | Knowledge Curator — wiki query, living documentation |

## Key Commands

```bash
# Search knowledge base (831 entries, 23 domains)
python3 .agent/skills/ba-kit-search/scripts/ba_search.py "<query>"

# Check US/AC coverage
python3 .agent/skills/ba-kit-search/scripts/coverage_checker.py <file>
```

## Development Principles

- YAGNI / KISS / DRY
- System 2 reflection before every output
- Verify math with Python, verify links with Grep, verify standards with WebSearch
- Never hallucinate file contents — check with Grep/Read

## Documentation Structure

```
.agent/skills/ba-*/SKILL.md   — 44 agent skill files + 2 connectors + 1 meta
.agent/templates/              — 14 BA document templates
.agent/scripts/                — BM25+ search, ba_e2e_test, sprint-spine helpers
.github/workflows/e2e-skills.yml — CI quality gate (Phase 08)
docs/                          — guides, cheat sheet, prompt library, sprint-spine
outputs/mini-app-cham-cong/    — BA showcase reference (12 modules, 53 US)
ebooks/                        — 7 synthesized BA ebooks
```

---

## 2. Documentation Quality Rules

### 2.1 Template Completeness
Every module README must contain:
- [ ] Process Flow diagram (`graph TD`)
- [ ] Use Case diagram (`graph LR`)
- [ ] Metadata table
- [ ] User needs table
- [ ] NFR section

### 2.2 Test Suite Standards
Every test-cases.md must have:
- 7-column format: TC-ID | Category | Precondition | Steps | Input | Expected Result | Priority
- BVA (Boundary Value Analysis) section for numeric fields
- All 7 categories: Happy, Edge, Error, Security, Concurrency, Data, Performance
- Coverage Summary table

### 2.3 Batch Generation Limit
- Generate complex artifacts (test suites, API specs) for **max 3 modules** per session
- Quality degrades with larger batches due to context pressure

---

## 3. Confluence Sync Rules

### 3.1 Environment
- `CONFLUENCE_BASE_URL` and `CONFLUENCE_PAT` must be set in `.env`
- Target space: `CVH` (C-Vision Hub)
- Target instance: CTS Knowledge Hub (kms.cmcts.com.vn) — Data Center

### 3.2 Local vs Confluence Formats
- **Local markdown**: Keep native languages (`json`, `gherkin`, `mermaid`) — VSCode/GitHub renders them
- **Confluence upload**: Use `confluence_xhtml.py` which auto-maps to DC-safe equivalents
- Never manually construct XHTML with `language="json"` or `language="gherkin"`

### 3.3 Post-Upload Checklist
After every bulk upload:
1. Run `validate_rendered_pages()` scan
2. Verify 0 broken pages
3. Spot-check 2-3 pages visually via browser

---

## 4. Agent Skill References

| Skill | Reference Files |
|-------|----------------|
| confluence-connector | `references/confluence-dc-rendering-rules.md`, `scripts/confluence_xhtml.py` |
| ba-diagram | HARD RULES R1-R5 in SKILL.md |
| ba-test-gen | 7-category system, 7-column output format |
| ba-as-built | `.agent/scripts/ba_as_built.py`, 3 drift buckets (spec-only/code-only/both-differ), System 2 citation rule |
| ba-autoreview | Strict-sequential contract: consistency→gate→trace→audit, dual-voice optional, short-circuit on REJECT |
| ba-retro | `.agent/scripts/ba_retro.py`, git-log only, 45min session gap, snapshot to `.ba-kit/retros/` |
| ba-learn | `.agent/scripts/ba_learn.py` with `capture()` API, per-project JSONL, 5 types, PII filter |
| ba-checkpoint | YAML frontmatter + 4-section markdown, storage `~/.ba-kit/projects/{slug}/checkpoints/` |
| ba-challenger | 5-vector attack protocol, max 2 attacks per vector, mitigation-required |
| ba-second-opinion | `.agent/scripts/ba_second_opinion.py`, zero-dep (stdlib urllib), 4 providers (gemini/openai/ollama/manual), canonical prompt |
| ba-baseline | `.agent/scripts/ba_baseline.py`, sha256 hash, append-only history, supersede semantics |
| ba-guard | Shares `ba_baseline.py` script (guard-* sub-commands), 3 modes (off/warn/strict), optional git pre-commit hook |
| ba-shotgun | Pure prompt (no script), 4 modes (stories/ac/priority/emails), ≤ 5 variants, preference capture |

## 5. Sprint Spine (v3.4)

BA-Kit v3.4 introduces a unified 7-phase sprint loop that all agents map into:

**Discover → Elicit → Define → Validate → Prioritize → Publish → Reflect**

- Full spec: `docs/sprint-spine.md`
- Phase mapping per agent lives in the agent registry inside `ba-master/SKILL.md`
- 5 new skills (`ba-as-built`, `ba-autoreview`, `ba-retro`, `ba-learn`, `ba-checkpoint`) added in v3.4 from the gstack distillation analysis
- See `plans/260413-1532-gstack-distillation-implementation/plan.md` for rollout status

## 6. Metrics & State Directories

BA-Kit v3.4 writes runtime state and metrics to the following locations:

| Path | Owner | Purpose |
|------|-------|---------|
| `.ba-kit/metrics/autoreview-{slug}.jsonl` | `@ba-autoreview` | Per-run verdict + findings, consumed by `@ba-retro` |
| `.ba-kit/metrics/gate-rejections.jsonl` | `@ba-quality-gate` (future hook) | Rejection events for trend analysis |
| `.ba-kit/metrics/drift-events.jsonl` | `@ba-as-built` | Per-run drift finding counts |
| `.ba-kit/retros/{slug}-{date}.json` | `@ba-retro` | JSON snapshot for delta comparison |
| `.ba-kit/as-built/last-run.json` | `@ba-as-built` | Incremental run state (last git SHA) |
| `.ba-kit/baselines/manifest.json` | `@ba-baseline` | Active baselines with sha256 + rationale |
| `.ba-kit/baselines/history.jsonl` | `@ba-baseline` | Append-only baseline audit trail |
| `.ba-kit/guard/config.json` | `@ba-guard` | Guard mode + exempt paths |
| `.ba-kit/guard/audit.jsonl` | `@ba-guard` | Every pre-flight check result |
| `~/.ba-kit/projects/{slug}/learnings.jsonl` | `@ba-learn` | Per-project emergent memory |
| `~/.ba-kit/projects/{slug}/checkpoints/*.md` | `@ba-checkpoint` | Session save/resume state |

These directories are created on first run. Add `.ba-kit/` to `.gitignore` if you don't want local metrics tracked.

## 7. Second-Opinion Provider Auto-Detection

`@ba-second-opinion` (and `@ba-autoreview --dual-voice`) detect the review provider in the following strict priority order on each invocation. **No config file needed** — the script honors environment variables.

| Priority | Trigger | Provider | Default model |
|----------|---------|----------|---------------|
| 1 | `--provider <name>` flag (not `auto`) | explicit | as specified |
| 2 | `GEMINI_API_KEY` env var set | `gemini` | `gemini-1.5-pro` |
| 3 | `OPENAI_API_KEY` env var set | `openai` | `gpt-4o` |
| 4 | `OLLAMA_HOST` env var set | `ollama` | `llama3` |
| 5 | none of the above | `manual` | (paste-into-other-tool) |

**Important behaviors:**
- If multiple env vars are set, **GEMINI wins** (priority 2 beats 3 beats 4).
- The default mode is `manual` — works on first run with **zero configuration and zero outbound network calls**. Privacy-safe by default.
- Model overridable per call: `--model gpt-4o-mini` or `--model llama3.1`.
- All providers use `urllib` (Python stdlib only) — **no `pip install` required**.

**To upgrade from manual to API mode**, set ONE of the env vars in your shell rc file (`.zshrc` / `.bashrc`):

```bash
# Option 1: Gemini (recommended — cheap, good for long context)
export GEMINI_API_KEY=...

# Option 2: OpenAI (premium quality, higher cost)
export OPENAI_API_KEY=...

# Option 3: Ollama (privacy-first — fully local, no outbound calls)
export OLLAMA_HOST=http://localhost:11434
```

The next `@ba-autoreview --dual-voice` call auto-uses the upgraded provider.

## 8. Strict CCB Workflow (Optional, for Regulated Projects)

Teams using strict change control (CMMI REQM, regulated industries) can opt into git-level enforcement of `@ba-baseline` after install:

```bash
# Step 1: Install BA-Kit (any host)
./.agent/scripts/setup.sh

# Step 2: Install the git pre-commit hook for baseline enforcement
python3 .agent/scripts/ba_baseline.py guard-install-hook

# Step 3: (Optional) switch ba-guard to strict mode
python3 .agent/scripts/ba_baseline.py guard-enable strict
```

After step 2, every `git commit` runs `ba_baseline.py check --strict-exit`. If any baselined artifact has drifted (sha256 mismatch), the commit is blocked with this message:

> `ba-guard: baselined artifacts drifted. Run @ba-guard check for details.`

To resolve: either revert the unauthorized edit, or run `@ba-baseline supersede --from vN --to vN+1 --rationale "..."` to record a new CCB-approved version.

**This is opt-in only.** The hook is never auto-installed by `setup.sh`. Teams not using strict CCB can ignore steps 2–3 entirely.
