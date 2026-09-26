"""Distribution notices: one classification + one status (brand/notices.json, decisions.md Part 10)."""
import json
from pathlib import Path

N = json.loads((Path(__file__).resolve().parent.parent / 'brand/notices.json').read_text())


STRICT = ['final', 'draft', 'superseded', 'specimen', 'do-not-use']  # later = stricter


def check_release(data):
    """Release rules for a document or deck settings dict (decisions.md Part 10)."""
    cls = data.get('classification') or (data.get('notice') if data.get('notice') in N['classifications'] else None)
    if data.get('draft'):
        return
    if cls == 'proposal':
        missing = [k for k in ('recipient', 'validity') if not data.get(k) or data[k] in ('Client name', 'the named recipient')]
        if missing:
            raise ValueError(f'A released proposal must name its {" and ".join(missing)} (decisions.md Part 10)')
    if (data.get('status') or 'final') in ('specimen',):
        raise ValueError('A design specimen cannot be released; set status to final, draft or do-not-use')


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
    for sec in data.get('sections', []):
        if sec.get('status') and sec['status'] not in N['statuses']:
            raise ValueError(f"Unknown section status {sec['status']}")
    label = ' · '.join(x for x in (c['label'], s['label']) if x)
    line = ' '.join(x for x in (fill(c['line']), s['line']) if x)
    return label, line


def label_with(data, status):
    """Footer label for one page that carries a stricter status than its document."""
    return resolve({**data, 'status': status})[0]
