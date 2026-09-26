// Ocean RCS slide component library.
// Every slide in every deck must be created through one of these layout functions.
// Text-fit guards throw an Error instead of shrinking text. Fix by editing content.

const fs = require("fs");
const path = require("path");
const PptxGenJS = require("pptxgenjs");

const BRAND = JSON.parse(
  fs.readFileSync(path.join(__dirname, "..", "brand", "color-system.json"), "utf8")
);
const C = { ...BRAND.colors, ...BRAND.tints };
const T = BRAND.typeScale;
const FONT_H = BRAND.fonts.heading;
const FONT_B = BRAND.fonts.body;

// Geometry (inches)
const W = 13.333;
const H = 7.5;
const M = 0.6; // safe margin
const CW = W - 2 * M; // content width
const COL = CW / 12; // 12-column grid unit (no gutters; use GUT between blocks)
const GUT = 0.3;
const HEAD_Y = 0.95; // headline top on content slides
const BODY_Y = 2.35; // body zone top on content slides
const FOOT_Y = H - 0.45;

// ---------- text-fit guard ----------
// Conservative estimate for Arial / Stack Sans: average glyph ≈ 0.52 em.
function linesNeeded(text, widthIn, pt, bold) {
  const em = bold ? 0.56 : 0.52;
  const cpl = Math.max(1, Math.floor((widthIn * 72) / (pt * em)));
  return String(text)
    .split("\n")
    .reduce((n, para) => {
      // word-wrap simulation
      const words = para.split(/\s+/).filter(Boolean);
      let lines = 1,
        cur = 0;
      for (const w of words) {
        const len = w.length + (cur ? 1 : 0);
        if (cur + len > cpl) {
          lines++;
          cur = w.length;
        } else cur += len;
      }
      return n + lines;
    }, 0);
}
function fit(label, text, widthIn, heightIn, pt, { bold = false, lineSpacing = 1.2, maxLines } = {}) {
  const pad = 0.1; // pptx inner padding both sides
  const lines = linesNeeded(text, widthIn - pad * 2, pt, bold);
  const need = (lines * pt * lineSpacing) / 72 + 0.05;
  if (need > heightIn + 0.01 || (maxLines && lines > maxLines)) {
    throw new Error(
      `[ocean fit] "${label}" does not fit (${lines} lines @ ${pt}pt in ${widthIn.toFixed(
        2
      )}x${heightIn.toFixed(2)}in). Shorten or split the content — do not reduce font size.\n  Text: ${String(
        text
      ).slice(0, 120)}`
    );
  }
  return lines;
}
function maxItems(label, arr, n) {
  if (!Array.isArray(arr) || arr.length === 0) throw new Error(`[ocean] "${label}" is empty.`);
  if (arr.length > n)
    throw new Error(`[ocean] "${label}" has ${arr.length} items; max is ${n}. Split the slide.`);
}

// ---------- deck ----------
class OceanDeck {
  constructor({ title = "Ocean RCS", confidential = true, footer = "OCEAN RCS" } = {}) {
    this.pptx = new PptxGenJS();
    this.pptx.defineLayout({ name: "OCEAN_16x9", width: W, height: H });
    this.pptx.layout = "OCEAN_16x9";
    this.pptx.title = title;
    this.pptx.company = "Ocean RCS";
    this.pptx.theme = { headFontFace: FONT_H, bodyFontFace: FONT_B };
    this.footer = footer;
    this.confidential = confidential;
    this.n = 0;
  }

  // ----- shared chrome -----
  _new(dark) {
    const s = this.pptx.addSlide();
    this.n++;
    s.background = { color: dark ? C.blackmoss : C.white };
    return s;
  }
  _footer(s, dark) {
    const col = dark ? C.sage : C.sage;
    s.addShape("line", { x: M, y: FOOT_Y - 0.08, w: CW, h: 0, line: { color: dark ? C.cedar : C.fog, width: 0.75 } });
    s.addText(this.footer + (this.confidential ? "  |  CONFIDENTIAL" : ""), {
      x: M, y: FOOT_Y, w: 6, h: 0.3, fontFace: FONT_B, fontSize: T.footnote, color: col, charSpacing: 1, margin: 0,
    });
    s.addText(String(this.n), {
      x: W - M - 1, y: FOOT_Y, w: 1, h: 0.3, fontFace: FONT_B, fontSize: T.footnote, color: col, align: "right", margin: 0,
    });
  }
  _head(s, eyebrow, headline, dark = false) {
    if (eyebrow) {
      fit("eyebrow", eyebrow.toUpperCase(), CW, 0.3, T.label, { maxLines: 1 });
      s.addText(eyebrow.toUpperCase(), {
        x: M, y: HEAD_Y - 0.45, w: CW, h: 0.3, fontFace: FONT_B, fontSize: T.label, bold: true,
        color: C.sage, charSpacing: 2, margin: 0.05,
      });
    }
    fit("headline", headline, CW * 0.85, 1.15, T.headline, { bold: true, maxLines: 2 });
    s.addText(headline, {
      x: M, y: HEAD_Y, w: CW * 0.85, h: 1.15, fontFace: FONT_H, fontSize: T.headline, bold: true,
      color: dark ? C.white : C.blackmoss, valign: "top", margin: 0.05, lineSpacingMultiple: 1.05,
    });
  }
  _image(s, img, x, y, w, h, label) {
    if (img && fs.existsSync(img)) {
      s.addImage({ path: img, x, y, w, h, sizing: { type: "cover", w, h } });
    } else {
      s.addShape("rect", { x, y, w, h, fill: { color: C.peacock }, line: { color: C.cedar, width: 1 } });
      if (w < 2 || h < 1.2) return;
      const tw = Math.min(w - 0.4, 4.6);
      s.addText(`[IMAGE: ${label || img || "to be supplied"}]`, {
        x: x + w - tw - 0.2 - (x + w >= W - 0.01 ? M - 0.2 : 0), y: y + h - 1.0 - (y + h >= H - 0.01 ? 0.4 : 0), w: tw, h: 0.8, fontFace: FONT_B, fontSize: T.label,
        color: C.sage, align: "right", valign: "bottom",
      });
    }
  }
  _bullets(s, points, x, y, w, h, { dark = false, pt = T.body, label = "points" } = {}) {
    maxItems(label, points, 3);
    fit(label, points.join("\n"), w - 0.3, h, pt, { lineSpacing: 1.45 });
    s.addText(
      points.map((p) => ({
        text: p,
        options: { bullet: { code: "25A0", indent: 18 }, color: dark ? C.white : C.blackmoss, paraSpaceAfter: 10 },
      })),
      { x, y, w, h, fontFace: FONT_B, fontSize: pt, valign: "top", margin: 0.05, lineSpacingMultiple: 1.15 }
    );
  }
  _notes(s, notes) {
    if (notes) s.addNotes(notes);
  }

  // ----- 1. Cinematic cover -----
  cover({ title, subtitle, date, image, imageLabel, notes }) {
    const s = this._new(true);
    this._image(s, image, 0, 0, W, H, imageLabel || "Higgsfield cover visual, 16:9, no text");
    s.addShape("rect", { x: 0, y: 0, w: W * 0.62, h: H, fill: { color: C.blackmoss, transparency: 12 }, line: { type: "none" } });
    s.addShape("rect", { x: M, y: 1.4, w: 0.9, h: 0.06, fill: { color: C.sage }, line: { type: "none" } });
    s.addText("OCEAN RCS", { x: M, y: 0.6, w: 5, h: 0.4, fontFace: FONT_H, fontSize: T.label + 1, bold: true, color: C.white, charSpacing: 4, margin: 0 });
    const cl = fit("cover title", title, 7.2, 2.6, T.coverTitle, { bold: true, maxLines: 3 });
    const subY = 1.7 + (cl * T.coverTitle * 1.2) / 72 + 0.45;
    s.addText(title, { x: M, y: 1.7, w: 7.2, h: subY - 1.75, fontFace: FONT_H, fontSize: T.coverTitle, bold: true, color: C.white, valign: "top", margin: 0, lineSpacingMultiple: 1.0 });
    if (subtitle) {
      fit("cover subtitle", subtitle, 6.8, 1.0, T.subhead + 2);
      s.addText(subtitle, { x: M, y: subY, w: 6.8, h: 1.0, fontFace: FONT_B, fontSize: T.subhead + 2, color: C.fog, valign: "top", margin: 0 });
    }
    if (date) s.addText(date, { x: M, y: H - 1.1, w: 5, h: 0.35, fontFace: FONT_B, fontSize: T.label, color: C.sage, margin: 0 });
    this._notes(s, notes);
    return s;
  }

  // ----- 2. Section divider -----
  divider({ number, title, subtitle, image, imageLabel, notes }) {
    const s = this._new(true);
    const split = W * 0.48;
    this._image(s, image, split, 0, W - split, H, imageLabel || "section visual");
    if (number) s.addText(String(number).padStart(2, "0"), { x: M, y: 1.6, w: 3, h: 1.0, fontFace: FONT_H, fontSize: 54, bold: true, color: C.cedar, margin: 0 });
    const dl = fit("divider title", title, split - M - 0.5, 1.9, T.dividerTitle, { bold: true, maxLines: 3 });
    const dSubY = 2.8 + (dl * T.dividerTitle * 1.15) / 72 + 0.3;
    s.addText(title, { x: M, y: 2.8, w: split - M - 0.5, h: dSubY - 2.85, fontFace: FONT_H, fontSize: T.dividerTitle, bold: true, color: C.white, valign: "top", margin: 0 });
    if (subtitle) {
      fit("divider subtitle", subtitle, split - M - 0.5, 1.0, T.subhead);
      s.addText(subtitle, { x: M, y: dSubY, w: split - M - 0.5, h: 1.0, fontFace: FONT_B, fontSize: T.subhead, color: C.sageLight, valign: "top", margin: 0 });
    }
    this._footer(s, true);
    this._notes(s, notes);
    return s;
  }

  // ----- 3. One idea / one image -----
  statement({ eyebrow, headline, support, image, imageLabel, notes }) {
    const s = this._new(true);
    const split = W * 0.5;
    this._image(s, image, split, 0, W - split, H, imageLabel);
    if (eyebrow) s.addText(eyebrow.toUpperCase(), { x: M, y: 1.5, w: split - M, h: 0.3, fontFace: FONT_B, fontSize: T.label, bold: true, color: C.sage, charSpacing: 2, margin: 0 });
    const sl = fit("statement headline", headline, split - M - 0.5, 2.4, 32, { bold: true, maxLines: 4 });
    const sSubY = 1.9 + (sl * 32 * 1.15) / 72 + 0.35;
    s.addText(headline, { x: M, y: 1.9, w: split - M - 0.5, h: sSubY - 1.95, fontFace: FONT_H, fontSize: 32, bold: true, color: C.white, valign: "top", margin: 0 });
    if (support) {
      fit("statement support", support, split - M - 0.5, 1.4, T.subhead);
      s.addText(support, { x: M, y: sSubY, w: split - M - 0.5, h: 1.4, fontFace: FONT_B, fontSize: T.subhead, color: C.fog, valign: "top", margin: 0 });
    }
    this._footer(s, true);
    this._notes(s, notes);
    return s;
  }

  // ----- 4. Two column (problem -> solution) -----
  twoColumn({ eyebrow, headline, left, right, notes }) {
    const s = this._new(false);
    this._head(s, eyebrow, headline);
    const colW = (CW - 1.0) / 2;
    const h = FOOT_Y - BODY_Y - 0.35;
    [[left, M, C.mist, C.blackmoss], [right, M + colW + 1.0, C.peacock, C.white]].forEach(([col, x, bg, fg], i) => {
      s.addShape("rect", { x, y: BODY_Y, w: colW, h, fill: { color: bg }, line: { type: "none" } });
      s.addShape("rect", { x, y: BODY_Y, w: colW, h: 0.07, fill: { color: i ? C.sage : C.cedar }, line: { type: "none" } });
      s.addText(col.label.toUpperCase(), { x: x + 0.35, y: BODY_Y + 0.3, w: colW - 0.7, h: 0.35, fontFace: FONT_B, fontSize: T.label, bold: true, color: i ? C.sageLight : C.cedar, charSpacing: 2, margin: 0 });
      this._bullets(s, col.points, x + 0.35, BODY_Y + 0.85, colW - 0.7, h - 1.1, { dark: i === 1, label: col.label });
    });
    s.addText("→", { x: M + colW, y: BODY_Y + h / 2 - 0.4, w: 1.0, h: 0.8, fontFace: FONT_H, fontSize: 32, color: C.cedar, align: "center", valign: "middle", margin: 0 });
    this._footer(s, false);
    this._notes(s, notes);
    return s;
  }

  // ----- 5. Three pillars -----
  pillars({ eyebrow, headline, pillars, notes }) {
    maxItems("pillars", pillars, 3);
    const s = this._new(false);
    this._head(s, eyebrow, headline);
    const n = pillars.length;
    const pw = (CW - GUT * (n - 1)) / n;
    const h = FOOT_Y - BODY_Y - 0.35;
    pillars.forEach((p, i) => {
      const x = M + i * (pw + GUT);
      s.addShape("rect", { x, y: BODY_Y, w: pw, h, fill: { color: C.mist }, line: { type: "none" } });
      s.addShape("rect", { x, y: BODY_Y, w: 0.07, h, fill: { color: C.cedar }, line: { type: "none" } });
      s.addText(String(i + 1).padStart(2, "0"), { x: x + 0.35, y: BODY_Y + 0.3, w: 1, h: 0.45, fontFace: FONT_H, fontSize: 22, bold: true, color: C.sage, margin: 0 });
      fit(`pillar ${i + 1} title`, p.title, pw - 0.6, 0.9, 20, { bold: true, maxLines: 2 });
      s.addText(p.title, { x: x + 0.35, y: BODY_Y + 0.85, w: pw - 0.6, h: 0.9, fontFace: FONT_H, fontSize: 20, bold: true, color: C.blackmoss, valign: "top", margin: 0 });
      fit(`pillar ${i + 1} text`, p.text, pw - 0.6, h - 2.1, T.body, { lineSpacing: 1.3 });
      s.addText(p.text, { x: x + 0.35, y: BODY_Y + 1.85, w: pw - 0.6, h: h - 2.1, fontFace: FONT_B, fontSize: T.body, color: C.peacock, valign: "top", margin: 0, lineSpacingMultiple: 1.15 });
    });
    this._footer(s, false);
    this._notes(s, notes);
    return s;
  }

  // ----- 6. Metric cards -----
  metrics({ eyebrow, headline, metrics, footnote, notes }) {
    maxItems("metrics", metrics, 4);
    const s = this._new(false);
    this._head(s, eyebrow, headline);
    const n = metrics.length;
    const mw = (CW - GUT * (n - 1)) / n;
    const y = BODY_Y + 0.3, h = 2.9;
    metrics.forEach((m, i) => {
      const x = M + i * (mw + GUT);
      s.addShape("rect", { x, y, w: mw, h, fill: { color: i === 0 ? C.peacock : C.mist }, line: { type: "none" } });
      fit(`metric ${i + 1} value`, m.value, mw - 0.5, 1.1, 40, { bold: true, maxLines: 1 });
      s.addText(m.value, { x: x + 0.3, y: y + 0.35, w: mw - 0.5, h: 1.1, fontFace: FONT_H, fontSize: 40, bold: true, color: i === 0 ? C.white : C.cedar, margin: 0 });
      fit(`metric ${i + 1} label`, m.label, mw - 0.5, 0.75, T.body, { bold: true });
      s.addText(m.label, { x: x + 0.3, y: y + 1.5, w: mw - 0.5, h: 0.75, fontFace: FONT_B, fontSize: T.body, bold: true, color: i === 0 ? C.white : C.blackmoss, valign: "top", margin: 0 });
      if (m.note) {
        fit(`metric ${i + 1} note`, m.note, mw - 0.5, 0.5, T.label);
        s.addText(m.note, { x: x + 0.3, y: y + 2.3, w: mw - 0.5, h: 0.5, fontFace: FONT_B, fontSize: T.label, color: i === 0 ? C.sageLight : C.sage, valign: "top", margin: 0 });
      }
    });
    this._footnote(s, footnote);
    this._footer(s, false);
    this._notes(s, notes);
    return s;
  }

  // ----- 7. Timeline / phased deployment -----
  timeline({ eyebrow, headline, phases, footnote, notes }) {
    maxItems("phases", phases, 5);
    const s = this._new(false);
    this._head(s, eyebrow, headline);
    const n = phases.length;
    const pw = (CW - GUT * (n - 1)) / n;
    const lineY = BODY_Y + 0.55;
    s.addShape("line", { x: M, y: lineY, w: CW, h: 0, line: { color: C.fog, width: 2 } });
    phases.forEach((p, i) => {
      const x = M + i * (pw + GUT);
      s.addShape("ellipse", { x: x, y: lineY - 0.14, w: 0.28, h: 0.28, fill: { color: i === 0 ? C.cedar : C.sage }, line: { color: C.white, width: 2 } });
      s.addText(p.label.toUpperCase(), { x, y: BODY_Y - 0.15, w: pw, h: 0.35, fontFace: FONT_B, fontSize: T.label, bold: true, color: C.sage, charSpacing: 1, margin: 0 });
      fit(`phase ${i + 1} title`, p.title, pw - 0.1, 0.85, 19, { bold: true, maxLines: 2 });
      s.addText(p.title, { x, y: lineY + 0.4, w: pw - 0.1, h: 0.85, fontFace: FONT_H, fontSize: 19, bold: true, color: C.blackmoss, valign: "top", margin: 0 });
      fit(`phase ${i + 1} text`, p.text, pw - 0.1, 2.2, T.body, { lineSpacing: 1.3 });
      s.addText(p.text, { x, y: lineY + 1.35, w: pw - 0.1, h: 2.2, fontFace: FONT_B, fontSize: T.body, color: C.peacock, valign: "top", margin: 0, lineSpacingMultiple: 1.15 });
    });
    this._footnote(s, footnote);
    this._footer(s, false);
    this._notes(s, notes);
    return s;
  }

  // ----- 8. Comparison table -----
  table({ eyebrow, headline, header, rows, footnote, notes, colW, appendix = false }) {
    if (rows.length > (appendix ? 10 : 6))
      throw new Error(`[ocean] table has ${rows.length} rows; max ${appendix ? 10 : 6}. Split or move to appendix.`);
    const s = this._new(false);
    this._head(s, eyebrow, headline);
    const pt = appendix ? T.label : 15;
    const widths = colW || header.map(() => CW / header.length);
    const rowH = appendix ? 0.38 : 0.55;
    const data = [
      header.map((h) => ({ text: h, options: { bold: true, color: C.white, fill: { color: C.peacock }, fontSize: T.label } })),
      ...rows.map((r, ri) =>
        r.map((c, ci) => ({ text: String(c), options: { color: C.blackmoss, bold: ci === 0, fill: { color: ri % 2 ? C.white : C.mist }, fontSize: pt } }))
      ),
    ];
    const maxH = FOOT_Y - BODY_Y - 0.7;
    if ((rows.length + 1) * rowH > maxH + 0.01) throw new Error("[ocean] table too tall. Reduce rows.");
    rows.forEach((r, ri) => r.forEach((c, ci) => fit(`table r${ri + 1}c${ci + 1}`, String(c), widths[ci], rowH * 1.6, pt, { maxLines: 2 })));
    s.addTable(data, { x: M, y: BODY_Y, w: CW, colW: widths, rowH, fontFace: FONT_B, valign: "middle", margin: [0.05, 0.12, 0.05, 0.12], border: { type: "solid", color: C.fog, pt: 0.5 } });
    this._footnote(s, footnote);
    this._footer(s, false);
    this._notes(s, notes);
    return s;
  }

  // ----- 9. Native chart -----
  chart({ eyebrow, headline, type = "bar", categories, series, takeaway, footnote, valueFormat = "#,##0", notes }) {
    const s = this._new(false);
    this._head(s, eyebrow, headline);
    const chartW = takeaway ? CW * 0.66 : CW;
    const palette = [C.cedar, C.sage, C.peacock, C.sageLight];
    const t = { bar: this.pptx.ChartType.bar, line: this.pptx.ChartType.line }[type];
    s.addChart(t, series.map((sr) => ({ name: sr.name, labels: categories, values: sr.values })), {
      x: M, y: BODY_Y, w: chartW, h: FOOT_Y - BODY_Y - 0.75,
      barDir: "col", barGapWidthPct: 60, chartColors: palette.slice(0, series.length),
      catAxisLabelFontSize: T.label, valAxisLabelFontSize: T.label, catAxisLabelColor: C.peacock, valAxisLabelColor: C.peacock,
      catAxisLabelFontFace: FONT_B, valAxisLabelFontFace: FONT_B, valAxisLabelFormatCode: valueFormat,
      valGridLine: { color: C.fog, size: 0.5 }, catGridLine: { style: "none" },
      showLegend: series.length > 1, legendPos: "t", legendFontSize: T.label, legendFontFace: FONT_B,
      showValue: series.length === 1, dataLabelFontSize: T.label, dataLabelColor: C.blackmoss, dataLabelFormatCode: valueFormat,
      lineSize: 3, lineDataSymbolSize: 8,
    });
    if (takeaway) {
      const x = M + chartW + GUT, w = CW - chartW - GUT;
      s.addShape("rect", { x, y: BODY_Y, w, h: FOOT_Y - BODY_Y - 0.75, fill: { color: C.peacock }, line: { type: "none" } });
      s.addText("TAKEAWAY", { x: x + 0.3, y: BODY_Y + 0.3, w: w - 0.6, h: 0.3, fontFace: FONT_B, fontSize: T.label, bold: true, color: C.sageLight, charSpacing: 2, margin: 0 });
      fit("chart takeaway", takeaway, w - 0.6, 3.0, T.subhead + 2, { lineSpacing: 1.3 });
      s.addText(takeaway, { x: x + 0.3, y: BODY_Y + 0.75, w: w - 0.6, h: 3.0, fontFace: FONT_H, fontSize: T.subhead + 2, color: C.white, valign: "top", margin: 0, lineSpacingMultiple: 1.15 });
    }
    this._footnote(s, footnote);
    this._footer(s, false);
    this._notes(s, notes);
    return s;
  }

  // ----- 10. Case study / project -----
  caseStudy({ eyebrow, headline, image, imageLabel, facts, summary, notes }) {
    maxItems("case facts", facts, 4);
    const s = this._new(false);
    this._head(s, eyebrow, headline);
    const imgW = CW * 0.5, h = FOOT_Y - BODY_Y - 0.35;
    this._image(s, image, M, BODY_Y, imgW, h, imageLabel || "project photo");
    const x = M + imgW + 0.5, w = CW - imgW - 0.5;
    facts.forEach((f, i) => {
      const y = BODY_Y + i * 0.72;
      s.addText(f.label.toUpperCase(), { x, y, w: w * 0.45, h: 0.6, fontFace: FONT_B, fontSize: T.label, bold: true, color: C.sage, valign: "middle", margin: 0, charSpacing: 1 });
      fit(`fact ${i + 1}`, f.value, w * 0.55, 0.6, T.body, { bold: true, maxLines: 2 });
      s.addText(f.value, { x: x + w * 0.45, y, w: w * 0.55, h: 0.6, fontFace: FONT_B, fontSize: T.body, bold: true, color: C.blackmoss, valign: "middle", margin: 0 });
      s.addShape("line", { x, y: y + 0.66, w, h: 0, line: { color: C.fog, width: 0.75 } });
    });
    if (summary) {
      const y = BODY_Y + facts.length * 0.72 + 0.25;
      fit("case summary", summary, w, FOOT_Y - y - 0.35, T.body, { lineSpacing: 1.3 });
      s.addText(summary, { x, y, w, h: FOOT_Y - y - 0.35, fontFace: FONT_B, fontSize: T.body, color: C.peacock, valign: "top", margin: 0, lineSpacingMultiple: 1.15 });
    }
    this._footer(s, false);
    this._notes(s, notes);
    return s;
  }

  // ----- 11. Team / credibility -----
  team({ eyebrow, headline, people, notes }) {
    maxItems("people", people, 4);
    const s = this._new(false);
    this._head(s, eyebrow, headline);
    const n = people.length, pw = (CW - GUT * (n - 1)) / n, h = FOOT_Y - BODY_Y - 0.35;
    people.forEach((p, i) => {
      const x = M + i * (pw + GUT);
      s.addShape("rect", { x, y: BODY_Y, w: pw, h, fill: { color: C.mist }, line: { type: "none" } });
      this._image(s, p.photo, x + 0.3, BODY_Y + 0.3, 1.1, 1.1, "photo");
      fit(`person ${i + 1} name`, p.name, pw - 0.6, 0.45, 19, { bold: true, maxLines: 1 });
      s.addText(p.name, { x: x + 0.3, y: BODY_Y + 1.6, w: pw - 0.6, h: 0.45, fontFace: FONT_H, fontSize: 19, bold: true, color: C.blackmoss, margin: 0 });
      s.addText(p.role, { x: x + 0.3, y: BODY_Y + 2.05, w: pw - 0.6, h: 0.35, fontFace: FONT_B, fontSize: T.label, bold: true, color: C.cedar, margin: 0 });
      fit(`person ${i + 1} bio`, p.bio, pw - 0.6, h - 2.75, T.body - 1 < 16 ? 16 : T.body, { lineSpacing: 1.3 });
      s.addText(p.bio, { x: x + 0.3, y: BODY_Y + 2.5, w: pw - 0.6, h: h - 2.75, fontFace: FONT_B, fontSize: T.body, color: C.peacock, valign: "top", margin: 0 });
    });
    this._footer(s, false);
    this._notes(s, notes);
    return s;
  }

  // ----- 12. Ask / next steps -----
  ask({ eyebrow = "The ask", headline, amount, amountLabel, uses = [], nextSteps = [], notes }) {
    const s = this._new(true);
    this._head(s, eyebrow, headline, true);
    const lw = CW * 0.42;
    s.addShape("rect", { x: M, y: BODY_Y, w: lw, h: FOOT_Y - BODY_Y - 0.35, fill: { color: C.peacock }, line: { type: "none" } });
    fit("ask amount", amount, lw - 0.6, 1.2, 48, { bold: true, maxLines: 1 });
    s.addText(amount, { x: M + 0.3, y: BODY_Y + 0.3, w: lw - 0.6, h: 1.2, fontFace: FONT_H, fontSize: 48, bold: true, color: C.white, margin: 0 });
    if (amountLabel) s.addText(amountLabel, { x: M + 0.3, y: BODY_Y + 1.45, w: lw - 0.6, h: 0.4, fontFace: FONT_B, fontSize: T.body, color: C.sageLight, margin: 0 });
    maxItems("uses of funds", uses, 4);
    uses.forEach((u, i) => {
      const y = BODY_Y + 2.05 + i * 0.5;
      s.addText(u.label, { x: M + 0.3, y, w: lw - 1.9, h: 0.45, fontFace: FONT_B, fontSize: T.body, color: C.white, margin: 0, valign: "middle" });
      s.addText(u.value, { x: M + lw - 1.6, y, w: 1.3, h: 0.45, fontFace: FONT_B, fontSize: T.body, bold: true, color: C.sageLight, align: "right", margin: 0, valign: "middle" });
    });
    const x = M + lw + 0.6, w = CW - lw - 0.6;
    s.addText("NEXT STEPS", { x, y: BODY_Y, w, h: 0.35, fontFace: FONT_B, fontSize: T.label, bold: true, color: C.sage, charSpacing: 2, margin: 0 });
    maxItems("next steps", nextSteps, 4);
    nextSteps.forEach((st, i) => {
      const y = BODY_Y + 0.6 + i * 0.95;
      s.addText(String(i + 1), { x, y, w: 0.5, h: 0.5, fontFace: FONT_H, fontSize: 20, bold: true, color: C.blackmoss, align: "center", valign: "middle", fill: { color: C.sage }, margin: 0 });
      fit(`next step ${i + 1}`, st, w - 0.8, 0.85, T.body + 1, { maxLines: 2 });
      s.addText(st, { x: x + 0.75, y: y - 0.1, w: w - 0.8, h: 0.8, fontFace: FONT_B, fontSize: T.body + 1, color: C.white, valign: "middle", margin: 0 });
    });
    this._footer(s, true);
    this._notes(s, notes);
    return s;
  }

  // ----- 13. Appendix table -----
  appendix({ title, header, rows, footnote, colW, notes }) {
    return this.table({ eyebrow: "Appendix", headline: title, header, rows, footnote, colW, notes, appendix: true });
  }

  _footnote(s, text) {
    if (!text) return;
    fit("footnote", text, CW, 0.35, T.footnote, { maxLines: 2 });
    s.addText(text, { x: M, y: FOOT_Y - 0.5, w: CW, h: 0.35, fontFace: FONT_B, fontSize: T.footnote, color: C.sage, valign: "bottom", margin: 0 });
  }

  async save(name) {
    const out = path.join(__dirname, "..", "output", "pptx", `${name}.pptx`);
    fs.mkdirSync(path.dirname(out), { recursive: true });
    await this.pptx.writeFile({ fileName: out });
    console.log(`Saved ${out} (${this.n} slides)`);
    return out;
  }
}

module.exports = { OceanDeck, BRAND, C, T, W, H, M, CW };
