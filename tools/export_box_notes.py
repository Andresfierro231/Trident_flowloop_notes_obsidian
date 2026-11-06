#!/usr/bin/env python3
"""Prepare a hash-verified regular-file export of an exact notes Git commit.

No Box writes, alias traversal or content rendering. Partial staging is retained
on error and must never be published without a successful manifest.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]


def git(repo, *args):
    return subprocess.check_output(['git', *args], cwd=repo)


def export_tree(repo, revision, destination, receipt, workers=4):
    if not 1 <= workers <= 32:
        raise ValueError('workers must be between 1 and 32, within the allocation')
    repo, destination, receipt = map(lambda p: Path(p).resolve(), (repo, destination, receipt))
    if destination == repo or repo in destination.parents:
        raise ValueError('Export must be outside the notes Git worktree')
    if receipt == destination or destination in receipt.parents:
        raise ValueError('Receipt must be outside the export')
    if receipt.exists():
        raise FileExistsError(receipt)
    pinned = git(repo, 'rev-parse', '--verify', '--end-of-options', revision + '^{commit}').decode().strip()
    tree = git(repo, 'ls-tree', '-rz', pinned)
    entries, skipped = [], []
    for raw in tree.split(b'\0'):
        if not raw:
            continue
        metadata, path_bytes = raw.split(b'\t', 1)
        mode, kind, oid = metadata.decode().split()
        path = os.fsdecode(path_bytes)
        relative = PurePosixPath(path)
        if relative.is_absolute() or '..' in relative.parts or '.git' in relative.parts:
            raise ValueError('Unsafe Git path: ' + path)
        if kind != 'blob' or mode not in ('100644', '100755'):
            skipped.append({'path': path, 'reason': 'non-regular tracked entry; target not traversed'})
        else:
            entries.append((path, mode, oid))
    destination.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()

    def copy_one(entry):
        path, mode, expected_oid = entry
        source, target = repo / path, destination / path
        if not source.resolve().is_relative_to(repo):
            raise ValueError('Source escapes notes worktree: ' + path)
        target.parent.mkdir(parents=True, exist_ok=True)
        flags = os.O_RDONLY | getattr(os, 'O_NOFOLLOW', 0)
        with os.fdopen(os.open(source, flags), 'rb') as incoming:
            size = os.fstat(incoming.fileno()).st_size
            blob = hashlib.sha1(b'blob ' + str(size).encode() + b'\0')
            sha1, sha256, copied = hashlib.sha1(), hashlib.sha256(), 0
            with target.open('xb') as outgoing:
                while True:
                    chunk = incoming.read(1024 * 1024)
                    if not chunk:
                        break
                    outgoing.write(chunk)
                    blob.update(chunk)
                    sha1.update(chunk)
                    sha256.update(chunk)
                    copied += len(chunk)
        if copied != size or blob.hexdigest() != expected_oid:
            raise ValueError('Source differs from pinned Git blob; partial export NOT publishable: ' + path)
        target.chmod(0o755 if mode == '100755' else 0o644)
        return {'path': path, 'bytes': copied, 'git_blob': expected_oid,
                'sha1': sha1.hexdigest(), 'sha256': sha256.hexdigest()}

    with ThreadPoolExecutor(max_workers=workers) as pool:
        rows = sorted(pool.map(copy_one, entries), key=lambda row: row['path'])
    result = {'status': 'prepared_not_published', 'revision': pinned,
              'destination': str(destination), 'file_count': len(rows),
              'bytes': sum(row['bytes'] for row in rows), 'files': rows,
              'skipped': skipped, 'workers': workers,
              'elapsed_seconds': round(time.monotonic() - started, 3),
              'limits': 'Every exported byte matches its pinned Git blob; no Box delivery or scientific content review claimed.'}
    receipt.parent.mkdir(parents=True, exist_ok=True)
    temporary = receipt.with_name(receipt.name + '.tmp')
    with temporary.open('x') as output:
        json.dump(result, output, indent=2)
        output.write('\n')
    temporary.replace(receipt)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--revision', default='HEAD')
    parser.add_argument('--destination', required=True, type=Path)
    parser.add_argument('--receipt', required=True, type=Path)
    parser.add_argument('--workers', type=int, default=4)
    args = parser.parse_args()
    result = export_tree(ROOT, args.revision, args.destination, args.receipt, args.workers)
    print(json.dumps({key: value for key, value in result.items() if key != 'files'}, indent=2))


if __name__ == '__main__':
    main()
