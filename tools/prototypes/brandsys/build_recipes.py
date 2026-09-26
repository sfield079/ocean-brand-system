from PIL import Image, ImageDraw, ImageFont
FB='/home/user/.fonts/StackSansHeadline-variable.ttf'
def f(sz,w):
    x=ImageFont.truetype(FB,sz); x.set_variation_by_axes([w]); return x
P=dict(BM='#0B1617',PC='#102426',CE='#1B4039',SG='#618C7C',HD='#F3FBF8',SP='#D5CCA0',CR='#EB3819',WT='#FFFFFF')
pair={'cover':('SG','HD'),'close':('SG','HD'),'agenda':('HD','BM'),'site':('HD','PC'),'system':('SP','PC'),'econ':('HD','CE'),'stmt':('BM','HD'),'next':('HD','CE'),
      'div_site':('PC','HD'),'div_system':('SP','PC'),'div_econ':('CE','HD'),'appx':('WT','BM')}
R={'5 SLIDES · BRIEFING':[('cover','Cover'),('site','Situation'),('system','Solution · photo'),('stmt','Key number'),('close','Close')],
 '10 SLIDES · CLIENT PRESENTATION':[('cover','Cover'),('agenda','Agenda'),('site','Site'),('site','Site data'),('system','System · photo'),('system','System detail'),('econ','Economics chart'),('stmt','Key number'),('next','Next steps'),('close','Close')],
 '15 SLIDES · INVESTOR / FULL PROPOSAL':[('cover','Cover'),('agenda','Agenda'),('div_site','01 Site'),('site','Site'),('site','Site data'),('div_system','02 System'),('system','Photo'),('system','Detail'),('system','Schedule'),('div_econ','03 Economics'),('econ','Chart'),('econ','Table'),('stmt','Key number'),('next','Next steps'),('close','Close')],
}
S=2; tw,th=150*S,84*S; gap=12*S; L=60*S
W=L*2+15*(tw+gap); H=0
img=Image.new('RGB',(W,200*S+len(R)*(th+120*S)+300*S),P['HD']); d=ImageDraw.Draw(img); ink=P['BM']
d.text((L,40*S),'OCEAN DECK RECIPES  ·  SAME SYSTEM, ANY LENGTH',font=f(18*S,700),fill=ink)
d.text((L,72*S),'Cover and close bookend every deck. One Crimson key-number slide per deck. Agenda from 8 slides; section dividers from 12. 2–4 content pairings, one per section (bookends, agenda, dividers and the key number do not count).',font=f(13*S,400),fill=ink)
y=130*S
for title,seq in R.items():
    d.text((L,y),title,font=f(12*S,700),fill=ink); y+=28*S
    for i,(k,lab) in enumerate(seq):
        x=L+i*(tw+gap); fld,ik=pair[k]
        d.rounded_rectangle([x,y,x+tw,y+th],radius=6*S,fill=P[fld],outline='#C9D3CF' if fld in('HD','WT') else None,width=S)
        # mini content marks
        d.rectangle([x+10*S,y+10*S,x+44*S,y+13*S],fill=P[ik])
        if k in('cover','close'): d.text((x+10*S,y+40*S),'Title',font=f(22*S,300),fill=P[ik])
        elif k.startswith('div'): d.text((x+10*S,y+30*S),lab[:2],font=f(34*S,300),fill=P[ik])
        elif k=='stmt': d.text((x+10*S,y+30*S),'38%',font=f(30*S,300),fill=P['CR'])
        else:
            d.rectangle([x+10*S,y+22*S,x+90*S,y+28*S],fill=P[ik])
            if 'photo' in lab.lower() or lab=='Photo': d.rounded_rectangle([x+10*S,y+38*S,x+tw-10*S,y+th-10*S],radius=4*S,fill='#8A9A8F')
            elif 'chart' in lab.lower() or lab=='Chart':
                for b in range(6): hh=(10+b*5)*S; d.rectangle([x+(12+b*20)*S,y+th-10*S-hh,x+(26+b*20)*S,y+th-10*S],fill=P[ik])
            else:
                for r in range(4): d.rectangle([x+10*S,y+(40+r*9)*S,x+tw-(20+r*8)*S,y+(42+r*9)*S],fill=P[ik])
        d.text((x,y+th+8*S),lab,font=f(10*S,400),fill=ink)
    y+=th+60*S
d.text((L,y),'PAIRINGS USED',font=f(12*S,700),fill=ink); y+=28*S
legend=[('SG','HD','Sage + Honeydew · cover/close'),('HD','BM','Honeydew + Blackmoss · agenda'),('HD','PC','Honeydew + Peacock · section 1'),('SP','PC','Sprig + Peacock · section 2'),('HD','CE','Honeydew + Cedar · section 3'),('BM','HD','Blackmoss + Honeydew · key number (Crimson)'),('PC','HD','Peacock + Honeydew · divider 01'),('SP','PC','Sprig + Peacock · divider 02'),('CE','HD','Cedar + Honeydew · divider 03')]
for i,(a,b,t) in enumerate(legend):
    x=L+(i%3)*(760*S//2); yy=y+(i//3)*36*S
    d.rounded_rectangle([x,yy,x+26*S,yy+22*S],radius=4*S,fill=P[a],outline='#C9D3CF',width=S); d.rectangle([x+6*S,yy+9*S,x+20*S,yy+13*S],fill=P[b])
    d.text((x+36*S,yy+3*S),t,font=f(11*S,400),fill=ink)
img=img.crop((0,0,W,y+130*S)); img.save('render/png/deck_recipes.png'); print(img.size)
