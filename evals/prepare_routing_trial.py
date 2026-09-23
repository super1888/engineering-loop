"""Prepare isolated skill-routing trials without running agents."""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "evals/fixtures/skill-routing"
TASKS = {
    "full": "完成订单创建：表单提交商品和数量，后端保存并返回编号，失败时保留输入。遵循项目约定。",
    "backend": "实现后端订单创建与校验，遵循项目约定；前端保持原状。",
}
ROUTING_RULE = (
    "\n- Before implementation, select repository skills by the affected backend/form files. "
    "Read only the matching skills; use both when the requested behavior crosses the API and form. "
    "The user need not name skills or agent roles.\n"
)
TEST_RULE = (
    "\nWhen accepted behavior adds or changes a boundary, add or update one focused "
    "regression in the existing test file unless it already covers that boundary.\n"
)


def hashes(directory: Path) -> dict[str, str]:
    return {path.relative_to(directory).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in sorted(directory.rglob("*")) if path.is_file()
            and ".git" not in path.parts and "__pycache__" not in path.parts and path.suffix != ".pyc"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="New disposable parent directory")
    args = parser.parse_args()
    root = args.output.resolve() if args.output else Path(tempfile.mkdtemp(prefix="engineering-loop-routing-ab-"))
    if root.exists() and any(root.iterdir()):
        parser.error("Output directory must be empty")
    root.mkdir(parents=True, exist_ok=True)
    revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    manifest = {"source_revision": revision, "fixture_hashes": hashes(FIXTURE),
                "skill_hashes": hashes(ROOT / "skills/engineering-loop"),
                "tasks": TASKS, "routing_rule": ROUTING_RULE, "test_rule": TEST_RULE,
                "trials": {}}
    for task_name, task in TASKS.items():
        for variant in ("A", "B", "C"):
            trial_id = f"{task_name}-{variant}"
            directory = root / trial_id
            workspace = directory / "workspace"
            shutil.copytree(FIXTURE, workspace, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            shutil.copytree(ROOT / "skills/engineering-loop", workspace / ".agents/skills/engineering-loop")
            if variant in ("B", "C"):
                with (workspace / "AGENTS.md").open("a", encoding="utf-8") as document:
                    document.write(ROUTING_RULE)
            if variant == "C":
                for skill_name in ("order-backend", "order-form"):
                    skill_file = workspace / ".agents/skills" / skill_name / "SKILL.md"
                    with skill_file.open("a", encoding="utf-8") as document:
                        document.write(TEST_RULE)
            subprocess.run(["git", "init", "--quiet", str(workspace)], check=True)
            subprocess.run(["git", "config", "core.autocrlf", "false"], cwd=workspace, check=True)
            subprocess.run(["git", "add", "."], cwd=workspace, check=True)
            subprocess.run(["git", "-c", "user.name=Engineering Loop Eval",
                            "-c", "user.email=eval@example.invalid", "commit", "--quiet", "-m", "Synthetic baseline"],
                           cwd=workspace, check=True)
            prompt = (
                f"Complete the user's request in the isolated synthetic workspace {workspace}:\n{task}\n\n"
                "Use normal project instructions and skill discovery; the user has not chosen a skill. "
                "Only inspect or edit this workspace. Do not inspect the evaluator, source repository "
                "or sibling trials. Do not delegate, commit, publish or install dependencies in this "
                "controlled trial. Run applicable project checks and report actual results.\n"
            )
            (directory / "prompt.txt").write_text(prompt, encoding="utf-8")
            (directory / "evidence").mkdir()
            manifest["trials"][trial_id] = {"workspace": str(workspace),
                                             "input_hashes": hashes(workspace),
                                             "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest()}
    (root / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(root)


if __name__ == "__main__":
    main()
