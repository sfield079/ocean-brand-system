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
| D3 | Deck and document type sizes | Rule 9 of the typography file is approved as written. Weights, case, tracking and line-spacing ratios are fixed. **Sizes live in one token file (implemented in `lib/ocean.js`, `lib/publication.py` and `tokens/ocean.tokens.json`) so they can be changed later without touching layouts.** Minimums: 10.5 pt on slides; 7.5 pt for tracked caps in print | **Yes — flagged for possible revision by leadership** |
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
| D21 | Logo sizing and the graphic mark | Minimum logo sizes per surface are fixed in Spec §16 (for example 44 px in the web header, 28 pt on letters, 0.9 in on the card front). The graphic mark alone is used for app icons, continuation pages, photo corners, chart sheets and signage corners | **Approved 26 Sep 2026** |
| D22 | Emphasis | Six-step ladder (Bold, chip, scale, highlighted tile, bottom-line band, Crimson); one device per idea; works on every pairing without Crimson (Part 9) | **Approved 26 Sep 2026** |
| D23 | Distribution notices | Classification plus status in one footer (for example Confidential · Draft · Do not use) on every deck, proposal, report and contract page; cover line; investor notice slide (Part 10) | **Approved 26 Sep 2026; wording to be reviewed by counsel** |
| D24 | Environment backgrounds | One place photograph per color; gradient-mapped for dividers and optional covers; the image SOP in Part 6 still applies where the use case calls for Ocean, stock or AI photos (Part 11) | **Approved 26 Sep 2026** |
| D25 | Pairings | No new pairings. Olive + Honeydew, Sage + Sprig and Sprig + Crimson are leadership priorities with defined uses; every pairing has a tier and use (Part 12) | **Approved 26 Sep 2026** |
| D26 | Cover and close | Close repeats the cover pairing and background and shows the logo only (Part 13) | **Approved 26 Sep 2026** |

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

The guide's cover texture can be recreated. A proof was built in this session: a particle-wave field drawn in code in exact palette colors, fading to a flat field behind the type. Codex should build it as a reusable generator (implemented: textures in `assets/textures/`, drawn in `lib/ocean.js`) so every cover texture is:
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
- **Budget:** one large Crimson moment per deck; at most one small accent per page; none in body text. For other emphasis use the ladder in Part 9.
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

**Manifest:** every image is logged in `assets/images/image-manifest.json` with its source type (Ocean / stock / AI), file, date, and license or prompt. This makes the two limits checkable and keeps a record if anything is questioned later.

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
- **Notice (Part 10):** classification `proposal` with the recipient and pricing validity. Every page footer reads, for example, `OCN-PRP-0001 · Confidential proposal · Draft · Do not use`; the cover and a closing "Distribution notice" block carry the full sentences. A section can carry a stricter status (for example pricing marked `do-not-use` until approved), and every page it touches shows it. A proposal cannot be released without a named recipient and validity, or while its status is `specimen`. Starters: `documents/_starter/proposal.json` (Letter PDF) and `decks/proposals/_starter/` (proposal deck).

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
   - type sizes per format (implemented in `lib/ocean.js` and `lib/publication.py`, leadership-adjustable);
   - the 30 pairs with tiers and uses (implemented in `tokens/ocean.tokens.json` → `pairing.detail`);
   - profiles P1–P10 (kept in Part 7 of this file);
   - cover textures (implemented in `assets/textures/`).
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

---

## Part 9 — Emphasis: making information pop (D22, 26 Sep 2026)

Leadership asked for a reliable way to make important information stand out: statements, bottom-line conclusions, strong numbers and ROI. Crimson is one tool, not the only one. The ladder below runs from quietest to loudest; use the lowest step that does the job, and **one device per idea**.

| Step | Device | How it looks | Use for | Code |
|---|---|---|---|---|
| E1 | Weight shift | Regular text with the key words in Bold | The words that carry the point in a sentence | `**412 kW**` in any deck text |
| E2 | Inverted chip | The words set in the field color on a solid ink block | One fact per slide that must pop inside a sentence | `==One team==` |
| E3 | Scale | Light display numeral (34–165 pt) with a caps key | Key figures in tiles, the key-number slide | `metrics`, `keyNumber` |
| E4 | Highlighted tile | One metric tile filled solid in the ink, value in Bold | The one figure among several that decides it (payback, ROI, savings) | `metrics: [{..., highlight: true}]` |
| E5 | Bottom line band | Full-width chamfered band in the ink, "BOTTOM LINE" key in Light caps, conclusion in Bold | The slide's conclusion or the number the reader must remember | `bottomLine: '10-year savings of $819K.'` |
| E6 | Crimson | Crimson numeral or diamond | The deck's single key-number moment, a warning, or the diamond on a bottom-line band | `keyNumber`, automatic on the band where approved |

Rules:
- One highlighted tile and one bottom line per slide at most. A chip and a bottom line may share a slide; never stack E1, E2 and E5 on the same words.
- Crimson keeps Part 4's limits (approved fields only; one moment per deck; one small accent per page). Where Crimson is not approved (Sage, Cedar, Olive, Citron fields or bands), the code falls back to E2, E4 or E5 automatically, so emphasis never depends on Crimson.
- Emphasis is information, never decoration: the emphasized text must be a conclusion, a decision figure or a warning.
- Reports and proposals use the same ladder: Bold in running text, glance tiles, and a risk flag for warnings.

## Part 10 — Distribution notices (D23)

Every deck, proposal, report and contract carries one **classification** (who may see it) and one **status** (whether it may be used). The footer shows both together on every page, for example `OCEAN RCS · CONFIDENTIAL · DRAFT · DO NOT USE`; the cover carries the full sentences. Values live in `brand/notices.json`.

| Classification | Footer | Cover line (summary) |
|---|---|---|
| `confidential` (default) | Confidential | Prepared for the recipient; do not copy, forward or distribute without written consent |
| `proposal` | Confidential proposal | Names the recipient and pricing validity; not binding until a contract is signed |
| `investor` | Confidential · For discussion only | Not an offer of securities. Adds an "Important notice" slide before the close automatically |
| `internal` | Internal use only | Do not share outside Ocean RCS |
| `public` | Not confidential | May be shared with attribution |

| Status | Footer addition | Use |
|---|---|---|
| `final` (default) | none | Issued material |
| `draft` | Draft · Do not use | Work in progress |
| `specimen` | Design specimen · Do not use | Templates and reference files |
| `do-not-use` | Do not use | Anything withdrawn or not cleared for use |
| `superseded` | Superseded · Do not use | Replaced by a newer version |

Examples: a draft client deck reads **Confidential · Draft · Do not use**; a reference template reads **Confidential · Design specimen · Do not use**; a draft contract reads **OCN-EPC-2026-014 · v1.0 · Confidential · Draft · Do not use** on every page. A single slide or page can carry a stricter status than its document (`deck.mark(slide, 'do-not-use')` in decks; `"status"` on a section in proposals and reports). The classification never gets weaker on a single slide.

Where the notice appears:
- **Decks:** every slide except the cover and the close, including the agenda, dividers and the key-number slide. The cover carries the full sentences. On display pairings the 9 pt footer uses the field's darkest text partner (for example Peacock on Sprig) so it stays readable.
- **Proposals and reports:** every page footer, the cover and a closing "Distribution notice" block.
- **Contracts:** every page footer, next to the document ID and version, in the PDF and the Word template.

Release rules (enforced in `lib/ocean.js`, `lib/notices.py` and `scripts/qa.py`): a released proposal names its recipient and validity; a `specimen` status cannot be released; every interior slide of any PPTX must carry a notice, including decks built outside this pipeline.

The wording is a business template; counsel should approve it before it is relied on, and legal agreements keep their own confidentiality clauses.

## Part 11 — Environment backgrounds (D24)

Guide 04 grounds each color in a place, and Guide 07 allows brand-color overlays and gradient maps on photography. The repository now holds one place photograph per color (`assets/environments/source/`, AI-generated representative images) and builds two treatments from them with `scripts/make_environment.py`:

- **Gradient-mapped background** (`env_<color>_map_dark|light.jpg`): the photograph mapped into tones of the field color, kept within about 1.5:1 of the field and faded toward the title area, so it stays inside the two-color rule and Part 5's 1.8:1 limit.
- **Photo strip** (`env_<color>_strip.jpg`): the photograph with an 18% field overlay, like the strips on the guide's palette cards.

Where they are used:
- **Dividers:** always, on the section ink's environment (Peacock = misty forested hills, Cedar = forest canopy, Olive = olive grove, and so on).
- **Covers and closes:** optional (`background: 'environment'`) instead of the particle-wave texture. Olive + Honeydew with the olive grove is the earthy option.
- **Never** behind body text, tables, charts or on report body pages.
- Content slides keep unaltered real photographs (Ocean crews and sites first).

**The image SOP still applies (Part 6).** The environment photographs are one option, not a replacement for the image rules. When the use case calls for it, any Part 6 source can take the environment's place, and the same integrity limits hold:
- A case study, "our work" section or site-evidence page uses real Ocean project photos, never an environment or AI image presented as Ocean's work.
- A divider can carry an Ocean project photo instead of the environment (`divider({image})`), and a cover or close can gradient-map any approved photo, such as an Ocean site, licensed stock or an AI image, into its field (`cover({environmentImage})`).
- AI and stock images stay labeled "Representative image" wherever a reader could mistake them for a specific project, and every image is logged in the manifest.

## Part 12 — Pairings: where each one is used (D25)

No new pairings are added. The guide approves 30 of the 36 possible pairs; the six it leaves out cannot be read (Sage + Crimson 1.09:1, Olive + Crimson 1.21:1, Sage + Citron 1.31:1, Sage + Olive 1.32:1, Citron + Crimson 1.42:1, Cedar + Crimson 2.78:1).

### Leadership priority pairings

| Pairing | Contrast | What it is for | Where it is used | Where it is not used |
|---|---|---|---|---|
| **Olive + Honeydew** | 4.73:1 | The earthy pairing: land, growth, economics and sustainability | Earthy covers and closes (olive grove environment); Economics, sustainability, land, agriculture and water sections (Honeydew field, Olive ink); Olive dividers; Olive chart focus | Nowhere is off limits for text. Crimson is not approved on Olive, so emphasis uses chips, highlighted tiles and bottom lines |
| **Sage + Sprig** | 2.34:1 | The calm natural pairing: lake and shallow water | Section dividers (Sprig field, Sage 120 pt numeral and 44 pt title on the shallow-water background), pull-quote and statement slides, brand-atmosphere backgrounds, card backs, social tiles, signage idle screens | Body text, captions, labels, tables, charts, footers and content slides. Type 44 pt and up only |
| **Sprig + Crimson** | 2.54:1 | The warm urgency pairing (Guide 04's Crimson card) | The alternative key-number moment on warm briefings; action-required and deadline slides; incentive-deadline banners; signage alerts; campaign and social graphics | Body text, tables, charts and routine pages. Type 44 pt and up only; supporting detail goes on the next slide or in notes. Counts as the deck's one Crimson moment |

### Tiers (enforced in code)

| Tier | Contrast | Allowed |
|---|---|---|
| Text | 4.5:1 and up | Any text size, content slides and documents |
| Large | 3 to 4.5:1 | Type 25 pt and up, bold labels and graphics (D2, D18) |
| Display | 2 to 3:1 | Type 44 pt and up and graphics: dividers, pull quotes, key moments. Never content slides |
| Tonal | Under 2:1 | Textures, marks and environment maps. No text |

`lib/ocean.js` rejects content slides on display or tonal pairings, text under 44 pt on display pairings, and any text on tonal pairings.

### All 30 pairings

| Pairing | Contrast | Tier | Where it is used |
|---|---|---|---|
| Blackmoss + Honeydew | 17.49:1 | Text | Default dark pairing. Key-number slide (with the Crimson moment), investor covers, app default, signage. Any text size. |
| Peacock + Honeydew | 15.33:1 | Text | Workhorse content pairing on Honeydew (Site sections, tables). Peacock field + Honeydew for dividers and the app light alternative. Any text size. |
| Blackmoss + Sprig | 11.37:1 | Text | Warm dark pairing. Sprig text on Blackmoss for premium pages, card backs, signage. Any text size. |
| Cedar + Honeydew | 10.86:1 | Text | Content on Honeydew with Cedar ink (chart pages), Cedar dividers, formal brand pieces. Any text size. |
| Peacock + Sprig | 9.96:1 | Text | Warm content pairing (Sprig field, Peacock ink) for photo and detail slides. Any text size. |
| Cedar + Sprig | 7.05:1 | Text | System and technical sections (Sprig field, Cedar ink); Cedar dividers with Sprig type. Any text size. |
| Blackmoss + Citron | 6.35:1 | Text | Premium accent: award, milestone or headline-figure slides; Citron type on Blackmoss. Any text size. |
| Peacock + Citron | 5.56:1 | Text | Premium accent on Peacock; headline figures and quotes. Any text size. |
| Blackmoss + Sage | 4.86:1 | Text | Dark data pages and dashboards: Sage type and chart context on Blackmoss. Any text size. |
| Honeydew + Olive | 4.73:1 | Text | The earthy pairing: covers and closes, Economics, sustainability, land, agriculture and water sections, Olive dividers. Olive ink on Honeydew is body-safe (4.73:1); Crimson is not approved on Olive, so emphasis uses chips, highlighted tiles and bottom lines. |
| Blackmoss + Crimson | 4.48:1 | Large | Warnings and the key-number moment on Blackmoss. Crimson type 25 pt and up. |
| Peacock + Sage | 4.26:1 | Large | Secondary dark content with Sage type; headlines 25 pt and up, labels, charts. |
| Cedar + Citron | 3.94:1 | Large | Warm accent on Cedar: headlines 25 pt and up, figures, icons. |
| Peacock + Crimson | 3.93:1 | Large | Alert or key figure on Peacock; Crimson 25 pt and up. |
| Honeydew + Crimson | 3.91:1 | Large | Alerts, risk flags and past-due notices on Honeydew; Crimson type 25 pt and up or bold labels. |
| Blackmoss + Olive | 3.7:1 | Large | Earthy dark accent: Olive headlines 25 pt and up and graphics on Blackmoss. |
| Sage + Honeydew | 3.6:1 | Large | Default cover and close (Sage field, Honeydew type), card fronts, hero lines. 25 pt and up; never body text (D18). |
| Peacock + Olive | 3.24:1 | Large | Earthy dark accent: headlines 25 pt and up, graphics. |
| Sprig + Olive | 3.07:1 | Large | Warm earthy pairing: Sprig field with Olive headlines 25 pt and up; sustainability graphics. |
| Cedar + Sage | 3.02:1 | Large | Tonal green: headlines 25 pt and up, charts (Sage context on Cedar). |
| Honeydew + Citron | 2.75:1 | Display | Display only (44 pt and up) and graphics: sunlight accents, icons on Honeydew. |
| Sprig + Crimson | 2.54:1 | Display | The warm urgency pairing (Guide 04's Crimson card): the alternative key-number moment on a warm briefing, action-required and deadline slides, incentive-deadline banners, signage alerts and campaign or social graphics. Display type 44 pt and up only; the supporting detail goes on the next slide or in notes. Counts as the deck's Crimson moment. |
| Sage + Sprig | 2.34:1 | Display | The calm natural pairing (lake and shallow water): section dividers, pull-quote and statement slides, brand-atmosphere backgrounds, card backs, social tiles and signage idle screens. Display type 44 pt and up and graphics only; never body text, captions, tables or charts. |
| Cedar + Olive | 2.29:1 | Display | Display only (44 pt and up) and graphics: forest and grove textures. |
| Sprig + Citron | 1.79:1 | Tonal | Tonal only: textures and marks; no text. |
| Olive + Citron | 1.72:1 | Tonal | Tonal only: textures and marks; no text. |
| Blackmoss + Cedar | 1.61:1 | Tonal | Tonal only: textures, the cover particle wave, marks; no text. |
| Honeydew + Sprig | 1.54:1 | Tonal | Tonal only: textures, watermark marks; no text. |
| Peacock + Cedar | 1.41:1 | Tonal | Tonal only: textures and marks; no text. |
| Blackmoss + Peacock | 1.14:1 | Tonal | Tonal only: textures, the premium background wave; no text. |

## Part 13 — Cover and close (D26)

- The close always uses the same pairing and background as the cover, whichever pairing the cover uses. The code copies it and rejects anything else.
- The close carries the vertical logo only: no words, address, URL or notice. Contact details go on the next-steps slide.
