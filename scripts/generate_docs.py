import os
import argparse
from pathlib import Path
import subprocess
from datetime import datetime
import json
import requests

# -----------------------------
# Helpers
# -----------------------------
def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")

def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

def git(cmd):
    try:
        return subprocess.check_output(cmd, stderr=subprocess.DEVNULL).decode("utf-8").strip()
    except Exception:
        return ""

def safe_repo_tree(max_lines: int = 500) -> str:
    out = git(["git", "ls-files"])
    files = out.splitlines() if out else []
    return "\n".join(files[:max_lines])

def pick_key_files() -> list[Path]:
    candidates = [
        Path("README.md"),
        Path("package.json"),
        Path("pyproject.toml"),
        Path("requirements.txt"),
        Path("Dockerfile"),
        Path("docker-compose.yml"),
        Path(".github/workflows"),
    ]
    picked = []
    for c in candidates:
        if c.is_file():
            picked.append(c)
        elif c.is_dir():
            for wf in sorted(c.glob("*.yml"))[:3]:
                picked.append(wf)
    return picked

def build_context(max_chars: int) -> str:
    parts = ["## REPO TREE\n" + safe_repo_tree()]
    for p in pick_key_files():
        try:
            parts.append(f"\n## FILE: {p}\n{read_text(p)[:20000]}")
        except Exception:
            pass
    return "\n".join(parts)[:max_chars]

# -----------------------------
# Azure OpenAI
# -----------------------------
def azure_chat(system: str, user: str) -> str:
    endpoint = os.environ["AZURE_OPENAI_ENDPOINT"].rstrip("/")
    api_key = os.environ["AZURE_OPENAI_API_KEY"]
    deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    api_version = os.environ.get("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")

    url = f"{endpoint}/openai/deployments/{deployment}/chat/completions?api-version={api_version}"
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key,
    }

    payload = {
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "temperature": 0.2,
    }

    r = requests.post(url, headers=headers, json=payload, timeout=120)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]

# -----------------------------
# Generation
# -----------------------------
DOCS = {
    # Core System Docs (1A-1J)
    "core-solution": ("1A-Core-System-Docs-solution-overview(1).md", "1A-CoreSystem-SolutionOverview.md"),
    "core-architecture": ("1B-Core-System-Docs-architecture-overview.md", "1B-CoreSystem-ArchitectureOverview.md"),
    "core-diagrams": ("1C-Core-System-Docs-architecture-diagrams.md", "1C-CoreSystem-ArchitectureDiagrams.md"),
    "core-components": ("1D-Core-System-Docs-system-components.md", "1D-CoreSystem-SystemComponents.md"),
    "core-dataflow": ("1E-Core-System-Docs-data-flow.md", "1E-CoreSystem-DataFlow.md"),
    "core-deployment": ("1F-Core-System-Docs-deployment-and-environments.md", "1F-CoreSystem-DeploymentEnvironments.md"),
    "core-repo": ("1G-Core-System-Docs-repo-structure-code-map.md", "1G-CoreSystem-RepoStructure.md"),
    "core-build": ("1H-Core-System-Docs-build-and-deploy.md", "1H-CoreSystem-BuildDeploy.md"),
    "core-dependencies": ("1I-Core-System-Docs-dependency-inventory.md", "1I-CoreSystem-DependencyInventory.md"),
    "core-modules": ("1J-Core-System-Docs-module-level-documentation.md", "1J-CoreSystem-ModuleDocs.md"),
    
    # AI/Automation Docs (2A-2G)
    "ai-overview": ("2A-AI-Automation-Docs-ai-overview.md", "2A-AI-Overview.md"),
    "ai-prompts": ("2B-AI-Automation-Docs-prompt-library.md", "2B-AI-PromptLibrary.md"),
    "ai-guardrails": ("2C-AI-Automation-Docs-model-behavior-and-guardrails.md", "2C-AI-ModelGuardrails.md"),
    "ai-testing": ("2D-AI-Automation-Docs-evaluation-and-testing.md", "2D-AI-EvaluationTesting.md"),
    "ai-hitl": ("2E-AI-Automation-Docs-human-in-the-loop.md", "2E-AI-HumanInTheLoop.md"),
    "ai-ops": ("2F-AI-Automation-Docs-ai-operations-and-monitoring.md", "2F-AI-OperationsMonitoring.md"),
    "ai-privacy": ("2G-AI-Automation-Docs-data-usage-and-privacy.md", "2G-AI-DataPrivacy.md"),
    
    # API/Integration Docs (3A-3D)
    "api-reference": ("3A-API-Integration-Docs-api-reference.md", "3A-API-Reference.md"),
    "api-integration": ("3B-API-Integration-Docs-integration-guide.md", "3B-API-IntegrationGuide.md"),
    "api-auth": ("3C-API-Integration-Docs-auth-and-access-control.md", "3C-API-AuthAccessControl.md"),
    "api-contracts": ("3D-API-Integration-Docs-data-contracts.md", "3D-API-DataContracts.md"),
    
    # Data Docs (4A-4E)
    "data-schema": ("4A-Data-Docs-database-schema.md", "4A-Data-DatabaseSchema.md"),
    "data-dictionary": ("4B-Data-Docs-data-dictionary.md", "4B-Data-DataDictionary.md"),
    "data-logging": ("4C-Data-Docs-logging-and-telemetry.md", "4C-Data-LoggingTelemetry.md"),
    "data-pipeline": ("4D-Data-Docs-data-pipeline-etl.md", "4D-Data-PipelineETL.md"),
    "data-retention": ("4E-Data-Docs-data-retention-and-archival.md", "4E-Data-RetentionArchival.md"),
    
    # Security Docs (5A-5G)
    "security-overview": ("5A-Security-Docs-security-overview.md", "5A-Security-Overview.md"),
    "security-threat": ("5B-Security-Docs-threat-model.md", "5B-Security-ThreatModel.md"),
    "security-risk": ("5C-Security-Docs-risk-register.md", "5C-Security-RiskRegister.md"),
    "security-secrets": ("5D-Security-Docs-secrets-management.md", "5D-Security-SecretsManagement.md"),
    "security-vuln": ("5E-Security-Docs-vulnerability-and-patch-management.md", "5E-Security-VulnPatchManagement.md"),
    "security-incident": ("5F-Security-Docs-incident-response-runbook.md", "5F-Security-IncidentResponse.md"),
    "security-compliance": ("5G-Security-Docs-compliance-and-control-mapping.md", "5G-Security-ComplianceMapping.md"),
    
    # Operations Docs (6A-6F)
    "ops-runbook": ("6A-Operations-Docs-operations-runbook.md", "6A-Operations-Runbook.md"),
    "ops-monitoring": ("6B-Operations-Docs-monitoring-and-alerting.md", "6B-Operations-MonitoringAlerting.md"),
    "ops-backup": ("6C-Operations-Docs-backup-and-recovery.md", "6C-Operations-BackupRecovery.md"),
    "ops-release": ("6D-Operations-Docs-release-management.md", "6D-Operations-ReleaseManagement.md"),
    "ops-support": ("6E-Operations-Docs-support-and-escalation.md", "6E-Operations-SupportEscalation.md"),
    "ops-capacity": ("6F-Operations-Docs-capacity-planning-and-scaling.md", "6F-Operations-CapacityPlanning.md"),
    
    # Engineering Process Docs (7A-7F)
    "eng-onboarding": ("7A-Engineering-Process-Docs-onboarding-guide.md", "7A-Engineering-OnboardingGuide.md"),
    "eng-workflow": ("7B-Engineering-Process-Docs-development-workflow.md", "7B-Engineering-DevWorkflow.md"),
    "eng-review": ("7C-Engineering-Process-Docs-code-review-checklist.md", "7C-Engineering-CodeReviewChecklist.md"),
    "eng-standards": ("7D-Engineering-Process-Docs-coding-standards.md", "7D-Engineering-CodingStandards.md"),
    "eng-dod": ("7E-Engineering-Process-Docs-definition-of-done.md", "7E-Engineering-DefinitionOfDone.md"),
    "eng-change": ("7F-Engineering-Process-Docs-change-management.md", "7F-Engineering-ChangeManagement.md"),
    
    # Customer Docs (8A-8F)
    "customer-solution": ("8A-Customer-Docs-customer-solution-overview.md", "8A-Customer-SolutionOverview.md"),
    "customer-architecture": ("8B-Customer-Docs-customer-architecture-overview.md", "8B-Customer-ArchitectureOverview.md"),
    "customer-integration": ("8C-Customer-Docs-customer-integration-guide.md", "8C-Customer-IntegrationGuide.md"),
    "customer-security": ("8D-Customer-Docs-customer-security-overview.md", "8D-Customer-SecurityOverview.md"),
    "customer-ops": ("8E-Customer-Docs-customer-operations-and-support.md", "8E-Customer-OperationsSupport.md"),
    "customer-requirements": ("8F-Customer-Docs-requirements-traceability.md", "8F-Customer-RequirementsTraceability.md"),
    
    # Business Docs (9A-9G)
    "business-brief": ("9A-Business-Docs-executive-solution-brief.md", "9A-Business-ExecutiveBrief.md"),
    "business-roi": ("9B-Business-Docs-business-value-and-roi.md", "9B-Business-ValueROI.md"),
    "business-status": ("9C-Business-Docs-program-status-and-milestones.md", "9C-Business-StatusMilestones.md"),
    "business-risk": ("9D-Business-Docs-risk-and-compliance-summary.md", "9D-Business-RiskCompliance.md"),
    "business-roadmap": ("9E-Business-Docs-solution-roadmap-and-vision.md", "9E-Business-RoadmapVision.md"),
    "business-faq": ("9F-Business-Docs-executive-faq-and-positioning.md", "9F-Business-ExecutiveFAQ.md"),
    "business-marketing": ("9G-Business-Docs-marketing-one-pager.md", "9G-Business-MarketingOnePager.md"),
    
    # Legacy templates (keep for backward compatibility)
    "solution": ("solution-overview.md", "SolutionOverview.md"),
    "architecture": ("architecture.md", "Architecture.md"),
    "developer": ("developer.md", "Developer.md"),
    "processes": ("processes.md", "BusinessProcesses.md"),
    "customer": ("customer.md", "Customer.md"),
}

# Doc set presets for convenience
DOC_SETS = {
    "core": "core-solution,core-architecture,core-diagrams,core-components,core-dataflow,core-deployment,core-repo,core-build,core-dependencies,core-modules",
    "ai": "ai-overview,ai-prompts,ai-guardrails,ai-testing,ai-hitl,ai-ops,ai-privacy",
    "api": "api-reference,api-integration,api-auth,api-contracts",
    "data": "data-schema,data-dictionary,data-logging,data-pipeline,data-retention",
    "security": "security-overview,security-threat,security-risk,security-secrets,security-vuln,security-incident,security-compliance",
    "operations": "ops-runbook,ops-monitoring,ops-backup,ops-release,ops-support,ops-capacity",
    "engineering": "eng-onboarding,eng-workflow,eng-review,eng-standards,eng-dod,eng-change",
    "customer": "customer-solution,customer-architecture,customer-integration,customer-security,customer-ops,customer-requirements",
    "business": "business-brief,business-roi,business-status,business-risk,business-roadmap,business-faq,business-marketing",
}

SYSTEM_PROMPT = """You are a documentation generator.
Rules:
- Use only provided repository context
- Do not invent architecture or APIs
- Mark missing info as TODO
"""

def expand_doc_sets(doc_set_str: str) -> list[str]:
    """Expand preset names and return list of individual doc keys."""
    keys = []
    for item in doc_set_str.split(","):
        item = item.strip()
        if item in DOC_SETS:
            # Recursively expand presets
            keys.extend(expand_doc_sets(DOC_SETS[item]))
        else:
            keys.append(item)
    return keys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="docs/generated")
    parser.add_argument("--doc-set", default="core")
    args = parser.parse_args()

    mode = os.environ.get("DOCGEN_MODE", "ai")
    context = build_context(int(os.environ.get("MAX_CONTEXT_CHARS", "120000")))

    templates_dir = Path(__file__).resolve().parents[1] / "templates"
    out_dir = Path(args.output_dir)

    repo = os.environ.get("GITHUB_REPOSITORY", "unknown")
    sha = os.environ.get("GITHUB_SHA", "unknown")
    now = datetime.utcnow().isoformat()

    header = f"""<!--
Generated by docs-gen
Repo: {repo}
Commit: {sha}
Generated: {now}
-->
"""

    index = ["# Generated Documentation", ""]
    
    # Expand doc sets and deduplicate
    doc_keys = list(dict.fromkeys(expand_doc_sets(args.doc_set)))

    for key in doc_keys:
        if key not in DOCS:
            print(f"Warning: Unknown doc key '{key}', skipping")
            continue

        tpl_name, out_name = DOCS[key]
        tpl_path = templates_dir / tpl_name
        
        if not tpl_path.exists():
            print(f"Warning: Template '{tpl_name}' not found, skipping")
            continue
            
        tpl = read_text(tpl_path)

        if mode == "static":
            content = tpl
        else:
            prompt = f"{tpl}\n\nRepository context:\n{context}"
            content = azure_chat(SYSTEM_PROMPT, prompt)

        write_text(out_dir / out_name, header + content)
        index.append(f"- [{out_name}]({out_name})")

    write_text(out_dir / "README.md", "\n".join(index))

if __name__ == "__main__":
    main()
