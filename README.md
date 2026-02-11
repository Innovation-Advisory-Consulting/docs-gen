# docs-gen

Reusable GitHub workflow for AI-powered documentation generation. Deeply analyzes your entire repository (all files, folders, and code structure) and generates comprehensive documentation using Azure OpenAI.

## Quick Start

In your target repo, create `.github/workflows/docs.yml`:

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

## Available Doc Sets

**Presets** (use these for quick generation):
- `core` - Core system docs (10 docs: solution, architecture, diagrams, components, data flow, deployment, repo structure, build, dependencies, modules)
- `ai` - AI/Automation docs (7 docs: overview, prompts, guardrails, testing, HITL, ops, privacy)
- `api` - API/Integration docs (4 docs: reference, integration, auth, contracts)
- `data` - Data docs (5 docs: schema, dictionary, logging, pipeline, retention)
- `security` - Security docs (7 docs: overview, threat model, risk, secrets, vuln management, incident response, compliance)
- `operations` - Operations docs (6 docs: runbook, monitoring, backup, release, support, capacity)
- `engineering` - Engineering process docs (6 docs: onboarding, workflow, code review, standards, DoD, change management)
- `customer` - Customer-facing docs (6 docs: solution, architecture, integration, security, ops, requirements)
- `business` - Business docs (7 docs: executive brief, ROI, status, risk, roadmap, FAQ, marketing)

**Examples**:
```yaml
# Single preset
doc_set: "core"

# Multiple presets
doc_set: "core,security,operations"

# Specific individual docs
doc_set: "core-solution,core-architecture,security-overview"

# Mix presets and individual docs
doc_set: "core,ai-overview,customer-solution"
```

See [EXAMPLES.md](EXAMPLES.md) for complete list of individual doc keys.

## Configuration

| Parameter | Default | Description |
|-----------|---------|-------------|
| `docs_gen_repo` | required | This repo (e.g., `Innovation-Advisory-Consulting/docs-gen`) |
| `output_dir` | `docs/generated` | Where to save generated docs |
| `doc_set` | `core` | Comma-separated doc sets or individual keys |
| `create_pr` | `false` | Create PR instead of direct commit |
| `mode` | `ai` | `ai` for AI generation, `static` for template copy |
| `max_context_chars` | `120000` | Max repo context sent to AI (increase for larger repos) |

## What Gets Analyzed

The system performs deep analysis of your repository:
- **All tracked files** (respects .gitignore)
- **Complete directory structure** (up to 1000 files)
- **Configuration files** (package.json, requirements.txt, etc.) - full content
- **Infrastructure** (Dockerfiles, workflows, terraform) - full content
- **Documentation** (README, existing docs) - full content
- **Source code** (up to 100 files) - extracts imports, classes, functions
- **Test files** (sample) - structure analysis

This comprehensive scanning ensures the AI has full context of your codebase to generate accurate documentation.

## Required Secrets

Set these in your target repo's Settings → Secrets:
- `AZURE_OPENAI_ENDPOINT` - Your Azure OpenAI endpoint URL
- `AZURE_OPENAI_KEY` - Your Azure OpenAI API key
- `DEPLOYMENT_NAME` - Your Azure OpenAI deployment name
- `AZURE_OPENAI_API_VERSION` (optional) - Defaults to `2024-02-15-preview`
- `DOCS_GEN_TOKEN` (optional) - Only needed if docs-gen repo is private
