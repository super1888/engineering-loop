"""Build a deterministic offline skill ZIP with license and no repository history."""

import argparse
from pathlib import Path
import stat
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def build_archive(source, output, license_path):
    source = Path(source).resolve()
    output = Path(output).resolve()
    license_path = Path(license_path).resolve()
    output_exists = output.exists()
    if (output == source or source in output.parents or output == license_path
            or (output_exists and license_path.exists() and output.samefile(license_path))):
        raise ValueError("Archive output must be outside the skill source and must not overwrite the license")
    if not (source / "SKILL.md").is_file():
        raise ValueError("Source is not a skill directory")
    payload = []
    for path in source.rglob("*"):
        if (path.is_symlink() or getattr(path.lstat(), "st_reparse_tag", 0)
                == getattr(stat, "IO_REPARSE_TAG_MOUNT_POINT", -1)):
            raise ValueError("Symlinks and directory junctions are not accepted in the offline payload")
        if path.is_file():
            if output_exists and output.samefile(path):
                raise ValueError("Archive output must not overwrite a skill source file")
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
