# Ocean RCS Style Guide — Independent Visual Audit

Audit-only review. No files, branches, or pull requests were changed.

| Scope | What was inspected |
|---|---|
| Style guide | `Ocean_StyleGuide_2026.pdf`, 11 PDF pages (1080 × 1920 pt, 9:16 portrait "Small Format"), rendered and inspected at 54, 150 and 300 dpi, with zoomed crops of the header system, containers, palette cards and pairing grid |
| Repository | `sfield079/ocean-deck-system`, `main` at `ef0da86` ("Correct Ocean logo proportions in shared layouts"), read-only clone |
| Deck | `output/pptx/ocean-layout-reference.pptx` (13 slides), rendered through LibreOffice with bundled Stack Sans Headline installed, inspected slide by slide at 80 and 300 dpi; also compared against `templates/ocean-layout-reference.pptx` |
| Proposal | `output/pdf/ocean-proposal-reference.pdf` (2 pages, Letter), rendered at 110 dpi and measured |
| Report | `output/pdf/ocean-report-reference.pdf` (1 page, Letter), rendered at 110 dpi and measured |
| Rules | `AGENTS.md`, `brand/DESIGN-SYSTEM.md`, `brand/REFERENCE-NOTES.md`, `brand/color-system.json`, `brand/ocean-color-system.md`, `brand/CHATGPT-PROJECT-INSTRUCTIONS.md`, `CODEX-PROMPTS.md`, `README.md`, `lib/ocean.js`, `lib/publication.py`, `scripts/qa.py`, `scripts/qa_pdf.py`, logo assets |
| Method | Visual inspection plus pixel measurement. Each render was mapped to the nine brand colors to measure how much of each page each color actually covers. |

Page references use the guide's own labels, with the PDF page in brackets. Example: "Guide 05 [PDF 7]".

---

## Executive verdict

The repository is well engineered but visually off-brand. It gets the mechanics right: embedded Stack Sans Headline, no-shrink fitting, placeholder gates, and rules against invented claims. The visual rules, however, came from a separate ChatGPT chat and the oceanrcs.com website rather than from the style guide. `REFERENCE-NOTES.md` says so directly: the style guide was adopted only for "Logos, core hex values, Stack Sans Headline, clearance," and its imagery language was marked "superseded."

Measured result: every page of all three artifacts is **83–95% pure white `#FFFFFF`**, and no brand color covers more than about 5% of any page. In the guide, **every page is built on one dominant brand-color field (45–90% of the page) plus one accent color.** The guide never uses pure white as a content canvas; it appears only behind the two swatch-specimen pages. The artifacts use four of the nine brand colors, invent three non-brand tints, render the logo in pure black `#000000` (not a brand color), and leave out the guide's structural signature: the staging header, rounded-and-chamfered containers, tracked micro-labels, and photo-strip cards.

**Recommendation: not ready for production client or investor decks.** Keep the engineering layer, replace the visual layer, then regenerate all three specimens.

---

## 1. True Style Guide Findings

### 1.1 Complete core palette — Guide 04 [PDF 6]

The guide describes the palette as "a spectrum of warm, earthy green and brown tones that feel rooted to the strength and beauty of the natural world."

| Color | Hex | RGB | How the guide uses it visually |
|---|---|---|---|
| Blackmoss | `#0B1617` | 11/22/23 | Primary dark field (cover, 03 Usage, 08 Imagery); primary ink on light pages |
| Peacock | `#102426` | 16/36/38 | Secondary dark field; ink on Citron (02 Spacing); low-contrast texture on cover |
| Cedar | `#1B4039` | 27/64/57 | Logo specimen ink on Honeydew (01); dark field in gradient maps (back cover) |
| Sage | `#618C7C` | 97/140/124 | Full-page accent ink for UI, titles and rules on Honeydew (01) |
| Honeydew | `#F3FBF8` | 243/251/248 | **The light canvas** (TOC, 01, 07); display type on Blackmoss (cover) |
| Sprig | `#D5CCA0` | 213/204/160 | Warm light field (06 Typography); outline labels on Olive (02) |
| Olive | `#6E734C` | 110/115/76 | Container fill on Citron (02); UI accent on the palette page (04) |
| Citron | `#A69856` | 166/152/86 | Full-page field (02); accent for logo, year and titles on Blackmoss (cover, 03); oversized mark on Sprig (06) |
| Crimson | `#EB3819` | 235/56/25 | Accent-only color: full UI/title color on White (05) and Blackmoss (08); never a large field in page chrome |

Each swatch card on Guide 04 is itself a demonstration pairing: the card field in one color with the logo, name and data in its partner color, plus a natural photo strip under a translucent color overlay. The card pairings are Blackmoss/Citron, Peacock/Sage, Cedar/Sprig, Sage/Blackmoss, Honeydew/Crimson, Sprig/Olive, Olive/Honeydew, Citron/Cedar, and Crimson/Sprig.

### 1.2 Approved general-use two-color pairings — Guide 05 [PDF 7]

The guide shows 31 tiles. Two tiles are mislabeled:

- Row 2, tile 4 is labeled "Blackmoss + Citron," but the swatch is clearly **Blackmoss + Crimson**.
- "Sprig + Citron" appears twice (row 7, tile 4 and row 8, tile 1).

That leaves **30 unique approved pairings out of the 36 possible**. Guide text: "Not all brand colors play nicely together. Avoid pairings that clash in temperature or lack sufficient contrast."

Contrast was calculated with the WCAG 2.x formula. Use class: **Body** ≥ 4.5:1, safe for any text size. **Large** 3.0–4.49:1, for headlines ≥ 24 pt, bold labels ≥ 18.5 pt, or graphics only. **Tonal** < 3:1, for fields, textures, containers and logo-on-field staging only, never for text.

| # | Pairing | Contrast | Use class |
|---|---|---:|---|
| 1 | Blackmoss + Peacock | 1.14 | Tonal |
| 2 | Blackmoss + Cedar | 1.61 | Tonal |
| 3 | Blackmoss + Sage | 4.86 | Body |
| 4 | Blackmoss + Honeydew | 17.49 | Body |
| 5 | Blackmoss + Sprig | 11.37 | Body |
| 6 | Blackmoss + Olive | 3.70 | Large |
| 7 | Blackmoss + Citron | 6.35 | Body |
| 8 | Blackmoss + Crimson (mislabeled in guide) | 4.48 | Large |
| 9 | Peacock + Cedar | 1.41 | Tonal |
| 10 | Peacock + Sage | 4.26 | Large |
| 11 | Peacock + Honeydew | 15.33 | Body |
| 12 | Peacock + Sprig | 9.96 | Body |
| 13 | Peacock + Olive | 3.24 | Large |
| 14 | Peacock + Citron | 5.56 | Body |
| 15 | Peacock + Crimson | 3.93 | Large |
| 16 | Cedar + Sage | 3.02 | Large |
| 17 | Cedar + Honeydew | 10.86 | Body |
| 18 | Cedar + Sprig | 7.05 | Body |
| 19 | Cedar + Olive | 2.29 | Tonal |
| 20 | Cedar + Citron | 3.94 | Large |
| 21 | Sage + Honeydew | 3.60 | Large |
| 22 | Sage + Sprig | 2.34 | Tonal |
| 23 | Honeydew + Sprig | 1.54 | Tonal |
| 24 | Honeydew + Olive | 4.73 | Body |
| 25 | Honeydew + Citron | 2.75 | Tonal |
| 26 | Honeydew + Crimson | 3.91 | Large |
| 27 | Sprig + Olive | 3.07 | Large |
| 28 | Sprig + Citron | 1.79 | Tonal |
| 29 | Sprig + Crimson | 2.54 | Tonal |
| 30 | Olive + Citron | 1.72 | Tonal |

**Not approved (absent from the grid):** Cedar + Crimson, Sage + Olive, Sage + Citron, Sage + Crimson, Olive + Crimson, Citron + Crimson.

On every tile, the logo is drawn in the partner color: a single color, never mixed. This is the guide's model for logo coloring.

### 1.3 Do pages use two dominant colors? Yes, consistently

Measured on the guide's own pages:

| Guide page | Dominant field (measured coverage) | Accent / UI color | Functional ink | Notes |
|---|---|---|---|---|
| Cover [PDF 1] | Blackmoss (84%) | Citron (logo, year, subtitle) | Honeydew display title | Peacock/Cedar particle wave at low contrast behind the upper half |
| 00 Contents [PDF 2] | Honeydew (83%) | Blackmoss | — | Strict two-color page |
| 01 Lockups [PDF 3] | Honeydew (91%) | Sage (all UI, titles, rules, container lines) | Cedar logo specimens | Tonal one-family page |
| 02 Spacing [PDF 4] | Citron (46%) | Olive containers (46%) | Peacock/Cedar ink; Sprig label outlines | Olive + Citron is an approved pairing |
| 03 Usage [PDF 5] | Blackmoss (58%) | Citron (UI, titles) | — | The multi-color tiles are deliberate "DO NOT" examples |
| 04 Palette [PDF 6] | White `#FFFFFF` | Olive (UI) | — | Specimen page: a neutral backdrop for nine cards |
| 05 Pairings [PDF 7] | White `#FFFFFF` | Crimson (UI) | Blackmoss labels | Specimen page |
| 06 Typography [PDF 8] | Sprig (72%) | Citron (oversized graphic mark, 11%) | Blackmoss type | Graphic-only mark used as a large decorative element behind type |
| 07 Imagery 1 [PDF 9] | Honeydew (45%) | Blackmoss | — | Natural photography fills the rest |
| 08 Imagery 2 [PDF 10] | Blackmoss (62%) | Crimson (UI, titles) | — | Abstract/futurist imagery |
| Back cover [PDF 11] | Cedar/Olive/Blackmoss gradient-mapped abstract | Citron (logo, frame outline) | — | Gradient map made from one tonal family |

**Rule observed:** one dominant field color plus one accent/UI color per page. The page title, section label, header frame, rules, active navigation state and logo all take the **accent** color. Blackmoss or Honeydew may carry body type when the pairing itself isn't a body-text pairing. Everything else is photography or tonal texture.

### 1.4 Functional role of light and neutral backgrounds

- **Honeydew is the brand's light canvas.** Every light content page (00, 01, 07) is Honeydew, not white.
- Pure White appears only behind the two swatch specimen pages (04, 05), where color judgment requires a neutral base. The guide does not show White as a general content canvas.
- Light pages are never "white + four accents." They are Honeydew plus one accent (Sage on 01, Blackmoss on 00 and 07).
- Dark pages (cover, 03, 08) are about half of the guide. Dark staging is a core mode, not an exception.

### 1.5 Logo system — Guides 01–03 [PDF 3–5]

| Topic | Guide rule |
|---|---|
| Lockups | Three formats: vertical graphic + type; horizontal graphic + type; graphic-only |
| Selection | Use the graphic + type versions "in all cases where the full logo must be displayed, or there is ample staging space." Graphic-only is for small-scale use where space is limited, and "can also be used as a branded decorative graphical element." |
| Clear space | Vertical: **0.5× full asset height**. Horizontal: **1× full asset height**. Graphic-only: **0.5× full asset height** (Guide 02) |
| Do not | Rotate; change lockup orientation; distort or skew; crowd it; place it on backgrounds that obscure legibility or clash with the palette; recolor to non-brand colors; change or recreate the typeface or graphic; mix undesignated brand colors within the logo; use low-resolution versions (Guide 03) |
| Color | The guide renders the logo in a **single brand color taken from the page pairing**: Citron on Blackmoss (cover, 03), Sage/Cedar on Honeydew (01), Peacock on Citron (02), Olive on White (04), Crimson on White (05), Blackmoss on Sprig (06), Crimson on Blackmoss (08). "Non-brand colors" and "mixed" colors are forbidden, not brand recoloring. |
| In decks | Horizontal lockup inside a staging header on content pages. Vertical lockup centered on covers and back covers (cover, back cover). Graphic-only mark as a small UI glyph or as an oversized tonal decorative element (06). |

### 1.6 Typography — Guide 06 [PDF 8]

- **Family:** Stack Sans Headline (Google Fonts), Latin, six weights (ExtraLight 200 to Bold 700), with variable-font support. No second typeface is specified.
- **Display:** very large, tightly set type with negative tracking. The cover's "Brand Guidelines" appears to be Regular. "Table of Contents" and "Stack Sans Headline" are set in heavier and regular weights respectively, at huge sizes with near-solid leading.
- **Page titles:** two-line titles ("Brandmark / Lockup Variations"), Medium–SemiBold, in the page's accent color.
- **Micro-labels:** a signature element. UPPERCASE, SemiBold/Bold, very small, **widely tracked (about +20–30%)**. Used for section kickers ("LOGO SYSTEM"), container tabs, the header meta block, the navigation, and "PAGE 01."
- **Lede:** a tracked, uppercase, bold 3–4-line statement in the right column.
- **Body:** small Regular, often justified, in a narrow right-hand column.
- **Index numerals:** large Regular/Light ("01 … 07" on the contents page).
- **Tone:** precise, architectural, "clean and modern geometric," with "notched detailing, inspired by the building process."
- **Verify:** the embedded fonts are Type 3, so exact weights cannot be read from the file. Confirm weights against the source design file.

### 1.7 Page composition and grid

- **Staging header (every interior page).** A two-row bordered frame. Top row: a horizontal-logo cell (about 60% width) and a meta cell ("SMALL FORMAT / VISUAL IDENTITY MANUAL / OCEAN RCS"). Bottom row: "PAGE nn," a section navigation strip ("LOGO SYSTEM — COLOR — TYPOGRAPHY — MEDIA") with the active item shown as an inverted fill chip, and a seven-cell icon strip with the active cell filled. All lines are hairlines in the accent color.
- **Title block.** A tracked kicker, then a two-line title on the left (about 45%). A tracked lede and small body text sit in the right column (about 50%), with a full-width hairline rule between.
- **Content zone.** Large bordered containers aligned to the same outer margins as the header, on a two-column grid with a consistent gutter.
- **Whitespace.** Generous. Top 25–30% is header and title; content fills the rest. There are no half-empty pages and no floating single lines.
- **Close.** A heavier full-width rule at the bottom margin.
- **Character.** Editorial and technical, like an instrument panel or spec sheet, not a minimalist memo.

### 1.8 Brand geometry

- **Container shape.** Rounded rectangles with **one 45° chamfered corner**: bottom-right on lockup containers, top-left on palette cards, pairing tiles and imagery. This is taken from the logo's rounded frame and sharp intersecting "X."
- **Markers.** Small rotated-square (diamond) glyphs sit just outside the chamfer, one or two per container.
- **Tabs.** Container labels are tracked caps inside a thin-outline pill that breaks the container's top border (01, 02).
- **Image masks.** Photos are cropped into the same rounded-plus-chamfer shapes (07, 08).
- **Frame.** The back cover uses a hairline frame with one chamfered corner.
- **Intent** (Guide 07 text): "adds subtle cohesion and reinforces the brand without drawing too much attention to itself."

### 1.9 Imagery, overlays and abstract visuals — Guides 07–08 [PDF 9–10]

- **Primary imagery.** "Real environments and real people in action, lit by natural sun or warm industrial tones." The examples show a worker in a hard hat and vest with a tablet, two installers on a metal roof with panels, a residential rooftop array against blue sky, an ocean wave, fog over forest, and a misty river valley.
- **Nature.** Mountains, water and nature can be used "on top of industry-relevant imagery" to express the renewable and conservation link.
- **Overlays and gradient maps.** "Use designated harmonies of brand colors to overlay or gradient map imagery **alongside unaltered photography**." Treated and natural images appear together, never all washed. The palette cards (04) show this as a translucent color panel over part of a photo strip.
- **Avoid.** "Generic staged scenes or overly polished edits." Let layout and UI staging complement clean, natural photography.
- **Abstract/futurist.** Allowed as "textural background elements and secondary visuals" with "modern-futurist stylization," best in **lower contrast**. Examples: light-trail city, particle wave, sage marble texture, data-light skyline. The cover and back cover use this treatment at low contrast.

---

## 2. Artifact-by-Artifact Audit

### 2.1 System-wide findings (all artifacts)

| Aspect | Follows | Partly follows | Conflicts |
|---|---|---|---|
| Palette | Hex values for the four colors used are exact | — | Only four of nine brand colors; three invented tints (Fog `#D5DED9`, Mist `#EEF2F0`, sageLight `#A9C2B8`); White instead of Honeydew |
| Pairing | — | — | No page has a dominant brand field. Measured 83–95% White everywhere; brand coverage under 5% |
| Logo | Original artwork; aspect ratio fixed in `ef0da86`; horizontal 1× clear space respected | — | PNG is pure black `#000000` (non-brand); never takes the pairing color; vertical lockup and graphic-only mark never used |
| Type | Stack Sans Headline embedded (PDF) and themed (PPTX) | Hierarchy is clear | Bold 700 for every headline; untracked uppercase labels (the repo bans letter-spacing, which removes the guide's signature micro-label); no display-scale type |
| Composition | Consistent margins and footer | Two-column logic exists | No staging header, containers, tabs or chamfers; a "memo" layout rather than the guide's instrument-panel layout |
| Imagery | Truth rules on photography are good | — | No imagery anywhere; overlays, gradient maps and low-contrast textures are banned outright |

### 2.2 `ocean-layout-reference.pptx` (13 slides, 13.333 × 7.5 in)

Every slide shares these traits: White canvas; black PNG horizontal logo 1.25 × 0.349 in at top-left; 10 pt Cedar footer "Ocean RCS  Design specimen" with page number over a Fog hairline; right-aligned untracked 13 pt Cedar uppercase eyebrow; 32 pt Bold Blackmoss headline.

| Slide | What it shows | Follows | Conflicts / defects | Credibility |
|---|---|---|---|---|
| 1 Cover | "One clear story. Every page considered." 48 pt Bold; Sage rule; Cedar subtitle; date | Stack Sans; clean fit | Guide cover is Blackmoss + Citron with a centered vertical lockup, display type and low-contrast texture. This cover is White with a 1.25-in black logo, and the right 55% and bottom third are empty. The headline is meta-copy about design. | Reads as a Word template; weak for investors or lenders |
| 2 Divider | "01" 54 pt Bold Sage; title; subtitle | Section number idea | White, no field color, no image; bottom 40% and right 60% empty; Sage on White = 3.78:1, acceptable only because it is large | Looks unfinished |
| 3 Statement | Headline, Sage rule, 24 pt Cedar statement | Hierarchy | Content fills the top-left 40%; lower half and right side empty; no image or container | Unbalanced |
| 4 Two-column | Presentation vs. proposal lists | Grid and rules | Sage/Fog hairlines only; bullet rows spaced 0.87 in apart, so the lists float; no containers or tabs | Acceptable but generic |
| 5 Pillars | Typography / Color / Evidence | Three-column grid | Fog rules (`#D5DED9` on White, about 1.37:1) nearly invisible; the copy codifies the wrong rule ("White creates space… Sage adds restrained emphasis") | Generic |
| 6 Metrics | 48 / 32 / 17 / 11 type scale | Aligned numerals | Bold numerals; the guide uses Regular/Light index numerals. No containers. The "11 Report prose" metric sits beside presentation sizes. | Internal only |
| 7 Timeline | Brief → Compose → Verify → Deliver | Clear sequence | Sage line plus untracked "01 / Brief" labels; no phase containers or chamfered markers | Generic |
| 8 Color roles | Table: Canvas White, Primary ink Blackmoss, Accent Sage, Secondary ink Cedar, Structure Peacock | Table is editable | **Directly contradicts the guide.** It documents a five-color system, omits Honeydew, Sprig, Olive, Citron and Crimson, and defines White as the canvas | Would mislead every future author |
| 9 Chart | Single series A–D, values 2/4/3/5 | Native, editable, labeled "Illustrative" | One series colored with four fills (Cedar, Sage, Peacock, sageLight), which reads as a rainbow. sageLight is not a brand color. Uppercase 10 pt footnote. No pairing logic. | Weak data-viz practice |
| 10 Case study | Identity / Scope / Status / Source rows | Truth-first structure | No image slot rendered; rows float in White; no container | Too sparse for proof |
| 11 Team | Leadership / Operations / Technical | No fake avatars (good) | Untracked uppercase Cedar role labels; lower 30% empty | Acceptable |
| 12 Ask | "[TBD]" at 48 pt; "[TBD]" in scope and terms; three steps | Placeholder gate exists | Visible placeholders in a reference deck; the ask slide should be the most confident composition, not the emptiest | Not presentable |
| 13 Appendix | Four-row table, Peacock header | Readable 13 pt table | Bottom 40% empty; Fog borders; White | Acceptable for an appendix |

More deck defects:

- `templates/ocean-layout-reference.pptx` is **stale**. It still contains the pre-`ef0da86` logo frame; every slide differs from `output/pptx/` in the logo region.
- `output/pdf/ocean-layout-reference.pdf` dates from commit `8d3e9cb`, before the logo fix. It is also stale.
- The same 33 KB logo PNG is embedded 13 times (once per slide). Minor.
- `output/renders/` contains only `.gitkeep`. The QA evidence the rules require is not committed.

### 2.3 `ocean-proposal-reference.pdf` (2 pages, Letter)

| Page | Follows | Conflicts / defects | Credibility |
|---|---|---|---|
| 1 | Embedded Stack Sans Headline (Regular, SemiBold, Bold); live text; clear H1/H2; no invented prices | White canvas; black logo at 83 × 22 pt top-left; Mist (non-brand) table header fill. **Alignment defect:** body text starts at 45.8 pt while the logo and footer start at about 41 pt (6 pt inset from the default frame padding), and tables run to 578 pt while the title rule ends at 566 pt (tables overrun the rule by about 12 pt). No cover, pairing, project-at-a-glance block, image or container. Bottom 15% empty. | Reads as an internal memo, not a branded commercial proposal |
| 2 | Tables repeat cleanly; KeepTogether items | Same alignment defect; 9 pt bold item labels are untracked and read as bold body text; bottom 20% empty; no acceptance, signature or contact block | Missing the commercial close |

Also: the PDF references an **unembedded Helvetica** font resource (ReportLab's default initial font). No glyphs use it, so `qa_pdf.py` passes, but a print preflight or PDF/A check may flag it.

### 2.4 `ocean-report-reference.pdf` (1 page, Letter)

| Page | Follows | Conflicts / defects | Credibility |
|---|---|---|---|
| 1 | Clear report logic (finding, evidence, recommendations, limitations); honest specimen note | Same White, black logo and Mist issues; the same 6 pt text inset and table overrun (table reaches the right margin, rule stops short). A single page shows no cover, executive-summary callout, figure, chart, photo or appendix pattern, so it cannot serve as a reference for multi-page reports. | Credible as a memo; not a brand reference |

### 2.5 What looks generic, over-simplified or AI-default

- "White page + black logo + bold sans headline + thin green rule" is the default of most AI deck tools. Nothing except the logo makes it Ocean.
- Empty lower halves on slides 1, 2, 3, 11 and 13 read as "template not filled."
- Meta-copy about design ("One clear story," "The evidence leads the page") instead of real specimen content.
- A multi-color single-series chart, which is the standard auto-chart look.
- The system was simplified by exclusion. It solved "AI clutter" by removing the guide's identity devices too: color fields, staging UI, geometry and textures.

---

## 3. Keep / Revise / Remove / Add / Verify

| Item | Location | Finding | Guide evidence | Recommendation | Priority |
|---|---|---|---|---|---|
| Keep — Stack Sans Headline bundled, installed, embedded | `brand/fonts/`, `scripts/install_fonts.py`, `qa_pdf.py` | Correct family, verified embedding | Guide 06 [PDF 8] | Keep; add ExtraLight/Light files for display and index numerals | — |
| Keep — no-shrink fitting and unbreakable-word errors | `lib/ocean.js` `wrap()`/`text()` | Prevents clipping and overflow | General quality | Keep | — |
| Keep — release placeholder gate | `lib/ocean.js`, `publication.py`, `qa.py`, `qa_pdf.py` | Blocks "[TBD]" in release output | — | Keep | — |
| Keep — truth and claims rules | `AGENTS.md` "Truth and editorial discipline"; `decks/investor/AGENTS.md` | Strong and appropriate | — | Keep unchanged | — |
| Keep — native editable tables and charts | `lib/ocean.js` `table()`/`chart()` | Correct production approach | — | Keep; restyle only | — |
| Keep — slide vs. document type scales | `color-system.json`, `DESIGN-SYSTEM.md` | Sensible separation | — | Keep; add display and micro-label tiers | — |
| Keep — logo aspect-ratio fix and horizontal 1× clear space | `lib/ocean.js` `logo()` (`ef0da86`) | Matches guide | Guide 02 [PDF 4] | Keep; extend to the other lockups | — |
| Keep — CI publication QA workflow | `.github/workflows/publication-qa.yml` | Good gate | — | Keep; add the new pairing checks | — |
| Revise — palette tokens | `brand/color-system.json` | Four brand colors plus White; five brand colors missing | Guide 04 [PDF 6] | Replace with the full nine-color palette, the 30-pair matrix and a contrast class per pair (Section 4.3) | P0 |
| Revise — canvas default | `AGENTS.md`, `DESIGN-SYSTEM.md`, `ocean-color-system.md`, `lib/ocean.js` `page()`, `publication.py` | White is the default everywhere; measured 83–95% White | Guides 00, 01, 07 use Honeydew; White only on specimen pages 04–05 | Honeydew becomes the light canvas. White only by leadership exception (see decisions). | P0 |
| Revise — "Default dark covers are retired" | `ocean-color-system.md`, `DESIGN-SYSTEM.md`, `CODEX-PROMPTS.md` | Contradicts the guide | Cover [PDF 1], 03, 08 and back cover are dark | Covers default to a dark pairing (Blackmoss + Citron); light covers become optional | P0 |
| Revise — logo color | `assets/logos/Ocean_LOGO_Horizontal.png` (pure `#000000`), SVGs (`#fff`), "never recolored" rule | Black is a non-brand color; the logo never follows the pairing | Guide 03 [PDF 5] "non-brand colors"; Guide 05 tiles | Render the logo from the SVG in one brand color, the page's accent or the pairing partner. Ban mixed colors and non-brand colors. | P0 |
| Revise — typography rules | `DESIGN-SYSTEM.md` "No… artificial letter spacing"; `lib/ocean.js` Bold-only headlines | Removes the guide's tracked micro-labels; everything is Bold | Guide 01–08 headers and kickers; Guide 06 weights | Allow tracking on labels only (+20–30%); set tight tracking on display (−2% to −3%); use Medium/SemiBold for titles; Regular/Light for index numerals | P0 |
| Revise — chart colors | `lib/ocean.js` `chartColors:[cedar,sage,peacock,sageLight]` | Four colors on one series; sageLight is off-brand | Guide 05 pairing logic | Single series uses the accent color only. Multiple series use the two pairing colors plus tints of them (Section 4.5). | P1 |
| Revise — "no gradients / no watermark logos / no AI backgrounds" | `AGENTS.md`, `DESIGN-SYSTEM.md`, `CHATGPT-PROJECT-INSTRUCTIONS.md` | Blanket ban covers guide-approved devices | Guide 01 ("graphic-only… decorative element"), 06 (oversized mark), 07 (overlays and gradient maps), 08 (low-contrast abstract) | Replace with controlled permissions: tonal only, secondary, never behind body text at more than 1.8:1 contrast | P1 |
| Revise — reference authorities | `REFERENCE-NOTES.md` ("Abstract/gradient backgrounds superseded"; OceanAshers, OceanOP081926, oceanrcs.com as design sources) | The guide is subordinate to a chat and the website | The guide is the "Core Visual Identity Manual" | Make the guide the controlling authority; other references become secondary examples only | P0 |
| Revise — proposal/report margins | `lib/publication.py` `SimpleDocTemplate` frame padding; `Table` width = full frame | 6 pt text inset vs. logo/footer; tables overrun the rule by about 12 pt | Guide aligns all elements to one outer margin | Set frame paddings to 0 or width = frame width; align logo, text, rules, tables and footer to one x | P1 |
| Revise — color-roles slide | Deck slide 8 | Teaches the wrong five-color system | Guide 04–05 | Replace with a nine-color palette slide and a pairing-in-use slide | P0 |
| Revise — cover, divider and ask specimens | Deck slides 1, 2, 12 | Empty, White, placeholder-led | Cover [PDF 1], back cover [PDF 11] | Rebuild as dark pairing compositions with the vertical lockup, display type and optional low-contrast texture | P0 |
| Revise — ChatGPT bridge instructions | `brand/CHATGPT-PROJECT-INSTRUCTIONS.md`, `CODEX-PROMPTS.md`, `README.md` line 4 | Repeat "white pages… sparse Sage… light covers" | — | Synchronize with the new rules in the same PR | P0 |
| Remove — invented tints | `color-system.json` `tints` (Fog, Mist, sageLight) | Not in the guide | Guide 04 lists nine colors only | Delete; replace with opacity tints of the active pairing colors | P0 |
| Remove — White/Blackmoss/Sage "balance" rule | `DESIGN-SYSTEM.md` intro, `AGENTS.md` "Default to white pages…" | Core cause of the off-brand result | Guide 05 | Delete | P0 |
| Remove — "Honeydew/Sprig/Olive/Citron/Crimson are not the default palette" | `DESIGN-SYSTEM.md` | Explicitly excludes brand colors | Guide 04 | Delete | P0 |
| Remove — "Do not apply a green wash to images" as an absolute | `DESIGN-SYSTEM.md` | Conflicts with approved overlays and gradient maps | Guide 07 | Replace with the controlled overlay rule (Section 4.6) | P1 |
| Remove — stale artifacts | `templates/ocean-layout-reference.pptx`, `output/pdf/ocean-layout-reference.pdf` | Pre-logo-fix builds | — | Regenerate from source in CI or delete; one canonical copy | P1 |
| Add — pairing declaration per slide/page | `lib/ocean.js` API, `publication.py` JSON schema | No pairing concept exists | Guide 05 | Every page call takes `pairing: ['blackmoss','citron']`; builder rejects unapproved pairs | P0 |
| Add — staging header component | `lib/ocean.js`, `publication.py` chrome | Signature UI missing | Guides 00–08 header frame | 16:9 adaptation: a hairline band with logo cell, meta cell, section nav with active chip, page number | P1 |
| Add — brand-geometry containers | `lib/ocean.js` shapes | No containers, tabs, chamfers or markers | Guides 01, 02, 04, 05, 07 | Rounded rectangle with one 45° chamfer, diamond marker and tab label; same mask for images | P1 |
| Add — photo-card and image-mask layouts | `lib/ocean.js` `image()` | Rectangular crop only; no overlay option | Guides 04, 07, 08 | Chamfer mask; optional translucent pairing overlay on one image per spread, beside an unaltered image | P1 |
| Add — pairing-aware visual QA | `scripts/qa.py`, new `scripts/qa_color.py` | Only text-run colors checked; fills unchecked; no page-level coverage check | Guide 05 | XML check of all fills, lines and text, plus a render-based coverage check (Section 4.7) | P0 |
| Add — vertical and graphic-only lockup rules | `lib/ocean.js` | Only horizontal used; 0.5× clearances not encoded | Guides 01–02 | Encode 0.5× clearance for vertical and graphic-only; vertical on covers | P1 |
| Add — committed render evidence | `output/renders/` | Empty | — | CI uploads renders as artifacts; PRs include before/after PNGs | P2 |
| Verify — weights and tracking values | Guide 06 source file | Type 3 fonts prevent exact weight readout | Guide 06 | Confirm with the designer's source (Figma/AI) | P1 |
| Verify — guide errata | Guide 05 [PDF 7] | "Blackmoss + Citron" duplicated (second is Crimson); "Sprig + Citron" duplicated | Visual swatches | Leadership confirms that 30 unique pairs is correct | P1 |
| Verify — oceanrcs.com as a reference | `REFERENCE-NOTES.md` | Live site computes to a White body with Blackmoss Stack Sans text ([oceanrcs.com](https://oceanrcs.com/)) | Guide is the identity manual | Decide whether the site is off-guide too; don't let it override the guide | P2 |
| Verify — PPTX rendering in PowerPoint | Deck | Rendered here through LibreOffice | — | Open in PowerPoint 365 (Win/Mac) with fonts installed; check chamfer shapes and tracking once built | P1 |
| Verify — Helvetica resource in PDFs | `publication.py` `initialFontName` | Unembedded font object present | — | Run a preflight; remove the default Helvetica reference | P2 |

---

## 4. Required Repository Rules

Drop-in text for Codex. "Replace" means delete the named section and insert this one.

### 4.1 `AGENTS.md` — replace "Identity and design"

```md
## Identity and design (controlling authority: brand/Ocean_StyleGuide_2026.pdf)

- The Ocean Style Guide 2026 is the controlling visual authority. Other references
  (OceanAshers, OceanOP081926, oceanrcs.com, chat logs) are secondary examples and
  may never override it. Where they conflict, follow the guide.
- Use the full nine-color palette in brand/color-system.json. No other colors,
  tints or grays, except opacity tints of the active pairing colors.
- TWO-COLOR RULE: every slide and page declares exactly one approved pairing
  [dominant, accent] from brand/color-system.json → pairings. The dominant color
  is the page field (background or largest color area). The accent color carries
  the title, section label, rules, staging header, active states, logo, diagram
  lines and highlights. No third brand color may appear, except as allowed below.
- Allowed additions: (1) functional ink, meaning Blackmoss or Honeydew used only
  for text when the pairing's own contrast class is not "body"; (2) unaltered
  photography; (3) opacity tints (10–60%) of the two pairing colors; (4) the chart
  exception; (5) the alert exception.
- Light canvas is Honeydew #F3FBF8, not White. White #FFFFFF is allowed only
  [LEADERSHIP DECISION: specimen/print pages | never].
- Covers, section dividers and closing slides default to a dark pairing
  (Blackmoss + Citron unless the deck family specifies otherwise).
- Build rhythm, not monotony: a deck uses 2–4 pairings total, drawn from its
  deck family (brand/pairing-families.md). Adjacent slides may share a pairing.
- Logo: original SVG artwork only, rendered in ONE brand color, meaning the page
  accent or the pairing partner. Never black #000000, never non-brand, never two
  colors, never rotated, distorted, re-typed or crowded. Clear space: horizontal
  1× asset height; vertical 0.5×; graphic-only 0.5×. Vertical lockup on covers
  and closers; horizontal in the staging header; graphic-only for small UI marks
  or as a tonal decorative element.
- Brand geometry: containers and image masks are rounded rectangles with one
  45° chamfered corner, an optional diamond marker and a tracked tab label on
  the top border. Geometry stays subtle: hairlines, no drop shadows, no glows.
- Imagery: real environments, real people and workers, real infrastructure,
  natural sun or warm industrial light; relevant nature (water, forest,
  mountains). Pairing-color overlays or gradient maps are allowed on at most one
  image per spread, and always beside unaltered photography. No staged stock
  scenes, no over-polished edits, no AI images implying real Ocean projects.
- Abstract/futurist renders (particle waves, light trails, textures) are allowed
  only as low-contrast secondary texture on covers, dividers and closers:
  ≤ 1.8:1 contrast against the field, never behind body text, never the subject.
```

### 4.2 `AGENTS.md` — replace the "Fonts and fit" type lines

```md
- Stack Sans Headline only. Bundle and install ExtraLight 200, Light 300,
  Regular 400, Medium 500, SemiBold 600 and Bold 700.
- Tiers (slides): Display 60–96 pt Regular or Bold, tracking −2%, leading 0.95;
  Title 32–40 pt Medium/SemiBold, tracking −1%; Lede 14–16 pt SemiBold UPPERCASE,
  tracking +20%; Body 16–18 pt Regular; Micro-label 10–12 pt SemiBold UPPERCASE,
  tracking +25% (kickers, tabs, header meta, nav, page number); Index numeral
  40–72 pt Light/Regular; Table 13–16 pt; Footnote 10 pt.
- Tiers (Letter/A4): Display 36–48 pt; Title 22–28 pt Medium; Section 16–18 pt
  SemiBold; Body 10.5–11 pt; Micro-label 7.5–8.5 pt SemiBold UPPERCASE, +25%;
  Table 9.5–10 pt; Footer 8–9 pt.
- Tracking is allowed on UPPERCASE labels and ledes only, never on sentence-case
  prose. Headlines are Medium/SemiBold by default; Bold is reserved for display
  and numerals.
- Micro-labels below 12 pt on slides must use a "body" contrast pairing or
  functional ink.
```

### 4.3 `brand/color-system.json` — replace `colors`, `tints`, `roles`

```json
{
  "colors": {
    "blackmoss": "0B1617", "peacock": "102426", "cedar": "1B4039",
    "sage": "618C7C", "honeydew": "F3FBF8", "sprig": "D5CCA0",
    "olive": "6E734C", "citron": "A69856", "crimson": "EB3819"
  },
  "neutralException": { "white": "FFFFFF", "allowed": "LEADERSHIP_DECISION" },
  "functionalInk": ["blackmoss", "honeydew"],
  "tintOpacities": [0.10, 0.20, 0.35, 0.60],
  "pairings": [
    ["blackmoss","peacock","tonal"], ["blackmoss","cedar","tonal"],
    ["blackmoss","sage","body"], ["blackmoss","honeydew","body"],
    ["blackmoss","sprig","body"], ["blackmoss","olive","large"],
    ["blackmoss","citron","body"], ["blackmoss","crimson","large"],
    ["peacock","cedar","tonal"], ["peacock","sage","large"],
    ["peacock","honeydew","body"], ["peacock","sprig","body"],
    ["peacock","olive","large"], ["peacock","citron","body"],
    ["peacock","crimson","large"], ["cedar","sage","large"],
    ["cedar","honeydew","body"], ["cedar","sprig","body"],
    ["cedar","olive","tonal"], ["cedar","citron","large"],
    ["sage","honeydew","large"], ["sage","sprig","tonal"],
    ["honeydew","sprig","tonal"], ["honeydew","olive","body"],
    ["honeydew","citron","tonal"], ["honeydew","crimson","large"],
    ["sprig","olive","large"], ["sprig","citron","tonal"],
    ["sprig","crimson","tonal"], ["olive","citron","tonal"]
  ],
  "forbiddenPairings": [
    ["cedar","crimson"], ["sage","olive"], ["sage","citron"],
    ["sage","crimson"], ["olive","crimson"], ["citron","crimson"]
  ],
  "contrastClasses": { "body": 4.5, "large": 3.0, "tonal": 0 }
}
```

Pairings are order-independent. Either color may be dominant.

### 4.4 New `brand/pairing-families.md` — recommended slide-family matrix

| Slide / page type | Default pairing (dominant + accent) | Alternates | Why |
|---|---|---|---|
| Cover, closer | Blackmoss + Citron | Cedar + Citron (large); Blackmoss + Honeydew | Mirrors the guide cover and back cover |
| Section divider | Blackmoss + Sage | Peacock + Sprig; Cedar + Honeydew | Dark field, calm accent |
| Investment thesis / statement | Cedar + Honeydew | Peacock + Honeydew | High contrast, confident |
| Content, light (most pages) | Honeydew + Blackmoss | Honeydew + Olive; Sage + Honeydew (large titles only) | Guide 00 and 07 |
| Technical diagram / process | Honeydew + Peacock | Peacock + Sage (large) | Structured, precise |
| Financial / metrics | Peacock + Citron | Blackmoss + Citron | Warm emphasis on numbers |
| Market / opportunity | Sprig + Blackmoss (functional) with Citron texture | Sprig + Olive | Guide 06 warmth |
| Project case study / field work | Olive + Honeydew | Honeydew + Olive | Earthy and industrial |
| Proposal body pages | Honeydew + Cedar | Honeydew + Blackmoss | Readable at 10.5–11 pt |
| Report body pages | Honeydew + Blackmoss | Honeydew + Peacock | Long-read contrast |
| Team | Honeydew + Peacock | Sprig + Peacock | Quiet and credible |
| Call to action / urgency | Blackmoss + Crimson (large text only) | Honeydew + Crimson (large only) | Guide 08; use rarely, at most one per deck |
| Appendix | Honeydew + Blackmoss | White + Blackmoss (if approved) | Density |

### 4.5 Chart and data exception

```md
- Single-series charts: one fill = page accent color. Never vary colors by point.
- Multi-series (≤ 4): the accent color, then the dominant color's contrast
  partner, then 60% and 35% opacity tints of the accent. Axis text in functional
  ink; gridlines at 20% tint of the ink.
- Where categories genuinely need a third hue (e.g., a map legend or
  status), one extra brand color may be used if it forms an approved pairing
  with the dominant color. It must cover < 10% of the page area and
  the reason must be recorded in the slide notes.
- Alert exception: Crimson may mark a single alert, risk or deadline (≤ 2% of the
  page area) only when Crimson is approved with the page's dominant color.
```

### 4.6 Image-treatment rules (`DESIGN-SYSTEM.md`, replace the Color-roles paragraph on images)

```md
- Photography is used unaltered by default, inside a chamfer-masked container or
  full-bleed.
- A pairing-color overlay (35–60% opacity) or a two-stop gradient map (dominant →
  accent) is allowed on at most one image per slide/spread, beside an unaltered
  image or a solid pairing field.
- Photo strips inside cards may carry a translucent pairing panel (palette-card
  pattern, Guide 04).
- Abstract/futurist texture: covers, dividers and closers only; ≤ 1.8:1
  against the field; never under body copy.
- Graphic-only mark as decoration: tonal only (≤ 1.8:1), cropped off-canvas
  like Guide 06; never behind small text; never more than one per page.
- Never: generic staged stock, heavy retouching, neon/rainbow effects, fake
  dashboards, AI images of "Ocean projects," or text baked into images.
```

### 4.7 Visual QA checklist and automated checks (`scripts/qa_color.py`, new)

Automated checks, all blocking in release mode:

1. **Declared pairing present** on every slide or page, and a member of `pairings`.
2. **XML color audit.** Every `srgbClr` in `a:solidFill`, `a:ln`, text runs, chart series and table cells maps to a pairing color, a functional ink, or an approved tint. Otherwise fail with slide number and element name.
3. **Render coverage.** Render at 80 dpi. Map pixels to the nearest palette color (ΔRGB < 18) inside non-photo regions. Requirements:
   - dominant color ≥ 40% of the page;
   - accent ≥ 1%;
   - any third brand color ≤ 2% (alert) or ≤ 10% (chart exception, logged);
   - White ≤ 5% unless the White exception is approved.
4. **Contrast.** Text runs < 18.5 pt bold or < 24 pt regular must be ≥ 4.5:1 against their field. Larger text must be ≥ 3:1.
5. **Logo.** The source is `assets/logos/*.svg` rendered in one brand color. Checks: pixel color within ΔRGB 6 of a brand hex; aspect ratio within 1% of source; clear space per lockup.
6. **Font.** Only Stack Sans Headline; embedded; no unembedded font resources, including an unused Helvetica.
7. **Alignment.** Logo, title, body, rules, tables and footer share the left and right margins within 1 pt (documents) or 0.02 in (slides).
8. **Balance.** No slide with more than 45% contiguous empty field area unless it is a cover, divider or closer.
9. Existing checks stay: overflow, overlap, safe area, placeholders, minimum sizes.

Manual review, required in every PR:

- [ ] Every page reads as one color relationship at thumbnail size.
- [ ] Deck rhythm: 2–4 pairings, a dark cover and closer, one Crimson moment at most.
- [ ] Staging header, containers, tabs and chamfers are consistent and subtle.
- [ ] Imagery is real and relevant; treated images sit beside unaltered ones.
- [ ] Micro-labels tracked; prose untracked; headlines Medium/SemiBold.
- [ ] No page looks like an unfilled template.
- [ ] Before/after renders attached for every changed page.

### 4.8 Ban on generic AI deck aesthetics (`AGENTS.md`, new section)

```md
## Banned aesthetics
White-page + black-logo + bold-headline + thin-rule defaults; rainbow or
multi-hue single-series charts; neon glows; blue/purple tech gradients; generic
isometric icons; fake dashboards/UI; stock "handshake/smiling team" scenes;
glossy 3D blobs; drop shadows; emoji; decorative grids behind text; more than
two brand colors competing on a page; meta-copy about design in place of content.
```

---

## 5. Implementation Plan for Codex

### 5.1 Correct now (P0) — PR 1 `brand/guide-compliance-foundation`

1. Replace `brand/color-system.json` with Section 4.3. Delete the Fog, Mist and sageLight tints.
2. Rewrite `AGENTS.md` identity, type and banned sections (4.1, 4.2, 4.8). Rewrite `DESIGN-SYSTEM.md`, `ocean-color-system.md`, `REFERENCE-NOTES.md`, `CHATGPT-PROJECT-INSTRUCTIONS.md`, `CODEX-PROMPTS.md` and `README.md` line 4 to match. Add `brand/pairing-families.md` (4.4).
3. Logo pipeline: render SVGs to PNG per brand color at build time (e.g., `resvg`/`cairosvg`). `logo(s, {lockup, color})` defaults to the page accent. Remove the black PNG.
4. Add a `pairing` parameter to every `OceanDeck` layout and to the document JSON schema. Throw on unapproved pairs. Set the background to the dominant color and route all accents through the pairing.
5. Add `scripts/qa_color.py` (checks 1–5) and wire it into `npm test` and CI.

### 5.2 Correct next (P1) — PR 2 `layouts/guide-geometry-and-type`

1. Staging-header component for 16:9 (a 0.55-in band: logo cell, meta cell, section nav with active chip, page number) and a Letter version.
2. Chamfer container, diamond marker, tab label and chamfer image mask as reusable PptxGenJS custom geometry and ReportLab path helpers.
3. Type tiers from 4.2, including tracked micro-labels (`charSpacing` in PPTX, `Paragraph` with `wordSpace`/`charSpace` in ReportLab), Medium/SemiBold titles, Light numerals, and the full weight set bundled.
4. Chart colors per 4.5.
5. Fix `publication.py` frame padding and table widths (alignment defect). Remove the unembedded Helvetica reference.
6. Encode vertical and graphic-only lockups with 0.5× clearance.
7. Add QA checks 6–8.

### 5.3 PR 3 `specimens/guide-compliant-references`

1. Delete `templates/ocean-layout-reference.pptx` or regenerate it in CI. Regenerate `output/pdf/ocean-layout-reference.pdf`.
2. Rebuild the deck specimen as a 13-slide demonstration: dark cover (Blackmoss + Citron, vertical lockup, low-contrast texture), palette slide (nine cards), pairing slide, dividers, statement, diagram, metrics, chart, case-study photo card, team, ask (no visible "[TBD]": use labeled sample values or a styled "Amount to be confirmed" field), appendix, and a closer.
3. Rebuild the proposal specimen at 4–6 pages: dark cover, project-at-a-glance container, scope and exclusions, schedule, commercial terms table, acceptance block.
4. Rebuild the report specimen at 4–6 pages: cover, executive-summary callout, figure with caption, table spanning pages, limitations, appendix.
5. Commit before/after renders under `output/renders/` and attach them to the PR. Do not auto-merge.

### 5.4 Keep as-is

Truth rules, the investor sub-rules, the fit/overflow engine, placeholder gates, font embedding checks, CI scaffolding, native editable charts and tables, the logo aspect fix, and the folder structure.

### 5.5 Decisions needed from Ocean leadership

| # | Decision | Options | Recommendation |
|---|---|---|---|
| 1 | Is White `#FFFFFF` ever a canvas? | Never / print and appendix only / free | Print and appendix only; Honeydew everywhere else |
| 2 | Default cover pairing | Blackmoss + Citron / Cedar + Citron / Blackmoss + Honeydew | Blackmoss + Citron (matches the guide cover) |
| 3 | Low-contrast abstract textures allowed on covers and dividers? | Yes, tonal only / No | Yes, tonal only, as the guide permits |
| 4 | Logo recolor within brand colors | Allowed per pairing / Blackmoss only | Allowed per pairing, which is the guide's own practice |
| 5 | Confirm guide errata | 30 unique pairings (Blackmoss + Crimson; duplicate Sprig + Citron) | Confirm, and ask the designer for a corrected Guide 05 |
| 6 | Crimson budget | 1 per deck / per section | 1 per deck, large type only |
| 7 | Photo library | Real Ocean project photos / licensed real-world stock / both | Both, labeled; never imply stock is an Ocean project |
| 8 | 9:16 guide to 16:9 and Letter translation | Approve the staging-header adaptation | Approve after the PR 2 specimens |
| 9 | Designer source file | Request Figma/AI to confirm weights and tracking | Request it |

### 5.6 Test protocol for the new system

Run all three in PR 3, render them, and review them against this audit.

| Test | Build | Must pass |
|---|---|---|
| Investor deck (12–13 slides) | Ocean platform teaser from `source/` only, with illustrative numbers labeled | Two-color check on every slide; 2–4 pairings; dark cover and closer; one Crimson moment at most; chart exception logged; no "[TBD]" in release; staging header on every interior slide; opens cleanly in PowerPoint 365 and Keynote |
| Commercial proposal (4–6 pages, Letter) | Solar-plus-storage structure with neutral sample scope, no real prices | Honeydew pages; aligned margins (±1 pt); tables within the rule; cover pairing; acceptance block; embedded fonts only |
| Technical report (4–6 pages, Letter) | Site-feasibility structure with a sample figure and photo card | Figure and photo in chamfer masks; one treated image beside an unaltered one; multi-page tables repeat headers; body contrast ≥ 4.5:1 |
| Regression | `npm test`, `qa.py`, `qa_pdf.py`, `qa_color.py` | All pass in CI; renders uploaded as artifacts |

---

Evidence board: `ocean-audit-evidence-board.png`. Top row: all 11 guide pages with their dominant and accent pairing. Bottom row: current deck slides 1, 2, 8 and 9, plus proposal page 1 and report page 1.
