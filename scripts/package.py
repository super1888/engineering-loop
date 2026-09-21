"""Build a deterministic offline skill ZIP with license and no repository history."""

import argparse
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def build_archive(source, output, license_path):
    source = Path(source).resolve()
    output = Path(output).resolve()
    license_path = Path(license_path).resolve()
    if output == source or source in output.parents:
        raise ValueError("Archive output must be outside the skill source")
    if not (source / "SKILL.md").is_file():
        raise ValueError("Source is not a skill directory")
    payload = []
    for path in sorted(source.rglob("*")):
        if path.is_symlink():
            raise ValueError("Symlinks are not accepted in the offline payload")
        if path.is_file():
            payload.append((path.relative_to(source).as_posix(), path.read_bytes()))
    if not any(name == "LICENSE" for name, _ in payload):
        payload.append(("LICENSE", license_path.read_bytes()))
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, data in sorted(payload):
            info = zipfile.ZipInfo(f"engineering-loop/{name}", date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "dist/engineering-loop.zip")
    args = parser.parse_args()
    archive = build_archive(ROOT / "skills/engineering-loop", args.output, ROOT / "LICENSE")
    print(f"Packaged {archive}")
