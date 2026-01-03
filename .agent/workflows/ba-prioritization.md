---
description: Prioritization Techniques - rank features and make trade-off decisions (SKILL-05)
---

# 🟡 SKILL-05: Prioritization Techniques Workflow

## Purpose
Provide structured methods for prioritizing requirements and features using proven frameworks.

## Step 1: Select Prioritization Technique

| Technique | Best For | Complexity | Stakeholders |
|-----------|----------|------------|--------------|
| **MoSCoW** | Quick categorization | Low | Few |
| **Kano Model** | Customer satisfaction | Medium | Many |
| **Value vs Effort** | Resource allocation | Low | Few |
| **WSJF** | SAFe/Lean environments | High | Many |
| **100-Point** | Democratic consensus | Medium | Many |
| **Risk-Based** | Risk mitigation | Medium | Technical |

## Step 2: Apply Selected Technique

### 📊 MoSCoW Method

| Category | Definition | Rule |
|----------|------------|------|
| **M**ust | Critical, non-negotiable | Without it = project failure |
| **S**hould | Important but not vital | Workaround exists if needed |
| **C**ould | Nice to have | Only if time/budget permits |
| **W**on't | Not this time | Explicitly excluded |

**MoSCoW Template:**
```
┌──────────┬───────────────────────────────────────────────────────┐
│ Priority │ Requirements                                          │
├──────────┼───────────────────────────────────────────────────────┤
│ MUST     │ • FR-001: User login                                  │
│          │ • FR-002: Process payment                             │
├──────────┼───────────────────────────────────────────────────────┤
│ SHOULD   │ • FR-003: Email notifications                         │
│          │ • FR-004: Export reports                              │
├──────────┼───────────────────────────────────────────────────────┤
│ COULD    │ • FR-005: Social login                                │
│          │ • FR-006: Dark mode                                   │
├──────────┼───────────────────────────────────────────────────────┤
│ WON'T    │ • FR-007: Mobile app (Phase 2)                        │
│          │ • FR-008: AI chatbot (Future)                         │
└──────────┴───────────────────────────────────────────────────────┘
```

**MoSCoW Decision Questions:**
- "Can the system launch without this?" → If NO = MUST
- "Is there a workaround?" → If YES = SHOULD
- "Will users complain if missing?" → If NO = COULD
- "Is this out of current scope?" → If YES = WON'T

---

### 📈 KANO Model

| Category | Description | Impact |
|----------|-------------|--------|
| **Must-Be** (Basic) | Expected, causes dissatisfaction if absent | ↓ if missing |
| **Performance** (Linear) | More is better, satisfies proportionally | ↑ as increases |
| **Delighter** (Excitement) | Unexpected, creates delight | ↑↑ if present |
| **Indifferent** | Users don't care | No impact |
| **Reverse** | Presence causes dissatisfaction | ↓ if present |

**Kano Questionnaire:**
```
For each feature, ask two questions:

1. Functional: "How would you feel if [feature] IS present?"
2. Dysfunctional: "How would you feel if [feature] IS NOT present?"

Answer options:
• I like it
• I expect it  
• I am neutral
• I can tolerate it
• I dislike it
```

**Kano Evaluation Matrix:**
```
                    DYSFUNCTIONAL (Feature Absent)
                    Like  Expect Neutral Tolerate Dislike
FUNCTIONAL    Like    ?     A      A       A        O
(Feature      Expect  R     I      I       I        M
Present)      Neutral R     I      I       I        M
              Tolerate R    I      I       I        M
              Dislike  R     R      R       R        ?

A = Attractive (Delighter)
O = One-dimensional (Performance)  
M = Must-be (Basic)
I = Indifferent
R = Reverse
? = Questionable
```

---

### ⚖️ Value vs Effort Matrix

```
                    HIGH VALUE
                         │
         ┌───────────────┼───────────────┐
         │   QUICK WINS  │   BIG BETS    │
         │   Do First!   │   Plan Well   │
         │               │               │
LOW      ├───────────────┼───────────────┤      HIGH
EFFORT   │   FILL-INS    │   MONEY PITS  │      EFFORT
         │   Do If Time  │   Avoid!      │
         │               │               │
         └───────────────┼───────────────┘
                         │
                    LOW VALUE
```

**Scoring Template:**
```
┌────────┬─────────────────────────┬───────┬────────┬───────────┐
│ REQ-ID │ Requirement             │ Value │ Effort │ Priority  │
│        │                         │ (1-5) │ (1-5)  │ (V/E)     │
├────────┼─────────────────────────┼───────┼────────┼───────────┤
│ FR-001 │ User authentication     │   5   │   2    │ 2.5 HIGH  │
│ FR-002 │ Advanced analytics      │   4   │   5    │ 0.8 LOW   │
│ FR-003 │ Email notifications     │   3   │   1    │ 3.0 HIGH  │
│ FR-004 │ Custom themes           │   2   │   4    │ 0.5 LOW   │
└────────┴─────────────────────────┴───────┴────────┴───────────┘

Priority = Value / Effort
Higher ratio = Higher priority
```

---

### 🎯 WSJF (Weighted Shortest Job First) - SAFe

**Formula:**
```
WSJF = Cost of Delay / Job Duration

Cost of Delay = User Value + Time Criticality + Risk Reduction

Scale: Use Fibonacci (1, 2, 3, 5, 8, 13, 21)
```

**WSJF Template:**
```
┌────────┬───────────┬───────┬───────┬──────────┬────────┬───────┐
│ Feature│ User      │ Time  │ Risk  │ Cost of  │ Job    │ WSJF  │
│        │ Value     │ Crit. │ Reduc.│ Delay    │ Size   │       │
├────────┼───────────┼───────┼───────┼──────────┼────────┼───────┤
│ Epic A │    8      │   5   │   3   │    16    │   5    │ 3.2   │
│ Epic B │    5      │   8   │   2   │    15    │   3    │ 5.0 ⬆│
│ Epic C │   13      │   2   │   1   │    16    │   8    │ 2.0   │
│ Epic D │    3      │   3   │   8   │    14    │   2    │ 7.0 ⬆│
└────────┴───────────┴───────┴───────┴──────────┴────────┴───────┘

Higher WSJF = Do First
```

**WSJF Component Definitions:**
- **User/Business Value**: Revenue impact, user satisfaction
- **Time Criticality**: Deadline pressure, market window
- **Risk Reduction/Opportunity Enablement**: Reduces risk or enables future work
- **Job Size**: Relative effort (proxy for duration)

---

### 💯 100-Point Method

**Process:**
1. Each stakeholder receives 100 points
2. Stakeholders distribute points across features
3. Features are ranked by total points

**Template:**
```
┌─────────────────────────┬─────────┬─────────┬─────────┬───────┐
│ Feature                 │ User A  │ User B  │ User C  │ TOTAL │
├─────────────────────────┼─────────┼─────────┼─────────┼───────┤
│ Feature 1               │   30    │   25    │   40    │  95   │
│ Feature 2               │   20    │   35    │   20    │  75   │
│ Feature 3               │   25    │   15    │   25    │  65   │
│ Feature 4               │   15    │   20    │   10    │  45   │
│ Feature 5               │   10    │    5    │    5    │  20   │
├─────────────────────────┼─────────┼─────────┼─────────┼───────┤
│ TOTAL                   │  100    │  100    │  100    │ 300   │
└─────────────────────────┴─────────┴─────────┴─────────┴───────┘
```

---

### ⚠️ Risk-Based Prioritization

**Risk Score = Probability × Impact**

```
┌────────┬─────────────────────┬──────┬────────┬───────┬──────────┐
│ REQ-ID │ Requirement         │ Prob │ Impact │ Score │ Priority │
├────────┼─────────────────────┼──────┼────────┼───────┼──────────┤
│ FR-001 │ Payment integration │ High │  High  │   9   │ 1st      │
│ FR-002 │ Data migration      │ Med  │  High  │   6   │ 2nd      │
│ FR-003 │ Reporting           │ Low  │  Med   │   2   │ 4th      │
│ FR-004 │ External API        │ High │  Med   │   6   │ 2nd      │
└────────┴─────────────────────┴──────┴────────┴───────┴──────────┘

Probability: Low=1, Med=2, High=3
Impact: Low=1, Med=2, High=3
```

## Step 3: Decision Guide

| Situation | Recommended Technique |
|-----------|----------------------|
| Quick, small team | MoSCoW |
| Customer-facing product | Kano Model |
| Resource constrained | Value vs Effort |
| SAFe/Scaled Agile | WSJF |
| Need consensus | 100-Point |
| High-risk project | Risk-Based |
| Complex prioritization | Combine multiple |

## Step 4: Facilitation Tips

**Before Session:**
- [ ] Define prioritization criteria upfront
- [ ] Ensure all stakeholders understand the method
- [ ] Prepare feature list with descriptions

**During Session:**
- [ ] Set ground rules (no interrupting, respect opinions)
- [ ] Use timeboxing to prevent endless debate
- [ ] Document rationale for decisions

**After Session:**
- [ ] Circulate results for validation
- [ ] Document any dissenting opinions
- [ ] Review priorities periodically

## Next Steps
After prioritization, proceed to:
- `/ba-conflict` if stakeholders disagree
- `/ba-agile` for backlog grooming
- Template workflows for documentation
