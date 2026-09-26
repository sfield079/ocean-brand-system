"""Flowing Ocean PDF documents with live text and embedded brand fonts.

The source JSON is the editable master. This is not a rasterized slide export.
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
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
    TableStyle, KeepTogether, PageBreak, HRFlowable)

ROOT = Path(__file__).resolve().parent.parent
BRAND = json.loads((ROOT/'brand/color-system.json').read_text())
C = {k: colors.HexColor('#'+v) for k,v in {**BRAND['colors'], **BRAND['tints']}.items()}
for weight in ('Regular','Medium','SemiBold','Bold'):
    pdfmetrics.registerFont(TTFont('Ocean'+weight, str(ROOT/f'brand/fonts/StackSansHeadline-{weight}.ttf')))
pdfmetrics.registerFontFamily('OceanRegular', normal='OceanRegular', bold='OceanBold', italic='OceanRegular', boldItalic='OceanBold')

def make_styles():
    base=dict(fontName='OceanRegular',textColor=C['blackmoss'],alignment=TA_LEFT,
              splitLongWords=False,allowWidows=0,allowOrphans=0)
    specs={
      'title':dict(fontName='OceanBold',fontSize=30,leading=33,spaceAfter=15),
      'subtitle':dict(fontSize=12,leading=17,spaceAfter=16),
      'section':dict(fontName='OceanBold',fontSize=18,leading=22,spaceBefore=15,spaceAfter=9,keepWithNext=True),
      'body':dict(fontSize=11,leading=15.5,spaceAfter=9),
      'label':dict(fontName='OceanSemiBold',fontSize=9,leading=12,spaceAfter=8),
      'cell':dict(fontSize=10,leading=14),
      'head':dict(fontName='OceanSemiBold',fontSize=10,leading=14),
      'note':dict(fontSize=9,leading=12,spaceBefore=8,spaceAfter=8)}
    return {name:ParagraphStyle(name,**(base|opts)) for name,opts in specs.items()}

def build(source, output):
    data=json.loads(Path(source).read_text(encoding='utf-8'))
    if not data.get('draft',False) and re.search(r'\[TBD|\[IMAGE|\[PLACEHOLDER',json.dumps(data),re.I):
        raise ValueError('Release document contains unresolved placeholders')
    st=make_styles(); size=A4 if data.get('format')=='A4' else letter
    margin=39.6; width=size[0]-2*margin
    output=Path(output); output.parent.mkdir(parents=True,exist_ok=True)
    doc=SimpleDocTemplate(str(output),pagesize=size,leftMargin=margin,rightMargin=margin,
       topMargin=82,bottomMargin=58,title=data['title'],author='Ocean RCS',
       initialFontName='OceanRegular')
    story=[]
    def p(text,kind='body'):
        return Paragraph(escape(str(text)).replace('\n','<br/>'),st[kind])
    story += [p(data.get('label','Ocean RCS'),'label'),p(data['title'],'title')]
    if data.get('subtitle'): story.append(p(data['subtitle'],'subtitle'))
    story += [HRFlowable(width='100%',thickness=0.8,color=C['sage']),Spacer(1,9)]
    for section in data['sections']:
        if section.get('pageBreak'): story.append(PageBreak())
        if section.get('title'): story.append(p(section['title'],'section'))
        for text in section.get('paragraphs',[]): story.append(p(text))
        for item in section.get('items',[]):
            story.append(KeepTogether([p(item['title'],'label'),p(item['text'])]))
        if 'table' in section:
            table=section['table']; rows=[table['headers']]+table['rows']; n=len(rows[0])
            if any(len(row)!=n for row in rows): raise ValueError('Table column counts differ')
            fractions=table.get('widths',[1/n]*n)
            if len(fractions)!=n or abs(sum(fractions)-1)>0.001: raise ValueError('Table widths must sum to 1')
            cells=[[p(cell,'head' if ri==0 else 'cell') for cell in row] for ri,row in enumerate(rows)]
            t=Table(cells,colWidths=[v*width for v in fractions],repeatRows=1,hAlign='LEFT')
            t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),
                ('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),9),
                ('BOTTOMPADDING',(0,0),(-1,-1),9),('BACKGROUND',(0,0),(-1,0),C['mist']),
                ('LINEBELOW',(0,0),(-1,0),0.8,C['sage']),('LINEBELOW',(0,1),(-1,-1),0.4,C['fog'])]))
            story += [t,Spacer(1,9)]
        if section.get('note'): story.append(p(section['note'],'note'))
    def chrome(canvas,doc):
        canvas.saveState(); w,h=size
        canvas.drawImage(str(ROOT/'assets/logos/Ocean_LOGO_Horizontal.png'),margin,h-49,
                         width=83,height=22,preserveAspectRatio=True,mask='auto')
        canvas.setFont('OceanRegular',9); canvas.setFillColor(C['cedar'])
        canvas.drawRightString(w-margin,h-40,data.get('edition','Ocean RCS'))
        canvas.setStrokeColor(C['fog']);canvas.setLineWidth(0.6)
        canvas.line(margin,43,w-margin,43)
        canvas.drawString(margin,29,'Ocean RCS' + ('   Design specimen' if data.get('draft') else ''))
        canvas.drawRightString(w-margin,29,f'{doc.page:02d}')
        canvas.restoreState()
    doc.build(story,onFirstPage=chrome,onLaterPages=chrome)
    print(f'Saved {output}')
