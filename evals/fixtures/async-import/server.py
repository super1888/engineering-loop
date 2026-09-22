import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import sys
import threading
from urllib.parse import urlparse, unquote

from backend.service import ImportService


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--db', required=True)
    parser.add_argument('--port', type=int, default=0)
    parser.add_argument('--manual-worker', action='store_true')
    parser.add_argument('--fail-once-row', default='')
    args = parser.parse_args()
    failed = set()
    lock = threading.Lock()

    def processor(row):
        with lock:
            if row['rowId'] == args.fail_once_row and row['rowId'] not in failed:
                failed.add(row['rowId'])
                raise RuntimeError('temporary processor failure')
        return row['name']

    service = ImportService(args.db, processor)
    ui = Path(__file__).parent / 'ui'

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *unused):
            pass

        def reply(self, status, body):
            payload = json.dumps(body).encode()
            self.send_response(status)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)

        def do_GET(self):
            path = urlparse(self.path).path
            if path.startswith('/api/batches/'):
                try:
                    self.reply(200, service.snapshot(unquote(path[len('/api/batches/'):])) )
                except KeyError:
                    self.reply(404, {'error': 'batch not found'})
                return
            name = path.lstrip('/') or 'index.html'
            if name not in ('index.html', 'app.js'):
                self.reply(404, {'error': 'not found'})
                return
            payload = (ui / name).read_bytes()
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8' if name.endswith('.html') else 'text/javascript')
            self.end_headers()
            self.wfile.write(payload)

        def do_POST(self):
            try:
                body = json.loads(self.rfile.read(int(self.headers.get('Content-Length', 0))))
                path = urlparse(self.path).path
                if path == '/api/batches':
                    result = service.submit(body.get('requestId'), body.get('rows'))
                elif path.startswith('/api/batches/') and path.endswith('/retry'):
                    batch_id = unquote(path[len('/api/batches/'):-len('/retry')])
                    result = service.retry(batch_id, body.get('requestId'))
                else:
                    self.reply(404, {'error': 'not found'})
                    return
                self.reply(202, result)
            except KeyError:
                self.reply(404, {'error': 'batch not found'})
            except ValueError as error:
                self.reply(409 if 'conflict' in str(error).lower() else 400, {'error': str(error)})
            except NotImplementedError as error:
                self.reply(501, {'error': str(error)})

    server = ThreadingHTTPServer(('127.0.0.1', args.port), Handler)
    stop = threading.Event()

    def work():
        if args.manual_worker:
            for line in sys.stdin:
                if line.strip() == 'process':
                    service.process_next()
        else:
            while not stop.wait(0.05):
                service.process_next()

    threading.Thread(target=work, daemon=True).start()
    print(json.dumps({'port': server.server_port}), flush=True)
    try:
        server.serve_forever()
    finally:
        stop.set()
        server.server_close()


if __name__ == '__main__':
    main()
