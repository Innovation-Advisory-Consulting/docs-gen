import os
import argparse
from pathlib import Path
import subprocess
from datetime import datetime

def read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

def git(cmd):
    try:
        return subprocess.check_output(cmd, stderr=subprocess.DEVNULL).decode("utf-8").strip()
    except Exception:
        return ""

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="docs/generated")
    parser.add_argument("--doc-set", default="architecture,developer,processes,customer")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    templates_dir = Path(__file__).resolve().parents[1] / "templates"

    repo = os.environ.get("GITHUB_REPOSITORY", "unknown/repo")
    sha = os.environ.get("GITHUB_SHA", git(["git", "rev-parse", "HEAD"]) or "unknown")
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%SZ")

    system_purpose = (
        f"Auto-generated placeholder. Update with system purpose.\n\n"
        f"Source repo: {repo}\n"
        f"Source commit: {sha}\n"
        f"Generated at: {now}\n"
    )

    selected = [x.strip() for x in args.doc_set.split(",") if x.strip()]
    mapping = {
        "architecture": ("architecture.md", "Architecture.md"),
        "developer": ("developer.md", "Developer.md"),
        "processes": ("processes.md", "BusinessProcesses.md"),
        "customer": ("customer.md", "Customer.md"),
    }

    for key in selected:
        if key not in mapping:
            continue
        tpl_name, out_name = mapping[key]
        tpl = read_file(templates_dir / tpl_name)
        tpl = tpl.replace("{{SYSTEM_PURPOSE}}", system_purpose)
        write_file(output_dir / out_name, tpl)

    index = [
        "# Generated Documentation",
        "",
        f"- Source repo: `{repo}`",
        f"- Source commit: `{sha}`",
        f"- Generated at (UTC): `{now}`",
        "",
        "## Documents",
    ]
    for key in selected:
        if key in mapping:
            index.append(f"- [{mapping[key][1]}]({mapping[key][1]})")
    write_file(output_dir / "README.md", "\n".join(index) + "\n")

    print(f"Wrote docs to {output_dir}")

if __name__ == "__main__":
    main()
