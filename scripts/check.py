"""Dependency-free distribution checks; not a model behavior evaluation."""

import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def check(root=ROOT):
    errors = []
    skill = root / "skills/engineering-loop"
    entry = skill / "SKILL.md"
    text = entry.read_text(encoding="utf-8")
    if not text.startswith("---\nname: engineering-loop\n"):
        errors.append("Missing expected skill name/frontmatter")
    if not re.search(r"^description: .+", text, re.M):
        errors.append("Missing skill description")
    # A packaging budget, not a token estimate or a runtime guarantee.
    if len(text.encode("utf-8")) > 7000:
        errors.append("Entrypoint exceeds the 7 KB maintenance budget")
    for path in skill.rglob("*"):
        if path.is_symlink():
            errors.append(f"Skill payload must be self-contained: {path.relative_to(root)}")
    for path in root.rglob("*.md"):
        if any(part in {".git", "dist", "node_modules"} for part in path.parts):
            continue
        content = path.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^\s)]+)\)", content):
            if "://" in target or target.startswith(("#", "mailto:")):
                continue
            target = target.split("#", 1)[0]
            if target and not (path.parent / target).is_file():
                errors.append(f"Broken link in {path.relative_to(root)}: {target}")
    for path in root.rglob("*.json"):
        if not any(part in {".git", "dist", "node_modules"} for part in path.parts):
            json.loads(path.read_text(encoding="utf-8"))
    plugin = json.loads((root / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
    market = json.loads((root / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
    if plugin["name"] != "engineering-loop" or market["plugins"][0]["name"] != plugin["name"]:
        errors.append("Plugin and marketplace names disagree")
    if f'version: "{plugin["version"]}"' not in text:
        errors.append("Skill and plugin versions disagree")
    if market["plugins"][0]["source"] != "./":
        errors.append("Marketplace must resolve to the root plugin")
    cases = json.loads((root / "evals/cases.json").read_text(encoding="utf-8"))
    ids = [case["id"] for case in cases["cases"]]
    if len(ids) != len(set(ids)):
        errors.append("Duplicate evaluation case IDs")
    for case in cases["cases"]:
        if not case["prompt"] or not case["fixture_description"] or not case["expectations"]:
            errors.append(f"Incomplete evaluation scenario: {case['id']}")
    return errors


if __name__ == "__main__":
    failures = check()
    for failure in failures:
        print(f"ERROR: {failure}")
    if failures:
        sys.exit(1)
    print("Distribution checks passed. Model behavior was not evaluated.")
