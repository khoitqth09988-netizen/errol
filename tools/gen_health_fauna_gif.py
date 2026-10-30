#!/usr/bin/env python3
"""Generate real animated GIFs (bird + butterfly) for the Health scene of index.html.

Outputs (into media/):
  media/health-bird.gif          160x80, 10 frames, 93ms  (flap cycle ~0.93s)
  media/health-butterfly.gif     140x124, 8 frames, 102ms (flap cycle ~0.82s)
  media/health-bird-static.png   first/mid frame for prefers-reduced-motion
  media/health-butterfly-static.png
"""
import base64, io, math, os
from PIL import Image, ImageDraw

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "media")
SS = 4  # supersample factor
os.makedirs(OUT, exist_ok=True)

def lerp(a, b, t): return a + (b - a) * t
def smooth(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)

def bez2(p0, p1, p2, n=28):
    pts = []
    for i in range(n + 1):
        t = i / n; u = 1 - t
        pts.append((u*u*p0[0] + 2*u*t*p1[0] + t*t*p2[0],
                    u*u*p0[1] + 2*u*t*p1[1] + t*t*p2[1]))
    return pts

def bez3(p0, p1, p2, p3, n=36):
    pts = []
    for i in range(n + 1):
        t = i / n; u = 1 - t
        pts.append((u*u*u*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t*t*t*p3[0],
                    u*u*u*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t*t*t*p3[1]))
    return pts

def stroke(draw, pts, color, w):
    draw.line(pts, fill=color, width=int(round(w)), joint="curve")
    r = w / 2.0
    for x, y in (pts[0], pts[-1]):
        draw.ellipse([x - r, y - r, x + r, y + r], fill=color)

def to_frames(rgba_frames, path, durations):
    pframes = []
    for im in rgba_frames:
        alpha = im.getchannel("A")
        p = im.convert("RGB").convert("P", palette=Image.ADAPTIVE, colors=255)
        # Paint index 255 (the GIF transparency key) where the source is
        # EMPTY — mask must mark background, not sprite, or the GIF inverts.
        mask = alpha.point(lambda v: 255 if v <= 127 else 0).convert("1")
        p.paste(255, mask)
        pframes.append(p)
    pframes[0].save(
        path, save_all=True, append_images=pframes[1:], duration=durations,
        loop=0, transparency=255, disposal=2, optimize=False,
    )
    return pframes

# ---------------------------------------------------------------- bird ----
def bird_frame(i, n):
    """Front-view sparrow, wings flapping; mirrors the original SVG geometry
    (viewBox 0 0 90 45) with animated control/tip points."""
    W, H = 160 * SS, 80 * SS
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    S = W / 90.0                      # viewBox units -> pixels (45*7.111=320)
    phase = 2 * math.pi * i / n
    flap = math.sin(phase)            # -1 wings up .. +1 wings down
    bob = 1.8 * flap                  # body follows the stroke a little
    off = 3.0 + bob                   # keep everything inside the canvas
    def P(x, y): return (x * S, (y + off) * S)

    wing = (136, 172, 194, 255)       # rgba(189,224,243,.68) baked over black
    body = (112, 146, 168, 255)       # body path at .6 opacity
    w = 2.2 * S                       # stroke-width 2.2

    ctrl_y = 6 + 7 * flap
    tip_y  = 18 + 12 * flap
    # left wing  M45 28 Q(27,cy) (4,ty)
    stroke(d, bez2(P(45, 28), P(27, ctrl_y), P(4, tip_y)), wing, w)
    # right wing M45 28 Q(63,cy) (86,ty)  (mirrored)
    stroke(d, bez2(P(45, 28), P(63, ctrl_y), P(86, tip_y)), wing, w)
    # tail/body  M41 26 Q45 30 49 26
    stroke(d, bez2(P(41, 26), P(45, 30), P(49, 26)), body, w)

    return im.resize((160, 80), Image.LANCZOS)

# ----------------------------------------------------------- butterfly ----
def butterfly_frame(i, n):
    """Pink butterfly; left/right wing groups scale horizontally about x=44
    (same .43 -> 1 motion as the old CSS keyframes). viewBox 0 0 88 78."""
    FW, FH = 140, 124
    W, H = FW * SS, FH * SS
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    S = W / 88.0
    p = i / n
    # wing flap: .43 -> 1 peaking at 55% of the cycle, smooth both ends
    if p <= 0.55:
        s = lerp(0.43, 1.0, smooth(p / 0.55))
    else:
        s = lerp(1.0, 0.43, smooth((p - 0.55) / 0.45))

    def LX(x): return 44 - (44 - x) * s   # squeeze about center
    def RX(x): return 44 + (x - 44) * s
    def P(x, y): return (x * S, y * S)

    stroke_c = (222, 184, 204, 255)   # rgba(255,211,234,.87) over black
    fill_c   = (36, 22, 30, 255)      # rgba(255,155,213,.14) over black
    body_c   = (216, 207, 255, 255)   # #d8cfff
    wsw = 1.6 * S
    bw = 2.3 * S

    # left wing:  M44 39 C17 6 1 17 20 43 C1 59 22 73 44 42 Z
    lw = bez3(P(44, 39), P(LX(17), 6), P(LX(1), 17), P(LX(20), 43)) + \
         bez3(P(LX(20), 43), P(LX(1), 59), P(LX(22), 73), P(LX(44), 42))[1:]
    # right wing (mirrored control points, same as the original path)
    rw = bez3(P(44, 39), P(RX(71), 6), P(RX(87), 17), P(RX(68), 43)) + \
         bez3(P(RX(68), 43), P(RX(87), 59), P(RX(66), 73), P(RX(44), 42))[1:]

    for wing in (lw, rw):
        d.polygon(wing, fill=fill_c)
        stroke(d, wing + [wing[0]], stroke_c, wsw)

    # body + antennae:  M44 30 Q47 42 44 55 / M44 30 L36 23 / M44 30 L52 23
    stroke(d, bez2(P(44, 30), P(47, 42), P(44, 55)), body_c, bw)
    stroke(d, [P(44, 30), P(36, 23)], body_c, bw)
    stroke(d, [P(44, 30), P(52, 23)], body_c, bw)

    return im.resize((FW, FH), Image.LANCZOS)

if __name__ == "__main__":
    # bird: 12 frames x 80ms ~= 0.96s flap (matches old tinyWings timing).
    # 12 avoids consecutive-identical sin() frames that PIL would merge.
    n_b = 12
    bird_frames = [bird_frame(i, n_b) for i in range(n_b)]
    bio = io.BytesIO()
    to_frames(bird_frames, os.path.join(OUT, "health-bird.gif"), [80] * n_b)
    with open(os.path.join(OUT, "health-bird.gif"), "rb") as f:
        bird_bytes = f.read()
    bird_frames[0].save(os.path.join(OUT, "health-bird-static.png"))

    # butterfly: 8 frames x 100ms ~= 0.80s flap (matches old keyframes)
    n_f = 8
    but_frames = [butterfly_frame(i, n_f) for i in range(n_f)]
    to_frames(but_frames, os.path.join(OUT, "health-butterfly.gif"), [100] * n_f)
    with open(os.path.join(OUT, "health-butterfly.gif"), "rb") as f:
        but_bytes = f.read()
    but_frames[n_f // 2].save(os.path.join(OUT, "health-butterfly-static.png"))


    # sanity: reload and count frames
    g = Image.open(os.path.join(OUT, "health-bird.gif"))
    print("bird frames:", getattr(g, "n_frames", 1), g.size)
    g2 = Image.open(os.path.join(OUT, "health-butterfly.gif"))
    print("butterfly frames:", getattr(g2, "n_frames", 1), g2.size)
