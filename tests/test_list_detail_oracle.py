import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ListDetailOracleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not shutil.which("node"):
            raise unittest.SkipTest("Node is unavailable")
        probe = subprocess.run(["node", "-e",
            "const fs = require('node:fs'); const {chromium} = require('playwright'); "
            "process.exit(fs.existsSync(process.env.EVAL_BROWSER_EXECUTABLE || chromium.executablePath()) ? 0 : 1);"],
            capture_output=True, timeout=10)
        if probe.returncode:
            raise unittest.SkipTest("Playwright and a local Chromium browser must be configured")

    def test_browser_oracle_rejects_saving_unrelated_records(self):
        fixture = ROOT / "evals/fixtures/list-detail"
        original = (fixture / "app.js").read_text(encoding="utf-8")
        save = "  RecordState.rename(state, activeId, nameInput.value);"
        self.assertEqual(original.count(save), 1)
        names = {f"{entry}-{action}" for entry in ("list", "direct")
                 for action in ("save", "cancel", "close", "escape", "backdrop")}
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory) / "workspace"
            shutil.copytree(fixture, workspace)
            for mode in ("behavior", "copy"):
                app = original.replace("leaveDetail(false)", "leaveDetail(true)") if mode == "behavior" else original
                html = (fixture / "index.html").read_text(encoding="utf-8")
                if mode == "copy":
                    html = html.replace('id="save">Save<', 'id="save">Save draft<')
                (workspace / "index.html").write_text(html, encoding="utf-8")
                for broken in (False, True):
                    with self.subTest(mode=mode, saves_all_records=broken):
                        source = app.replace(save,
                            "  for (const record of state.records) RecordState.rename(state, record.id, nameInput.value);") if broken else app
                        (workspace / "app.js").write_text(source, encoding="utf-8")
                        before = {p.name: p.read_bytes() for p in workspace.iterdir() if p.is_file()}
                        result = subprocess.run(["node", str(ROOT / "evals/list_detail_oracle.cjs"), str(workspace), mode],
                            capture_output=True, text=True, timeout=60)
                        report = json.loads(result.stdout)
                        self.assertEqual({row["name"] for row in report["results"]}, names)
                        self.assertEqual(result.returncode, int(broken), result.stdout + result.stderr)
                        failed = {row["name"] for row in report["results"] if not row["passed"]}
                        self.assertEqual(failed, {"list-save", "direct-save"} if broken else set())
                        if broken:
                            self.assertTrue(all("unrelated record name" in row["error"]
                                for row in report["results"] if not row["passed"]))
                        self.assertEqual({p.name: p.read_bytes() for p in workspace.iterdir() if p.is_file()}, before)

    def test_browser_oracle_preserves_close_accessible_name(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory) / "workspace"
            shutil.copytree(ROOT / "evals/fixtures/list-detail", workspace)
            app = workspace / "app.js"
            app.write_text(app.read_text(encoding="utf-8").replace(
                "leaveDetail(false)", "leaveDetail(true)"), encoding="utf-8")
            html = workspace / "index.html"
            source = html.read_text(encoding="utf-8")
            self.assertEqual(source.count(' aria-label="Close detail"'), 1)
            for misplaced in (False, True):
                with self.subTest(name_on_cancel=misplaced):
                    candidate = source.replace(' aria-label="Close detail"', '')
                    if misplaced:
                        candidate = candidate.replace('id="cancel"', 'id="cancel" aria-label="Close detail"')
                    html.write_text(candidate, encoding="utf-8")
                    before = {p.name: p.read_bytes() for p in workspace.iterdir() if p.is_file()}
                    result = subprocess.run(["node", str(ROOT / "evals/list_detail_oracle.cjs"), str(workspace), "behavior"],
                        capture_output=True, text=True, timeout=60)
                    report = json.loads(result.stdout)
                    self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                    self.assertEqual(len(report["results"]), 10)
                    self.assertTrue(all(not row["passed"] and "close accessible name" in row["error"]
                        for row in report["results"]))
                    self.assertEqual({p.name: p.read_bytes() for p in workspace.iterdir() if p.is_file()}, before)


if __name__ == "__main__":
    unittest.main()
