import os
A = 'file:///home/user/workspace/examples/assets/'
G = 'file:///home/user/workspace/brandsys/icons/svg/'
P = dict(blackmoss='#0B1617', peacock='#102426', cedar='#1B4039', sage='#618C7C', honeydew='#F3FBF8',
         sprig='#D5CCA0', olive='#6E734C', citron='#A69856', crimson='#EB3819', white='#FFFFFF')
bm, pc, ce, sg, hd, sp, cr, wt = (P[k] for k in ['blackmoss', 'peacock', 'cedar', 'sage', 'honeydew', 'sprig', 'crimson', 'white'])
OUT = '/home/user/workspace/brandsys/render/html'; os.makedirs(OUT, exist_ok=True)
CSS = """@font-face{font-family:SSH;src:url(file:///home/user/.fonts/StackSansHeadline-variable.ttf);font-weight:200 700}
*{box-sizing:border-box;margin:0;padding:0}body{font-family:SSH;-webkit-font-smoothing:antialiased}
.cap{text-transform:uppercase;letter-spacing:.25em}.b{font-weight:700}.l{font-weight:300}.r{font-weight:400}.m{font-weight:500}
.abs{position:absolute}.dia{display:inline-block;transform:rotate(45deg)}"""

def name_of(h):
    return next(k for k, v in P.items() if v.lower() == h.lower())

def frame(w, h, color, sw=1, c=40, r=18, corner='tl'):
    o = sw / 2; x0, y0, x1, y1 = o, o, w - o, h - o
    a = lambda x, y: f'A{r},{r} 0 0 1 {x},{y}'
    if corner == 'tl':
        d = f'M{x0},{y0+c} L{x0+c},{y0} L{x1-r},{y0} {a(x1,y0+r)} L{x1},{y1-r} {a(x1-r,y1)} L{x0+r},{y1} {a(x0,y1-r)} Z'
    else:
        d = f'M{x0+r},{y0} L{x1-r},{y0} {a(x1,y0+r)} L{x1},{y1-c} L{x1-c},{y1} L{x0+r},{y1} {a(x0,y1-r)} L{x0},{y0+r} {a(x0+r,y0)} Z'
    return f'<svg width="{w}" height="{h}" style="position:absolute;left:0;top:0;overflow:visible"><path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}"/></svg>'

def photo(x, y, w, h, img, c=40, r=18, u='px'):
    return (f'<div class="abs" style="left:{x}{u};top:{y}{u};width:{w}{u};height:{h}{u};background:url({A}{img}) center/cover;'
            f'border-radius:0 {r}{u} {r}{u} {r}{u};clip-path:polygon({c}{u} 0,100% 0,100% 100%,0 100%,0 {c}{u})"></div>')

def icon(n, size, color):
    s = open(f'/home/user/workspace/brandsys/icons/svg/{n}.svg').read().replace('currentColor', color)
    return s.replace('width="24" height="24"', f'width="{size}" height="{size}" style="display:block"')

def page(name, w, h, bg, inner, u='px'):
    open(f'{OUT}/{name}.html', 'w').write(
        f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}html,body{{width:{w}{u};height:{h}{u}}}'
        f'.pg{{position:relative;width:{w}{u};height:{h}{u};background:{bg};overflow:hidden}}@page{{size:{w}{u} {h}{u};margin:0}}</style></head>'
        f'<body><div class="pg">{inner}</div></body></html>')

import segno
segno.make('https://www.oceanrcs.com/card/firstname-lastname', error='m').save('/home/user/workspace/brandsys/graphics/card-qr.svg', dark=bm, light=None, border=0)
QR='file:///home/user/workspace/brandsys/graphics/card-qr.svg'
# ============ BUSINESS CARD  3.5 x 2 in + 0.125 bleed  (pt) ============
BW, BH, BL = 252 + 18, 144 + 18, 9  # with bleed
front = f'''
<img class="abs" src="{A}tex_deck_blackmoss.png" style="left:0;top:-10pt;width:{BW}pt;height:{BH+20}pt;opacity:.95">
<div class="abs" style="left:{BL+10}pt;top:{BL+10}pt;width:{252-20}pt;height:{144-20}pt">{frame((252-20)*4/3, (144-20)*4/3, hd, 1, 14, 7)}</div>
<img class="abs" src="{A}logo_vertical_honeydew.svg" style="left:{BW/2-36.4}pt;top:{BH/2-32}pt;height:64pt">'''
page('card_front', BW, BH, bm, front, 'pt')
back = f'''
<img class="abs" src="{A}logo_horizontal_blackmoss.svg" style="left:{BL+18}pt;top:{BL+16}pt;height:16pt">
<img class="abs" src="{QR}" style="right:{BL+18}pt;top:{BL+46}pt;width:38pt;height:38pt">
<div class="abs cap" style="right:{BL+18}pt;top:{BL+16}pt;text-align:right;font-size:4.6pt;line-height:7pt;color:{bm}"><div class="l">HOUSTON, TX</div><div class="b">OCEAN RCS</div></div>
<div class="abs m" style="left:{BL+17}pt;top:{BL+56}pt;font-size:13pt;letter-spacing:-.01em;color:{bm}">Firstname Lastname</div>
<div class="abs cap b" style="left:{BL+18}pt;top:{BL+74}pt;font-size:4.8pt;color:{bm}">FOUNDER · PRINCIPAL</div>
<div class="abs" style="left:{BL+18}pt;top:{BL+92}pt;width:{252-36}pt;height:.5pt;background:{bm}"></div>
<div class="abs cap" style="left:{BL+18}pt;top:{BL+99}pt;font-size:4.6pt;line-height:8.6pt;color:{bm};display:grid;grid-template-columns:34pt 90pt 30pt 70pt">
<span class="l">MOBILE</span><span class="b">+1 000 000 0000</span><span class="l">WEB</span><span class="b">OCEANRCS.COM</span>
<span class="l">EMAIL</span><span class="b" style="text-transform:none;letter-spacing:.12em">name@oceanrcs.com</span><span class="l">LIC.</span><span class="b">TX 00000</span></div>'''
page('card_back', BW, BH, hd, back, 'pt')

# ============ SIGNAGE LANDSCAPE 1920x1080 lobby ============
sgl = f'''
{photo(0, 0, 1920, 1080, 'rooftop.jpg', 0, 0)}
<div class="abs" style="left:0;top:0;width:1920px;height:1080px;background:linear-gradient(90deg,{bm}F7 0%,{bm}E6 48%,{bm}33 80%,{bm}00 100%)"></div>
<img class="abs" src="{A}logo_horizontal_honeydew.svg" style="left:96px;top:96px;height:88px">
<div class="abs cap" style="right:96px;top:96px;text-align:right;font-size:26px;line-height:44px;color:{hd}"><div class="l">26 SEP 2026</div><div class="b">09:30</div></div>
<div class="abs cap b" style="left:96px;top:560px;font-size:30px;color:{hd}">WELCOME</div>
<div class="abs l" style="left:88px;top:604px;font-size:150px;line-height:136px;letter-spacing:-.04em;color:{hd}">Client Name<br>Leadership Team</div>
<div class="abs" style="left:96px;top:930px;width:1728px;height:2px;background:{hd}"></div>
<div class="abs cap" style="left:96px;top:958px;font-size:26px;color:{hd};display:flex;gap:72px">
 <span><span class="l">ROOM&nbsp;&nbsp;&nbsp;</span><span class="b">BOARDROOM 2</span></span><span><span class="l">HOST&nbsp;&nbsp;&nbsp;</span><span class="b">OCEAN RCS</span></span><span><span class="l">WI-FI&nbsp;&nbsp;&nbsp;</span><span class="b">OCEAN-GUEST</span></span></div>'''
page('sign_landscape', 1920, 1080, bm, sgl)

# ============ SIGNAGE PORTRAIT 1080x1920 live energy ============
def kpi(y, ic, k, v, unit, n):
    d = ''.join(f'<span class="dia" style="width:16px;height:16px;background:{hd};margin-left:14px"></span>' for _ in range(n))
    return f'''<div class="abs" style="left:72px;top:{y}px;width:936px;height:260px">{frame(936, 260, hd, 2, 48, 22, 'br')}
<div class="abs" style="left:48px;top:48px">{icon(ic, 64, hd)}</div><div class="abs" style="right:52px;top:52px">{d}</div>
<div class="abs cap l" style="left:48px;top:136px;font-size:28px;color:{hd}">{k}</div>
<div class="abs l" style="left:44px;top:168px;font-size:76px;letter-spacing:-.02em;color:{hd}">{v}<span class="cap b" style="font-size:30px;margin-left:18px">{unit}</span></div></div>'''
sgp = f'''<img class="abs" src="{A}tex_deck_blackmoss.png" style="left:-420px;top:-60px;width:1920px;height:1080px">
<img class="abs" src="{A}logo_horizontal_honeydew.svg" style="left:72px;top:84px;height:76px">
<div class="abs cap" style="right:72px;top:88px;text-align:right;font-size:24px;line-height:38px;color:{hd}"><div class="l">LIVE · UPDATED 09:30</div><div class="b">CAMDEN, NJ</div></div>
<div class="abs cap b" style="left:72px;top:560px;font-size:28px;color:{hd}">TODAY ON THIS ROOF</div>
<div class="abs m" style="left:68px;top:604px;width:940px;font-size:92px;line-height:100px;letter-spacing:-.02em;color:{hd}">Solar is covering 64% of the building load</div>
{kpi(960, 'solar_power', 'SOLAR OUTPUT', '312', 'KW', 1)}
{kpi(1250, 'battery_charging_full', 'BATTERY', '86', '%', 2)}
{kpi(1540, 'energy_program_saving', 'CO₂ AVOIDED TODAY', '1.9', 'T', 3)}
<div class="abs cap l" style="left:72px;top:1840px;font-size:22px;color:{hd}">ILLUSTRATIVE FIGURES · SAMPLE</div><img class="abs" src="{A}logo_graphic_honeydew.svg" style="right:72px;top:1812px;height:64px">'''
page('sign_portrait', 1080, 1920, bm, sgp)

# ============ EMAIL SIGNATURE (as rendered) ============
em = f'''<div style="position:absolute;left:40px;top:40px;width:560px;font-family:SSH;color:{bm}">
<div style="font-size:14px;line-height:20px">Best regards,</div>
<div style="height:24px"></div>
<table style="border-collapse:collapse"><tr>
<td style="padding-right:18px;border-right:1px solid {bm};vertical-align:top"><img src="{A}logo_vertical_blackmoss.svg" style="height:78px;display:block"></td>
<td style="padding-left:18px;vertical-align:top">
<div class="m" style="font-size:16px;line-height:20px">Firstname Lastname</div>
<div class="cap b" style="font-size:9px;line-height:18px">FOUNDER · OCEAN RCS</div>
<div style="font-size:12px;line-height:18px;margin-top:6px"><span class="cap l" style="font-size:9px">M&nbsp;&nbsp;</span>+1 000 000 0000&nbsp;&nbsp;&nbsp;<span class="cap l" style="font-size:9px">W&nbsp;&nbsp;</span>oceanrcs.com</div>
</td></tr></table>
<div style="margin-top:18px;font-size:10px;line-height:15px;color:{bm};opacity:.75;width:520px">This message may contain confidential information intended only for the addressee.</div></div>'''
page('email_signature', 640, 220, wt, em)

# ============ FORMAL: letterhead + contract p1 + signature page (Letter, pt) ============
LW, LH, M = 612, 792, 72
BODY = 'font-size:10.5pt;line-height:15.5pt'
LEGAL = '<style>.pg,.pg *{font-family:"Times New Roman","Liberation Serif",Times,serif !important}.pg .m{font-weight:700}</style>'
def formal_footer(doc, n, of, initials=False):
    ini = (f'<span style="display:inline-flex;gap:6pt;align-items:center">Initials <span style="width:30pt;height:12pt;border:.6pt solid {bm}"></span>'
           f'<span style="width:30pt;height:12pt;border:.6pt solid {bm}"></span></span>') if initials else ''
    return (f'<div class="abs r" style="left:{M}pt;top:{LH-48}pt;width:{LW-2*M}pt;font-size:7.5pt;color:{bm};display:flex;justify-content:space-between;align-items:center">'
            f'<span>{doc}</span><span>Page {n} of {of}</span>{ini or "<span>Confidential</span>"}</div>')
letter = f'''<img class="abs" src="{A}logo_horizontal_blackmoss.svg" style="left:{M}pt;top:46pt;height:28pt">
<div class="abs r" style="right:{M}pt;top:47pt;text-align:right;font-size:7.5pt;line-height:9.5pt;color:{bm}">Ocean RCS<br>Houston, Texas<br>oceanrcs.com</div>
<div class="abs r" style="left:{M}pt;top:150pt;width:{LW-2*M}pt;{BODY};color:{bm}">
26 September 2026<br><br>Client Name<br>Attn: Facilities Director<br>Street Address<br>Camden, NJ 08100<br><br>
<span class="m">Re: Proposal for rooftop solar and battery storage</span><br><br>
Dear Director,<br><br>
Thank you for the opportunity to review the Camden facility. Enclosed is our proposal for a rooftop solar array and battery storage system, together with the site findings that support it.<br><br>
The proposal remains open for sixty days. We would welcome a working session to confirm the utility interconnection path and the final roof layout before pricing is fixed.<br><br>
Sincerely,<br><br><br><br>
Firstname Lastname<br>Founder, Ocean RCS</div>
{formal_footer('Ocean RCS', 1, 1)}'''
page('f01_letter', LW, LH, wt, letter, 'pt')

BODYL = 'font-size:11.5pt;line-height:16.5pt'
cl = [('1', 'Definitions', [('1.1', '“Agreement” means this Engineering, Procurement and Construction Agreement, including its exhibits.'),
                            ('1.2', '“Project” means the rooftop solar and battery energy storage system described in Exhibit A.'),
                            ('1.3', '“Substantial Completion” means the date on which the Project is mechanically complete, energized and accepted under Section 8.')]),
      ('2', 'Scope of work', [('2.1', 'Contractor shall design, procure, construct, test and commission the Project in accordance with the Specifications, Applicable Law and Prudent Industry Practice.'),
                              ('2.2', 'Owner shall provide access to the Site, existing drawings and utility account information reasonably required by Contractor.')]),
      ('3', 'Contract price', [('3.1', 'Owner shall pay Contractor the Contract Price set out in Exhibit B, subject only to adjustment by a Change Order executed by both Parties.'),
                               ('3.2', 'Payments are due within thirty (30) days of an undisputed invoice issued under the Exhibit C milestones.')]),
      ('4', 'Schedule', [('4.1', 'Contractor shall achieve Substantial Completion within one hundred (100) days after Notice to Proceed, subject to Excusable Delay.')])]
body = ''
for n, h, subs in cl:
    body += f'<div class="m" style="font-size:11.5pt;margin:0 0 6pt">{n}.&nbsp;&nbsp;{h}</div>'
    for sn, t in subs:
        body += f'<div style="display:grid;grid-template-columns:28pt 1fr;margin-bottom:6pt"><div class="r" style="{BODYL}">{sn}</div><div class="r" style="{BODYL}">{t}</div></div>'
    body += '<div style="height:8pt"></div>'
contract = f'''<img class="abs" src="{A}logo_horizontal_blackmoss.svg" style="left:{M}pt;top:48pt;height:24pt">
<div class="abs r" style="right:{M}pt;top:54pt;font-size:7.5pt;color:{bm}">Agreement No. OCN-EPC-2026-014</div>
<div class="abs m" style="left:{M}pt;top:120pt;width:{LW-2*M}pt;text-align:center;font-size:15pt;line-height:20pt;color:{bm}">Engineering, Procurement and<br>Construction Agreement</div>
<div class="abs r" style="left:{M}pt;top:176pt;width:{LW-2*M}pt;{BODYL};color:{bm}">
This Agreement is made on 26 September 2026 between <span class="m">Client Name</span> (“Owner”) and <span class="m">Ocean RCS</span> (“Contractor”) for the Project at the Site in Camden, New Jersey. The Parties agree as follows:</div>
<div class="abs" style="left:{M}pt;top:236pt;width:{LW-2*M}pt;color:{bm}">{body}</div>
{formal_footer('OCN-EPC-2026-014 · v1.0', 1, 12, True)}'''
page('f02_contract', LW, LH, wt, LEGAL + contract, 'pt')

def sigblock(x, party, name):
    return f'''<div class="abs" style="left:{x}pt;top:210pt;width:210pt;color:{bm}">
<div class="m" style="font-size:10.5pt">{party}</div>
<div style="height:46pt;border-bottom:.6pt solid {bm}"></div><div class="r" style="font-size:8pt;margin-top:4pt">Signature</div>
<div class="r" style="{BODYL};margin-top:14pt">Name: {name}<br>Title:<br>Date:</div></div>'''
sig = f'''<img class="abs" src="{A}logo_graphic_blackmoss.svg" style="left:{M}pt;top:50pt;height:22pt"><div class="abs r" style="right:{M}pt;top:56pt;font-size:8pt;color:{bm}">Agreement No. OCN-EPC-2026-014</div>
<div class="abs r" style="left:{M}pt;top:112pt;width:{LW-2*M}pt;{BODYL};color:{bm}">
IN WITNESS WHEREOF, the Parties have executed this Agreement as of the Effective Date.</div>
<svg class="abs" style="left:{LW/2-5}pt;top:168pt" width="14" height="14"><rect x="3" y="3" width="8" height="8" transform="rotate(45 7 7)" fill="{bm}"/></svg>
{sigblock(M, 'OWNER', 'Client Name')}{sigblock(LW-M-210, 'CONTRACTOR · OCEAN RCS', 'Firstname Lastname')}
{formal_footer('OCN-EPC-2026-014 · v1.0', 12, 12)}'''
page('f03_signature', LW, LH, wt, LEGAL + sig, 'pt')

# ============ WEBSITE HOME 1440x900 ============
nav = ''.join(f'<span>{s}</span>' for s in ['SOLAR', 'STORAGE', 'EV CHARGING', 'DATA CENTERS', 'PROJECTS'])
cells = ''.join(f'<div style="width:72px;border-left:2px solid {bm};display:flex;align-items:center;justify-content:center">{icon(i, 26, bm)}</div>' for i in ['call', 'mail'])
web = f'''
<div class="abs" style="left:48px;top:32px;width:1344px;height:84px;border:2px solid {bm};display:flex;color:{bm}">
 <div style="width:250px;border-right:2px solid {bm};display:flex;align-items:center;padding-left:28px"><img src="{A}logo_horizontal_blackmoss.svg" style="height:44px"></div>
 <div class="cap b" style="flex:1;display:flex;align-items:center;gap:30px;padding-left:32px;font-size:12px;white-space:nowrap">{nav}</div>
 <div style="width:250px;border-left:2px solid {bm};display:flex;align-items:center;justify-content:center;background:{bm};color:{hd};white-space:nowrap" class="cap b"><span style="font-size:12px">REQUEST A SITE REVIEW</span></div>
 {cells}</div>
<div class="abs cap b" style="left:48px;top:176px;font-size:14px;color:{bm}">COMMERCIAL ENERGY INFRASTRUCTURE</div>
<div class="abs l" style="left:42px;top:200px;font-size:92px;line-height:88px;letter-spacing:-.04em;color:{bm}">Power that<br>pays for itself</div>
<div class="abs r" style="left:48px;top:410px;width:540px;font-size:18px;line-height:28px;color:{bm}">Ocean RCS designs, builds and operates rooftop solar, battery storage, EV charging and modular compute for commercial sites.</div>
<div class="abs" style="left:48px;top:540px;display:flex;gap:16px">
 <div class="cap b" style="background:{bm};color:{hd};font-size:13px;padding:18px 26px;clip-path:polygon(12px 0,100% 0,100% 100%,0 100%,0 12px)">REQUEST A SITE REVIEW</div>
 <div class="cap b" style="border:2px solid {bm};color:{bm};font-size:13px;padding:16px 26px;display:flex;align-items:center;gap:12px">SEE PROJECTS {icon('arrow_forward', 18, bm)}</div></div>
{photo(680, 176, 712, 440, 'rooftop.jpg', 44, 20)}<img class="abs" src="{A}logo_graphic_honeydew.svg" style="left:1308px;top:532px;height:60px">
<div class="abs" style="left:0;top:664px;width:1440px;height:236px;background:{sg}"></div>
''' + ''.join(f'''<div class="abs" style="left:{48+i*336}px;top:700px;width:312px;height:164px">{frame(312, 164, hd, 1.5, 24, 14, 'br')}
<div class="abs" style="left:24px;top:24px">{icon(ic, 32, hd)}</div>
<div class="abs cap b" style="left:24px;top:78px;font-size:12px;color:{hd}">{k}</div>
<div class="abs r" style="left:24px;top:100px;width:260px;font-size:16px;line-height:22px;color:{hd}">{t}</div></div>'''
    for i, (ic, k, t) in enumerate([('solar_power', 'SOLAR', 'Rooftop and carport arrays sized to the load'), ('battery_charging_full', 'STORAGE', 'Peak shaving and backup for critical load'),
                                    ('ev_station', 'EV CHARGING', 'Fleet and public DC fast charging'), ('dns', 'MODULAR COMPUTE', 'GPU capacity where the power already is')]))
page('web_home', 1440, 900, hd, web)

# ============ MICRO APP 1440x900 (dark) ============
side = ''.join(f'''<div style="height:56px;display:flex;align-items:center;gap:14px;padding-left:24px;{'background:'+hd+';color:'+bm if i==0 else 'color:'+hd}">
{icon(ic, 22, bm if i==0 else hd)}<span class="cap b" style="font-size:11px">{t}</span></div>''' for i, (ic, t) in enumerate(
    [('dashboard', 'OVERVIEW'), ('solar_power', 'SITES'), ('battery_charging_full', 'STORAGE'), ('ev_station', 'CHARGERS'), ('description', 'REPORTS'), ('schedule', 'ALERTS')]))
rows = [('Camden NJ', '412 kW', '86%', 'Online'), ('Houston TX', '1.2 MW', '72%', 'Online'), ('Mead OK', '640 kW', '—', 'Commissioning'), ('Colfax WI', '—', '—', 'Planning')]
tr = ''.join(f'<tr><td>{a}</td><td class="cap b" style="letter-spacing:.12em">{b}</td><td class="cap b" style="letter-spacing:.12em">{c}</td><td>{d}</td></tr>' for a, b, c, d in rows)
app = f'''<div class="abs" style="left:0;top:0;width:240px;height:900px;border-right:1px solid {hd}33">
<div style="height:104px;display:flex;align-items:center;padding-left:24px"><img src="{A}logo_horizontal_honeydew.svg" style="height:40px"></div>{side}
<img class="abs" src="{A}logo_graphic_honeydew.svg" style="left:24px;top:808px;height:44px"><div class="abs cap l" style="left:82px;top:816px;font-size:10px;line-height:15px;color:{hd}">OCEAN OPS<br><span class="b">V 1.0</span></div></div>
<div class="abs cap b" style="left:288px;top:40px;font-size:11px;color:{hd}">PORTFOLIO · LIVE</div>
<div class="abs m" style="left:286px;top:60px;font-size:36px;letter-spacing:-.01em;color:{hd}">Portfolio overview</div>
''' + ''.join(f'''<div class="abs" style="left:{288+i*282}px;top:140px;width:262px;height:150px">{frame(262, 150, sg, 1.5, 22, 12, 'br')}
<div class="abs cap l" style="left:22px;top:24px;font-size:11px;color:{hd}">{k}</div>
<div class="abs l" style="left:20px;top:48px;font-size:48px;letter-spacing:-.02em;color:{hd}">{v}</div>
<div class="abs r" style="left:22px;top:112px;font-size:13px;color:{hd}">{s}</div></div>''' for i, (k, v, s) in enumerate(
    [('GENERATION TODAY', '6.8 MWh', '+4% vs 7-day avg'), ('STORAGE STATE', '79%', 'Across 3 systems'), ('CHARGER UPTIME', '99.2%', '30-day rolling'), ('OPEN ALERTS', '1', 'Inverter comms · Camden')])) + f'''
<svg class="abs" style="left:{288+3*282+226}px;top:162px" width="16" height="15"><path d="M8 1.5 L14.5 13 L1.5 13 Z" fill="{cr}"/></svg>
<style>table.t{{border-collapse:collapse;width:1104px;color:{hd};font-size:14px}}table.t th{{text-align:left;font-weight:700;text-transform:uppercase;letter-spacing:.25em;font-size:10px;padding:0 0 12px;border-bottom:1px solid {hd}}}table.t td{{padding:16px 0;border-bottom:1px solid {hd}33}}</style>
<div class="abs cap b" style="left:288px;top:340px;font-size:11px;color:{hd}">SITES</div>
<div class="abs" style="left:288px;top:372px"><table class="t"><tr><th>SITE</th><th>CAPACITY</th><th>STORAGE</th><th>STATUS</th></tr>{tr}</table></div>
<div class="abs cap l" style="left:288px;top:850px;font-size:10px;color:{hd}">ILLUSTRATIVE DATA · SAMPLE</div>'''
page('app_dashboard', 1440, 900, bm, app)
lt = app.replace(bm, '@@F').replace(hd, pc).replace(sg, pc).replace('@@F', hd).replace('logo_horizontal_honeydew', 'logo_horizontal_peacock').replace('logo_graphic_honeydew', 'logo_graphic_peacock')
page('app_dashboard_light', 1440, 900, hd, lt)
print('ok')
