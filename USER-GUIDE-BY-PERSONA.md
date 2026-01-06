# 📚 BA-Kit User Guide by Persona
## Hướng Dẫn Sử Dụng BA-Kit Theo Cấp Độ

<p align="center">
  <img src="assets/logo.png?v=2.2.0" alt="BA-Kit Logo" width="150">
</p>

<div align="center">

**🎯 Learn BA-Kit through a Real-World Example: Attendance System**

**🎯 Học BA-Kit qua Ví dụ Thực tế: Hệ Thống Chấm Công**

</div>

---

## 📋 Table of Contents | Mục Lục

| English | Tiếng Việt |
|---------|------------|
| [Persona Overview](#-persona-overview) | [Tổng Quan Persona](#-persona-overview) |
| [🟢 Beginner: Junior BA](#-beginner-junior-ba) | [🟢 Beginner: BA Mới](#-beginner-junior-ba) |
| [🟡 Intermediate: Senior BA](#-intermediate-senior-ba) | [🟡 Intermediate: BA Giàu Kinh Nghiệm](#-intermediate-senior-ba) |
| [🔵 Advanced: Lead BA/PO](#-advanced-lead-bapo) | [🔵 Advanced: Trưởng Nhóm BA](#-advanced-lead-bapo) |

---

## 🎭 Persona Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         BA-KIT LEARNING PATH                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  🟢 BEGINNER (1-2 years)          Focus: DOING THE WORK RIGHT               │
│  ├── Core Skills: SKILL-02, 03, 12                                          │
│  ├── Goal: Write clear requirements, conduct interviews                     │
│  └── Output: User Stories, Basic SRS                                        │
│                           │                                                 │
│                           ▼                                                 │
│  🟡 INTERMEDIATE (3-5 years)      Focus: DOING THE RIGHT WORK               │
│  ├── + Skills: SKILL-04, 05, 06, 13, 14                                     │
│  ├── Goal: Manage complexity, resolve conflicts, prioritize                 │
│  └── Output: Complete BRD, SRS with NFRs, Data Models                       │
│                           │                                                 │
│                           ▼                                                 │
│  🔵 ADVANCED (5+ years)           Focus: IMPROVING HOW WORK IS DONE         │
│  ├── + Skills: SKILL-17, 18, 19, 20                                         │
│  ├── Goal: Measure, optimize, innovate                                      │
│  └── Output: Business Cases, Process Improvements, SPC                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

# 🟢 BEGINNER: Junior BA
## Cấp Độ Mới Bắt Đầu (1-2 năm kinh nghiệm)

### 🎯 Your Mission | Nhiệm Vụ Của Bạn

| English | Tiếng Việt |
|---------|------------|
| Learn to gather requirements correctly | Học cách thu thập yêu cầu đúng cách |
| Write clear, testable requirements | Viết yêu cầu rõ ràng, có thể kiểm thử |
| Follow established templates | Tuân theo template có sẵn |

### 📚 Skills to Master | Kỹ Năng Cần Thành Thạo

| Skill | Name | Why Important |
|-------|------|---------------|
| **SKILL-02** | Elicitation | Foundation of all BA work |
| **SKILL-03** | Writing Quality | Every requirement must be clear |
| **SKILL-12** | Agile Artifacts | User Stories are industry standard |

---

### 🚀 Step-by-Step: Attendance System (Beginner)

#### Step 1: Stakeholder Interview (SKILL-02)
**Phỏng vấn Stakeholder**

Load workflow: `/ba-elicitation`

```markdown
## Interview Preparation Checklist | Chuẩn Bị Phỏng Vấn

☐ Identify stakeholder role (HR, Manager, Employee?)
  → Xác định vai trò người được phỏng vấn

☐ Prepare 5-7 open questions using 5W1H
  → Chuẩn bị 5-7 câu hỏi mở theo 5W1H

☐ Book 30-45 minute session
  → Đặt lịch 30-45 phút

☐ Prepare note-taking template
  → Chuẩn bị template ghi chú
```

**Example Questions for HR Manager:**

| English | Tiếng Việt | Type |
|---------|------------|------|
| "What is the main problem with current attendance tracking?" | "Vấn đề chính với hệ thống chấm công hiện tại là gì?" | Exploratory |
| "How many employees need to use this system?" | "Bao nhiêu nhân viên sẽ sử dụng hệ thống?" | Clarifying |
| "What happens when an employee forgets to check in?" | "Điều gì xảy ra khi nhân viên quên check-in?" | Probing |
| "So you need a report showing late arrivals daily?" | "Vậy bạn cần báo cáo hiển thị đi trễ hàng ngày?" | Confirming |

---

#### Step 2: Write User Stories (SKILL-03 + SKILL-12)
**Viết User Stories**

Load workflow: `/ba-writing`

**Template:**
```gherkin
As a [ROLE]
I want [ACTION]
So that [BENEFIT]

Acceptance Criteria:
Given [CONTEXT]
When [ACTION]
Then [RESULT]
```

**Example: Check-in Feature**

```gherkin
# English
As an Employee
I want to check in using my phone
So that I can record my arrival time easily

Acceptance Criteria:
Given I am within 100m of office location
When I tap "Check In" button
Then system records current time as my arrival
And shows confirmation with timestamp

# Tiếng Việt
Với vai trò Nhân viên
Tôi muốn check-in bằng điện thoại
Để tôi có thể ghi nhận giờ đến dễ dàng

Tiêu chí chấp nhận:
Cho trước tôi ở trong bán kính 100m văn phòng
Khi tôi nhấn nút "Check In"
Thì hệ thống ghi nhận thời gian hiện tại là giờ đến
Và hiển thị xác nhận kèm timestamp
```

---

#### Step 3: Create Simple Use Case (SKILL-12)
**Tạo Use Case Đơn Giản**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                   USE CASE: UC-001 Check In                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Actor: Employee                                                            │
│  Precondition: Employee has mobile app installed, GPS enabled              │
│                                                                             │
│  Main Flow:                                                                 │
│  1. Employee opens Attendance app                                           │
│  2. System displays current location and time                               │
│  3. Employee taps "Check In" button                                         │
│  4. System validates location is within allowed range                       │
│  5. System records check-in time                                            │
│  6. System displays confirmation message                                    │
│                                                                             │
│  Alternative Flow:                                                          │
│  4a. Location is outside allowed range                                      │
│      → System shows error: "You are not at office location"                 │
│      → Use case ends                                                        │
│                                                                             │
│  Postcondition: Check-in time is recorded in database                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### ✅ Beginner Checklist | Checklist Cho Người Mới

```
☐ Completed at least 3 stakeholder interviews using SKILL-02 techniques
  → Hoàn thành ít nhất 3 buổi phỏng vấn stakeholder

☐ Written 10+ User Stories with proper format (As a/I want/So that)
  → Viết 10+ User Stories đúng format

☐ Created Use Cases for main features
  → Tạo Use Cases cho các tính năng chính

☐ All requirements have Acceptance Criteria
  → Tất cả yêu cầu đều có Tiêu chí chấp nhận

☐ No ambiguous words (fast, easy, user-friendly)
  → Không có từ mơ hồ (nhanh, dễ, thân thiện)
```

---

# 🟡 INTERMEDIATE: Senior BA
## Cấp Độ Trung Cấp (3-5 năm kinh nghiệm)

### 🎯 Your Mission | Nhiệm Vụ Của Bạn

| English | Tiếng Việt |
|---------|------------|
| Manage complex requirements with dependencies | Quản lý yêu cầu phức tạp có phụ thuộc |
| Specify NFRs with measurable criteria | Xác định NFR với tiêu chí đo lường được |
| Resolve stakeholder conflicts | Giải quyết xung đột giữa các stakeholder |
| Prioritize features with business value | Ưu tiên tính năng theo giá trị kinh doanh |

### 📚 Additional Skills | Kỹ Năng Bổ Sung

| Skill | Name | When to Use |
|-------|------|-------------|
| **SKILL-04** | NFR Framework | Performance, Security requirements |
| **SKILL-05** | Prioritization | Feature ranking, MVP definition |
| **SKILL-06** | Conflict Resolution | Stakeholder disagreements |
| **SKILL-13** | Data Modeling | Database design, ERD |
| **SKILL-14** | UX Research | User personas, journey maps |

---

### 🚀 Step-by-Step: Attendance System (Intermediate)

#### Step 1: Define NFRs (SKILL-04)
**Xác Định Yêu Cầu Phi Chức Năng**

Load workflow: `/ba-nfr`

**Using ISO 25010 Framework:**

| Quality Attribute | Requirement | Measure | Target |
|-------------------|-------------|---------|--------|
| **Performance** | Check-in response time | Seconds | < 2s |
| **Performance** | Concurrent users | Users | 500 simultaneous |
| **Reliability** | System uptime | Percentage | 99.5% |
| **Security** | Authentication | Method | Biometric or PIN |
| **Security** | Data encryption | Standard | AES-256 |

**NFR Template (ISO 25010):**

```markdown
## NFR-PERF-001: Check-in Response Time

**Category:** Performance Efficiency > Time Behavior
**Priority:** High

**Requirement:**
The system SHALL complete check-in transaction within 2 seconds 
under normal load conditions.

**Measurement:**
- Tool: Application Performance Monitoring (APM)
- Method: 95th percentile response time
- Sample: 1000 consecutive check-ins

**Acceptance Criteria:**
- P95 response time ≤ 2 seconds
- P99 response time ≤ 5 seconds
- Zero timeout errors under 500 concurrent users
```

---

#### Step 2: Prioritize Features (SKILL-05)
**Ưu Tiên Tính Năng**

Load workflow: `/ba-prioritization`

**MoSCoW Analysis for Attendance MVP:**

| Feature | Must | Should | Could | Won't |
|---------|:----:|:------:|:-----:|:-----:|
| Check-in/Check-out | ✅ | | | |
| GPS Validation | ✅ | | | |
| Leave Request | ✅ | | | |
| Manager Approval | ✅ | | | |
| Monthly Report | | ✅ | | |
| Overtime Request | | ✅ | | |
| Face Recognition | | | ✅ | |
| Payroll Integration | | | ✅ | |
| AI Anomaly Detection | | | | ❌ |

**WSJF Calculation (for SAFe teams):**

| Feature | User Value | Time Criticality | Risk Reduction | Job Size | WSJF |
|---------|:----------:|:----------------:|:--------------:|:--------:|:----:|
| Check-in/out | 10 | 10 | 8 | 3 | 9.3 |
| Leave Request | 8 | 7 | 5 | 5 | 4.0 |
| Monthly Report | 6 | 5 | 3 | 8 | 1.75 |

> **Formula:** WSJF = (User Value + Time Criticality + Risk Reduction) / Job Size

---

#### Step 3: Create Data Model (SKILL-13)
**Thiết Kế Mô Hình Dữ Liệu**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ATTENDANCE SYSTEM ERD                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────────┐        ┌──────────────────┐        ┌──────────────┐      │
│  │  EMPLOYEE    │        │  ATTENDANCE      │        │  LOCATION    │      │
│  ├──────────────┤        ├──────────────────┤        ├──────────────┤      │
│  │ PK emp_id    │───┐    │ PK attendance_id │    ┌───│ PK loc_id    │      │
│  │    name      │   │    │ FK emp_id        │────┘   │    name      │      │
│  │    email     │   └────│ FK loc_id        │        │    latitude  │      │
│  │    dept_id   │        │    check_in_time │        │    longitude │      │
│  │    manager_id│        │    check_out_time│        │    radius_m  │      │
│  └──────────────┘        │    status        │        └──────────────┘      │
│         │                │    source        │                              │
│         │                └──────────────────┘                              │
│         │                                                                  │
│         │                ┌──────────────────┐                              │
│         │                │  LEAVE_REQUEST   │                              │
│         │                ├──────────────────┤                              │
│         └────────────────│ PK request_id    │                              │
│                          │ FK emp_id        │                              │
│                          │ FK approver_id   │                              │
│                          │    leave_type    │                              │
│                          │    start_date    │                              │
│                          │    end_date      │                              │
│                          │    status        │                              │
│                          │    reason        │                              │
│                          └──────────────────┘                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Data Dictionary Extract:**

| Table | Column | Type | Constraints | Description |
|-------|--------|------|-------------|-------------|
| ATTENDANCE | check_in_time | TIMESTAMP | NOT NULL | Exact check-in moment |
| ATTENDANCE | status | ENUM | 'PRESENT','LATE','ABSENT' | Calculated status |
| ATTENDANCE | source | ENUM | 'MOBILE','WEB','DEVICE' | Check-in method |

---

#### Step 4: Resolve Conflicts (SKILL-06)
**Giải Quyết Xung Đột**

Load workflow: `/ba-conflict`

**Scenario: HR vs IT Conflict**

| Stakeholder | Position | Interest |
|-------------|----------|----------|
| **HR** | "We need Face Recognition" | Prevent buddy punching |
| **IT** | "Face Recognition is too complex" | Keep system simple |

**Resolution using Harvard Method:**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CONFLICT RESOLUTION MATRIX                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. SEPARATE POSITIONS FROM INTERESTS                                       │
│     HR's real need: Prevent fraudulent check-ins                            │
│     IT's real need: Manageable implementation scope                         │
│                                                                             │
│  2. GENERATE OPTIONS                                                        │
│     Option A: Full Face Recognition (expensive, complex)                    │
│     Option B: GPS + Photo capture (medium, simpler)                         │
│     Option C: GPS only + Random photo verification (simple, effective)      │
│                                                                             │
│  3. EVALUATE WITH OBJECTIVE CRITERIA                                        │
│     • Implementation time: C < B < A                                        │
│     • Fraud prevention: A > B > C (but C is 80% effective)                 │
│     • Cost: C < B < A                                                       │
│                                                                             │
│  4. RECOMMENDATION                                                          │
│     → Start with Option C for MVP                                           │
│     → Roadmap to Option B in Phase 2 if fraud detected                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### ✅ Intermediate Checklist | Checklist Cho BA Trung Cấp

```
☐ Created NFR specifications with ISO 25010 framework
  → Viết đặc tả NFR theo chuẩn ISO 25010

☐ Prioritized features using MoSCoW or WSJF
  → Ưu tiên tính năng bằng MoSCoW hoặc WSJF

☐ Built ERD with Data Dictionary
  → Xây dựng ERD và Data Dictionary

☐ Successfully resolved at least 1 stakeholder conflict
  → Giải quyết thành công ít nhất 1 xung đột stakeholder

☐ All NFRs have measurable acceptance criteria
  → Tất cả NFR đều có tiêu chí chấp nhận đo lường được
```

---

# 🔵 ADVANCED: Lead BA/PO
## Cấp Độ Nâng Cao (5+ năm kinh nghiệm)

### 🎯 Your Mission | Nhiệm Vụ Của Bạn

| English | Tiếng Việt |
|---------|------------|
| Build Business Case with ROI | Xây dựng Business Case với ROI |
| Measure requirements quality with SPC | Đo lường chất lượng yêu cầu bằng SPC |
| Identify and fix root causes of defects | Xác định và sửa nguyên nhân gốc rễ lỗi |
| Drive continuous process improvement | Thúc đẩy cải tiến quy trình liên tục |

### 📚 Advanced Skills | Kỹ Năng Nâng Cao

| Skill | Name | Process Level |
|-------|------|---------------|
| **SKILL-17** | Solution Evaluation | Advanced |
| **SKILL-18** | Metrics & SPC | Advanced |
| **SKILL-19** | Root Cause Analysis | Advanced |
| **SKILL-20** | Innovation (OID) | Advanced |

---

### 🚀 Step-by-Step: Attendance System (Advanced)

#### Step 1: Build Business Case (SKILL-17)
**Xây Dựng Business Case**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    BUSINESS CASE: ATTENDANCE SYSTEM                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  📊 CURRENT STATE ANALYSIS                                                  │
│  ├── Manual tracking: 2 hours/day HR effort                                 │
│  ├── Error rate: 15% inaccurate records                                     │
│  ├── Payroll disputes: 5/month average                                      │
│  └── Buddy punching estimated: 8% of workforce                              │
│                                                                             │
│  💰 COST-BENEFIT ANALYSIS (3 Years)                                         │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │ COSTS                                           │ Year 1 │ Year 2-3  │  │
│  │ ─────────────────────────────────────────────── │ ────── │ ───────── │  │
│  │ Development                                     │ $80,000│     -     │  │
│  │ Licenses (cloud)                                │ $12,000│ $24,000   │  │
│  │ Training                                        │  $5,000│     -     │  │
│  │ Maintenance                                     │  $8,000│ $16,000   │  │
│  │ ─────────────────────────────────────────────── │ ────── │ ───────── │  │
│  │ TOTAL COST                                      │$105,000│ $40,000   │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │ BENEFITS                                        │ Year 1 │ Year 2-3  │  │
│  │ ─────────────────────────────────────────────── │ ────── │ ───────── │  │
│  │ HR time savings (2h/day × $30 × 250 days)       │ $15,000│ $30,000   │  │
│  │ Reduced payroll errors                          │ $10,000│ $20,000   │  │
│  │ Buddy punching prevention (8% × payroll)        │ $40,000│ $80,000   │  │
│  │ Compliance / audit readiness                    │  $5,000│ $10,000   │  │
│  │ ─────────────────────────────────────────────── │ ────── │ ───────── │  │
│  │ TOTAL BENEFIT                                   │ $70,000│$140,000   │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│  📈 FINANCIAL METRICS                                                       │
│  ├── NPV (3 years, 10% discount): $124,500                                  │
│  ├── ROI: 108%                                                              │
│  ├── Payback Period: 18 months                                              │
│  └── IRR: 42%                                                               │
│                                                                             │
│  ✅ RECOMMENDATION: PROCEED                                                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

#### Step 2: Define Quality KPIs (SKILL-18)
**Xác Định KPI Chất Lượng**

**Requirements Quality Dashboard:**

| KPI | Formula | Target | Current |
|-----|---------|--------|---------|
| **Defect Density** | Defects / Page | < 0.5 | 0.8 |
| **Requirements Volatility** | Changes / Total Reqs | < 15% | 22% |
| **Traceability Coverage** | Traced Reqs / Total | > 95% | 87% |
| **Review Defect Rate** | Defects Found / Hour | 4-8 | 3.2 |

**Control Chart Setup:**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│              DEFECT DENSITY CONTROL CHART                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Defects/Page                                                               │
│      │                                                                      │
│  1.2 ├ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  UCL (Upper Control)      │
│      │                     ×                                                │
│  1.0 ├                                                                      │
│      │         ×                                                            │
│  0.8 ├ ─ ─ × ─ ─ ─ × ─ ─ ─ ─ ─ × ─ ─ ─ × ─ ─ ─ ─  Mean (Target: 0.5)        │
│      │   ×             ×           ×       ×                                │
│  0.5 ├ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  Target                   │
│      │                                                                      │
│  0.2 ├ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  LCL (Lower Control)      │
│      │                                                                      │
│    0 └──────────────────────────────────────────────────────────────────    │
│        Sprint 1   2   3   4   5   6   7   8   9   10                        │
│                                                                             │
│  ACTION: Sprint 4 exceeded UCL → Trigger Root Cause Analysis                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

#### Step 3: Root Cause Analysis (SKILL-19)
**Phân Tích Nguyên Nhân Gốc Rễ**

**Scenario:** High defect rate in Sprint 4 (exceeded UCL)

**5 Whys Analysis:**

| Level | Question | Answer |
|-------|----------|--------|
| **Why 1** | Why did defect rate spike? | Many ambiguous requirements |
| **Why 2** | Why were requirements ambiguous? | Rushed writing due to deadline |
| **Why 3** | Why was there a rushed deadline? | Late stakeholder feedback |
| **Why 4** | Why was feedback late? | No review checkpoint scheduled |
| **Why 5** | Why no checkpoint? | Process didn't mandate it |
| **ROOT CAUSE** | **Missing mandatory review checkpoint in process** |

**Corrective Action:**

```markdown
## CAR-001: Mandatory Review Checkpoint

**Problem:** 40% increase in defect density (Sprint 4)
**Root Cause:** No mandatory stakeholder review before dev handoff

**Corrective Action (Immediate):**
- Add "Stakeholder Review" gate before Sprint Planning
- Require sign-off from at least 2 stakeholders

**Preventive Action (Systemic):**
- Update BA process template with review checkpoint
- Add review reminder in Sprint calendar
- Train all BAs on review protocol

**Success Metric:**
- Defect density returns below UCL within 2 sprints
- Stakeholder sign-off rate: 100%
```

---

#### Step 4: Pilot New Method (SKILL-20)
**Thử Nghiệm Phương Pháp Mới**

**Innovation Proposal: AI-Assisted Requirements Review**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PILOT PLAN: AI REQUIREMENTS CHECKER                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  HYPOTHESIS:                                                                │
│  "Using AI to pre-check requirements will reduce defect density by 30%"    │
│                                                                             │
│  PILOT DESIGN:                                                              │
│  ├── Control Group: Team A (manual review only)                             │
│  ├── Test Group: Team B (AI + manual review)                                │
│  ├── Duration: 4 sprints                                                    │
│  └── Metrics: Defect density, review time, reviewer satisfaction            │
│                                                                             │
│  SUCCESS CRITERIA:                                                          │
│  ├── Defect density reduction: ≥ 25%                                        │
│  ├── Review time increase: ≤ 10%                                            │
│  └── Reviewer satisfaction: No decrease                                     │
│                                                                             │
│  ROI CALCULATION (if successful):                                           │
│  ├── Tool cost: $2,000/year                                                 │
│  ├── Defect fix savings: $15,000/year (30% × current rework cost)          │
│  └── ROI: 650%                                                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### ✅ Advanced Checklist | Checklist Cho BA Cao Cấp

```
☐ Built Business Case with NPV, ROI, Payback calculations
  → Xây dựng Business Case với NPV, ROI, Payback

☐ Established quality KPIs with SPC control charts
  → Thiết lập KPI chất lượng với biểu đồ kiểm soát SPC

☐ Conducted at least 1 formal Root Cause Analysis
  → Thực hiện ít nhất 1 phân tích nguyên nhân gốc rễ

☐ Piloted a process improvement with measurable results
  → Thử nghiệm cải tiến quy trình với kết quả đo lường được

☐ Achieved Cpk ≥ 1.33 for at least 1 quality metric
  → Đạt Cpk ≥ 1.33 cho ít nhất 1 chỉ số chất lượng
```

---

## 📊 Skill Progression Summary | Tổng Kết Lộ Trình

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     BA-KIT SKILL PROGRESSION                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  LEVEL       │ SKILLS              │ OUTPUT                │ CMMI         │
│  ════════════│═════════════════════│═══════════════════════│══════════════│
│  🟢 Beginner │ 02, 03, 12          │ User Stories          │ Level 2-3    │
│              │                     │ Basic Use Cases       │              │
│  ────────────│─────────────────────│───────────────────────│──────────────│
│  🟡 Intermed │ + 04, 05, 06, 13, 14│ Complete BRD/SRS      │ Level 3-4    │
│              │                     │ Data Models, NFRs     │              │
│  ────────────│─────────────────────│───────────────────────│──────────────│
│  🔵 Advanced │ + 17, 18, 19, 20    │ Business Cases        │ Level 4-5    │
│              │                     │ SPC, Process Improv.  │              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🎓 Next Steps | Bước Tiếp Theo

| Your Level | Recommended Action |
|------------|-------------------|
| 🟢 Beginner | Practice with `/ba-elicitation` and `/ba-writing` on a real project |
| 🟡 Intermediate | Learn `/ba-nfr` and `/ba-prioritization`, try `/ba-conflict` |
| 🔵 Advanced | Implement SKILL-18 (SPC) metrics on your current project |

---

<p align="center">
  <strong>BA-Kit v2.0 | BABOK v3 Certified</strong><br>
  <em>From Beginner to Legendary Business Analyst</em>
</p>
