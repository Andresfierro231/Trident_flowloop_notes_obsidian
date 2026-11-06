#!/usr/bin/env python3
"""Verify original manifest digests through explicit, relocation-only routes."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def verify(root: Path) -> list[dict[str, object]]:
    root = root.resolve()
    manifest = root / "MANIFEST.sha256"
    routes = json.loads((root / "manifest_routes.json").read_text())["routes"]
    entries = [line.split(maxsplit=1) for line in manifest.read_text().splitlines() if line.strip()]
    if not entries:
        raise ValueError("reference manifest is empty")
    names = [name.lstrip("*") for _, name in entries]
    if len(set(names)) != len(names) or set(routes) != set(names):
        raise ValueError("routes must cover each original manifest entry exactly once")
    results = []
    for (expected, _), name in zip(entries, names):
        target = (root / routes[name]).resolve()
        if not target.is_relative_to(root):
            raise ValueError(f"reference route escapes reference root: {name}")
        # An existing original path cannot be bypassed to conceal a changed source.
        original = root / name
        candidates = [target] + ([original] if original.exists() and original.resolve() != target else [])
        checks = []
        for candidate in candidates:
            digest = None
            if candidate.is_file():
                with candidate.open("rb") as stream:
                    digest = hashlib.file_digest(stream, "sha256").hexdigest()
            checks.append(digest == expected)
        results.append({"original": name, "resolved": target.relative_to(root).as_posix(),
                        "expected_sha256": expected, "ok": all(checks)})
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("reference"))
    args = parser.parse_args()
    try:
        results = verify(args.root)
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(json.dumps({"ok": False, "error": str(error)}))
        return 1
    print(json.dumps({"ok": all(x["ok"] for x in results), "entries": results}, indent=2))
    return int(not all(x["ok"] for x in results))


if __name__ == "__main__":
    raise SystemExit(main())
