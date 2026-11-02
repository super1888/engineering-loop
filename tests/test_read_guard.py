"""Read restriction probes are tool controls, not model evaluations."""
from pathlib import Path
import json
import platform
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'evals'))
from read_guard import run_guarded


class ReadGuardTests(unittest.TestCase):
    def test_unsupported_platform_never_dispatches(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); work = root/'work'; work.mkdir(); denied = root/'denied'; denied.mkdir()
            with patch('read_guard.platform.system', return_value='Unsupported'), patch('read_guard.subprocess.run') as run:
                with self.assertRaises(RuntimeError):
                    run_guarded(['ignored'], work, [denied], root/'receipt')
                run.assert_not_called()

    def test_stale_receipt_is_rejected_without_dispatch(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory); receipt=root/'receipt'; receipt.write_text('old')
            work=root/'work'; work.mkdir(); denied=root/'denied'; denied.mkdir()
            with patch('read_guard.subprocess.run') as run:
                with self.assertRaises(ValueError):
                    run_guarded(['ignored'], work, [denied], receipt)
                run.assert_not_called()
            self.assertEqual(receipt.read_text(), 'old')

    def test_workspace_cannot_be_denied(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); work = root/'work'; work.mkdir()
            with patch('read_guard.subprocess.run') as run:
                with self.assertRaises(ValueError):
                    run_guarded(['ignored'], work, [root], root/'receipt')
                run.assert_not_called()

    @unittest.skipUnless(platform.system() == 'Darwin', 'macOS seatbelt control')
    def test_probe_failure_never_runs_target(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); work = root/'work'; work.mkdir(); denied = root/'denied'; denied.mkdir()
            with patch('read_guard.subprocess.run', return_value=subprocess.CompletedProcess([], 1)) as run:
                with self.assertRaises(RuntimeError):
                    run_guarded(['must-not-run'], work, [denied], root/'receipt')
                self.assertEqual(run.call_count, 1)
            self.assertEqual(list(denied.iterdir()), [])

    @unittest.skipUnless(platform.system() == 'Darwin', 'macOS seatbelt control')
    def test_zero_exit_without_completion_never_dispatches(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory); work=root/'work'; work.mkdir(); denied=root/'denied'; denied.mkdir()
            with patch('read_guard.subprocess.run', return_value=subprocess.CompletedProcess([], 0, stdout=b'')) as run:
                with self.assertRaises(RuntimeError):
                    run_guarded(['must-not-run'], work, [denied], root/'receipt')
                self.assertEqual(run.call_count, 1)

    @unittest.skipUnless(platform.system() == 'Darwin', 'macOS seatbelt control')
    def test_real_policy_denies_both_roots_and_preserves_argv_and_exit(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); work = root/'work'; work.mkdir()
            roots = [root/'hidden one', root/'隐藏 "two"']
            for hidden in roots:
                hidden.mkdir(); (hidden/'oracle.txt').write_text('SYNTHETIC')
            receipt = root/'receipt.json'
            code = '''import pathlib,sys
for path in sys.argv[1:3]:
 try: pathlib.Path(path).read_text()
 except PermissionError: pass
 else: raise SystemExit(29)
assert sys.argv[3] == 'literal; $(not-a-command)'
pathlib.Path('target-output').write_text('OK')
raise SystemExit(7)
'''
            result = run_guarded([sys.executable, '-c', code, *[str(p/'oracle.txt') for p in roots],
                'literal; $(not-a-command)'], work, roots, receipt)
            self.assertEqual(result, 7)
            self.assertEqual((work/'target-output').read_text(), 'OK')
            report = json.loads(receipt.read_text())
            self.assertTrue(report['probe_passed'])
            self.assertEqual(report['command_exit_code'], 7)
            for hidden in roots:
                self.assertEqual([p.name for p in hidden.iterdir()], ['oracle.txt'])

    @unittest.skipUnless(platform.system() == 'Darwin', 'macOS seatbelt control')
    def test_probe_uses_resolved_interpreter_without_reopening_denied_paths(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); work = root/'work'; work.mkdir()
            denied = root/'denied'; denied.mkdir()
            external = Path(sys.executable).resolve()
            alias = denied/'python-alias'; alias.symlink_to(external)
            parent = subprocess.run([str(alias), '-c', "print('PARENT-READY')"],
                                    capture_output=True, text=True, check=True)
            self.assertEqual(parent.stdout.strip(), 'PARENT-READY')
            script = denied/'hidden.py'; script.write_text('HIDDEN', encoding='utf-8')
            code = "import pathlib,sys\ntry: pathlib.Path(sys.argv[1]).read_bytes()\nexcept PermissionError: pass\nelse: raise SystemExit(31)\npathlib.Path('ran').write_text('OK')"
            with patch('read_guard.sys.executable', str(alias)):
                result = run_guarded([str(external), '-c', code, str(script)], work,
                                     [denied], root/'receipt.json')
            self.assertEqual(result, 0)
            self.assertEqual((work/'ran').read_text(), 'OK')
            self.assertTrue(json.loads((root/'receipt.json').read_text())['probe_passed'])


if __name__ == '__main__':
    unittest.main()
