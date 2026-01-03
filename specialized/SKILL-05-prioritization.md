# 🟡 SKILL-05: PRIORITIZATION TECHNIQUES
## Specialized Skill - Requirements Prioritization

---

## 📌 SKILL METADATA

| Attribute | Value |
|-----------|-------|
| **Skill ID** | SKILL-05 |
| **Category** | 🟡 Specialized |
| **Load When** | Prioritizing requirements, trade-off decisions |
| **Dependencies** | SKILL-01, SKILL-02 |
| **Output** | Prioritized backlog, release plan |

---

## 🎯 MỤC ĐÍCH

Skill này cung cấp các **kỹ thuật ưu tiên hóa requirements** để xác định thứ tự triển khai và đưa ra quyết định trade-off.

---

## 🎨 TECHNIQUE OVERVIEW

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PRIORITIZATION TECHNIQUES                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  CATEGORICAL          RANKING              QUANTITATIVE                     │
│  ┌─────────────┐      ┌─────────────┐      ┌─────────────┐                 │
│  │   MoSCoW    │      │   Kano      │      │   WSJF      │                 │
│  │             │      │   Model     │      │   (SAFe)    │                 │
│  └─────────────┘      └─────────────┘      └─────────────┘                 │
│                                                                             │
│  ┌─────────────┐      ┌─────────────┐      ┌─────────────┐                 │
│  │   Value/    │      │   100-Point │      │   Risk-     │                 │
│  │   Effort    │      │   Method    │      │   Value     │                 │
│  └─────────────┘      └─────────────┘      └─────────────┘                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1️⃣ MoSCoW METHOD

### Definition

```
┌─────────────────────────────────────────────────────────────┐
│                    MoSCoW CATEGORIES                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐                                            │
│  │    MUST     │  Không có thì KHÔNG thể go-live            │
│  │    HAVE     │  • Core functionality                      │
│  │             │  • Legal/compliance requirements           │
│  │             │  • ~60% of effort                          │
│  └─────────────┘                                            │
│                                                             │
│  ┌─────────────┐                                            │
│  │   SHOULD    │  Quan trọng nhưng CÓ workaround            │
│  │    HAVE     │  • High business value                     │
│  │             │  • Can delay without major impact          │
│  │             │  • ~20% of effort                          │
│  └─────────────┘                                            │
│                                                             │
│  ┌─────────────┐                                            │
│  │   COULD     │  Nice to have                              │
│  │    HAVE     │  • Enhancement features                    │
│  │             │  • If time/budget permits                  │
│  │             │  • ~10% of effort                          │
│  └─────────────┘                                            │
│                                                             │
│  ┌─────────────┐                                            │
│  │   WON'T     │  Không làm trong release này               │
│  │    HAVE     │  • Explicitly out of scope                 │
│  │  (this time)│  • Deferred to future                      │
│  │             │  • Documented for transparency             │
│  └─────────────┘                                            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Decision Questions

| Category | Ask These Questions |
|----------|---------------------|
| **Must** | "Can we go live without this?" If NO → Must |
| **Should** | "Is there a workaround?" If YES but painful → Should |
| **Could** | "Would users be disappointed without it?" If minor → Could |
| **Won't** | "Can we defer this to next release?" If YES → Won't |

### MoSCoW Template

| REQ-ID | Requirement | MoSCoW | Rationale |
|--------|-------------|--------|-----------|
| FR-001 | User login | **Must** | Cannot use system without auth |
| FR-002 | Password reset | **Should** | Admin can reset manually |
| FR-003 | Social login | **Could** | Convenience only |
| FR-004 | Biometric | **Won't** | Phase 2 feature |

---

## 2️⃣ KANO MODEL

### Understanding Kano Categories

```
                     Satisfaction
                          ▲
                          │        ╱ DELIGHTERS
                          │      ╱   (Excitement)
                          │    ╱     "Wow factor"
                          │  ╱
                          │╱          PERFORMANCE
         ─────────────────┼───────── (One-dimensional)
        Not               │           "More is better"
        Implemented       │                     Fully
                         ╱│                     Implemented
                       ╱  │
                     ╱    │
         BASIC     ╱      │
         (Must-be)        │
         "Expected"       │
                          ▼
                    Dissatisfaction
```

### Kano Categories Explained

| Category | If Present | If Absent | Example |
|----------|------------|-----------|---------|
| **Basic** | No increase in satisfaction | Strong dissatisfaction | Login works, no crashes |
| **Performance** | Satisfaction increases | Dissatisfaction increases | Faster = happier |
| **Delighters** | Strong satisfaction | No effect | Unexpected useful feature |
| **Indifferent** | No effect | No effect | Internal code refactoring |
| **Reverse** | Dissatisfaction | Satisfaction | Unwanted complexity |

### Kano Questionnaire

For each feature, ask TWO questions:

```
FUNCTIONAL Question:
"How would you feel IF the system HAS [feature]?"
( ) I like it
( ) I expect it
( ) I'm neutral
( ) I can tolerate it
( ) I dislike it

DYSFUNCTIONAL Question:
"How would you feel IF the system DOES NOT HAVE [feature]?"
( ) I like it
( ) I expect it
( ) I'm neutral
( ) I can tolerate it
( ) I dislike it
```

### Kano Evaluation Matrix

|  | DYSFUNCTIONAL → |||||
|--|--|--|--|--|--|
| **FUNCTIONAL ↓** | Like | Expect | Neutral | Tolerate | Dislike |
| **Like** | Q | A | A | A | O |
| **Expect** | R | I | I | I | M |
| **Neutral** | R | I | I | I | M |
| **Tolerate** | R | I | I | I | M |
| **Dislike** | R | R | R | R | Q |

*M=Must-be, O=One-dimensional, A=Attractive, I=Indifferent, R=Reverse, Q=Questionable*

---

## 3️⃣ VALUE VS EFFORT MATRIX

### 2x2 Matrix

```
                        VALUE (Business Impact)
                        High
                          ▲
           ┌──────────────┼──────────────┐
           │              │              │
           │   QUICK      │    DO        │
           │   WINS       │    FIRST     │
           │              │              │
           │  Low effort  │  High effort │
           │  High value  │  High value  │
    Low ───┼──────────────┼──────────────┼─── High
    EFFORT │              │              │    EFFORT
           │   DON'T      │   MAJOR      │
           │   DO (or     │   PROJECTS   │
           │   deprioritize)│  (Plan     │
           │              │   carefully) │
           │  Low value   │  Low value   │
           └──────────────┼──────────────┘
                          │
                        Low
                        VALUE
```

### Scoring Guidelines

**Value Score (1-5):**
| Score | Meaning |
|-------|---------|
| 5 | Critical business impact, revenue driver |
| 4 | Significant improvement |
| 3 | Moderate benefit |
| 2 | Minor improvement |
| 1 | Minimal impact |

**Effort Score (1-5):**
| Score | Meaning |
|-------|---------|
| 1 | < 1 day |
| 2 | 1-3 days |
| 3 | 1-2 weeks |
| 4 | 2-4 weeks |
| 5 | > 1 month |

### Value/Effort Template

| REQ-ID | Requirement | Value (1-5) | Effort (1-5) | Ratio | Quadrant |
|--------|-------------|-------------|--------------|-------|----------|
| FR-001 | Auto-save | 4 | 2 | 2.0 | Quick Win |
| FR-002 | AI recommendations | 5 | 5 | 1.0 | Major Project |
| FR-003 | Change font color | 1 | 1 | 1.0 | Don't Do |
| FR-004 | Export to PDF | 4 | 3 | 1.3 | Do First |

---

## 4️⃣ WSJF (Weighted Shortest Job First)

### SAFe Prioritization Formula

```
                    Cost of Delay
        WSJF = ─────────────────────
                    Job Duration

Where:
Cost of Delay = User Value + Time Criticality + Risk Reduction/Opportunity
```

### Scoring Components

| Component | Question | Scale |
|-----------|----------|-------|
| **User/Business Value** | How valuable is this to users/business? | 1-10 |
| **Time Criticality** | How urgent? Does value decay over time? | 1-10 |
| **Risk Reduction** | Does this reduce risk or enable opportunities? | 1-10 |
| **Job Size** | How much effort/time required? | 1-10 |

### WSJF Calculation Template

| Feature | User Value | Time Critical | Risk Reduc. | CoD | Size | WSJF | Rank |
|---------|------------|---------------|-------------|-----|------|------|------|
| Feature A | 8 | 5 | 3 | 16 | 5 | **3.2** | 2 |
| Feature B | 5 | 8 | 5 | 18 | 3 | **6.0** | 1 |
| Feature C | 3 | 3 | 8 | 14 | 8 | **1.75** | 3 |

**Priority Order: B → A → C**

### Fibonacci for Relative Sizing
Use Fibonacci sequence: 1, 2, 3, 5, 8, 13, 21...
- Compare items relatively, not absolutely
- Bigger gaps at higher numbers account for uncertainty

---

## 5️⃣ 100-POINT METHOD

### Process

1. Give stakeholders 100 points
2. They distribute points across requirements
3. Higher points = higher priority
4. Aggregate across all stakeholders

### Template

| Requirement | Stakeholder A | Stakeholder B | Stakeholder C | Total | Rank |
|-------------|---------------|---------------|---------------|-------|------|
| FR-001 | 30 | 25 | 40 | **95** | 1 |
| FR-002 | 25 | 35 | 20 | **80** | 2 |
| FR-003 | 20 | 15 | 25 | **60** | 3 |
| FR-004 | 15 | 15 | 10 | **40** | 4 |
| FR-005 | 10 | 10 | 5 | **25** | 5 |
| **Total** | 100 | 100 | 100 | 300 | |

---

## 6️⃣ RISK-BASED PRIORITIZATION

### Risk-Value Matrix

```
                          RISK
                          High
                            ▲
             ┌──────────────┼──────────────┐
             │              │              │
             │   AVOID or   │   PHASE 1    │
             │   MITIGATE   │   Priority   │
             │              │              │
             │  High Risk   │  High Risk   │
             │  Low Value   │  High Value  │
      Low ───┼──────────────┼──────────────┼─── High
      VALUE  │              │              │   VALUE
             │   PHASE 3    │   PHASE 2    │
             │   or DROP    │   Priority   │
             │              │              │
             │  Low Risk    │  Low Risk    │
             │  Low Value   │  High Value  │
             └──────────────┼──────────────┘
                            │
                          Low
                          RISK
```

### Risk Factors to Consider
- Technical complexity
- Dependency on external systems
- Team experience with technology
- Requirement stability (likely to change?)
- Integration complexity

---

## 📊 PRIORITIZATION DECISION GUIDE

| Situation | Recommended Technique |
|-----------|----------------------|
| Quick categorization | MoSCoW |
| Understanding user needs | Kano Model |
| Resource-constrained decisions | Value/Effort Matrix |
| Agile/SAFe environment | WSJF |
| Multiple stakeholder input | 100-Point Method |
| High uncertainty/complexity | Risk-Based |
| Simple ranking | Pairwise Comparison |

---

## 📋 FACILITATION TIPS

### Before Prioritization Session
- [ ] Define criteria clearly
- [ ] Align on scoring guidelines
- [ ] Prepare requirement summaries
- [ ] Identify decision makers

### During Session
- [ ] Explain technique
- [ ] Use visual aids
- [ ] Time-box discussions
- [ ] Document rationale

### After Session
- [ ] Distribute results
- [ ] Get sign-off
- [ ] Update backlog/plan
- [ ] Review periodically

---

## 🔗 RELATED SKILLS

| For... | Load |
|--------|------|
| Gathering requirements | SKILL-02 |
| Handling disagreements | SKILL-06 |
| Creating backlogs | SKILL-12 |
| Planning releases | SKILL-09, 10, 11 |

---

*Use this skill to make informed decisions about what to build first.*
