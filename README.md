# docs-gen (MVP)

This repo provides a reusable GitHub workflow that can generate documentation for any target repo.

## How target repos call it

In a target repo, create `.github/workflows/docs.yml`:

```yaml
name: Generate Documentation

on:
  workflow_dispatch:

jobs:
  docs:
    uses: <OWNER>/docs-gen/.github/workflows/generate-docs.yml@v1
    with:
      output_dir: docs/generated
      doc_set: "architecture,developer,processes,customer"
      create_pr: false
```

## Azure OpenAI

MVP doesn’t call Azure OpenAI yet. Next iteration will add:
- AZURE_OPENAI_ENDPOINT
- AZURE_OPENAI_API_KEY
- AZURE_OPENAI_DEPLOYMENT
- AZURE_OPENAI_API_VERSION
