"""Create the same local repository alias on another Mac; never clone/move code."""
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--papers-root', type=Path, default=Path.home() / 'projects/research/Paper_and_Presentations')
args = parser.parse_args()
hub = Path(__file__).resolve().parents[1]
target = args.papers_root.expanduser().resolve(strict=True)
if not target.is_dir():
    raise SystemExit('The repository parent must be a real directory.')
if target == hub or target in hub.parents or hub in target.parents:
    raise SystemExit('Refusing a parent/child link that could make a loop.')
alias = hub / '80_repository_links/Papers'
alias.parent.mkdir(exist_ok=True)
if alias.is_symlink():
    if alias.resolve() != target:
        raise SystemExit('Existing Papers alias points elsewhere; inspect it before changing.')
elif alias.exists():
    raise SystemExit('Existing Papers path is not a symlink; left unchanged.')
else:
    alias.symlink_to(target, target_is_directory=True)
print('Papers alias is ready:', alias, '->', target)

proposal = target / "Andres_Fierro_Dissertation_Proposal"
current = hub / "03_proposal/current"
if not (proposal / "main.tex").is_file():
    raise SystemExit("Papers ready, proposal main.tex unavailable; current unchanged.")
if current.is_symlink():
    if current.resolve() != proposal.resolve():
        raise SystemExit("Current points elsewhere; inspect it.")
elif current.exists():
    raise SystemExit("Current is a real file/folder; left unchanged.")
else:
    current.symlink_to("../80_repository_links/Papers/Andres_Fierro_Dissertation_Proposal", target_is_directory=True)
print("Current proposal alias ready:", current)

for date in ("2026-11-02", "2026-11-03"):
    legacy = hub / "03_proposal" / date / "staged"
    frozen = legacy.parent / "archive/staged"
    if not frozen.is_dir():
        continue
    if legacy.is_symlink():
        if legacy.resolve() != frozen.resolve():
            raise SystemExit("Legacy staged alias points elsewhere; inspect.")
    elif legacy.exists():
        raise SystemExit("Legacy staged is real content; inspect before archiving.")
    else:
        legacy.symlink_to("archive/staged", target_is_directory=True)
