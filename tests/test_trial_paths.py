"""Summary normalization preserves unrelated path identities."""
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'evals'))
from trial_paths import neutralize_trial_paths


class TrialPathTests(unittest.TestCase):
    def test_root_text_inside_another_path_is_not_rewritten(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for spelling in {str(root), str(root.resolve())}:
                for prefix in ('/archive', 'another', '.', '~', 'C:'):
                    with self.subTest(root=spelling, prefix=prefix):
                        message = prefix + spelling + '/trial/workspace'
                        self.assertEqual(neutralize_trial_paths(message, root / 'trial'), message)
                sibling = spelling + '-other/trial/workspace'
                self.assertEqual(neutralize_trial_paths(sibling, root / 'trial'), sibling)

    def test_standalone_roots_and_punctuation_remain_normalized(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for spelling in {str(root), str(root.resolve())}:
                for before, after in (('', ''), ('See ', '.'), ('("', '")'), ('path: ', '/trial/workspace')):
                    with self.subTest(root=spelling, before=before, after=after):
                        self.assertEqual(neutralize_trial_paths(before + spelling + after, root / 'trial'),
                                         before + '<trial-root>' + after)


if __name__ == '__main__':
    unittest.main()
