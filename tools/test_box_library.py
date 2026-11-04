"""Integration checks for document identity, refresh and preservation."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("library", Path(__file__).with_name("box_library.py"))
lib = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lib)

class CatalogTest(unittest.TestCase):
    def test_identity_lifecycle_and_curation(self):
        with tempfile.TemporaryDirectory() as temp, contextlib.redirect_stdout(io.StringIO()):
            root = Path(temp)/"library"; root.mkdir()
            home = Path(temp)/"catalog"
            a = root/"one.txt"; a.write_text("Abstract\nUseful source for parameter estimation in natural circulation loops. "*5+"\nKeywords: inverse problems; calibration\n1 Introduction\nBody.")
            first = lib.refresh(root, home)
            self.assertEqual(first["files"], 1)
            ident = lib.records(home)[0]["id"]
            self.assertEqual(lib.records(home)[0]["abstract"]["status"], "extracted_candidate")
            snapshot = (home/"catalog.jsonl").read_bytes()
            self.assertFalse(any(lib.refresh(root, home)["changes"].values()))
            self.assertEqual(snapshot, (home/"catalog.jsonl").read_bytes())
            a.rename(root/"renamed.txt")
            report = lib.refresh(root, home)
            self.assertEqual(lib.records(home)[0]["id"], ident)
            self.assertEqual(report["changes"]["moved_or_alias_changed"][0]["before"], ["one.txt"])
            (root/"copy.txt").write_bytes((root/"renamed.txt").read_bytes())
            self.assertEqual(lib.refresh(root, home)["duplicates_extra_copies"], 1)
            (root/"ignored.txt").symlink_to(root/"copy.txt")
            self.assertEqual(lib.refresh(root, home)["files"], 2)
            (home/"annotations.json").write_text(json.dumps({ident: {"title": "Verified title", "tags": ["unique_tag"]}}))
            self.assertEqual(lib.search(home, "unique_tag", 1)[0]["title"], "Verified title")
            (root/"copy.txt").write_text("Different source bytes")
            report = lib.refresh(root, home)
            self.assertEqual(report["changes"]["changed"][0]["path"], "copy.txt")
            (root/"renamed.txt").unlink()
            lib.refresh(root, home)
            retired = next(r for r in lib.records(home) if r["id"] == ident)
            self.assertEqual(retired["status"], "not_present")
            self.assertEqual(next(r for r in lib.annotated(home) if r["id"] == ident)["curation"]["title"], "Verified title")
            self.assertIn(ident, json.loads((home/"annotations.json").read_text()))
            with self.assertRaises(ValueError):
                lib.refresh(root/"missing", home)
            (root/"copy.txt").unlink()
            with self.assertRaises(ValueError):
                lib.refresh(root, home)
    def test_unavailable_bytes_do_not_claim_a_document_changed(self):
        with tempfile.TemporaryDirectory() as temp, contextlib.redirect_stdout(io.StringIO()):
            root=Path(temp)/"library"; root.mkdir()
            home=Path(temp)/"catalog"
            path=root/"one.txt"; path.write_text("Existing source")
            lib.refresh(root,home)
            ident=lib.records(home)[0]["id"]
            with patch.object(lib,"bounded_hash",lambda p:(p,None,"timeout")):
                report=lib.refresh(root,home)
            self.assertFalse(report["changes"]["removed"])
            self.assertFalse(report["changes"]["changed"])
            old=next(r for r in lib.records(home) if r["id"]==ident)
            self.assertEqual(old["status"],"unverified_current_bytes")
            lib.refresh(root,home)
            old=next(r for r in lib.records(home) if r["id"]==ident)
            self.assertEqual(old["status"],"present")

    def test_absence_not_invented(self):
        self.assertEqual(lib.abstract_from("Book title and contents")["text"], "")
if __name__ == "__main__":
    unittest.main()

