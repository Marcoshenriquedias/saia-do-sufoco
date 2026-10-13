from lib import build, hook_html, cta_html, icon

hook = hook_html("PRODUTOR, ATENÇÃO", ["A JUSTIÇA", "PODE TIRAR", "SUA *TERRA?*"], 180, pill_icon="scale")

digits = "".join(f"<div>{d}</div>" for d in "9876543210")
body = f"""
<div class="odo-wrap">
  <div class="ring"></div>
  <div class="odo anton"><div class="strip shine">{digits}</div></div>
</div>
<div class="badge anton">{icon("scale", "#06190f", 54, 6)}Súmula 298 do STJ</div>
<div class="phrase">
  <div class="ln">Se houver direito à</div>
  <div class="ln"><span class="mk">prorrogação</span> por</div>
  <div class="ln"><span class="mk">quebra de safra</span>,</div>
  <div class="ln big anton">o banco <span class="no">não</span> pode</div>
  <div class="ln big anton">simplesmente <span class="gold">executar!</span></div>
</div>
<div class="seal anton">{icon("gavel", "#f6f1e3", 70, 5)}<span>Direito do<br/>produtor</span></div>
"""

H = 420
css = f"""
#body{{padding-top:175px}}
.odo-wrap{{position:relative;width:520px;height:{H}px;display:flex;align-items:center;justify-content:center}}
.ring{{position:absolute;width:500px;height:500px;border-radius:50%;border:10px solid rgba(217,178,76,.5);
 box-shadow:0 0 80px rgba(217,178,76,.35),inset 0 0 80px rgba(217,178,76,.25)}}
.odo{{position:relative;height:{H}px;overflow:hidden;border-radius:40px;-webkit-mask-image:linear-gradient(transparent,#000 7%,#000 93%,transparent);mask-image:linear-gradient(transparent,#000 7%,#000 93%,transparent);font-size:{int(H * 1.0)}px;line-height:{H}px}}
.strip div{{height:{H}px}}
.badge{{margin-top:40px;display:flex;align-items:center;gap:16px;font-size:58px;color:var(--green-900);background:var(--gold);
 padding:12px 34px 8px;border-radius:16px;box-shadow:0 12px 30px rgba(0,0,0,.4)}}
.phrase{{margin-top:44px}}
.phrase .ln{{font-weight:900;font-size:54px;line-height:1.18}}
.phrase .ln.big{{font-size:84px;line-height:1.08;margin-top:6px}}
.phrase .no{{color:#ff6b57;text-decoration:line-through;text-decoration-thickness:0;position:relative}}
.seal{{position:absolute;right:120px;top:190px;width:250px;height:250px;border-radius:50%;background:var(--red);border:8px solid var(--cream);
 display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;font-size:40px;line-height:1.02;color:var(--cream);
 box-shadow:0 14px 40px rgba(0,0,0,.5);text-align:center}}
"""

js = f"""
mood(0.9, "sad");
point(1.2, -62);
armDown(2.05);

// odômetro sobe e trava no 0
tl.fromTo(".ring", {{ opacity: 0, scale: 0.3 }}, {{ opacity: 1, scale: 1, duration: 0.5, ease: "back.out(1.8)" }}, 2.25);
tl.fromTo(".strip", {{ y: 0 }}, {{ y: -{9 * H}, duration: 1.15, ease: "power3.inOut" }}, 2.3);
tl.fromTo(".odo", {{ scale: 0.7 }}, {{ scale: 1, duration: 1.15, ease: "power2.out" }}, 2.3);
tl.to(".odo", {{ scale: 1.15, duration: 0.08, ease: "power2.out" }}, 3.45);
tl.to(".odo", {{ scale: 1, duration: 0.35, ease: "back.out(3)" }}, 3.53);
punch(3.45, 1.07);
shine(".strip", 3.6);
tl.to(".ring", {{ scale: 1.08, duration: 0.5, repeat: 9, yoyo: true, ease: "sine.inOut" }}, 3.6);
point(2.4, -88);
mood(3.5, "happy");

stamp(".badge", 3.9);
tl.fromTo(".phrase .ln", {{ opacity: 0, y: 40 }}, {{ opacity: 1, y: 0, duration: 0.3, stagger: 0.45, ease: "power3.out" }}, 4.5);
marker(".phrase .mk", 5.3);
// "NÃO" bate com destaque
tl.fromTo(".phrase .no", {{ scale: 1 }}, {{ scale: 1.35, duration: 0.12, ease: "power2.out" }}, 6.0);
tl.to(".phrase .no", {{ scale: 1, duration: 0.3, ease: "back.out(3)" }}, 6.12);
punch(6.0, 1.04);
shine(".phrase .gold", 6.6);
point(4.6, -75);
nodYes(6.2);

// selo
tl.to(".odo-wrap", {{ x: -110, scale: 0.9, duration: 0.4, ease: "power2.inOut" }}, 7.6);
stamp(".seal", 7.9);
jolt(".seal", 8.18);
punch(7.95, 1.05);
point(8.0, -82);
shakeNo(9.2);
point(11.8, -24);
"""

says = [("Será, sô?!", 1.3, 2.1), ("Zero, uai!", 3.6, 5.4), ("Tá na lei, sô!", 5.6, 7.7), ("Direito é direito!", 8.4, 11.2),
        ("Comenta aí, sô!", 12.45, 15.2)]

SFX = [(2.25, "riser", 0.8)] + [(2.3 + 1.15 * (1 - (1 - k / 10) ** 0.6), "tick", 1.2) for k in range(10)] + [
    (3.45, "thud"), (3.48, "ding"), (3.6, "sparkle", 0.6), (3.9, "stamp", 0.7),
    (4.5, "whoosh", 0.4), (4.95, "whoosh", 0.4), (5.4, "whoosh", 0.4), (5.85, "whoosh", 0.4), (6.0, "thud", 0.8), (6.3, "whoosh", 0.4),
    (6.6, "ding", 0.4), (7.6, "whoosh", 0.6), (7.9, "stamp"), (8.0, "good")]

d = build("r2-numero-que-choca", "Número que Choca", hook, body, css, js,
          cta_html("LEI", 'que eu te <span class="goldl mk">ajudo</span>', 230), says, 0.13, SFX)
print(d)
