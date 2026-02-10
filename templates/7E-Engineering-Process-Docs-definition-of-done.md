# Definition of Done

> **Document ID:** 7E  
> **Document purpose**  
> This document defines the minimum completion criteria required for work items, features, fixes, or deliverables to be considered "done."  
> It is intended for internal engineering and delivery stakeholders.

This document supports consistent delivery quality and reduces ambiguity in completion expectations.

---

## 1. Overview

The Definition of Done (DoD) establishes shared criteria for when engineering work is complete.

DoD may apply to:
- features
- bug fixes
- infrastructure updates
- documentation changes
- AI prompt updates

Not all items apply to every task, but deviations should be documented.

---

## 2. General completion criteria

A work item is considered done when:

- [ ] The implementation meets defined requirements
- [ ] The change is reviewed and approved
- [ ] Code is merged into the appropriate branch
- [ ] CI/CD checks pass
- [ ] Relevant documentation is updated

---

## 3. Testing criteria

- [ ] Unit tests written or updated (if applicable)
- [ ] Integration tests written or updated (if applicable)
- [ ] End-to-end validation performed (if applicable)
- [ ] Test failures resolved
- [ ] Edge cases reviewed

---

## 4. Security criteria

- [ ] No secrets or sensitive values committed
- [ ] Access controls reviewed for correctness
- [ ] Input validation performed where required
- [ ] Logging does not expose sensitive information
- [ ] Dependencies reviewed if added or updated

---

## 5. Documentation criteria

- [ ] README or supporting documentation updated
- [ ] API docs updated if interface changes occurred
- [ ] Architecture docs updated if structure changed
- [ ] Configuration steps documented if required

---

## 6. Deployment readiness criteria

- [ ] Deployment impact assessed
- [ ] Rollback strategy considered
- [ ] Monitoring updates included if needed
- [ ] Release notes created if applicable

---

## 7. Operational readiness criteria

- [ ] Operational procedures updated if needed
- [ ] Alerts and dashboards updated if required
- [ ] Support team notified if change impacts operations

---

## 8. AI and automation criteria (if applicable)

- [ ] Prompt updates reviewed for safety and reliability
- [ ] Guardrails reviewed and still effective
- [ ] Evaluation tests updated and executed
- [ ] Output format validated
- [ ] HITL workflow reviewed if required

---

## 9. Exception handling

If any DoD criteria are not met, document:

- {{Criteria not met}}
- {{Reason for exception}}
- {{Planned follow-up action}}
- {{Owner}}

---

## 10. Assumptions and open items

### Assumptions
- {{Assumption}}
- {{Assumption}}

### Open items / TODOs
- {{DoD not aligned across teams}}
- {{Review thresholds unclear}}

---

## 11. Summary

This document defines completion criteria for engineering work.

It supports consistent quality, predictable delivery, and shared expectations across the team.
