"""Freeze matched old/current skill trials; never runs model agents."""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "evals/fixtures/convention-boundary"
TASKS = {
    "amount": "Fix the order amount limit according to ORDER.md and this project's conventions.",
    "comment": "Correct the false uppercase-only comment in format_reference. Keep the order amount behavior unchanged.",
}


def git_output(*args: str) -> bytes:
    return subprocess.check_output(["git", *args], cwd=ROOT)


def copy_skill_revision(revision: str, destination: Path) -> None:
    paths = git_output("ls-tree", "-r", "--name-only", revision, "skills/engineering-loop").decode().splitlines()
    for path in paths:
        target = destination / Path(path).relative_to("skills/engineering-loop")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(git_output("show", f"{revision}:{path}"))


def hashes(directory: Path) -> dict[str, str]:
    return {path.relative_to(directory).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in sorted(directory.rglob("*"))
            if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", default="HEAD^", help="Prior committed skill revision")
    parser.add_argument("--style-skill", type=Path, help="Optional competing style skill for both variants")
    args = parser.parse_args()
    if args.style_skill and not (args.style_skill / "SKILL.md").is_file():
        parser.error("--style-skill must name a skill directory containing SKILL.md")
    baseline = git_output("rev-parse", args.baseline).decode().strip()
    candidate = git_output("rev-parse", "HEAD").decode().strip()
    root = Path(tempfile.mkdtemp(prefix="engineering-loop-convention-ab-"))
    variants = {"A": baseline, "B": candidate}
    tasks = dict(TASKS)
    if args.style_skill:
        tasks["amount"] = "Simplify order validation while raising its amount limit as approved in ORDER.md. Preserve this project's conventions."
    manifest = {"baseline": baseline, "candidate": candidate, "tasks": tasks,
                "style_skill": args.style_skill.name if args.style_skill else None,
                "fixture_hashes": hashes(FIXTURE), "trials": {}}
    for task_name, task in tasks.items():
        for variant, revision in variants.items():
            trial_id = f"{task_name}-{variant}"
            directory = root / trial_id
            workspace = directory / "workspace"
            skill = directory / "skill"
            shutil.copytree(FIXTURE, workspace, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            subprocess.run(["git", "init", "--quiet", str(workspace)], check=True)
            subprocess.run(["git", "config", "core.autocrlf", "false"], cwd=workspace, check=True)
            subprocess.run(["git", "add", "."], cwd=workspace, check=True)
            subprocess.run(["git", "-c", "user.name=Engineering Loop Eval",
                            "-c", "user.email=eval@example.invalid", "commit", "--quiet", "-m", "Synthetic baseline"],
                           cwd=workspace, check=True)
            copy_skill_revision(revision, skill)
            style_instruction = (f"Also use the coding-style skill at {args.style_skill / 'SKILL.md'} "
                                 "in its default full mode.\n" if args.style_skill else "")
            prompt = (
                f"Complete the following user request in the isolated exercise workspace {workspace}:\n"
                f"{task}\n\n"
                f"Read the workspace AGENTS.md and use Engineering Loop at {skill / 'SKILL.md'}. "
                f"{style_instruction}"
                "This is a disposable synthetic exercise. Only inspect or edit the supplied workspace "
                "and read-only skill snapshot. Do not inspect the source repository, sibling trials, "
                "the evaluator, or prior conversations. Do not commit, publish, install dependencies, "
                "or delegate. Run the project's relevant public check and report what actually passed.\n"
            )
            (directory / "prompt.txt").write_text(prompt, encoding="utf-8")
            (directory / "evidence").mkdir()
            manifest["trials"][trial_id] = {"workspace": str(workspace),
                                             "skill_revision": revision,
                                             "skill_hashes": hashes(skill),
                                             "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest()}
    (root / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(root)


if __name__ == "__main__":
    main()
