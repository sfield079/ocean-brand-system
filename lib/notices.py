"""Distribution notices: one classification + one status (brand/notices.json, decisions.md Part 10)."""
import json
from pathlib import Path

N = json.loads((Path(__file__).resolve().parent.parent / 'brand/notices.json').read_text())


def resolve(data):
    """Return (footer_label, cover_line) for a document settings dict."""
    notice, cls, status = data.get('notice'), data.get('classification'), data.get('status')
    if notice in N['statuses']:
        status = status or notice
    elif notice:
        cls = cls or notice
    cls = cls or N['defaults']['classification']
    status = status or ('specimen' if data.get('draft') else N['defaults']['status'])
    c, s = N['classifications'][cls], N['statuses'][status]
    fill = lambda t: (t or '').replace('{recipient}', data.get('recipient', 'the named recipient')).replace('{validity}', data.get('validity', '30 days'))
    label = ' · '.join(x for x in (c['label'], s['label']) if x)
    line = ' '.join(x for x in (fill(c['line']), s['line']) if x)
    return label, line
