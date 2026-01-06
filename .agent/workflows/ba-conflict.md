---
description: Conflict Resolution & Negotiation - resolve stakeholder disagreements and conflicting requirements (SKILL-06)
---

# 🟡 SKILL-06: Conflict Resolution Workflow

## Purpose
Provide techniques to resolve conflicts among stakeholders and contradictory requirements using principled negotiation.

## Step 1: Identify Conflict Type

| Conflict Type | Description | Example |
|---------------|-------------|---------|
| **Contradictory Requirements** | Two requirements cannot both be true | "Real-time" vs "Batch processing" |
| **Resource Conflict** | Competing for limited resources | Budget, timeline, team capacity |
| **Stakeholder Disagreement** | Different stakeholders want different things | Sales vs Operations priorities |
| **Priority Conflict** | Disagreement on what's most important | Feature A vs Feature B first |
| **Scope Creep** | New requirements threatening timeline | "Can we also add..." |

## Step 2: Apply Conflict Resolution Process

```
┌─────────────────────────────────────────────────────────────┐
│              CONFLICT RESOLUTION WORKFLOW                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. IDENTIFY    →  Recognize conflicting requirements       │
│       │                                                     │
│       ▼                                                     │
│  2. ANALYZE     →  Understand root cause and interests      │
│       │                                                     │
│       ▼                                                     │
│  3. OPTIONS     →  Generate multiple solutions              │
│       │                                                     │
│       ▼                                                     │
│  4. NEGOTIATE   →  Facilitate discussion, find agreement    │
│       │                                                     │
│       ▼                                                     │
│  5. ESCALATE?   →  If unresolved, escalate appropriately    │
│       │                                                     │
│       ▼                                                     │
│  6. DOCUMENT    →  Record decision and rationale            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Step 3: Use Conflict Analysis Template

```
┌─────────────────────────────────────────────────────────────┐
│                 CONFLICT ANALYSIS                           │
├─────────────────────────────────────────────────────────────┤
│ Conflict ID: [CONF-XXX]                                     │
│ Date Identified: [YYYY-MM-DD]                               │
│ Status: [Open/In Discussion/Escalated/Resolved]             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ CONFLICTING REQUIREMENTS:                                   │
│ • Requirement A: [REQ-ID]: [Description]                    │
│ • Requirement B: [REQ-ID]: [Description]                    │
│                                                             │
│ WHY THEY CONFLICT:                                          │
│ [Explain the contradiction or incompatibility]              │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ STAKEHOLDER POSITIONS:                                      │
│                                                             │
│ Stakeholder 1: [Name/Role]                                  │
│ • Position: [What they want]                                │
│ • Interests: [Why they want it - underlying need]           │
│                                                             │
│ Stakeholder 2: [Name/Role]                                  │
│ • Position: [What they want]                                │
│ • Interests: [Why they want it - underlying need]           │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ POSSIBLE OPTIONS:                                           │
│ 1. [Option A - description]                                 │
│    Pros: [Benefits]                                         │
│    Cons: [Drawbacks]                                        │
│                                                             │
│ 2. [Option B - description]                                 │
│    Pros: [Benefits]                                         │
│    Cons: [Drawbacks]                                        │
│                                                             │
│ 3. [Option C - compromise]                                  │
│    Pros: [Benefits]                                         │
│    Cons: [Drawbacks]                                        │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ RESOLUTION:                                                 │
│ Decision: [Selected option]                                 │
│ Rationale: [Why this option was chosen]                     │
│ Decided by: [Who made the decision]                         │
│ Date: [YYYY-MM-DD]                                          │
│ Dissenting opinions: [Any recorded disagreement]            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Step 4: Apply Principled Negotiation (Harvard Method)

### The 4 Principles

**1️⃣ Separate PEOPLE from the PROBLEM**
- Attack the problem, not the person
- Acknowledge emotions
- Build working relationship

**2️⃣ Focus on INTERESTS, not POSITIONS**
| Position | Interest |
|----------|----------|
| "Must be real-time" | Need current data for decisions |
| "Batch is sufficient" | Concerned about system load |

Questions to uncover interests:
- "Why is this important to you?"
- "What problem are you trying to solve?"
- "What would happen if we didn't do this?"

**3️⃣ Generate OPTIONS for mutual gain**
- Brainstorm before deciding
- Look for creative solutions
- Expand the pie before dividing it

**4️⃣ Use OBJECTIVE CRITERIA**
- Industry standards
- Precedent
- Cost/benefit analysis
- Expert opinion
- Legal/regulatory requirements

## Step 5: Use Escalation Matrix

| Level | Escalate When | Decision Maker | Timeframe |
|-------|---------------|----------------|-----------|
| **1** | Minor disagreement | BA + Stakeholders | Same meeting |
| **2** | Cannot agree after discussion | Team Lead / SM | 1-2 days |
| **3** | Impacts timeline/budget | Project Manager | 2-3 days |
| **4** | Cross-functional conflict | Director / VP | 1 week |
| **5** | Strategic conflict | Executive / Sponsor | When needed |

### Before Escalating:
- [ ] All parties have had opportunity to present
- [ ] Options have been explored
- [ ] Impact is clearly documented
- [ ] Recommendation prepared

## Step 6: Apply Conflict Prevention Strategies

### ✅ Prevent Conflicts Before They Start

1. **Early stakeholder mapping** - Know who has what interests
2. **Clear scope definition** - Reduce ambiguity
3. **Regular alignment meetings** - Catch mismatches early
4. **Shared glossary** - Same words = same meaning
5. **Documented decisions** - Avoid revisiting closed topics
6. **Neutral facilitation** - BA stays objective

### ⚠️ Early Warning Signs
- Repeated discussions of the same topic
- Stakeholders missing meetings
- Email threads with multiple CCs
- "We already discussed this"
- Sidebar conversations

## Step 7: Use Facilitation Phrases

### Opening
- "I notice there are different perspectives on this. Let's explore each one."
- "Both requirements have merit. Let's understand the underlying needs."

### Exploring
- "Help me understand why this is important to your team."
- "What problem would this solve for you specifically?"
- "If we couldn't do exactly this, what else might work?"

### Finding Common Ground
- "It sounds like you both want [shared goal]. The difference is [specific point]."
- "What if we considered [alternative] that addresses both concerns?"

### Moving Forward
- "Let's document both options and the trade-offs."
- "Given the constraints, which option best serves the project goals?"

### When Stuck
- "It seems we need more information. Can we [research/prototype/ask sponsor]?"
- "Let's table this for now and revisit with [additional data/person]."

## Step 8: Document Resolution

Every resolved conflict should be documented with:
- Original positions
- Final decision
- Rationale
- Who decided
- Date
- Impact on requirements

## Common Pitfalls to Avoid

| ❌ Don't | ✅ Do Instead |
|----------|---------------|
| Take sides prematurely | Stay neutral, facilitate |
| Ignore emotional aspects | Acknowledge feelings |
| Rush to solution | Understand interests first |
| Let conflicts fester | Address promptly |
| Skip documentation | Record all decisions |
| Assume silence = agreement | Explicitly confirm |

## Step 9: Log the Resolution (Auto-Run)
// turbo
Record the decision for future reference:

```bash
./ba log --id [REQ-ID] --reason "Resolution: [brief summary of decision]"
```

## Step 10: AI Conflict Analysis (Optional, Auto-Run)
// turbo
For complex conflicts, get AI analysis of stakeholder positions:

```bash
python3 tools/gen_prompt.py [conflict_document.md]
```

The AI can provide objective perspective on trade-offs.

## Next Steps
After resolution, proceed to:
- `/ba-writing` to update requirements
- `/ba-traceability` to document decision
- `/ba-validation` for stakeholder sign-off
