"""Record path-neutral evidence from completed synthetic skill-routing trials."""

import argparse
import json
from pathlib import Path
import re
import subprocess
import sys

from routing_oracle import assess
from public_test_results import node_tap_passed, unittest_passed


TRIALS = ("full-A", "full-B", "full-C", "backend-A", "backend-B", "backend-C")


def record(directory: Path, output: Path, name: str) -> dict:
    directory = directory.resolve()
    workspace = directory / "workspace"
    events = [json.loads(line) for line in (directory / "evidence/events.jsonl").read_text(encoding="utf-8").splitlines()]
    completed = [event for event in events if event.get("type") == "turn.completed"]
    if len(completed) != 1:
        raise ValueError(f"Expected one completed turn for {name}")
    commands = [event["item"] for event in events if event.get("type") == "item.completed"
                and event.get("item", {}).get("type") == "command_execution"]
    skills = sorted({match for command in commands for match in
                     re.findall(r"skills[\\/]+([a-z-]+)[\\/]+SKILL\.md", command.get("command", ""), re.I)})
    changed = subprocess.check_output(["git", "diff", "HEAD", "--name-only", "-z"],
                                      cwd=workspace).decode("utf-8").split("\0")[:-1]
    patch = subprocess.check_output(["git", "diff", "HEAD", "--"], cwd=workspace)
    (output / f"{name}.patch").write_bytes(patch)
    messages = [event["item"]["text"] for event in events if event.get("type") == "item.completed"
                and event.get("item", {}).get("type") == "agent_message"]
    final = messages[-1] if messages else ""
    for path in (str(directory.parent), str(directory.parent).replace("\\", "/")):
        final = final.replace(path, "<trial-root>")
    (output / f"{name}-final.txt").write_text(final + "\n", encoding="utf-8")
    backend = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "backend/tests", "-v"],
                             cwd=workspace, capture_output=True, text=True, encoding="utf-8",
                             errors="replace", timeout=30)
    form = None
    if name.startswith("full"):
        form = subprocess.run(["node", "--test", "--test-reporter=tap", "ui/order-form.test.mjs"],
                              cwd=workspace, capture_output=True, text=True, encoding="utf-8",
                              errors="replace", timeout=30)
    oracle = assess(workspace)
    untracked = subprocess.check_output(["git", "ls-files", "--others", "--exclude-standard", "-z"],
                                        cwd=workspace).decode("utf-8").split("\0")[:-1]
    return {"changed_files": changed, "untracked_non_cache": [file for file in untracked
            if "__pycache__" not in file and not file.endswith(".pyc")],
            "skills_read": skills, "usage": completed[0].get("usage"),
            "public_backend_pass": unittest_passed(backend),
            "public_form_pass": None if form is None else node_tap_passed(form, minimum_tests=2),
            "oracle_backend_pass": oracle["backend"] is None,
            "oracle_form_pass": oracle["form"] is None,
            "completed_commands": len(commands),
            "failed_commands": sum(command.get("exit_code") not in (0, None) for command in commands)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ab-root", type=Path, required=True)
    parser.add_argument("--c-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.ab_root = args.ab_root.resolve()
    args.c_root = args.c_root.resolve()
    ab = json.loads((args.ab_root / "manifest.json").read_text(encoding="utf-8"))
    c = json.loads((args.c_root / "manifest.json").read_text(encoding="utf-8"))
    for field in ("source_revision", "fixture_hashes", "skill_hashes", "tasks", "routing_rule"):
        if ab[field] != c[field]:
            raise ValueError(f"Trial input mismatch: {field}")
    normalized_prompts = {}
    for task in ("full", "backend"):
        prompts = []
        for variant in ("A", "B", "C"):
            root = args.c_root if variant == "C" else args.ab_root
            trial = root / f"{task}-{variant}"
            prompt = (trial / "prompt.txt").read_text(encoding="utf-8")
            prompts.append(prompt.replace(str(trial / "workspace"), "<workspace>"))
        if len(set(prompts)) != 1:
            raise ValueError(f"Prompt mismatch: {task}")
        normalized_prompts[task] = prompts[0]
    args.output.mkdir(parents=True, exist_ok=True)
    inputs = {field: ab[field] for field in ("source_revision", "fixture_hashes", "skill_hashes", "tasks", "routing_rule")}
    inputs["test_rule"] = c["test_rule"]
    inputs["normalized_prompts"] = normalized_prompts
    (args.output / "inputs.json").write_text(json.dumps(inputs, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    results = {}
    for name in TRIALS:
        root = args.c_root if name.endswith("-C") else args.ab_root
        results[name] = record(root / name, args.output, name)
    (args.output / "outcomes.json").write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
