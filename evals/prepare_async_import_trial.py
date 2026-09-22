"""Freeze an owner-change A/B experiment; actual contributors run separately."""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

from prepare_list_detail_trial import CANDIDATE, OVERLAY, hashes

ROOT = Path(__file__).resolve().parents[1]
PROMPT = """Implement the asynchronous batch-import feature in {workspace}, coordinating separate backend and frontend contributors. You own shared contract decisions and integrated verification. Use at most two child agents concurrently; those contributors must not delegate further. All agents inherit the available model configuration without overrides. Keep backend and UI writes disjoint and explicitly own shared files.

Use Engineering Loop at {skill}/SKILL.md and the additional guidance at {guidance}. Read the workspace's AGENTS.md, PRODUCT.md, API.md, DECISIONS.md and SERVICE.md. Work only in the supplied workspace, read-only skill/guidance and evidence directory {evidence}; do not inspect sibling trials, source-repository/evaluator files or previous conversations. Your shell may initially point elsewhere; always supply the intended working directory. Do not install dependencies, commit, publish or use real services.

A scheduled owner review is part of this task. After both contributors have inspected their assigned areas and begun an independent bounded step, send CHECKPOINT_READY to the parent with contributor identities, current contract interpretation and unresolved product questions. Await the owner's response before dependent implementation; independent work can continue. Address consequential questions to the parent acting as the synthetic owner, not the real user. Do not infer an unresolved business policy from the stub.

After the owner response, finish the authorized feature and relevant verification. Record concise task/ownership decisions, contributor instructions and important updates in {evidence}/coordination.md. Preserve commands/results in {evidence}/commands.txt (contributors may keep separate evidence files). Finish with {evidence}/agent-report.md: actual outcomes, unresolved failures, questions/owner decisions, delegated roles and verification limits. Report actual evidence, not hidden tests or unavailable telemetry.

Available tools: Python and Node on PATH. Playwright is resolvable with NODE_PATH={node_modules}; a local Chromium executable is {browser}. The fixture documents its public tests and real local-server controls. Use disposable local databases and stop owned processes.
"""
CHANGE_MESSAGE = """Owner review complete. Read OWNER_CHANGE.md in your workspace: revision 2 is accepted and supersedes the conflicting revision-1 processing policy and aggregate-only response. The 100-row limit remains settled. Apply the change to affected active contributions, effective documents and verification; no further approval is needed for this scope. Continue to completion and report integrated evidence and remaining limits."""
EARLY_REPLY = """The owner decision is scheduled at the agreed checkpoint. Continue independent bounded work and send CHECKPOINT_READY once both contributors have inspected their areas and begun an independent step; do not choose an unresolved business policy in the meantime."""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--node-modules', required=True)
    parser.add_argument('--browser', required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    if (output / 'inputs.json').exists():
        parser.error('Frozen input manifest already exists; choose a new result directory.')
    evaluators = ['async_import_oracle.py', 'async_import_browser_oracle.cjs', 'async_import_change.md']
    evaluator_hashes = {name: hashlib.sha256((ROOT / 'evals' / name).read_bytes()).hexdigest()
                        for name in evaluators}
    scratch = Path(tempfile.mkdtemp(prefix='engineering-loop-import-ab-'))
    trials = {}
    for variant in ('A', 'B'):
        directory = scratch / variant
        workspace, skill, evidence = (directory / name for name in ('workspace', 'skill', 'evidence'))
        shutil.copytree(ROOT / 'evals/fixtures/async-import', workspace,
                        ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        shutil.copytree(ROOT / 'skills/engineering-loop', skill)
        evidence.mkdir()
        guidance = directory / 'trial-guidance.md'
        guidance.write_text(OVERLAY + (CANDIDATE if variant == 'B' else ''), encoding='utf-8')
        (directory / 'prompt.txt').write_text(PROMPT.format(workspace=workspace, skill=skill,
            guidance=guidance, evidence=evidence, node_modules=args.node_modules, browser=args.browser), encoding='utf-8')
        trials[variant] = str(directory)
    manifest = {'source_revision': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
        'fixture_hashes': {name: digest for name, digest in hashes(ROOT / 'evals/fixtures/async-import').items()
                           if '__pycache__' not in Path(name).parts and not name.endswith('.pyc')},
        'skill_hashes': hashes(ROOT / 'skills/engineering-loop'), 'evaluator_hashes': evaluator_hashes,
        'guidance_A': OVERLAY, 'guidance_B': OVERLAY + CANDIDATE, 'prompt_template': PROMPT,
        'owner_reply': CHANGE_MESSAGE, 'early_reply': EARLY_REPLY, 'order': ['A', 'B'],
        'checkpoint': 'Both backend and frontend contributors inspected their inputs and began an independent bounded step.',
        'limits': 'Procedural file isolation; one matched run per condition; role count and checkpoint are controlled by the experiment.'}
    (output / 'inputs.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    (scratch / 'trials.json').write_text(json.dumps(trials, indent=2), encoding='utf-8')
    print(json.dumps({'scratch': str(scratch), 'trials': trials}, indent=2))


if __name__ == '__main__':
    main()
