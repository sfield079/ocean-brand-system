"""SUPERSEDED 26 Sep 2026. The examples in output/reference/examples/ are now copied from the
production pipelines (npm run starter, npm run documents). This prototype predates the deck recipes,
the logo-only close and the combined notices. Do not use it."""
raise SystemExit("Superseded: run npm run starter and npm run documents")
import os, subprocess
A = 'file:///home/user/workspace/examples/assets/'
P = dict(blackmoss='#0B1617', peacock='#102426', cedar='#1B4039', sage='#618C7C', honeydew='#F3FBF8',
         sprig='#D5CCA0', olive='#6E734C', citron='#A69856', crimson='#EB3819', white='#FFFFFF')
OUT = '/home/user/workspace/examples/html'; os.makedirs(OUT, exist_ok=True)

BASE_CSS = """
@font-face{font-family:SSH;src:url(file:///home/user/.fonts/StackSansHeadline-variable.ttf);font-weight:200 700}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:SSH;-webkit-font-smoothing:antialiased;font-kerning:normal}
.cap{text-transform:uppercase;letter-spacing:.25em}
.b{font-weight:700}.l{font-weight:300}.r{font-weight:400}.m{font-weight:500}
.abs{position:absolute}
.photo{position:absolute;overflow:hidden;background-size:cover;background-position:center}
.dia{display:inline-block;transform:rotate(45deg)}
"""

def frame_svg(w, h, color, sw=1, c=40, r=18, corner='tl', dash=None):
    """rounded rect with one 45deg chamfer; returns svg string sized w x h"""
    o = sw / 2; x0, y0, x1, y1 = o, o, w - o, h - o
    def arc(x, y): return f'A{r},{r} 0 0 1 {x},{y}'
    if corner == 'tl':
        d = (f'M{x0},{y0+c} L{x0+c},{y0} L{x1-r},{y0} {arc(x1,y0+r)} L{x1},{y1-r} {arc(x1-r,y1)} '
             f'L{x0+r},{y1} {arc(x0,y1-r)} Z')
    else:  # br chamfer
        d = (f'M{x0+r},{y0} L{x1-r},{y0} {arc(x1,y0+r)} L{x1},{y1-c} L{x1-c},{y1} L{x0+r},{y1} '
             f'{arc(x0,y1-r)} L{x0},{y0+r} {arc(x0+r,y0)} Z')
    da = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<svg width="{w}" height="{h}" style="position:absolute;left:0;top:0;overflow:visible">'
            f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}"{da}/></svg>')

def photo(x, y, w, h, img, c=40, r=18, unit='px'):
    u = unit
    return (f'<div class="photo" style="left:{x}{u};top:{y}{u};width:{w}{u};height:{h}{u};'
            f'background-image:url({A}{img});border-radius:0 {r}{u} {r}{u} {r}{u};'
            f'clip-path:polygon({c}{u} 0,100% 0,100% 100%,0 100%,0 {c}{u})"></div>')

def page(name, w, h, bg, inner, unit='px'):
    html = (f'<!doctype html><html><head><meta charset="utf-8"><style>{BASE_CSS}'
            f'html,body{{width:{w}{unit};height:{h}{unit}}}'
            f'.pg{{position:relative;width:{w}{unit};height:{h}{unit};background:{bg};overflow:hidden}}'
            f'@page{{size:{w}{unit} {h}{unit};margin:0}}</style></head>'
            f'<body><div class="pg">{inner}</div></body></html>')
    open(f'{OUT}/{name}.html', 'w').write(html)

# ---------------------------------------------------------------- DECK (1920x1080, 1pt = 2px)
DW, DH, M = 1920, 1080, 64
SECTIONS = ['SITE', 'SYSTEM', 'ECONOMICS', 'NEXT STEPS']

def deck_header(ink, field, active, num):
    nav = ''
    for i, s in enumerate(SECTIONS):
        if i: nav += f'<span style="margin:0 14px">—</span>'
        if s == active:
            nav += f'<span style="background:{ink};color:{field};padding:4px 8px 4px 12px">{s}</span>'
        else:
            nav += s
    cells = ''
    for i in range(4):
        on = SECTIONS[i] == active
        cells += (f'<div style="width:88px;height:100%;border-left:2px solid {ink};display:flex;align-items:center;'
                  f'justify-content:center;background:{ink if on else "transparent"};color:{field if on else ink}" class="b cap">'
                  f'<span style="letter-spacing:.1em;font-size:22px">0{i+1}</span></div>')
    return f'''
<div class="abs" style="left:{M}px;top:48px;width:{DW-2*M}px;height:96px;border:2px solid {ink};display:flex;color:{ink}">
  <div style="width:330px;border-right:2px solid {ink};display:flex;align-items:center;padding-left:28px">
    <img src="{A}logo_horizontal_{name_of(ink)}.svg" style="height:40px"></div>
  <div style="width:140px;border-right:2px solid {ink};display:flex;flex-direction:column;justify-content:center;padding-left:22px;font-size:21px;line-height:1.45" class="cap">
    <span class="l">PAGE</span><span class="b">{num:02d}</span></div>
  <div style="flex:1;display:flex;align-items:center;padding-left:30px;font-size:20px;white-space:nowrap" class="cap b">{nav}</div>
  <div style="width:330px;border-left:2px solid {ink};display:flex;flex-direction:column;justify-content:center;padding-left:26px;font-size:19px;line-height:1.5" class="cap">
    <span class="l">CLIENT BRIEFING</span><span class="b">OCEAN RCS</span></div>
  {cells}
</div>'''

def name_of(hexv):
    for k, v in P.items():
        if v.lower() == hexv.lower(): return k

def title_block(ink, kicker, t1, t2, lede, top=210, rule=True):
    return f'''
<div class="abs cap b" style="left:{M}px;top:{top}px;font-size:22px;color:{ink}">{kicker}</div>
<div class="abs m" style="left:{M-3}px;top:{top+38}px;font-size:70px;line-height:78px;letter-spacing:-.01em;color:{ink};width:1000px">{t1}<br>{t2}</div>
<div class="abs cap b" style="left:1110px;top:{top+38}px;height:156px;width:740px;display:flex;align-items:flex-end;font-size:21px;line-height:34px;color:{ink}"><div>{lede}</div></div>
''' + (f'<div class="abs" style="left:{M}px;top:{top+220}px;width:{DW-2*M}px;height:2px;background:{ink}"></div>' if rule else '')

def illus(ink, x, y):
    return f'<div class="abs cap l" style="left:{x}px;top:{y}px;font-size:18px;color:{ink}">ILLUSTRATIVE FIGURES · SAMPLE</div>'

# 1 cover: Sage field + Honeydew
hd, sg = P['honeydew'], P['sage']
page('d01_cover', DW, DH, sg, f'''
<img class="abs" src="{A}tex_deck_sage.png" style="left:0;top:0;width:{DW}px;height:{DH}px">
<div class="abs" style="left:48px;top:48px;width:{DW-96}px;height:{DH-96}px">{frame_svg(DW-96, DH-96, hd, 2, 44, 20)}</div>
<img class="abs" src="{A}logo_vertical_honeydew.svg" style="left:112px;top:108px;height:132px">
<div class="abs r" style="right:112px;top:104px;font-size:60px;letter-spacing:-.02em;color:{hd}">2026</div>
<div class="abs cap" style="right:112px;top:196px;text-align:right;font-size:22px;line-height:40px;color:{hd}">
  <div class="l">CLIENT BRIEFING</div><div class="l">CAMDEN, NJ</div><div class="b">OCEAN RCS</div></div>
<div class="abs cap b" style="left:112px;top:520px;font-size:24px;color:{hd}">COMMERCIAL ENERGY</div>
<div class="abs l" style="left:104px;top:556px;font-size:200px;line-height:168px;letter-spacing:-.04em;color:{hd}">Rooftop Solar<br>+ Storage</div>
<div class="abs" style="left:112px;top:958px;width:{DW-224}px;height:2px;background:{hd}"></div>
<div class="abs cap" style="left:112px;top:982px;font-size:20px;color:{hd};display:flex;gap:64px">
  <span><span class="l">PREPARED FOR&nbsp;&nbsp;&nbsp;</span><span class="b">CLIENT NAME</span></span>
  <span><span class="l">DATE&nbsp;&nbsp;&nbsp;</span><span class="b">26 SEP 2026</span></span>
  <span><span class="l">STATUS&nbsp;&nbsp;&nbsp;</span><span class="b">SAMPLE</span></span></div>
''')

# 2 agenda: Honeydew + Blackmoss (Bold display exception)
bm = P['blackmoss']
rows = [('01', 'SITE', 'What the roof and service can carry'), ('02', 'SYSTEM', 'Solar, storage and interconnection'),
        ('03', 'ECONOMICS', 'Savings, incentives and payback'), ('04', 'NEXT STEPS', 'Decisions and schedule')]
r_html = ''
for i, (n, k, t) in enumerate(rows):
    y = 470 + i * 140
    r_html += (f'<div class="abs" style="left:{M}px;top:{y}px;width:{DW-2*M}px;height:2px;background:{bm}"></div>'
               f'<div class="abs l" style="left:{M-4}px;top:{y+6}px;font-size:120px;line-height:130px;letter-spacing:-.06em;color:{bm}">{n}</div>'
               f'<div class="abs cap b" style="left:700px;top:{y+34}px;font-size:22px;color:{bm}">{k}</div>'
               f'<div class="abs r" style="left:697px;top:{y+66}px;font-size:60px;letter-spacing:-.01em;color:{bm}">{t}</div>')
r_html += f'<div class="abs" style="left:{M}px;top:{470+4*140}px;width:{DW-2*M}px;height:2px;background:{bm}"></div><div class="abs" style="left:{M}px;top:{470+4*140+8}px;width:{DW-2*M}px;height:6px;background:{bm}"></div>'
page('d02_agenda', DW, DH, hd, f'''
<img class="abs" src="{A}logo_horizontal_blackmoss.svg" style="left:{M}px;top:64px;height:40px">
<div class="abs cap" style="right:{M}px;top:62px;text-align:right;font-size:20px;line-height:34px;color:{bm}"><div class="l">CLIENT BRIEFING</div><div class="b">OCEAN RCS</div></div>
<div class="abs b" style="left:{M-10}px;top:180px;font-size:250px;line-height:230px;letter-spacing:-.06em;color:{bm}">Agenda</div>
{r_html}''')

# 3 site content: Honeydew + Peacock
pc = P['peacock']
def kv_tile(x, y, w, h, n, key, val, sub, ink):
    dias = ''.join(f'<span class="dia" style="width:12px;height:12px;background:{ink};margin-right:10px"></span>' for _ in range(n))
    return f'''<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;color:{ink}">{frame_svg(w, h, ink, 1.5, 36, 18, 'br')}
<div class="abs" style="right:34px;top:36px">{dias}</div>
<div class="abs cap l" style="left:32px;top:34px;font-size:21px">{key}</div>
<div class="abs cap b" style="left:32px;top:60px;font-size:40px;letter-spacing:.12em">{val}</div>
<div class="abs r" style="left:32px;top:{h-46}px;font-size:24px">{sub}</div></div>'''
page('d03_site', DW, DH, hd, deck_header(pc, hd, 'SITE', 3) +
     title_block(pc, '01 &nbsp;SITE', 'The Camden roof can carry', 'about 412 kW of solar',
                 'A NEW TPO ROOF, CLEAR ARRAY ZONES AND AN EXISTING 2,000 A SERVICE MAKE THIS A STRONG ROOFTOP SITE.') +
     photo(M, 480, 1080, 520, 'rooftop.jpg', 44, 20) +
     kv_tile(1190, 480, 666, 164, 1, 'ARRAY SIZE', '412 KW DC', 'About 1,030 modules after keep-outs', pc) +
     kv_tile(1190, 660, 666, 164, 2, 'USABLE ROOF', '68,400 FT²', 'Setbacks and HVAC zones removed', pc) +
     kv_tile(1190, 840, 666, 164, 3, 'SERVICE', '2,000 A · 480 V', 'Line-side tap to be confirmed with PSE&G', pc) +
     illus(pc, 1190, 1036) +
     f'<div class="abs r" style="left:{M}px;top:1016px;font-size:24px;color:{pc}">Representative image of a comparable rooftop array</div>')

# 4 statement: Blackmoss + Honeydew with one Crimson moment
cr = P['crimson']
page('d04_statement', DW, DH, bm, f'''
<img class="abs" src="{A}tex_deck_blackmoss.png" style="left:0;top:-80px;width:{DW}px;height:{DH}px;opacity:.9">
<div class="abs cap b" style="left:{M}px;top:560px;font-size:22px;color:{hd}">03 &nbsp;ECONOMICS</div>
<div class="abs l" style="left:{M-12}px;top:560px;font-size:330px;line-height:330px;letter-spacing:-.05em;color:{cr};margin-top:20px">38%</div>
<div class="abs m" style="left:860px;top:640px;width:980px;font-size:76px;line-height:84px;letter-spacing:-.02em;color:{hd}">Lower grid electricity spend from the first year of operation</div>
<div class="abs" style="left:{M}px;top:940px;width:{DW-2*M}px;height:2px;background:{hd}"></div>
<div class="abs cap" style="left:{M}px;top:966px;font-size:20px;color:{hd};display:flex;gap:64px">
 <span><span class="l">BASIS&nbsp;&nbsp;&nbsp;</span><span class="b">12-MONTH INTERVAL DATA</span></span>
 <span><span class="l">STATUS&nbsp;&nbsp;&nbsp;</span><span class="b">ILLUSTRATIVE</span></span></div>
<img class="abs" src="{A}logo_graphic_honeydew.svg" style="right:{M}px;top:64px;height:56px">
''')

# 5 chart: Honeydew + Cedar, single series in the ink, highlighted value
ce = P['cedar']
vals = [62, 66, 70, 75, 79, 84, 88, 93, 98, 104]
bars = ''
cw, gap, base, top = 118, 40, 980, 540
mx = 110
for i, v in enumerate(vals):
    h = (base - top) * v / mx; x = M + 40 + i * (cw + gap)
    hi = i == 9
    bars += (f'<div class="abs" style="left:{x}px;top:{base-h}px;width:{cw}px;height:{h}px;background:{ce};opacity:{1 if hi else .35};border-radius:6px 6px 0 0"></div>'
             f'<div class="abs cap b" style="left:{x}px;top:{base+14}px;width:{cw}px;text-align:center;font-size:20px;color:{ce}">Y{i+1:02d}</div>')
bars += (f'<div class="abs cap b" style="left:{M+40+9*(cw+gap)-30}px;top:{base-(base-top)*104/mx-60}px;width:180px;text-align:center;font-size:30px;letter-spacing:.12em;color:{ce}">$104K</div>'
         f'<div class="abs" style="left:{M}px;top:{base}px;width:{10*(cw+gap)+40}px;height:2px;background:{ce}"></div>')
page('d05_chart', DW, DH, hd, deck_header(ce, hd, 'ECONOMICS', 5) +
     title_block(ce, '03 &nbsp;ECONOMICS', 'Savings grow each year', 'as utility rates rise',
                 'ANNUAL BILL SAVINGS, YEARS 1–10, AT A 3.5% UTILITY ESCALATOR. YEAR 10 IS HIGHLIGHTED.') + bars +
     f'''<div class="abs" style="left:1700px;top:520px;width:156px;color:{ce}">
        <div class="cap l" style="font-size:20px">10-YEAR</div><div class="cap b" style="font-size:40px;letter-spacing:.1em">$819K</div>
        <div class="cap l" style="font-size:20px;margin-top:34px">PAYBACK</div><div class="cap b" style="font-size:40px;letter-spacing:.1em">6.4 YR</div></div>''' +
     illus(ce, M, 1042))

# 6 photos: Sprig + Peacock, treated beside unaltered, nature beside industry
sp = P['sprig']
page('d06_photos', DW, DH, sp, deck_header(pc, sp, 'SYSTEM', 6) +
     title_block(pc, '02 &nbsp;SYSTEM', 'Storage is inspected and', 'commissioned on site',
                 'EVERY CABINET IS TESTED, TORQUED AND LOGGED BEFORE HANDOVER.') +
     photo(M, 480, 880, 500, 'nature_gm.jpg', 44, 20) + photo(976, 480, 880, 500, 'worker.jpg', 44, 20) +
     f'<div class="abs r" style="left:{M}px;top:1004px;font-size:24px;color:{pc}">Gradient map in the Peacock + Sprig pairing</div>'
     f'<div class="abs r" style="left:976px;top:1004px;font-size:24px;color:{pc}">Unaltered photo · representative image</div>')

# 7 back cover
page('d07_back', DW, DH, bm, f'''
<img class="abs" src="{A}tex_deck_blackmoss.png" style="left:0;top:0;width:{DW}px;height:{DH}px">
<div class="abs" style="left:48px;top:48px;width:{DW-96}px;height:{DH-96}px">{frame_svg(DW-96, DH-96, hd, 2, 44, 20)}</div>
<img class="abs" src="{A}logo_vertical_honeydew.svg" style="left:{DW/2-102}px;top:384px;height:180px">
<div class="abs cap" style="left:0;width:{DW}px;top:624px;text-align:center;font-size:20px;line-height:36px;color:{hd}">
 <div class="l">HOUSTON, TEXAS</div><div class="b">OCEANRCS.COM</div></div>''')

# ---------------------------------------------------------------- REPORT (Letter, pt)
LW, LH, LM = 612, 792, 40
def rep_header(ink, field, active, num):
    nav = ''
    for i, s in enumerate(SECTIONS):
        if i: nav += '<span style="margin:0 5pt">—</span>'
        nav += (f'<span style="background:{ink};color:{field};padding:1pt 2pt 1pt 3pt">{s}</span>' if s == active else s)
    return f'''
<div class="abs" style="left:{LM}pt;top:32pt;width:{LW-2*LM}pt;height:52pt;border:1.2pt solid {ink};color:{ink}">
 <div class="abs" style="left:0;top:0;width:{LW-2*LM}pt;height:30pt;border-bottom:1.2pt solid {ink}">
  <img src="{A}logo_horizontal_{name_of(ink)}.svg" class="abs" style="left:12pt;top:8pt;height:14pt">
  <div class="abs" style="left:356pt;top:0;height:30pt;border-left:1.2pt solid {ink}"></div>
  <div class="abs cap" style="left:370pt;top:6pt;font-size:5.6pt;line-height:9pt"><div class="l">SITE FEASIBILITY REPORT</div><div class="b">OCEAN RCS</div></div></div>
 <div class="abs" style="left:58pt;top:30pt;height:21pt;border-left:1.2pt solid {ink}"></div><div class="abs cap" style="left:12pt;top:33pt;font-size:5.6pt;line-height:8pt"><span class="l">PAGE</span><br><span class="b">{num:02d}</span></div>
 <div class="abs cap b" style="left:74pt;top:38pt;font-size:5.8pt">{nav}</div>
</div>'''
def rep_footer(ink, num):
    return (f'<div class="abs" style="left:{LM}pt;top:{LH-44}pt;width:{LW-2*LM}pt;height:.8pt;background:{ink}"></div>'
            f'<div class="abs cap" style="left:{LM}pt;top:{LH-36}pt;width:{LW-2*LM}pt;font-size:5.6pt;color:{ink};display:flex;justify-content:space-between">'
            f'<span><span class="l">REPORT NO.&nbsp;&nbsp;</span><span class="b">0001</span>&nbsp;&nbsp;&nbsp;&nbsp;<span class="l">DATE&nbsp;&nbsp;</span><span class="b">26 SEP 2026</span></span>'
            f'<span><span class="l">PAGE&nbsp;&nbsp;</span><span class="b">{num:02d} OF 24</span></span></div>')
def rep_title(ink, kicker, t1, t2, lede):
    return f'''
<div class="abs cap b" style="left:{LM}pt;top:106pt;font-size:6pt;color:{ink}">{kicker}</div>
<div class="abs m" style="left:{LM-1}pt;top:118pt;font-size:23pt;line-height:25.5pt;letter-spacing:-.01em;color:{ink}">{t1}<br>{t2}</div>
<div class="abs cap b" style="left:320pt;top:118pt;width:252pt;height:47pt;display:flex;align-items:flex-end;font-size:6pt;line-height:9.6pt;color:{ink}"><div>{lede}</div></div>
<div class="abs" style="left:{LM}pt;top:180pt;width:{LW-2*LM}pt;height:.8pt;background:{ink}"></div>'''
BODY = f'font-size:9.6pt;line-height:14.9pt;text-align:justify;hyphens:none'

# R1 cover
page('r01_cover', LW, LH, sg, f'''
<img class="abs" src="{A}tex_letter_sage.png" style="left:0;top:0;width:{LW}pt;height:{LH}pt">
<div class="abs" style="left:28pt;top:28pt;width:{LW-56}pt;height:{LH-56}pt">{frame_svg((LW-56)*4/3, (LH-56)*4/3, hd, 1.3, 26, 12)}</div>
<img class="abs" src="{A}logo_vertical_honeydew.svg" style="left:56pt;top:60pt;height:64pt">
<div class="abs r" style="right:56pt;top:58pt;font-size:20pt;letter-spacing:-.02em;color:{hd}">2026</div>
<div class="abs cap" style="right:56pt;top:90pt;text-align:right;font-size:6.4pt;line-height:11pt;color:{hd}"><div class="l">REPORT NO. 0001</div><div class="l">CAMDEN, NJ</div><div class="b">OCEAN RCS</div></div>
<div class="abs cap b" style="left:56pt;top:486pt;font-size:7pt;color:{hd}">SITE FEASIBILITY REPORT</div>
<div class="abs l" style="left:52pt;top:500pt;font-size:66pt;line-height:56pt;letter-spacing:-.04em;color:{hd}">Camden<br>Rooftop Solar<br>+ Storage</div>
<div class="abs" style="left:56pt;top:700pt;width:{LW-112}pt;height:.8pt;background:{hd}"></div>
<div class="abs cap" style="left:56pt;top:710pt;font-size:6pt;color:{hd};display:flex;gap:26pt">
 <span><span class="l">PREPARED FOR&nbsp;&nbsp;</span><span class="b">CLIENT NAME</span></span><span><span class="l">DATE&nbsp;&nbsp;</span><span class="b">26 SEP 2026</span></span><span><span class="l">STATUS&nbsp;&nbsp;</span><span class="b">SAMPLE</span></span></div>''', unit='pt')

# R2 contents (Bold display exception)
toc = [('01', 'SITE', 'Roof, structure and keep-outs', '03'), ('02', 'SITE', 'Electrical service and interconnection', '07'),
       ('03', 'SYSTEM', 'Solar and storage design', '10'), ('04', 'ECONOMICS', 'Production, savings and incentives', '15'),
       ('05', 'NEXT STEPS', 'Open items, risks and schedule', '20'), ('06', 'APPENDIX', 'Data sources and assumptions', '22')]
t_html = ''
for i, (n, k, t, pgn) in enumerate(toc):
    y = 300 + i * 62
    t_html += (f'<div class="abs" style="left:{LM}pt;top:{y}pt;width:{LW-2*LM}pt;height:.8pt;background:{bm}"></div>'
               f'<div class="abs l" style="left:{LM-1}pt;top:{y+6}pt;font-size:40pt;line-height:44pt;letter-spacing:-.06em;color:{bm}">{n}</div>'
               f'<div class="abs cap b" style="left:220pt;top:{y+14}pt;font-size:6pt;color:{bm}">{k}</div>'
               f'<div class="abs r" style="left:220pt;top:{y+25}pt;font-size:17pt;letter-spacing:-.01em;color:{bm}">{t}</div>'
               f'<div class="abs cap b" style="right:{LM}pt;top:{y+30}pt;font-size:7pt;color:{bm}">{pgn}</div>')
t_html += f'<div class="abs" style="left:{LM}pt;top:{300+6*62}pt;width:{LW-2*LM}pt;height:.8pt;background:{bm}"></div><div class="abs" style="left:{LM}pt;top:{300+6*62+3}pt;width:{LW-2*LM}pt;height:2.4pt;background:{bm}"></div>'
page('r02_contents', LW, LH, hd, rep_header(bm, hd, None, 2) +
     f'<div class="abs b" style="left:{LM-4}pt;top:118pt;font-size:84pt;line-height:78pt;letter-spacing:-.06em;color:{bm}">Contents</div>' +
     t_html + rep_footer(bm, 2), unit='pt')

# R3 body page
def pt_tile(x, y, w, h, n, key, val, ink):
    dias = ''.join(f'<span class="dia" style="width:4.5pt;height:4.5pt;background:{ink};margin-left:4pt"></span>' for _ in range(n))
    return (f'<div class="abs" style="left:{x}pt;top:{y}pt;width:{w}pt;height:{h}pt;color:{ink}">{frame_svg(w*4/3, h*4/3, ink, 1, 16, 8, "br")}'
            f'<div class="abs" style="right:4pt;bottom:-11pt">{dias}</div>'
            f'<div class="abs cap l" style="left:10pt;top:10pt;font-size:6pt">{key}</div>'
            f'<div class="abs cap b" style="left:10pt;top:22pt;font-size:10pt;letter-spacing:.2em">{val}</div></div>')
page('r03_body', LW, LH, hd, rep_header(bm, hd, 'SITE', 3) +
     rep_title(bm, '01 &nbsp;SITE', 'Roof, structure', 'and keep-outs',
               'THE NEW TPO ROOF CAN CARRY A 412 KW DC ARRAY ONCE HVAC, DRAINS AND FIRE SETBACKS ARE REMOVED.') +
     f'''<div class="abs r" style="left:320pt;top:196pt;width:252pt;{BODY};color:{bm}">
The roof was surveyed in two passes: a drone orthomosaic for layout and a walk-down of curbs, drains and penetrations. Fire-code setbacks of 6 ft at the perimeter and 4 ft pathways between array blocks remove about 18% of the gross roof area.<br><br>
The remaining usable area is about 68,400 square feet across three blocks. The structural review assumes a ballasted racking load below 5 psf; the engineer of record must confirm this against the original joist drawings before layout is frozen.</div>
<div class="abs cap b" style="left:{LM}pt;top:198pt;font-size:6pt;color:{bm}">KEY FINDINGS</div>''' +
     pt_tile(LM, 214, 250, 52, 1, 'USABLE ROOF', '68,400 FT²', bm) +
     pt_tile(LM, 282, 250, 52, 2, 'ARRAY SIZE', '412 KW DC', bm) +
     pt_tile(LM, 350, 250, 52, 3, 'RACKING LOAD', '< 5 PSF', bm) +
     photo(LM, 440, LW-2*LM, 250, 'rooftop.jpg', 20, 9, 'pt') +
     f'''<div class="abs r" style="left:{LM}pt;top:698pt;font-size:8pt;color:{bm}">Figure 01 &nbsp;Roof layout context · placeholder: replace with the site survey photo before issue (evidence images must be real)</div>''' +
     rep_footer(bm, 3), unit='pt')

# R4 table page: Honeydew + Peacock, Crimson risk triangles
rows = [('Solar array', '412 kW DC', '1,030 modules', 'Confirmed layout'), ('Battery storage', '500 kW / 1,000 kWh', '2 cabinets', 'Pending utility'),
        ('Interconnection', '2,000 A line-side tap', 'PSE&G', 'Application due'), ('Roof', 'TPO, 20-yr warranty', '68,400 ft²', 'Complete'),
        ('Incentives', 'ITC 30% + adders', 'Domestic content TBC', 'Verify'), ('Schedule', '14 weeks', 'NTP to COD', 'Draft')]
tr = ''.join(
    f'<tr><td class="r">{a}</td><td class="b cap" style="letter-spacing:.12em;font-size:7.4pt">{b}</td><td class="r">{c}</td><td class="r">{d}</td></tr>' for a, b, c, d in rows)
risks = [('Utility tap approval', 'PSE&G may require a separate service; adds 6–10 weeks'),
         ('Domestic-content evidence', 'Written supplier certification needed before the adder is claimed')]
rk = ''
for i, (a, b) in enumerate(risks):
    y = 500 + i * 44
    rk += (f'<svg class="abs" style="left:{LM}pt;top:{y}pt" width="16" height="15"><circle cx="8" cy="8" r="7.5" fill="{P["white"]}" stroke="{cr}" stroke-width="0"/>'
           f'<path d="M8 2.5 L13.5 12.5 L2.5 12.5 Z" fill="{cr}"/></svg>'
           f'<div class="abs cap b" style="left:{LM+22}pt;top:{y+1}pt;font-size:6.4pt;color:{pc}">{a}</div>'
           f'<div class="abs r" style="left:{LM+22}pt;top:{y+12}pt;font-size:9.6pt;color:{pc}">{b}</div>')
page('r04_table', LW, LH, hd, rep_header(pc, hd, 'ECONOMICS', 15) +
     rep_title(pc, '04 &nbsp;ECONOMICS', 'System summary', 'and open risks',
               'SIX LINE ITEMS DEFINE THE PROJECT. TWO RISKS COULD MOVE THE SCHEDULE AND ARE FLAGGED BELOW.') +
     f'''<style>table{{border-collapse:collapse;width:{LW-2*LM}pt;color:{pc};font-size:9.4pt}}
     th{{text-align:left;font-weight:700;text-transform:uppercase;letter-spacing:.25em;font-size:6pt;padding:0 0 7pt 0;border-bottom:1.2pt solid {pc}}}
     td{{padding:9pt 0;border-bottom:.6pt solid {pc}}}</style>
     <div class="abs" style="left:{LM}pt;top:204pt"><table><tr><th>ITEM</th><th>SPECIFICATION</th><th>QUANTITY</th><th>STATUS</th></tr>{tr}</table></div>
     <div class="abs cap b" style="left:{LM}pt;top:476pt;font-size:6pt;color:{pc}">RISK FLAGS</div>''' + rk +
     f'<div class="abs cap l" style="left:{LM}pt;top:600pt;font-size:5.6pt;color:{pc}">ILLUSTRATIVE FIGURES · SAMPLE</div>' +
     rep_footer(pc, 15), unit='pt')

# ---------------------------------------------------------------- CONTRACT page 1 (White + Blackmoss)
wt = P['white']
clauses = [('1', 'DEFINITIONS', [('1.1', '"Agreement" means this Engineering, Procurement and Construction Agreement, including all attached exhibits.'),
                                  ('1.2', '"Project" means the rooftop solar photovoltaic and battery energy storage system described in Exhibit A.'),
                                  ('1.3', '"Substantial Completion" means the date on which the Project is mechanically complete, energized and accepted under Section 8.')]),
           ('2', 'SCOPE OF WORK', [('2.1', 'Contractor shall design, procure, construct, test and commission the Project in accordance with the Specifications, Applicable Law and Prudent Industry Practice.'),
                                    ('2.2', 'Owner shall provide access to the Site, existing drawings and utility account information reasonably required by Contractor.')]),
           ('3', 'CONTRACT PRICE', [('3.1', 'Owner shall pay Contractor the Contract Price set out in Exhibit B, subject only to adjustment by a Change Order executed by both Parties.'), ('3.2', 'Payments are due within thirty (30) days of an undisputed invoice issued under the Exhibit C milestones.')]),
           ('4', 'SCHEDULE', [('4.1', 'Contractor shall achieve Substantial Completion within one hundred (100) days after Notice to Proceed, subject to Excusable Delay.')]),
           ('5', 'WARRANTIES', [('5.1', 'Contractor warrants that the Work will be free from defects in workmanship for two (2) years after Substantial Completion, and shall assign all manufacturer warranties to Owner.')])]
cl = f'<div class="abs" style="left:{LM}pt;top:262pt;width:{LW-2*LM}pt;color:{bm}">'
for n, h, subs in clauses[:4]:
    cl += f'<div class="cap b" style="font-size:7pt;margin:0 0 7pt">{n}.&nbsp;&nbsp;{h}</div>'
    for sn, t in subs:
        cl += f'<div style="display:grid;grid-template-columns:30pt 1fr;margin-bottom:7pt"><div class="r" style="font-size:9.6pt;line-height:14.9pt">{sn}</div><div class="r" style="{BODY}">{t}</div></div>'
    cl += '<div style="height:10pt"></div>'
cl += '</div>'
page('c01_contract', LW, LH, wt, f'''
<img class="abs" src="{A}logo_horizontal_blackmoss.svg" style="left:{LM}pt;top:40pt;height:16pt">
<div class="abs cap" style="right:{LM}pt;top:38pt;text-align:right;font-size:6pt;line-height:10pt;color:{bm}"><div class="l">AGREEMENT NO.</div><div class="b">OCN-EPC-2026-014</div></div>
<div class="abs" style="left:{LM}pt;top:72pt;width:{LW-2*LM}pt;height:.8pt;background:{bm}"></div>
<div class="abs m" style="left:{LM-1}pt;top:96pt;font-size:23pt;line-height:25.5pt;letter-spacing:-.01em;color:{bm}">Engineering, Procurement<br>and Construction Agreement</div>
<div class="abs cap" style="left:{LM}pt;top:170pt;font-size:6pt;line-height:15pt;color:{bm};display:grid;grid-template-columns:110pt 150pt 110pt 150pt">
 <span class="l">EFFECTIVE DATE</span><span class="b">26 SEP 2026</span><span class="l">OWNER</span><span class="b">CLIENT NAME</span>
 <span class="l">CONTRACTOR</span><span class="b">OCEAN RCS</span><span class="l">SITE</span><span class="b">CAMDEN, NJ</span></div>
<div class="abs" style="left:{LM}pt;top:220pt;width:{LW-2*LM}pt;height:.8pt;background:{bm}"></div>
<div class="abs r" style="left:{LM}pt;top:232pt;width:{LW-2*LM}pt;font-size:9.6pt;line-height:14.9pt;color:{bm}">The Parties agree as follows:</div>
{cl}
<div class="abs" style="left:{LM}pt;top:{LH-54}pt;width:{LW-2*LM}pt;height:.8pt;background:{bm}"></div>
<div class="abs cap" style="left:{LM}pt;top:{LH-44}pt;font-size:5.6pt;color:{bm}"><span class="l">DOC&nbsp;&nbsp;</span><span class="b">OCN-EPC-2026-014 · V1.0 · SAMPLE</span></div>
<div class="abs cap" style="left:{LW/2-30}pt;top:{LH-44}pt;font-size:5.6pt;color:{bm}"><span class="l">PAGE&nbsp;&nbsp;</span><span class="b">01 OF 12</span></div>
<div class="abs cap" style="right:{LM}pt;top:{LH-48}pt;font-size:5.6pt;color:{bm};display:flex;gap:6pt;align-items:center"><span class="l">INITIALS</span>
 <span style="width:34pt;height:14pt;border:.8pt solid {bm}"></span><span style="width:34pt;height:14pt;border:.8pt solid {bm}"></span></div>
''', unit='pt')
print('built')
