from lib import build, hook_html, cta_html, icon

hook = hook_html("TESTE RÁPIDO", ["*MITO* OU", "*VERDADE*", "NO CRÉDITO", "RURAL"], 165, pill_icon="search")

CLAIMS = [
    ("Seca e quebra de safra obrigam o banco a <b>prorrogar</b>?", True,
     "É <b>direito do produtor</b>, não favor do banco (Súmula 298 STJ)"),
    ("O banco pode vencer a cédula <b>antecipadamente</b> sem motivo?", False,
     "Vencimento antecipado exige <b>motivo previsto</b> em contrato e na lei"),
    ("A pequena propriedade rural pode ser <b>penhorada</b>?", False,
     "Se trabalhada pela família, é <b>impenhorável</b> (CF, art. 5º, XXVI)"),
]

cards = ""
for i, (q, true, ex) in enumerate(CLAIMS):
    lab = "VERDADE" if true else "MITO"
    cards += f"""
<div class="claim" id="c{i}">
  <div class="num anton">Afirmação {i + 1}/3</div>
  <div class="q">{q}</div>
  <div class="chips">
    <div class="chip mito anton"><div class="lit"></div><span>{icon("x", "#f6f1e3", 46, 8)}Mito</span></div>
    <div class="chip verd anton"><div class="lit"></div><span>{icon("check", "#f6f1e3", 46, 8)}Verdade</span></div>
  </div>
  <div class="seal anton {'ok' if true else 'no'}">{lab}</div>
  <div class="ex">{ex}</div>
</div>"""

body = f"""
<div class="head anton"><span class="gold">Mito</span> ou <span class="gold">Verdade</span>?</div>
<div class="dots"><i></i><i></i><i></i></div>
<div class="stack">{cards}</div>
"""

css = """
#body{padding-top:150px}
.head{font-size:84px;line-height:1.1}
.dots{display:flex;gap:18px;margin:20px 0 28px}
.dots i{width:22px;height:22px;border-radius:50%;background:rgba(217,178,76,.25);border:3px solid var(--gold)}
.stack{position:relative;width:100%;height:960px}
.claim{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center}
.claim .num{font-size:44px;color:var(--gold);letter-spacing:.06em}
.claim .q{margin-top:18px;width:100%;background:rgba(6,25,15,.6);border:4px solid rgba(217,178,76,.6);border-radius:30px;
 padding:30px 36px;font-weight:900;font-size:56px;line-height:1.15;color:var(--cream)}
.claim .q b{color:var(--gold-light)}
.chips{display:flex;gap:30px;margin-top:30px}
.chip{position:relative;overflow:hidden;width:380px;height:104px;border-radius:24px;font-size:60px;display:flex;align-items:center;justify-content:center;
 border:5px solid;color:var(--cream)}
.chip span{position:relative;display:flex;align-items:center;gap:16px;padding-top:6px}
.chip.mito{border-color:#d64533;background:rgba(214,69,51,.18)}
.chip.verd{border-color:#2f9e5b;background:rgba(47,158,91,.18)}
.chip .lit{position:absolute;inset:0;opacity:0}
.chip.mito .lit{background:#c23a2a}
.chip.verd .lit{background:#23824a}
.seal{position:relative;margin-top:32px;font-size:104px;line-height:1;padding:16px 44px 4px;border:12px solid;border-radius:24px;transform:rotate(-6deg);
 background:rgba(6,25,15,.85);box-shadow:0 14px 40px rgba(0,0,0,.5)}
.seal.ok{color:#4fd18a;border-color:#4fd18a}
.seal.no{color:#ff6b57;border-color:#ff6b57}
.ex{margin-top:30px;font-weight:900;font-size:42px;line-height:1.2;color:#dfe4de}
.ex b{color:var(--gold-light)}
"""

T = [2.35, 5.35, 8.35]
TRUTH = [c[1] for c in CLAIMS]
js = """
mood(0.9, "sad");
tl.to("#cb-head", { rotation: -8, svgOrigin: HEAD, duration: 0.3 }, 1.0);
tl.to("#cb-head", { rotation: 0, svgOrigin: HEAD, duration: 0.3 }, 2.0);
tl.fromTo(".head", { opacity: 0, y: -40 }, { opacity: 1, y: 0, duration: 0.3, ease: "power3.out" }, 2.2);
shine(".head .gold", 2.5);
const T = %s, TRUTH = %s;
T.forEach((t, i) => {
  const c = "#c" + i, good = TRUTH[i];
  const right = c + (good ? " .verd" : " .mito"), wrong = c + (good ? " .mito" : " .verd");
  tl.fromTo(".dots i:nth-child(" + (i + 1) + ")", { backgroundColor: "rgba(217,178,76,.25)", scale: 1 },
    { backgroundColor: "#d9b24c", scale: 1.3, duration: 0.2 }, t);
  tl.fromTo(c, { opacity: 0, x: 900 }, { opacity: 1, x: 0, duration: 0.4, ease: "power4.out" }, t);
  marker(c + " .q b", t + 0.5);
  tl.fromTo(c + " .chip", { opacity: 0, y: 60 }, { opacity: 1, y: 0, duration: 0.3, stagger: 0.08, ease: "back.out(2)" }, t + 0.3);
  // suspense: luzes alternando
  [0, 1, 2, 3].forEach((k) => {
    const el = c + (k %% 2 ? " .verd .lit" : " .mito .lit");
    tl.fromTo(el, { opacity: 0 }, { opacity: 0.9, duration: 0.06, immediateRender: false }, t + 0.65 + k * 0.16);
    tl.to(el, { opacity: 0, duration: 0.08 }, t + 0.75 + k * 0.16);
  });
  // revelação
  tl.to(right + " .lit", { opacity: 1, duration: 0.1 }, t + 1.35);
  tl.to(right, { scale: 1.08, duration: 0.15, ease: "back.out(3)" }, t + 1.35);
  tl.to(wrong, { opacity: 0.3, scale: 0.92, duration: 0.2 }, t + 1.35);
  stamp(c + " .seal", t + 1.45);
  punch(t + 1.5, 1.05);
  jolt(c + " .q", t + 1.55);
  tl.fromTo(c + " .ex", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.3, ease: "power3.out" }, t + 1.75);
  marker(c + " .ex b", t + 2.0);
  if (good) { mood(t + 1.45, "happy"); nodYes(t + 1.5); point(t + 1.4, -78); }
  else { mood(t + 1.45, "happy"); shakeNo(t + 1.5); point(t + 1.4, -70); }
  armDown(t + 2.6);
  if (i < 2) tl.to(c, { opacity: 0, x: -900, duration: 0.3, ease: "power3.in" }, t + 2.7);
});
point(11.8, -24);
""" % (T, str(TRUTH).lower())

says = [("Hmm... será?", 1.25, 2.1), ("Verdade, sô!", 3.85, 5.25), ("Mito, uai!", 6.85, 8.25), ("Mito também!", 9.85, 11.2),
        ("Comenta aí, sô!", 12.45, 15.2)]

SFX = []
for i, t in enumerate(T):
    SFX += [(t, "whoosh"), (t + 0.3, "pop", 0.6), (t + 0.38, "pop", 0.6)]
    SFX += [(t + 0.65 + k * 0.16, "tick", 1.4) for k in range(4)]
    SFX += [(t + 1.35, "good" if TRUTH[i] else "bad"), (t + 1.45, "stamp"), (t + 1.75, "whoosh", 0.4)]
    if i < 2:
        SFX.append((t + 2.7, "whoosh", 0.6))

d = build("r4-mito-ou-verdade", "Mito ou Verdade", hook, body, css, js,
          cta_html("DIREITO", 'que eu te <span class="goldl mk">explico</span>', 190), says, 0.12, SFX)
print(d)
