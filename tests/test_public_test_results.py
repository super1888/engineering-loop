from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "evals"))
from public_test_results import unittest_passed


class PublicTestResultTests(unittest.TestCase):
    def test_diagnostic_ok_does_not_replace_the_native_terminal_summary(self):
        for decorator, body, expected in (("", "pass", True),
                                          ('@unittest.skip("not executed")', "pass", False),
                                          ("@unittest.expectedFailure", 'self.fail("control")', False)):
            with self.subTest(decorator=decorator), tempfile.TemporaryDirectory() as directory:
                (Path(directory) / "test_native.py").write_text(
                    'import sys, unittest\nprint("OK", file=sys.stderr)\n'
                    'class Checks(unittest.TestCase):\n'
                    f'    {decorator}\n    def test_boundary(self):\n        {body}\n',
                    encoding="utf-8")
                result = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", directory, "-v"],
                                        capture_output=True, text=True, timeout=15)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(unittest_passed(result), expected, result.stderr)


if __name__ == "__main__":
    unittest.main()
