import hashlib
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
            with self.assertRaises(ValueError):
                build_archive(source, source / "SKILL.md", ROOT / "LICENSE")
            self.assertEqual((source / "SKILL.md").read_bytes(), before)

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


if __name__ == "__main__":
    unittest.main()
