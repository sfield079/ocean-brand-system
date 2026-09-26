from PIL import Image, ImageDraw, ImageFont
FB='/home/user/.fonts/StackSansHeadline-variable.ttf'
def f(sz,w):
    x=ImageFont.truetype(FB,sz); x.set_variation_by_axes([w]); return x
W=3000; img=Image.new('RGB',(W,4200),'#F3FBF8'); d=ImageDraw.Draw(img); ink='#0B1617'
def put(path,x,y,w,label,border=False):
    im=Image.open(path).convert('RGB'); h=int(im.height*w/im.width); im=im.resize((w,h),Image.LANCZOS); img.paste(im,(x,y))
    if border: d.rectangle([x,y,x+w,y+h],outline='#C9D3CF',width=2)
    d.text((x,y+h+14),label,font=f(22,700),fill=ink); return y+h+60
d.text((80,60),'OCEAN BRAND SYSTEM  ·  EVERY SURFACE, ONE SET OF TOKENS',font=f(34,700),fill=ink)
y=140
a=put('render/png/web_home.png',80,y,1400,'WEBSITE · OCEANRCS.COM'); put('render/png/app_dashboard.png',1520,y,690,'MICRO-APP · DEFAULT (DARK)'); put('render/png/app_dashboard_light.png',2230,y,690,'MICRO-APP · ALTERNATIVE (LIGHT)',True)
y=a
b=put('render/png/card_front.png',80,y,700,'BUSINESS CARD · FRONT'); put('render/png/card_back.png',820,y,700,'BUSINESS CARD · BACK',True)
put('render/png/email_signature.png',1560,y,760,'EMAIL SIGNATURE',True)
y=b
c=put('render/png/sign_landscape.png',80,y,1400,'SIGNAGE · LOBBY 16:9'); put('render/png/sign_portrait.png',1520,y,500,'SIGNAGE · LIVE 9:16')
yy=y
for i,n in enumerate(['f01_letter','f02_contract','f03_signature']):
    put(f'render/png/{n}.png',2060+(i%2)*450,yy+(i//2)*660,420,['LETTER · STACK SANS','CONTRACT · TIMES NEW ROMAN','SIGNATURE PAGE · TIMES NEW ROMAN'][i],True)
y=max(c,yy+1320)
img.crop((0,0,W,y)).save('render/png/brand-system-overview.png')
