from PIL import Image,ImageDraw,ImageFont,ImageFilter
import sys
S=sys.argv[1]; K=2; W,H=1080*K,1920*K
F="/usr/share/fonts/opentype/inter/Inter-"
def font(w,sz): return ImageFont.truetype(f"{F}{w}.otf",int(sz*K))
BG=(16,23,29); Y=(255,200,0); WH=(255,255,255); G=(37,211,102)
def base():
    im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
    glow=Image.new("L",(W,H),0); ImageDraw.Draw(glow).ellipse([W*0.05,H*0.22,W*0.95,H*0.72],fill=60)
    glow=glow.filter(ImageFilter.GaussianBlur(160*K))
    im.paste(Image.new("RGB",(W,H),(40,52,62)),mask=glow)
    return im,ImageDraw.Draw(im)
def r(v): return [x*K for x in v]
def wrap(d,text,f,maxw):
    out=[];cur=""
    for w in text.split():
        t=(cur+" "+w).strip()
        if d.textlength(t,font=f)>maxw*K and cur: out.append(cur);cur=w
        else: cur=t
    return out+[cur]
def bubble(d,x,y,w,text,fill,col,f,right=False,outline=None):
    lines=wrap(d,text,f,w-60); lh=f.size*1.3
    h=len(lines)*lh/K+44
    x0=x if not right else x-w
    d.rounded_rectangle(r([x0,y,x0+w,y+h]),radius=26*K,fill=fill,outline=outline,width=6*K if outline else 0)
    for i,l in enumerate(lines): d.text(((x0+30)*K,(y+22)*K+i*lh),l,font=f,fill=col)
    return y+h
def check(d,x,y,s,col):
    d.line(r([x,y+s*0.55,x+s*0.38,y+s*0.9,x+s,y+s*0.15]),fill=col,width=int(s*0.16*K),joint="curve")
# 1) WhatsApp
im,d=base()
d.rounded_rectangle(r([280,400,800,1400]),radius=70*K,fill=(8,10,12),outline=(70,80,90),width=8*K)
d.rounded_rectangle(r([300,420,780,1380]),radius=56*K,fill=(11,20,26))
d.rectangle(r([300,470,780,570]),fill=(31,44,52)); d.rounded_rectangle(r([300,420,780,520]),radius=56*K,fill=(31,44,52))
d.ellipse(r([325,490,385,550]),fill=(90,105,115)); d.text((405*K,494*K),"Banco",font=font("Bold",30),fill=WH)
d.text((405*K,530*K),"online",font=font("Regular",22),fill=(170,180,190))
y=bubble(d,325,610,400,"Bom dia! Saiu sua proposta de renegociação.",(32,44,52),WH,font("Medium",28))
y=bubble(d,325,y+22,410,"Assina hoje que sai o desconto.",(32,44,52),WH,font("Bold",32),outline=Y)
y=bubble(d,760,y+60,270,"Ok, assino.",(0,92,75),WH,font("Medium",28),right=True)
check(d,700,y-38,18,(83,189,235)); check(d,712,y-38,18,(83,189,235))
d.text((540*K,1300*K),"sem cópia · sem valor total",font=font("SemiBold",26),fill=(150,160,170),anchor="mm")
im.resize((1080,1920),Image.LANCZOS).save(f"{S}/img1.png")
# 2) checklist do Produtor B
im,d=base()
d.rounded_rectangle(r([150,470,930,1330]),radius=36*K,fill=(248,246,240))
d.rectangle(r([150,470,930,600]),fill=Y); d.rounded_rectangle(r([150,470,930,560]),radius=36*K,fill=Y)
d.text((540*K,535*K),"O que o Produtor B pediu",font=font("ExtraBold",44),fill=BG,anchor="mm")
items=["Proposta por escrito","Cópia do contrato","Tempo para ler antes de decidir"]
for i,t in enumerate(items):
    y=680+i*200
    d.rounded_rectangle(r([220,y,300,y+80]),radius=14*K,outline=(30,40,48),width=6*K)
    check(d,232,y+8,58,(20,150,80))
    for l_i,l in enumerate(wrap(d,t,font("Bold",42),540)): d.text((340*K,(y+10)*K+l_i*54*K),l,font=font("Bold",42),fill=(25,32,38))
    if i<2: d.line(r([220,y+150,860,y+150]),fill=(215,210,200),width=3*K)
im.resize((1080,1920),Image.LANCZOS).save(f"{S}/img2.png")
# 3) contrato com encargo escondido
im,d=base()
for o in (60,30):
    d.rounded_rectangle(r([200+o,430-o*0.6,880+o,1340-o*0.6]),radius=18*K,fill=(205,200,190) if o==60 else (225,221,212))
d.rounded_rectangle(r([200,430,880,1340]),radius=18*K,fill=(250,248,242))
d.text((240*K,470*K),"CONTRATO DE RENEGOCIAÇÃO",font=font("ExtraBold",30),fill=(40,48,56))
d.text((840*K,470*K),"pág. 7",font=font("SemiBold",26),fill=(130,130,130),anchor="ra")
import random; random.seed(4)
for i in range(17):
    y=540+i*44
    if i==9: continue
    d.rounded_rectangle(r([240,y,240+random.randint(380,600),y+14]),radius=7*K,fill=(205,205,205))
hy=540+9*44-14
d.rectangle(r([232,hy-4,850,hy+44]),fill=(255,226,90))
d.text((250*K,(hy+2)*K),"Cl. 12.4 –",font=font("Bold",28),fill=(30,30,30))
d.text((410*K,(hy+2)*K),"“taxa de estruturação”",font=font("Bold",28),fill=(30,30,30))
cx,cy,rr=567,hy+20,190
d.ellipse(r([cx-rr,cy-rr,cx+rr,cy+rr]),outline=(20,26,32),width=18*K)
d.line(r([cx+rr*0.72,cy+rr*0.72,cx+rr*1.6,cy+rr*1.6]),fill=(20,26,32),width=34*K)
im.resize((1080,1920),Image.LANCZOS).save(f"{S}/img3.png")
