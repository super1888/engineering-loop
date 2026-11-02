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
            report = json.loads((root/'receipt').read_text(encoding='utf-8'))
            self.assertEqual(report['state'], 'failed')
            self.assertFalse(report['probe_passed'])
            self.assertFalse(report['command_dispatch_attempted'])
            self.assertIsNone(report['command_exit_code'])

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

    @unittest.skipUnless(platform.system() == 'Darwin', 'macOS seatbelt control')
    def test_invalid_receipt_parent_stops_before_target_side_effects(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); work = root/'work'; work.mkdir()
            denied = root/'denied'; denied.mkdir()
            blocked = root/'not-a-directory'; blocked.write_text('KEEP', encoding='utf-8')
            with self.assertRaises(OSError):
                run_guarded([str(Path(sys.executable).resolve()), '-c',
                             "from pathlib import Path; Path('ran').write_text('RAN')"],
                            work, [denied], blocked/'receipt.json')
            self.assertFalse((work/'ran').exists())
            self.assertEqual(blocked.read_text(encoding='utf-8'), 'KEEP')
            self.assertEqual(list(denied.iterdir()), [])

    @unittest.skipUnless(platform.system() == 'Darwin', 'macOS symlink control')
    def test_existing_dangling_receipt_symlink_is_not_followed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); work = root/'work'; work.mkdir()
            denied = root/'denied'; denied.mkdir()
            destination = root/'unrelated-new.json'
            receipt = root/'receipt.json'; receipt.symlink_to(destination)
            with patch('read_guard.subprocess.run') as run:
                with self.assertRaises(ValueError):
                    run_guarded(['must-not-run'], work, [denied], receipt)
                run.assert_not_called()
            self.assertTrue(receipt.is_symlink())
            self.assertFalse(destination.exists())

    @unittest.skipUnless(platform.system() == 'Darwin', 'macOS receipt control')
    def test_receipt_open_failure_prevents_all_subprocess_dispatch(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); work = root/'work'; work.mkdir()
            denied = root/'denied'; denied.mkdir()
            receipt = (root/'receipt.json').resolve()
            original_open = Path.open
            def refuse_receipt(path, *args, **kwargs):
                if path == receipt:
                    raise PermissionError('Synthetic unwritable receipt')
                return original_open(path, *args, **kwargs)
            with patch.object(Path, 'open', refuse_receipt), patch('read_guard.subprocess.run') as run:
                with self.assertRaises(PermissionError):
                    run_guarded(['must-not-run'], work, [denied], receipt)
                run.assert_not_called()
            self.assertFalse(receipt.exists())

    @unittest.skipUnless(platform.system() == 'Darwin', 'macOS parent symlink control')
    def test_new_receipt_through_parent_symlink_is_reserved_before_target(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); work = root/'work'; work.mkdir()
            denied = root/'denied'; denied.mkdir()
            actual = root/'receipts'; actual.mkdir()
            alias = root/'receipt-directory'; alias.symlink_to(actual, target_is_directory=True)
            receipt = alias/'new.json'
            code = ("import json,pathlib,sys\n"
                    "report=json.loads(pathlib.Path(sys.argv[1]).read_text())\n"
                    "if report['state']!='running' or not report['probe_passed']: raise SystemExit(31)\n"
                    "pathlib.Path('ran').write_text('RAN')\nraise SystemExit(3)")
            result = run_guarded([str(Path(sys.executable).resolve()), '-c', code, str(receipt)],
                                 work, [denied], receipt)
            self.assertEqual(result, 3)
            report = json.loads(receipt.read_text(encoding='utf-8'))
            self.assertEqual(report['state'], 'completed')
            self.assertEqual(report['command_exit_code'], 3)
            self.assertTrue(report['command_dispatch_attempted'])
            self.assertTrue((work/'ran').exists())
            self.assertTrue(alias.is_symlink())


if __name__ == '__main__':
    unittest.main()
