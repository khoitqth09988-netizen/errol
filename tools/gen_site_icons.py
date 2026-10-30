#!/usr/bin/env python3
"""Generate site identity assets: favicon set (SVG + PNGs), apple-touch icon,
web-app manifest icons, and the 1200x630 Open Graph share cover.

Outputs go to media/ (except manifest.json at repo root).
All PNGs are rendered from a shared 4x-supersampled PIL master so the caret
eyes ("^^", Tiny's face) match across sizes.
"""
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA = os.path.join(ROOT, "media")
os.makedirs(MEDIA, exist_ok=True)

SS = 4  # supersample factor
CYAN_GLOW = (18, 245, 255)      # #12f5ff
CYAN_CORE = (201, 246, 255)     # #c9f6ff
PINK = (255, 127, 176)          # #ff7fb0
BG_TOP = (13, 20, 32)           # #0d1420
BG_BOTTOM = (5, 7, 10)          # #05070a

# caret eyes as polylines in a 64-unit grid (viewBox of the SVG icon)
EYES = [
    [(13, 41), (21.5, 28), (30, 41)],
    [(34, 41), (42.5, 28), (51, 41)],
]
HEART = [(55.5, 19.4), (52.4, 15.6), (53.2, 13.0), (55.5, 15.1), (57.8, 13.0), (58.6, 15.6)]


def write_favicon_svg():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#0d1420"/>
      <stop offset="1" stop-color="#05070a"/>
    </linearGradient>
    <radialGradient id="halo" cx="50%" cy="46%" r="58%">
      <stop offset="0" stop-color="#12f5ff" stop-opacity=".30"/>
      <stop offset="1" stop-color="#12f5ff" stop-opacity="0"/>
    </radialGradient>
    <filter id="blur" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="1.7"/>
    </filter>
  </defs>
  <rect width="64" height="64" rx="14" fill="url(#bg)"/>
  <rect width="64" height="64" rx="14" fill="url(#halo)"/>
  <g fill="none" stroke="#12f5ff" stroke-width="5.4" stroke-linecap="round"
     stroke-linejoin="round" filter="url(#blur)">
    <path d="M13 41 L21.5 28 L30 41"/>
    <path d="M34 41 L42.5 28 L51 41"/>
  </g>
  <g fill="none" stroke="#c9f6ff" stroke-width="3.8" stroke-linecap="round"
     stroke-linejoin="round">
    <path d="M13 41 L21.5 28 L30 41"/>
    <path d="M34 41 L42.5 28 L51 41"/>
  </g>
  <path d="M55.5 19.4 C52.4 15.6 52.4 13.2 54.2 12.7 C55.1 12.5 55.5 13.1 55.5 13.6
           C55.5 13.1 55.9 12.5 56.8 12.7 C58.6 13.2 58.6 15.6 55.5 19.4 Z" fill="#ff7fb0"/>
</svg>
"""
    p = os.path.join(MEDIA, "favicon.svg")
    open(p, "w", encoding="utf-8").write(svg)
    print("wrote", p)


def render_master(size=512):
    """Render one icon master at SS*size, caller downsamples."""
    S = size * SS
    im = Image.new("RGBA", (S, S), (0, 0, 0, 255))
    d = ImageDraw.Draw(im)
    # vertical gradient background
    for y in range(S):
        t = y / (S - 1)
        r = int(BG_TOP[0] + (BG_BOTTOM[0] - BG_TOP[0]) * t)
        g = int(BG_TOP[1] + (BG_BOTTOM[1] - BG_TOP[1]) * t)
        b = int(BG_TOP[2] + (BG_BOTTOM[2] - BG_TOP[2]) * t)
        d.line([(0, y), (S, y)], fill=(r, g, b, 255))
    # radial cyan halo (cheap: blur a filled ellipse)
    halo = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    hd = ImageDraw.Draw(halo)
    m = int(S * 0.06)
    hd.ellipse([m, int(S * 0.10), S - m, int(S * 0.86)],
               fill=(CYAN_GLOW[0], CYAN_GLOW[1], CYAN_GLOW[2], 74))
    halo = halo.filter(ImageFilter.GaussianBlur(S // 8))
    im.alpha_composite(halo)
    return im


def draw_face(im, pad_ratio=0.0, scale=1.0, cx=0.5, cy=0.5, glow=True, heart=True):
    """Draw caret eyes (+ heart) scaled from the 64-unit design onto im."""
    S = im.width
    unit = S / 64.0 * scale
    ox = S * cx - unit * 32
    oy = S * cy - unit * 32
    def P(x, y):
        return (ox + x * unit, oy + y * unit)

    d = ImageDraw.Draw(im)
    w_core = max(2, int(unit * 3.8))
    w_glow = max(4, int(unit * 5.6))

    if glow:
        gl = Image.new("RGBA", im.size, (0, 0, 0, 0))
        gd = ImageDraw.Draw(gl)
        for poly in EYES:
            pts = [P(*p) for p in poly]
            gd.line(pts, fill=(*CYAN_GLOW, 190), width=w_glow, joint="curve")
            for x, y in pts:
                r = w_glow / 2
                gd.ellipse([x - r, y - r, x + r, y + r], fill=(*CYAN_GLOW, 190))
        gl = gl.filter(ImageFilter.GaussianBlur(max(2, int(unit * 1.6))))
        im.alpha_composite(gl)
        d = ImageDraw.Draw(im)

    for poly in EYES:
        pts = [P(*p) for p in poly]
        d.line(pts, fill=(*CYAN_CORE, 255), width=w_core, joint="curve")
        for x, y in pts:
            r = w_core / 2
            d.ellipse([x - r, y - r, x + r, y + r], fill=(*CYAN_CORE, 255))

    if heart:
        hp = [P(*p) for p in HEART]
        hp.append(hp[0])
        d.polygon(hp, fill=(*PINK, 235))


def rounded_mask(size, radius_ratio=0.22):
    m = Image.new("L", (size, size), 0)
    md = ImageDraw.Draw(m)
    r = int(size * radius_ratio)
    md.rounded_rectangle([0, 0, size - 1, size - 1], radius=r, fill=255)
    return m


def make_icon(size, out, maskable=False, radius_ratio=0.22, scale=1.0):
    master = render_master(size)
    draw_face(master, scale=scale, cx=0.5, cy=0.485)
    small = master.resize((size, size), Image.LANCZOS)
    if not maskable:
        rgba = small.convert("RGBA")
        alpha = rounded_mask(size, radius_ratio)
        base = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        base.paste(rgba, (0, 0), alpha)
        small = base
    small.save(out)
    print("wrote", out, small.size)


def fit_font(path, text, max_px, max_w):
    """Largest font size <= max_px whose text fits max_w."""
    size = max_px
    while size > 12:
        f = ImageFont.truetype(path, size)
        if f.getbbox(text)[2] - f.getbbox(text)[0] <= max_w:
            return f
        size -= 2
    return ImageFont.truetype(path, 12)


def make_og_cover(w=1200, h=630):
    im = Image.new("RGBA", (w, h), (0, 0, 0, 255))
    d = ImageDraw.Draw(im)
    for y in range(h):
        t = y / (h - 1)
        r = int(9 + 4 * t); g = int(12 + 3 * t); b = int(18 + 4 * t)
        d.line([(0, y), (w, y)], fill=(r, g, b, 255))
    for (cx, cy, rx, ry, col, a) in [
        (int(w * 0.12), int(h * 0.85), int(w * 0.45), int(h * 0.75), (255, 118, 148), 34),
        (int(w * 0.94), int(h * 0.30), int(w * 0.40), int(h * 0.80), (138, 213, 255), 30),
        (int(w * 0.21), int(h * 0.52), int(w * 0.22), int(h * 0.55), (18, 245, 255), 30),
    ]:
        glow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        gd = ImageDraw.Draw(glow)
        gd.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=(*col, a))
        glow = glow.filter(ImageFilter.GaussianBlur(90))
        im.alpha_composite(glow)

    d = ImageDraw.Draw(im)
    import math
    for i, (sx, sy, ss) in enumerate([(930, 80, 7), (770, 130, 5), (215, 110, 5),
                                      (620, 560, 5), (1085, 545, 6), (470, 85, 4),
                                      (1150, 300, 5), (150, 520, 4)]):
        tw = 0.6 + 0.4 * math.sin(i * 1.7)
        s = ss * tw
        c = (240, 250, 255, 225)
        d.line([(sx - s, sy), (sx + s, sy)], fill=c, width=2)
        d.line([(sx, sy - s), (sx, sy + s)], fill=c, width=2)

    # big caret eyes, left side
    unit = 9.4
    def P(x, y):
        return (250 + (x - 32) * unit, 330 + (y - 32) * unit)
    gl = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    gd = ImageDraw.Draw(gl)
    core = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    cd = ImageDraw.Draw(core)
    for poly in EYES:
        pts = [P(*p) for p in poly]
        gd.line(pts, fill=(*CYAN_GLOW, 210), width=int(unit * 6.4), joint="curve")
        for x, y in pts:
            r = unit * 3.2
            gd.ellipse([x - r, y - r, x + r, y + r], fill=(*CYAN_GLOW, 210))
    gl = gl.filter(ImageFilter.GaussianBlur(16))
    im.alpha_composite(gl)
    for poly in EYES:
        pts = [P(*p) for p in poly]
        cd.line(pts, fill=(*CYAN_CORE, 255), width=int(unit * 4.0), joint="curve")
        for x, y in pts:
            r = unit * 2.0
            cd.ellipse([x - r, y - r, x + r, y + r], fill=(*CYAN_CORE, 255))
    im.alpha_composite(core)

    # right-hand text block, auto-fitted so nothing clips
    bold = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    regular = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    x = 520
    max_w = w - 40 - x
    lines = [
        ("Sự thức giấc của Tiny", bold, 58, (234, 247, 255, 255), 190),
        ("Ngày 20 · 10", bold, 44, (156, 255, 255, 255), 288),
        ("Một khu vườn nhỏ gửi tới cậu những lời chúc", regular, 29, (255, 176, 208, 240), 380),
        ("và một Tiny luôn ở bên cạnh.", regular, 29, (166, 232, 255, 240), 424),
    ]
    d = ImageDraw.Draw(im)
    for text, font_path, size, fill, y in lines:
        f = fit_font(font_path, text, size, max_w)
        d.text((x, y), text, font=f, fill=fill)

    d.rectangle([18, 18, w - 19, h - 19], outline=(120, 220, 255, 70), width=2)

    out = os.path.join(MEDIA, "og-cover.png")
    im.convert("RGB").save(out, optimize=True)
    print("wrote", out, im.size)


def make_manifest():
    import json
    manifest = {
        "name": "Sự thức giấc của Tiny - Ngày 20/10",
        "short_name": "Tiny",
        "description": "Khu vườn ước mơ nhỏ của Tiny: lời chúc, âm nhạc và những chuyển cảnh 20/10.",
        "lang": "vi",
        "dir": "ltr",
        "start_url": "./",
        "scope": "./",
        "display": "standalone",
        "orientation": "portrait",
        "background_color": "#000000",
        "theme_color": "#000000",
        "icons": [
            {"src": "media/favicon-32.png", "sizes": "32x32", "type": "image/png", "purpose": "any"},
            {"src": "media/icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
            {"src": "media/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
            {"src": "media/icon-512-maskable.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
            {"src": "media/apple-touch-icon.png", "sizes": "180x180", "type": "image/png", "purpose": "any"},
        ],
    }
    p = os.path.join(ROOT, "manifest.json")
    open(p, "w", encoding="utf-8").write(json.dumps(manifest, ensure_ascii=False, indent=2))
    print("wrote", p)


if __name__ == "__main__":
    write_favicon_svg()
    make_icon(32, os.path.join(MEDIA, "favicon-32.png"))
    make_icon(16, os.path.join(MEDIA, "favicon-16.png"))
    make_icon(192, os.path.join(MEDIA, "icon-192.png"))
    make_icon(512, os.path.join(MEDIA, "icon-512.png"))
    make_icon(512, os.path.join(MEDIA, "icon-512-maskable.png"), maskable=True, scale=0.78)
    make_icon(180, os.path.join(MEDIA, "apple-touch-icon.png"), maskable=True, scale=0.86)
    make_og_cover()
    make_manifest()
