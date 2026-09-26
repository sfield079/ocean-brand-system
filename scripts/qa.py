#!/usr/bin/env python3
"""Automated pre-flight checks for Ocean RCS decks.

Usage: python3 scripts/qa.py output/pptx/<deck>.pptx
Checks: font-size minimums, off-slide objects, safe-margin violations,
off-palette text colors, overlapping text boxes, and open [TBD placeholders.
Automated checks do not replace inspecting every rendered PNG.
"""
import json, sys, itertools
from pathlib import Path
from pptx import Presentation
from pptx.util import Emu

ROOT = Path(__file__).resolve().parent.parent
brand = json.loads((ROOT / "brand" / "color-system.json").read_text())
PALETTE = {v.upper() for v in {**brand["colors"], **brand["tints"]}.values()}
MIN_PT = brand["typeScale"]["footnote"]
MARGIN_IN = 0.6 - 0.05
EMU_IN = 914400

def inch(v): return v / EMU_IN

def main(path):
    prs = Presentation(path)
    W, H = inch(prs.slide_width), inch(prs.slide_height)
    errors, warnings, tbd = [], [], 0
    for i, slide in enumerate(prs.slides, 1):
        boxes = []
        for sh in slide.shapes:
            x, y = inch(sh.left or 0), inch(sh.top or 0)
            w, h = inch(sh.width or 0), inch(sh.height or 0)
            full_bleed = sh.shape_type == 13 or (w >= W - 0.01 or h >= H - 0.01) or (x + w >= W - 0.01 and sh.shape_type == 13)
            if x < -0.01 or y < -0.01 or x + w > W + 0.01 or y + h > H + 0.01:
                errors.append(f"slide {i}: '{sh.name}' extends off the slide")
            if sh.has_text_frame and sh.text_frame.text.strip():
                txt = sh.text_frame.text.strip()
                if txt.startswith('[IMAGE:'):
                    tbd += 1
                    continue
                tbd += txt.count("[TBD")
                if not full_bleed and (x < MARGIN_IN or x + w > W - MARGIN_IN + 0.01):
                    warnings.append(f"slide {i}: text '{txt[:30]}' inside safe margin")
                boxes.append((sh.name, x, y, w, h, txt[:30]))
                for p in sh.text_frame.paragraphs:
                    for r in p.runs:
                        if r.font.size and r.font.size.pt < MIN_PT:
                            errors.append(f"slide {i}: {r.font.size.pt}pt text '{r.text[:30]}' below {MIN_PT}pt")
                        try:
                            rgb = str(r.font.color.rgb).upper() if r.font.color and r.font.color.type else None
                        except AttributeError:
                            rgb = None
                        if rgb and rgb not in PALETTE:
                            errors.append(f"slide {i}: off-palette color #{rgb} on '{r.text[:30]}'")
        for a, b in itertools.combinations(boxes, 2):
            ox = min(a[1] + a[3], b[1] + b[3]) - max(a[1], b[1])
            oy = min(a[2] + a[4], b[2] + b[4]) - max(a[2], b[2])
            if ox > 0.05 and oy > 0.05:
                warnings.append(f"slide {i}: text boxes overlap: '{a[5]}' / '{b[5]}'")
    print(f"QA: {path}  ({len(prs.slides)} slides)")
    for e in errors: print("  ERROR  ", e)
    for w in warnings: print("  WARN   ", w)
    print(f"  INFO    {tbd} open [TBD] placeholder(s)")
    print("  RESULT  " + ("FAIL" if errors else "PASS (now inspect every rendered PNG)"))
    sys.exit(1 if errors else 0)

if __name__ == "__main__":
    main(sys.argv[1])
