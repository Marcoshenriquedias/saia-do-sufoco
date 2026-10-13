from lib import build, hook_html, cta_html, icon

hook = hook_html("PASSO A PASSO", ["COMO *PRORROGAR*", "SUA DÍVIDA RURAL", "POR *QUEBRA* *DE* *SAFRA*"], 118, pill_icon="calendar")

STEPS = [
    ("cloud", "Perícia técnica", "de <b>frustração de safra</b>"),
    ("mail", "Notificação", "<b>administrativa</b> ao banco"),
    ("gavel", "Ação na Justiça", "com pedido de <b>liminar</b>"),
]
steps = "".join(f"""
<div class="step" id="s{i}">
  <div class="ic">{icon(ic, "#06190f", 104, 5)}<div class="n anton">{i + 1}</div></div>
  <div class="tx"><div class="t1 anton">{t1}</div><div class="t2">{t2}</div></div>
  <div class="ok">{icon("check", "#f6f1e3", 44, 8)}</div>
</div>""" for i, (ic, t1, t2) in enumerate(STEPS))

body = f"""
<div class="head anton">Prorrogação em <span class="gold">3 passos</span></div>
<div class="rule"></div>
<div class="steps"><div class="line"><div class="lf"></div></div>{steps}</div>
"""

css = """
#body{padding-top:170px}
.head{font-size:74px;line-height:1.12;white-space:nowrap}
.rule{width:260px;height:10px;background:var(--gold);border-radius:6px;margin:24px auto 44px}
.steps{position:relative;width:100%}
.line{position:absolute;left:95px;top:122px;width:10px;height:560px;background:rgba(217,178,76,.2);border-radius:6px;overflow:hidden}
.lf{width:100%;height:100%;background:var(--gold);transform-origin:top center}
.step{position:relative;display:flex;align-items:center;gap:34px;text-align:left;margin-bottom:36px;padding:22px 30px 22px 0}
.ic{position:relative;flex:0 0 200px;height:200px;border-radius:50%;background:var(--gold);display:flex;align-items:center;justify-content:center;
 box-shadow:0 0 0 10px rgba(6,25,15,.9),0 0 50px rgba(217,178,76,.4)}
.ic .n{position:absolute;top:-8px;left:-8px;width:64px;height:64px;border-radius:50%;background:var(--green-900);border:4px solid var(--gold);
 color:var(--gold);font-size:40px;display:flex;align-items:center;justify-content:center}
.tx{flex:1;background:rgba(6,25,15,.6);border:3px solid rgba(217,178,76,.5);border-radius:24px;padding:24px 30px}
.t1{font-size:70px;line-height:1.05;color:var(--cream)}
.t2{font-weight:900;font-size:39px;white-space:nowrap;line-height:1.15;color:#d7dcd6;margin-top:6px}
.t2 b{color:var(--gold-light)}
.ok{position:absolute;right:-6px;top:-4px;width:76px;height:76px;border-radius:50%;background:#2f9e5b;border:5px solid var(--cream);
 display:flex;align-items:center;justify-content:center;box-shadow:0 8px 20px rgba(0,0,0,.45)}
"""

T = [2.75, 5.55, 8.35]
js = """
point(1.2, -62);
nodYes(1.4);
armDown(2.05);
tl.fromTo(".head", { opacity: 0, y: -40 }, { opacity: 1, y: 0, duration: 0.3, ease: "power3.out" }, 2.2);
shine(".head .gold", 2.5);
tl.fromTo(".rule", { scaleX: 0 }, { scaleX: 1, duration: 0.3, ease: "power3.out" }, 2.35);
const T = %s, ANG = [-80, -70, -58];
T.forEach((t, i) => {
  const s = "#s" + i;
  if (i > 0) {
    tl.fromTo(".lf", { scaleY: (i - 1) / 2 }, { scaleY: i / 2, duration: 0.35, ease: "power2.inOut", immediateRender: false }, t - 0.3);
    tl.to("#s" + (i - 1) + " .tx", { opacity: 0.55, duration: 0.25 }, t);
  }
  tl.fromTo(s + " .ic", { scale: 0, rotation: -120 }, { scale: 1, rotation: 0, duration: 0.45, ease: "back.out(2.2)" }, t);
  tl.fromTo(s + " .tx", { opacity: 0, x: 700 }, { opacity: 1, x: 0, duration: 0.4, ease: "power4.out" }, t + 0.1);
  tl.fromTo(s + " .t2", { opacity: 0 }, { opacity: 1, duration: 0.25 }, t + 0.4);
  marker(s + " .t2 b", t + 0.65);
  tl.to(s + " .ic svg", { rotation: 12, duration: 0.12, yoyo: true, repeat: 3, ease: "sine.inOut" }, t + 0.5);
  stamp(s + " .ok", t + 1.35);
  punch(t + 1.38, 1.03);
  point(t + 0.1, ANG[i]);
  nodYes(t + 1.45);
});
tl.fromTo(".lf", { scaleY: 0 }, { scaleY: 0, duration: 0.01 }, 2.2);
tl.to(".lf", { scaleY: 1, duration: 0.3, ease: "power2.out" }, 9.8);
tl.to(["#s0 .tx", "#s1 .tx"], { opacity: 1, duration: 0.3 }, 10.2);
point(11.8, -24);
""" % T

says = [("Tem jeito, sô!", 1.3, 2.1), ("Primeiro, a prova!", 3.0, 5.45), ("Depois, avisa o banco!", 5.8, 8.25),
        ("E a Justiça decide!", 8.6, 11.2), ("Comenta aí, sô!", 12.45, 15.2)]

SFX = [(2.2, "whoosh", 0.5)]
for t in T:
    SFX += [(t, "pop", 1.0), (t + 0.1, "whoosh"), (t + 0.5, "tick"), (t + 0.62, "tick"), (t + 0.74, "tick"),
            (t + 1.35, "stamp", 0.5), (t + 1.38, "good", 0.9)]
SFX += [(9.8, "riser", 0.5), (10.1, "sparkle")]

d = build("r3-passo-a-passo", "Passo a Passo", hook, body, css, js,
          cta_html("SAFRA", 'que eu te <span class="goldl mk">ajudo</span>', 220), says, 0.1, SFX)
print(d)
