"""macOS command wrapper restricting reads of explicitly named directories only."""
import json
from pathlib import Path
import platform
import subprocess
import tempfile
import sys
import os


def run_guarded(command, workspace, denied_roots, receipt):
    """Probe the actual policy, then run argv; unsupported or failed probes stop dispatch."""
    workspace = Path(workspace).resolve(strict=True)
    roots = [Path(root).resolve(strict=True) for root in denied_roots]
    receipt = Path(receipt).resolve()
    if receipt.exists():
        raise ValueError('receipt must be a new path; stale receipts are not reused')
    if not command or not roots or not workspace.is_dir() or any(not root.is_dir() for root in roots):
        raise ValueError('command, workspace and existing denied directories are required')
    if any(workspace == root or root in workspace.parents for root in roots):
        raise ValueError('workspace must not be under a denied root')
    if any(receipt == root or root in receipt.parents for root in roots):
        raise ValueError('receipt must be outside denied roots')
    if platform.system() != 'Darwin' or not Path('/usr/bin/sandbox-exec').is_file():
        raise RuntimeError('macOS sandbox-exec is required; command was not started')
    # Never expose real evaluator data: create synthetic probes in each real denied root.
    with tempfile.TemporaryDirectory(prefix='read-guard-', dir=workspace) as local:
        local = Path(local)
        inside = local / 'inside'; inside.write_text('INSIDE', encoding='utf-8')
        output = local / 'output'
        profile = '(version 1)(allow default)' + ''.join(
            '(deny file-read* (subpath ' + json.dumps(str(root), ensure_ascii=False) + '))' for root in roots)
        markers = []
        try:
            for index, root in enumerate(roots):
                handle = tempfile.NamedTemporaryFile(prefix='.read-guard-', dir=root, delete=False)
                marker = Path(handle.name); markers.append(marker)
                with handle: handle.write(b'SYNTHETIC-CANARY')
                if marker.read_bytes() != b'SYNTHETIC-CANARY':
                    raise RuntimeError('unrestricted canary read failed; command was not started')
                link = local / ('link-' + str(index)); link.symlink_to(marker)
                # PermissionError is distinct from missing files or failed interpreter startup.
                script = '''import pathlib,sys
for name in sys.argv[1:4]:
 try: pathlib.Path(name).read_bytes()
 except PermissionError: pass
 else: raise SystemExit(31)
if pathlib.Path(sys.argv[4]).read_text() != 'INSIDE': raise SystemExit(32)
pathlib.Path(sys.argv[5]).write_text('WRITABLE')
print('READ-GUARD-PROBE-COMPLETE')
'''
                result = subprocess.run(['/usr/bin/sandbox-exec', '-p', profile, sys.executable,
                    '-c', script, str(marker), os.path.relpath(marker, workspace), str(link),
                    str(inside), str(output)], cwd=workspace, capture_output=True)
                if result.returncode != 0 or result.stdout.strip() != b'READ-GUARD-PROBE-COMPLETE' or not output.exists() or output.read_text() != 'WRITABLE':
                    raise RuntimeError('read restriction probe failed; command was not started')
                output.unlink()
            result = subprocess.run(['/usr/bin/sandbox-exec', '-p', profile, *map(str, command)], cwd=workspace)
            report = {'scope': 'reads of specified canonical directories only',
                      'denied_roots': list(map(str, roots)), 'root_probes': [
                          {'root': str(root), 'absolute_relative_symlink_denied': True,
                           'workspace_read_write': True} for root in roots], 'probe_passed': True,
                      'command_exit_code': result.returncode}
            receipt.parent.mkdir(parents=True, exist_ok=True)
            with receipt.open('x', encoding='utf-8') as stream:
                stream.write(json.dumps(report, indent=2) + '\n')
            return result.returncode
        finally:
            for marker in markers: marker.unlink(missing_ok=True)
