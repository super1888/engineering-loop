"""Bundle local skill-feedback records into one ZIP for the maintainer. Sends nothing."""

import argparse
from datetime import datetime
from pathlib import Path
import re
import sys
import zipfile

STORE = ".engineering-loop"
# A coarse reminder, not a scanner: it cannot recognise personal or business data.
SUSPECT = re.compile(
    r"(?i)(password\s*[:=]|passwd|secret\s*[:=]|api[_-]?key|access[_-]?key|private[_-]?key"
    r"|bearer\s+[a-z0-9._-]{8,}|token\s*[:=]|sk-[a-z0-9]{8,}|ghp_[a-z0-9]{8,}|AKIA[0-9A-Z]{8,}"
    r"|eyJ[a-z0-9_-]{8,}\.[a-z0-9_-]{8,}|://[^/\s:@]+:[^/\s@]+@|-----BEGIN)")


class CollectError(Exception):
    """A problem the person must fix before a bundle can be written."""


def ensure_ignored(store):
    """Make the store ignore itself without touching any tracked file."""
    ignore = store / ".gitignore"
    if not ignore.exists():
        ignore.write_text("*\n", encoding="utf-8")


def find_records(root):
    store = Path(root) / STORE
    folder = store / "feedback"
    if store.is_symlink() or folder.is_symlink():
        raise CollectError(f"Refusing to follow a symbolic link: {folder}")
    if not folder.is_dir():
        return []
    return sorted(path for path in folder.iterdir()
                  if path.is_file() and not path.is_symlink() and path.suffix in {".md", ".log"})


def looks_secret(path):
    return bool(SUSPECT.search(path.read_text(encoding="utf-8", errors="replace")))


def unique_roots(roots):
    resolved = []
    for root in roots:
        path = Path(root).resolve()
        if not path.is_dir():
            raise CollectError(f"Not a directory: {root}")
        if path not in resolved:
            resolved.append(path)
    return resolved


def collect(roots, output=None, now=None):
    roots = unique_roots(roots)
    entries, warnings, seen = [], [], set()
    for root in roots:
        label = root.name or "project"
        while label in seen:
            label += "_"
        seen.add(label)
        for path in find_records(root):
            if looks_secret(path):
                warnings.append(str(path))
            entries.append((f"{label}/{path.name}", path.read_text(encoding="utf-8", errors="replace")))
    if not entries:
        return None, 0, warnings
    if output is None:
        store = roots[0] / STORE
        store.mkdir(exist_ok=True)
        ensure_ignored(store)
        stamp = (now or datetime.now()).strftime("%Y%m%d-%H%M%S")
        output = store / "outbox" / f"engineering-loop-feedback-{stamp}.zip"
        number = 2
        while output.exists():
            output = output.with_name(f"engineering-loop-feedback-{stamp}-{number}.zip")
            number += 1
    output = Path(output).resolve()
    if output.exists():
        raise CollectError(f"Output already exists and is not overwritten: {output}")
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "x", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, text in entries:
            archive.writestr(name, text)
    return output, len(entries), warnings


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("roots", nargs="*", default=["."], help="project roots to collect from (default: current directory)")
    parser.add_argument("--output", type=Path, help="ZIP path (default: <first root>/.engineering-loop/outbox/)")
    parser.add_argument("--strict", action="store_true", help="stop without writing when a record looks like it holds a secret")
    args = parser.parse_args(argv)
    try:
        if args.strict:
            suspects = [str(path) for root in unique_roots(args.roots) for path in find_records(root) if looks_secret(path)]
            if suspects:
                print("Possible secrets; nothing was bundled:\n  " + "\n  ".join(suspects))
                return 3
        output, count, warnings = collect(args.roots, args.output)
    except CollectError as error:
        print(f"Nothing was bundled. {error}")
        return 2
    if warnings:
        print("Review before sending; these may hold a secret:\n  " + "\n  ".join(warnings))
    if not count:
        print(f"No feedback records found under {STORE}/feedback/ in: " + ", ".join(map(str, args.roots)))
        return 1
    print(f"Bundled {count} file(s) into {output}")
    print("Nothing was sent. Read the bundle, then pass it to the skill maintainer yourself.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
