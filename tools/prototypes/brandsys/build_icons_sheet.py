import json, cairosvg, io
from PIL import Image, ImageDraw, ImageFont
man=json.load(open('icons/manifest.json'))
FB='/home/user/.fonts/StackSansHeadline-variable.ttf'
def f(sz,w):
    x=ImageFont.truetype(FB,sz); x.set_variation_by_axes([w]); return x
S=2; cell=96*S; cols=10
rows=sum((len(v)+cols-1)//cols for v in man.values())
W=cols*cell+160*S; H=120*S+rows*(cell+34*S)+len(man)*60*S+60*S
img=Image.new('RGB',(W,H),'#F3FBF8'); d=ImageDraw.Draw(img); ink='#0B1617'
d.text((80*S,50*S),'OCEAN ICON KIT  ·  MATERIAL SYMBOLS OUTLINED · WEIGHT 400 · FILL 0 · GRADE 0 · 24 OPTICAL',font=f(15*S,700),fill=ink)
y=110*S
for grp,names in man.items():
    d.text((80*S,y),grp.upper(),font=f(13*S,700),fill=ink); y+=36*S
    for i,n in enumerate(names):
        x=80*S+(i%cols)*cell; yy=y+(i//cols)*(cell+34*S)
        d.rectangle([x,yy,x+cell-8*S,yy+cell-8*S],outline=ink,width=2*S if grp=='guide' else S)
        svg=open(f'icons/svg/{n}.svg').read().replace('currentColor',ink).replace('width="24" height="24"',f'width="{44*S}" height="{44*S}"')
        ic=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode()))).convert('RGBA')
        img.paste(ic,(x+(cell-8*S-44*S)//2,yy+(cell-8*S-44*S)//2),ic)
        d.text((x,yy+cell-2*S),n if len(n)<17 else n[:15]+'…',font=f(9*S,400),fill=ink)
    y+=((len(names)+cols-1)//cols)*(cell+34*S)+24*S
img=img.crop((0,0,W,y+20*S)); img.save('icons/ocean-icon-kit.png'); print(img.size)
