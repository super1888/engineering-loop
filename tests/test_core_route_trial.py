"""Native mock-protocol and input/evidence controls, not model-efficacy tests."""
from pathlib import Path
import json
import os
import platform
import signal
import subprocess
import sys
import tempfile
import tomllib
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'evals'))
import core_route_trial as trial


REPOSITORY = Path(__file__).resolve().parents[1]


class CoreRouteTrialTests(unittest.TestCase):
    def request(self, identity, method, params=None):
        item = {'jsonrpc': '2.0', 'id': identity, 'method': method}
        if params is not None:
            item['params'] = params
        return item

    def server(self, log, requests, prefix=None):
        raw = ''.join((item if isinstance(item, str) else json.dumps(item)) + '\n' for item in requests)
        command = [str(Path(sys.executable).resolve()), '-u', '-c', trial.MOCK_PROGRAM, str(log)]
        run = subprocess.run((prefix or []) + command, input=raw, capture_output=True, text=True,
                             encoding='utf-8', check=True)
        self.assertEqual(run.stderr, '')
        return [json.loads(line) for line in run.stdout.splitlines()]

    def minimal_skill(self, root):
        skill = root / 'source-skill'
        (skill / 'references').mkdir(parents=True)
        for name in ('SKILL.md', 'references/connection.md', 'references/grill.md', 'references/implementation.md'):
            (skill / name).write_text('Synthetic ' + name + '\n', encoding='utf-8')
        return skill

    def test_native_initialize_list_and_three_real_read_results(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            requests = [self.request(1, 'initialize', {'protocolVersion': '2025-03-26'}),
                        {'jsonrpc': '2.0', 'method': 'notifications/initialized'},
                        self.request(2, 'tools/list'),
                        self.request(3, 'tools/call', {'name': 'whoami', 'arguments': {}}),
                        self.request(4, 'tools/call', {'name': 'get_project', 'arguments': {'id': 'core-route-project'}}),
                        self.request(5, 'tools/call', {'name': 'list_project_columns', 'arguments': {'projectId': 'core-route-project'}})]
            responses = self.server(root / 'calls.jsonl', requests)
            self.assertEqual([item['id'] for item in responses], [1, 2, 3, 4, 5])
            self.assertEqual(responses[0]['result']['protocolVersion'], '2025-03-26')
            self.assertEqual({item['name'] for item in responses[1]['result']['tools']},
                             {'whoami', 'get_project', 'list_project_columns'})
            for tool in responses[1]['result']['tools']:
                self.assertEqual(tool['annotations'], {'readOnlyHint': True, 'destructiveHint': False,
                                                       'idempotentHint': True, 'openWorldHint': False})
            payloads = [json.loads(item['result']['content'][0]['text']) for item in responses[2:]]
            self.assertEqual(payloads[0]['id'], 'synthetic-user-17')
            self.assertEqual(payloads[1]['id'], 'core-route-project')
            self.assertEqual([column['name'] for column in payloads[2]], ['Todo', 'Doing', 'Done'])
            self.assertEqual([column['slug'] for column in payloads[2]], ['todo', 'doing', 'done'])
            self.assertEqual([column['isFinal'] for column in payloads[2]], [False, False, True])
            calls = [json.loads(line) for line in (root / 'calls.jsonl').read_text().splitlines()]
            self.assertEqual([item['tool'] for item in calls if 'tool' in item],
                             ['whoami', 'get_project', 'list_project_columns'])

    def test_native_malformed_rpc_and_unknown_method_fail_without_stopping_later_reads(self):
        with tempfile.TemporaryDirectory() as directory:
            responses = self.server(Path(directory) / 'calls.jsonl', [
                '{', [], self.request(1, 'not-a-method'), self.request(2, 'ping', []),
                self.request(3, 'tools/call', {'name': 'whoami', 'arguments': {}})])
            self.assertEqual([item['error']['code'] for item in responses[:4]],
                             [-32700, -32600, -32601, -32602])
            self.assertFalse(responses[4]['result']['isError'])

    def test_mutations_and_wrong_project_are_refused_and_log_is_append_only(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            log = root / 'calls.jsonl'
            sentinel = {'earlier': 'retained'}
            log.write_text(json.dumps(sentinel) + '\n')
            first = self.server(log, [self.request(1, 'tools/call', {
                'name': 'create_task', 'arguments': {'token': 'SYNTHETIC-DO-NOT-LOG', 'title': 'do not write'}})])
            second = self.server(log, [self.request(2, 'tools/call', {
                'name': 'get_project', 'arguments': {'id': 'other-project'}})])
            self.assertTrue(first[0]['result']['isError'])
            self.assertTrue(second[0]['result']['isError'])
            calls = [json.loads(line) for line in log.read_text().splitlines()]
            self.assertEqual(calls[0], sentinel)
            self.assertEqual(len(calls), 3)
            self.assertTrue(calls[1]['write_refused'])
            self.assertFalse(calls[2]['accepted'])
            self.assertNotIn('SYNTHETIC-DO-NOT-LOG', log.read_text())
            self.assertEqual({item.name for item in root.iterdir()}, {'calls.jsonl'})

    @unittest.skipUnless(platform.system() == 'Darwin', 'macOS specified-root guard control')
    def test_mock_can_append_while_its_log_directory_is_read_denied(self):
        with tempfile.TemporaryDirectory() as directory:
            evidence = Path(directory).resolve() / 'evidence'
            evidence.mkdir()
            profile = '(version 1)(allow default)(deny file-read* (subpath ' + json.dumps(str(evidence)) + '))'
            responses = self.server(evidence / 'calls.jsonl', [self.request(1, 'tools/call', {
                'name': 'whoami', 'arguments': {}})], ['/usr/bin/sandbox-exec', '-p', profile])
            self.assertFalse(responses[0]['result']['isError'])
            self.assertTrue(json.loads((evidence / 'calls.jsonl').read_text())['accepted'])

    def test_final_message_comes_from_completed_events_without_opening_worker_output_path(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            command = trial.command_for('codex', root / 'workspace', root / 'evidence', 'mcp-missing',
                                        ['-c', 'default_permissions="core_route"'])
            self.assertNotIn('-o', command)
            self.assertNotIn('--output-last-message', command)
            events = root / 'events.jsonl'
            message = {'type': 'item.completed', 'item': {'type': 'agent_message', 'text': 'Actual final'}}
            events.write_text(json.dumps(message) + '\n')
            self.assertIsNone(trial.terminal_message(events))
            with events.open('a') as stream:
                stream.write(json.dumps({'type': 'turn.completed'}) + '\n')
            self.assertEqual(trial.terminal_message(events), 'Actual final')
            with events.open('a') as stream:
                stream.write(json.dumps({'type': 'item.completed', 'item': {'type': 'agent_message', 'text': 'Incomplete later message'}}) + '\n')
            self.assertIsNone(trial.terminal_message(events))

    def test_preparation_freezes_equal_inputs_and_rejects_reuse(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill = self.minimal_skill(root)
            output = root / 'trial'
            manifest = trial.prepare(output, skill, REPOSITORY)
            a, b = [manifest['conditions'][key] for key in ('mcp-present', 'mcp-missing')]
            self.assertEqual(a['before'], b['before'])
            self.assertEqual(a['prompt_sha256'], b['prompt_sha256'])
            self.assertEqual((output / 'mcp-present/prompt.txt').read_bytes(),
                             (output / 'mcp-missing/prompt.txt').read_bytes())
            self.assertIsNone(manifest['model_override'])
            self.assertFalse(manifest['real_pms'])
            with self.assertRaises(ValueError):
                trial.prepare(output, skill, REPOSITORY)

    def test_input_drift_blocks_before_authentication_or_process_creation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output = root / 'trial'
            trial.prepare(output, self.minimal_skill(root), REPOSITORY)
            (output / 'mcp-present/workspace/index.html').write_text('drift')
            with patch.object(trial, 'existing_auth_home') as auth, patch.object(trial.subprocess, 'Popen') as launch:
                with self.assertRaises(ValueError):
                    trial.run_condition(output, 'mcp-present', 'unused-cli', 1)
            auth.assert_not_called()
            launch.assert_not_called()

    def test_sequential_conditions_keep_frozen_runtime_and_cannot_be_replayed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output = root / 'trial'
            manifest = trial.prepare(output, self.minimal_skill(root), REPOSITORY)
            with patch.object(trial, 'existing_auth_home', return_value='synthetic-auth-channel'), \
                 patch.object(trial, 'native_permission_probe', return_value={'passed': True}), \
                 patch.object(trial.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, stdout='synthetic-cli\n')), \
                 patch.object(trial.subprocess, 'Popen') as launch:
                launch.return_value.pid = 123
                launch.return_value.returncode = 0
                for condition in ('mcp-present', 'mcp-missing'):
                    result = trial.run_condition(output, condition, 'unused-cli', 1)
                    self.assertEqual(result['state'], 'completed')
                    self.assertTrue((output / condition / 'control/job.json').is_file())
                    self.assertEqual(trial.inventory(output / 'runtime'), manifest['runtime_hashes'])
                with self.assertRaises(ValueError):
                    trial.run_condition(output, 'mcp-present', 'unused-cli', 1)
            self.assertEqual(launch.call_count, 2)

    def test_changed_mock_blocks_before_authentication_or_process_creation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output = root / 'trial'
            trial.prepare(output, self.minimal_skill(root), REPOSITORY)
            with patch.object(trial, 'MOCK_PROGRAM', trial.MOCK_PROGRAM + '\n# changed'), \
                 patch.object(trial, 'existing_auth_home') as auth, \
                 patch.object(trial.subprocess, 'Popen') as launch:
                with self.assertRaises(ValueError):
                    trial.run_condition(output, 'mcp-present', 'unused-cli', 1)
            auth.assert_not_called()
            launch.assert_not_called()

    def test_commands_have_no_model_override_or_trust_and_missing_condition_has_no_mcp(self):
        workspace, evidence = Path('/synthetic/workspace'), Path('/synthetic/evidence')
        config = ['-c', 'default_permissions="core_route"']
        present = trial.command_for('codex', workspace, evidence, 'mcp-present', config)
        missing = trial.command_for('codex', workspace, evidence, 'mcp-missing', config)
        for command in (present, missing):
            self.assertIn('--ignore-user-config', command)
            self.assertIn('--ignore-rules', command)
            self.assertIn('--ephemeral', command)
            self.assertNotIn('--sandbox', command)
            self.assertIn('default_permissions="core_route"', command)
            self.assertFalse({'--trust', '-m', '--model', '--dangerously-bypass-approvals-and-sandbox'}.intersection(command))
        self.assertTrue(any(item.startswith('mcp_servers.kaneo.command=') for item in present))
        self.assertFalse(any('mcp_servers' in item for item in missing))

    def test_native_profile_allows_only_workspace_writes_and_retains_denials(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            workspace = root / 'workspace'
            workspace.mkdir()
            denied = [root / 'source', root / 'personal skills', root / 'evaluator']
            overrides = trial.native_permission_overrides(workspace, denied)
            config = tomllib.loads('\n'.join(overrides[1::2]))
            self.assertEqual(config['default_permissions'], 'core_route')
            profile = config['permissions']['core_route']
            self.assertEqual(profile['filesystem']['/'], 'read')
            self.assertEqual(profile['filesystem'][str(workspace)], 'write')
            self.assertEqual([path for path, mode in profile['filesystem'].items() if mode == 'write'], [str(workspace)])
            for path in denied:
                self.assertEqual(profile['filesystem'][str(path)], 'deny')
            self.assertFalse(profile['network']['enabled'])
            with self.assertRaises(ValueError):
                trial.native_permission_overrides(workspace, [root])

    def test_optimized_native_probe_rejects_bad_input_before_any_write(self):
        for optimization in ('-O', '-OO'):
            with self.subTest(optimization=optimization), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                workspace, local, outside = root / 'workspace', root / 'workspace/local', root / 'outside'
                local.mkdir(parents=True)
                outside.mkdir()
                (local / 'input.txt').write_text('WRONG', encoding='utf-8')
                (outside / 'input.txt').write_text('READONLY-SYNTHETIC', encoding='utf-8')
                spec = {'workspace': str(workspace), 'local': str(local), 'outside': str(outside),
                        'denied_files': [], 'denied_directories': [], 'auth_paths': [], 'port': 0}
                run = subprocess.run([str(Path(sys.executable).resolve()), optimization, '-B', '-c',
                                      trial.NATIVE_PROBE_PROGRAM, json.dumps(spec)],
                                     capture_output=True, text=True, timeout=10)
                observed = {'exit_code': run.returncode, 'local_write_created': (local / 'write.txt').exists(),
                            'outside_write_created': (outside / 'new.txt').exists()}
                self.assertEqual(observed, {'exit_code': 56, 'local_write_created': False,
                                            'outside_write_created': False})
                self.assertEqual((outside / 'input.txt').read_text(encoding='utf-8'), 'READONLY-SYNTHETIC')

    def test_auth_uses_existing_channel_without_copying_or_overwriting(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            original = root / 'existing'
            original.mkdir()
            (original / 'auth.json').write_text('{"synthetic":true}')
            destination = root / 'private'
            with patch.dict(os.environ, {'CODEX_HOME': str(original)}):
                try:
                    description = trial.existing_auth_home(destination)
                except OSError as error:
                    if os.name == 'nt' and getattr(error, 'winerror', None) == 1314:
                        self.skipTest('Windows host does not permit creating file symlinks')
                    raise
                with self.assertRaises(FileExistsError):
                    trial.existing_auth_home(destination)
            self.assertTrue((destination / 'auth.json').is_symlink())
            self.assertEqual((original / 'auth.json').read_text(), '{"synthetic":true}')
            self.assertNotIn('synthetic', description)

    def test_path_mention_is_not_full_reference_read_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workspace = root / 'workspace'
            skill = workspace / '.agents/skills/engineering-loop'
            skill.mkdir(parents=True)
            (skill / 'SKILL.md').write_text('Frozen entrypoint\n')
            path = '.agents/skills/engineering-loop/SKILL.md'
            events = root / 'events.jsonl'
            records = [
                {'type': 'item.completed', 'item': {'type': 'command_execution', 'command': 'echo ' + path,
                 'aggregated_output': path, 'exit_code': 0}},
                {'type': 'item.completed', 'item': {'type': 'command_execution', 'command': 'cat ' + path,
                 'aggregated_output': 'Frozen entrypoint\n', 'exit_code': 0}}]
            events.write_text(''.join(json.dumps(item) + '\n' for item in records))
            summary = trial.event_summary(events, workspace, trial.inventory(workspace))
            self.assertFalse(summary['reference_read_candidates'][0]['full_frozen_content_in_output'])
            self.assertTrue(summary['reference_read_candidates'][1]['full_frozen_content_in_output'])

    def test_modified_reference_cannot_be_called_full_frozen_content(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workspace = root / 'workspace'
            skill = workspace / '.agents/skills/engineering-loop'
            skill.mkdir(parents=True)
            entry = skill / 'SKILL.md'
            entry.write_text('Original frozen entrypoint\n')
            frozen = trial.inventory(workspace)
            entry.write_text('Candidate replacement\n')
            events = root / 'events.jsonl'
            event = {'type': 'item.completed', 'item': {'type': 'command_execution',
                     'command': 'cat .agents/skills/engineering-loop/SKILL.md',
                     'aggregated_output': 'Candidate replacement\n', 'exit_code': 0}}
            events.write_text(json.dumps(event) + '\n')
            summary = trial.event_summary(events, workspace, frozen)
            self.assertEqual(summary['reference_drift'], ['.agents/skills/engineering-loop/SKILL.md'])
            self.assertFalse(summary['reference_read_candidates'][0]['reference_matches_frozen_hash'])
            self.assertFalse(summary['reference_read_candidates'][0]['full_frozen_content_in_output'])

    @unittest.skipUnless(os.name == 'posix', 'owned POSIX process-group control')
    def test_timeout_cleanup_kills_and_reaps_a_real_term_ignoring_group(self):
        code = 'import signal,time\nsignal.signal(signal.SIGTERM,signal.SIG_IGN)\nprint("READY",flush=True)\nwhile True: time.sleep(1)\n'
        process = subprocess.Popen([str(Path(sys.executable).resolve()), '-c', code],
                                   stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   start_new_session=True)
        try:
            self.assertEqual(process.stdout.readline(), b'READY\n')
            with self.assertRaises(subprocess.TimeoutExpired):
                process.communicate(timeout=0.01)
            details = trial.terminate_process_group(process, grace=0.05)
            self.assertTrue(details['term_sent'])
            self.assertTrue(details['kill_sent'])
            self.assertTrue(details['wrapper_reaped'])
            self.assertEqual(process.returncode, -signal.SIGKILL)
        finally:
            if process.poll() is None:
                os.killpg(process.pid, signal.SIGKILL)
                process.communicate(timeout=2)

    @unittest.skipUnless(os.name == 'posix', 'owned POSIX process-group state control')
    def test_timeout_persists_terminal_state_and_refuses_replay_after_second_wait_expires(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output = root / 'trial'
            trial.prepare(output, self.minimal_skill(root), REPOSITORY)
            with patch.object(trial, 'existing_auth_home', return_value='synthetic-auth-channel'), \
                 patch.object(trial, 'native_permission_probe', return_value={'passed': True}), \
                 patch.object(trial.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, stdout='synthetic-cli\n')), \
                 patch.object(trial.subprocess, 'Popen') as launch, \
                 patch.object(trial.os, 'killpg') as send:
                process = launch.return_value
                process.pid, process.returncode = 123, -signal.SIGKILL
                process.communicate.side_effect = [subprocess.TimeoutExpired('synthetic', 1),
                                                   subprocess.TimeoutExpired('synthetic', 1), (b'', b'')]
                result = trial.run_condition(output, 'mcp-present', 'unused-cli', 1)
                self.assertEqual(result['state'], 'timeout')
                manifest = json.loads((output / 'manifest.json').read_text())
                self.assertTrue(manifest['conditions']['mcp-present']['termination']['wrapper_reaped'])
                self.assertTrue(manifest['conditions']['mcp-present']['termination']['kill_sent'])
                with self.assertRaises(ValueError):
                    trial.run_condition(output, 'mcp-present', 'unused-cli', 1)
                self.assertEqual([call.args[1] for call in send.call_args_list], [signal.SIGTERM, signal.SIGKILL])

    def test_independent_byte_comparison_rejects_extra_changes_and_handles_deletion(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            base = root / 'trial'
            workspace, evidence = base / 'workspace', base / 'evidence'
            workspace.mkdir(parents=True)
            evidence.mkdir()
            (evidence / 'events.jsonl').write_text('')
            (workspace / 'index.html').write_text(trial.BEFORE)
            (workspace / 'AGENTS.md').write_text('original')
            initial = trial.inventory(workspace)
            (workspace / 'index.html').write_text(trial.AFTER)
            (workspace / 'AGENTS.md').write_text('changed')
            result = trial.result_summary(base, initial, 0, False)
            self.assertTrue(result['index_exact_approved_result'])
            self.assertEqual(result['changed_paths'], ['AGENTS.md', 'index.html'])
            (workspace / 'index.html').unlink()
            deleted = trial.result_summary(base, initial, 0, False)
            self.assertFalse(deleted['index_exact_approved_result'])
            self.assertFalse(deleted['index_unchanged'])


if __name__ == '__main__':
    unittest.main()
