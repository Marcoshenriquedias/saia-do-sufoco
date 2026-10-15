import json,wave,numpy as np,sys
S=sys.argv[1]; VER=sys.argv[2]
D=143.833
ws=[w for s in json.load(open(f"{S}/words.json")) for w in s['words']]
sil=json.load(open(f"{S}/sil.json"))
wf=wave.open(f"{S}/audio16.wav");a=np.frombuffer(wf.readframes(wf.getnframes()),np.int16).astype(np.float32)/32768
hop=160; env=np.sqrt(np.convolve(a**2,np.ones(hop)/hop,'same'))[::hop]
def snap(t,r=0.2):
    i0=max(0,int((t-r)*100)); i1=min(len(env)-1,int((t+r)*100))
    return (i0+int(np.argmin(env[i0:i1+1])))/100
STEP={2:[(150,151),(188,189),(202,202)],3:[(122,131),(140,149)],4:[(200,201),(220,227)]}
EXTRA=[(27,53),(75,83),(94,113),(203,219),(228,236)]
if len(sys.argv)>3: EXTRA+= [tuple(map(int,x.split('-'))) for x in sys.argv[3:]]
cutsW=[c for k in (2,3,4) for c in STEP[k]] + (EXTRA if VER=="60" else [])
rem=[(s+0.15,e-0.15) for s,e in sil if e-s>0.3]
for i,j in cutsW:
    s=snap(ws[i]['s']); e=snap(ws[j+1]['s']) if j+1<len(ws) else D
    if (i,j)==(27,53): e=31.58
    rem.append((s,e))
rem.sort(); m=[]
for s,e in rem:
    if m and s<=m[-1][1]+0.05: m[-1]=(m[-1][0],max(m[-1][1],e))
    else: m.append((s,e))
keep=[];t=0
for s,e in m:
    if s>t+0.04: keep.append((round(t,3),round(s,3)))
    t=max(t,e)
if t<D-0.05: keep.append((round(t,3),D))
cut_idx=set(k for i,j in cutsW for k in range(i,j+1))
tot=sum(e-s for s,e in keep)
print(VER,"kept",round(tot,2),"final(1.05x+2s)",round(tot/1.05+2,2),"segments",len(keep))
json.dump({"keep":keep,"cut_idx":sorted(cut_idx)},open(f"{S}/keep_{VER}.json","w"))
