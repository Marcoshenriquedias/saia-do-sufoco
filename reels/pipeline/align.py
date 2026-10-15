import json,sys,difflib,unicodedata,re
S,VER=sys.argv[1],sys.argv[2]
def norm(x):
    x=unicodedata.normalize('NFD',x.lower()); x=''.join(c for c in x if unicodedata.category(c)!='Mn')
    return re.sub(r'[^a-z0-9]','',x)
NUM={"5":"cinco","3":"tres"}
ws=[w for s in json.load(open(f"{S}/words.json")) for w in s['words']]
cut=set(json.load(open(f"{S}/keep_{VER}.json"))["cut_idx"])
exp=[(i,norm(w['w'])) for i,w in enumerate(ws) if i not in cut]
out=[w for s in json.load(open(f"{S}/out_words.json")) for w in s['words']]
ot=[NUM.get(norm(w['w']),norm(w['w'])) for w in out]
sm=difflib.SequenceMatcher(None,[e for _,e in exp],ot,autojunk=False)
al={}
for a,b,n in sm.get_matching_blocks():
    for k in range(n): al[exp[a+k][0]]=[out[b+k]['s'],out[b+k]['e']]
# substituições 1:1 (ex.: produto/produtor)
for tag,a1,a2,b1,b2 in sm.get_opcodes():
    if tag=='replace' and a2-a1==b2-b1:
        for k in range(a2-a1): al[exp[a1+k][0]]=[out[b1+k]['s'],out[b1+k]['e']]
print("aligned",len(al),"of",len(exp))
json.dump(al,open(f"{S}/align_{VER}.json","w"))
