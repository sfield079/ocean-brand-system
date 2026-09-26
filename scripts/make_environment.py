"""Build the Ocean environment backgrounds from the nine colour-place photographs.

Guide 04 grounds every colour in a place (Blackmoss = ocean rapids, Peacock = misty
forested hills, Cedar = forest canopy, Sage = alpine lake, Honeydew = sky and sea,
Sprig = shallow water over sand, Olive = olive grove, Citron = sun rays through forest,
Crimson = red earth). Guide 07 allows "designated harmonies of brand colors to overlay
or gradient map imagery alongside unaltered photography".

Outputs in assets/environments/:
  env_<colour>_map_dark.jpg   full-bleed gradient map, field -> darker tone (use with a light ink)
  env_<colour>_map_light.jpg  full-bleed gradient map, field -> lighter tone (use with a dark ink)
  env_<colour>_strip.jpg      the photograph with a light field-colour overlay (palette-card strip)

The maps stay within about 1.5:1 contrast of the field (decisions.md Part 5 allows up to
1.8:1 behind text) and fade toward the flat field on the left, where titles sit.
"""
import json
from pathlib import Path

from PIL import Image, ImageOps, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / 'assets/environments/source'
OUT = ROOT / 'assets/environments'
TOK = json.loads((ROOT / 'tokens/ocean.tokens.json').read_text())
COL = {k: v['value'] for k, v in TOK['color'].items() if k != 'white'}
SIZE = (2400, 1350)
TARGET = 1.5


def rgb(h): return tuple(int(h.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))


def lum(c):
    f = [x / 255 for x in c]
    f = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in f]
    return 0.2126 * f[0] + 0.7152 * f[1] + 0.0722 * f[2]


def ratio(a, b):
    la, lb = sorted([lum(a), lum(b)])
    return (lb + 0.05) / (la + 0.05)


def mix(a, b, t): return tuple(round(x + (y - x) * t) for x, y in zip(a, b))


def partner(field, toward):
    """Tone of the field moved toward black/white until it reaches the contrast target."""
    t = 0.0
    while t < 1 and ratio(field, mix(field, toward, t)) < TARGET:
        t += 0.01
    return mix(field, toward, t)


def cover_crop(im, size):
    return ImageOps.fit(im, size, Image.LANCZOS, centering=(0.5, 0.5))


def gradient_map(photo, a, b):
    g = ImageOps.autocontrast(photo.convert('L'), cutoff=2).filter(ImageFilter.GaussianBlur(1.2))
    lut = [tuple(round(a[k] + (b[k] - a[k]) * i / 255) for k in range(3)) for i in range(256)]
    return Image.merge('RGB', [g.point([lut[i][k] for i in range(256)]) for k in range(3)])


def fade(mapped, field):
    """Left 45% eases back to the flat field so titles sit on a quiet surface."""
    w, h = mapped.size
    mask = Image.new('L', (w, 1))
    for x in range(w):
        t = x / w
        mask.putpixel((x, 0), round(255 * (0.3 + 0.7 * min(1, max(0, (t - 0.15) / 0.5)))))
    flat = Image.new('RGB', mapped.size, field)
    return Image.composite(mapped, flat, mask.resize((w, h)))


def main():
    for name, hexv in COL.items():
        src = SRC / f'env_{name}.jpg'
        if not src.exists():
            continue
        photo = Image.open(src).convert('RGB')
        field = rgb(hexv)
        base = cover_crop(photo, SIZE)
        for mode, toward in (('dark', (0, 0, 0)), ('light', (255, 255, 255))):
            tone = partner(field, toward)
            lo, hi = (tone, field) if mode == 'dark' else (field, tone)
            fade(gradient_map(base, lo, hi), field).save(OUT / f'env_{name}_map_{mode}.jpg', quality=88, optimize=True)
        overlay = Image.blend(photo, Image.new('RGB', photo.size, field), 0.18)
        overlay.save(OUT / f'env_{name}_strip.jpg', quality=88, optimize=True)
        print('built', name)


if __name__ == '__main__':
    main()
