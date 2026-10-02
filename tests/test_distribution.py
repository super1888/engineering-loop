import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from check import check
from package import build_archive


class DistributionTests(unittest.TestCase):
    def test_local_links_and_metadata(self):
        self.assertEqual(check(), [])

    def test_skill_frontmatter_cannot_be_supplied_by_documentation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in ("skills", ".claude-plugin"):
                shutil.copytree(ROOT / name, root / name)
            (root / "evals").mkdir()
            shutil.copyfile(ROOT / "evals/cases.json", root / "evals/cases.json")
            entry = root / "skills/engineering-loop/SKILL.md"
            version = json.loads((root / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))["version"]
            original = ('---\nname: engineering-loop\ndescription: Metadata fixture.\n'
                        f'metadata:\n  version: "{version}"\n---\n')
            valid = original.replace("metadata:\n", "metadata:\n  note: distribution control\n", 1)
            valid = valid.replace(f'  version: "{version}"', f'  version: "{version}" # local version', 1)
            entry.write_text(valid + '\nExample version: "999.0.0"\n', encoding="utf-8")
            self.assertEqual(check(root), [])
            missing_description = original.replace("description: Metadata fixture.\n", "", 1)
            entry.write_text(missing_description + "\ndescription: Documentation example.\n", encoding="utf-8")
            self.assertIn("Missing skill description", check(root))
            for empty_value in ("", " ", "   ", "\t ", "# metadata note", "  # metadata note", "\t # metadata note",
                                '""', "''", '" \t "', "' \t '", "~", "null", "Null", "NULL", "null # missing value"):
                with self.subTest(description_value=empty_value):
                    blank_description = original.replace("Metadata fixture.", empty_value, 1)
                    entry.write_text(blank_description + "\ndescription: Documentation example.\n", encoding="utf-8")
                    self.assertIn("Missing skill description", check(root))
            for description in ("  Metadata fixture.", "'# useful description'", '"# useful description"',
                                '"null"', "'~'", "null#literal", "Metadata fixture. # inline comment"):
                with self.subTest(valid_description=description):
                    entry.write_text(original.replace("Metadata fixture.", description, 1), encoding="utf-8")
                    self.assertEqual(check(root), [])
            mismatch = original.replace(f'  version: "{version}"', '  version: "999.0.0"', 1)
            for location in ("body", "description"):
                with self.subTest(location=location):
                    if location == "body":
                        content = mismatch + f'\nExample version: "{version}"\n'
                    else:
                        lines = mismatch.splitlines()
                        lines[2] = f'description: \'Notes on version: "{version}"\''
                        content = "\n".join(lines) + "\n"
                    entry.write_text(content, encoding="utf-8")
                    self.assertIn("Skill and plugin versions disagree", check(root))

    def test_archive_is_complete_and_contains_only_skill_and_license(self):
        source = ROOT / "skills/engineering-loop"
        with tempfile.TemporaryDirectory() as directory:
            output = build_archive(source, Path(directory) / "skill.zip", ROOT / "LICENSE")
            with zipfile.ZipFile(output) as archive:
                expected = {"engineering-loop/" + p.relative_to(source).as_posix()
                            for p in source.rglob("*") if p.is_file()}
                expected.add("engineering-loop/LICENSE")
                self.assertEqual(set(archive.namelist()), expected)
                self.assertIsNone(archive.testzip())
                for path in source.rglob("*"):
                    if path.is_file():
                        self.assertEqual(archive.read("engineering-loop/" + path.relative_to(source).as_posix()),
                                         path.read_bytes())
                self.assertEqual(archive.read("engineering-loop/LICENSE"), (ROOT / "LICENSE").read_bytes())

    def test_repeated_build_is_identical(self):
        with tempfile.TemporaryDirectory() as directory:
            outputs = [build_archive(ROOT / "skills/engineering-loop", Path(directory) / name, ROOT / "LICENSE")
                       for name in ("first.zip", "second.zip")]
            self.assertEqual(*(hashlib.sha256(p.read_bytes()).hexdigest() for p in outputs))

    def test_output_cannot_overwrite_source(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source"
            shutil.copytree(ROOT / "skills/engineering-loop", source)
            before = (source / "SKILL.md").read_bytes()
            license_path = Path(directory) / "LICENSE"
            license_bytes = (ROOT / "LICENSE").read_bytes()
            license_path.write_bytes(license_bytes)
            for output in (source / "SKILL.md", license_path):
                with self.subTest(output=output), self.assertRaises(ValueError):
                    build_archive(source, output, license_path)
            self.assertEqual((source / "SKILL.md").read_bytes(), before)
            self.assertEqual(license_path.read_bytes(), license_bytes)

    def test_external_symlink_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source"
            source.mkdir()
            (source / "SKILL.md").write_text("example", encoding="utf-8")
            try:
                (source / "outside.txt").symlink_to(ROOT / "README.md")
            except OSError:
                self.skipTest("Host does not permit creating a test symlink")
            with self.assertRaises(ValueError):
                build_archive(source, Path(directory) / "skill.zip", ROOT / "LICENSE")

    def test_output_hardlinks_cannot_overwrite_inputs(self):
        for relative in ("SKILL.md", "references/review.md", "LICENSE"):
            with self.subTest(input=relative), tempfile.TemporaryDirectory() as directory:
                source = Path(directory) / "source"
                shutil.copytree(ROOT / "skills/engineering-loop", source)
                license_path = Path(directory) / "LICENSE"
                license_path.write_bytes((ROOT / "LICENSE").read_bytes())
                protected = license_path if relative == "LICENSE" else source / relative
                before = protected.read_bytes()
                output = Path(directory) / "skill.zip"
                try:
                    output.hardlink_to(protected)
                except OSError:
                    self.skipTest("Host does not permit creating a test hardlink")
                with self.assertRaises(ValueError):
                    build_archive(source, output, license_path)
                self.assertEqual(protected.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
