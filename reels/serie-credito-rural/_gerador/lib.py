"""Gerador da série de reels (HyperFrames) — base comum: cowboy, gancho, CTA, progresso."""
import json
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, "..", "reel")

COWBOY = open(os.path.join(HERE, "cowboy.svg.html")).read()
# expressões: boca/sobrancelha alegre x triste + gota de suor
COWBOY = COWBOY.replace(
    '<path d="M236,334 Q260,358 284,334 Z" fill="#7a2e1c" />',
    '<path id="mouth-happy" d="M236,334 Q260,358 284,334 Z" fill="#7a2e1c" />'
    '<path id="mouth-sad" d="M238,346 Q260,326 282,346" stroke="#7a2e1c" stroke-width="7" fill="none" '
    'stroke-linecap="round" opacity="0" />',
)
COWBOY = COWBOY.replace(
    '<path d="M205,224 Q228,208 251,222" stroke="#3b2412" stroke-width="10" fill="none" stroke-linecap="round" />\n'
    '              <path d="M269,222 Q292,208 315,224" stroke="#3b2412" stroke-width="10" fill="none" stroke-linecap="round" />',
    '<g id="brows-happy"><path d="M205,224 Q228,208 251,222" stroke="#3b2412" stroke-width="10" fill="none" stroke-linecap="round" />'
    '<path d="M269,222 Q292,208 315,224" stroke="#3b2412" stroke-width="10" fill="none" stroke-linecap="round" /></g>'
    '<g id="brows-sad" opacity="0"><path d="M207,214 Q230,214 251,230" stroke="#3b2412" stroke-width="10" fill="none" stroke-linecap="round" />'
    '<path d="M269,230 Q290,214 313,214" stroke="#3b2412" stroke-width="10" fill="none" stroke-linecap="round" /></g>'
    '<path id="sweat" d="M330,200 C322,214 318,222 318,230 A12,12 0 0 0 342,230 C342,222 338,214 330,200 Z" fill="#8fd3ff" opacity="0" />',
)
assert 'id="mouth-sad"' in COWBOY and 'id="brows-sad"' in COWBOY

STROKE = 'fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"'
ICONS = {
    "tractor": '<circle cx="20" cy="44" r="12"/><circle cx="20" cy="44" r="4"/><circle cx="50" cy="48" r="8"/>'
    '<path d="M10 34V22h20v12M14 22V10h14v12M30 32h24v10M46 32V20M32 46h10"/>',
    "shield": '<path d="M32 6l22 8v16c0 14-10 24-22 28C20 54 10 44 10 30V14z"/><path d="M22 32l7 7 13-14"/>',
    "lock": '<rect x="12" y="28" width="40" height="28" rx="5"/><path d="M20 28v-8a12 12 0 0 1 24 0v8M32 40v6"/>',
    "search": '<circle cx="27" cy="27" r="15"/><path d="M38 38l16 16"/>',
    "doc": '<path d="M16 6h22l12 12v40H16z"/><path d="M38 6v12h12M24 32h18M24 40h18M24 48h12"/>',
    "mail": '<rect x="6" y="14" width="52" height="36" rx="5"/><path d="M8 18l24 18 24-18"/>',
    "gavel": '<g transform="rotate(-40 32 30)"><rect x="18" y="8" width="28" height="14" rx="3"/><path d="M32 22v30"/></g><path d="M10 56h30"/>',
    "scale": '<path d="M32 8v46M12 16h40M20 56h24M12 16L5 34h14zM52 16l-7 18h14z"/>',
    "cloud": '<path d="M18 38a10 10 0 0 1 2-20 14 14 0 0 1 26 4 9 9 0 0 1 0 16z"/><path d="M22 46l-3 8M32 46l-3 8M42 46l-3 8"/>',
    "chartdown": '<path d="M8 8v48h48"/><path d="M16 18l12 12 8-6 16 18"/><path d="M52 34v8h-8"/>',
    "chartup": '<path d="M8 8v48h48"/><path d="M16 44l12-12 8 6 16-18"/><path d="M44 20h8v8"/>',
    "house": '<path d="M8 30L32 10l24 20M14 26v28h36V26"/><path d="M27 54V40h10v14"/>',
    "people": '<circle cx="22" cy="22" r="8"/><circle cx="44" cy="24" r="6"/><path d="M8 52c0-10 6-16 14-16s14 6 14 16M36 52c0-8 3-13 8-13s10 5 10 13"/>',
    "idcard": '<rect x="6" y="14" width="52" height="36" rx="5"/><circle cx="22" cy="30" r="6"/><path d="M14 44c2-5 14-5 16 0M36 26h14M36 34h14M36 42h8"/>',
    "stop": '<path d="M22 6h20l14 14v20L42 54H22L8 40V20z"/><path d="M22 30h20"/>',
    "check": '<path d="M12 34l12 12 28-28"/>',
    "x": '<path d="M16 16l32 32M48 16L16 48"/>',
    "calendar": '<rect x="8" y="12" width="48" height="44" rx="5"/><path d="M8 24h48M20 6v12M44 6v12M20 36h8M36 36h8M20 46h8"/>',
    "alert": '<path d="M32 6L60 56H4z"/><path d="M32 24v14M32 46v1"/>',
    "coins": '<ellipse cx="32" cy="16" rx="18" ry="7"/><path d="M14 16v10c0 4 8 7 18 7s18-3 18-7V16M14 26v10c0 4 8 7 18 7s18-3 18-7V26M14 36v10c0 4 8 7 18 7s18-3 18-7V36"/>',
}


def icon(name, color="#d9b24c", size=64, width=4, cls=""):
    return (f'<svg class="{cls}" width="{size}" height="{size}" viewBox="0 0 64 64" '
            + STROKE.format(c=color, w=width) + f'>{ICONS[name]}</svg>')


BASE_CSS = """
:root{--green-900:#06190f;--green-800:#0b2b1c;--green-700:#12402a;--gold:#d9b24c;--gold-light:#f3d987;--cream:#f6f1e3;--red:#d64533;--gray:#8d958f}
*{margin:0;padding:0;box-sizing:border-box}
html,body{margin:0;width:1080px;height:1920px;overflow:hidden;background:var(--green-900)}
#root{position:relative;width:100%;height:100%;font-family:"Montserrat",sans-serif;color:var(--cream);
 background:radial-gradient(120% 80% at 50% 35%,var(--green-700) 0%,var(--green-800) 45%,var(--green-900) 100%);overflow:hidden}
.frame{position:absolute;inset:40px;border:3px solid rgba(217,178,76,.35);border-radius:28px;pointer-events:none}
.clip{position:absolute;inset:0}
.scene{display:flex;flex-direction:column;justify-content:flex-start;align-items:center;padding:0 90px;text-align:center}
.anton{font-family:"Anton","Montserrat",sans-serif;font-weight:400;text-transform:uppercase;letter-spacing:.01em}
.gold{color:var(--gold)}
.goldl{color:var(--gold-light)}
/* gancho */
#hook{padding-top:200px}
#hook .pill{font-weight:900;font-size:44px;letter-spacing:.16em;color:var(--green-900);background:var(--gold);
 padding:14px 34px;border-radius:999px;margin-bottom:46px;display:flex;align-items:center;gap:14px}
#hook .pill.red{background:var(--red);color:var(--cream)}
#hook .h{line-height:1.13;color:var(--cream);text-shadow:0 8px 0 rgba(0,0,0,.35)}
#hook .w{display:inline-block}
#hook .w.hl{color:var(--gold)}
#flash{position:absolute;inset:0;background:var(--cream);opacity:0;pointer-events:none}
/* CTA */
#cta{padding-top:230px}
#cta .lead{font-size:120px;line-height:1}
#cta .word{margin:44px 0;line-height:1;color:var(--green-900);background:var(--gold);padding:30px 64px 20px;border-radius:34px;
 box-shadow:0 0 0 10px rgba(217,178,76,.25),0 20px 60px rgba(0,0,0,.5);white-space:nowrap}
#cta .tail{font-weight:900;font-size:72px;line-height:1.12;color:var(--cream)}
#cta .bubble{align-self:flex-end;margin:60px 60px 0 0;width:150px;height:150px}
/* cowboy */
#cowboy-layer{pointer-events:none}
#cowboy{position:absolute;left:20px;bottom:-50px;width:560px;height:646px;overflow:visible}
.say{position:absolute;left:600px;top:1390px;max-width:420px;background:var(--cream);color:var(--green-900);font-weight:900;
 font-size:50px;line-height:1.08;padding:26px 34px;border-radius:34px;border:5px solid var(--gold);
 box-shadow:0 14px 34px rgba(0,0,0,.45);transform-origin:10% 100%}
.say::after{content:"";position:absolute;left:30px;bottom:-40px;border-width:40px 34px 0 0;border-style:solid;
 border-color:var(--gold) transparent transparent transparent}
/* progresso */
#progress{position:absolute;left:90px;right:90px;top:auto;bottom:70px;height:12px;border-radius:8px;background:rgba(246,241,227,.12);overflow:hidden}
#progress .fill{width:100%;height:100%;background:var(--gold);transform-origin:left center}
"""

BASE_JS = """
const tl = gsap.timeline({ paused: true });
const SHOULDER = "392 440", HEAD = "260 300";
tl.fromTo("#progress .fill", { scaleX: 0 }, { scaleX: 1, duration: 15, ease: "none" }, 0);

// gancho: palavras batendo + flash + tremida
tl.fromTo("#flash", { opacity: 0.85 }, { opacity: 0, duration: 0.35, ease: "power2.out" }, 0);
tl.fromTo("#hook .pill", { opacity: 0, y: -60, scale: 0.6 }, { opacity: 1, y: 0, scale: 1, duration: 0.28, ease: "back.out(2.5)" }, 0);
tl.fromTo("#hook .w", { opacity: 0, scale: 2.4, y: -20 }, { opacity: 1, scale: 1, y: 0, duration: 0.2, stagger: HOOK_STAGGER, ease: "power4.out" }, 0.08);
const HOOK_END = 0.08 + HOOK_STAGGER * (document.querySelectorAll("#hook .w").length - 1) + 0.2;
tl.to("#hook .h", { x: 14, duration: 0.04, ease: "none" }, HOOK_END);
tl.to("#hook .h", { x: -12, duration: 0.05, ease: "none" }, HOOK_END + 0.04);
tl.to("#hook .h", { x: 6, duration: 0.05, ease: "none" }, HOOK_END + 0.09);
tl.to("#hook .h", { x: 0, duration: 0.05, ease: "none" }, HOOK_END + 0.14);
tl.to("#hook .h .hl", { scale: 1.08, duration: 0.5, ease: "sine.inOut" }, HOOK_END + 0.2);
tl.to("#hook", { opacity: 0, scale: 0.9, duration: 0.18, ease: "power2.in" }, 2.08);

// cowboy
tl.fromTo("#cowboy", { y: 700 }, { y: 0, duration: 0.45, ease: "back.out(1.6)" }, 0.75);
tl.fromTo("#cb-arm", { rotation: 85, svgOrigin: SHOULDER }, { rotation: 85, svgOrigin: SHOULDER, duration: 0.01 }, 0);
tl.fromTo("#cb-all", { y: 0 }, { y: -8, duration: 0.6, repeat: 22, yoyo: true, ease: "sine.inOut" }, 1.2);
[1.9, 4.6, 7.2, 9.9, 13.1].forEach((t) => {
  tl.to("#cb-eyes", { scaleY: 0.1, svgOrigin: "260 254", duration: 0.06, ease: "none" }, t);
  tl.to("#cb-eyes", { scaleY: 1, svgOrigin: "260 254", duration: 0.08, ease: "none" }, t + 0.06);
});
function point(t, a) {
  tl.to("#cb-arm", { rotation: a, svgOrigin: SHOULDER, duration: 0.3, ease: "back.out(2)" }, t);
  tl.to("#cb-arm", { rotation: a - 5, svgOrigin: SHOULDER, duration: 0.1, ease: "power1.out" }, t + 0.35);
  tl.to("#cb-arm", { rotation: a, svgOrigin: SHOULDER, duration: 0.15, ease: "power1.in" }, t + 0.45);
}
function armDown(t) { tl.to("#cb-arm", { rotation: 85, svgOrigin: SHOULDER, duration: 0.25, ease: "power2.in" }, t); }
function shakeNo(t) {
  [9, -9, 7, -4, 0].forEach((r, i) => tl.to("#cb-head", { rotation: r, svgOrigin: HEAD, duration: 0.12, ease: "sine.inOut" }, t + i * 0.12));
}
function nodYes(t) {
  [12, 0, 10, 0].forEach((y, i) => tl.to("#cb-head", { y: y, duration: 0.12, ease: "sine.inOut" }, t + i * 0.12));
}
function mood(t, m) {
  const sad = m === "sad" ? 1 : 0;
  tl.to("#mouth-sad", { opacity: sad, duration: 0.1 }, t);
  tl.to("#brows-sad", { opacity: sad, duration: 0.1 }, t);
  tl.to("#sweat", { opacity: sad, duration: 0.15 }, t);
  tl.to("#mouth-happy", { opacity: 1 - sad, duration: 0.1 }, t);
  tl.to("#brows-happy", { opacity: 1 - sad, duration: 0.1 }, t);
}
function say(sel, a, b) {
  tl.fromTo(sel, { opacity: 0, scale: 0.3 }, { opacity: 1, scale: 1, duration: 0.25, ease: "back.out(2.5)" }, a);
  if (b < 15) tl.to(sel, { opacity: 0, scale: 0.6, duration: 0.15, ease: "power2.in" }, b);
}
function stamp(sel, t) {
  tl.fromTo(sel, { opacity: 0, scale: 3, rotation: -30 }, { opacity: 1, scale: 1, rotation: 0, duration: 0.28, ease: "back.out(2.5)" }, t);
}
function jolt(sel, t) {
  [10, -10, 6, 0].forEach((x, i) => tl.to(sel, { x: x, duration: 0.05, ease: "none" }, t + i * 0.05));
}

// CTA (11.5–15s)
tl.fromTo("#cta .lead", { opacity: 0, y: 70 }, { opacity: 1, y: 0, duration: 0.3, ease: "power3.out" }, 11.55);
tl.fromTo("#cta .word", { opacity: 0, scale: 0.2, rotation: -8 }, { opacity: 1, scale: 1, rotation: 0, duration: 0.45, ease: "back.out(2)" }, 11.7);
tl.fromTo("#cta .tail", { opacity: 0, y: 50 }, { opacity: 1, y: 0, duration: 0.3, ease: "power3.out" }, 12.05);
tl.fromTo("#cta .bubble", { opacity: 0, scale: 0 }, { opacity: 1, scale: 1, duration: 0.35, ease: "back.out(3)" }, 12.3);
[12.8, 13.6, 14.4].forEach((t) => {
  tl.to("#cta .word", { scale: 1.08, duration: 0.15, ease: "power2.out" }, t);
  tl.to("#cta .word", { scale: 1, duration: 0.25, ease: "power2.in" }, t + 0.15);
  tl.to("#cta .bubble", { y: -18, duration: 0.15, ease: "power2.out" }, t + 0.05);
  tl.to("#cta .bubble", { y: 0, duration: 0.2, ease: "power2.in" }, t + 0.2);
});
tl.to("#cb-hat", { rotation: -18, y: -40, svgOrigin: "260 186", duration: 0.3, ease: "back.out(2)" }, 13.9);
"""


def hook_html(pill, lines, size, pill_red=False, pill_icon=None, extra=""):
    """lines: lista de linhas; palavras com *asterisco* viram douradas."""
    out = []
    for line in lines:
        ws = []
        for w in line.split():
            hl = w.startswith("*")
            ws.append(f'<span class="w{" hl" if hl else ""}">{w.strip("*")}</span>')
        out.append('<div class="hl-line">' + " ".join(ws) + "</div>")
    ic = icon(pill_icon, "#f6f1e3" if pill_red else "#06190f", 44, 6) if pill_icon else ""
    return (f'<section id="hook" class="clip scene" data-start="0" data-duration="2.3" data-track-index="0">'
            f'<div class="pill{" red" if pill_red else ""}">{ic}{pill}</div>'
            f'<div class="h anton" style="font-size:{size}px">{"".join(out)}</div>{extra}</section>')


def cta_html(word, tail_html, word_size=200):
    return (f'<section id="cta" class="clip scene" data-start="11.5" data-duration="3.5" data-track-index="2">'
            f'<div class="lead anton">Comenta</div><div class="word anton" style="font-size:{word_size}px">{word}</div>'
            f'<div class="tail">{tail_html}</div>'
            '<svg class="bubble" viewBox="0 0 24 24" fill="none" stroke="#d9b24c" stroke-width="2" stroke-linejoin="round">'
            '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20.5l1.4-4.6A8 8 0 1 1 21 12z" /></svg></section>')


def build(slug, title, hook, body_html, body_css, body_js, cta, says, hook_stagger=0.09):
    """says: lista de (texto, entra, sai)."""
    say_html = "".join(f'<div class="say" id="say{i}">{t}</div>' for i, (t, a, b) in enumerate(says))
    say_js = "".join(f'say("#say{i}", {a}, {b});\n' for i, (t, a, b) in enumerate(says))
    html = f"""<!doctype html>
<html lang="pt-BR" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>{title}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link href="https://fonts.googleapis.com/css2?family=Anton&family=Montserrat:wght@700;800;900&display=block" rel="stylesheet" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>{BASE_CSS}{body_css}</style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="15" data-width="1080" data-height="1920">
      <div class="frame"></div>
      {hook}
      <section id="body" class="clip scene" data-start="2.2" data-duration="9.4" data-track-index="1">{body_html}</section>
      {cta}
      <div id="cowboy-layer" class="clip" data-start="0" data-duration="15" data-track-index="4">{COWBOY}{say_html}</div>
      <div id="progress" class="clip" data-start="0" data-duration="15" data-track-index="3"><div class="fill"></div></div>
      <div id="flash" class="clip" data-start="0" data-duration="0.5" data-track-index="5"></div>
    </div>
    <script>
const HOOK_STAGGER = {hook_stagger};
{BASE_JS}
{say_js}
// ---------- corpo ----------
tl.fromTo("#body", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.15 }}, 2.2);
tl.to("#body", {{ opacity: 0, y: -80, duration: 0.25, ease: "power2.in" }}, 11.35);
{body_js}
window.__timelines = window.__timelines || {{}};
window.__timelines["main"] = tl;
tl.seek(0);
    </script>
  </body>
</html>
"""
    d = os.path.join(HERE, slug)
    os.makedirs(d, exist_ok=True)
    for f in ("hyperframes.json", "package.json"):
        shutil.copy(os.path.join(TEMPLATE, f), d)
    json.dump({"id": slug, "name": title}, open(os.path.join(d, "meta.json"), "w"))
    open(os.path.join(d, "index.html"), "w").write(html)
    return d
