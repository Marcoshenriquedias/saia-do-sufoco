from lib import build, hook_html, cta_html, icon, ICONS

ICONS["sun"] = '<circle cx="32" cy="32" r="11"/><path d="M32 6v8M32 50v8M6 32h8M50 32h8M13 13l6 6M45 45l6 6M13 51l6-6M45 19l6-6"/>'
ICONS["thermo"] = '<path d="M26 38V12a6 6 0 0 1 12 0v26a11 11 0 1 1-12 0z"/><path d="M32 22v20"/>'
ICONS["drop"] = '<path d="M32 6C24 20 16 30 16 40a16 16 0 0 0 32 0C48 30 40 20 32 6z"/><path d="M14 54L50 18"/>'
ICONS["camera"] = '<rect x="6" y="18" width="52" height="36" rx="6"/><circle cx="32" cy="36" r="10"/><path d="M22 18l4-8h12l4 8"/>'

DUR = 30
hook = hook_html("URGENTE", ["*EL* *NIÑO* CHEGOU", "SUA LAVOURA", "ESTÁ *PROTEGIDA?*"], 132, pill_red=True, pill_icon="alert")

REG = [("cloud", "#5aa9e6", "Sul", "Excesso de chuva"),
       ("sun", "#f0a33a", "Centro-Sul", "Seca moderada e calor"),
       ("thermo", "#f07a3a", "Norte do Sudeste", "Risco de seca"),
       ("drop", "#e0603a", "Nordeste e Norte", "Estiagem (inclui Amazônia)")]
rows = "".join(f"""
<div class="reg" id="r{i}" style="--c:{c}">
  <div class="ric">{icon(ic, "#06190f", 72, 5)}</div>
  <div><div class="rn anton">{n}</div><div class="rd">{d}</div></div>
</div>""" for i, (ic, c, n, d) in enumerate(REG))

CHIPS = ["Clima", "Crédito rural", "Seguro rural", "Zarc", "Assistência técnica", "Plano Safra", "Avisos do tempo",
         "Painel El Niño", "Tecnologias Embrapa"]
chips = "".join(f'<span class="chip">{c}</span>' for c in CHIPS)

BEN = ["Juros mais favoráveis", "Prazos melhores", "Limites maiores", "Prioridade para quem tem seguro"]
bens = "".join(f'<div class="ben">{icon("check", "#f6f1e3", 40, 8)}<span>{b}</span></div>' for b in BEN)

body = f"""
<div class="scn" id="sA">
  <div class="tt anton">Previsão do <span class="gold shine">El Niño</span></div>
  <div class="src">Fonte: Mapa / Inmet</div>
  {rows}
</div>
<div class="scn" id="sB">
  <div class="tt anton">O governo <span class="gold shine">se mexeu</span></div>
  <div class="card">
    <div class="ch">{icon("search", "#d9b24c", 54, 5)}<span><b>Mapa + Inmet</b> lançaram uma página oficial com:</span></div>
    <div class="chips">{chips}</div>
  </div>
  <div class="info" id="iB1">{icon("people", "#d9b24c", 64, 4)}<span>Grupo de Trabalho acompanha o fenômeno e propõe medidas</span></div>
  <div class="info" id="iB2">{icon("shield", "#d9b24c", 64, 4)}<span>Núcleo <b class="mk">permanente</b> de gestão de riscos climáticos</span></div>
</div>
<div class="scn" id="sC">
  <div class="law anton">{icon("doc", "#06190f", 50, 5)}Nova lei · DOU 30/9</div>
  <div class="eq">
    <div class="eqb" id="e1"><div class="eqi">{icon("shield", "#06190f", 92, 5)}</div><div class="anton">Seguro<br/>rural</div></div>
    <div class="plus anton">=</div>
    <div class="eqb" id="e2"><div class="eqi">{icon("lock", "#06190f", 92, 5)}</div><div class="anton">Garantia do<br/>crédito</div></div>
  </div>
  <div class="eqt">O seguro rural agora entra entre as <b class="mk">garantias do crédito rural</b></div>
  <div class="bens">{bens}</div>
</div>
<div class="scn" id="sD">
  <div class="tt anton">O que fazer <span class="gold shine">agora?</span></div>
  <div class="tip" id="t1"><div class="tic">{icon("camera", "#06190f", 80, 5)}</div><div>Guarde <b class="mk">laudos, fotos e notas</b> da lavoura</div></div>
  <div class="tip" id="t2"><div class="tic">{icon("calendar", "#06190f", 80, 5)}</div><div>Quebrou a safra pelo clima? Você pode ter <b class="mk">direito à prorrogação</b> da dívida</div></div>
</div>
"""

css = """
#body{padding-top:0}
.scn{position:absolute;left:100px;right:100px;top:150px;display:flex;flex-direction:column;align-items:center;opacity:0}
.tt{font-size:92px;line-height:1.08}
.src{font-weight:800;font-size:34px;color:#b9c2ba;margin:10px 0 34px}
.reg{width:100%;display:flex;align-items:center;gap:30px;text-align:left;background:rgba(6,25,15,.6);border:3px solid rgba(217,178,76,.4);
 border-left:16px solid var(--c);border-radius:24px;padding:22px 30px;margin-bottom:24px}
.ric{flex:0 0 120px;height:120px;border-radius:50%;background:var(--c);display:flex;align-items:center;justify-content:center}
.rn{font-size:60px;line-height:1;color:var(--gold-light)}
.rd{font-weight:900;font-size:44px;line-height:1.15;color:var(--cream);margin-top:6px}
.card{margin-top:40px;width:100%;background:rgba(6,25,15,.6);border:4px solid rgba(217,178,76,.6);border-radius:30px;padding:30px}
.card .ch{display:flex;align-items:center;gap:18px;text-align:left;font-weight:800;font-size:44px;line-height:1.15}
.card .ch b{color:var(--gold-light)}
.chips{display:flex;flex-wrap:wrap;gap:14px;justify-content:center;margin-top:26px}
.chip{font-weight:900;font-size:38px;color:var(--green-900);background:var(--gold);border-radius:999px;padding:10px 26px}
.info{width:100%;display:flex;align-items:center;gap:24px;text-align:left;font-weight:900;font-size:44px;line-height:1.18;margin-top:34px}
.info svg{flex:0 0 64px}
.info b{color:var(--gold-light)}
.law{display:flex;align-items:center;gap:16px;font-size:64px;color:var(--green-900);background:var(--gold);border-radius:18px;padding:12px 34px 6px;
 box-shadow:0 12px 30px rgba(0,0,0,.45)}
.eq{display:flex;align-items:center;gap:26px;margin-top:44px}
.eqb{display:flex;flex-direction:column;align-items:center;gap:14px;font-size:54px;line-height:1.02}
.eqi{width:170px;height:170px;border-radius:50%;background:var(--gold);display:flex;align-items:center;justify-content:center;
 box-shadow:0 0 0 10px rgba(217,178,76,.2),0 0 50px rgba(217,178,76,.35)}
.plus{font-size:120px;color:var(--gold)}
.eqt{margin-top:34px;font-weight:900;font-size:46px;line-height:1.18}
.eqt b{color:var(--gold-light)}
.bens{margin-top:28px;display:grid;grid-template-columns:1fr 1fr;gap:16px;width:100%}
.ben{display:flex;align-items:center;gap:14px;text-align:left;background:rgba(47,158,91,.22);border:3px solid #2f9e5b;border-radius:18px;
 padding:16px 20px;font-weight:900;font-size:36px;line-height:1.12}
.ben svg{flex:0 0 40px;background:#2f9e5b;border-radius:50%;padding:4px}
.tip{width:100%;display:flex;align-items:center;gap:30px;text-align:left;background:rgba(6,25,15,.6);border:4px solid rgba(217,178,76,.6);
 border-radius:30px;padding:34px;margin-top:40px;font-weight:900;font-size:52px;line-height:1.15}
.tic{flex:0 0 140px;height:140px;border-radius:50%;background:var(--gold);display:flex;align-items:center;justify-content:center}
.tip b{color:var(--gold-light)}
"""

js = """
mood(0.9, "sad");
point(1.2, -62);
armDown(2.05);
wtilt(1.2, -6);
function sceneIn(sel, t) { tl.fromTo(sel, { opacity: 0, y: 60 }, { opacity: 1, y: 0, duration: 0.35, ease: "power3.out" }, t); }
function sceneOut(sel, t) { tl.to(sel, { opacity: 0, x: -700, duration: 0.3, ease: "power3.in" }, t); }

// A — previsão (2.2–8.9)
sceneIn("#sA", 2.25);
shine("#sA .shine", 2.6);
[0, 1, 2, 3].forEach((i) => {
  const t = 2.7 + i * 1.05;
  tl.fromTo("#r" + i, { opacity: 0, x: 800 }, { opacity: 1, x: 0, duration: 0.4, ease: "power4.out" }, t);
  tl.fromTo("#r" + i + " .ric", { scale: 0, rotation: -90 }, { scale: 1, rotation: 0, duration: 0.45, ease: "back.out(2.4)" }, t + 0.12);
  tl.to("#r" + i + " .ric svg", { rotation: 14, duration: 0.14, yoyo: true, repeat: 3, ease: "sine.inOut" }, t + 0.55);
});
point(2.8, -80); point(3.85, -76); point(4.9, -70); point(5.95, -64);
wnod(6.2);
sceneOut("#sA", 8.85);

// B — governo (9.1–15.4)
mood(9.0, "happy");
sceneIn("#sB", 9.15);
shine("#sB .shine", 9.5);
tl.fromTo("#sB .card", { opacity: 0, scale: 0.85 }, { opacity: 1, scale: 1, duration: 0.35, ease: "back.out(2)" }, 9.4);
tl.fromTo("#sB .chip", { opacity: 0, scale: 0 }, { opacity: 1, scale: 1, duration: 0.25, stagger: 0.17, ease: "back.out(3)" }, 9.9);
wfolder(9.7);
tl.fromTo("#iB1", { opacity: 0, x: 700 }, { opacity: 1, x: 0, duration: 0.4, ease: "power4.out" }, 12.0);
tl.fromTo("#iB2", { opacity: 0, x: 700 }, { opacity: 1, x: 0, duration: 0.4, ease: "power4.out" }, 13.1);
marker("#iB2 .mk", 13.5);
point(12.1, -66);
nodYes(13.3);
armDown(14.6);
sceneOut("#sB", 15.25);

// C — nova lei (15.5–22.3)
sceneIn("#sC", 15.5);
stamp("#sC .law", 15.6);
punch(15.7, 1.05);
tl.fromTo("#e1", { opacity: 0, x: -300 }, { opacity: 1, x: 0, duration: 0.4, ease: "back.out(1.8)" }, 16.2);
tl.fromTo("#sC .plus", { opacity: 0, scale: 0 }, { opacity: 1, scale: 1, duration: 0.3, ease: "back.out(3)" }, 16.6);
tl.fromTo("#e2", { opacity: 0, x: 300 }, { opacity: 1, x: 0, duration: 0.4, ease: "back.out(1.8)" }, 16.85);
tl.fromTo("#sC .eqt", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.3 }, 17.5);
marker("#sC .eqt .mk", 17.8);
tl.fromTo("#sC .ben", { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: 0.3, stagger: 0.35, ease: "back.out(2.5)" }, 19.0);
point(16.3, -70);
nodYes(17.6);
wnod(19.6);
armDown(21.4);
sceneOut("#sC", 22.2);

// D — o que fazer (22.45–26.3)
sceneIn("#sD", 22.45);
shine("#sD .shine", 22.8);
tl.fromTo("#t1", { opacity: 0, x: 800 }, { opacity: 1, x: 0, duration: 0.4, ease: "power4.out" }, 22.9);
tl.fromTo("#t1 .tic", { scale: 0 }, { scale: 1, duration: 0.4, ease: "back.out(2.5)" }, 23.05);
marker("#t1 .mk", 23.4);
wfolder(23.1);
tl.fromTo("#t2", { opacity: 0, x: 800 }, { opacity: 1, x: 0, duration: 0.4, ease: "power4.out" }, 24.3);
tl.fromTo("#t2 .tic", { scale: 0 }, { scale: 1, duration: 0.4, ease: "back.out(2.5)" }, 24.45);
marker("#t2 .mk", 24.9);
punch(24.95, 1.04);
point(24.4, -64);
point(26.8, -48);
wnod(27.3);
"""

says = [("Ih, e agora?", 1.25, 2.1),
        ("Cada região de um jeito!", 3.0, 5.4),
        ("Tem que se preparar!", 6.0, 8.6, "w"),
        ("Saiu página oficial!", 9.7, 12.0, "w"),
        ("Bom saber, sô!", 12.5, 15.0),
        ("Seguro agora ajuda no crédito!", 16.4, 18.9),
        ("Juros e prazos melhores!", 19.3, 22.0, "w"),
        ("Guarda laudo e foto!", 23.1, 25.2, "w"),
        ("Tem direito, sô!", 25.4, 26.3),
        ("Comenta aí, sô!", 27.45, 30.2)]

SFX = [(2.25, "whoosh")]
for i in range(4):
    t = 2.7 + i * 1.05
    SFX += [(t, "whoosh", 0.7), (t + 0.12, "pop"), (t + 0.55, "tick"), (t + 0.7, "tick")]
SFX += [(8.85, "swish", 0.7), (9.15, "whoosh"), (9.4, "pop")] + [(9.9 + k * 0.17, "pop", 0.55) for k in range(9)]
SFX += [(12.0, "whoosh"), (13.1, "whoosh"), (13.5, "ding", 0.5), (15.25, "swish", 0.7),
        (15.6, "stamp"), (16.2, "whoosh"), (16.6, "thud", 0.7), (16.85, "whoosh"), (17.5, "ding", 0.5)]
SFX += [(19.0 + k * 0.35, "good", 0.6) for k in range(4)]
SFX += [(22.2, "swish", 0.7), (22.9, "whoosh"), (23.05, "pop"), (24.3, "whoosh"), (24.45, "pop"), (24.95, "sparkle")]

d = build("n1-el-nino", "El Niño e Crédito Rural", hook, body, css, js,
          cta_html("CLIMA", 'que eu te <span class="goldl mk">explico</span>', 230, DUR), says, 0.1, SFX, dur=DUR, wife=True)
print(d)
