"""Fail if any instruction file names a repository file that does not exist.

Every AI tool that reads this repository follows these paths, so a missing file is an error.
brand/audit/ is a historical record and is skipped. Run: python3 scripts/check_references.py
"""
import re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
EXT = 'md|json|js|py|pdf|png|pptx|docx|css|svg|sh|mplstyle|jpg|yml|ttf|txt|woff2|html|mdc'
SKIP = ('node_modules/', 'brand/audit/', 'output/')
bad = []
files = [p for p in ROOT.rglob('*') if p.suffix in ('.md', '.mdc', '.txt') and not any(str(p.relative_to(ROOT)).startswith(s) for s in SKIP)]
names = {str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if 'node_modules' not in p.parts}
for md in files:
    for ref in set(re.findall(rf'`([A-Za-z0-9_./<>-]+\.(?:{EXT}))`', md.read_text(errors='ignore'))):
        if '<' in ref or ref.startswith('output/renders'): continue
        cand = [ROOT / ref, md.parent / ref]
        if not any(c.exists() for c in cand) and not any(n.endswith('/' + ref) or n == ref for n in names):
            bad.append(f'{md.relative_to(ROOT)}: `{ref}` does not exist')
print('\n'.join(bad) or 'PASS: every referenced file exists')
sys.exit(1 if bad else 0)
