"""Loopback-only two-version release exercise; not a deployment service."""
import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--port', type=int, default=0)
    args = parser.parse_args()
    root = args.root.resolve()
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass
        def do_GET(self):
            config = json.loads((root / 'deployment.json').read_text(encoding='utf-8'))
            active = config['active']
            if self.path == '/health':
                content, mime = b'{"alive":true}', 'application/json'
            elif self.path == '/':
                content, mime = (root / 'assets' / active / 'index.html').read_bytes(), 'text/html; charset=utf-8'
            elif self.path in ('/assets/v1/detail.js', '/assets/v2/detail.js'):
                version = self.path.split('/')[2]
                if version not in [active, *config['retained']]:
                    self.send_error(404); return
                content, mime = (root / self.path.lstrip('/')).read_bytes(), 'text/javascript; charset=utf-8'
            else:
                self.send_error(404); return
            self.send_response(200)
            self.send_header('Content-Type', mime)
            self.send_header('Cache-Control', 'no-store')
            self.send_header('Content-Length', str(len(content)))
            self.end_headers()
            self.wfile.write(content)
    server = ThreadingHTTPServer(('127.0.0.1', args.port), Handler)
    print(json.dumps({'port': server.server_port}), flush=True)
    server.serve_forever()


if __name__ == '__main__':
    main()
