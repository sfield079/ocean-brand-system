// Ocean RCS deck layouts (approved brand system, 26 Sep 2026).
// Every value comes from tokens/ocean.tokens.json. All text, tables and charts stay editable.
// Visual reference: output/reference/examples/Ocean_Example_Presentation.pdf
const fs = require('fs');
const path = require('path');
const PptxGenJS = require('pptxgenjs');
const opentype = require('opentype.js');

const ROOT = path.join(__dirname, '..');
const TOKENS = JSON.parse(fs.readFileSync(path.join(ROOT, 'tokens/ocean.tokens.json')));
const BRAND = JSON.parse(fs.readFileSync(path.join(ROOT, 'brand/color-system.json')));
const C = Object.fromEntries(Object.entries(TOKENS.color).map(([k, v]) => [k, v.value.replace('#', '').toUpperCase()]));
const T = BRAND.typeScale;
const NAME = Object.fromEntries(Object.entries(C).map(([k, v]) => [v, k]));

// 16:9 at 13.333 x 7.5 in. The reference was drawn at 1920 x 1080 px, so 144 px = 1 in and 2 px = 1 pt.
const W = 13.333, H = 7.5, M = 0.6, CW = W - M * 2;
const px = v => v / 144;
const BODY = 3.33, BOTTOM = 6.95;

const FAMILY = TOKENS.font.family.brand;
const FACE = {light: `${FAMILY} Light`, regular: FAMILY, medium: `${FAMILY} Medium`, bold: FAMILY};
const faces = Object.fromEntries(['Light', 'Regular', 'Medium', 'Bold'].map(w => [w.toLowerCase(),
  opentype.parse(fs.readFileSync(path.join(ROOT, `brand/fonts/StackSansHeadline-${w}.ttf`)).buffer)]));
const EM = v => parseFloat(v) || 0;
const TRACK = {caps: EM(TOKENS.tracking.caps), label: EM(TOKENS.tracking.label), title: EM(TOKENS.tracking.title),
  display: EM(TOKENS.tracking.display), hero: EM(TOKENS.tracking.hero), heroBold: EM(TOKENS.tracking['hero-bold'])};

// Approved two-color pairings (brand/decisions.md Part 2). Order does not matter.
const APPROVED = new Set([
  ...['peacock', 'cedar', 'sage', 'honeydew', 'sprig', 'olive', 'citron', 'crimson'].map(c => ['blackmoss', c]),
  ...['cedar', 'sage', 'honeydew', 'sprig', 'olive', 'citron', 'crimson'].map(c => ['peacock', c]),
  ...['sage', 'honeydew', 'sprig', 'olive', 'citron'].map(c => ['cedar', c]),
  ['sage', 'honeydew'], ['sage', 'sprig'],
  ...['sprig', 'olive', 'citron', 'crimson'].map(c => ['honeydew', c]),
  ...['olive', 'citron', 'crimson'].map(c => ['sprig', c]),
  ['olive', 'citron'],
].map(p => p.sort().join('+')));
function pairing(name) {
  const [field, ink] = String(name).split('-');
  if (!C[field] || !C[ink] || !APPROVED.has([field, ink].sort().join('+')))
    throw new Error(`Pairing ${name} is not an approved Ocean pairing (brand/decisions.md Part 2)`);
  return {name, field, ink, F: C[field], I: C[ink]};
}
const TEXTURE = {sage: 'tex_deck_sage.png', blackmoss: 'tex_deck_blackmoss.png'};

function advance(text, pt, weight, track) {
  return faces[weight].getAdvanceWidth(text, pt) + track * pt * Math.max(0, text.length - 1);
}
function wrap(text, width, pt, bold = false, weight = null, track = 0) {
  weight = weight || (bold ? 'bold' : 'regular');
  const lines = [];
  for (const para of String(text).split('\n')) {
    let line = '';
    for (const word of para.split(/\s+/).filter(Boolean)) {
      if (advance(word, pt, weight, track) > width * 72)
        throw new Error(`Unbreakable word does not fit: ${word}. Widen the column.`);
      const candidate = line ? `${line} ${word}` : word;
      if (line && advance(candidate, pt, weight, track) > width * 72) { lines.push(line); line = word; }
      else line = candidate;
    }
    lines.push(line);
  }
  return lines;
}
function count(label, items, max) {
  if (!Array.isArray(items) || !items.length || items.length > max)
    throw new Error(`${label}: requires 1–${max} items. Split the content.`);
}
// Rounded rectangle with one 45-degree chamfer, the guide's panel geometry.
function chamferPoints(w, h, c, r, corner) {
  const q = (x, y, x1, y1) => ({x, y, curve: {type: 'quadratic', x1, y1}});
  if (corner === 'tl') return [{x: 0, y: c}, {x: c, y: 0}, {x: w - r, y: 0}, q(w, r, w, 0), {x: w, y: h - r},
    q(w - r, h, w, h), {x: r, y: h}, q(0, h - r, 0, h), {close: true}];
  return [{x: r, y: 0}, {x: w - r, y: 0}, q(w, r, w, 0), {x: w, y: h - c}, {x: w - c, y: h}, {x: r, y: h},
    q(0, h - r, 0, h), {x: 0, y: r}, q(r, 0, 0, 0), {close: true}];
}

class OceanDeck {
  constructor({title = 'Ocean RCS', confidential = true, footer = 'Ocean RCS', draft = false,
    sections = [], kind = 'Client briefing', client = 'Ocean RCS'} = {}) {
    if (sections.length > 5) throw new Error('Staging header holds at most five sections');
    this.pptx = new PptxGenJS();
    this.pptx.defineLayout({name: 'OCEAN', width: W, height: H});
    this.pptx.layout = 'OCEAN';
    this.pptx.title = title; this.pptx.company = 'Ocean RCS';
    this.pptx.theme = {headFontFace: FAMILY, bodyFontFace: FAMILY};
    Object.assign(this, {footer, confidential, draft, sections, kind, client, n: 0, crimson: 0});
  }
  // ---------------------------------------------------------------- primitives
  text(s, text, x, y, w, h, {pt = 14, bold = false, weight = null, color = C.blackmoss, role = 'body', align = 'left',
    caps = false, track = null, leading = null, valign = 'top'} = {}) {
    if (text === undefined || text === null || text === '') return;
    text = String(text);
    if (!this.draft && /\[TBD|\[IMAGE|\[PLACEHOLDER/i.test(text)) throw new Error('Unresolved placeholder in release output');
    weight = weight || (bold ? 'bold' : 'regular');
    if (caps) { text = text.toUpperCase(); if (track === null) track = TRACK.caps; if (!['bold', 'light'].includes(weight)) weight = 'bold'; }
    track = track || 0;
    const lead = leading || pt * 1.24;
    const lines = wrap(text, w - 0.08, pt, false, weight, Math.max(0, track));
    // A one-line label box grows to its line height; text is never shrunk.
    if (lines.length === 1 && h < lead / 72 + 0.03) h = lead / 72 + 0.03;
    if (lines.length * lead / 72 > h - 0.025)
      throw new Error(`Text does not fit ${role}: ${text.slice(0, 80)}. Edit or split; do not shrink.`);
    s.addText(lines.join('\n'), {x, y, w, h, fontFace: FACE[weight], fontSize: pt, bold: weight === 'bold', color,
      margin: 0, breakLine: false, valign, align, lineSpacing: lead, charSpacing: track ? track * pt : undefined,
      objectName: `ocean:${role}`, paraSpaceAfterPt: 0});
  }
  rule(s, x, y, w, color = C.blackmoss, pt = 1) { s.addShape('line', {x, y, w, h: 0, line: {color, width: pt}}); }
  frame(s, x, y, w, h, color, {corner = 'br', c = px(36), r = px(18), pt = 0.75, fill = null} = {}) {
    s.addShape('custGeom', {x, y, w, h, points: chamferPoints(w, h, c, r, corner),
      line: {color, width: pt}, fill: fill ? {color: fill} : {type: 'none'}, objectName: 'ocean:frame'});
  }
  diamonds(s, x, y, n, color) {
    for (let i = 0; i < n; i++) s.addShape('diamond', {x: x - i * px(22), y, w: px(13), h: px(13), fill: {color}, line: {color, width: 0}});
  }
  logo(s, kind, color, {x, y, h}) {
    const file = path.join(ROOT, `assets/logos/png/logo_${kind}_${NAME[color]}.png`);
    if (!fs.existsSync(file)) throw new Error(`Approved logo missing: ${file}`);
    const ratio = {horizontal: 510.07 / 142.42, vertical: 241.6 / 212.6, graphic: 1}[kind];
    s.addImage({path: file, x, y, w: h * ratio, h, objectName: `ocean:logo-${kind}`});
  }
  image(s, img, x, y, w, h, label, field = C.honeydew) {
    if (img && fs.existsSync(img)) {
      s.addImage({path: img, x, y, w, h, sizing: {type: 'cover', w, h}, objectName: 'ocean:photo'});
      // Top-left chamfer mask in the field color (guide image frame).
      s.addShape('rtTriangle', {x: x - 0.005, y: y - 0.005, w: px(44), h: px(44), flipV: true, fill: {color: field}, line: {color: field, width: 0}});
      return;
    }
    if (!this.draft) throw new Error(`Missing supplied image: ${img || label}`);
    this.frame(s, x, y, w, h, C.sage, {corner: 'tl', c: px(44), r: px(20)});
    this.text(s, '[IMAGE: supplied photograph required]', x + 0.25, y + 0.3, w - 0.5, 0.4, {pt: 10, caps: true, color: C.cedar, role: 'label'});
  }
  // ---------------------------------------------------------------- page scaffolding
  page(notes, pairName = 'honeydew-blackmoss', {texture = false} = {}) {
    const p = pairing(pairName);
    const s = this.pptx.addSlide(); this.n++;
    s.background = {color: p.F};
    if (texture && TEXTURE[p.field]) s.addImage({path: path.join(ROOT, 'assets/textures', TEXTURE[p.field]), x: 0, y: 0, w: W, h: H, objectName: 'ocean:texture'});
    s._ocean = p;
    if (notes) s.addNotes(notes);
    return s;
  }
  footerLine(s, p) {
    const bits = [this.footer, this.confidential ? 'Confidential' : '', this.draft ? 'Design specimen' : ''].filter(Boolean).join('   ·   ');
    this.text(s, bits, M, 7.02, 8, 0.2, {pt: 9, caps: true, weight: 'light', color: p.I, role: 'footer'});
  }
  header(s, active) {
    const p = s._ocean, y = 0.36, h = px(96), ink = p.I;
    s.addShape('rect', {x: M, y, w: CW, h, fill: {type: 'none'}, line: {color: ink, width: 1}, objectName: 'ocean:header'});
    const cells = this.sections.length || 1;
    const logoW = px(330), pageW = px(140), clientW = px(330), numW = px(88);
    const vline = x => s.addShape('line', {x, y, w: 0, h, line: {color: ink, width: 1}});
    this.logo(s, 'horizontal', ink, {x: M + px(28), y: y + (h - px(44)) / 2, h: px(44)});
    let x = M + logoW; vline(x);
    this.text(s, 'Page', x + px(22), y + 0.1, pageW - 0.2, 0.2, {pt: 9, caps: true, weight: 'light', color: ink, role: 'header'});
    this.text(s, String(this.n).padStart(2, '0'), x + px(22), y + 0.33, pageW - 0.2, 0.2, {pt: 9, caps: true, color: ink, role: 'header'});
    x += pageW; vline(x);
    const navEnd = M + CW - clientW - numW * cells;
    let nx = x + px(30);
    this.sections.forEach((name, i) => {
      const label = name.toUpperCase(), wIn = advance(label, 9, 'bold', 0.12) / 72 + 0.14;
      if (nx + wIn > navEnd) throw new Error('Staging header sections do not fit; shorten section names');
      const on = name === active;
      if (on) s.addShape('rect', {x: nx - 0.04, y: y + h / 2 - 0.13, w: wIn, h: 0.26, fill: {color: ink}, line: {color: ink, width: 0}});
      this.text(s, label, nx + 0.03, y + h / 2 - 0.09, wIn, 0.2, {pt: 9, weight: 'bold', track: 0.12, color: on ? p.F : ink, role: 'header'});
      nx += wIn + 0.16;
    });
    x = navEnd; vline(x);
    this.text(s, this.kind, x + px(26), y + 0.1, clientW - 0.3, 0.2, {pt: 9, caps: true, weight: 'light', color: ink, role: 'header'});
    this.text(s, this.client, x + px(26), y + 0.33, clientW - 0.3, 0.2, {pt: 9, caps: true, color: ink, role: 'header'});
    x += clientW;
    for (let i = 0; i < cells; i++) {
      vline(x);
      const on = this.sections[i] === active;
      if (on) s.addShape('rect', {x, y, w: numW, h, fill: {color: ink}, line: {color: ink, width: 0}});
      if (this.sections.length) this.text(s, String(i + 1).padStart(2, '0'), x + 0.05, y + h / 2 - 0.1, numW - 0.1, 0.22,
        {pt: 11, weight: 'bold', track: 0.1, align: 'center', color: on ? p.F : ink, role: 'header'});
      x += numW;
    }
  }
  titleBlock(s, kicker, headline, lede) {
    const ink = s._ocean.I;
    if (kicker) this.text(s, kicker, M, 1.46, 6.9, 0.22, {pt: 11, caps: true, color: ink, role: 'label'});
    this.text(s, headline, M - 0.02, 1.72, 6.94, 1.14, {pt: 35, weight: 'medium', track: TRACK.title, leading: 39, color: ink, role: 'headline'});
    if (lede) this.text(s, lede, 7.7, 1.72, CW - 7.1, 1.14, {pt: 10.5, caps: true, leading: 17, color: ink, role: 'lede', valign: 'bottom'});
    this.rule(s, M, 2.99, CW, ink);
  }
  content(notes, pairName, {section, kicker, headline, lede}) {
    const s = this.page(notes, pairName);
    this.header(s, section); this.titleBlock(s, kicker, headline, lede); this.footerLine(s, s._ocean);
    return s;
  }
  head(s, eyebrow, headline) { this.titleBlock(s, eyebrow, headline); }
  note(s, text) { if (text) this.text(s, text, M, 6.72, CW, 0.22, {pt: 9, caps: true, weight: 'light', color: s._ocean.I, role: 'footnote'}); }
  crimsonMoment() {
    if (++this.crimson > 1) throw new Error('Crimson appears once per deck as a moment (brand/decisions.md Part 4)');
    return C.crimson;
  }
  metaLine(s, items, x, y, ink) {
    // Key (Light caps) + value (Bold caps) pairs, the guide's key/value footer pattern.
    let cx = x;
    items.forEach(([k, v]) => {
      const kw = advance(String(k).toUpperCase(), 10, 'light', TRACK.caps) / 72 + 0.12;
      const vw = advance(String(v).toUpperCase(), 10, 'bold', TRACK.caps) / 72 + 0.12;
      this.text(s, k, cx, y, kw, 0.22, {pt: 10, caps: true, weight: 'light', color: ink, role: 'meta'});
      this.text(s, v, cx + kw + 0.12, y, vw, 0.22, {pt: 10, caps: true, color: ink, role: 'meta'});
      cx += kw + vw + 0.6;
    });
  }
  // ---------------------------------------------------------------- layouts
  cover({title, subtitle, date, kicker = 'Ocean RCS', year = String(new Date().getFullYear()), meta = [], image, notes, pair = 'sage-honeydew'}) {
    const s = this.page(notes, pair, {texture: true}), p = s._ocean, ink = p.I;
    this.frame(s, px(48), px(48), W - px(96), H - px(96), ink, {corner: 'tl', c: px(44), r: px(20), pt: 1});
    this.logo(s, 'vertical', ink, {x: px(112), y: px(108), h: px(132)});
    this.text(s, year, W - 3.2 - px(112), px(100), 3.2, 0.56, {pt: 30, track: TRACK.display, align: 'right', color: ink, role: 'label'});
    this.text(s, date, W - 4.2 - px(112), 1.36, 4.2, 0.3, {pt: 11, caps: true, weight: 'light', align: 'right', color: ink, role: 'label'});
    const tw = image ? 7.4 : W - px(224);
    this.text(s, kicker, px(112), 3.3, tw, 0.25, {pt: 12, caps: true, color: ink, role: 'label'});
    this.text(s, title, px(104), 3.6, tw, 2.35, {pt: 84, weight: 'light', track: TRACK.hero, leading: 72, color: ink, role: 'cover'});
    if (image) this.image(s, image, 8.6, 1.5, 4.0, 4.4, 'Cover photograph', p.F);
    this.rule(s, px(112), px(958), W - px(224), ink);
    this.metaLine(s, subtitle ? [['Prepared for', subtitle], ...meta] : meta, px(112), px(982), ink);
    return s;
  }
  agenda({items, notes, pair = 'honeydew-blackmoss'}) {
    count('Agenda items', items, 5);
    const s = this.page(notes, pair), ink = s._ocean.I;
    this.logo(s, 'horizontal', ink, {x: M, y: px(64), h: px(44)});
    this.text(s, this.kind, W - M - 3.5, px(62), 3.5, 0.2, {pt: 10, caps: true, weight: 'light', align: 'right', color: ink, role: 'label'});
    this.text(s, this.client, W - M - 3.5, px(96), 3.5, 0.2, {pt: 10, caps: true, align: 'right', color: ink, role: 'label'});
    this.text(s, 'Agenda', 0.56, 1.2, 8, 1.7, {pt: 125, weight: 'bold', track: TRACK.heroBold, leading: 115, color: ink, role: 'cover'});
    const rowH = (px(1030) - 3.26) / items.length;
    items.forEach((it, i) => {
      const y = 3.26 + i * rowH;
      this.rule(s, M, y, CW, ink);
      this.text(s, String(i + 1).padStart(2, '0'), 0.56, y + 0.05, 3, rowH - 0.08, {pt: Math.min(60, rowH * 60), weight: 'light', track: TRACK.heroBold, leading: Math.min(62, rowH * 62), color: ink, role: 'metric'});
      this.text(s, it.key, 4.86, y + 0.2, 7.8, 0.2, {pt: 11, caps: true, color: ink, role: 'label'});
      this.text(s, it.title, 4.84, y + 0.42, 7.9, rowH - 0.46, {pt: 28, track: TRACK.title, leading: 32, color: ink, role: 'section'});
    });
    const yEnd = 3.26 + items.length * rowH;
    this.rule(s, M, yEnd, CW, ink); s.addShape('rect', {x: M, y: yEnd + px(8), w: CW, h: px(6), fill: {color: ink}, line: {color: ink, width: 0}});
    return s;
  }
  divider({number, title, subtitle, image, notes, pair = 'blackmoss-honeydew'}) {
    const s = this.page(notes, pair, {texture: true}), ink = s._ocean.I;
    this.logo(s, 'graphic', ink, {x: W - M - px(56), y: px(64), h: px(56)});
    this.text(s, String(number || 1).padStart(2, '0'), 0.56, 1.9, 4, 1.6, {pt: 120, weight: 'light', track: TRACK.hero, leading: 118, color: ink, role: 'metric'});
    const w = image ? 6.8 : CW;
    this.text(s, title, M, 3.9, w, 1.4, {pt: 40, weight: 'medium', track: TRACK.display, leading: 44, color: ink, role: 'headline'});
    this.text(s, subtitle, M, 5.45, w, 0.9, {pt: 11, caps: true, leading: 18, color: ink, role: 'subhead'});
    if (image) this.image(s, image, 8.3, 1.45, 4.43, 4.85, 'Section photograph', s._ocean.F);
    return s;
  }
  statement({eyebrow, headline, support, image, section, notes, pair = 'honeydew-blackmoss'}) {
    const s = this.content(notes, pair, {section, kicker: eyebrow, headline});
    const w = image ? 5.6 : 9.4, ink = s._ocean.I;
    this.text(s, support, M, BODY, w, 3.2, {pt: 26, track: TRACK.title, leading: 33, color: ink, role: 'statement'});
    if (image) this.image(s, image, 7.25, BODY, 5.48, 3.4, 'Evidence photograph', s._ocean.F);
    return s;
  }
  keyNumber({kicker, value, text, meta = [], notes, pair = 'blackmoss-honeydew'}) {
    const s = this.page(notes, pair, {texture: true}), ink = s._ocean.I;
    this.logo(s, 'graphic', ink, {x: W - M - px(56), y: px(64), h: px(56)});
    this.text(s, kicker, M, 3.72, 5.4, 0.22, {pt: 11, caps: true, color: ink, role: 'label'});
    this.text(s, value, 0.56, 3.98, 5.2, 2.3, {pt: 165, weight: 'light', track: TRACK.hero, leading: 165, color: this.crimsonMoment(), role: 'metric'});
    this.text(s, text, 5.97, 4.44, 6.8, 1.8, {pt: 38, weight: 'medium', track: TRACK.display, leading: 42, color: ink, role: 'statement'});
    this.rule(s, M, px(940), CW, ink);
    this.metaLine(s, meta, M, px(966), ink);
    return s;
  }
  twoColumn({eyebrow, headline, lede, left, right, section, notes, pair = 'honeydew-peacock'}) {
    const s = this.content(notes, pair, {section, kicker: eyebrow, headline, lede}), ink = s._ocean.I;
    const w = (CW - 0.5) / 2;
    [left, right].forEach((col, i) => {
      const x = M + i * (w + 0.5); count(col.label, col.points, 3);
      this.frame(s, x, BODY, w, BOTTOM - BODY - 0.2, ink, {corner: 'br'});
      this.diamonds(s, x + w - 0.35, BODY + 0.26, i + 1, ink);
      this.text(s, col.label, x + 0.25, BODY + 0.22, w - 1.2, 0.25, {pt: 11, caps: true, color: ink, role: 'section'});
      col.points.forEach((pt, j) => {
        const y = BODY + 0.72 + j * 0.8;
        this.rule(s, x + 0.25, y, w - 0.5, ink, 0.5);
        this.text(s, pt, x + 0.25, y + 0.12, w - 0.5, 0.62, {pt: 15, color: ink});
      });
    }); return s;
  }
  pillars({eyebrow, headline, lede, pillars, section, notes, pair = 'honeydew-cedar'}) {
    count('Pillars', pillars, 3);
    const s = this.content(notes, pair, {section, kicker: eyebrow, headline, lede}), ink = s._ocean.I;
    const w = (CW - (pillars.length - 1) * 0.3) / pillars.length, h = BOTTOM - BODY - 0.2;
    pillars.forEach((p, i) => {
      const x = M + i * (w + 0.3);
      this.frame(s, x, BODY, w, h, ink, {corner: 'br'}); this.diamonds(s, x + w - 0.35, BODY + 0.26, i + 1, ink);
      this.text(s, String(i + 1).padStart(2, '0'), x + 0.25, BODY + 0.22, 1, 0.22, {pt: 10.5, caps: true, weight: 'light', color: ink, role: 'label'});
      this.text(s, p.title, x + 0.25, BODY + 0.72, w - 0.5, 0.9, {pt: 22, weight: 'medium', track: TRACK.title, leading: 26, color: ink, role: 'section'});
      this.text(s, p.text, x + 0.25, BODY + 1.75, w - 0.5, h - 1.95, {pt: 13, leading: 19, color: ink});
    }); return s;
  }
  metrics({eyebrow, headline, lede, metrics, footnote, section, notes, pair = 'honeydew-peacock'}) {
    count('Metrics', metrics, 4);
    const s = this.content(notes, pair, {section, kicker: eyebrow, headline, lede}), ink = s._ocean.I;
    const w = (CW - 0.25 * (metrics.length - 1)) / metrics.length, h = 2.2;
    metrics.forEach((m, i) => {
      const x = M + i * (w + 0.25);
      this.frame(s, x, BODY, w, h, ink, {corner: 'br'}); this.diamonds(s, x + w - 0.3, BODY + 0.26, i + 1, ink);
      this.text(s, m.label, x + 0.22, BODY + 0.22, w - 0.9, 0.42, {pt: 10.5, caps: true, weight: 'light', leading: 15, color: ink, role: 'label'});
      this.text(s, m.value, x + 0.22, BODY + 0.72, w - 0.4, 0.62, {pt: 34, weight: 'light', track: TRACK.display, leading: 40, color: ink, role: 'metric'});
      this.text(s, m.note, x + 0.22, BODY + 1.45, w - 0.44, 0.6, {pt: 12, leading: 16, color: ink, role: 'label'});
    });
    this.note(s, footnote); return s;
  }
  timeline({eyebrow, headline, lede, phases, footnote, section, notes, pair = 'honeydew-blackmoss'}) {
    count('Phases', phases, 5);
    const s = this.content(notes, pair, {section, kicker: eyebrow, headline, lede}), ink = s._ocean.I;
    const w = (CW - 0.3 * (phases.length - 1)) / phases.length;
    this.rule(s, M, BODY + 0.55, CW, ink);
    phases.forEach((p, i) => {
      const x = M + i * (w + 0.3);
      s.addShape('diamond', {x: x, y: BODY + 0.55 - px(9), w: px(18), h: px(18), fill: {color: ink}, line: {color: ink, width: 0}});
      this.text(s, p.label, x, BODY, w, 0.22, {pt: 10, caps: true, color: ink, role: 'label'});
      this.text(s, p.title, x, BODY + 0.85, w, 0.8, {pt: 20, weight: 'medium', track: TRACK.title, leading: 24, color: ink, role: 'section'});
      this.text(s, p.text, x, BODY + 1.75, w, 1.5, {pt: 13, leading: 19, color: ink});
    });
    this.note(s, footnote); return s;
  }
  table({eyebrow, headline, lede, header, rows, footnote, notes, colW, section, appendix = false, pair = 'honeydew-peacock'}) {
    count('Rows', rows, appendix ? 10 : 6);
    const widths = colW || header.map(() => CW / header.length);
    if (widths.length !== header.length || Math.abs(widths.reduce((a, b) => a + b, 0) - CW) > 0.02)
      throw new Error('Table column widths must sum to content width');
    const s = this.content(notes, appendix ? 'honeydew-blackmoss' : pair, {section, kicker: eyebrow, headline, lede});
    const p = s._ocean, pt = appendix ? 12 : 13;
    const data = [header, ...rows];
    const heights = data.map((row, ri) => {
      if (row.length !== header.length) throw new Error('Table row column count mismatch');
      return ri === 0 ? 0.4 : Math.max(0.42, ...row.map((cell, ci) => wrap(String(cell), widths[ci] - 0.2, pt).length * pt * 1.3 / 72 + 0.16));
    });
    if (heights.reduce((a, b) => a + b, 0) > BOTTOM - BODY) throw new Error('Table too tall; split across pages');
    s.addTable(data.map((row, ri) => row.map(cell => ({text: ri === 0 ? String(cell).toUpperCase() : String(cell), options: ri === 0
      ? {bold: true, fontSize: 9, charSpacing: 9 * TRACK.caps, color: p.I, border: [{type: 'none'}, {type: 'none'}, {type: 'solid', color: p.I, pt: 1.2}, {type: 'none'}]}
      : {color: p.I, border: [{type: 'none'}, {type: 'none'}, {type: 'solid', color: C.sage, pt: 0.5}, {type: 'none'}]}}))),
      {x: M, y: BODY, w: CW, colW: widths, rowH: heights, fontFace: FAMILY, fontSize: pt, margin: [0.06, 0.1, 0.06, 0],
        fill: {color: p.F}, valign: 'middle', autoPage: false, objectName: 'ocean:table'});
    this.note(s, footnote); return s;
  }
  // Charts: Sage for context, Cedar for the focus; every number on a data shape is Honeydew Bold (BRAND-SYSTEM.md §9).
  chart({eyebrow, headline, lede, type = 'bar', categories, series, focus = null, takeaway, footnote, valueFormat = '#,##0', section, notes, pair = 'honeydew-cedar'}) {
    if (!['bar', 'line'].includes(type)) throw new Error('Supported charts: bar, line');
    count('Series', series, 4);
    if (!categories?.length || series.some(sr => sr.values.length !== categories.length || sr.values.some(v => !Number.isFinite(v))))
      throw new Error('Chart categories and finite values must match');
    const s = this.content(notes, pair, {section, kicker: eyebrow, headline, lede}), ink = s._ocean.I;
    const cw = takeaway ? 9.2 : CW;
    const base = {x: M - 0.1, y: BODY - 0.05, w: cw, h: BOTTOM - BODY - 0.25,
      catAxisLabelFontFace: FAMILY, valAxisLabelFontFace: FAMILY, legendFontFace: FAMILY, dataLabelFontFace: FAMILY,
      catAxisLabelFontSize: 10, valAxisLabelFontSize: 10, legendFontSize: 10, dataLabelFontSize: 11,
      catAxisLabelColor: C.cedar, valAxisLabelColor: C.cedar, legendColor: ink, catAxisLineShow: true,
      catAxisLineColor: C.cedar, valAxisHidden: true, valGridLine: {style: 'none'}, catGridLine: {style: 'none'},
      showBorder: false, legendPos: 'b', valAxisLabelFormatCode: valueFormat};
    if (type === 'bar' && series.length === 1) {
      const vals = series[0].values, f = focus === null ? vals.length - 1 : focus;
      s.addChart(this.pptx.ChartType.bar, [
        {name: series[0].name, labels: categories, values: vals.map((v, i) => i === f ? 0 : v)},
        {name: `${series[0].name} (focus)`, labels: categories, values: vals.map((v, i) => i === f ? v : 0)}],
      {...base, barDir: 'col', barGrouping: 'stacked', barGapWidthPct: 38, chartColors: [C.sage, C.cedar],
        showValue: true, dataLabelPosition: 'inEnd', dataLabelColor: C.honeydew, dataLabelFontBold: true,
        dataLabelFormatCode: `${valueFormat};;;`, showLegend: false});
    } else if (type === 'bar') {
      s.addChart(this.pptx.ChartType.bar, series.map(sr => ({name: sr.name, labels: categories, values: sr.values})),
        {...base, barDir: 'col', barGapWidthPct: 50, chartColors: [C.cedar, C.sage, C.citron, C.olive], showValue: true,
          dataLabelPosition: 'inEnd', dataLabelColor: C.honeydew, dataLabelFontBold: true, dataLabelFormatCode: valueFormat, showLegend: true});
    } else {
      s.addChart(this.pptx.ChartType.line, series.map(sr => ({name: sr.name, labels: categories, values: sr.values})),
        {...base, chartColors: [C.cedar, C.sage, C.olive, C.citron], lineSize: 2.6, lineDataSymbol: 'none', showValue: false,
          showLegend: series.length > 1, valAxisHidden: false, valGridLine: {color: C.sage, size: 0.5}});
    }
    if (takeaway) {
      this.rule(s, 10.1, BODY, CW - 9.5, ink);
      this.text(s, takeaway, 10.1, BODY + 0.2, CW - 9.5, 3, {pt: 10.5, caps: true, leading: 17, color: ink});
    }
    this.note(s, footnote); return s;
  }
  caseStudy({eyebrow, headline, lede, image, imageLabel, facts, summary, section, notes, pair = 'honeydew-peacock'}) {
    count('Facts', facts, 4);
    const s = this.content(notes, pair, {section, kicker: eyebrow, headline, lede}), ink = s._ocean.I;
    const x = image ? 7.9 : M, w = image ? W - M - 7.9 : CW;
    if (image) this.image(s, image, M, BODY, 7.05, 3.1, imageLabel, s._ocean.F);
    const th = 0.7;
    facts.forEach((f, i) => {
      const y = BODY + i * (th + 0.1);
      this.frame(s, x, y, w, th, ink, {corner: 'br', c: px(24), r: px(12)});
      this.diamonds(s, x + w - 0.28, y + 0.14, i + 1, ink);
      this.text(s, f.label, x + 0.2, y + 0.1, w - 1.2, 0.2, {pt: 9.5, caps: true, weight: 'light', color: ink, role: 'label'});
      this.text(s, f.value, x + 0.2, y + 0.34, w - 0.4, 0.3, {pt: 14, weight: 'bold', color: ink});
    });
    this.text(s, summary, image ? M : x, BODY + (image ? 3.2 : facts.length * (th + 0.1) + 0.1), image ? 7.05 : w, 0.4, {pt: 12, color: ink});
    return s;
  }
  team({eyebrow, headline, lede, people, section, notes, pair = 'honeydew-blackmoss'}) {
    count('People', people, 3);
    const s = this.content(notes, pair, {section, kicker: eyebrow, headline, lede}), ink = s._ocean.I;
    const w = (CW - 0.3 * (people.length - 1)) / people.length;
    people.forEach((p, i) => {
      const x = M + i * (w + 0.3); this.rule(s, x, BODY, w, ink);
      // No supplied headshot means a typographic layout, never a fake avatar.
      if (p.photo) this.image(s, p.photo, x, BODY + 0.2, 1.0, 1.0, 'Verified headshot', s._ocean.F);
      const y = BODY + (p.photo ? 1.4 : 0.25);
      this.text(s, p.name, x, y, w, 0.5, {pt: 22, weight: 'medium', track: TRACK.title, color: ink, role: 'section'});
      this.text(s, p.role, x, y + 0.55, w, 0.4, {pt: 9.5, caps: true, leading: 14, color: ink, role: 'label'});
      this.text(s, p.bio, x, y + 1.0, w, BOTTOM - (y + 1.0), {pt: 13, leading: 19, color: ink});
    }); return s;
  }
  ask({eyebrow = 'Next steps', headline, lede, amount, amountLabel, uses = [], nextSteps = [], section, notes, pair = 'honeydew-blackmoss'}) {
    count('Uses', uses, 4); count('Next steps', nextSteps, 4);
    const s = this.content(notes, pair, {section, kicker: eyebrow, headline, lede}), ink = s._ocean.I;
    this.text(s, amountLabel, M, BODY, 5.6, 0.22, {pt: 10.5, caps: true, weight: 'light', color: ink, role: 'label'});
    this.text(s, amount, M - 0.03, BODY + 0.3, 5.6, 0.95, {pt: 60, weight: 'light', track: TRACK.display, leading: 64, color: ink, role: 'metric'});
    uses.forEach((u, i) => {
      const y = BODY + 1.45 + i * 0.44; this.rule(s, M, y, 5.6, ink, 0.5);
      this.text(s, u.label, M, y + 0.1, 3.9, 0.3, {pt: 13, color: ink});
      this.text(s, u.value, M + 3.9, y + 0.1, 1.7, 0.3, {pt: 12, caps: true, track: TRACK.label, align: 'right', color: ink});
    });
    const x = 6.8, w = W - M - x;
    nextSteps.forEach((st, i) => {
      const y = BODY + i * 0.86;
      this.frame(s, x, y, w, 0.74, ink, {corner: 'br', c: px(24), r: px(12)});
      this.diamonds(s, x + w - 0.28, y + 0.14, i + 1, ink);
      this.text(s, String(i + 1).padStart(2, '0'), x + 0.2, y + 0.12, 0.6, 0.22, {pt: 10, caps: true, weight: 'light', color: ink, role: 'label'});
      this.text(s, st, x + 0.2, y + 0.36, w - 0.6, 0.3, {pt: 13, color: ink});
    });
    return s;
  }
  appendix({title, ...args}) { return this.table({...args, eyebrow: 'Appendix', headline: title, appendix: true}); }
  back({location = 'Houston, Texas', url = 'oceanrcs.com', notes, pair = 'blackmoss-honeydew'} = {}) {
    const s = this.page(notes, pair, {texture: true}), ink = s._ocean.I;
    this.frame(s, px(48), px(48), W - px(96), H - px(96), ink, {corner: 'tl', c: px(44), r: px(20), pt: 1});
    const lh = px(180), lw = lh * 241.6 / 212.6;
    this.logo(s, 'vertical', ink, {x: (W - lw) / 2, y: px(384), h: lh});
    this.text(s, location, 3, px(624), W - 6, 0.22, {pt: 10, caps: true, weight: 'light', align: 'center', color: ink, role: 'label'});
    this.text(s, url, 3, px(660), W - 6, 0.22, {pt: 10, caps: true, align: 'center', color: ink, role: 'label'});
    return s;
  }
  async save(name) {
    if (!/^[a-z0-9][a-z0-9-]*$/.test(name)) throw new Error('Use a lowercase hyphenated output name');
    const out = path.join(ROOT, 'output/pptx', `${name}.pptx`); fs.mkdirSync(path.dirname(out), {recursive: true});
    await this.pptx.writeFile({fileName: out}); console.log(`Saved ${out} (${this.n} slides)`); return out;
  }
}
module.exports = {OceanDeck, BRAND, TOKENS, C, T, W, H, M, CW, wrap, pairing, APPROVED};
