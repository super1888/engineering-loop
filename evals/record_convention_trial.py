"""Save path-neutral artifacts from completed local convention trials."""

import argparse
import difflib
import json
from pathlib import Path

from convention_oracle import assess, assess_comment_control


FIXTURE = Path(__file__).resolve().parent / "fixtures/convention-boundary"


def run_result(directory: Path, output: Path, name: str) -> dict:
    events = [json.loads(line) for line in (directory / "evidence/events.jsonl").read_text(encoding="utf-8").splitlines()]
    completed = [event for event in events if event.get("type") == "turn.completed"]
    if len(completed) != 1:
        raise ValueError(f"Expected one completed turn: {name}")
    messages = [event["item"]["text"] for event in events
                if event.get("type") == "item.completed"
                and event.get("item", {}).get("type") == "agent_message"]
    workspace = directory / "workspace"
    patch = []
    changed = []
    paths = {path.relative_to(FIXTURE) for path in FIXTURE.rglob("*")
             if path.is_file() and path.suffix in {".py", ".md"} and "__pycache__" not in path.parts}
    paths |= {path.relative_to(workspace) for path in workspace.rglob("*")
              if path.is_file() and path.suffix in {".py", ".md"}
              and ".git" not in path.parts and "__pycache__" not in path.parts}
    for relative in sorted(paths):
        source = FIXTURE / relative
        target = workspace / relative
        before = source.read_text(encoding="utf-8").splitlines(keepends=True) if source.exists() else []
        after = target.read_text(encoding="utf-8").splitlines(keepends=True) if target.exists() else []
        if before != after:
            changed.append(relative.as_posix())
            patch.extend(difflib.unified_diff(before, after,
                                              fromfile="a/" + relative.as_posix(),
                                              tofile="b/" + relative.as_posix()))
    (output / f"{name}.patch").write_text("".join(patch), encoding="utf-8")
    final_message = messages[-1] if messages else ""
    trial_root = str(directory.parent)
    for location in (trial_root, trial_root.replace("\\", "/")):
        final_message = final_message.replace(location, "<trial-root>")
    (output / f"{name}-final.txt").write_text(final_message + "\n", encoding="utf-8")
    commands = [event["item"] for event in events if event.get("type") == "item.completed"
                and event.get("item", {}).get("type") == "command_execution"]
    oracle_failures = (assess_comment_control if name.startswith("comment") else assess)(workspace)
    return {"changed_files": changed, "usage": completed[0].get("usage"),
            "oracle_failures": oracle_failures,
            "completed_commands": len(commands),
            "failed_commands": sum(command.get("exit_code") not in (0, None) for command in commands)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--amount-root", type=Path, required=True)
    parser.add_argument("--comment-root", type=Path, required=True)
    parser.add_argument("--style-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    roots = {"amount-A": args.amount_root, "amount-B": args.amount_root,
             "comment-A": args.comment_root, "comment-B": args.comment_root,
             "style-A": args.style_root, "style-B": args.style_root}
    manifests = [json.loads((root / "manifest.json").read_text(encoding="utf-8"))
                 for root in (args.amount_root, args.comment_root, args.style_root)]
    if len({(manifest["baseline"], manifest["candidate"],
             json.dumps(manifest["fixture_hashes"], sort_keys=True)) for manifest in manifests}) != 1:
        raise ValueError("Trial roots have different revisions or fixture inputs")
    inputs = {"baseline": manifests[0]["baseline"], "candidate": manifests[0]["candidate"],
              "fixture_hashes": manifests[0]["fixture_hashes"],
              "standard_tasks": manifests[0]["tasks"], "style_tasks": manifests[2]["tasks"],
              "style_skill": manifests[2]["style_skill"]}
    (args.output / "inputs.json").write_text(json.dumps(inputs, indent=2) + "\n", encoding="utf-8")
    results = {}
    for name, root in roots.items():
        trial_id = name.replace("style", "amount")
        results[name] = run_result(root / trial_id, args.output, name)
    (args.output / "outcomes.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
