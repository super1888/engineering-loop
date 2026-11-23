from datetime import datetime
from pathlib import Path
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "skills/engineering-loop/scripts"))
import collect_feedback


def project(base, name, files):
    folder = Path(base) / name / ".engineering-loop" / "feedback"
    folder.mkdir(parents=True)
    for filename, text in files.items():
        (folder / filename).write_text(text, encoding="utf-8")
    return Path(base) / name


class CollectFeedbackTests(unittest.TestCase):
    def test_bundles_records_and_keeps_the_store_out_of_git(self):
        with tempfile.TemporaryDirectory() as base:
            root = project(base, "shop", {"20261123-101500-missing.md": "# missing: paging\n",
                                          "usage.log": "2026-11-23 | 0.1.36 | 03 / B1 | api.md | none\n",
                                          "notes.txt": "not a record\n"})
            output, count, warnings = collect_feedback.collect([root], now=datetime(2026, 11, 23, 10, 30, 0))
            self.assertEqual(count, 2)
            self.assertEqual(warnings, [])
            self.assertEqual(output, (root / ".engineering-loop/outbox/engineering-loop-feedback-20261123-103000.zip").resolve())
            self.assertEqual((root / ".engineering-loop/.gitignore").read_text(encoding="utf-8"), "*\n")
            with zipfile.ZipFile(output) as archive:
                self.assertEqual(sorted(archive.namelist()), ["shop/20261123-101500-missing.md", "shop/usage.log"])

    def test_several_roots_and_same_folder_names_do_not_collide(self):
        with tempfile.TemporaryDirectory() as base:
            first = project(Path(base) / "a", "api", {"1-missing.md": "one\n"})
            second = project(Path(base) / "b", "api", {"1-missing.md": "two\n"})
            target = Path(base) / "out.zip"
            output, count, _ = collect_feedback.collect([first, second], target)
            self.assertEqual(count, 2)
            with zipfile.ZipFile(output) as archive:
                self.assertEqual(sorted(archive.namelist()), ["api/1-missing.md", "api_/1-missing.md"])
                self.assertEqual(archive.read("api_/1-missing.md"), b"two\n")
            self.assertFalse((first / ".engineering-loop/.gitignore").exists())

    def test_no_records_writes_nothing_and_reports_failure(self):
        with tempfile.TemporaryDirectory() as base:
            self.assertEqual(collect_feedback.collect([base]), (None, 0, []))
            self.assertEqual(collect_feedback.main([base]), 1)
            self.assertFalse((Path(base) / ".engineering-loop").exists())

    def test_secret_like_text_is_flagged_and_strict_mode_stops(self):
        with tempfile.TemporaryDirectory() as base:
            root = project(base, "shop", {"1-conflict.md": "evidence: api_key = abc\n", "2-unused.md": "plain\n"})
            _, count, warnings = collect_feedback.collect([root], Path(base) / "out.zip")
            self.assertEqual(count, 2)
            self.assertEqual([Path(item).name for item in warnings], ["1-conflict.md"])
            strict = Path(base) / "strict.zip"
            self.assertEqual(collect_feedback.main([str(root), "--output", str(strict), "--strict"]), 3)
            self.assertFalse(strict.exists())

    def test_existing_output_is_not_overwritten_and_default_names_do_not_collide(self):
        with tempfile.TemporaryDirectory() as base:
            root = project(base, "shop", {"1-missing.md": "one\n"})
            moment = datetime(2026, 11, 23, 10, 30, 0)
            first, _, _ = collect_feedback.collect([root], now=moment)
            second, _, _ = collect_feedback.collect([root], now=moment)
            self.assertNotEqual(first, second)
            self.assertTrue(second.name.endswith("-2.zip"))
            taken = Path(base) / "taken.zip"
            taken.write_bytes(b"keep")
            self.assertEqual(collect_feedback.main([str(root), "--output", str(taken)]), 2)
            self.assertEqual(taken.read_bytes(), b"keep")
            self.assertEqual(collect_feedback.main([str(root), str(root), "--output", str(Path(base) / "ok.zip")]), 0)
            with zipfile.ZipFile(Path(base) / "ok.zip") as archive:
                self.assertEqual(archive.namelist(), ["shop/1-missing.md"])

    def test_missing_root_and_linked_store_are_refused(self):
        with tempfile.TemporaryDirectory() as base:
            root = project(base, "shop", {"1-missing.md": "one\n"})
            target = Path(base) / "out.zip"
            self.assertEqual(collect_feedback.main([str(Path(base) / "absent"), str(root), "--output", str(target)]), 2)
            outside = Path(base) / "outside"
            outside.mkdir()
            (outside / "private.md").write_text("not a record\n", encoding="utf-8")
            linked = Path(base) / "linked"
            (linked / ".engineering-loop").mkdir(parents=True)
            try:
                (linked / ".engineering-loop" / "feedback").symlink_to(outside, target_is_directory=True)
            except OSError:
                self.skipTest("symbolic links are unavailable")
            self.assertEqual(collect_feedback.main([str(linked), "--output", str(target)]), 2)
            self.assertFalse(target.exists())


if __name__ == "__main__":
    unittest.main()
