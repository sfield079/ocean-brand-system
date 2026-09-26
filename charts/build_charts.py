import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.font_manager as fm, numpy as np, io, cairosvg, subprocess, os, shutil
from matplotlib.patches import FancyBboxPatch
from PIL import Image
fm.fontManager.addfont('/home/user/.fonts/StackSansHeadline-variable.ttf')
plt.style.use('/home/user/workspace/brandsys/charts/ocean.mplstyle')
plt.rcParams.update({'path.simplify': False, 'lines.antialiased': True, 'patch.antialiased': True, 'svg.fonttype': 'path'})
C = dict(bm='#0B1617', pc='#102426', ce='#1B4039', sg='#618C7C', ol='#6E734C', ci='#A69856', cr='#EB3819', sp='#D5CCA0', hd='#F3FBF8')
OUT = '/home/user/workspace/brandsys/charts'
MARK = np.asarray(Image.open(io.BytesIO(cairosvg.svg2png(url='/home/user/workspace/examples/assets/logo_graphic_cedar.svg', output_width=240))))
THIN = '\u2009'
def caps(s):  # visual +0.25em tracking
    return '\u2003'.join((THIN * 2).join(w) for w in s.upper().split(' '))
def ease(t):
    t = min(max(t, 0), 1); return 1 - (1 - t) ** 3
def stage(t, a, b):
    return ease((t - a) / (b - a))
def chip(ax, x, y, txt, fc, tc=C['hd'], fs=9, ha='left'):
    ax.text(x, y, txt, fontsize=fs, fontweight='bold', color=tc, ha=ha, va='center', zorder=6,
            bbox=dict(boxstyle='round,pad=0.35,rounding_size=0.3', fc=fc, ec='none'))

def title(ax, k, t, ink):
    ax.text(0, 1.20, caps(k), transform=ax.transAxes, fontsize=8, fontweight='bold', color=ink, va='bottom')
    ax.text(0, 1.06, t, transform=ax.transAxes, fontsize=15, fontweight='medium', color=ink, va='bottom')

def draw(t=1.0):
    fig, axs = plt.subplots(2, 2, figsize=(16, 10), dpi=150)
    fig.subplots_adjust(hspace=.62, wspace=.25, left=.05, right=.97, top=.80, bottom=.09)
    fig.text(.05, .95, caps('ocean chart system'), fontsize=11, fontweight='bold', color=C['ce'])
    fig.text(.05, .915, 'Cedar, Sage and Citron carry the data. Every number on a data shape is Honeydew. Crimson flags one value.', fontsize=11, color=C['ce'])
    mk = fig.add_axes([.925, .905, .045, .072]); mk.imshow(MARK); mk.axis('off')
    # 1 single series: Sage bars, Cedar focus, Honeydew values inside
    ax = axs[0, 0]; v = np.array([62, 66, 70, 75, 79, 84, 88, 93, 98, 104]); x = np.arange(10)
    for i in range(10):
        g = stage(t, .02 + i * .035, .40 + i * .035); h = v[i] * g
        focus = i == 9
        ax.add_patch(FancyBboxPatch((i - .31, 0), .62, max(h, .01), boxstyle='round,pad=0,rounding_size=0.08',
                                    mutation_aspect=40, fc=C['ce'] if focus else C['sg'], ec='none', zorder=3))
        if g > .6:
            ax.text(i, h - 6, f'{int(round(v[i]*g))}', ha='center', va='center', fontsize=10, fontweight='bold', color=C['hd'], zorder=5, alpha=min(1, (g - .6) / .3))
    ax.set_xlim(-.6, 9.6); ax.set_ylim(0, 115)
    ax.set_xticks(x, [f'Y{i+1:02d}' for i in x], fontsize=9, fontweight='bold', color=C['ce'])
    ax.set_yticks([0, 50, 100], ['0', '50', '100 $K'], fontsize=9, color=C['ce'])
    ax.spines['bottom'].set_color(C['ce'])
    title(ax, '01 single series', 'Sage for context, Cedar for the focus value', C['ce'])
    # 2 line: Cedar actual, dashed forecast, Sage baseline, end chips
    ax = axs[0, 1]; m = np.linspace(0, 11, 111); a = 40 + 8 * np.sin(m / 1.9) + m * 1.2; f = a * .93
    k = max(2, int(len(m) * stage(t, .15, .85)))
    split = 71
    ax.plot(m[:min(k, split)], a[:min(k, split)], color=C['ce'], lw=2.6, solid_capstyle='round', zorder=4)
    if k > split: ax.plot(m[split - 1:k], a[split - 1:k], color=C['ce'], lw=2.6, ls=(0, (2, 3)), dash_capstyle='round', zorder=4)
    ax.plot(m[:k], f[:k], color=C['sg'], lw=2.6, solid_capstyle='round', zorder=3)
    pk = 50
    if k > pk:
        ax.scatter([m[pk]], [a[pk]], s=70, color=C['cr'], zorder=6, edgecolors=C['hd'], linewidths=1.5)
        chip(ax, m[pk] + .35, a[pk] + 3.2, 'PEAK · 53.2 MWh', C['cr'], fs=8.5)
    if k >= len(m) - 1:
        chip(ax, 11.25, a[-1], f'{a[-1]:.1f}', C['ce']); chip(ax, 11.25, f[-1] - 1.2, f'{f[-1]:.1f}', C['sg'])
        ax.text(8.6, a[86] + 2.0, 'Forecast', fontsize=9, color=C['ce']); ax.text(2.2, a[22] + 2.2, 'Actual', fontsize=9, color=C['ce'])
        ax.text(3.2, f[32] - 3.4, 'Baseline', fontsize=9, color=C['sg'])
    ax.set_xlim(-.3, 12.4); ax.set_ylim(30, 62)
    ax.set_xticks(range(12), list('JFMAMJJASOND'), fontsize=9, fontweight='bold', color=C['ce'])
    ax.set_yticks([30, 45, 60], ['30', '45', '60 MWh'], fontsize=9, color=C['ce']); ax.spines['bottom'].set_color(C['ce'])
    title(ax, '02 time series', 'Direct labels in chips; one Crimson flag', C['ce'])
    # 3 stacked: Cedar / Sage / Citron, Honeydew numbers
    ax = axs[1, 0]; cats = ['Site A', 'Site B', 'Site C', 'Site D']
    S = [np.array([46, 38, 52, 30]), np.array([30, 34, 20, 40]), np.array([24, 28, 28, 30])]; cols = [C['ce'], C['sg'], C['ci']]
    for i in range(4):
        g = stage(t, .05 + i * .06, .55 + i * .06); left = 0
        for s, c in zip(S, cols):
            w = s[i] * g
            ax.barh(i, w, left=left, color=c, height=.56, zorder=3, linewidth=0)
            if g > .7: ax.text(left + w / 2, i, f'{s[i]}%', ha='center', va='center', fontsize=10, fontweight='bold', color=C['hd'], zorder=5, alpha=min(1, (g - .7) / .25))
            left += w
    ax.set_yticks(range(4), cats, fontsize=10, color=C['ce']); ax.grid(False); ax.set_xticks([]); ax.set_xlim(0, 100)
    for j, (lab, c) in enumerate([('Solar', C['ce']), ('Storage', C['sg']), ('Grid', C['ci'])]):
        ax.add_patch(FancyBboxPatch((j * 26, 4.08), 3.2, .30, boxstyle='round,pad=0,rounding_size=.05', color=c, clip_on=False))
        ax.text(j * 26 + 4.6, 4.23, lab, va='center', fontsize=9, color=C['ce'])
    ax.set_ylim(4.6, -.6); ax.spines['bottom'].set_color(C['ce'])
    title(ax, '03 categorical', 'Cedar, Sage, Citron in fixed order', C['ce'])
    # 4 dark field
    ax = axs[1, 1]; ax.set_facecolor(C['bm']); ax.grid(color=C['hd'], alpha=.10)
    hh = np.linspace(0, 23, 231); y = np.clip(np.sin((hh - 6) / 12 * np.pi), 0, None) * 420
    k = max(2, int(len(hh) * stage(t, .2, .9)))
    ax.fill_between(hh[:k], y[:k], color=C['sp'], alpha=.22, lw=0); ax.plot(hh[:k], y[:k], color=C['sp'], lw=2.6, solid_capstyle='round')
    ax.set_xticks([0, 6, 12, 18, 23], ['00:00', '06:00', '12:00', '18:00', '23:00'], color=C['hd'], fontsize=9, fontweight='bold')
    ax.set_yticks([0, 200, 400], ['0', '200', '400'], color=C['hd'], fontsize=9); ax.spines['bottom'].set_color(C['hd']); ax.set_ylim(0, 600); ax.set_xlim(-.5, 23.5)
    if k > 120: chip(ax, 12, 455, '412 kW PEAK', C['sp'], tc=C['bm'], fs=8.5, ha='center')
    ax.text(.05, .85, f'{int(412*stage(t,.2,.9))} kW', transform=ax.transAxes, fontsize=22, fontweight='light', color=C['hd'])
    ax.text(.05, .77, caps('peak output'), transform=ax.transAxes, fontsize=7, fontweight='bold', color=C['hd'])
    title(ax, '04 dark field', 'On Blackmoss: Sprig series, Honeydew labels', C['hd'])
    import matplotlib.patches as mp
    bb = ax.get_position()
    fig.patches.append(mp.FancyBboxPatch((bb.x0 - .035, bb.y0 - .055), bb.width + .05, bb.height + .175, boxstyle='round,pad=0,rounding_size=.012',
                                         transform=fig.transFigure, color=C['bm'], zorder=-1))
    fig.text(.05, .02, caps('illustrative data · sample'), fontsize=8, color=C['ce'])
    return fig

fig = draw(1.0)
fig.savefig(f'{OUT}/ocean-chart-system.png', dpi=300)
fig.savefig(f'{OUT}/ocean-chart-system.svg')
fig.savefig(f'{OUT}/ocean-chart-system.pdf')
plt.close(fig)
if os.environ.get('ANIM'):
    fr = '/tmp/chartframes'; shutil.rmtree(fr, ignore_errors=True); os.makedirs(fr)
    N = 75
    for i in range(N):
        fg = draw(i / (N - 1)); fg.savefig(f'{fr}/f{i:03d}.png', dpi=120); plt.close(fg)
    for j in range(N, N + 45): shutil.copy(f'{fr}/f{N-1:03d}.png', f'{fr}/f{j:03d}.png')
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', '30', '-i', f'{fr}/f%03d.png', '-c:v', 'libx264', '-pix_fmt', 'yuv420p',
                    '-crf', '14', '-vf', 'scale=trunc(iw/2)*2:trunc(ih/2)*2', f'{OUT}/ocean-chart-system-animated.mp4'], check=True)
print('ok')
