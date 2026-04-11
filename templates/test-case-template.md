# Test Case Template

## TC-{MODULE}-{US_NUM}-{CATEGORY}-{SEQ}

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-{MODULE}-{US_NUM}-{CATEGORY}-{SEQ} |
| **User Story** | US-{ID}: {Title} |
| **Category** | Happy Path / Edge Case / Error Case / Security / Concurrency / Data Integrity / Performance |
| **Priority** | P1 (Critical) / P2 (High) / P3 (Medium) / P4 (Low) |
| **Preconditions** | {List all conditions that must be true before test execution} |

### Test Steps

| Step | Action | Input Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | {Action description} | {Specific input values} | {Observable expected outcome} |
| 2 | {Action description} | {Specific input values} | {Observable expected outcome} |
| 3 | {Action description} | {Specific input values} | {Observable expected outcome} |

### Postconditions
- {System state after test execution}
- {Data state after test execution}

### Traceability
| Traces To | Reference |
|-----------|-----------|
| User Story | US-{ID} |
| Acceptance Criteria | AC-{NUM} |
| Business Rule | BR-{NUM} (EAMS §X.Y) |
| API Endpoint | {METHOD} {path} |
| DB Table | {table_name} |

---

## Naming Convention

```
TC-{MODULE}-{US_NUM}-{CATEGORY}-{SEQ}

Where:
  MODULE   = ATTEN, SHIFT, HOL, EMP, CAM, NOTIF, REG, EXPL, APPR, RPT, SYS
  US_NUM   = 01, 02, 03, ...
  CATEGORY = HP (Happy Path), EC (Edge Case), ER (Error), 
             SEC (Security), CC (Concurrency), DI (Data Integrity), 
             PF (Performance)
  SEQ      = 01, 02, 03, ...

Examples:
  TC-ATTEN-01-HP-01   → Attendance Hub, Happy Path, Test #1
  TC-ATTEN-01-EC-03   → Attendance Hub, Edge Case, Test #3
  TC-SHIFT-02-SEC-01  → Shift Config, Security, Test #1
```
