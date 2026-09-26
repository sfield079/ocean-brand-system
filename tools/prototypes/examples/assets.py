import numpy as np, re
from PIL import Image, ImageDraw
P=dict(blackmoss='0B1617',peacock='102426',cedar='1B4039',sage='618C7C',honeydew='F3FBF8',sprig='D5CCA0',olive='6E734C',citron='A69856',crimson='EB3819')
rgb=lambda k:tuple(int(P[k][i:i+2],16) for i in (0,2,4))
def wave(W,H,dot,alpha,fade_from=0.5,fade_len=0.2,cy=0.36,seed=0,scale=1.0):
    K=2; img=Image.new('RGBA',(W*K,H*K),(0,0,0,0)); d=ImageDraw.Draw(img)
    nx,nz=int(150*scale),44
    for iz in range(nz):
        z=1.0+iz*0.11
        for ix in range(nx):
            u=(ix/(nx-1))*2-1; x=u*3.2
            y=0.35*np.sin(1.6*x+0.9*z+seed)+0.22*np.sin(0.7*x-1.3*z+1.0)+0.12*np.sin(3.1*x+2.2*z)
            sx=W*K*0.5+x/z*W*K*0.36; sy=H*K*cy-(y-0.9)/z*H*K*0.42*(W/H)/(16/9)
            a=max(0,min(1,alpha*(1.25-z/6.2))); r=max(1.0,3.2*K*(W/1920)/z*1.0)
            t=sy/(H*K); f=1-min(1,max(0,(t-fade_from)/fade_len))
            if f<=0: continue
            d.ellipse([sx-r,sy-r,sx+r,sy+r],fill=rgb(dot)+(int(255*a*f),))
    return img.resize((W,H),Image.LANCZOS)
wave(1920,1080,'honeydew',0.45).save('assets/tex_deck_sage.png')
wave(1920,1080,'sage',0.55,fade_from=0.55).save('assets/tex_deck_blackmoss.png')
wave(1275,1650,'honeydew',0.45,fade_from=0.42,fade_len=0.15,cy=0.30).save('assets/tex_letter_sage.png')
# gradient map nature into peacock->sprig harmony
im=Image.open('img/nature.png').convert('L'); a=np.asarray(im).astype(float)/255
lo=np.array(rgb('peacock'),float); hi=np.array(rgb('sprig'),float)
g=(lo+(hi-lo)*a[...,None]).clip(0,255).astype(np.uint8); Image.fromarray(g).save('assets/nature_gm.jpg',quality=92)
for f in ('rooftop','worker','bess','nature'): Image.open(f'img/{f}.png').convert('RGB').save(f'assets/{f}.jpg',quality=90)
# recolored logos as svg files
for name in ('Horizontal','Vertical','Graphic'):
    s=open(f'/home/user/workspace/audit2/zip/Ocean_LOGO_{name}.svg').read()
    for c in P: open(f'assets/logo_{name.lower()}_{c}.svg','w').write(s.replace('#fff','#'+P[c]))
print('ok')
