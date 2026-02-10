# Documentation Generation Examples

## Available Doc Sets

### Preset Groups
- `core` - Core system documentation (10 docs)
- `ai` - AI/Automation documentation (7 docs)
- `api` - API/Integration documentation (4 docs)
- `data` - Data documentation (5 docs)
- `security` - Security documentation (7 docs)
- `operations` - Operations documentation (6 docs)
- `engineering` - Engineering process documentation (6 docs)
- `customer` - Customer-facing documentation (6 docs)
- `business` - Business documentation (7 docs)

### Individual Doc Keys
See the full list in `scripts/generate_docs.py` under the `DOCS` dictionary.

## Example Workflows

### 1. Generate Core System Docs Only
```yaml
name: Generate Documentation

on:
  workflow_dispatch:
  push:
    branches: [ main ]

permissions:
  contents: write
  pull-requests: write

jobs:
  docs:
    uses: Innovation-Advisory-Consulting/docs-gen/.github/workflows/generate-docs.yml@main
    with:
      docs_gen_repo: Innovation-Advisory-Consulting/docs-gen
      output_dir: docs/generated
      doc_set: "core"
      create_pr: false
      mode: "ai"
      max_context_chars: 120000
    secrets:
      AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
      AZURE_OPENAI_KEY: ${{ secrets.AZURE_OPENAI_KEY }}
      DEPLOYMENT_NAME: ${{ secrets.DEPLOYMENT_NAME }}
```

### 2. Generate Multiple Doc Set Presets
```yaml
doc_set: "core,security,operations"
```

### 3. Generate All Customer-Facing Docs
```yaml
doc_set: "customer,business"
```

### 4. Generate Specific Individual Docs
```yaml
doc_set: "core-solution,core-architecture,security-overview,api-reference"
```

### 5. Mix Presets and Individual Docs
```yaml
doc_set: "core,ai-overview,security,customer-solution"
```

### 6. Generate Everything (Not Recommended - 70+ docs)
```yaml
doc_set: "core,ai,api,data,security,operations,engineering,customer,business"
```

### 7. Legacy Format (Backward Compatible)
```yaml
doc_set: "solution,architecture,developer,processes,customer"
```

## Doc Set Breakdown

### Core (10 docs)
- 1A: Solution Overview
- 1B: Architecture Overview
- 1C: Architecture Diagrams
- 1D: System Components
- 1E: Data Flow
- 1F: Deployment & Environments
- 1G: Repo Structure & Code Map
- 1H: Build & Deploy
- 1I: Dependency Inventory
- 1J: Module-Level Documentation

### AI (7 docs)
- 2A: AI Overview
- 2B: Prompt Library
- 2C: Model Behavior & Guardrails
- 2D: Evaluation & Testing
- 2E: Human-in-the-Loop
- 2F: AI Operations & Monitoring
- 2G: Data Usage & Privacy

### API (4 docs)
- 3A: API Reference
- 3B: Integration Guide
- 3C: Auth & Access Control
- 3D: Data Contracts

### Data (5 docs)
- 4A: Database Schema
- 4B: Data Dictionary
- 4C: Logging & Telemetry
- 4D: Data Pipeline/ETL
- 4E: Data Retention & Archival

### Security (7 docs)
- 5A: Security Overview
- 5B: Threat Model
- 5C: Risk Register
- 5D: Secrets Management
- 5E: Vulnerability & Patch Management
- 5F: Incident Response Runbook
- 5G: Compliance & Control Mapping

### Operations (6 docs)
- 6A: Operations Runbook
- 6B: Monitoring & Alerting
- 6C: Backup & Recovery
- 6D: Release Management
- 6E: Support & Escalation
- 6F: Capacity Planning & Scaling

### Engineering (6 docs)
- 7A: Onboarding Guide
- 7B: Development Workflow
- 7C: Code Review Checklist
- 7D: Coding Standards
- 7E: Definition of Done
- 7F: Change Management

### Customer (6 docs)
- 8A: Customer Solution Overview
- 8B: Customer Architecture Overview
- 8C: Customer Integration Guide
- 8D: Customer Security Overview
- 8E: Customer Operations & Support
- 8F: Requirements Traceability

### Business (7 docs)
- 9A: Executive Solution Brief
- 9B: Business Value & ROI
- 9C: Program Status & Milestones
- 9D: Risk & Compliance Summary
- 9E: Solution Roadmap & Vision
- 9F: Executive FAQ & Positioning
- 9G: Marketing One-Pager
