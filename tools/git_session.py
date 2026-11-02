#!/usr/bin/env python3
"""Pull before editing; explicitly stage, commit and push at each handoff."""
import argparse
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def git(*args, capture=False):
    result = subprocess.run(['git', *args], cwd=ROOT, text=True,
                            stdout=subprocess.PIPE if capture else None, check=True)
    return result.stdout.strip() if capture else None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='action', required=True)
    sub.add_parser('begin')
    finish = sub.add_parser('finish')
    finish.add_argument('--message')
    finish.add_argument('--paths', nargs='+', default=[])
    args = parser.parse_args()
    if Path(git('rev-parse', '--show-toplevel', capture=True)).resolve() != ROOT:
        parser.error('This directory must be its own Git repository')
    branch = git('symbolic-ref', '--quiet', '--short', 'HEAD', capture=True)
    git('remote', 'get-url', 'origin')
    if args.action == 'begin':
        if git('status', '--porcelain', '--untracked-files=normal', capture=True):
            parser.error('Worktree contains existing work. Preserve/reconcile it before pulling.')
        git('pull', '--ff-only', 'origin', branch)
        print('Synchronized. Read current instructions and handoff before editing.')
        return
    if git('diff', '--cached', '--name-only', capture=True):
        parser.error('Existing staged work must be reconciled explicitly; nothing was staged or committed.')
    if args.paths:
        if not args.message:
            parser.error('--message is required when staging paths')
        for raw in args.paths:
            if raw.startswith(':'):
                parser.error('Git pathspec magic is not accepted; use explicit relative paths')
            path = (ROOT / raw).resolve()
            if not path.is_relative_to(ROOT) or '.git' in path.relative_to(ROOT).parts:
                parser.error('All paths must stay inside the notes worktree, outside .git')
        git('add', '-A', '--', *args.paths)
        git('diff', '--cached', '--check')
        if git('diff', '--cached', '--name-only', capture=True):
            git('commit', '-m', args.message)
    if git('status', '--porcelain', '--untracked-files=normal', capture=True):
        parser.error('Uncommitted work remains; include/reconcile intended paths before the handoff.')
    git('push', '--set-upstream', 'origin', branch)
    print('Push completed. Record the resulting commit in the task handoff.')


if __name__ == '__main__':
    main()
