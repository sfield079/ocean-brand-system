"""Build the portable web kit (web-kit/) and tokens/build/ocean.css from tokens/ocean.tokens.json.

The web kit is the one folder any web builder (Base44, Lovable, v0, Bolt, Replit, a Next.js or
Vite app, oceanrcs.com) copies into its own project: CSS with self-hosted fonts, every approved
pairing, the Tailwind preset, logos and tokens. Run: python3 scripts/build_web_kit.py
CI fails if the committed kit differs from a fresh build (tests/test_web_kit.py).
"""
import json, shutil
from pathlib import Path
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
KIT = ROOT / 'web-kit'
T = json.loads((ROOT / 'tokens/ocean.tokens.json').read_text())
COLORS = {k: v['value'] for k, v in T['color'].items()}
DETAIL = T['pairing']['detail']
FONTS = {'Light': 300, 'Regular': 400, 'Medium': 500, 'Bold': 700}


def root_block():
    lines = [':root{']
    lines += [f'  --ocean-{k}:{v};' for k, v in COLORS.items()]
    lines += ['  --ocean-font:"Stack Sans Headline",system-ui,sans-serif;',
              '  --ocean-w-light:300;--ocean-w-regular:400;--ocean-w-medium:500;--ocean-w-bold:700;',
              '  --ocean-track-caps:.25em;--ocean-track-label:.125em;--ocean-track-title:-.01em;--ocean-track-display:-.02em;--ocean-track-hero:-.04em;',
              '  --ocean-radius-sm:4px;--ocean-radius-md:12px;--ocean-radius-lg:20px;',
              '  --ocean-chamfer-sm:12px;--ocean-chamfer-md:24px;--ocean-chamfer-lg:44px;',
              '  --ocean-rule:1px;--ocean-frame:2px;',
              '  /* default pairing: Honeydew field + Blackmoss ink (oceanrcs.com, L2) */',
              '  --ocean-field:var(--ocean-honeydew);--ocean-ink:var(--ocean-blackmoss);', '}']
    return '\n'.join(lines)


def pair_rules():
    out = ['/* Approved pairings (brand/decisions.md Part 12). data-pair="<field>-<ink>".',
           '   Tier: text = any size; large = 25px+ bold or 32px+; display = 44px+ only; tonal = no text. */']
    for d in DETAIL:
        a, b = d['pair'].split('+')
        for f, i in ((a, b), (b, a)):
            out.append(f'[data-pair="{f}-{i}"]{{--ocean-field:var(--ocean-{f});--ocean-ink:var(--ocean-{i});'
                       f'background:var(--ocean-field);color:var(--ocean-ink)}} /* {d["contrast"]}:1 {d["tier"]} */')
    out.append('[data-pair="white-blackmoss"]{--ocean-field:var(--ocean-white);--ocean-ink:var(--ocean-blackmoss);background:var(--ocean-field);color:var(--ocean-ink)} /* print and formal */')
    return '\n'.join(out)


UTIL = '''.ocean-caps{text-transform:uppercase;letter-spacing:var(--ocean-track-caps);font-weight:var(--ocean-w-bold)}
.ocean-caps-light{text-transform:uppercase;letter-spacing:var(--ocean-track-caps);font-weight:var(--ocean-w-light)}
.ocean-hero{font-weight:var(--ocean-w-light);letter-spacing:var(--ocean-track-hero);line-height:1.02}
.ocean-display{font-weight:var(--ocean-w-medium);letter-spacing:var(--ocean-track-display);line-height:1.08}
.ocean-chamfer{clip-path:polygon(var(--ocean-chamfer-md) 0,100% 0,100% 100%,0 100%,0 var(--ocean-chamfer-md));border-radius:0 var(--ocean-radius-lg) var(--ocean-radius-lg) var(--ocean-radius-lg)}
.ocean-card{position:relative;border:var(--ocean-rule) solid var(--ocean-ink);border-radius:var(--ocean-radius-md) var(--ocean-radius-md) 0 var(--ocean-radius-md)}
.ocean-card::after{content:"";position:absolute;right:-1px;bottom:-1px;width:var(--ocean-chamfer-sm);height:var(--ocean-chamfer-sm);background:linear-gradient(to top left,var(--ocean-field) calc(50% - .6px),var(--ocean-ink) calc(50% - .6px),var(--ocean-ink) calc(50% + .6px),transparent calc(50% + .6px))}
.ocean-btn{text-decoration:none;display:inline-flex;align-items:center;gap:.6em;padding:.9em 1.4em;background:var(--ocean-ink);color:var(--ocean-field);border:0;text-transform:uppercase;letter-spacing:var(--ocean-track-caps);font:700 12px/1 var(--ocean-font);clip-path:polygon(var(--ocean-chamfer-sm) 0,100% 0,100% 100%,0 100%,0 var(--ocean-chamfer-sm))}
.ocean-btn-secondary{background:transparent;color:var(--ocean-ink);border:var(--ocean-frame) solid var(--ocean-ink);clip-path:none}
.ocean-chip{background:var(--ocean-ink);color:var(--ocean-field);padding:0 .25em;font-weight:var(--ocean-w-bold)}
.ocean-bottom-line{display:flex;gap:1em;align-items:center;background:var(--ocean-ink);color:var(--ocean-field);padding:.8em 1.2em;font-weight:var(--ocean-w-bold)}
.ocean-bottom-line::before{content:"BOTTOM LINE";font-weight:var(--ocean-w-light);letter-spacing:var(--ocean-track-caps);font-size:.72em}
.ocean-notice{text-transform:uppercase;letter-spacing:var(--ocean-track-caps);font-weight:var(--ocean-w-light);font-size:11px}
:focus-visible{outline:2px solid var(--ocean-ink);outline-offset:2px}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
.material-symbols-outlined{font-family:"Material Symbols Outlined";font-weight:400;font-style:normal;font-variation-settings:"FILL" 0,"wght" 400,"GRAD" 0,"opsz" 24;line-height:1;display:inline-block}
/* Micro-app themes (L3): default dark, approved light alternative, user toggle on <html data-theme> */
[data-theme="dark"],.ocean-app{--ocean-field:var(--ocean-blackmoss);--ocean-ink:var(--ocean-honeydew);--ocean-tile:var(--ocean-sage)}
[data-theme="light"]{--ocean-field:var(--ocean-honeydew);--ocean-ink:var(--ocean-peacock);--ocean-tile:var(--ocean-peacock)}'''


def font_faces():
    faces = [f'@font-face{{font-family:"Stack Sans Headline";src:url("./fonts/StackSansHeadline-{n}.woff2") format("woff2");font-weight:{w};font-style:normal;font-display:swap}}'
             for n, w in FONTS.items()]
    faces.append('@font-face{font-family:"Material Symbols Outlined";src:url("./fonts/MaterialSymbolsOutlined.woff2") format("woff2");font-weight:400;font-style:normal;font-display:block}')
    return '\n'.join(faces)


def build():
    body = f'{root_block()}\nhtml,body{{font-family:var(--ocean-font);background:var(--ocean-field);color:var(--ocean-ink)}}\n{pair_rules()}\n{UTIL}\n'
    head = '/* GENERATED by scripts/build_web_kit.py from tokens/ocean.tokens.json. Do not edit by hand. */\n'
    (ROOT / 'tokens/build/ocean.css').write_text(head + body)
    if KIT.exists():
        for p in ('fonts', 'logos'):
            shutil.rmtree(KIT / p, ignore_errors=True)
    (KIT / 'fonts').mkdir(parents=True, exist_ok=True)
    for n in FONTS:
        f = TTFont(ROOT / f'brand/fonts/StackSansHeadline-{n}.ttf', recalcTimestamp=False); f.flavor = 'woff2'
        f.save(KIT / f'fonts/StackSansHeadline-{n}.woff2')
    f = TTFont(ROOT / 'assets/fonts/MaterialSymbolsOutlined-400-static.ttf', recalcTimestamp=False); f.flavor = 'woff2'
    f.save(KIT / 'fonts/MaterialSymbolsOutlined.woff2')
    shutil.copy(ROOT / 'brand/fonts/OFL.txt', KIT / 'fonts/OFL.txt')
    (KIT / 'ocean.css').write_text(head + font_faces() + '\n' + body)
    shutil.copytree(ROOT / 'assets/logos/variants', KIT / 'logos')
    for svg in ('Ocean_LOGO_Graphic.svg', 'Ocean_LOGO_Horizontal.svg', 'Ocean_LOGO_Vertical.svg'):
        shutil.copy(ROOT / 'assets/logos' / svg, KIT / 'logos' / svg)
    shutil.copy(ROOT / 'tokens/build/tailwind.preset.js', KIT / 'tailwind.preset.js')
    shutil.copy(ROOT / 'tokens/ocean.tokens.json', KIT / 'ocean.tokens.json')
    shutil.copy(ROOT / 'brand/notices.json', KIT / 'notices.json')
    print(f'Built {KIT.relative_to(ROOT)} and tokens/build/ocean.css ({len(DETAIL) * 2} pairings)')


if __name__ == '__main__':
    build()
