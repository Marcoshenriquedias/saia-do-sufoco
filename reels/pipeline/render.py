import json,sys,subprocess
S,VER,OUT=sys.argv[1],sys.argv[2],sys.argv[3]
SRC="/root/.claude/uploads/b0fd227e-bd34-5145-98d0-fa2802dc5338/89e8c350-WhatsApp_Video_2026-10-15_at_10.47.51.mp4"
SP=1.05; CARD=2.0
K=json.load(open(f"{S}/keep_{VER}.json")); keep=K["keep"]; cut=set(K["cut_idx"])
ws=[w for s in json.load(open(f"{S}/words.json")) for w in s['words']]
cum=[];c=0
for s,e in keep: cum.append(c); c+=e-s
MAIN=c/SP
def omap(t):
    for (s,e),c0 in zip(keep,cum):
        if t<s: return c0/SP
        if t<=e: return (c0+t-s)/SP
    return MAIN
# texto exibido (correções da transcrição automática)
FIX={27:"Mesma",28:"dívida",55:"produtor",56:"A",62:"WhatsApp",66:"“assina",71:"desconto”",86:"B",96:"planilha",
     127:"B",177:"produtor",178:"A",183:"B",205:"por",206:"",223:"WhatsApp",238:"ANÁLISE"}
END={10,15,20,26,30,37,53,71,74,83,88,93,113,121,131,139,149,161,175,180,187,197,199,201,202,219,227,236,239,253}
Q={26,236}
words=[]
for i,w in enumerate(ws):
    if i in cut: continue
    t=FIX.get(i,w['w'].strip())
    if t=="": continue
    words.append(dict(i=i,t=t,s=omap(w['s']),e=omap(w['e'])))
import os
AL=f"{S}/align_{VER}.json"
if os.path.exists(AL):
    al={int(k):v for k,v in json.load(open(AL)).items()}
    for w in words:
        if w['i'] in al: w['s'],w['e']=al[w['i']]
# capitalização e pontuação
prev_end=True
for w in words:
    if prev_end: w['t']=w['t'][0].upper()+w['t'][1:] if not w['t'].startswith("“") else "“"+w['t'][1].upper()+w['t'][2:]
    if w['i'] in END: w['t']+= "?" if w['i'] in Q else "."
    prev_end=w['i'] in END
# cortes de bloco: até 4 palavras / 24 caracteres, quebra em fim de frase e em cortes de conteúdo
chunks=[];cur=[]
for k,w in enumerate(words):
    if cur and (len(cur)>=4 or len(" ".join(x['t'] for x in cur+[w]))>24 or w['i']!=cur[-1]['i']+1 and not (w['i']==207)):
        chunks.append(cur);cur=[]
    cur.append(w)
    if w['i'] in END: chunks.append(cur);cur=[]
if cur: chunks.append(cur)
def ts(t):
    t=max(0,t);h=int(t//3600);m=int(t%3600//60);s=t%60
    return f"{h}:{m:02d}:{s:05.2f}"
ev=[]
YEL="&H0000C8FF&"  # amarelo (BGR)
for n,ch in enumerate(chunks):
    nxt=chunks[n+1][0]['s'] if n+1<len(chunks) else MAIN
    end=min(nxt, ch[-1]['e']+0.6)
    for j,w in enumerate(ch):
        a=w['s'] if j else ch[0]['s']
        b=ch[j+1]['s'] if j+1<len(ch) else end
        if b-a<0.02: continue
        txt=" ".join((f"{{\\c{YEL}}}{x['t']}{{\\c&H00FFFFFF&}}" if x is w else x['t']) for x in ch)
        ev.append(f"Dialogue: 1,{ts(a)},{ts(b)},Cap,,0,0,0,,{txt}")
# textos de tela (um de cada vez), ancorados no índice da palavra falada
CUES=[(0,"MESMA PROPOSTA.\\N{\\c&H0000C8FF&}DOIS DESFECHOS."),
      (54,"PRODUTOR A\\N{\\fs50}assinou pelo WhatsApp, sem ler"),
      (84,"PRODUTOR B\\N{\\fs50}pediu tudo por escrito"),
      (132,"O DETALHE\\N{\\c&H0000C8FF&}QUE MUDA TUDO"),
      (154,"{\\c&H0000C8FF&}ENCARGO ESCONDIDO\\N{\\c&H00FFFFFF&\\fs50}outra página, outro nome"),
      (190,"NÃO FOI SORTE.\\N{\\c&H0000C8FF&}FOI LEITURA."),
      (237,"Comente {\\c&H0000C8FF&}ANÁLISE")]
widx={w['i']:w for w in words}
cues=[(widx[i]['s'],t) for i,t in CUES if i in widx]
for n,(a,t) in enumerate(cues):
    b=cues[n+1][0] if n+1<len(cues) else MAIN
    ev.append(f"Dialogue: 2,{ts(a)},{ts(b)},Top,,0,0,0,,{{\\fad(120,80)}}{t}")
# rótulo de conformidade
lab_end=widx[237]['s'] if 237 in widx else MAIN
ev.append(f"Dialogue: 3,{ts(0)},{ts(lab_end)},Label,,0,0,0,,Exemplo ilustrativo")
# quadro final
ev.append(f"Dialogue: 4,{ts(MAIN)},{ts(MAIN+CARD)},Card,,0,0,0,,{{\\fad(150,0)\\pos(540,820)}}Comente")
ev.append(f"Dialogue: 4,{ts(MAIN)},{ts(MAIN+CARD)},CardBig,,0,0,0,,{{\\fad(150,0)\\pos(540,1000)}}ANÁLISE")
ev.append(f"Dialogue: 4,{ts(MAIN)},{ts(MAIN+CARD)},Card,,0,0,0,,{{\\fad(150,0)\\pos(540,1180)\\fs56\\c&H00DDDDDD&}}@advogado_divergente_")
ass=f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Inter ExtraBold,74,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,0,0,0,0,100,100,0,0,1,6,2,2,70,70,330,1
Style: Top,Inter ExtraBold,66,&H00FFFFFF,&H00FFFFFF,&H40201A12,&H40201A12,0,0,0,0,100,100,0,0,3,18,0,8,80,80,120,1
Style: Label,Inter SemiBold,34,&H00FFFFFF,&H00FFFFFF,&H50000000,&H50000000,0,0,0,0,100,100,1,0,3,8,0,7,40,40,40,1
Style: Card,Inter ExtraBold,80,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,5,40,40,0,1
Style: CardBig,Inter ExtraBold,150,&H0000C8FF,&H0000C8FF,&H00000000,&H00000000,0,0,0,0,100,100,2,0,1,0,0,5,40,40,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""+"\n".join(ev)+"\n"
open(f"{S}/subs_{VER}.ass","w").write(ass)
open(f"{S}/captions_{VER}.txt","w").write("\n".join(f"{ts(c[0]['s'])}  "+" ".join(x['t'] for x in c) for c in chunks))
# filtergraph
fg=[]
for n,(s,e) in enumerate(keep):
    d=e-s
    fg.append(f"[0:v]trim={s}:{e},setpts=PTS-STARTPTS[v{n}];[0:a]atrim={s}:{e},asetpts=PTS-STARTPTS,afade=t=in:d=0.01,afade=t=out:st={max(0,d-0.012):.3f}:d=0.012[a{n}]")
fg.append("".join(f"[v{n}][a{n}]" for n in range(len(keep)))+f"concat=n={len(keep)}:v=1:a=1[cv][ca]")
fg.append(f"[cv]setpts=PTS/{SP},fps=24,scale=1080:1920:flags=lanczos,unsharp=5:5:0.6,setsar=1,format=yuv420p[mv]")
fg.append(f"[ca]atempo={SP},highpass=f=70,aresample=48000[ma]")
fg.append(f"color=c=0x121A20:s=1080x1920:r=24:d={CARD},format=yuv420p,setsar=1[cardv];anullsrc=r=48000:cl=mono,atrim=0:{CARD}[carda]")
fg.append("[mv][ma][cardv][carda]concat=n=2:v=1:a=1[fv][fa0]")
fg.append(f"[fv]ass={S}/subs_{VER}.ass[outv];[fa0]loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[outa]")
open(f"{S}/fg_{VER}.txt","w").write(";\n".join(fg))
cmd=["ffmpeg","-v","error","-y","-i",SRC,"-filter_complex_script",f"{S}/fg_{VER}.txt","-map","[outv]","-map","[outa]",
     "-c:v","libx264","-profile:v","high","-preset","slow","-crf","19","-r","24","-pix_fmt","yuv420p",
     "-c:a","aac","-b:a","192k","-ac","2","-movflags","+faststart",OUT]
subprocess.run(cmd,check=True)
print("main",round(MAIN,2),"total",round(MAIN+CARD,2))
