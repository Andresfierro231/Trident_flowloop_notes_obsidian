"""Check unpublished edits/secrets and external aliases cannot enter an export."""
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location('exporter', Path(__file__).with_name('export_box_notes.py'))
EXPORTER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(EXPORTER)


class ExportSafety(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.repo = self.base / 'repo'
        self.repo.mkdir()
        def git(*args):
            return subprocess.check_output(['git', *args], cwd=self.repo, stderr=subprocess.DEVNULL)
        self.git = git
        git('init')
        git('config', 'user.name', 'Export test')
        git('config', 'user.email', 'export@example.invalid')
        (self.repo / 'note.md').write_bytes(b'Author note\r\n')
        (self.repo / 'asset.bin').write_bytes(bytes(range(256)))
        (self.base / 'outside_secret').write_text('outside unpublished secret')
        (self.repo / 'external_alias').symlink_to(self.base / 'outside_secret')
        git('add', '.')
        git('commit', '-m', 'Fixture')
        (self.repo / 'untracked_secret').write_text('not in committed tree')

    def test_regular_committed_bytes_only_and_parallel_equivalence(self):
        serial = EXPORTER.export_tree(self.repo, 'HEAD', self.base / 'serial', self.base / 's.json', 1)
        parallel = EXPORTER.export_tree(self.repo, 'HEAD', self.base / 'parallel', self.base / 'p.json', 4)
        self.assertEqual(serial['files'], parallel['files'])
        self.assertEqual(parallel['file_count'], 2)
        self.assertEqual([row['path'] for row in parallel['skipped']], ['external_alias'])
        self.assertFalse((self.base / 'parallel/external_alias').exists())
        self.assertFalse((self.base / 'parallel/untracked_secret').exists())
        self.assertEqual((self.base / 'parallel/asset.bin').read_bytes(), bytes(range(256)))
        self.assertEqual(json.loads((self.base / 'p.json').read_text())['status'], 'prepared_not_published')
        with self.assertRaises(FileExistsError):
            EXPORTER.export_tree(self.repo, 'HEAD', self.base / 'parallel', self.base / 'new.json')

    def test_uncommitted_changed_note_cannot_be_published_as_old_commit(self):
        (self.repo / 'note.md').write_text('Changed independently')
        with self.assertRaisesRegex(ValueError, 'differs from pinned Git blob'):
            EXPORTER.export_tree(self.repo, 'HEAD', self.base / 'bad', self.base / 'bad.json')
        self.assertFalse((self.base / 'bad.json').exists())


if __name__ == '__main__':
    unittest.main()
