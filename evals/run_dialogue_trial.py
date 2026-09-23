"""Run a frozen multi-turn skill dialogue in fresh disposable Codex workspaces."""

import argparse
import getpass
import hashlib
import json
from pathlib import Path
import platform
import shutil
import subprocess
from datetime import datetime, timezone


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_turn(command: list[str], workspace: Path, output: Path, replacements: dict[str, str]) -> dict:
    result = subprocess.run(command, cwd=workspace, capture_output=True, text=True,
                            encoding="utf-8", errors="replace", timeout=360)
    stdout = result.stdout
    stderr = result.stderr
    for original, replacement in replacements.items():
        stdout = stdout.replace(original, replacement)
        stderr = stderr.replace(original, replacement)
    (output / "events.jsonl").write_text(stdout, encoding="utf-8")
    (output / "stderr.txt").write_text(stderr, encoding="utf-8")
    events = [json.loads(line) for line in result.stdout.splitlines() if line.strip()]
    started = next((event for event in events if event.get("type") == "thread.started"), {})
    completed = next((event for event in reversed(events)
                      if event.get("type") == "turn.completed"), {})
    commands = [event["item"] for event in events if event.get("type") == "item.completed"
                and event.get("item", {}).get("type") == "command_execution"]
    return {"exit_code": result.returncode, "thread_id": started.get("thread_id"),
            "usage": completed.get("usage"), "commands": len(commands),
            "declined_commands": sum(item.get("status") == "declined" for item in commands)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--suite", type=Path, required=True)
    parser.add_argument("--skill", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--case", action="append", help="Run only these case IDs")
    args = parser.parse_args()
    suite = json.loads(args.suite.read_text(encoding="utf-8"))
    cases = [case for case in suite["cases"] if not args.case or case["id"] in args.case]
    if not cases or (args.case and len(cases) != len(set(args.case))):
        parser.error("Unknown or duplicate case ID")
    output = args.output.resolve()
    if output.exists() and any(output.iterdir()):
        parser.error("Output directory must be empty")
    output.mkdir(parents=True, exist_ok=True)
    skill = args.skill.resolve()
    skill_hashes = {path.relative_to(skill).as_posix(): sha256(path)
                    for path in sorted(skill.rglob("*")) if path.is_file()}
    cli = shutil.which("codex")
    if not cli:
        parser.error("codex CLI is unavailable")
    version = subprocess.check_output([cli, "--version"], text=True, encoding="utf-8").strip()
    manifest = {"suite": suite["id"], "suite_sha256": sha256(args.suite),
                "started_utc": datetime.now(timezone.utc).isoformat(),
                "host": platform.platform(), "cli_version": version,
                "model": "account default; identity not exposed by CLI JSON events",
                "skill_hashes": skill_hashes, "cases": {}}
    replacements = {getpass.getuser(): "<user>", str(output): "<TRIAL_ROOT>"}
    for case in cases:
        case_dir = output / case["id"]
        workspace = case_dir / "workspace"
        target_skill = workspace / ".agents/skills/engineering-loop"
        target_skill.parent.mkdir(parents=True)
        shutil.copytree(skill, target_skill)
        case_record = {"prompts": case["turns"], "turns": []}
        manifest["cases"][case["id"]] = case_record
        thread_id = None
        for number, prompt in enumerate(case["turns"], start=1):
            turn_dir = case_dir / f"turn{number}"
            turn_dir.mkdir()
            final_path = turn_dir / "final.txt"
            if number == 1:
                command = [cli, "exec", "--json", "--ignore-user-config",
                           "--skip-git-repo-check", "--sandbox", "read-only",
                           "-c", 'approval_policy="never"', "--cd", str(workspace),
                           "--output-last-message", str(final_path), prompt]
            else:
                command = [cli, "exec", "resume", "--json", "--ignore-user-config",
                           "--skip-git-repo-check", "-c", 'approval_policy="never"',
                           "--output-last-message", str(final_path), thread_id, prompt]
            print(f"{case['id']} turn {number}", flush=True)
            record = run_turn(command, workspace, turn_dir, replacements)
            case_record["turns"].append(record)
            thread_id = record["thread_id"] or thread_id
            if record["exit_code"] != 0 or not thread_id or not final_path.exists():
                (output / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False,
                                                                 indent=2) + "\n", encoding="utf-8")
                raise RuntimeError(f"{case['id']} turn {number} did not complete; see {turn_dir}")
        case_record["workspace_files"] = [path.relative_to(workspace).as_posix()
                                          for path in sorted(workspace.rglob("*")) if path.is_file()]
        (output / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False,
                                                         indent=2) + "\n", encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
