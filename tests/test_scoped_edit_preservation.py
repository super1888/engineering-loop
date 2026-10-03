from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


# Anonymous source-shaped bytes, not a compiled Java or model-behavior fixture.
ORIGINAL = (
    b"import java.util.List;\r\n"
    b"\n"
    b"class ReplayTest {\r\n"
    b'  // Keep every existing business assertion.\n'
    b'  String cases = "matching,missing,wrong-key";\r\n'
    b"  void matchingReplay() {\n"
    b"    verify(ordinary, times(2));\r\n"
    b"    verify(current, never());\n"
    b"    assertEquals(winner.id(), response.id());\r\n"
    b"    assertEquals(winner.children(), response.children());\n"
    b"  }\r\n"
    b"}\n"
)
EDITS = (
    (b"import java.util.List;\r\n",
     b"import java.util.List;\r\nimport java.util.function.Supplier;\n"),
    (b"verify(ordinary, times(2));", b"verify(ordinary, times(1));"),
    (b"verify(current, never());", b"verify(current, times(1));"),
    (b"class ReplayTest {\r\n",
     b"class ReplayTest {\r\n  void committedWinnerRegression() {\n"
     b"    assertEquals(winner, replay());\n  }\n"),
)


def apply_declared_edits(content):
    for old, new in EDITS:
        if content.count(old) != 1:
            raise ValueError("declared original edit is not unique")
        content = content.replace(old, new, 1)
    return content


def undo_declared_edits(content, *, normalize=False):
    for old, new in reversed(EDITS):
        if normalize:
            old, new = old.replace(b"\r\n", b"\n"), new.replace(b"\r\n", b"\n")
        if content.count(new) != 1:
            raise ValueError("declared candidate edit is missing or not unique")
        content = content.replace(new, old, 1)
    return content


class ScopedEditPreservationTests(unittest.TestCase):
    def test_declared_edits_restore_all_original_bytes_and_assertions(self):
        approved = apply_declared_edits(ORIGINAL)
        self.assertEqual(undo_declared_edits(approved), ORIGINAL)
        for removed in (b'"matching,missing,wrong-key"',
                        b"assertEquals(winner.children(), response.children());"):
            with self.subTest(removed=removed):
                weakened = approved.replace(removed, b"", 1)
                self.assertNotEqual(undo_declared_edits(weakened), ORIGINAL)

    @unittest.skipUnless(shutil.which("git"), "Git is unavailable; normalization reproduction was not run")
    def test_text_round_trip_changes_frozen_bytes_hidden_by_normalized_git_diff(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)

            def git(*args):
                result = subprocess.run(["git", *args], cwd=root, capture_output=True, timeout=15)
                self.assertEqual(result.returncode, 0, result.stderr.decode("utf-8", errors="replace"))
                return result.stdout

            git("init", "--quiet")
            (root / ".gitattributes").write_bytes(b"*.java text eol=lf\n")
            candidate = root / "ReplayTest.java"
            candidate.write_bytes(ORIGINAL)
            git("add", "--", ".gitattributes", "ReplayTest.java")
            approved = apply_declared_edits(ORIGINAL)
            candidate.write_bytes(approved)
            reviewed_diff = git("diff", "--", "ReplayTest.java")
            self.assertTrue(reviewed_diff)

            # Explicit LF output makes the read/write failure reproducible on Windows too.
            candidate.write_text(candidate.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")
            normalized = candidate.read_bytes()
            self.assertNotEqual(normalized, approved)
            self.assertEqual(git("diff", "--", "ReplayTest.java"), reviewed_diff)
            with self.assertRaisesRegex(ValueError, "missing"):
                undo_declared_edits(normalized)
            # Even accepting equivalent edit tokens cannot restore the frozen remainder.
            self.assertNotEqual(undo_declared_edits(normalized, normalize=True), ORIGINAL)

    def test_formatting_and_semantic_only_controls_do_not_require_original_endings(self):
        approved = apply_declared_edits(ORIGINAL).replace(b"\r\n", b"\n")
        restored = undo_declared_edits(approved, normalize=True)
        self.assertEqual(restored, ORIGINAL.replace(b"\r\n", b"\n"))
        # Both controls allow the normalized original text; neither allows lost assertions.
        weakened = approved.replace(b"assertEquals(winner.children(), response.children());", b"", 1)
        self.assertNotEqual(undo_declared_edits(weakened, normalize=True), restored)


if __name__ == "__main__":
    unittest.main()
