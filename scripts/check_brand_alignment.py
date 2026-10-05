"""Detect color drift and competing active instruction sources in this checkout."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
def check():
    errors = []
    tokens = json.loads((ROOT / 'tokens/ocean.tokens.json').read_text())
    legacy = json.loads((ROOT / 'brand/color-system.json').read_text())
    for name, item in tokens['color'].items():
        if legacy['colors'].get(name, '').lstrip('#').lower() != item['value'].lstrip('#').lower():
            errors.append(f'Color drift: {name}')
    kit = json.loads((ROOT / 'web-kit/ocean.tokens.json').read_text())
    if kit != tokens:
        errors.append('web-kit token copy differs from canonical tokens')
    for name in ('brand/DESIGN-SYSTEM.md', 'brand/REFERENCE-NOTES.md', 'brand/ocean-color-system.md'):
        if 'superseded' not in (ROOT / name).read_text(encoding='utf-8').lower():
            errors.append(f'Historical rules lack superseded notice: {name}')
    required = ('AGENTS.md', 'brand/REPO-MIGRATION.md', 'brand/LOCAL-ALIGNMENT.md',
                'brand/PRODUCT-KIT.md', 'brand/PROFORMA-KIT.md')
    errors += [f'Missing controlling file: {name}' for name in required if not (ROOT / name).is_file()]
    return errors
if __name__ == '__main__':
    errors = check()
    print('\n'.join(errors) if errors else 'PASS: brand sources and token copies align')
    raise SystemExit(bool(errors))
