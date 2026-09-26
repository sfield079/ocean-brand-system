import json, itertools
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
P={'blackmoss':'#0B1617','peacock':'#102426','cedar':'#1B4039','sage':'#618C7C','olive':'#6E734C','citron':'#A69856','crimson':'#EB3819','sprig':'#D5CCA0','honeydew':'#F3FBF8','white':'#FFFFFF'}
def L(h):
    c=[int(h[i:i+2],16)/255 for i in (1,3,5)]
    c=[x/12.92 if x<=0.04045 else ((x+0.055)/1.055)**2.4 for x in c]
    return 0.2126*c[0]+0.7152*c[1]+0.0722*c[2]
def cr(a,b):
    la,lb=sorted([L(P[a]),L(P[b])],reverse=True); return round((la+0.05)/(lb+0.05),2)
M={f'{a}/{b}':cr(a,b) for a,b in itertools.combinations(P,2)}
json.dump(M,open('tokens/contrast-matrix.json','w'),indent=1)
for f in ['honeydew','white','blackmoss','peacock','sage','sprig']:
    print(f, {k:cr(f,k) for k in P if k!=f})
# tokens
tok={'color':{k:{'value':v} for k,v in P.items()},
 'font':{'family':{'brand':'Stack Sans Headline','icon':'Material Symbols Outlined'},
   'weight':{'light':300,'regular':400,'medium':500,'bold':700}},
 'tracking':{'caps':'0.25em','label':'0.125em','body':'0','title':'-0.01em','display':'-0.02em','hero':'-0.04em','hero-bold':'-0.06em'},
 'radius':{'sm':'4px','md':'12px','lg':'20px'},'chamfer':{'sm':'12px','md':'24px','lg':'44px'},
 'rule':{'hairline':'1px','frame':'2px','double-gap':'4px'},
 'icon':{'style':'outlined','fill':0,'weight':400,'grade':0,'opsz':24,'cell-ratio':0.5}}
json.dump(tok,open('tokens/ocean.tokens.json','w'),indent=2)
css=':root{\n'+''.join(f'  --ocean-{k}:{v};\n' for k,v in P.items())+'''  --ocean-font:"Stack Sans Headline",system-ui,sans-serif;
  --ocean-w-light:300;--ocean-w-regular:400;--ocean-w-medium:500;--ocean-w-bold:700;
  --ocean-track-caps:.25em;--ocean-track-label:.125em;--ocean-track-title:-.01em;--ocean-track-display:-.02em;--ocean-track-hero:-.04em;
  --ocean-radius-sm:4px;--ocean-radius-md:12px;--ocean-radius-lg:20px;
  --ocean-chamfer-sm:12px;--ocean-chamfer-md:24px;--ocean-chamfer-lg:44px;
  --ocean-rule:1px;--ocean-frame:2px;
  /* default pairing: Honeydew field + Blackmoss ink */
  --ocean-field:var(--ocean-honeydew);--ocean-ink:var(--ocean-blackmoss);
}
[data-pair="honeydew-blackmoss"]{--ocean-field:var(--ocean-honeydew);--ocean-ink:var(--ocean-blackmoss)}
[data-pair="honeydew-peacock"]{--ocean-field:var(--ocean-honeydew);--ocean-ink:var(--ocean-peacock)}
[data-pair="honeydew-cedar"]{--ocean-field:var(--ocean-honeydew);--ocean-ink:var(--ocean-cedar)}
[data-pair="blackmoss-honeydew"]{--ocean-field:var(--ocean-blackmoss);--ocean-ink:var(--ocean-honeydew)}
[data-pair="peacock-honeydew"]{--ocean-field:var(--ocean-peacock);--ocean-ink:var(--ocean-honeydew)}
[data-pair="sage-honeydew"]{--ocean-field:var(--ocean-sage);--ocean-ink:var(--ocean-honeydew)}
[data-pair="sprig-peacock"]{--ocean-field:var(--ocean-sprig);--ocean-ink:var(--ocean-peacock)}
[data-pair="white-blackmoss"]{--ocean-field:var(--ocean-white);--ocean-ink:var(--ocean-blackmoss)}
.ocean-caps{text-transform:uppercase;letter-spacing:var(--ocean-track-caps);font-weight:var(--ocean-w-bold)}
.ocean-chamfer{clip-path:polygon(var(--ocean-chamfer-md) 0,100% 0,100% 100%,0 100%,0 var(--ocean-chamfer-md));border-radius:0 var(--ocean-radius-lg) var(--ocean-radius-lg) var(--ocean-radius-lg)}
.material-symbols-outlined{font-variation-settings:"FILL" 0,"wght" 400,"GRAD" 0,"opsz" 24}
'''
open('tokens/ocean.css','w').write(css)
tw='module.exports={theme:{extend:{colors:{ocean:'+json.dumps({k:v for k,v in P.items()})+'},fontFamily:{ocean:["Stack Sans Headline","system-ui","sans-serif"]},fontWeight:{light:300,normal:400,medium:500,bold:700},letterSpacing:{caps:".25em",label:".125em",title:"-.01em",display:"-.02em",hero:"-.04em"},borderRadius:{"ocean-sm":"4px","ocean-md":"12px","ocean-lg":"20px"}}}};\n'
open('tokens/tailwind.preset.js','w').write(tw)
# icons
f=TTFont('/home/user/workspace/brand/fonts/MaterialSymbolsOutlined-400-static.ttf'); lig=json.load(open('/tmp/lig.json'))
gs=f.getGlyphSet(); upm=f['head'].unitsPerEm
ICONS={'guide':['layers','dashboard','grid_guides','palette','format_color_fill','format_size','burst_mode'],
 'energy':['solar_power','battery_charging_full','ev_station','bolt','electric_meter','energy_program_saving','wind_power','power','charger','electrical_services'],
 'infrastructure':['factory','warehouse','dns','memory','developer_board','water_drop','water','construction','engineering','foundation','roofing','location_on'],
 'business':['description','contract','request_quote','payments','trending_up','schedule','calendar_month','verified','shield','handshake','groups','mail','call','language','download','arrow_forward','check','close','warning','info']}
man={}
for grp,names in ICONS.items():
    for n in names:
        if n not in lig: print('missing',n); continue
        g=lig[n]; pen=SVGPathPen(gs); gs[g].draw(pen); d=pen.getCommands()
        # font units: 960 upm? transform y flip; material glyph box 0..960, baseline so y from -? use bounds
        svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -{upm} {upm} {upm}" width="24" height="24"><path transform="scale(1,-1)" d="{d}" fill="currentColor"/></svg>'
        open(f'icons/svg/{n}.svg','w').write(svg); man.setdefault(grp,[]).append(n)
json.dump(man,open('icons/manifest.json','w'),indent=1)
print('upm',upm, sum(len(v) for v in man.values()),'icons')
