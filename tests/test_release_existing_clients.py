"""Browser mechanism controls, not a model evaluation."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReleaseClientTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not shutil.which('node'):
            raise unittest.SkipTest('Node unavailable')
        probe = subprocess.run(
            ['node', '-e',
             "const fs=require('node:fs');const {chromium}=require('playwright');"
             "process.exit(fs.existsSync(process.env.EVAL_BROWSER_EXECUTABLE||chromium.executablePath())?0:1)"],
            capture_output=True, timeout=10)
        if probe.returncode:
            raise unittest.SkipTest('Playwright/browser unavailable')

    def test_missing_assets_fail_and_retained_assets_preserve_open_clients(self):
        with tempfile.TemporaryDirectory() as d:
            candidate = Path(d) / 'candidate'
            shutil.copytree(ROOT / 'evals/fixtures/release-existing-clients', candidate)
            env = dict(os.environ, EVAL_PYTHON=str(Path(sys.executable).resolve()))
            for retained, passed in (([], False), (['v1'], True)):
                with self.subTest(retained=retained):
                    (candidate / 'deployment.json').write_text(
                        json.dumps({'active': 'v2', 'retained': retained}))
                    before = {
                        str(p.relative_to(candidate)): p.read_bytes()
                        for p in candidate.rglob('*') if p.is_file()
                    }
                    run = subprocess.run(
                        ['node', str(ROOT / 'evals/release_existing_clients_oracle.cjs'),
                         str(candidate)],
                        env=env, capture_output=True, text=True, timeout=40)
                    report = json.loads(run.stdout)
                    self.assertEqual(run.returncode, 0 if passed else 1, run.stdout + run.stderr)
                    self.assertEqual(
                        next(c['passed'] for c in report['checks']
                             if c['name'] == 'old-v1-continuity'), passed)
                    self.assertTrue(all(
                        c['passed'] for c in report['checks']
                        if c['name'] != 'old-v1-continuity'))
                    self.assertEqual(before, {
                        str(p.relative_to(candidate)): p.read_bytes()
                        for p in candidate.rglob('*') if p.is_file()
                    })

    def test_wrong_active_release_is_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            candidate = Path(d) / 'candidate'
            shutil.copytree(ROOT / 'evals/fixtures/release-existing-clients', candidate)
            (candidate / 'deployment.json').write_text(
                json.dumps({'active': 'v1', 'retained': ['v1']}))
            run = subprocess.run(
                ['node', str(ROOT / 'evals/release_existing_clients_oracle.cjs'), str(candidate)],
                capture_output=True, text=True, timeout=10)
            self.assertNotEqual(run.returncode, 0)
            self.assertIn('candidate must keep v2 active', run.stderr)


if __name__ == '__main__':
    unittest.main()
