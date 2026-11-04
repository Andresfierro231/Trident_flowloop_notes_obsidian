#!/usr/bin/env python3
"""Offline catalog/setup smoke tests; isolated temporary projects, no network/models."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('trident_catalog', HERE/'catalog.py')
catalog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalog)


class CatalogChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='trident-skills-')
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.notes = self.base/'notes'
        self.pack = self.notes/'.agents/skills'
        shutil.copytree(catalog.PACK, self.pack)
        self.index = self.notes/'SKILLS.md'
        self.index.write_text(catalog.render(catalog.entries(self.pack)))
        self.target = self.base/'a project with spaces'
        self.target.mkdir()
        (self.target/'AGENTS.md').write_text('Existing project instructions\n')

    def test_metadata_and_context_budgets(self):
        result = catalog.validate(self.pack, self.index)
        self.assertEqual(result['skills'], 7)
        self.assertLessEqual(result['catalog_characters'], catalog.MAX_CATALOG)
        self.assertLessEqual(result['largest_skill_characters'], catalog.MAX_SKILL)

    def test_real_task_lookup_metadata(self):
        items = catalog.entries(self.pack)
        cases = {'equations':'trident-equation-audit', 'citations':'trident-source-check',
                 'failures':'trident-debug', 'scoped diff':'trident-code-review',
                 'Obsidian':'trident-obsidian', 'LaTeX':'trident-manuscript',
                 'Slurm':'trident-hpc-jobs'}
        for query, expected in cases.items():
            selected = [item['name'] for item in items if query.casefold() in
                        (item['name']+' '+item['description']).casefold()]
            self.assertIn(expected, selected)
        self.assertFalse([item for item in items if 'unrelated arithmetic' in item['description']])

    def test_dry_run_writes_nothing(self):
        result = catalog.link_checkout(self.target, False, self.pack, self.index)
        self.assertEqual(result['status'], 'dry_run')
        self.assertFalse((self.target/'.agents').exists())
        self.assertFalse((self.target/'SKILLS.md').exists())

    def test_relative_aliases_idempotence_and_cross_owner_access(self):
        result = catalog.link_checkout(self.target, True, self.pack, self.index)
        self.assertEqual(result['status'], 'linked')
        for link in [self.target/'SKILLS.md', self.target/'.agents/skills']:
            self.assertTrue(link.is_symlink())
            self.assertFalse(Path(link.readlink()).is_absolute())
        self.assertEqual((self.target/'SKILLS.md').read_bytes(), self.index.read_bytes())
        self.assertEqual(len(list((self.target/'.agents/skills').glob('*/SKILL.md'))), 7)
        self.assertEqual(catalog.link_checkout(self.target, True, self.pack, self.index)['status'], 'unchanged')
        self.assertEqual((self.target/'AGENTS.md').read_text(), 'Existing project instructions\n')

    def test_catalog_collision_does_not_partially_install(self):
        (self.target/'SKILLS.md').write_text('User catalog\n')
        with self.assertRaises(ValueError):
            catalog.link_checkout(self.target, True, self.pack, self.index)
        self.assertFalse((self.target/'.agents').exists())
        self.assertEqual((self.target/'SKILLS.md').read_text(), 'User catalog\n')

    def test_existing_directory_and_broken_alias_preserved(self):
        destination = self.target/'.agents/skills'
        destination.mkdir(parents=True)
        sentinel = destination/'keep.txt'; sentinel.write_text('User skill\n')
        with self.assertRaises(ValueError):
            catalog.link_checkout(self.target, True, self.pack, self.index)
        self.assertEqual(sentinel.read_text(), 'User skill\n')
        sentinel.unlink(); destination.rmdir()
        destination.symlink_to('missing-user-pack')
        with self.assertRaises(ValueError):
            catalog.link_checkout(self.target, True, self.pack, self.index)
        self.assertEqual(str(destination.readlink()), 'missing-user-pack')
        self.assertFalse((self.target/'SKILLS.md').exists())

    def test_nested_discovery_is_not_duplicated(self):
        (self.target/'.git').mkdir()
        catalog.link_checkout(self.target, True, self.pack, self.index)
        child = self.target/'module';child.mkdir();(child/'AGENTS.md').write_text('Module rules\n')
        self.assertEqual(catalog.link_checkout(child, True, self.pack, self.index)['status'], 'inherited')
        self.assertFalse((child/'.agents').exists())

    def test_new_git_owner_can_have_own_discovery(self):
        (self.target/'.git').mkdir()
        catalog.link_checkout(self.target, True, self.pack, self.index)
        child = self.target/'separate repo';child.mkdir();(child/'.git').mkdir()
        self.assertEqual(catalog.link_checkout(child, True, self.pack, self.index)['status'], 'linked')

    def test_budget_and_unregistered_extension_fail_closed(self):
        skill = self.pack/'trident-debug/SKILL.md'
        original = skill.read_text();skill.write_text(original+'x'*catalog.MAX_SKILL)
        with self.assertRaises(ValueError):catalog.validate(self.pack, self.index)
        skill.write_text(original)
        extra = self.pack/'trident-new';extra.mkdir()
        (extra/'SKILL.md').write_text('---\nname: trident-new\ndescription: "A distinct new workflow."\n---\n\nNew original skill.\n')
        self.index.write_text(catalog.render(catalog.entries(self.pack)))
        with self.assertRaises(ValueError):catalog.validate(self.pack, self.index)

    def test_broken_index_and_missing_notice_are_detected(self):
        self.index.write_text('Stale catalog\n')
        with self.assertRaises(ValueError):catalog.validate(self.pack, self.index)
        self.index.write_text(catalog.render(catalog.entries(self.pack)))
        sources = json.loads((self.pack/'_support/sources.json').read_text())
        source = next(s for s in sources['sources'] if 'local_notice' in s['upstream_license'])
        notice = self.pack/'_support'/source['upstream_license']['local_notice']
        original = notice.read_bytes(); notice.write_bytes(original+b'changed')
        with self.assertRaises(ValueError):catalog.validate(self.pack, self.index)
        notice.unlink()
        with self.assertRaises(ValueError):catalog.validate(self.pack, self.index)

    def test_global_and_unknown_roots_rejected(self):
        for target in [Path.home(),Path('/'),self.base/'unknown']:
            with self.assertRaises(ValueError):catalog.link_checkout(target, True, self.pack, self.index)


if __name__ == '__main__':
    unittest.main(verbosity=1)
