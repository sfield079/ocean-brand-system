# Ocean Brand Bible — Typography, Weight and Text-System Rules

Companion to "Ocean Brand Guide Page-by-Page Analysis." This file treats `Ocean_StyleGuide_2026.pdf` as the brand bible: every size, weight, tracking value, line pitch and case choice in it is taken as a rule, whether or not the guide writes it down.

## How the values were measured

The guide's text layer does not store font weights (the fonts are embedded as outlines). But the guide shows in its own images which weight looks like what: Guide 06 prints six specimen lines labeled EXTRA LIGHT 200, LIGHT 300, REGULAR 400, MEDIUM 500, SEMIBOLD 600 and BOLD 700, and states the family uses "6 weights (standard)", so every weight is one of those six.

Every weight below was therefore read **from the page images, against the guide's own labeled specimens**:
1. Each page was rendered as an image at 600–1200 dpi.
2. The thickness of the vertical strokes was measured in pixels on every text style and divided by the type size. Stroke-to-size ratio does not change with scale, so a 191 pt title can be compared directly with a 40 pt specimen line.
3. The guide's labeled specimens give the reference ratios: ExtraLight 0.072, Light 0.090, Regular 0.105, Medium 0.126, SemiBold 0.132, Bold 0.141 (stroke width per em).
4. Each style was assigned the specimen weight it matches.

Tracking was calculated from character positions against the font's natural advance widths and is given in em (Illustrator/Figma units ÷ 1000). Line pitch was measured baseline to baseline.

Confidence: all 27 styles are now matched to the guide's own specimens, including the three large display styles that were uncertain before (cover title 0.090 = Light, type specimen 0.090 = Light, index numerals 0.091 = Light). The only borderline reading is the four digits of the cover "2026" (0.116, between Regular and Medium). Digits and capitals read slightly heavier than lowercase at the same weight, and the matching subtitle beside it reads Regular, so it is recorded as Regular.

---

## Rule 1 — The complete type table

Every text style in the guide. Nothing else is used.

| # | Role | Size | Weight | Case | Tracking | Line pitch | Where |
|---|---|---|---|---|---|---|---|
| T1 | Cover display | 191 pt | Light 300 | Title case | −0.04 em (−40) | 160 pt (84%) | "Brand / Guidelines" |
| T2 | Contents display | 191 pt | **Bold 700** | Title case | −0.06 em (−60) | 160 pt (84%) | "Table of / Contents" |
| T3 | Type specimen | 142 pt | Light 300 | Title case | −0.06 em (−60) | 142 pt (100%) | "Stack Sans / Headline" |
| T4 | Index numeral | 90 pt | Light 300 | Figures | ≈ −0.06 em | 121 pt row pitch | Contents 01–07 |
| T5 | Specimen sentence / glyph set | 40 pt | Each line in its named weight; glyph sets Medium 500 | Sentence case, no period | −0.02 em (−20) | 96 pt between labeled lines; 40 pt (100%) within glyph sets | Guide 06 |
| T6 | Page title | 35 pt | **Medium 500** | Title case, two lines | −0.01 em (−10) | 39 pt (111%) | Every interior page |
| T7 | Contents entry title | 35 pt | **Regular 400** | Title case | −0.01 em | single line | Contents |
| T8 | Color name | 35 pt | Medium 500 | Title case | −0.01 em | single line | Guide 04 cards |
| T9 | Edition / subtitle | 30 pt | Regular 400 | Title case | −0.02 em (−20) | 33 pt (110%) | Cover "2026", "Small Format / Core Visual Identity Manual", "Ocean RCS"; contents subtitle |
| T10 | Source credit | 30 pt | Medium 500 | Title case | −0.01 em | single line | "Google Fonts" |
| T11 | Section subhead | 25 pt | **Light 300** | Title case, two lines | −0.01 em | 28 pt (112%) | "Approved General-Use / 2-Color Pairings" |
| T12 | Cover chapter list | 14 pt | Bold 700 | ALL CAPS | +0.25 em (250) | 22 pt (157%) | Cover, right-aligned |
| T13 | Caption | 14 pt | Regular 400 | Sentence case, no end period | 0 | 20 pt (143%) | DO NOT captions |
| T14 | Data value | 14 pt | Bold 700 | ALL CAPS / figures | +0.25 em | single line | HEX and RGB values; padding values |
| T15 | Warning chip | 14 pt | Bold 700 | ALL CAPS | +0.25 em | single line | "DO NOT", reversed out of a Citron chip |
| T16 | Contents kicker | 12 pt | Bold 700 | ALL CAPS | +0.25 em | — | Contents |
| T17 | Specimen box label | 12 pt | Bold 700 | ALL CAPS | **+0.125 em (125)** | — | "LETTERFORMS", "NUMBERS & PUNCTUATION" |
| T18 | Section kicker | 11 pt | Bold 700 | ALL CAPS | +0.25 em | — | Above every page title |
| T19 | Lede | 11 pt | Bold 700 | ALL CAPS | +0.25 em | 17 pt (155%) | Right column, bottom-aligned to title |
| T20 | Body | 11 pt | Regular 400 | Sentence case | 0 | 17 pt (155%); paragraph gap = one empty line (34 pt baseline to baseline) | Justified, last line left |
| T21 | Emphasis in body | 11 pt | Bold 700 | Sentence case | 0 | 17 pt | Once only: "Not all brand colors play nicely together." |
| T22 | Navigation | 11 pt | Bold 700 | ALL CAPS | +0.25 em | — | Header; active item reversed in a chip |
| T23 | Tab / container label | 11 pt | Bold 700 | ALL CAPS | +0.25 em | — | Container tabs, weight box labels, "LATIN - 6 WEIGHTS…" |
| T24 | Meta key | 11 pt | **Light 300** | ALL CAPS | +0.25 em | 16 pt (145%) | "SMALL FORMAT", "VISUAL IDENTITY MANUAL", "PAGE" |
| T25 | Meta value | 11 pt | Bold 700 | ALL CAPS | +0.25 em | 16 pt | "OCEAN RCS", the page number |
| T26 | Data key | 11 pt | Regular 400 | ALL CAPS | +0.25 em | — | "HEX", "RGB", "PADDING", pairing names |
| T27 | Weight list | 11 pt | Regular 400 | ALL CAPS, middle-dot bullet | +0.25 em | 20 pt (182%) | Guide 06 weight inventory |

---

## Rule 2 — The weight rules the table reveals

### 2.1 Weight falls as size rises
Big type is light; small type is bold.
- **Display (90–191 pt): Light 300.** Cover title, type specimen, index numerals.
- **Headings (35–40 pt): Medium 500.** Page titles, color names, glyph sets.
- **Reading text (11–14 pt): Regular 400.** Body and captions.
- **Micro-labels (11–14 pt caps): Bold 700.** Kickers, ledes, navigation, tabs, values, chips.

This gives the guide its look: thin, calm, large shapes against small, dense, bold labels, with the middle carried by Medium headings. A layout that sets big headlines in Bold and small labels in Regular reverses the Ocean system.

### 2.2 One deliberate exception: the contents page is Bold
"Table of Contents" is 191 pt **Bold**, at the same size as the Light cover title. The cover is atmosphere; the contents page is structure. Use Bold display only for navigation and index pages (contents, agenda, section index). Never use it for a cover or a statement.

### 2.3 Hierarchy within one level is set by weight, not size
- Contents: the entry titles are **Regular** 35 pt, while every page title is **Medium** 35 pt. Same size, lower weight, because an index entry is a reference to a title, not the title itself.
- Guide 05: the 25 pt subhead is **Light**, below the Medium 35 pt title.
- Numerals are Light (T4) beside Regular titles (T7): the number is secondary to the name.

### 2.4 Key light, value bold
Every label-plus-value pair uses a light key and a bold value, at the same size and tracking:
- Header: "SMALL FORMAT / VISUAL IDENTITY MANUAL" (Light) → "OCEAN RCS" (Bold)
- Header: "PAGE" (Light) → "01" (Bold)
- Palette: "HEX", "RGB" (Regular) → "0B1617", "11/22/23" (Bold, 14 pt)
- Spacing: "PADDING" (Regular, Sprig) → "0.5X FULL ASSET HEIGHT" (Bold, Cedar)

The value may also step up in size (11 → 14 pt) and in tone (Sprig key, Cedar value). The key never outweighs the value. Use this pattern for every KPI tile, spec table, proposal summary ("SYSTEM SIZE" Light → "412 KW DC" Bold) and cover meta block.

### 2.5 Bold appears in only three places
1. Tracked caps at 11–14 pt (labels, ledes, navigation, values, chips).
2. The contents display (2.2).
3. One sentence of body copy in the whole guide (T21): the warning "Not all brand colors play nicely together." Bold in body text is a single-sentence warning device, not an emphasis habit. At most one bold sentence per page.

### 2.6 SemiBold and ExtraLight are specimen-only
Neither SemiBold 600 nor ExtraLight 200 is used anywhere in the guide except on its own specimen line. The working weights are exactly four: **Light 300, Regular 400, Medium 500 and Bold 700.** A builder that reaches for SemiBold is off-system.

### 2.7 The weight specimen is also the voice specimen
On Guide 06 each weight carries a sentence whose meaning matches its weight. ExtraLight carries "Bright beams… quiet rooftops" and Bold carries "Lines are clean, angles are sharp, energy flows." The lighter the weight, the quieter the message. Use lighter weights for atmosphere and heavier ones for assertions.

---

## Rule 3 — Tracking ladder

| Text | Tracking |
|---|---|
| All-caps labels at 11–14 pt (every kind) | **+0.25 em** — one value, no exceptions except below |
| Specimen box labels (12 pt Bold) | +0.125 em |
| Body and captions (11–14 pt sentence case) | 0 |
| 35 pt titles, names, 25 pt subhead, 30 pt credit | −0.01 em |
| 30 pt subtitle, 40 pt specimen lines | −0.02 em |
| 191 pt Light cover display | −0.04 em |
| 191 pt Bold display, 142 pt specimen, 90 pt numerals | −0.06 em |

Rules:
- **Caps are always tracked; lowercase and mixed case are never positively tracked.** No run in the guide uses untracked caps or tracked lowercase.
- **Tracking tightens as size grows.** Bold display gets tighter tracking than Light display at the same size (−0.06 vs −0.04), because heavier letters need less air.

---

## Rule 4 — Leading ladder

| Size | Pitch | Ratio |
|---|---|---|
| 191 pt display | 160 pt | 0.84 (lines nearly touch) |
| 142 pt specimen; 40 pt glyph sets | = size | 1.00 |
| 25–35 pt titles and subheads | 28–39 pt | 1.10–1.12 |
| 14 pt captions | 20 pt | 1.43 |
| 11 pt header meta | 16 pt | 1.45 |
| 11 pt body and ledes | 17 pt | 1.55 |
| 14 pt cover chapter list | 22 pt | 1.57 |
| 11 pt weight list | 20 pt | 1.82 |

Rule: leading opens as size falls. Display type is set solid or tighter; reading text is set at about 1.5. Paragraphs are separated by one full empty line, never by a partial space.

---

## Rule 5 — Case, punctuation and notation

| Item | Rule | Evidence |
|---|---|---|
| Titles, subheads, color names, contents entries | Title Case | Every 25–35 pt run |
| Body | Sentence case with full punctuation | Guides 01–08 |
| Captions | Sentence case, **no ending period** | All nine DO NOT captions |
| Labels, kickers, ledes, navigation, values | ALL CAPS via styling (the text layer is stored in lower or mixed case) | Text layer vs render |
| Title conjunction | "&" (shows the Stack Sans ampersand), never "and" | 4 of 7 titles |
| Label conjunction | "+" between color names, drawn as a circled plus on tiles | Guide 05 |
| Navigation separator | Spaced em dash " — " | Header |
| List bullet (inventory) | Middle dot "·" | Guide 06 weight list |
| Item marker (labeled specimen) | Filled diamond | Guide 06, Guides 01–02 containers |
| Page and index numbers | Always two digits: 00, 01, … 08 | Header, contents |
| Hex values | Uppercase, no "#" | Guide 04 |
| RGB values | Slash-separated, no spaces: 11/22/23 | Guide 04 |
| Multipliers | Lowercase x after the number: 0.5x, 1x | Guide 02 |
| Brand name in running text | "Ocean" capitalized; "Ocean RCS" in meta | Body copy |
| Units in labels | Written out in caps: "FULL ASSET HEIGHT" | Guide 02 |

Correction to the page-by-page report: errata #11 ("lowercase ocean") and #12 ("clean" after a period) are withdrawn. Both strings sit only in ledes, which render in ALL CAPS, so the reader sees "THE OCEAN LOGO…" and "…WORK WITH. CLEAN, DIRECTIONAL, AND FULL OF PURPOSE." The second is a deliberate sentence fragment in the brand voice, not an error.

---

## Rule 6 — Alignment and measure

- **Everything is left-aligned** to a grid line, with two exceptions, both on the cover: "2026" and the chapter list are right-aligned to the right margin (x 1016). Right alignment is a cover-only device.
- **Body is justified** (last line flush left). Ledes and captions are ragged right.
- **Measure:** 11 pt body runs about 380 pt wide on standard pages (≈ 75–80 characters) and about 540 pt on the imagery pages (≈ 105 characters). Ledes run about 20–27 characters per line in tracked caps, which is why they wrap to two to five lines.
- **Lede alignment:** the last lede baseline sits exactly on the last title baseline (y 370). Ledes grow upward, not downward.
- **Vertical rhythm of the title block:** header bottom → kicker baseline 56 pt; kicker → first title baseline 49 pt; title lines 39 pt apart; last title baseline → rule 23 pt; rule → first body baseline 33 pt.

---

## Rule 7 — Color of type

- One ink per page. Every run on a page (title, kicker, lede, body, navigation, meta) is the same palette color, except:
  - reversed text inside a filled chip (the field color on an ink chip);
  - a key/value pair can split into a tonal key and an ink value (Guide 02: Sprig key, Cedar value);
  - specimen content, such as color cards, where each card takes its own partner color.
- No gray type. No tints. No opacity on text. Every text pixel is an exact palette hex.

---

## Rule 8 — Other system rules of the same kind

| Rule | Detail |
|---|---|
| Stroke ladder | Header frame and row divider 2 pt; title rule and contents row rules 1 pt; container and tile outlines hairline; closing rules heavy. Heavier lines mean higher structural rank |
| One radius family | All containers, tiles, photo masks and the back-cover frame share the same rounded-plus-one-chamfer shape; chamfers are 45° |
| Markers count | 1, 2, 3 diamonds for containers 1, 2, 3 |
| One accent state | The active navigation item and the active icon cell are the only reversed elements in the header |
| Symbol meaning | Crimson triangle = warning; circle-slash = prohibition; circled plus = pairing; crosshair = measurement |
| Photography never carries text | No type is set on photos anywhere in the guide. Text sits on flat fields; photos sit in masked containers |
| No drop shadows, glows, gradients on UI or bevels | None anywhere; the only gradients are inside abstract imagery (Guide 08, back cover) |
| No page repeats a pairing | Nine interior pages, nine different field/ink pairings |

---

## Rule 9 — Translating the ladder to Ocean deliverables (approved 26 Sep 2026; sizes flagged as leadership-adjustable)

The guide is a 1080 × 1920 pt vertical "small format." Decks and documents need the same ladder at a different scale. **Keep the weights, case, tracking and leading ratios exactly; scale only the sizes.** Approved sizes (implemented in the layout code, `lib/ocean.js` and `lib/publication.py`, with tracking in `tokens/ocean.tokens.json`). Reports and presentations are separate systems; see "Reports and presentations are separate systems" in the decisions file:

| Role | Guide | Presentations: 16:9 (13.33 × 7.5 in) | Reports and proposals: Letter portrait |
|---|---|---|---|
| Cover display (Light, −0.04) | 191 | 96–120 | 60–72 |
| Index/agenda display (Bold, −0.06) | 191 | 96 | 60 |
| Section numeral (Light) | 90 | 60 | 40 |
| Slide / page title (Medium, −0.01) | 35 | 32–36 | 22–24 |
| Subhead (Light, −0.01) | 25 | 22–24 | 16 |
| Statement line (named weight, −0.02) | 40 | 36–40 | 24 |
| Data value (Bold caps +0.25) | 14 | 14–16 | 10 |
| Caption (Regular, no period) | 14 | 12–14 | 9 |
| Body (Regular, justified, 1.55) | 11 | 14–16 | 9.5–10 |
| Micro-label, kicker, lede, nav (Bold caps +0.25) | 11 | 10.5–12 | 7.5–8 |
| Meta key (Light caps +0.25) | 11 | 10.5–12 | 7.5–8 |

Floors: no text under 10.5 pt on slides, and no tracked caps under 7.5 pt in print.

---

## Rule 10 — Repository encoding (for Codex, after your approval)

Implemented 26 Sep 2026 in the layout libraries. Original instruction: add a type-scale token file with the 27 styles above (T1–T27) as named tokens: role, weight, case, tracking and leading ratio, plus size per format. Then:

1. Make every text helper in the deck and document builders take a style token, not a free size and weight.
2. Add a QA check that fails on:
   - untracked caps or tracked lowercase;
   - Bold at display size outside an index or agenda page;
   - SemiBold or ExtraLight anywhere;
   - more than one bold body sentence per page;
   - a label whose key is heavier than its value;
   - body not justified;
   - captions ending in a period;
   - text on photos;
   - any text color that is not the page ink.
3. Keep the measured values here as the controlling reference.
