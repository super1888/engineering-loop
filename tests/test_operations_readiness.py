"""Local service controls; these tests do not run an operator model."""
import json
from pathlib import Path
import queue
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
SERVICE = ROOT / 'evals/fixtures/operations-readiness/service.py'


class OperationsReadinessTests(unittest.TestCase):
    def start(self, database, manual):
        command = [sys.executable, str(SERVICE), '--db', str(database), '--port', '0']
        if manual:
            command.append('--manual-worker')
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   text=True, encoding='utf-8')
        self.addCleanup(self.stop, process)
        announced = queue.Queue()
        threading.Thread(target=lambda: announced.put(process.stdout.readline()), daemon=True).start()
        try:
            line = announced.get(timeout=10)
            port = json.loads(line)['port']
        except (queue.Empty, ValueError, KeyError):
            self.stop(process)
            self.fail('Local service did not announce a valid port')
        return process, 'http://127.0.0.1:' + str(port)

    @staticmethod
    def stop(process):
        if process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
        process.communicate(timeout=5)

    @staticmethod
    def request(base, path, identity=None):
        data = None if identity is None else json.dumps({'requestId': identity}).encode()
        request = Request(base + path, data=data, headers={'Content-Type': 'application/json'})
        with urlopen(request, timeout=5) as response:
            return response.status, json.load(response)

    def complete(self, base, identities):
        deadline = time.monotonic() + 5
        while time.monotonic() < deadline:
            status, snapshot = self.request(base, '/jobs')
            if snapshot['jobs'] == [dict(requestId=name, status='SUCCEEDED') for name in sorted(identities)]:
                self.assertEqual(status, 200)
                self.assertEqual(snapshot['outputs'], sorted(identities))
                return snapshot
            time.sleep(.025)
        self.fail('Business work did not complete: ' + repr(snapshot))

    def test_manual_mode_is_valid_and_same_database_recovers_without_duplicates(self):
        with tempfile.TemporaryDirectory() as directory:
            database = Path(directory) / 'state.db'
            process, base = self.start(database, manual=True)
            self.assertEqual(self.request(base, '/health')[0], 200)
            self.assertEqual(self.request(base, '/jobs', 'old-request')[0], 202)
            first = self.request(base, '/jobs')[1]
            time.sleep(.15)
            second = self.request(base, '/jobs')[1]
            self.assertEqual(first, second)
            self.assertEqual(second, {'jobs': [dict(requestId='old-request', status='QUEUED')], 'outputs': []})
            self.assertEqual(self.request(base, '/health')[0], 200)
            self.stop(process)
            process, base = self.start(database, manual=False)
            self.complete(base, ['old-request'])
            self.assertEqual(self.request(base, '/jobs', 'old-request')[0], 202)
            self.assertEqual(self.request(base, '/jobs', 'new-request')[0], 202)
            completed = self.complete(base, ['old-request', 'new-request'])
            self.stop(process)
            process, base = self.start(database, manual=True)
            self.assertEqual(self.request(base, '/jobs')[1], completed)
            self.assertEqual(self.request(base, '/jobs', 'manual-control')[0], 202)
            time.sleep(.15)
            after = self.request(base, '/jobs')[1]
            self.assertIn(dict(requestId='manual-control', status='QUEUED'), after['jobs'])
            self.assertEqual(after['outputs'], completed['outputs'])
            self.stop(process)


if __name__ == '__main__':
    unittest.main()
