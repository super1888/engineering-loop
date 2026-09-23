"""Create matched, disposable workspaces for the bar requirements golden suite."""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile


ROOT = Path(__file__).resolve().parents[1]
SUITE = ROOT / "evals/goldens/bar-boundaries-v1.json"
REFERENCE = "skills/engineering-loop/references/requirements.md"


def hashes(directory: Path) -> dict[str, str]:
    return {path.relative_to(directory).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in sorted(directory.rglob("*")) if path.is_file()
            and ".git" not in path.parts and "__pycache__" not in path.parts and path.suffix != ".pyc"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline-ref", required=True, help="Existing Git revision before the candidate guidance")
    parser.add_argument("--output", type=Path, help="New disposable parent directory")
    args = parser.parse_args()
    root = args.output.resolve() if args.output else Path(tempfile.mkdtemp(prefix="engineering-loop-bar-eval-"))
    if root.exists() and any(root.iterdir()):
        parser.error("Output directory must be empty")
    root.mkdir(parents=True, exist_ok=True)
    suite = json.loads(SUITE.read_text(encoding="utf-8"))
    baseline = subprocess.check_output(["git", "show", f"{args.baseline_ref}:{REFERENCE}"], cwd=ROOT)
    revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    manifest = {"suite": suite["id"], "source_revision": revision,
                "baseline_ref": args.baseline_ref, "candidate_skill_hashes": hashes(ROOT / "skills/engineering-loop"),
                "trials": {}}
    for case in suite["cases"]:
        for arm in ("baseline", "candidate"):
            name = f"{case['id']}-{arm}"
            directory = root / name
            workspace = directory / "workspace"
            shutil.copytree(ROOT / "evals/goldens" / case["fixture"], workspace)
            skill = workspace / ".agents/skills/engineering-loop"
            shutil.copytree(ROOT / "skills/engineering-loop", skill)
            if arm == "baseline":
                (skill / "references/requirements.md").write_bytes(baseline)
            subprocess.run(["git", "init", "--quiet", str(workspace)], check=True)
            subprocess.run(["git", "config", "core.autocrlf", "false"], cwd=workspace, check=True)
            subprocess.run(["git", "add", "."], cwd=workspace, check=True)
            subprocess.run(["git", "-c", "user.name=Engineering Loop Eval",
                            "-c", "user.email=eval@example.invalid", "commit", "--quiet",
                            "-m", "Synthetic baseline"], cwd=workspace, check=True)
            prompt = (
                f"Complete this task in the isolated workspace {workspace}:\n{case['task']}\n\n"
                "Read the workspace's AGENTS.md and relevant skill reference. Only inspect or edit this workspace. "
                "Do not inspect the evaluator, source repository or sibling trials. Do not delegate, commit, "
                "publish or install dependencies. Report the actual result.\n"
            )
            (directory / "prompt.txt").write_text(prompt, encoding="utf-8")
            (directory / "evidence").mkdir()
            manifest["trials"][name] = {"input_hashes": hashes(workspace),
                                       "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest()}
    (root / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(root)


if __name__ == "__main__":
    main()
