# Ocean RCS — Approved Decisions and Document Profiles

Status: approved by Ocean leadership on 26 September 2026 (Houston).
Controlling authority: `Ocean_StyleGuide_2026.pdf` (the brand bible).
Companion specs, in order of precedence:
1. This file (decisions and document profiles)
2. "Ocean Brand Bible — Typography, Weight and Text-System Rules"
3. "Ocean Brand Guide Page-by-Page Analysis"
4. "Ocean Style Guide Independent Audit" (turn 1; superseded where 1–3 differ)

---

## Part 1 — Decision register

| # | Decision | Approved rule | Changeable later? |
|---|---|---|---|
| D1 | Authority and scope | The Style Guide 2026 controls. **The system now governs every Ocean surface: oceanrcs.com, Ocean micro-apps, decks, reports, proposals, formal documents, cards, email, signage, charts, icons and graphics** (see "Ocean Brand System Spec"). The current oceanrcs.com is still not a design reference; it is a target to be rebuilt to this system | Updated 26 Sep 2026 |
| D2 | Body-text contrast | Body text in proposals, reports, contracts and investor/lender decks must reach at least 4.5:1 against its field. The guide's lower-contrast pairs (3.6–4.5:1) are allowed only for type 25 pt and larger and for brand pieces | — |
| D3 | Deck and document type sizes | Rule 9 of the typography file is approved as written. Weights, case, tracking and line-spacing ratios are fixed. **Sizes live in one token file (`brand/type-scale.json`) so they can be changed later without touching layouts.** Minimums: 10.5 pt on slides; 7.5 pt for tracked caps in print | **Yes — flagged for possible revision by leadership** |
| D4 | Canvas | Honeydew `#F3FBF8` is Ocean's off-white and the default light background. White `#FFFFFF` is used only for print-destined pages (contracts, transactional documents, appendices) where a full-bleed tint is impractical | — |
| D5 | Logo color | One brand color per placement, normally the page's ink. Never black `#000000`, never mixed colors, never non-brand colors. Build from the official SVG/EPS masters | — |
| D6 | Default cover | **Sage field + Honeydew ink/logo** with a code-generated tonal texture in the manner of the guide cover (see Part 3). Approved alternates: Honeydew field + Sage ink (light), Blackmoss field + Honeydew ink (premium/investor). All three are approved pairings on Guide 05 | — |
| D7 | Guide errata | Confirmed. The second "Blackmoss + Citron" tile on Guide 05 is **Blackmoss + Crimson**. "Sprig + Citron" is a duplicate. The approved matrix has 30 unique pairs | — |
| D8 | Crimson | One Crimson "moment" per deck (large type), plus small accents where design allows (Part 4) | — |
| D9 | Textures behind text | Allowed under the guide's own limits (Part 5). Never on contract, transactional or report body pages | — |
| D10 | Image sources | All sources are equal and may be mixed in any order: Ocean project photos, licensed or free-license stock, and any high-quality AI image generator (Higgsfield or other top-rated models). Two integrity limits apply (Part 6) | — |
| D11 | Staging header | Required on every interior slide and report/proposal page, adapted to 16:9 and Letter. **Not used on formal documents (D13)** | Updated 26 Sep 2026 |
| D12 | Pairing rotation | 2–4 approved pairings per deck or document, rotated by section. Never one pairing for everything | — |
| D13 | Formal documents | Plain institutional standard: White, Blackmoss only, logo on page 1 (graphic mark on continuation pages), sentence-case numbered headings, left-aligned body, no tracked caps, header frame, textures, photos, chamfers, icons or color. One diamond as the end-of-document mark. **Legal documents are set in Times New Roman; letters and transactional documents in Stack Sans** (Spec §6) | **Approved 26 Sep 2026** |
| D14 | Tokens first | Every surface reads colors, weights, tracking, radius, chamfer and icon settings from `tokens/`. Hard-coded values fail QA (Spec §2) | **Approved 26 Sep 2026** |
| D15 | Icons | Material Symbols Outlined, weight 400, fill 0, grade 0, optical size 24; icon = 50% of its cell. Measured from the guide's header strip (Spec §3, §10) | **Approved 26 Sep 2026** |
| D16 | Charts | Sage for context, Cedar for the focus; max four categories in fixed order; **every number on a data shape is Honeydew Bold**; vector output, animated entry on screen; Crimson flags one value; direct labels and chips; no pies, 3D or gradients (Spec §9) | **Approved 26 Sep 2026** |
| D17 | Deck length | Deck recipes scale from 1 to 30 slides; above 20, split into a deck plus a report (Spec §8) | **Approved 26 Sep 2026** |
| D18 | Sage + Honeydew | Measured at 3.6:1, so it is for large text and graphics only: covers, card fronts, hero lines. Never body text | **Approved 26 Sep 2026** |
| D19 | Business cards, email, signage | Profiles in Spec §7, §12, §13. Card extras approved: registered emboss, optional Sage edge, and a personal QR code linking to oceanrcs.com. Arial is the only substitute font in email | **Approved 26 Sep 2026** |
| D20 | Web and apps | oceanrcs.com defaults to Honeydew + Blackmoss with section pairings; micro-apps default to Blackmoss + Honeydew **with an approved Honeydew + Peacock alternative and a user toggle**; Crimson in apps only for alerts (Spec §4) | **Approved 26 Sep 2026** |

---
| D21 | Logo sizing and the graphic mark | Minimum logo sizes per surface are fixed in Spec §16 (for example 44 px in the web header, 28 pt on letters, 0.9 in on the card front). The graphic mark alone is used for app icons, continuation pages, photo corners, chart sheets and signage corners | **Approved 26 Sep 2026** |

## Part 2 — Pairing reference (30 approved)

Blackmoss + Peacock, Cedar, Sage, Honeydew, Sprig, Olive, Citron, Crimson ·
Peacock + Cedar, Sage, Honeydew, Sprig, Olive, Citron, Crimson ·
Cedar + Sage, Honeydew, Sprig, Olive, Citron ·
Sage + Honeydew, Sprig ·
Honeydew + Sprig, Olive, Citron, Crimson ·
Sprig + Olive, Citron, Crimson ·
Olive + Citron

Not approved: Cedar + Crimson, Sage + Olive, Sage + Citron, Sage + Crimson, Olive + Crimson, Citron + Crimson.

---

## Part 3 — Cover system (D6)

The guide's cover texture can be recreated. A proof was built in this session: a particle-wave field drawn in code in exact palette colors, fading to a flat field behind the type. Codex should build it as a reusable generator (`scripts/make_texture.py`) so every cover texture is:
- drawn in the cover's own two colors only (texture = ink color at 35–55% opacity, or a tonal partner such as Sage on Blackmoss);
- fully deterministic (same seed, same image), so there are no stock or AI licensing questions;
- faded out below about 50% of the height, so the title sits on a flat field;
- exported at 2× for decks and at 300 dpi for Letter.

Cover composition (all three variants):
- Hairline frame inset at the margin, with the single top-left 45° chamfer (the guide's back-cover device).
- Vertical lockup, top-left, in the ink color.
- Year and meta block right-aligned at top-right (the guide's only right-aligned device): year Regular 30-scale; meta keys Light and value Bold, tracked caps.
- Kicker: Bold tracked caps. Title: Light display, −0.04 em, two lines.
- Closing rule and a key/value footer ("PROPOSAL NO." Light → "0001" Bold; "PREPARED FOR" Light → client Bold).
- No Crimson on Sage covers (Sage + Crimson is not approved).

---

## Part 4 — Crimson accents (D8)

Design reasoning: Crimson is the palette's only hot color, and the guide uses it for warnings (the triangle markers on Guide 03) and for one full-page pairing (Guide 08). Small accents work, provided they stay rare and keep one meaning.

- **Where allowed:** only on Blackmoss, Peacock, Honeydew or Sprig fields (its approved partners). Never on Sage, Cedar, Olive or Citron fields.
- **What it may mark:** one key number per page, a risk or warning flag, the active navigation chip, or a single diamond marker.
- **Budget:** one large Crimson moment per deck; at most one small accent per page; none in body text.
- **Meaning:** attention or warning. Never decoration, and never a chart series unless that series is the flagged value.
- **Contracts and transactional documents:** Crimson only for legal warnings (for example "PAST DUE" or a required notice), nothing else.

---

## Part 5 — Textures and marks behind text (D9)

Answer to leadership's question: **no, the guide does not say textures can never sit behind body text.** That was my rule, not the guide's. What the guide says and does:
- Guide 08: abstract and edited imagery "can be used… as textural background elements and secondary visuals… best utilized in lower-contrast, as to not pull too much attention away from brand messaging, information, UI elements or relevant photography."
- Guide 01: the graphic-only logo "can also be used as a branded decorative graphical element."
- Guide 06 places an oversized Citron mark **directly behind its lede and body text** on a Sprig field. Measured contrast between the mark and the field: **1.79:1**.
- No page puts text on top of photography.

Rules derived from the guide:
1. A texture or oversized mark may sit behind text if its contrast against the field is no more than about 1.8:1 (the guide's own example).
2. The text must still meet D2 against both the field and the texture.
3. Never behind body text on photographs, and never on contract, transactional or report body pages (legibility and print reproduction).
4. Covers, section dividers, statement slides and brand pieces may use textures freely within rules 1–2.

---

## Part 6 — Image sources (D10)

**Sources — no priority order.** Any of these may be used anywhere, alone or mixed, chosen purely on quality and fit:
- Ocean project photos
- Stock photography (paid-license or free-license libraries)
- AI-generated images from any high-quality generator (Higgsfield or other top-rated image models), chosen for resolution and realism

**Quality bar (applies to every source):** high resolution (at least 2× the placed size; 300 dpi at print size); natural light and real textures; no staged, over-polished or obviously synthetic look (the guide's "avoid generic staged scenes or overly polished edits"); no AI-generated text, logos or distorted hands, panels or equipment. The real Ocean logo is always placed in layout, never generated into an image.

**Two integrity limits (the only restrictions):**
1. **Never present an image as Ocean's own work unless it is.** A stock or AI image can show solar, storage, crews or sites generically, but it must not be captioned or positioned as a specific Ocean project, client or crew. Case studies and "our work" sections use real Ocean photos.
2. **Report evidence must be real.** When an image is used as evidence (a site photo, roof condition, equipment nameplate, existing service), it must be a real photo of that site. AI or stock may still be used for covers, dividers and illustrative figures in reports.

**Photos you don't have rights to:** leadership asked to allow unlicensed photos. Recommendation: treat free-license libraries (e.g. Unsplash, Pexels) as allowed, but don't use copyrighted photos without permission in commercial materials. That creates takedown and infringement exposure on proposals and investor decks that are sent outside Ocean. **Needs a leadership decision.**

**Manifest:** every image is logged in `assets/image-manifest.json` with its source type (Ocean / stock / AI), file, date, and license or prompt. This makes the two limits checkable and keeps a record if anything is questioned later.

**Treatment rules (Guides 04, 07, 08):**
- Photos go in the rounded-plus-chamfer mask.
- Pair a gradient-mapped or overlaid image with an unaltered one on the same spread.
- Overlays and gradient maps use one approved pairing only.
- Alternate nature and industry when images sit side by side.

---

## Part 7 — Document profiles

Each Ocean deliverable has a fixed configuration. Codex should build each one as a named profile (for example `profile: "proposal"`) that sets the format, pairings, components and QA checks automatically.

### Reports and presentations are separate systems

Reports and presentations share the brand (palette, pairings, type ladder ratios, logo, geometry), but they are built for different jobs and must never be generated from the same template.

| | Reports (P3, and P2 proposals as a close relative) | Presentations (P4, P5, P6) |
|---|---|---|
| Job | Read, studied, filed, forwarded; the document is the record | Presented or skimmed on screen; the speaker or story carries the detail |
| Format | Letter portrait PDF (DOCX where editing is needed) | 16:9 PPTX, exported to PDF for sending |
| Density | Full paragraphs, tables and appendices; 400–600 words a page is normal | One idea per slide; a headline plus at most about 40 words; no paragraphs |
| Body type | 9.5–10 pt Regular, justified, 1.55 leading | 14–16 pt Regular, left or justified, only where text is unavoidable |
| Titles | Page and section titles in the Medium 22–24 pt style; numbered sections (01, 02…) | Slide headline Medium 32–36 pt, written as the takeaway |
| Grid | Two-column text grid (kicker/title left, text right, as on the guide's pages) | Full-bleed 16:9 grid; the 12-column system scaled to 13.33 in |
| Header | Staging header on every page, plus a running footer with report ID, date and "Page 01 of 24" | Staging header on content slides; none on cover, dividers and statement slides |
| Color | Honeydew + Blackmoss or Peacock for reading pages; one section pairing per chapter; appendices on White | 2–4 pairings rotated by section, including dark full-field slides |
| Imagery | Evidence and figures, captioned with source and date; evidence photos must be real | Atmosphere and proof; large photo cards and full-bleed images |
| Textures | Cover and dividers only | Cover, dividers, statement slides |
| Charts | Detailed, with axes, sources and data tables in the appendix | One message per chart, highlighted value, minimal axes |
| Tables | Multi-page, repeating headers | Short (≤ 6 rows); detail goes to an appendix or leave-behind |
| Crimson | Risk flags only | One moment per deck, plus small accents |
| Navigation | Contents page, section numbers, cross-references | Agenda slide (Bold display allowed), section dividers |
| Output QA | Page-by-page render, text flow, widows and orphans, table breaks, PDF/A | Slide-by-slide render, overflow, speaker notes, opens in PowerPoint and Keynote |

A report delivered as slides (for example a quarterly investor update) uses the presentation system, with its detailed data moved to a report-style appendix PDF.

### Summary matrix

| Profile | Format | Cover | Interior field + ink | Textures | Photos | Crimson | Header |
|---|---|---|---|---|---|---|---|
| **P1 Contracts and legal** (EPC agreement, MSA, PPA, NDA, lien waiver) | Letter, print | White title page, Blackmoss ink | White + Blackmoss | No | No | Legal warnings only | Compact |
| **P2 Commercial proposals** | Letter, digital-first | D6 default (Sage + Honeydew) | Honeydew + Blackmoss; sections rotate Honeydew + Peacock / Honeydew + Cedar | Cover, dividers | Yes | One accent per page | Full |
| **P3 Technical and feasibility reports** | Letter | D6 default | Honeydew + Blackmoss or Peacock | Cover and dividers | Any source; evidence photos real | Risk flags only | Full + running footer |
| **P4 Investor and lender decks** | 16:9 | Blackmoss + Honeydew (premium alternate) or D6 default | Rotate 2–4 pairings | Cover, dividers, statements | Yes | One moment + accents | Full |
| **P5 Sales and customer presentations** | 16:9 | D6 default | Honeydew-led, rotate 2–3 pairings | Cover, dividers | Yes, photo-heavy | One moment + accents | Full |
| **P6 Internal and operations decks** | 16:9 | Honeydew + Sage | Honeydew + Blackmoss | Optional | Optional | Warnings only | Compact |
| **P7 One-pagers, spec sheets, leave-behinds** | Letter, 1–2 pages | None (header acts as cover) | Honeydew + Blackmoss or Peacock | No | One hero photo | One key number | Full |
| **P8 Quotes, invoices, change orders, transmittals** | Letter, print | None | White + Blackmoss | No | No | "PAST DUE"/notices only | Compact |
| **P9 Letters and memos** | Letter | None | White (print) or Honeydew (digital) + Blackmoss | No | No | No | Letterhead |
| **P10 Social and digital graphics** | 9:16, 1:1, 16:9 | — | Any approved pairing | Yes | Yes | Per Part 4 | Optional |

### P1 — Contracts and legal (replaced 26 Sep 2026 by D13)
- Follows the plain institutional standard in "Ocean Brand System Spec" §6. The earlier P1 rules (justified body, tracked-caps clause headings, key/value caps block, header on every page) are withdrawn.
- White field, Blackmoss only. Horizontal logo 24 pt on page 1; graphic mark 24 pt on continuation pages.
- **Times New Roman throughout** (approved L5): Bold 15 pt centered title, 11.5 / 16.5 pt body left-aligned, numbered sentence-case Bold headings with hanging clause numbers.
- Footer on every page: document number and version, "Page X of Y", initials boxes.
- One Blackmoss diamond as the end-of-document mark. No other graphic.
- QA: fonts embedded, no placeholder text, page count correct, PDF/A preflight.

### P2 — Commercial proposals
- Cover per Part 3. Back cover: the Part 3 texture at low contrast, with the vertical lockup centered and a contact block.
- Page 2 is "Project at a Glance": key/value tiles (SYSTEM SIZE, STORAGE, ANNUAL PRODUCTION, INCENTIVES, SCHEDULE) in chamfered containers with counting diamonds.
- Interior: Honeydew + Blackmoss body pages; one section pairing per chapter (Honeydew + Peacock for technical, Honeydew + Cedar for financial).
- Pricing tables align to the margin and never run past the title rule; totals shown as Bold values.
- Photos: any source (Part 6). Case studies use real Ocean projects.
- Closes with an acceptance and signature block (P1 style) and a terms appendix on White.
- One Crimson accent per page at most (for example a deadline or incentive expiry).

### P3 — Technical and feasibility reports
- Cover per Part 3; interior Honeydew + Blackmoss (long reading) or Honeydew + Peacock.
- Figures and site photos in chamfer masks, captioned in the 14-scale caption style (no end period), with source and date.
- Evidence images must be real photos of the site, with no overlays or gradient maps. Covers, dividers and illustrative figures may use any source.
- Charts: single series in the page ink; multiple series in the pairing colors plus tints of them; Crimson only for the flagged value or risk.
- Tables repeat headers across pages. Appendices on White.
- Findings summary uses the key/value pattern; risks flagged with the Crimson triangle marker.

### P4 — Investor and lender decks
- Cover: Blackmoss + Honeydew (premium) or the D6 default; texture per Part 3.
- Sequence rotates 2–4 pairings: e.g. Blackmoss + Honeydew (cover, dividers), Honeydew + Peacock (content), Honeydew + Blackmoss (financials), Sprig + Peacock (statement).
- One Crimson moment (for example the ask or headline return figure) on a Blackmoss, Peacock, Honeydew or Sprig field.
- Illustrative figures labeled "Illustrative". No "[TBD]" in a release build.
- Agenda or index slide may use Bold display (the guide's contents-page exception).

### P5 — Sales and customer presentations
- D6 default cover. Honeydew-led interiors with photo cards, alternating nature and industry.
- Case studies use real Ocean projects only.
- Pricing, if shown, follows the P2 table rules.

### P6 — Internal and operations decks
- Honeydew + Sage cover (light alternate), Honeydew + Blackmoss interiors.
- Compact header; fewer components; speed over polish, but the same type ladder.

### P7 — One-pagers, spec sheets and leave-behinds
- The full staging header serves as the cover.
- One hero photo in a chamfer mask, one key/value block, one Crimson key number at most.
- Front and back only; contact block at the bottom.

### P8 — Quotes, invoices, change orders and transmittals (updated by D13)
- Formal standard (Spec §6): White, Blackmoss only, logo on page 1.
- Header block in Regular: document number, date, client, project. No tracked caps.
- Line-item tables with hairline rules, right-aligned tabular numbers, and one Medium total line.
- No Crimson. A "past due" notice is set in Medium text, not color.

### P9 — Letters and memos (updated by D13)
- Letterhead: the horizontal logo at 12 pt top-left and the Regular 7.5 pt address block top-right. No rule or meta caps.
- Body Regular 10.5 / 15.5 pt, left-aligned, on White. Follows Spec §6.

### P10 — Social and digital graphics
- The guide is itself a 9:16 "small format", so 9:16 stories and posts use the guide's sizes 1:1 (T1–T27 as measured).
- Any approved pairing; textures allowed; Crimson per Part 4.
- Website (oceanrcs.com) excluded until leadership updates it.

---

## Part 8 — Implementation instructions for Codex

1. Create branch `refine/ocean-style-guide-compliance`. Do not merge automatically.
2. Add to `brand/`:
   - the guide PDF;
   - the official logo masters (SVG, PDF, EPS);
   - this file and the three companion specs under `docs/`.
3. Replace the color, pairing, type and canvas rules in:
   - `AGENTS.md`
   - `DESIGN-SYSTEM.md`
   - `ocean-color-system.md`
   - `brand/color-system.json`
   - the ChatGPT and Codex instruction files
4. Add:
   - `brand/type-scale.json` (27 styles; sizes per format, **marked as leadership-adjustable**);
   - `brand/pairings.json` (30 pairs);
   - `brand/profiles.json` (P1–P10);
   - `scripts/make_texture.py`.
5. Update `lib/ocean.js` and `lib/publication.py` so every page takes `profile` and `pairing`, and every text call takes a style token.
6. Extend QA to reject:
   - unapproved pairs;
   - text below D2 contrast;
   - Crimson outside Part 4;
   - textures breaking Part 5;
   - images without a manifest entry, and non-real images used as report evidence or labeled as Ocean projects;
   - the typography violations in Rule 10 of the typography file.
7. Build one sample per profile P1–P5 and P7–P8. Render every page. Open a pull request with before-and-after renders and a list of any unresolved decisions.
8. Do not invent commercial data; mark all sample figures "Illustrative".
