# Data Dictionary

> **Document ID:** 4B  
> **Document purpose**  
> This document defines the meaning, format, and usage of data elements used by the solution.  
> It is intended for internal engineering, data, analytics, and integration stakeholders.

This document supports shared understanding of data semantics across teams.

---

## 1. Overview

This data dictionary provides authoritative definitions for data elements used within the solution.

It complements the Database Schema by focusing on meaning and usage rather than structure alone.

---

## 2. Scope

Describe what is covered.

- {{In-scope schemas or domains}}
- {{In-scope integrations}}
- {{Out-of-scope data (if any)}}

---

## 3. Data element inventory

List key data elements.

| Data element | Domain / Table | Type | Description | Notes |
|-------------|----------------|------|-------------|------|
| {{Element}} | {{Location}} | {{Type}} | {{Description}} | {{Notes}} |
| {{Element}} | {{Location}} | {{Type}} | {{Description}} | {{Notes}} |

---

## 4. Data element definition template

Repeat this section for each important data element.

---

### Data element: {{Element name}}

#### Description
{{Plain-language definition of the data element.}}

#### Source
{{Where the data originates (user input, system-generated, external source).}}

#### Format and constraints
- **Type:** {{Type}}
- **Length / precision:** {{Details}}
- **Allowed values:** {{Enum or range}}

---

#### Usage
Describe how the element is used.

- {{Business logic usage}}
- {{Reporting or analytics usage}}
- {{Integration usage}}

---

#### Sensitivity and classification
- **Sensitivity level:** {{Low/Medium/High/Unknown}}
- **Contains personal or sensitive data:** {{Yes/No/Unknown}}

---

#### Lifecycle
- **Created:** {{When}}
- **Updated:** {{When}}
- **Retired or archived:** {{When}}

---

#### Notes / TODOs
- {{Open item}}
- {{Open item}}

---

## 5. Naming and formatting standards

Document standards.

- {{Naming conventions}}
- {{Date/time formats}}
- {{Boolean representation}}

---

## 6. Assumptions and open items

### Assumptions
- {{Assumption}}
- {{Assumption}}

### Open items / TODOs
- {{Definition missing}}
- {{Classification pending}}

---

## 7. Summary

This document defines data elements used by the solution to support consistent interpretation and integration.

It should be updated as data models and integrations evolve.
