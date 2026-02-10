# Code Review Checklist

> **Document ID:** 7C  
> **Document purpose**  
> This document provides a standardized checklist for reviewing code changes in the solution.  
> It is intended for internal engineering stakeholders.

This checklist supports quality, maintainability, security, and consistency.

---

## 1. Overview

This checklist is used during pull request review to confirm code changes meet expected standards.

Not all items apply to every change. Reviewers should apply judgment based on scope and risk.

---

## 2. General review checklist

- [ ] Code changes align with the intended ticket or work item
- [ ] Code is readable and follows naming conventions
- [ ] Logic is clear and maintainable
- [ ] No unnecessary complexity introduced
- [ ] Comments are used where needed

---

## 3. Functional correctness

- [ ] Code produces expected behavior
- [ ] Edge cases are handled appropriately
- [ ] Error handling is appropriate and consistent
- [ ] Failure paths are tested or considered

---

## 4. Testing checklist

- [ ] Unit tests added or updated (if applicable)
- [ ] Integration tests added or updated (if applicable)
- [ ] Tests pass locally or in CI pipeline
- [ ] Test coverage appears reasonable for change scope
- [ ] Mocking/stubbing is used appropriately

---

## 5. Security checklist

- [ ] No secrets or credentials committed to the repository
- [ ] Access control checks are applied consistently
- [ ] Input validation is performed where needed
- [ ] Output does not expose sensitive data
- [ ] Dependencies added are reviewed for risk

---

## 6. Performance checklist

- [ ] No obvious performance regressions introduced
- [ ] Queries, loops, or high-cost operations reviewed
- [ ] Caching used appropriately (if applicable)
- [ ] Logging level is appropriate for production

---

## 7. API and integration checklist (if applicable)

- [ ] API contract remains stable or versioning is applied
- [ ] Request/response schemas validated
- [ ] Backward compatibility maintained
- [ ] Error responses are meaningful and consistent
- [ ] Integration documentation updated (if required)

---

## 8. Data and database checklist (if applicable)

- [ ] Schema changes are documented
- [ ] Migration scripts reviewed and tested
- [ ] Backward compatibility considered
- [ ] Indexing implications considered
- [ ] Data retention and privacy implications reviewed

---

## 9. AI and automation checklist (if applicable)

- [ ] Prompt changes reviewed for safety and reliability
- [ ] Guardrails remain intact
- [ ] Evaluation tests updated or reviewed
- [ ] Output format remains stable
- [ ] Human-in-the-loop workflow impacts considered

---

## 10. Documentation checklist

- [ ] Relevant documentation updated
- [ ] README changes made if needed
- [ ] Configuration instructions updated if required

---

## 11. Deployment and operational checklist

- [ ] Deployment impact assessed
- [ ] Monitoring implications considered
- [ ] Rollback approach understood (if applicable)

---

## 12. Reviewer notes

Use this section to record reviewer-specific observations.

- {{Reviewer note}}
- {{Reviewer note}}

---

## 13. Summary

This checklist supports consistent code review practices across the engineering team.

It should be updated as standards, tooling, and architecture evolve.
