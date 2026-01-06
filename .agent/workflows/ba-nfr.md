---
description: NFR Framework with ISO 25010 - specify quality attributes and non-functional requirements (SKILL-04)
---

# 🟡 SKILL-04: NFR Framework Workflow (ISO 25010)

## Purpose
Provide structured templates for specifying Non-Functional Requirements based on the ISO/IEC 25010 quality model.

## Step 1: Understand NFR Categories (ISO 25010)

```
┌─────────────────────────────────────────────────────────────┐
│                  ISO 25010 QUALITY MODEL                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ Functional   │  │ Performance  │  │Compatibility │      │
│  │ Suitability  │  │ Efficiency   │  │              │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  Usability   │  │ Reliability  │  │  Security    │      │
│  │              │  │              │  │              │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐                        │
│  │Maintainability│ │ Portability  │                        │
│  │              │  │              │                        │
│  └──────────────┘  └──────────────┘                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Step 2: Use NFR Templates by Category

### 🚀 PERFORMANCE EFFICIENCY

#### Response Time Template
```
NFR-PERF-[XXX]: Response Time - [Component/Feature]
────────────────────────────────────────────────────────────────
The system SHALL respond to [action type] within:
• [Action 1]: < [X] seconds (95th percentile)
• [Action 2]: < [Y] seconds (95th percentile)
• [Action 3]: < [Z] seconds (95th percentile)

Measured: Under [N] concurrent users
Environment: [Production/Staging]
Tool: [APM tool name]
────────────────────────────────────────────────────────────────
```

#### Throughput Template
```
NFR-PERF-[XXX]: Throughput
────────────────────────────────────────────────────────────────
The system SHALL support:
• Normal load: [X] transactions per minute
• Peak load: [Y] transactions per minute  
• Concurrent users: [Z] simultaneous sessions

Growth capacity: [X]% per year for [N] years
────────────────────────────────────────────────────────────────
```

#### Resource Utilization Template
```
NFR-PERF-[XXX]: Resource Utilization
────────────────────────────────────────────────────────────────
Under normal load, the system SHALL NOT exceed:
• CPU: [X]% average, [Y]% peak
• Memory: [X] GB ([Y]% of available)
• Storage: [X] GB initial, [Y] GB/month growth
• Network: [X] Mbps bandwidth
────────────────────────────────────────────────────────────────
```

### 🔐 SECURITY

#### Authentication Template
```
NFR-SEC-[XXX]: Authentication
────────────────────────────────────────────────────────────────
The system SHALL implement:
• Password policy: [min length, complexity, expiry]
• MFA: [Required for: admin/all/sensitive operations]
• Session timeout: [X] minutes inactivity
• Account lockout: After [N] failed attempts for [M] minutes

Compliance: [OWASP ASVS Level X / Other standard]
────────────────────────────────────────────────────────────────
```

#### Authorization Template
```
NFR-SEC-[XXX]: Authorization
────────────────────────────────────────────────────────────────
The system SHALL implement Role-Based Access Control:

┌──────────┬──────────────────────────────────────────────────┐
│ Role     │ Permissions                                      │
├──────────┼──────────────────────────────────────────────────┤
│ Admin    │ [Full access description]                        │
│ Manager  │ [Manager permissions]                            │
│ User     │ [Standard user permissions]                      │
│ Guest    │ [Limited permissions]                            │
└──────────┴──────────────────────────────────────────────────┘
────────────────────────────────────────────────────────────────
```

#### Data Protection Template
```
NFR-SEC-[XXX]: Data Protection
────────────────────────────────────────────────────────────────
The system SHALL protect data:

At Rest:
• Encryption: [Algorithm, e.g., AES-256]
• Key management: [Approach]

In Transit:
• Protocol: [TLS 1.2+/1.3]
• Certificate: [Requirements]

PII Handling:
• Masking: [Fields and approach]
• Retention: [Period and deletion]
• Audit: [Logging requirements]

Compliance: [GDPR/HIPAA/PCI-DSS/etc.]
────────────────────────────────────────────────────────────────
```

### ⚡ RELIABILITY

#### Availability Template
```
NFR-REL-[XXX]: Availability
────────────────────────────────────────────────────────────────
The system SHALL maintain:
• Availability target: [X]% (e.g., 99.9%)
• Maximum unplanned downtime: [X] hours/year
• Planned maintenance window: [Day/Time UTC]
• Recovery Time Objective (RTO): [X] hours
• Recovery Point Objective (RPO): [X] hours
────────────────────────────────────────────────────────────────
```

#### Disaster Recovery Template
```
NFR-REL-[XXX]: Disaster Recovery
────────────────────────────────────────────────────────────────
The system SHALL implement:
• Backup frequency: [Hourly/Daily incremental, Weekly full]
• Backup retention: [X] days
• Backup location: [Geo-redundant specification]
• DR testing: [Frequency]
• Failover: [Automatic/Manual, time to failover]
────────────────────────────────────────────────────────────────
```

### 👤 USABILITY

#### Accessibility Template
```
NFR-USA-[XXX]: Accessibility
────────────────────────────────────────────────────────────────
The system SHALL comply with:
• Standard: [WCAG 2.1 Level AA]
• Screen reader: [Compatible with NVDA, JAWS, VoiceOver]
• Keyboard navigation: [Full functionality without mouse]
• Color contrast: [Minimum ratio, e.g., 4.5:1]
• Text scaling: [Support up to 200%]
────────────────────────────────────────────────────────────────
```

#### Learnability Template
```
NFR-USA-[XXX]: Learnability
────────────────────────────────────────────────────────────────
The system SHALL be learnable such that:
• New users: Complete [core task] within [X] minutes without training
• Experienced users: Complete [advanced task] within [Y] minutes
• Help: Context-sensitive help available on all screens
• Onboarding: [Guided tour / Tutorial requirements]
────────────────────────────────────────────────────────────────
```

### 🔧 MAINTAINABILITY

#### Logging & Monitoring Template
```
NFR-MNT-[XXX]: Logging & Monitoring
────────────────────────────────────────────────────────────────
The system SHALL log:
• All user actions with: timestamp, user ID, action, result
• All errors with: stack trace, context, severity
• All API calls with: request/response, latency, status

Log retention: [X] days
Log format: [JSON/Structured]
Monitoring: [Health endpoints, alerting thresholds]
────────────────────────────────────────────────────────────────
```

### 🔄 PORTABILITY

#### Deployment Template
```
NFR-PRT-[XXX]: Deployment
────────────────────────────────────────────────────────────────
The system SHALL be deployable on:
• Cloud providers: [AWS, Azure, GCP]
• Container: [Docker, Kubernetes]
• On-premise: [Requirements if applicable]

The system SHALL NOT have vendor lock-in for:
• [Specific services to avoid]
────────────────────────────────────────────────────────────────
```

## Step 3: NFR Elicitation Questions

When gathering NFRs, ask:

### Performance
- "How fast must [operation] complete?"
- "How many users will be concurrent?"
- "What's the expected data volume growth?"

### Security
- "What compliance requirements apply?"
- "Who should have access to what?"
- "How should sensitive data be handled?"

### Reliability
- "What's acceptable downtime?"
- "How quickly must system recover?"
- "How much data loss is acceptable?"

### Usability
- "Who are the users and their skill levels?"
- "Are there accessibility requirements?"
- "How quickly should users learn the system?"

## Step 4: NFR Checklist

```
☐ Performance targets are specific and measurable
☐ Security requirements address CIA (Confidentiality, Integrity, Availability)
☐ Compliance requirements identified
☐ Availability targets defined with SLA
☐ Disaster recovery plan specified
☐ Usability standards referenced (WCAG)
☐ Logging requirements documented
☐ Scalability requirements quantified
☐ All NFRs are testable/verifiable
```

## Step 5: Validate NFR Quality (Auto-Run)
// turbo
Before finalizing NFRs, run the expert linter:

```bash
./ba check [nfr_document.md]
```

## Step 6: AI NFR Review (Auto-Run)
// turbo
Get expert AI review of your NFR document:

```bash
python3 tools/gen_prompt.py [nfr_document.md]
```

Copy the generated prompt and send to AI for architectural quality review.

## Next Steps
After specifying NFRs, proceed to:
- `/ba-srs` or `/ba-frd` for complete documentation
- `/ba-validation` for requirements review
