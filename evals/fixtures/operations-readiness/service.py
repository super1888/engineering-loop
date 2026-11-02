"""Local operational exercise: durable jobs with an optional automatic worker."""
import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import sqlite3
import threading
import time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--db', required=True)
    parser.add_argument('--port', type=int, default=0)
    parser.add_argument('--manual-worker', action='store_true')
    args = parser.parse_args()
    def connect():
        return sqlite3.connect(args.db, timeout=5)
    with connect() as db:
        db.executescript('CREATE TABLE IF NOT EXISTS jobs(request_id TEXT PRIMARY KEY, status TEXT NOT NULL); CREATE TABLE IF NOT EXISTS outputs(request_id TEXT PRIMARY KEY);')
    def snapshot():
        with connect() as db:
            return {'jobs': [dict(requestId=r[0], status=r[1]) for r in db.execute('SELECT request_id,status FROM jobs ORDER BY request_id')], 'outputs': [r[0] for r in db.execute('SELECT request_id FROM outputs ORDER BY request_id')]}
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass
        def reply(self, code, body):
            content = json.dumps(body).encode()
            self.send_response(code); self.send_header('Content-Type', 'application/json'); self.send_header('Content-Length', str(len(content))); self.end_headers(); self.wfile.write(content)
        def do_GET(self):
            if self.path == '/health': self.reply(200, {'alive': True})
            elif self.path == '/jobs': self.reply(200, snapshot())
            else: self.reply(404, {'error': 'not found'})
        def do_POST(self):
            if self.path != '/jobs': self.reply(404, {'error': 'not found'}); return
            try:
                body = json.loads(self.rfile.read(int(self.headers.get('Content-Length', '0'))))
                identity = body['requestId']
                if not isinstance(identity, str) or not identity.strip(): raise ValueError()
            except (ValueError, KeyError, TypeError): self.reply(400, {'error': 'requestId required'}); return
            with connect() as db:
                db.execute('INSERT OR IGNORE INTO jobs VALUES (?, ?)', (identity, 'QUEUED'))
            self.reply(202, snapshot())
    def worker():
        while True:
            with connect() as db:
                db.execute('BEGIN IMMEDIATE')
                for identity, in db.execute("SELECT request_id FROM jobs WHERE status='QUEUED'").fetchall():
                    db.execute('INSERT OR IGNORE INTO outputs VALUES (?)', (identity,))
                    db.execute("UPDATE jobs SET status='SUCCEEDED' WHERE request_id=?", (identity,))
            time.sleep(.05)
    if not args.manual_worker: threading.Thread(target=worker, daemon=True).start()
    server = ThreadingHTTPServer(('127.0.0.1', args.port), Handler)
    print(json.dumps({'port': server.server_port}), flush=True)
    server.serve_forever()


if __name__ == '__main__': main()
