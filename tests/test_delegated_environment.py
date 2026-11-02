"""Contributor-environment controls; these tests do not evaluate a model."""
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'evals'))
from read_guard import run_guarded


class DelegatedEnvironmentTests(unittest.TestCase):
    @unittest.skipUnless(platform.system() == 'Darwin', 'macOS read-guard control')
    def test_parent_runtime_success_does_not_establish_guarded_child_readiness(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            work, denied = root / 'work', root / 'denied'
            work.mkdir()
            denied.mkdir()
            interpreter = str(Path(sys.executable).resolve())
            source = "print('RUNTIME-READY')\n"
            unavailable = denied / 'runtime_check.py'
            unavailable.write_text(source, encoding='utf-8')
            self.assertEqual(unavailable.read_text(encoding='utf-8'), source)
            parent = subprocess.run([interpreter, str(unavailable)], capture_output=True, text=True, check=True)
            self.assertEqual(parent.stdout.strip(), 'RUNTIME-READY')
            available = work / 'runtime_check.py'
            available.write_text(source, encoding='utf-8')
            broken = work / 'broken.py'
            broken.write_text("print('CODE-STARTED', flush=True)\nraise RuntimeError('BUSINESS-CODE-FAILURE')\n", encoding='utf-8')
            report = work / 'child.json'
            child = '''import json,pathlib,subprocess,sys
unavailable,available,broken,report = map(pathlib.Path,sys.argv[1:])
def denied_read():
 try: unavailable.read_bytes()
 except PermissionError: return True
 raise SystemExit('Expected an actual permission denial')
before=denied_read()
blocked=subprocess.run([sys.executable,str(unavailable)],capture_output=True,text=True)
ready=subprocess.run([sys.executable,str(available)],capture_output=True,text=True)
code_error=subprocess.run([sys.executable,str(broken)],capture_output=True,text=True)
report.write_text(json.dumps({'denied_before':before,'denied_after':denied_read(),
 'blocked_exit':blocked.returncode,'blocked_error':blocked.stderr,
 'ready_exit':ready.returncode,'ready_output':ready.stdout,
 'code_exit':code_error.returncode,'code_output':code_error.stdout,'code_error':code_error.stderr}))
'''
            result = run_guarded([interpreter, '-c', child, str(unavailable), str(available),
                                  str(broken), str(report)], work, [denied], root / 'receipt.json')
            self.assertEqual(result, 0)
            observed = json.loads(report.read_text(encoding='utf-8'))
            self.assertTrue(observed['denied_before'])
            self.assertTrue(observed['denied_after'])
            self.assertNotEqual(observed['blocked_exit'], 0)
            self.assertRegex(observed['blocked_error'].lower(), r'permission denied|operation not permitted')
            self.assertEqual((observed['ready_exit'], observed['ready_output'].strip()), (0, 'RUNTIME-READY'))
            self.assertNotEqual(observed['code_exit'], 0)
            self.assertEqual(observed['code_output'].strip(), 'CODE-STARTED')
            self.assertIn('BUSINESS-CODE-FAILURE', observed['code_error'])
            self.assertEqual(unavailable.read_text(encoding='utf-8'), source)

    def test_node_dependency_must_be_available_in_the_actual_child_environment(self):
        node = shutil.which('node')
        if node is None:
            self.skipTest('Node is unavailable')
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            work, modules = root / 'work', root / 'modules'
            work.mkdir()
            package = modules / 'delegated-environment-fixture'
            package.mkdir(parents=True)
            (package / 'index.js').write_text("module.exports = 'MODULE-READY';\n", encoding='utf-8')
            code = "process.stdout.write(require('delegated-environment-fixture'))"
            missing_env = os.environ.copy()
            missing_env.pop('NODE_PATH', None)
            missing_env.pop('NODE_OPTIONS', None)
            ready_env = dict(missing_env, NODE_PATH=str(modules))
            parent = subprocess.run([node, '-e', code], cwd=work, env=ready_env,
                                    capture_output=True, text=True)
            self.assertEqual((parent.returncode, parent.stdout), (0, 'MODULE-READY'))
            child_missing = subprocess.run([node, '-e', code], cwd=work, env=missing_env,
                                           capture_output=True, text=True)
            self.assertNotEqual(child_missing.returncode, 0)
            self.assertIn('MODULE_NOT_FOUND', child_missing.stderr)
            child_ready = subprocess.run([node, '-e', code], cwd=work, env=ready_env,
                                         capture_output=True, text=True)
            self.assertEqual((child_ready.returncode, child_ready.stdout), (0, 'MODULE-READY'))


if __name__ == '__main__':
    unittest.main()
