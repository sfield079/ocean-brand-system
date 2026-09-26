"""Crop a photograph to an exact aspect ratio (never stretch) and cache it.

Usage: python3 scripts/fit_image.py SRC WIDTH_IN HEIGHT_IN [FOCUS_X FOCUS_Y]
Prints the cached file path. FOCUS is 0-1 (0.5 0.5 = centre).

Why: PowerPoint/LibreOffice stretch a picture to its frame unless the file itself
already has the frame's aspect ratio. Every Ocean photo is cropped here first.
"""
import hashlib
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / 'output' / '.cache' / 'fit'
MAX_W = 2600  # 13.33 in at ~195 dpi, enough for a full-bleed 16:9 slide


def fit(src, w, h, fx=0.5, fy=0.5):
    src = Path(src)
    key = hashlib.sha1(f'{src.resolve()}|{src.stat().st_mtime}|{w:.4f}|{h:.4f}|{fx}|{fy}'.encode()).hexdigest()[:16]
    out = CACHE / f'{src.stem}-{key}.jpg'
    if out.exists():
        return out
    im = Image.open(src).convert('RGB')
    iw, ih = im.size
    target = w / h
    if iw / ih > target:  # too wide: crop the sides
        cw, ch = round(ih * target), ih
    else:  # too tall: crop top and bottom
        cw, ch = iw, round(iw / target)
    x = min(max(round(fx * iw - cw / 2), 0), iw - cw)
    y = min(max(round(fy * ih - ch / 2), 0), ih - ch)
    im = im.crop((x, y, x + cw, y + ch))
    if im.width > MAX_W:
        im = im.resize((MAX_W, round(MAX_W / target)), Image.LANCZOS)
    CACHE.mkdir(parents=True, exist_ok=True)
    im.save(out, quality=88, optimize=True)
    return out


if __name__ == '__main__':
    a = sys.argv[1:]
    fx, fy = (float(a[3]), float(a[4])) if len(a) >= 5 else (0.5, 0.5)
    print(fit(a[0], float(a[1]), float(a[2]), fx, fy))
