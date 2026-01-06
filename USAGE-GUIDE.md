# 📘 BA-Kit Usage Guide (Antigravity Native)

**Welcome to the Cognitive Swarm.**
This guide explains how to pilot the 15 Agents of the BA-Kit to achieve "World Class" results.

---

## 🏗️ Architecture: The "System 2" Difference

Unlike standard "Chat with LLM" workflows, BA-Kit agents operate on a **Cognitive Loop**:

1.  **Stimulus**: User Input.
2.  **System 1 (Fast)**: The Agent drafts an immediate response based on pattern matching.
3.  **System 2 (Slow)**: The Agent **Reflects**.
    *   It critiques its own draft ("Is this too vague?").
    *   It checks for hallucinations ("Did I invent that dependency?").
    *   It verifies facts ("Let me grep the codebase to be sure").
4.  **Response**: The polished, verified output.

**Benefit**: You get fewer errors, better math, and real citations.

---

## 🚦 The 15 Agents: When to Use Who?

### 🔴 The Boss
*   **`@ba-master`**: Use when you don't know who to use. "I have a problem, help."

### 🔵 The Creator Phase (Lifecycle Start)
1.  **`@ba-identity`**: Start here. Define *Who* are the stakeholders? Who is the Sponsor?
2.  **`@ba-elicitation`**: Use this to interview users. "What do you need?" (Funnel Questioning).
3.  **`@ba-writing`**: Use this to draft the Requirements (User Stories / GHERKIN).

### 🟡 The Engineering Phase (Lifecycle Middle)
4.  **`@ba-nfr`**: Define *Constraints*. "How fast? How secure?" (ISO 25010).
5.  **`@ba-process`**: Draw the flow. "Visualize the checkout process." (BPMN).
6.  **`@ba-traceability`**: Map the links. "What breaks if I change X?" (Graph Theory).
7.  **`@ba-conflict`**: Resolve fights. "Sales wants A, Dev wants B." (Harvard Negotiation).

### 🟣 The Optimization Phase (Lifecycle End)
8.  **`@ba-validation`**: Check quality. "Find bugs in this spec." (Visual QA).
9.  **`@ba-prioritization`**: Decide order. "What do we build first?" (WSJF).
10. **`@ba-solution`**: Check money. "Is this profitable?" (ROI/NPV).
11. **`@ba-export`**: Publish. "Make it a PDF." (Compliance).

### ⚫ The "Level 5" Phase (Deep Optimization)
12. **`@ba-metrics`**: Audit the *Process*. "Are we getting faster or just sloppier?" (SPC).
13. **`@ba-root-cause`**: Fix the *System*. "Why do we keep having bugs?" (5 Whys).
14. **`@ba-innovation`**: Design *Experiments*. "Will AI help?" (A/B Testing).

---

## 🛠️ Tool Mandates (Why Agents Run Commands)

You will see Agents running `run_command` or `grep_search`. **Do not stop them.**

*   **Python**: Used by `@ba-solution`, `@ba-innovation`, `@ba-metrics` to ensure **Math Integrity**. LLMs cannot add; Python can.
*   **Grep**: Used by `@ba-traceability` to ensure **Link Integrity**. The Agent must "see" the file to link it.
*   **Web Search**: Used by `@ba-nfr` to ensure **Standard Integrity**. It checks the live web for GDPR/ISO updates.

---

## 🎓 Pro-Tips

### 1. The "Persona Handover"
You can chain agents manually for powerful workflows:
> *User*: `@ba-elicitation Interview me about the Login feature.`
> *(Conversation happens...)*
> *User*: `Great. Now @ba-writing turn that interview into Gherkin scenarios.`

### 2. The "Bias Check"
If sure an Agent is being too nice, ask it to use its Critic Mode explicitly:
> *User*: `@ba-validation Roast this requirement. Be extremely harsh.`

### 3. The "Visual Scan"
You can show images to Agents (Drag & Drop):
> *User*: `@[image.png] @ba-writing Write UI requirements based on this mockup.`

---

**End of Guide**
*Go forth and Engineer.*
