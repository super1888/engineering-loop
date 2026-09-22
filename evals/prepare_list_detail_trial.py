"""Prepare fresh A/B workspaces and freeze inputs; does not run any agents."""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
TASKS = {
    "behavior": "Returning from record detail sometimes loses the list state. Fix this according to PRODUCT.md, preserving existing behavior and public tests.",
    "copy": "Change the Save button label to Save draft. Preserve all other behavior and existing public tests.",
}
PROMPT = """Complete this task in the isolated exercise workspace {workspace}:
{task}

Use Engineering Loop at {skill}/SKILL.md and read {guidance} as additional trial guidance. Read the workspace's AGENTS.md. Your shell may initially be in another repository; use the supplied workspace explicitly.
Only inspect or edit that workspace, the supplied read-only skill/guidance, and the trial evidence directory {evidence}. Do not inspect sibling trials, the source repository, evaluator material or prior task conversations. Do not commit, publish or install dependencies. This is a disposable synthetic exercise, not the current root project.
Perform appropriate verification and report passed, failed and unrun checks. Delegation is permitted when useful and available, within the same resource boundaries; it is not required. Keep command/output evidence in {evidence}/commands.txt and write a short final account to {evidence}/agent-report.md, including actual verification, any delegation, questions and known limits. Do not claim access to hidden tests or model telemetry.
Available tools: node and Python; Playwright can be resolved with NODE_PATH={node_modules}. A local browser executable is {browser}. Use these only when useful; the public project test is node --test state.test.cjs.
"""
OVERLAY = """# Trial guidance

Use the supplied skill normally.
"""
CANDIDATE = """
Before deciding whether to delegate, identify the concrete uncertainty an additional contributor would resolve. Delegate only work with an independent useful outcome; settled local work can remain with one agent. No extra planning artifact or approval is required.

When review is warranted, select a material completion claim and seek a concrete supported scenario that could falsify it. Use the relevant evidence, preserve legitimate exceptions, and stop once the claim and required checks are supported. Do not add generic critique or an extra reviewer without an unresolved reason.
"""


def hashes(directory):
    return {p.relative_to(directory).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(directory.rglob("*")) if p.is_file()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--node-modules", required=True)
    parser.add_argument("--browser", required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    if (output / "inputs.json").exists():
        parser.error("A frozen input manifest already exists; choose a new result directory.")
    scratch = Path(tempfile.mkdtemp(prefix="engineering-loop-ui-ab-"))
    trials = {}
    for task, text in TASKS.items():
        for variant in ("A", "B"):
            trial_id = f"{task}-{variant}"
            directory = scratch / trial_id
            workspace = directory / "workspace"
            skill = directory / "skill"
            evidence = directory / "evidence"
            shutil.copytree(ROOT / "evals/fixtures/list-detail", workspace)
            shutil.copytree(ROOT / "skills/engineering-loop", skill)
            evidence.mkdir()
            guidance = directory / "trial-guidance.md"
            guidance.write_text(OVERLAY + (CANDIDATE if variant == "B" else ""), encoding="utf-8")
            prompt = PROMPT.format(workspace=workspace, task=text, skill=skill, guidance=guidance,
                                   evidence=evidence, node_modules=args.node_modules, browser=args.browser)
            (directory / "prompt.txt").write_text(prompt, encoding="utf-8")
            trials[trial_id] = str(directory)
    manifest = {
        "source_revision": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "fixture_hashes": hashes(ROOT / "evals/fixtures/list-detail"),
        "skill_hashes": hashes(ROOT / "skills/engineering-loop"),
        "oracle_sha256": hashlib.sha256((ROOT / "evals/list_detail_oracle.cjs").read_bytes()).hexdigest(),
        "tasks": TASKS, "prompt_template": PROMPT,
        "guidance_A": OVERLAY, "guidance_B": OVERLAY + CANDIDATE,
        "execution_order": ["behavior-A", "copy-B", "behavior-B", "copy-A"],
        "isolation": "Fresh conversation contexts; file access separation is procedural, not a security sandbox.",
    }
    (output / "inputs.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    # Local paths remain outside the committed result artifacts.
    (scratch / "trials.json").write_text(json.dumps(trials, indent=2), encoding="utf-8")
    print(json.dumps({"scratch": str(scratch), "trials": trials}, indent=2))


if __name__ == "__main__":
    main()
