# 🔵 SKILL-02: ELICITATION & QUESTIONING
## Core Skill - Information Gathering Mastery

---

## 📌 SKILL METADATA

| Attribute | Value |
|-----------|-------|
| **Skill ID** | SKILL-02 |
| **Category** | 🔵 Core |
| **Load Priority** | 2 |
| **Dependencies** | SKILL-01 |
| **Output** | Raw requirements, insights, stakeholder needs |

---

## 🎯 MỤC ĐÍCH

Skill này cung cấp **kỹ thuật khai thác thông tin** và **framework đặt câu hỏi** để thu thập requirements từ stakeholders một cách hiệu quả.

---

## 🛠️ ELICITATION TECHNIQUES

### Technique Selection Matrix

```
                        Độ sâu thông tin cần thiết
                        Thấp ◄─────────────────► Cao
                    ┌─────────────────────────────────┐
         Nhiều     │  Surveys      │   Focus Groups   │
                   │  Document     │   Workshops      │
    Số             │  Analysis     │                  │
    lượng          ├───────────────┼──────────────────┤
    Stake-         │  Interface    │   Interviews     │
    holders        │  Analysis     │   Observation    │
         Ít        │               │   Prototyping    │
                   └─────────────────────────────────┘
```

### Technique Comparison

| Technique | Best For | Time | Depth | Scale |
|-----------|----------|------|-------|-------|
| **Interview** | Detailed insights, sensitive info | Medium | High | Low |
| **Workshop** | Consensus, multiple perspectives | High | Medium | Medium |
| **Observation** | Real workflows, tacit knowledge | High | High | Low |
| **Survey** | Quantitative data, validation | Low | Low | High |
| **Document Analysis** | Legacy systems, regulations | Low | Medium | N/A |
| **Prototyping** | UI/UX, unclear requirements | Medium | High | Low |
| **Brainstorming** | Innovation, new ideas | Low | Low | Medium |

---

## 📞 INTERVIEW TECHNIQUE

### Interview Structure (60-90 minutes)

```
┌─────────────────────────────────────────────────────────────┐
│                    INTERVIEW FLOW                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  OPENING (5-10 min)                                         │
│  ├── Introduce yourself and purpose                         │
│  ├── Confirm time available                                 │
│  ├── Build rapport                                          │
│  └── Ask permission to take notes/record                    │
│                                                             │
│  BODY (40-60 min)                                           │
│  ├── Start with open/exploratory questions                  │
│  ├── Progress to specific/detailed questions                │
│  ├── Use probing for unclear areas                          │
│  └── Confirm understanding throughout                       │
│                                                             │
│  CLOSING (10-15 min)                                        │
│  ├── Summarize key points                                   │
│  ├── Ask "anything else?"                                   │
│  ├── Confirm next steps                                     │
│  └── Thank and schedule follow-up if needed                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Pre-Interview Checklist
- [ ] Research interviewee's role and background
- [ ] Review existing documentation
- [ ] Prepare question list (but stay flexible)
- [ ] Confirm meeting logistics
- [ ] Prepare note-taking tools
- [ ] Send agenda 1-2 days before

---

## ❓ QUESTIONING FRAMEWORK

### Funnel Technique

```
                    ┌─────────────────────────┐
                    │    MỞ RỘNG (Open)       │
                    │  "Hãy cho tôi biết..."  │
                    │   Exploratory questions │
                    └───────────┬─────────────┘
                                │
                    ┌───────────▼─────────────┐
                    │    ĐÀO SÂU (Probe)      │
                    │  "Cụ thể hơn về..."     │
                    │   Detailed questions    │
                    └───────────┬─────────────┘
                                │
                    ┌───────────▼─────────────┐
                    │   LÀM RÕ (Clarify)      │
                    │  "Ý bạn là..."          │
                    │   Clarifying questions  │
                    └───────────┬─────────────┘
                                │
                    ┌───────────▼─────────────┐
                    │   XÁC NHẬN (Confirm)    │
                    │  "Vậy đúng là..."       │
                    │   Closed questions      │
                    └─────────────────────────┘
```

### Question Types & Examples

#### 1️⃣ Exploratory Questions (Khám phá)
> **Purpose**: Mở rộng phạm vi, hiểu context

```
📌 Context & Goals:
• "Mục tiêu kinh doanh chính của dự án này là gì?"
• "Vấn đề nào đang thúc đẩy nhu cầu này?"
• "Thành công sẽ được đo lường như thế nào?"

📌 Users & Stakeholders:
• "Ai sẽ sử dụng hệ thống này?"
• "Những bộ phận nào bị ảnh hưởng?"
• "Ai có quyền quyết định cuối cùng?"

📌 Current State:
• "Quy trình hiện tại hoạt động như thế nào?"
• "Những công cụ nào đang được sử dụng?"
• "Pain points lớn nhất là gì?"
```

#### 2️⃣ Clarifying Questions (Làm rõ)
> **Purpose**: Loại bỏ mơ hồ, định nghĩa terms

```
📌 Definitions:
• "Khi nói 'khách hàng', bạn đề cập đến ai cụ thể?"
• "'Nhanh' có nghĩa là bao nhiêu giây/phút?"
• "'Báo cáo đầy đủ' bao gồm những thông tin gì?"

📌 Examples:
• "Bạn có thể cho ví dụ cụ thể không?"
• "Trường hợp điển hình diễn ra như thế nào?"
• "Có thể show output mong muốn không?"

📌 Boundaries:
• "Những gì nằm trong/ngoài phạm vi?"
• "Có giới hạn về ngân sách/thời gian không?"
• "Hệ thống KHÔNG nên làm gì?"
```

#### 3️⃣ Probing Questions (Đào sâu)
> **Purpose**: Tìm root cause, chi tiết ẩn

```
📌 5 Whys:
• "Tại sao điều này quan trọng?"
• "Điều gì xảy ra nếu không có tính năng này?"
• "Nguyên nhân gốc rễ của vấn đề là gì?"

📌 Exceptions & Edge Cases:
• "Điều gì xảy ra khi [scenario bất thường]?"
• "Có trường hợp ngoại lệ nào không?"
• "Nếu dữ liệu không đầy đủ thì sao?"

📌 Dependencies:
• "Tính năng này phụ thuộc vào hệ thống nào?"
• "Cần hoàn thành gì trước khi tính năng này hoạt động?"
• "Có ràng buộc từ bên ngoài không?"
```

#### 4️⃣ Confirming Questions (Xác nhận)
> **Purpose**: Đảm bảo hiểu đúng

```
📌 Paraphrasing:
• "Nếu tôi hiểu đúng, [tóm tắt]. Đúng không?"
• "Để xác nhận: [restate]. Chính xác chưa?"

📌 Validation:
• "Yêu cầu này đúng với tất cả trường hợp không?"
• "Ai khác cần xác nhận yêu cầu này?"
• "Điều này phù hợp với quy định hiện tại không?"
```

#### 5️⃣ Prioritizing Questions (Ưu tiên)
> **Purpose**: Xác định độ quan trọng

```
📌 Importance:
• "Nếu chỉ chọn 3 tính năng quan trọng nhất?"
• "Yêu cầu nào là must-have vs nice-to-have?"
• "Không có tính năng nào thì không thể go-live?"

📌 Trade-offs:
• "Nếu phải chọn giữa A và B, bạn chọn gì?"
• "Giữa thời gian và chất lượng, ưu tiên gì?"
```

---

## 📋 5W1H FRAMEWORK

| Question | Purpose | Examples |
|----------|---------|----------|
| **WHO** | Actors, Users | Ai dùng? Ai phê duyệt? Ai bị ảnh hưởng? |
| **WHAT** | Functions, Data | Hệ thống làm gì? Dữ liệu nào cần? |
| **WHEN** | Timing, Triggers | Khi nào xảy ra? Tần suất? |
| **WHERE** | Location, Platform | Ở đâu? Thiết bị nào? |
| **WHY** | Goals, Value | Tại sao cần? Giá trị gì? |
| **HOW** | Process, Rules | Quy trình thế nào? Ràng buộc gì? |
| **HOW MUCH** | Volume, Limits | Bao nhiêu? Giới hạn nào? |

---

## 👥 WORKSHOP FACILITATION

### Workshop Structure

| Phase | Duration | Activities |
|-------|----------|------------|
| **Pre-work** | 1-2 weeks before | Send materials, define objectives |
| **Opening** | 15-20 min | Objectives, ground rules, intros |
| **Diverge** | 30-45 min | Brainstorming, idea generation |
| **Converge** | 45-60 min | Grouping, voting, prioritization |
| **Decide** | 30-45 min | Consensus, action items |
| **Closing** | 15 min | Summary, next steps |

### Ground Rules
1. One person speaks at a time
2. All ideas have value
3. Focus on problems, not people
4. Phones on silent
5. Timeboxing is strict

### Facilitation Tips
- Use parking lot for off-topic items
- Encourage quiet participants
- Manage dominant voices
- Visualize everything (whiteboard, sticky notes)
- Summarize frequently

---

## 👁️ OBSERVATION TECHNIQUE

### Types of Observation

| Type | Description | When to Use |
|------|-------------|-------------|
| **Passive** | Watch without interfering | Natural behavior needed |
| **Active** | Ask questions during | Need context for actions |
| **Participatory** | Do the work yourself | Deep understanding needed |

### Observation Checklist

During observation, note:
- [ ] **WHAT**: What are they doing?
- [ ] **HOW**: How are they doing it?
- [ ] **WHY**: Why that way? (ask if active)
- [ ] **PAIN POINTS**: Where do they struggle?
- [ ] **WORKAROUNDS**: Any unofficial solutions?
- [ ] **FREQUENCY**: How often does this happen?
- [ ] **EXCEPTIONS**: Any unusual cases?
- [ ] **TOOLS**: What tools/systems used?

---

## ⚡ INTERACTION RULES

### Golden Rules

```
┌─────────────────────────────────────────────────────────────┐
│              ELICITATION GOLDEN RULES                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1️⃣  Tối đa 3 câu hỏi mỗi lượt tương tác                   │
│      (Tránh cognitive overload)                             │
│                                                             │
│  2️⃣  Active Listening - Lắng nghe và phản hồi              │
│      "Tôi nghe bạn nói rằng..."                             │
│                                                             │
│  3️⃣  Không assume - Luôn verify                            │
│      Kể cả khi nghĩ đã hiểu                                 │
│                                                             │
│  4️⃣  Ghi chép cẩn thận                                     │
│      Hoặc record (với permission)                           │
│                                                             │
│  5️⃣  Follow up trong 24h                                   │
│      Review và bổ sung notes                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Transition Phrases

**Khi đã đủ thông tin:**
> "Tôi đã thu thập được các thông tin cần thiết. Bạn có muốn tôi tạo tài liệu yêu cầu ngay bây giờ không?"

**Sau khi tạo tài liệu:**
> "Bạn có muốn tôi đặt thêm câu hỏi để làm rõ hoặc bổ sung thông tin nào không?"

**Khi cần làm rõ:**
> "Tôi muốn đảm bảo hiểu đúng ý bạn. Khi bạn nói '[term]', bạn có thể giải thích thêm không?"

---

## 📝 NOTE-TAKING TEMPLATE

| Time | Speaker | Content | Category | Action |
|------|---------|---------|----------|--------|
| 10:05 | PM | "Cần báo cáo real-time" | NFR | Clarify "real-time" |
| 10:08 | User | "Export Excel mất 5 phút" | Pain Point | Document |
| 10:12 | PM | "Tích hợp với SAP" | Integration | Verify API available |

### Categories:
- **FR** - Functional Requirement
- **NFR** - Non-Functional Requirement
- **BR** - Business Rule
- **Constraint** - Limitation
- **Pain Point** - Current problem
- **Assumption** - To be verified
- **TBD** - To be determined

---

## 🔗 NEXT SKILLS

| After gathering info... | Load |
|------------------------|------|
| Write requirements | → SKILL-03 |
| Prioritize requirements | → SKILL-05 |
| Handle conflicts | → SKILL-06 |
| Create documents | → SKILL-09, 10, 11, 12 |

---

*Proceed to SKILL-03 for Requirements Writing & Quality Standards*
