from lib import build, hook_html, cta_html, icon

hook = hook_html("ALERTA", ["O *PERIGO* DA", "*EXECUÇÃO*", "BANCÁRIA", "NA FAZENDA"], 160, pill_red=True, pill_icon="alert")

body = f"""
<div class="vs-title anton">A situação do <span class="gold">produtor</span></div>
<div class="split">
  <div class="panel before" id="pA">
    <div class="tag anton">Antes</div>
    <div class="art">{icon("tractor", "#8d958f", 250, 3.5)}
      <div class="lockb">{icon("lock", "#f6f1e3", 64, 5)}</div>
      <div class="penh anton">Penhorado</div>
    </div>
    <div class="txt">Desespero com o <b>trator</b> e a <b>terra penhorada</b></div>
  </div>
  <div class="arrow" id="arr"><svg width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="#06190f" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div>
  <div class="panel after" id="pB">
    <div class="tag anton">Depois</div>
    <div class="art"><div class="glow"></div>{icon("shield", "#d9b24c", 250, 3.5, "shieldic")}
      <div class="susp anton">Execução suspensa</div>
    </div>
    <div class="txt">Defesa <b>blindada</b> e <b>suspensão</b> da execução</div>
  </div>
</div>
<div class="result" id="res">
  <div class="rays"></div>
  <svg class="bigshield" width="400" height="440" viewBox="0 0 64 70">
    <path d="M32 4l26 9v19c0 17-12 29-26 34C18 61 6 49 6 32V13z" fill="#d9b24c" stroke="#f3d987" stroke-width="2"/>
    <path d="M32 10l20 7v15c0 13-9 23-20 27-11-4-20-14-20-27V17z" fill="#0b2b1c"/>
    <path id="tick" d="M21 34l8 8 15-16" fill="none" stroke="#f3d987" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
  <div class="r1 anton">Patrimônio</div>
  <div class="r2 anton">Protegido</div>
</div>
"""

css = """
#body{padding-top:150px}
.vs-title{font-size:84px;line-height:1.1;margin-bottom:50px}
.split{position:relative;width:100%;display:flex;gap:40px;justify-content:space-between}
.panel{position:relative;width:430px;height:780px;border-radius:30px;padding:36px 30px;display:flex;flex-direction:column;align-items:center;text-align:center}
.panel .tag{font-size:96px;line-height:1}
.panel .art{position:relative;margin:30px 0 70px;height:300px;display:flex;align-items:center;justify-content:center}
.panel .txt{font-weight:900;font-size:46px;line-height:1.14}
.before{background:rgba(141,149,143,.12);border:4px solid rgba(141,149,143,.55)}
.before .tag{color:#a7aea9}
.before .txt{color:#b9beb9}
.before .txt b{color:#e7e9e6}
.lockb{position:absolute;right:-6px;top:-6px;width:96px;height:96px;border-radius:50%;background:#5b625d;display:flex;align-items:center;justify-content:center;border:4px solid #8d958f}
.penh{position:absolute;bottom:-46px;left:50%;margin-left:-170px;width:340px;font-size:60px;color:var(--red);border:7px solid var(--red);border-radius:14px;
 padding:4px 0 0;transform:rotate(-12deg);background:rgba(6,25,15,.75)}
.after{background:linear-gradient(180deg,rgba(217,178,76,.22),rgba(18,64,42,.6));border:4px solid var(--gold);box-shadow:0 0 50px rgba(217,178,76,.25)}
.after .tag{color:var(--gold)}
.after .txt b{color:var(--gold-light)}
.glow{position:absolute;width:300px;height:300px;border-radius:50%;background:radial-gradient(circle,rgba(243,217,135,.55),rgba(243,217,135,0) 65%)}
.shieldic{position:relative}
.susp{position:absolute;bottom:-46px;left:50%;margin-left:-185px;width:370px;font-size:46px;white-space:nowrap;color:var(--green-900);background:var(--gold);border-radius:14px;padding:8px 0 4px;transform:rotate(-4deg)}
.arrow{position:absolute;left:50%;top:250px;margin-left:-55px;width:110px;height:110px;border-radius:50%;background:var(--gold);display:flex;align-items:center;justify-content:center;
 box-shadow:0 0 0 10px rgba(6,25,15,.9);z-index:2}
.result{position:absolute;left:0;right:0;top:150px;display:flex;flex-direction:column;align-items:center}
.rays{position:absolute;top:-60px;width:760px;height:760px;border-radius:50%;
 background:repeating-conic-gradient(rgba(217,178,76,.16) 0deg 10deg,rgba(217,178,76,0) 10deg 20deg);
 -webkit-mask:radial-gradient(circle,#000 30%,transparent 70%);mask:radial-gradient(circle,#000 30%,transparent 70%)}
.bigshield{position:relative;filter:drop-shadow(0 20px 40px rgba(0,0,0,.5))}
.r1{position:relative;font-size:150px;line-height:1;margin-top:40px}
.r2{position:relative;font-size:190px;line-height:1;color:var(--gold)}
"""

js = """
// hook: cowboy assustado
mood(0.9, "sad");
point(1.2, -62);
armDown(2.0);

tl.fromTo(".vs-title", { opacity: 0, y: -40 }, { opacity: 1, y: 0, duration: 0.3, ease: "power3.out" }, 2.2);
// ANTES
tl.fromTo("#pA", { opacity: 0, x: -500 }, { opacity: 1, x: 0, duration: 0.45, ease: "power4.out" }, 2.35);
tl.fromTo("#pA .art svg", { y: -300, opacity: 0 }, { y: 0, opacity: 1, duration: 0.4, ease: "bounce.out" }, 2.6);
tl.fromTo("#pA .txt", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.3 }, 2.85);
tl.fromTo("#pA .lockb", { opacity: 0, scale: 0 }, { opacity: 1, scale: 1, duration: 0.3, ease: "back.out(3)" }, 3.3);
stamp("#pA .penh", 3.7);
jolt("#pA", 3.95);
point(2.6, -84);
// DEPOIS
tl.to("#pA", { opacity: 0.55, scale: 0.97, duration: 0.3 }, 5.55);
tl.fromTo("#arr", { opacity: 0, scale: 0, rotation: -180 }, { opacity: 1, scale: 1, rotation: 0, duration: 0.35, ease: "back.out(2.5)" }, 5.5);
tl.fromTo("#pB", { opacity: 0, x: 500 }, { opacity: 1, x: 0, duration: 0.45, ease: "power4.out" }, 5.7);
tl.fromTo("#pB .shieldic", { scale: 0, rotation: -30 }, { scale: 1, rotation: 0, duration: 0.5, ease: "back.out(2.5)" }, 6.0);
tl.fromTo("#pB .glow", { opacity: 0, scale: 0.4 }, { opacity: 1, scale: 1, duration: 0.5 }, 6.1);
tl.to("#pB .glow", { scale: 1.2, opacity: 0.6, duration: 0.6, repeat: 3, yoyo: true, ease: "sine.inOut" }, 6.6);
tl.fromTo("#pB .txt", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.3 }, 6.35);
stamp("#pB .susp", 6.9);
mood(5.75, "happy");
point(5.8, -72);
nodYes(6.95);
// RESULTADO
tl.to([".vs-title", ".split"], { opacity: 0, scale: 0.85, duration: 0.25, ease: "power2.in" }, 8.9);
tl.fromTo("#res", { opacity: 0 }, { opacity: 1, duration: 0.01 }, 9.1);
tl.fromTo(".rays", { opacity: 0, scale: 0.5, rotation: 0 }, { opacity: 1, scale: 1, rotation: 40, duration: 2.3, ease: "power1.out" }, 9.1);
tl.fromTo(".bigshield", { scale: 0, rotation: -25 }, { scale: 1, rotation: 0, duration: 0.5, ease: "back.out(2)" }, 9.15);
tl.fromTo("#tick", { strokeDasharray: 40, strokeDashoffset: 40 }, { strokeDasharray: 40, strokeDashoffset: 0, duration: 0.35, ease: "power2.out" }, 9.55);
tl.fromTo(".r1", { opacity: 0, y: 60 }, { opacity: 1, y: 0, duration: 0.3, ease: "power3.out" }, 9.7);
tl.fromTo(".r2", { opacity: 0, scale: 2.2 }, { opacity: 1, scale: 1, duration: 0.3, ease: "power4.out" }, 9.9);
jolt(".r2", 10.2);
point(9.3, -58);
nodYes(10.3);
point(11.8, -24);
"""

says = [("Ai, meu Deus... e agora?", 2.7, 5.45), ("Agora sim, sô!", 6.1, 8.8), ("Isso que é defesa!", 9.4, 11.3), ("Comenta aí, sô!", 12.45, 15.2)]

d = build("r1-antes-depois", "Antes e Depois", hook, body, css, js,
          cta_html("PROTEÇÃO", 'que eu te <span class="goldl">explico</span>', 168), says, 0.11)
print(d)
