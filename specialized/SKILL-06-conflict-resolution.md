# 🟡 SKILL-06: CONFLICT RESOLUTION & NEGOTIATION
## Specialized Skill - Managing Stakeholder Conflicts

---

## 📌 SKILL METADATA

| Attribute | Value |
|-----------|-------|
| **Skill ID** | SKILL-06 |
| **Category** | 🟡 Specialized |
| **Load When** | Stakeholders disagree, requirements conflict |
| **Dependencies** | SKILL-01, SKILL-02 |
| **Output** | Resolved conflicts, documented decisions |

---

## 🎯 MỤC ĐÍCH

Skill này cung cấp **framework và kỹ thuật** để giải quyết xung đột giữa các stakeholders và requirements mâu thuẫn.

---

## ⚡ TYPES OF CONFLICTS

```
┌─────────────────────────────────────────────────────────────┐
│                 REQUIREMENT CONFLICT TYPES                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. CONTRADICTORY REQUIREMENTS                              │
│     └── Two requirements that cannot both be true           │
│     Example: "Auto-save every 30s" vs "Never save without   │
│              user action"                                   │
│                                                             │
│  2. RESOURCE CONFLICTS                                      │
│     └── Limited budget/time, multiple competing needs       │
│     Example: Both Dept A and B want priority                │
│                                                             │
│  3. STAKEHOLDER DISAGREEMENT                                │
│     └── Different opinions on same requirement              │
│     Example: Marketing wants X, Engineering says infeasible │
│                                                             │
│  4. PRIORITY CONFLICTS                                      │
│     └── Everyone thinks their requirement is #1             │
│     Example: All requirements marked "Must Have"            │
│                                                             │
│  5. SCOPE CREEP                                             │
│     └── Continuous additions beyond agreed scope            │
│     Example: "Just one more small feature..."               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔄 CONFLICT RESOLUTION PROCESS

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CONFLICT RESOLUTION WORKFLOW                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Step 1: IDENTIFY                                                           │
│  ├── Recognize conflict early                                               │
│  ├── Document the disagreement clearly                                      │
│  └── Identify all parties involved                                          │
│          │                                                                  │
│          ▼                                                                  │
│  Step 2: ANALYZE                                                            │
│  ├── Understand root cause (positions vs interests)                         │
│  ├── Assess impact of each option                                           │
│  └── Identify constraints and dependencies                                  │
│          │                                                                  │
│          ▼                                                                  │
│  Step 3: GENERATE OPTIONS                                                   │
│  ├── Brainstorm alternative solutions                                       │
│  ├── Look for win-win compromises                                           │
│  └── Evaluate trade-offs objectively                                        │
│          │                                                                  │
│          ▼                                                                  │
│  Step 4: NEGOTIATE                                                          │
│  ├── Facilitate discussion between parties                                  │
│  ├── Present facts objectively                                              │
│  └── Focus on interests, not positions                                      │
│          │                                                                  │
│          ▼                                                                  │
│  Step 5: ESCALATE (if needed)                                               │
│  ├── Escalate to appropriate decision maker                                 │
│  ├── Provide recommendation with rationale                                  │
│  └── Accept and document final decision                                     │
│          │                                                                  │
│          ▼                                                                  │
│  Step 6: DOCUMENT & COMMUNICATE                                             │
│  ├── Record the resolution and reasoning                                    │
│  ├── Update affected requirements                                           │
│  └── Communicate to all stakeholders                                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🤝 PRINCIPLED NEGOTIATION (Harvard Method)

### Four Principles

| Principle | Description | Application |
|-----------|-------------|-------------|
| **Separate People from Problem** | Focus on the issue, not personalities | "The requirement has challenges" NOT "You are wrong" |
| **Focus on Interests, Not Positions** | Understand WHY behind requests | "Why is this feature important to you?" |
| **Generate Options for Mutual Gain** | Create win-win alternatives | "What if we do X instead of Y?" |
| **Use Objective Criteria** | Base decisions on facts/standards | "Industry benchmark shows..." |

### Position vs Interest

```
┌─────────────────────────────────────────────────────────────┐
│              POSITION vs INTEREST EXAMPLE                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Stakeholder A says: "I need a 5-second response time"      │
│                      ↑ This is a POSITION                   │
│                                                             │
│  Ask: "Why do you need 5 seconds?"                          │
│                                                             │
│  Answer: "Users abandon the page if it's slow"              │
│          ↑ This is the INTEREST                             │
│                                                             │
│  Alternative solutions to the interest:                     │
│  • 5-second response time (original position)               │
│  • Loading indicator to keep users engaged                  │
│  • Progressive loading showing partial results              │
│  • Caching for frequently accessed data                     │
│  • Background processing with notification                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Interest Discovery Questions

```
📌 WHY Questions:
• "Why is this requirement important to you?"
• "What problem are you trying to solve?"
• "What would happen if we didn't have this?"

📌 WHAT Questions:
• "What does success look like for you?"
• "What would make this acceptable?"
• "What are you trying to avoid?"

📌 HOW Questions:
• "How would this impact your work?"
• "How are you handling this today?"
• "How flexible is this requirement?"
```

---

## 📊 CONFLICT ANALYSIS TEMPLATE

```
┌─────────────────────────────────────────────────────────────┐
│ CONFLICT ANALYSIS FORM                                      │
├─────────────────────────────────────────────────────────────┤
│ Conflict ID: [CR-XXX]         Date: [YYYY-MM-DD]            │
│ Status: [Open/In Progress/Resolved/Escalated]               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ CONFLICT DESCRIPTION:                                       │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ [Clear description of the conflict]                     │ │
│ └─────────────────────────────────────────────────────────┘ │
│                                                             │
│ PARTIES INVOLVED:                                           │
│ ┌───────────────┬───────────────┬───────────────┐           │
│ │ Party         │ Position      │ Interest      │           │
│ ├───────────────┼───────────────┼───────────────┤           │
│ │ [Name/Role]   │ [What they    │ [Why they     │           │
│ │               │  want]        │  want it]     │           │
│ ├───────────────┼───────────────┼───────────────┤           │
│ │ [Name/Role]   │ [What they    │ [Why they     │           │
│ │               │  want]        │  want it]     │           │
│ └───────────────┴───────────────┴───────────────┘           │
│                                                             │
│ IMPACT ANALYSIS:                                            │
│ • If Party A's position wins: [Impact]                      │
│ • If Party B's position wins: [Impact]                      │
│ • If no resolution: [Impact]                                │
│                                                             │
│ OPTIONS CONSIDERED:                                         │
│ ┌───────────────┬───────────────┬───────────────┐           │
│ │ Option        │ Pros          │ Cons          │           │
│ ├───────────────┼───────────────┼───────────────┤           │
│ │ Option 1      │               │               │           │
│ │ Option 2      │               │               │           │
│ │ Option 3      │               │               │           │
│ └───────────────┴───────────────┴───────────────┘           │
│                                                             │
│ RECOMMENDATION: [Option X]                                  │
│ RATIONALE: [Why this option]                                │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ RESOLUTION:                                                 │
│ Decision: [Final decision]                                  │
│ Decision Maker: [Name/Role]                                 │
│ Date: [YYYY-MM-DD]                                          │
│ Rationale: [Why this decision]                              │
│                                                             │
│ AFFECTED REQUIREMENTS:                                      │
│ • [REQ-ID]: [How it changes]                                │
│ • [REQ-ID]: [How it changes]                                │
│                                                             │
│ COMMUNICATION:                                              │
│ • Notified: [List of people]                                │
│ • Date: [YYYY-MM-DD]                                        │
└─────────────────────────────────────────────────────────────┘
```

---

## 📈 ESCALATION MATRIX

### Escalation Levels

| Level | Decision Maker | Conflict Type | Timeline |
|-------|---------------|---------------|----------|
| **L0** | BA/Facilitator | Minor clarifications | Same meeting |
| **L1** | PM/Scrum Master | Scope/priority within team | 1-2 days |
| **L2** | Product Owner | Feature scope, user needs | 3-5 days |
| **L3** | Steering Committee | Cross-team, budget impact | 1-2 weeks |
| **L4** | Executive Sponsor | Strategic, major scope | 2-4 weeks |

### Escalation Triggers

```
ESCALATE TO NEXT LEVEL WHEN:
□ Parties cannot reach agreement after 2 attempts
□ Conflict affects project timeline/budget
□ Decision requires authority beyond current level
□ Conflict involves multiple departments
□ Risk of significant business impact
```

### Escalation Template

```
TO: [Decision Maker]
FROM: [BA/PM]
DATE: [YYYY-MM-DD]
RE: Escalation - [Conflict Summary]

SITUATION:
[Brief description of conflict]

PARTIES:
• [Party A]: Position [X], Interest [Y]
• [Party B]: Position [X], Interest [Y]

OPTIONS CONSIDERED:
1. [Option A] - [Pros/Cons]
2. [Option B] - [Pros/Cons]
3. [Option C] - [Pros/Cons]

IMPACT:
• Schedule: [Impact]
• Budget: [Impact]
• Quality: [Impact]

RECOMMENDATION:
[Your recommendation with rationale]

DECISION REQUESTED BY: [Date]
```

---

## 🛡️ CONFLICT PREVENTION STRATEGIES

### Proactive Measures

```
┌─────────────────────────────────────────────────────────────┐
│              CONFLICT PREVENTION CHECKLIST                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  BEFORE PROJECT:                                            │
│  ☐ Define clear decision-making authority (RACI)            │
│  ☐ Establish escalation path upfront                        │
│  ☐ Align stakeholders on project goals                      │
│  ☐ Document constraints and boundaries                      │
│                                                             │
│  DURING ELICITATION:                                        │
│  ☐ Include all relevant stakeholders                        │
│  ☐ Document assumptions and get agreement                   │
│  ☐ Surface conflicts early, don't avoid                     │
│  ☐ Validate requirements across stakeholder groups          │
│                                                             │
│  ONGOING:                                                   │
│  ☐ Regular stakeholder alignment meetings                   │
│  ☐ Transparent communication of trade-offs                  │
│  ☐ Change control process in place                          │
│  ☐ Document decisions and rationale                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 💬 FACILITATION PHRASES

### Opening Discussion
```
"I've noticed we have different perspectives on [topic]. 
Let's explore this together to find the best solution."
```

### Understanding Positions
```
"Help me understand - why is [specific aspect] important to you?"
"What problem are you trying to solve with this approach?"
```

### Reframing
```
"It sounds like you both want [common goal]. 
Let's explore different ways to achieve that."
```

### Generating Options
```
"What if we tried [alternative]? Would that address your concern?"
"Are there other ways we could meet both needs?"
```

### Moving Forward
```
"Given the constraints, what would be an acceptable compromise?"
"If we had to choose, what's the most critical aspect for you?"
```

### Closing
```
"Let me summarize what we've agreed: [summary]. 
Does everyone confirm this?"
```

---

## ⚠️ COMMON PITFALLS TO AVOID

| Pitfall | Why It's Bad | Instead |
|---------|--------------|---------|
| Taking sides | Loses trust | Stay neutral, focus on facts |
| Avoiding conflict | Issues fester | Address early and openly |
| Assuming bad intent | Damages relationships | Assume positive intent |
| Seeking "winner" | Creates losers | Seek mutual gain |
| Deciding for them | No ownership | Facilitate their decision |
| Ignoring emotions | Feels dismissive | Acknowledge feelings |

---

## 🔗 RELATED SKILLS

| For... | Load |
|--------|------|
| Better questioning | SKILL-02 |
| Prioritization help | SKILL-05 |
| Documenting decisions | SKILL-07 |
| Validating resolution | SKILL-08 |

---

*Use this skill to transform conflicts into collaborative solutions.*
