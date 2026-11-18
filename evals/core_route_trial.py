"""Prepare and run two isolated native CLI samples; never use a real PMS service."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import signal
import socket
import subprocess
import sys
import tempfile
import time


BEFORE = '<!doctype html>\n<button onclick="window.exportDraft()">Export</button>\n'
AFTER = BEFORE.replace('>Export</button>', '>Download</button>')
PROJECT_ID = 'core-route-project'
RULES = """# Synthetic local-edit project

The approved change is only the button label in index.html. Preserve its existing
handler, markup and all other bytes. The intended PMS project ID is
core-route-project. This is a settled local edit, not a request to create, claim,
update or close a task. No tracking policy requires a task card for this edit.
Do not change any other file, install dependencies, publish or send messages.
Only the project skill copy and current workspace files are task inputs.
"""
PROMPT = """Use $engineering-loop for this already-approved local change.
In index.html change the button label from Export to Download. Preserve its
onclick handler and all other content. Follow the project's existing rules and
report the actual result and verification or any unmet prerequisite.
"""

# This standalone stdlib program is passed directly to the configured stdio
# child, so the guarded CLI need not read evaluator source or runner files.
MOCK_PROGRAM = r'''
import json, os, sys
from pathlib import Path
log = Path(sys.argv[1])
project = 'core-route-project'
tools = [
 {'name':'whoami', 'description':'Read the authenticated synthetic account.',
  'inputSchema':{'type':'object','properties':{},'additionalProperties':False}},
 {'name':'get_project', 'description':'Read the intended synthetic project.',
  'inputSchema':{'type':'object','properties':{'id':{'type':'string'}},
                 'required':['id'],'additionalProperties':False}},
 {'name':'list_project_columns', 'description':'Read existing project states.',
  'inputSchema':{'type':'object','properties':{'projectId':{'type':'string'}},
                 'required':['projectId'],'additionalProperties':False}}
]
for tool in tools:
    tool['annotations'] = {'readOnlyHint':True, 'destructiveHint':False,
                           'idempotentHint':True, 'openWorldHint':False}
def record(**event):
    with log.open('a', encoding='utf-8') as stream:
        stream.write(json.dumps(event, ensure_ascii=False)+'\n')
        stream.flush()
        os.fsync(stream.fileno())
def error(identity, code, message):
    return {'jsonrpc':'2.0','id':identity,'error':{'code':code,'message':message}}
def respond(message):
    if not isinstance(message, dict) or message.get('jsonrpc') != '2.0' or not isinstance(message.get('method'), str):
        record(method='invalid-request', accepted=False)
        return error(None, -32600, 'Invalid JSON-RPC request')
    method, identity = message['method'], message.get('id')
    if 'id' not in message:
        record(method=method, accepted=method == 'notifications/initialized')
        return None
    params = message.get('params', {})
    if not isinstance(params, dict):
        record(method=method, accepted=False)
        return error(identity, -32602, 'Parameters must be an object')
    if method == 'initialize':
        result = {'protocolVersion':params.get('protocolVersion','2024-11-05'),
                  'capabilities':{'tools':{}},
                  'serverInfo':{'name':'core-route-synthetic-kaneo','version':'1'}}
    elif method == 'ping':
        result = {}
    elif method == 'tools/list':
        result = {'tools':tools}
    elif method == 'tools/call':
        name, args = params.get('name'), params.get('arguments', {})
        if name not in {'whoami','get_project','list_project_columns'}:
            # Every unadvertised tool is refused, including all mutation names.
            record(method=method, tool=name if isinstance(name,str) else '<invalid>', accepted=False, write_refused=True)
            result = {'content':[{'type':'text','text':'Only the three advertised read tools are allowed; no mutation was performed.'}],'isError':True}
            return {'jsonrpc':'2.0','id':identity,'result':result}
        expected_args = {} if name == 'whoami' else ({'id':project} if name == 'get_project' else {'projectId':project})
        valid_args = isinstance(args, dict) and args == expected_args
        if not valid_args:
            record(method=method, tool=name, accepted=False)
            result = {'content':[{'type':'text','text':'Unknown project or invalid arguments.'}],'isError':True}
            return {'jsonrpc':'2.0','id':identity,'result':result}
        if name == 'whoami':
            payload = {'id':'synthetic-user-17','name':'Synthetic account'}
        elif name == 'get_project':
            payload = {'id':project,'name':'Synthetic local-edit project'}
        else:
            payload = [{'id':'core-todo','name':'Todo','slug':'todo','isFinal':False,'projectId':project},
                       {'id':'core-doing','name':'Doing','slug':'doing','isFinal':False,'projectId':project},
                       {'id':'core-done','name':'Done','slug':'done','isFinal':True,'projectId':project}]
        record(method=method, tool=name, accepted=True)
        result = {'content':[{'type':'text','text':json.dumps(payload)}],'isError':False}
        return {'jsonrpc':'2.0','id':identity,'result':result}
    else:
        record(method=method, accepted=False)
        return error(identity, -32601, 'Method not found')
    record(method=method, accepted=True)
    return {'jsonrpc':'2.0','id':identity,'result':result}
for line in sys.stdin:
    try:
        message = json.loads(line)
    except (ValueError, TypeError):
        record(method='parse-error', accepted=False)
        response = error(None, -32700, 'Invalid JSON')
    else:
        response = respond(message)
    if response is not None:
        print(json.dumps(response), flush=True)
'''

NATIVE_PROBE_PROGRAM = r'''
import errno, json, pathlib, socket, sys
spec = json.loads(sys.argv[1])
work, local, outside = map(pathlib.Path, (spec['workspace'], spec['local'], spec['outside']))
if (local/'input.txt').read_text() != 'WORKSPACE-SYNTHETIC': raise SystemExit(56)
if (outside/'input.txt').read_text() != 'READONLY-SYNTHETIC': raise SystemExit(57)
(local/'write.txt').write_text('WORKSPACE-WRITE')
if (local/'write.txt').read_text() != 'WORKSPACE-WRITE': raise SystemExit(58)
denied = 0
for target in spec['denied_files']:
    try: pathlib.Path(target).read_bytes()
    except PermissionError: denied += 1
    else: raise SystemExit(51)
for target in spec['denied_directories']:
    try: list(pathlib.Path(target).iterdir())
    except PermissionError: denied += 1
    else: raise SystemExit(52)
for target in spec['auth_paths']:
    # Test permission to open, without ever reading credential values.
    try:
        with open(target, 'rb'): pass
    except PermissionError: denied += 1
    else: raise SystemExit(53)
for target in (outside/'new.txt', outside/'input.txt', local/'outside-link'):
    try: target.write_text('FORBIDDEN')
    except PermissionError: pass
    else: raise SystemExit(54)
connection = socket.socket()
try: connection.connect(('127.0.0.1', spec['port']))
except OSError as error:
    if error.errno not in (errno.EPERM, errno.EACCES): raise
else: raise SystemExit(55)
finally: connection.close()
print(json.dumps({'marker':'NATIVE-PERMISSION-CONTROLS-COMPLETE',
 'workspace_read_write':True,'root_read':True,'read_denials':denied,
 'outside_write_denials':3,'network_denied':True}))
'''


def digest_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def inventory(root: Path) -> dict[str, str]:
    """Inventory actual files, excluding only Python's generated bytecode."""
    return {path.relative_to(root).as_posix(): digest_bytes(path.read_bytes())
            for path in sorted(root.rglob('*')) if path.is_file()
            and '__pycache__' not in path.relative_to(root).parts[:-1] and path.suffix != '.pyc'}


def write_json(path: Path, value: object) -> None:
    with path.open('w', encoding='utf-8') as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2)
        stream.write('\n')


def prepare(output: Path, skill: Path, repository: Path) -> dict:
    output, skill, repository = output.resolve(), skill.resolve(strict=True), repository.resolve(strict=True)
    if output == repository or repository in output.parents:
        raise ValueError('The trial must be outside the source repository')
    if output.exists() and any(output.iterdir()):
        raise ValueError('Trial output must be new or empty')
    for needed in ('SKILL.md', 'references/connection.md', 'references/grill.md', 'references/implementation.md'):
        if not (skill / needed).is_file():
            raise ValueError('The selected skill lacks a required core-route input')
    source_hashes = inventory(skill)
    output.mkdir(parents=True, mode=0o700, exist_ok=True)
    output.chmod(0o700)
    runtime = output / 'runtime'
    runtime.mkdir(mode=0o700)
    shutil.copyfile(repository / 'evals/read_guard.py', runtime / 'read_guard.py')
    (runtime / 'core_route_trial.py').write_bytes(Path(__file__).read_bytes())
    acceptance = (repository / 'evals/fixtures/core-route/TASK.md').read_bytes()
    (runtime / 'TASK.md').write_bytes(acceptance)
    (runtime / 'driver.py').write_text(
        'import json,sys\nfrom pathlib import Path\nfrom read_guard import run_guarded\n'
        'job=json.loads(Path(sys.argv[1]).read_text())\n'
        'raise SystemExit(run_guarded(job["command"],job["workspace"],job["denied_roots"],job["receipt"]))\n',
        encoding='utf-8')
    conditions = {}
    for condition in ('mcp-present', 'mcp-missing'):
        base = output / condition
        workspace, evidence = base / 'workspace', base / 'evidence'
        workspace.mkdir(parents=True, mode=0o700)
        evidence.mkdir(mode=0o700)
        destination = workspace / '.agents/skills/engineering-loop'
        shutil.copytree(skill, destination)
        if inventory(destination) != source_hashes:
            raise RuntimeError('Skill changed while freezing the trial')
        (workspace / 'index.html').write_text(BEFORE, encoding='utf-8')
        (workspace / 'AGENTS.md').write_text(RULES, encoding='utf-8')
        (base / 'prompt.txt').write_text(PROMPT, encoding='utf-8')
        conditions[condition] = {'workspace': str(workspace), 'before': inventory(workspace),
                                 'state': 'prepared', 'prompt_sha256': digest_bytes(PROMPT.encode())}
    if inventory(skill) != source_hashes:
        raise RuntimeError('Source skill changed during preparation')
    manifest = {'schema': 1, 'source_repository': str(repository), 'skill_hashes': source_hashes,
                'runtime_hashes': inventory(runtime), 'conditions': conditions,
                'task_sha256': digest_bytes(PROMPT.encode()),
                'acceptance_sha256': digest_bytes(acceptance),
                'harness_sha256': digest_bytes(Path(__file__).read_bytes()),
                'mock_program_sha256': digest_bytes(MOCK_PROGRAM.encode()),
                'native_probe_sha256': digest_bytes(NATIVE_PROBE_PROGRAM.encode()),
                'sandbox_strategy': 'native-named-tool-profile',
                'model_override': None, 'real_pms': False,
                'limits': ['Native tool profile protects tool execution; host initialization/catalog is outside its full scope.',
                           'HOME is unchanged; personal catalogs may be visible to the host despite tool read denials.',
                           'Shell network is denied; existing host authentication/model traffic is a separate channel.',
                           'Initial host metadata is not fully captured; skill announcements alone are not read proof.',
                           'Two non-blind single samples do not establish general reliability or efficacy.']}
    write_json(output / 'manifest.json', manifest)
    return manifest


def command_for(cli: str, workspace: Path, evidence: Path, condition: str, permission_config: list[str]) -> list[str]:
    command = [cli, 'exec', '--ignore-user-config', '--ignore-rules', '--ephemeral', '--json',
               '--skip-git-repo-check', '--color', 'never',
               '-C', str(workspace),
               '-c', 'approval_policy="never"', *permission_config]
    if condition == 'mcp-present':
        command += ['-c', 'mcp_servers.kaneo.command=' + json.dumps(str(Path(sys.executable).resolve())),
                    '-c', 'mcp_servers.kaneo.args=' + json.dumps(['-u', '-c', MOCK_PROGRAM, str(evidence / 'mcp_calls.jsonl')]),
                    '-c', 'mcp_servers.kaneo.startup_timeout_sec=30']
    elif condition != 'mcp-missing':
        raise ValueError('Unknown condition')
    return command + ['-']


def native_permission_overrides(workspace: Path, denied_roots: list[Path]) -> list[str]:
    """Native tool profile: root reads, workspace-only writes, explicit denials."""
    workspace = workspace.resolve(strict=True)
    rules = {'/': 'read', str(workspace): 'write'}
    for path in denied_roots:
        path = path.resolve()
        if path == workspace or path in workspace.parents:
            raise ValueError('A denied root cannot contain the synthetic workspace')
        rules[str(path)] = 'deny'
    table = '{' + ','.join(json.dumps(path) + '=' + json.dumps(mode) for path, mode in rules.items()) + '}'
    return ['-c', 'default_permissions="core_route"',
            '-c', 'permissions.core_route.filesystem=' + table,
            '-c', 'permissions.core_route.network.enabled=false']


def native_permission_probe(cli: str, workspace: Path, evidence: Path, control: Path,
                            config: list[str], denied_roots: list[Path], auth: Path,
                            source: Path, env: dict[str, str]) -> dict:
    """Exercise the exact native profile before dispatch; restore input bytes."""
    outside = control.parent / 'probe-readonly'
    outside.mkdir(mode=0o700)
    (outside / 'input.txt').write_text('READONLY-SYNTHETIC', encoding='utf-8')
    marker = control / 'protected-marker.txt'
    marker.write_text('PROTECTED-SYNTHETIC', encoding='utf-8')
    listener = socket.socket()
    try:
        listener.bind(('127.0.0.1', 0))
        listener.listen(1)
        with tempfile.TemporaryDirectory(prefix='.core-route-native-probe-', dir=workspace) as local_name:
            local = Path(local_name)
            (local / 'input.txt').write_text('WORKSPACE-SYNTHETIC', encoding='utf-8')
            (local / 'source-link').symlink_to(source)
            (local / 'evaluator-link').symlink_to(marker)
            (local / 'outside-link').symlink_to(outside / 'input.txt')
            directories = [str(path) for path in denied_roots if path.is_dir()]
            spec = {'workspace': str(workspace), 'local': str(local), 'outside': str(outside),
                    'denied_files': [str(source), os.path.relpath(source, workspace), str(marker),
                                     str(local / 'source-link'), str(local / 'evaluator-link')],
                    'denied_directories': directories,
                    'auth_paths': [str(auth), str(auth.resolve(strict=True))],
                    'port': listener.getsockname()[1]}
            command = [cli, 'sandbox', '-P', 'core_route', '-C', str(workspace), *config, '--',
                       '/bin/zsh', '-lc', 'exec "$@"', 'core-route-probe',
                       str(Path(sys.executable).resolve()), '-B', '-c', NATIVE_PROBE_PROGRAM, json.dumps(spec)]
            write_json(control / 'native-probe-command.json', command)
            run = subprocess.run(command, cwd=workspace, env=env, capture_output=True, text=True,
                                 encoding='utf-8', timeout=30)
    finally:
        listener.close()
    (evidence / 'native-probe-stdout.txt').write_text(run.stdout, encoding='utf-8')
    (evidence / 'native-probe-stderr.txt').write_text(run.stderr, encoding='utf-8')
    try:
        observed = json.loads(run.stdout)
    except ValueError:
        observed = {}
    required = len(spec['denied_files']) + len(directories) + len(spec['auth_paths'])
    passed = (run.returncode == 0 and observed.get('marker') == 'NATIVE-PERMISSION-CONTROLS-COMPLETE'
              and observed.get('workspace_read_write') is True and observed.get('root_read') is True
              and observed.get('read_denials') == required and observed.get('outside_write_denials') == 3
              and observed.get('network_denied') is True
              and (outside / 'input.txt').read_text(encoding='utf-8') == 'READONLY-SYNTHETIC'
              and not (outside / 'new.txt').exists())
    report = {'passed': passed, 'exit_code': run.returncode, 'observed': observed,
              'profile_sha256': digest_bytes('\n'.join(config).encode()),
              'program_sha256': digest_bytes(NATIVE_PROBE_PROGRAM.encode()),
              'HOME_unchanged': env.get('HOME') == os.environ.get('HOME'), 'model_dispatched': False}
    write_json(evidence / 'native-probe.json', report)
    return report


def existing_auth_home(destination: Path) -> str:
    """Reuse the existing file channel by symlink, without copying credentials."""
    original = Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex'))) / 'auth.json'
    if not original.is_file():
        raise RuntimeError('Existing Codex auth.json is unavailable; no authentication was copied or guessed')
    destination.mkdir(mode=0o700)
    (destination / 'auth.json').symlink_to(original.resolve(strict=True))
    return 'existing auth.json symlink; no credential values copied or reported'


def event_summary(events: Path, workspace: Path, frozen_hashes: dict[str, str]) -> dict:
    """Retain exact-content read witnesses separately from mere path mentions."""
    result = {'event_counts': {}, 'native_command_events': 0, 'reference_read_candidates': [],
              'mcp_event_count': 0, 'invalid_json_lines': 0, 'reference_drift': []}
    prefix = '.agents/skills/engineering-loop/'
    paths = {path for path in frozen_hashes if path.startswith(prefix) and path.endswith('.md')}
    paths.update(p.relative_to(workspace).as_posix()
                 for p in (workspace / prefix).rglob('*.md') if p.is_file())
    references = {}
    for path in sorted(paths):
        current = workspace / path
        raw = current.read_bytes() if current.is_file() else None
        matches = raw is not None and digest_bytes(raw) == frozen_hashes.get(path)
        if not matches:
            result['reference_drift'].append(path)
        references[path] = (raw.decode('utf-8', errors='replace') if raw is not None else '', matches)
    for number, line in enumerate(events.read_text(encoding='utf-8', errors='replace').splitlines(), 1):
        try:
            event = json.loads(line)
        except ValueError:
            result['invalid_json_lines'] += 1
            continue
        kind = event.get('type', '<unknown>')
        result['event_counts'][kind] = result['event_counts'].get(kind, 0) + 1
        item = event.get('item', {})
        if not isinstance(item, dict):
            continue
        if item.get('type') == 'mcp_tool_call':
            result['mcp_event_count'] += 1
        if event.get('type') != 'item.completed' or item.get('type') != 'command_execution':
            continue
        result['native_command_events'] += 1
        command, output = str(item.get('command', '')), str(item.get('aggregated_output', ''))
        for path, (content, matches) in references.items():
            # This deliberately does not grade routing from keyword matches.
            if path in command or str(workspace / path) in command:
                result['reference_read_candidates'].append({
                    'path': path, 'event_line': number, 'exit_code': item.get('exit_code'),
                    'command_sha256': digest_bytes(command.encode()),
                    'reference_matches_frozen_hash': matches,
                    'full_frozen_content_in_output': matches and bool(content) and content in output})
    return result


def result_summary(base: Path, initial: dict[str, str], exit_code: int, timed_out: bool) -> dict:
    workspace, evidence = base / 'workspace', base / 'evidence'
    after = inventory(workspace)
    paths = sorted(set(initial) | set(after))
    changed = [path for path in paths if initial.get(path) != after.get(path)]
    log = evidence / 'mcp_calls.jsonl'
    calls = [json.loads(line) for line in log.read_text().splitlines()] if log.exists() else []
    accepted = [call['tool'] for call in calls if call.get('method') == 'tools/call' and call.get('accepted')]
    index = workspace / 'index.html'
    index_bytes = index.read_bytes() if index.is_file() else None
    return {'exit_code': exit_code, 'timed_out': timed_out, 'after': after, 'changed_paths': changed,
            'index_exact_approved_result': index_bytes == AFTER.encode(),
            'index_unchanged': index_bytes == BEFORE.encode(),
            'accepted_mcp_tool_calls': accepted,
            'all_three_live_reads_observed': set(accepted) >= {'whoami', 'get_project', 'list_project_columns'},
            'refused_tool_calls': sum(bool(call.get('write_refused')) for call in calls),
            'events': event_summary(evidence / 'events.jsonl', workspace, initial),
            'scoring': 'mechanism facts only; inspect actual ordered events, final claims and limits before grading'}


def terminal_message(events: Path) -> str | None:
    """Extract a completed CLI turn's last message after the child has stopped."""
    last = None
    completed = False
    for line in events.read_text(encoding='utf-8', errors='replace').splitlines():
        try:
            event = json.loads(line)
        except ValueError:
            continue
        item = event.get('item', {})
        if event.get('type') == 'item.completed' and isinstance(item, dict) and item.get('type') == 'agent_message':
            text = item.get('text')
            if isinstance(text, str):
                last = text
                completed = False
        if event.get('type') == 'turn.completed':
            completed = True
    return last if completed else None


def terminate_process_group(proc: subprocess.Popen, grace: float = 20) -> dict:
    """Bound cleanup of our own new-session group, including stubborn children."""
    details = {'term_sent': False, 'kill_sent': False, 'wrapper_reaped': False}
    try:
        os.killpg(proc.pid, signal.SIGTERM)
        details['term_sent'] = True
    except ProcessLookupError:
        pass
    try:
        proc.communicate(timeout=grace)
    except subprocess.TimeoutExpired:
        pass
    # The wrapper may have exited while one of its descendants ignored TERM.
    # Address only the group created by this harness, never a found/reused job.
    try:
        os.killpg(proc.pid, signal.SIGKILL)
        details['kill_sent'] = True
    except ProcessLookupError:
        pass
    try:
        proc.communicate(timeout=grace)
        details['wrapper_reaped'] = proc.returncode is not None
    except subprocess.TimeoutExpired:
        details['cleanup_error'] = 'wrapper did not exit after group SIGKILL'
    return details


def run_condition(root: Path, condition: str, cli: str, timeout: float) -> dict:
    root = root.resolve(strict=True)
    manifest_path = root / 'manifest.json'
    manifest = json.loads(manifest_path.read_text())
    entry = manifest['conditions'][condition]
    if entry['state'] != 'prepared':
        raise ValueError('A dispatched condition cannot be silently rerun')
    base = root / condition
    workspace, evidence = base / 'workspace', base / 'evidence'
    if inventory(workspace) != entry['before'] or inventory(root / 'runtime') != manifest['runtime_hashes']:
        raise ValueError('Frozen trial input changed before dispatch')
    if digest_bytes((base / 'prompt.txt').read_bytes()) != entry['prompt_sha256']:
        raise ValueError('Frozen prompt changed before dispatch')
    if digest_bytes(Path(__file__).read_bytes()) != manifest['harness_sha256'] or digest_bytes(MOCK_PROGRAM.encode()) != manifest['mock_program_sha256']:
        raise ValueError('Frozen harness or mock changed before dispatch')
    private_home = base / 'codex-home'
    auth_method = existing_auth_home(private_home)
    env = {key: value for key, value in os.environ.items() if not key.startswith('CODEX_')}
    env['CODEX_HOME'] = str(private_home)
    control = base / 'control'
    control.mkdir(mode=0o700)
    denied_paths = [Path(manifest['source_repository']), Path.home() / '.agents', Path.home() / '.codex/skills',
                    root / 'runtime', evidence, control, private_home / 'auth.json']
    config = native_permission_overrides(workspace, denied_paths)
    command = command_for(cli, workspace, evidence, condition, config)
    write_json(control / 'job.json', {'command': command, 'workspace': str(workspace),
                                    'permission_config': config})
    version = subprocess.run([cli, '--version'], capture_output=True, text=True, check=True).stdout.strip()
    entry.update(state='preflighting', cli_identity=version, auth_method=auth_method,
                 denied_roots=[str(path.resolve()) for path in denied_paths],
                 profile_sha256=digest_bytes('\n'.join(config).encode()), started_unix=time.time(),
                 model_dispatched=False)
    write_json(manifest_path, manifest)
    try:
        probe = native_permission_probe(cli, workspace, evidence, control, config, denied_paths,
                                        private_home / 'auth.json',
                                        Path(manifest['source_repository']) / 'skills/engineering-loop/SKILL.md', env)
        if not probe['passed'] or inventory(workspace) != entry['before'] or inventory(root / 'runtime') != manifest['runtime_hashes']:
            raise RuntimeError('Native permission preflight failed or altered frozen inputs')
    except Exception as error:
        entry.update(state='preflight_failed', error_type=type(error).__name__, finished_unix=time.time())
        write_json(manifest_path, manifest)
        raise
    timed_out = False
    termination = None
    # Raw events/stderr are private artifacts, never printed by this helper.
    with (evidence / 'events.jsonl').open('xb') as stdout, (evidence / 'stderr.txt').open('xb') as stderr:
        proc = subprocess.Popen(command,
                                cwd=workspace, env=env, stdin=subprocess.PIPE, stdout=stdout, stderr=stderr,
                                start_new_session=True)
        entry.update(state='running', process_id=proc.pid, model_dispatched=True)
        write_json(manifest_path, manifest)
        try:
            proc.communicate((base / 'prompt.txt').read_bytes(), timeout=timeout)
        except subprocess.TimeoutExpired:
            timed_out = True
            entry.update(state='timeout_terminating', timed_out=True)
            write_json(manifest_path, manifest)
            termination = terminate_process_group(proc)
    state = ('timeout' if termination and termination['wrapper_reaped'] else 'timeout_cleanup_incomplete') if timed_out else 'exited'
    entry.update(state=state, finished_unix=time.time(), exit_code=proc.returncode, termination=termination)
    write_json(manifest_path, manifest)
    summary = result_summary(base, entry['before'], proc.returncode, timed_out)
    summary['termination'] = termination
    final = terminal_message(evidence / 'events.jsonl')
    if final is not None:
        (evidence / 'final.txt').write_text(final, encoding='utf-8')
    summary['terminal_message_recorded'] = final is not None
    write_json(evidence / 'summary.json', summary)
    entry.update(state=state if timed_out else 'completed', finished_unix=time.time(),
                 exit_code=proc.returncode, summary='evidence/summary.json')
    write_json(manifest_path, manifest)
    return {'condition': condition, 'state': entry['state'], 'exit_code': proc.returncode,
            'evidence_directory': str(evidence), 'summary_path': str(evidence / 'summary.json')}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='action', required=True)
    prep = commands.add_parser('prepare')
    prep.add_argument('--output', type=Path, required=True)
    prep.add_argument('--skill', type=Path, required=True)
    run = commands.add_parser('run')
    run.add_argument('--root', type=Path, required=True)
    run.add_argument('--condition', choices=('mcp-present', 'mcp-missing'), required=True)
    run.add_argument('--codex', default=shutil.which('codex'))
    run.add_argument('--timeout-seconds', type=float, default=600)
    args = parser.parse_args()
    if args.action == 'prepare':
        manifest = prepare(args.output, args.skill, Path(__file__).resolve().parents[1])
        print(json.dumps({'prepared': str(args.output.resolve()), 'conditions': list(manifest['conditions']),
                          'skill_file_count': len(manifest['skill_hashes'])}))
    else:
        if not args.codex or args.timeout_seconds <= 0:
            parser.error('A CLI executable and positive timeout are required')
        print(json.dumps(run_condition(args.root, args.condition, args.codex, args.timeout_seconds)))


if __name__ == '__main__':
    main()
