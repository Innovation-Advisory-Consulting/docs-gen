# Prompt Library

> **Document ID:** 2B  
> **Document purpose**  
> This document provides a structured library of prompts used by the solution, including purpose, input format, expected output format, and usage constraints.  
> It is intended for internal engineering, AI development, and automation stakeholders.

This document supports maintainability, version control, and safe reuse of prompts.

---

## 1. Overview

This prompt library documents prompts used within the solution to support AI-driven functionality.

Each prompt entry should include:
- intended purpose
- required inputs
- output expectations
- validation rules
- known limitations
- version tracking

If prompts are still being collected, mark entries as **TODO**.

---

## 2. Prompt inventory

List all prompts used in the solution.

| Prompt ID | Prompt name | Use case | Output type | Status |
|----------|-------------|----------|-------------|--------|
| {{P-001}} | {{Prompt name}} | {{Use case}} | {{Structured/Text}} | {{Confirmed/TODO}} |
| {{P-002}} | {{Prompt name}} | {{Use case}} | {{Output type}} | {{Status}} |

---

## 3. Prompt template

Repeat this section for each prompt.

---

### Prompt ID: {{P-001}} — {{Prompt name}}

#### Purpose
{{Describe why this prompt exists and what it is intended to accomplish.}}

#### Trigger / invocation point
{{Describe when this prompt is called (workflow step, API request, automation job, etc.).}}

#### Input format
Describe the required input structure.

- **Input variables:**  
  - `{{variable_name}}`: {{description}}
  - `{{variable_name}}`: {{description}}

- **Input source(s):** {{Source system / user input / database / unknown}}

#### Prompt text
```text
{{Insert the actual prompt text here}}
```

#### Expected output format
Describe expected output.

- **Output type:** {{JSON / text / structured / unknown}}
- **Required fields:**  
  - {{Field name}}
  - {{Field name}}

Example output:
```json
{
  "field": "value",
  "field2": "value"
}
```

#### Validation rules
Describe how output is validated.

- {{Validation rule}}
- {{Validation rule}}

If validation is not implemented, state **Output validation not implemented**.

#### Error handling and retries
Describe what happens when output is invalid.

- {{Retry strategy}}
- {{Fallback behavior}}
- {{Escalation to human review}}

---

#### Safety and guardrails
Document guardrails for safe use.

- {{Restricted language rules}}
- {{Sensitive data handling}}
- {{Prompt injection mitigation}}

---

#### Known limitations
Document known weaknesses.

- {{Limitation}}
- {{Limitation}}

---

#### Version history
| Version | Date | Change summary | Author |
|--------|------|----------------|--------|
| {{v1}} | {{Date}} | {{Summary}} | {{Name}} |
| {{v2}} | {{Date}} | {{Summary}} | {{Name}} |

---

## 4. Prompt governance

Describe how prompts are managed.

- **Prompt approval process:** {{Process or Unknown}}
- **Storage location:** {{Repo path or Unknown}}
- **Review cadence:** {{Frequency or Unknown}}
- **Change tracking:** {{Git / manual / unknown}}

---

## 5. Assumptions and open items

### Assumptions
- {{Assumption}}
- {{Assumption}}

### Open items / TODOs
- {{Prompt missing}}
- {{Prompt needs validation schema}}

---

## 6. Summary

This document provides a structured prompt library to support safe and maintainable AI usage within the solution.

It should be updated whenever prompts are added, modified, or deprecated.
