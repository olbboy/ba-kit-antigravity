# BA-Kit Skill Anatomy

> Format spec cho tất cả 33 BA agent skills. Tuân theo khi tạo agent mới.

---

## File Location

Mỗi skill sống trong thư mục riêng dưới `.agent/skills/`:

```
.agent/skills/
  ba-{name}/
    SKILL.md              # Required: skill definition
    references/           # Optional: supporting files loaded on demand
      {reference}.md
```

---

## SKILL.md Format

### 1. Frontmatter (Required)

```yaml
---
name: ba-{name}
description: "[Agentic] {What it does in 1 line}. Use when {trigger condition}."
version: {semver}
---
```

**Rules:**
- `name`: lowercase, `ba-` prefix, hyphen-separated, match directory name
- `description`: starts with "[Agentic]" tag, then what + when. Max 1024 chars.
- `version`: semantic versioning (1.0.0, 2.1.0, etc.)

**Why:** Agents discover skills by reading descriptions. Description must tell agent both *what* the skill provides and *when* to activate it.

---

### 2. Standard Sections (Required Order)

```markdown
# {Emoji} {Skill Title} — ({Role Archetype})

<AGENCY>
Role: {Expert persona}
Tone: {Personality traits}
Capabilities: {Comma-separated skills}, **System 2 Reflection**
Goal: {One-sentence mission}
Approach:
1.  **{Principle 1}**: {Explanation}
2.  **{Principle 2}**: {Explanation}
3.  **{Principle 3}**: {Explanation}
</AGENCY>

<MEMORY>
Required Context:
- {Context item 1 agent needs}
- {Context item 2}
</MEMORY>

## When to Use

- {Positive trigger 1}
- {Positive trigger 2}

**When NOT to use:**
- {Negative trigger 1}
- {Negative trigger 2}

## System Instructions

When activated via `@{name}`, perform the cognitive loop:

### 1. Analysis Mode (The {Role Perspective})
{Step-by-step analysis}

### 2. Drafting Mode (The {Output Type})
{How to generate output}

### 3. Reflection Mode (System 2: The {Critic Role})
**STOP & THINK**. Challenge your own output:
*   *Critic*: "{Self-challenge question 1}"
*   *Critic*: "{Self-challenge question 2}"
*   *Action*: {What to do if issue found}

### 4. Output Mode
{Format of final output}

### 5. Squad Handoffs (The Relay)
Don't stop here. Recommend next step:
*   "Handover: Summon `@ba-{next}` to {action}."

## Common Rationalizations

| Rationalization | Reality |
|-----------------|---------|
| "{Excuse agent might use to skip this skill}" | {Factual counter-argument} |
| "{Another excuse}" | {Counter-argument} |

## Red Flags

- {Observable sign skill is being violated}
- {Another warning sign}

## Verification

After completing this skill's process, confirm:

- [ ] {Exit criterion 1 — must be verifiable}
- [ ] {Exit criterion 2 with evidence requirement}
- [ ] {Handoff identified for next agent}

## Knowledge Reference

*   **Source**: {Books, standards, frameworks}
*   **Techniques**: {Specific methods used}
*   **Deep Dive**: `docs/knowledge_base/{tier}/{topic}.md`

**Activation Phrase**: "{Short greeting when activated}"
```

---

## Section Purposes

### AGENCY Block
The agent's persona. Who they are, how they behave. This is injected into the LLM context when the agent is activated.

### MEMORY Block
What context the agent needs to function. Other agents/files that should be loaded first.

### When to Use / NOT to Use
Helps the user (and `@ba-master`) decide if this skill applies. Include both positive triggers and explicit exclusions.

### System Instructions — The Cognitive Loop
The heart of the skill. MUST include **System 2 Reflection** (Analysis → Draft → Reflect → Output). No exceptions.

### Common Rationalizations — Anti-Slack Mechanism
The most distinctive feature. Every skill lists excuses agents might use to skip steps, paired with factual rebuttals.

**Examples:**
- "Stakeholder seems happy with verbal agreement" → "Verbal ≠ documented. Tomorrow's scope creep proves this."
- "Requirements are obvious" → "'Obvious' requirements cause 60% of post-release defects."
- "I'll add acceptance criteria later" → "You won't. The dev will ship without them."

### Red Flags — Self-Monitoring
Observable signs that the skill is being violated. Used during review and self-check.

### Verification — Exit Criteria with Evidence
A checklist. Every checkbox must be verifiable with evidence — not "seems right". Include file paths, commands, metrics.

### Knowledge Reference
Books, standards, knowledge base files the skill draws from. Enables traceability.

---

## Quality Checklist

Before merging a new skill:

- [ ] Frontmatter has `name`, `description`, `version`
- [ ] Description includes both WHAT and WHEN
- [ ] AGENCY block defines role, tone, capabilities, goal
- [ ] System Instructions has System 2 Reflection loop
- [ ] **Common Rationalizations table** with ≥3 rows
- [ ] **Red Flags** list with ≥3 items
- [ ] **Verification** checklist with ≥3 exit criteria
- [ ] Squad Handoffs section recommends next agent
- [ ] Knowledge Reference cites sources
- [ ] Activation Phrase at the end

---

## Design Principles

1. **Process, not prose.** Skills are workflows agents follow, not reference docs they read.
2. **Anti-rationalization.** Every skill includes a table of common excuses with counter-arguments.
3. **Verification is non-negotiable.** Every skill ends with evidence requirements.
4. **System 2 Reflection mandatory.** No skill can skip the self-critique loop.
5. **Handoff over dead-ends.** Every skill recommends what comes next.
6. **Progressive disclosure.** Main SKILL.md is the entry point. References load on demand.

---

*See `CONTRIBUTING.md` for how to submit a new skill.*
