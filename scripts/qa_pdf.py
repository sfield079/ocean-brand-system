"""Verify live text, actual font use, embedded font programs and page bounds."""
import argparse,re
from pypdf import PdfReader
import pdfplumber

def embedded_fonts(resources):
    found={}
    if resources is None:return found
    resources=resources.get_object()
    for ref in resources.get('/Font',{}).values():
        font=ref.get_object(); name=str(font.get('/BaseFont','')).lstrip('/')
        child=font.get('/DescendantFonts',[ref])[0].get_object()
        desc=child.get('/FontDescriptor');desc=desc.get_object() if desc else {}
        found[name]=any(key in desc for key in ('/FontFile','/FontFile2','/FontFile3'))
    for ref in resources.get('/XObject',{}).values():
        obj=ref.get_object()
        if obj.get('/Subtype')=='/Form':found.update(embedded_fonts(obj.get('/Resources')))
    return found

def check(path,draft=False,legal=False):
    reader=PdfReader(path);errors=[]
    with pdfplumber.open(path) as pdf:
        for n,(page,raw) in enumerate(zip(pdf.pages,reader.pages),1):
            text=page.extract_text() or ''
            if not text.strip() and not (n==len(pdf.pages) and n>2):errors.append(f'page {n}: no selectable text')  # the logo-only close is exempt
            if not draft and re.search(r'\[TBD|\[IMAGE|\[PLACEHOLDER',text,re.I):errors.append(f'page {n}: unresolved placeholder')
            fonts=embedded_fonts(raw.get('/Resources'))
            for used in {c['fontname'] for c in page.chars}:
                flat=used.replace(' ','').replace('-','')
                ok='StackSansHeadline' in flat or (legal and ('TimesNewRoman' in flat or 'LiberationSerif' in flat))
                if not ok:
                    errors.append(f'page {n}: substituted font {used}')
                if not fonts.get(used,False):errors.append(f'page {n}: font not embedded: {used}')
            for char in page.chars:
                if char['x0']<0 or char['x1']>page.width+0.5 or char['top']<0 or char['bottom']>page.height+0.5:
                    errors.append(f'page {n}: text outside page');break
            # Intersected characters at the same baseline usually indicate overprint.
            chars=[c for c in page.chars if c['text'].strip()]
            byline={}
            for c in chars:byline.setdefault(round(c['top']/2),[]).append(c)
            for line in byline.values():
                line.sort(key=lambda c:c['x0'])
                if any(a['x1']-b['x0']>max(1.5,min(a['width'],b['width'])*0.5) and b['text'] not in '.,:;’\'' for a,b in zip(line,line[1:])):
                    errors.append(f'page {n}: possible text overprint; inspect');break
    for e in errors:print('ERROR:',e)
    print(f'PDF QA: {path} / {len(reader.pages)} pages')
    print('RESULT FAIL' if errors else 'RESULT PASS (embedded approved fonts; visual review still required)')
    return not errors
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('path');p.add_argument('--draft',action='store_true');p.add_argument('--legal',action='store_true',help='legal documents: Times New Roman permitted');a=p.parse_args()
    raise SystemExit(0 if check(a.path,a.draft,a.legal) else 1)
