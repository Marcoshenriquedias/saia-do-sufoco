"""Efeitos sonoros sintetizados (determinísticos, sem bancos de som externos)."""
import wave

import numpy as np

SR = 44100
RNG = np.random.default_rng(7)


def _t(d):
    return np.arange(int(SR * d)) / SR


def _lowpass_sweep(x, f0, f1):
    """Passa-baixa de 1 polo com corte variando de f0 a f1 (Hz)."""
    n = len(x)
    fc = np.geomspace(f0, f1, n)
    a = 1 - np.exp(-2 * np.pi * fc / SR)
    y = np.empty(n)
    acc = 0.0
    for i in range(n):
        acc += a[i] * (x[i] - acc)
        y[i] = acc
    return y


def whoosh(d=0.35, lo=300, hi=5000):
    n = int(SR * d)
    noise = RNG.standard_normal(n)
    half = n // 2
    y = np.concatenate([_lowpass_sweep(noise[:half], lo, hi), _lowpass_sweep(noise[half:], hi, lo)])
    env = np.sin(np.linspace(0, np.pi, n)) ** 2
    return y * env * 0.9


def thud(d=0.45):
    t = _t(d)
    f = 45 + 110 * np.exp(-t * 18)
    ph = 2 * np.pi * np.cumsum(f) / SR
    body = np.sin(ph) * np.exp(-t * 7)
    click = RNG.standard_normal(len(t)) * np.exp(-t * 180) * 0.6
    return np.tanh((body + click) * 2.2) * 0.9


def stamp():
    t = _t(0.3)
    crack = _lowpass_sweep(RNG.standard_normal(len(t)), 4000, 600) * np.exp(-t * 30) * 1.4
    out = thud(0.45)
    out[: len(crack)] += crack
    return out * 0.9


def ding(f=1318.5, d=1.1):
    t = _t(d)
    y = sum(a * np.sin(2 * np.pi * f * k * t) * np.exp(-t * (3 + k * 2)) for k, a in ((1, 1), (2, 0.4), (3, 0.18), (4.2, 0.1)))
    y *= np.minimum(1, t * 400)
    return y * 0.45


def sparkle():
    out = np.zeros(int(SR * 0.6))
    for i, f in enumerate((2093, 2637, 3136, 4186)):
        s = ding(f, 0.45) * 0.5
        o = int(SR * i * 0.05)
        out[o:o + len(s)] += s[: len(out) - o]
    return out


def pop(f0=500, f1=1100, d=0.09):
    t = _t(d)
    f = np.linspace(f0, f1, len(t))
    y = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.sin(np.linspace(0, np.pi, len(t)))
    return y * 0.6


def tock():
    t = _t(0.07)
    return np.sin(2 * np.pi * 900 * t) * np.exp(-t * 70) * 0.45


def tick():
    t = _t(0.03)
    return np.sin(2 * np.pi * 2200 * t) * np.exp(-t * 200) * 0.3


def riser(d=0.7):
    n = int(SR * d)
    y = _lowpass_sweep(RNG.standard_normal(n), 200, 8000) * np.linspace(0, 1, n) ** 2
    t = _t(d)
    y += np.sin(2 * np.pi * np.cumsum(np.linspace(200, 900, n)) / SR) * np.linspace(0, 0.4, n)
    return y * 0.6


def bad():
    """Buzzer de erro (duas notas descendo)."""
    t = _t(0.38)
    f = np.where(t < 0.16, 330, 220)
    y = np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)) * 0.25
    return _lowpass_sweep(y, 2500, 1200) * np.exp(-t * 3)


def good():
    out = np.zeros(int(SR * 0.6))
    for i, f in enumerate((784, 1175)):
        s = ding(f, 0.5) * 0.7
        o = int(SR * i * 0.09)
        out[o:o + len(s)] += s[: len(out) - o]
    return out


SOUNDS = {
    "whoosh": (whoosh, 0.55),
    "swish": (lambda: whoosh(0.5, 200, 7000), 0.6),
    "thud": (thud, 0.9),
    "stamp": (stamp, 1.0),
    "ding": (ding, 0.7),
    "sparkle": (sparkle, 0.55),
    "pop": (pop, 0.45),
    "tock": (tock, 0.5),
    "tick": (tick, 0.5),
    "riser": (riser, 0.5),
    "bad": (bad, 0.7),
    "good": (good, 0.7),
}


def render(events, path, dur=15.0):
    """events: lista de (tempo_s, nome[, ganho]). Grava WAV estéreo 16-bit."""
    mix = np.zeros(int(SR * dur) + SR)
    cache = {}
    for ev in events:
        t, name = ev[0], ev[1]
        g = ev[2] if len(ev) > 2 else 1.0
        if name not in cache:
            fn, vol = SOUNDS[name]
            cache[name] = fn() * vol
        s = cache[name] * g
        o = max(0, int(SR * t))
        end = min(len(mix), o + len(s))
        mix[o:end] += s[: end - o]
    mix = mix[: int(SR * dur)]
    peak = np.max(np.abs(mix)) or 1
    mix = np.tanh(mix / peak * 1.1) * 0.89
    pcm = (np.clip(mix, -1, 1) * 32767).astype(np.int16)
    st = np.repeat(pcm[:, None], 2, axis=1)
    with wave.open(path, "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(st.tobytes())
