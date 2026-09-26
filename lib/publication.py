"""Ocean reports and proposals (approved brand system, 26 Sep 2026).

Letter/A4 flowing PDFs with live text and embedded Stack Sans Headline. The source JSON is the
editable master. Visual reference: output/reference/examples/Ocean_Example_Report.pdf.
Profiles: brand/decisions.md P2 (proposals) and P3 (reports). Legal documents do NOT use this
module; they follow the plain Times New Roman standard in brand/BRAND-SYSTEM.md §6.
"""
import json, re
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    KeepTogether, PageBreak, Flowable, CondPageBreak)

ROOT = Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT/'tokens/ocean.tokens.json').read_text())
HEX = {k: v['value'] for k, v in TOKENS['color'].items()}
C = {k: colors.HexColor(v) for k, v in HEX.items()}
BRAND = json.loads((ROOT/'brand/color-system.json').read_text())  # legacy consumers
CAPS = float(TOKENS['tracking']['caps'].rstrip('em'))
for weight in ('Light', 'Regular', 'Medium', 'SemiBold', 'Bold'):
    pdfmetrics.registerFont(TTFont('Ocean'+weight, str(ROOT/f'brand/fonts/StackSansHeadline-{weight}.ttf')))
pdfmetrics.registerFontFamily('OceanRegular', normal='OceanRegular', bold='OceanBold', italic='OceanRegular', boldItalic='OceanBold')

# Approved interior pairings for documents (field, ink): P3 Honeydew + Blackmoss or Peacock; P2 adds Cedar.
PAIRS = {'honeydew-blackmoss': ('honeydew', 'blackmoss'), 'honeydew-peacock': ('honeydew', 'peacock'),
         'honeydew-cedar': ('honeydew', 'cedar'), 'white-blackmoss': ('white', 'blackmoss')}

def caps(c, x, y, text, size, ink, font='OceanBold', align='left'):
    """Draw tracked caps (+0.25 em), the guide's label style."""
    text = str(text).upper(); cs = CAPS*size
    w = pdfmetrics.stringWidth(text, font, size) + cs*(len(text)-1)
    if align == 'right': x -= w
    t = c.beginText(x, y); t.setFont(font, size); t.setCharSpace(cs); t.setFillColor(ink); t.textOut(text); t.setCharSpace(0); c.drawText(t)
    return w

def chamfer_path(c, x, y, w, h, ch=9, r=5, corner='br'):
    """Rounded rectangle with one 45-degree chamfer (reportlab y-up coordinates)."""
    p = c.beginPath()
    if corner == 'br':
        p.moveTo(x+r, y+h); p.lineTo(x+w-r, y+h); p.curveTo(x+w, y+h, x+w, y+h, x+w, y+h-r)
        p.lineTo(x+w, y+ch); p.lineTo(x+w-ch, y); p.lineTo(x+r, y); p.curveTo(x, y, x, y, x, y+r)
        p.lineTo(x, y+h-r); p.curveTo(x, y+h, x, y+h, x+r, y+h)
    else:  # tl
        p.moveTo(x, y+h-ch); p.lineTo(x+ch, y+h); p.lineTo(x+w-r, y+h); p.curveTo(x+w, y+h, x+w, y+h, x+w, y+h-r)
        p.lineTo(x+w, y+r); p.curveTo(x+w, y, x+w, y, x+w-r, y); p.lineTo(x+r, y); p.curveTo(x, y, x, y, x, y+r)
    p.close(); return p

def diamonds(c, x, y, n, ink, s=3.2):
    c.setFillColor(ink)
    for i in range(n):
        cx = x - i*(s*2.6); p = c.beginPath(); p.moveTo(cx, y+s); p.lineTo(cx+s, y); p.lineTo(cx, y-s); p.lineTo(cx-s, y); p.close()
        c.drawPath(p, stroke=0, fill=1)

class Caps(Flowable):
    def __init__(self, text, size, ink, space=6, font='OceanBold'):
        super().__init__(); self.text, self.size, self.ink, self.space, self.font = text, size, ink, space, font
    def wrap(self, aw, ah): return aw, self.size + self.space
    def draw(self): caps(self.canv, 0, self.space, self.text, self.size, self.ink, self.font)

class Rule(Flowable):
    def __init__(self, ink, weight=0.8, space=8):
        super().__init__(); self.ink, self.weight, self.space = ink, weight, space
    def wrap(self, aw, ah): self.w = aw; return aw, self.space
    def draw(self):
        self.canv.setStrokeColor(self.ink); self.canv.setLineWidth(self.weight); self.canv.line(0, self.space/2, self.w, self.space/2)

class Glance(Flowable):
    """Key/value tiles in chamfered containers with counting diamonds (P2 'Project at a glance')."""
    def __init__(self, items, ink, cols=3):
        super().__init__(); self.items, self.ink, self.cols = items, ink, min(cols, len(items))
    def wrap(self, aw, ah):
        self.w = aw; rows = -(-len(self.items)//self.cols); self.h = rows*56 + (rows-1)*8; return aw, self.h + 10
    def draw(self):
        c = self.canv; gap = 8; tw = (self.w - gap*(self.cols-1))/self.cols
        for i, it in enumerate(self.items):
            r, k = divmod(i, self.cols); x = k*(tw+gap); y = self.h - (r+1)*56 - r*gap + 10
            c.setStrokeColor(self.ink); c.setLineWidth(0.6); c.drawPath(chamfer_path(c, x, y, tw, 56), stroke=1, fill=0)
            diamonds(c, x+tw-10, y+44, i % 4 + 1, self.ink)
            caps(c, x+10, y+40, it['label'], 6, self.ink, 'OceanLight')
            caps(c, x+10, y+20, it['value'], 10, self.ink, 'OceanBold')

class RiskFlag(Flowable):
    """Crimson triangle marker beside a flagged risk (the only Crimson in a report)."""
    def __init__(self, title, text, ink, width_style):
        super().__init__(); self.title, self.text, self.ink, self.st = title, text, ink, width_style
    def wrap(self, aw, ah):
        self.aw = aw; self.p = Paragraph(escape(self.text), self.st); _, self.ph = self.p.wrap(aw-22, ah); return aw, self.ph + 16
    def draw(self):
        c = self.canv; h = self.ph + 16
        p = c.beginPath(); p.moveTo(0, h-12); p.lineTo(10, h-12); p.lineTo(5, h-3.5); p.close()
        c.setFillColor(C['crimson']); c.drawPath(p, stroke=0, fill=1)
        caps(c, 22, h-10, self.title, 6.4, self.ink); self.p.drawOn(c, 22, 2)

def make_styles(ink):
    base = dict(fontName='OceanRegular', textColor=ink, alignment=TA_LEFT, splitLongWords=False, allowWidows=0, allowOrphans=0)
    specs = {
      'title': dict(fontName='OceanMedium', fontSize=23, leading=25.5, spaceAfter=10),
      'subtitle': dict(fontSize=10.5, leading=15.5, spaceAfter=12),
      'section': dict(fontName='OceanMedium', fontSize=15, leading=19, spaceBefore=4, spaceAfter=8, keepWithNext=True),
      'body': dict(fontSize=10, leading=15, spaceAfter=8),
      'cell': dict(fontSize=9.4, leading=13),
      'head': dict(fontName='OceanBold', fontSize=6.6, leading=9),
      'note': dict(fontName='OceanLight', fontSize=8, leading=11, spaceBefore=6, spaceAfter=8),
      'caption': dict(fontSize=8, leading=11, spaceBefore=4, spaceAfter=10)}
    return {name: ParagraphStyle(name, **(base | opts)) for name, opts in specs.items()}

def numbered_canvas(total_holder):
    class NumberedCanvas(rl_canvas.Canvas):
        def __init__(self, *a, **k): super().__init__(*a, **k); self._saved = []
        def showPage(self): self._saved.append(dict(self.__dict__)); self._startPage()
        def save(self):
            total_holder['n'] = len(self._saved)
            for state in self._saved:
                self.__dict__.update(state); total_holder['draw'](self); super().showPage()
            super().save()
    return NumberedCanvas

from lib.notices import resolve as notice_for


def build(source, output):
    data = json.loads(Path(source).read_text(encoding='utf-8'))
    if not data.get('draft', False) and re.search(r'\[TBD|\[IMAGE|\[PLACEHOLDER', json.dumps(data), re.I):
        raise ValueError('Release document contains unresolved placeholders')
    field_name, ink_name = PAIRS[data.get('pair', 'honeydew-blackmoss')]
    FIELD, INK = C[field_name], C[ink_name]
    st = make_styles(INK); size = A4 if data.get('format') == 'A4' else letter
    LM = 40; width = size[0] - 2*LM
    label = data.get('label', 'Ocean RCS'); edition = data.get('edition', 'Ocean RCS')
    docid = data.get('id', 'OCN-DOC'); date = data.get('date', '')
    cover = data.get('cover', True)
    notice_label, notice_line = notice_for(data)
    output = Path(output); output.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(output), pagesize=size, leftMargin=LM, rightMargin=LM, topMargin=96, bottomMargin=62,
        title=data['title'], author='Ocean RCS', initialFontName='OceanRegular')
    def p(text, kind='body'): return Paragraph(escape(str(text)).replace('\n', '<br/>'), st[kind])

    story = []
    if cover: story.append(PageBreak())
    story += [Caps(label, 6.4, INK, 8), p(data['title'], 'title')]
    if data.get('subtitle'): story.append(p(data['subtitle'], 'subtitle'))
    story += [Rule(INK, 1, 14)]
    for n, section in enumerate(data['sections'], 1):
        if section.get('pageBreak'): story.append(PageBreak())
        block = []
        if section.get('title'):
            block += [Caps(f"{n:02d}  {section.get('kicker', '')}".strip(), 6, INK, 6), p(section['title'], 'section')]
        block += [p(t) for t in section.get('paragraphs', [])[:1]]
        story.append(KeepTogether(block) if block else Spacer(1, 0))
        for text in section.get('paragraphs', [])[1:]: story.append(p(text))
        if section.get('glance'): story.append(Glance(section['glance'], INK))
        for item in section.get('items', []):
            if item.get('risk'): story.append(RiskFlag(item['title'], item['text'], INK, st['body']))
            else: story.append(KeepTogether([Caps(item['title'], 6.4, INK, 5), p(item['text'])]))
        if 'table' in section:
            table = section['table']; rows = [table['headers']] + table['rows']; ncol = len(rows[0])
            if any(len(row) != ncol for row in rows): raise ValueError('Table column counts differ')
            fractions = table.get('widths', [1/ncol]*ncol)
            if len(fractions) != ncol or abs(sum(fractions)-1) > 0.001: raise ValueError('Table widths must sum to 1')
            cells = [[p(str(cell).upper() if ri == 0 else cell, 'head' if ri == 0 else 'cell') for cell in row] for ri, row in enumerate(rows)]
            t = Table(cells, colWidths=[v*width for v in fractions], repeatRows=1, hAlign='LEFT')
            t.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'), ('LEFTPADDING', (0, 0), (-1, -1), 0),
                ('RIGHTPADDING', (0, 0), (-1, -1), 8), ('TOPPADDING', (0, 0), (-1, -1), 7), ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
                ('LINEBELOW', (0, 0), (-1, 0), 1.2, INK), ('LINEBELOW', (0, 1), (-1, -1), 0.4, C['sage'])]))
            story += [CondPageBreak(80), t, Spacer(1, 10)]
        if section.get('note'): story.append(p(section['note'], 'note'))

    holder = {'n': 1}
    def draw_cover(c):
        w, h = size; hd = C['honeydew']
        c.setFillColor(C['sage']); c.rect(0, 0, w, h, stroke=0, fill=1)
        tex = ROOT/'assets/textures/tex_letter_sage.png'
        if tex.exists(): c.drawImage(str(tex), 0, 0, width=w, height=h, mask='auto')
        c.setStrokeColor(hd); c.setLineWidth(1); c.drawPath(chamfer_path(c, 24, 24, w-48, h-48, 22, 10, 'tl'), stroke=1, fill=0)
        c.drawImage(str(ROOT/'assets/logos/png/logo_vertical_honeydew.png'), 56, h-56-58, width=58*241.6/212.6, height=58, mask='auto')
        c.setFont('OceanRegular', 20); c.setFillColor(hd); c.drawRightString(w-56, h-78, data.get('year', date[-4:] or '2026'))
        caps(c, w-56, h-100, edition, 6.4, hd, 'OceanLight', 'right')
        caps(c, w-56, h-112, 'Ocean RCS', 6.4, hd, 'OceanBold', 'right')
        caps(c, 56, 300, label, 7, hd)
        c.setFont('OceanLight', 50); y = 262
        for line in str(data.get('coverTitle', data['title'])).split('\n'):
            c.drawString(52, y, line); y -= 46
        from reportlab.lib.utils import simpleSplit
        c.setFont('OceanLight', 7); c.setFillColor(hd)
        for k, ln in enumerate(reversed(simpleSplit(notice_line, 'OceanLight', 7, w-112))): c.drawString(56, 90 + k*9, ln)
        c.setStrokeColor(hd); c.line(56, 76, w-56, 76)
        x = 56
        for k, v in data.get('meta', [['Date', date or '—'], ['Status', 'Specimen' if data.get('draft') else 'Issued']]):
            x += caps(c, x, 60, k, 6, hd, 'OceanLight') + 8; x += caps(c, x, 60, v, 6, hd) + 26
    def chrome(c):
        c.saveState(); w, h = size; page = c.getPageNumber(); total = holder['n']
        if cover and page == 1: c.restoreState(); return
        # Staging header (D11): logo cell, page cell, document cell, edition cell.
        top = h - 26; hh = 34; c.setStrokeColor(INK); c.setLineWidth(1); c.rect(LM, top-hh, w-2*LM, hh, stroke=1, fill=0)
        c.drawImage(str(ROOT/f'assets/logos/png/logo_horizontal_{ink_name}.png'), LM+10, top-hh+9, width=16*510.07/142.42, height=16, mask='auto')
        x1 = LM + 92; c.line(x1, top-hh, x1, top)
        caps(c, x1+9, top-14, 'Page', 5.6, INK, 'OceanLight'); caps(c, x1+9, top-25, f'{page:02d}', 5.6, INK)
        x2 = x1 + 48; c.line(x2, top-hh, x2, top); caps(c, x2+12, top-20, label, 6, INK)
        x3 = w - LM - 160; c.line(x3, top-hh, x3, top)
        caps(c, x3+10, top-14, edition, 5.6, INK, 'OceanLight'); caps(c, x3+10, top-25, 'Ocean RCS', 5.6, INK)
        # Running footer: document ID, date, page X of Y.
        c.setLineWidth(0.6); c.line(LM, 46, w-LM, 46)
        caps(c, LM, 32, f"{docid} · {notice_label}", 5.6, INK)
        pw = caps(c, w-LM, 32, f'Page {page:02d} of {total:02d}', 5.6, INK, 'OceanBold', 'right')
        if date: caps(c, w-LM-pw-18, 32, date, 5.6, INK, 'OceanLight', 'right')
        c.restoreState()
    def background(c, _doc):
        # Runs before page content: field color, or the full cover.
        w, h = size; c.saveState()
        if cover and c.getPageNumber() == 1: draw_cover(c)
        else: c.setFillColor(FIELD); c.rect(0, 0, w, h, stroke=0, fill=1)
        c.restoreState()
    holder['draw'] = chrome
    doc.build(story, onFirstPage=background, onLaterPages=background, canvasmaker=numbered_canvas(holder))
    print(f'Saved {output}')
