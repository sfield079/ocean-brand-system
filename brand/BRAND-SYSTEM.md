# Ocean RCS Brand System: Repo-Wide Specification

Status: approved by leadership 26 September 2026 (decisions L1–L6 in Section 17); ready for Codex
Controls: Ocean Style Guide 2026 (the "Brand Bible"), plus the approved decisions in "Ocean Approved Decisions and Document Profiles" and the typography rules in "Ocean Brand Bible Typography Rules"
Scope change: the repository `sfield079/ocean-deck-system` stops being a deck generator. It becomes the **single brand source of truth** for every Ocean surface: oceanrcs.com, Ocean micro-apps, decks, reports, proposals, formal documents, business cards, email, digital signage, charts, icons and graphics.

Merged into the repository on 26 September 2026, and the production libraries were migrated the same day. Section 18 records the status.

---

## 1. What changes

| Before | After |
|---|---|
| Repo = presentation and PDF generator | Repo = Ocean Brand System. Documents are one consumer among several |
| Colors and type defined inside deck code | Colors, type, spacing, radius, chamfer and icon settings live in **tokens**. Every surface reads from the same token files |
| Website excluded | oceanrcs.com and every micro-app must follow the system. The current site is still **not a reference**; it is a **target** to be brought into compliance |
| Formal documents styled like reports | Formal documents follow a separate plain standard (Section 6): top-tier law-firm/institutional quality, logo only, no brand decoration |
| No card, email, signage, chart, icon or graphic rules | Each has a profile and assets below |
| Deck rules assume one length | Deck recipes scale the same rules from 5 to 30 slides (Section 8) |

---

## 2. Proposed repository structure

Rename to `ocean-brand-system` (approved, L1). Keep the old name as a redirect.

```
ocean-brand-system/
  AGENTS.md                         root rules for any AI agent (short; points to brand/)
  brand/
    Ocean_StyleGuide_2026.pdf       the Brand Bible (read-only)
    BRAND-SYSTEM.md                 this specification
    decisions.md                    approved decision register (D1–D20)
    typography.md                   T1–T27 and Rules 1–10
    errata.md                       guide errors and the corrected reading
  tokens/
    ocean.tokens.json               source of truth (colors, weights, tracking, radius, chamfer, icon)
    type-scale.json                 sizes per surface (deck, letter, web, signage, card); leadership-adjustable
    contrast-matrix.json            measured WCAG ratios for every palette pair
    build/ocean.css                 generated CSS custom properties + data-pair themes
    build/tailwind.preset.js        generated Tailwind preset for oceanrcs.com and micro-apps
    build/ocean.mplstyle            generated chart style
  assets/
    logos/                          official SVG/EPS/PDF masters + generated one-color variants (9 palette colors)
    fonts/                          Stack Sans Headline (OFL) + Material Symbols Outlined (Apache 2.0)
    icons/svg/                      Ocean icon kit (Material Symbols Outlined, wght 400, fill 0)
    icons/manifest.json             approved icon names by group
    graphics/                       chamfer frames, diamond counters, double rule, risk flag, nav chip
    textures/                       procedural wave textures (generator + exported PNG per pairing)
    images/                         image library + image-manifest.json (source, license, AI flag)
  surfaces/
    web/                            oceanrcs.com component rules + reference page
    apps/                           micro-app shell, dashboard and table patterns
    decks/                          16:9 layouts, recipes, starter
    reports/                        Letter report layouts
    proposals/                      Letter proposal layouts
    formal/                         contracts, letters, memos, NDAs, invoices, change orders
    print/                          business cards, letterhead, envelopes
    email/                          email signature HTML
    signage/                        lobby, site and live-data screen templates
    social/                         social and digital graphics
  charts/                           chart style, helper library, examples
  qa/                               render-and-inspect checks per surface
  output/                           generated artifacts (never hand-edited)
```

Rule: **tokens first**. A surface may not hard-code a hex value, weight or tracking number. Codex adds a QA check that fails on any hex outside `tokens/`.

---

## 3. Core tokens (all surfaces)

### Color
Blackmoss `#0B1617`, Peacock `#102426`, Cedar `#1B4039`, Sage `#618C7C`, Olive `#6E734C`, Citron `#A69856`, Crimson `#EB3819`, Sprig `#D5CCA0`, Honeydew `#F3FBF8`, plus White `#FFFFFF` for print only (D4). Only the 30 approved pairings may be used as field + ink (decisions file, Part 2).

### Measured contrast that governs use (WCAG 2.x)
Every pair below is also on the approved pairing list. Contrast decides what each pair may carry.

| Pair | Ratio | Allowed use |
|---|---|---|
| Honeydew / Blackmoss | 17.5 | Everything |
| Honeydew / Peacock | 15.3 | Everything |
| Honeydew / Cedar | 10.9 | Everything |
| Sprig / Peacock | 10.0 | Everything |
| Blackmoss / Citron | 6.4 | Everything |
| Blackmoss / Sage | 4.9 | Everything, but prefer large text |
| Honeydew / Olive | 4.7 | Everything, but prefer large text |
| Blackmoss / Crimson | 4.5 | Large text only (18 pt / 24 px and up) |
| Honeydew / Crimson | 3.9 | Large text and graphics only |
| **Sage / Honeydew (default cover)** | **3.6** | **Large text and graphics only.** Covers, card fronts, hero lines. Never body text |
| Honeydew / Citron | 2.8 | Graphics and fills only, never text |
| Honeydew / Sprig | 1.5 | Texture only |

### Type
Stack Sans Headline only. Four working weights: Light 300, Regular 400, Medium 500, Bold 700 (SemiBold and ExtraLight appear in the guide only as specimens). All caps always Bold or Light at +0.25 em. Sizes come from `type-scale.json` per surface.

### Shape
Rounded corners (4 / 12 / 20) and a single 45° chamfer (12 / 24 / 44), taken from the guide's panels and header frame. Frames are hairline (1 px) or structural (2 px). One chamfer per object, top-left for image and hero frames, bottom-right for data tiles.

### Icons
Measured against the guide's header strip: **Material Symbols Outlined, weight 400, fill 0, grade 0, optical size 24**. This matches the guide's glyph density to within 1% on three icons. The seven guide icons are `layers`, `dashboard`, `grid_guides`, `palette`, `format_color_fill`, `format_size` and a mirrored `burst_mode`. In the guide each icon sits at 24 pt inside a 48 pt cell, which gives the ratio rule "icon = 50% of its cell."

---

## 4. Website and micro-apps

oceanrcs.com and all Ocean micro-apps (dashboards, portals, calculators, internal tools) use `tokens/build/ocean.css` or the Tailwind preset. Reference renders: `web_home.png`, `app_dashboard.png`.

**Marketing site (oceanrcs.com)**
- Default theme: Honeydew field, Blackmoss ink. Each page section may switch to one other approved pairing through `data-pair`, with no two adjacent sections on the same pairing. Sage + Honeydew bands carry large text and icons only.
- Header: the guide's framed header adapted for the web. It has a 2 px frame with cells for logo, primary navigation (Bold caps, +0.25 em, 12 px), one filled call-to-action cell and icon cells. On mobile it collapses to logo, CTA and menu cells.
- Hero: Light display type at hero tracking (−0.04 em), a Bold caps kicker, a Regular lede at 18 px / 28 px, and a photo with the top-left chamfer.
- Buttons: the primary button is ink-filled with a 12 px chamfer and Bold caps. The secondary button is a 2 px outline with a trailing `arrow_forward` icon. No pill buttons, gradients or shadows.
- Cards: hairline frame with a bottom-right chamfer, a 32 px icon, a caps key and a Regular description.
- Motion: fades and short translates of 150–250 ms only. The wave texture may drift slowly on the hero. No parallax stacks, bouncing or glow effects.
- Accessibility: body text ≥4.5:1 (D2). Focus rings are 2 px in the section ink. The site must respect reduced-motion preferences.
- Fonts: self-host Stack Sans Headline (woff2) and a subset of Material Symbols, and preload both.

**Micro-apps**
- **Default theme (approved, L3):** Blackmoss field, Honeydew ink, Sage hairline tiles (`app_dashboard.png`).
- **Alternative theme (approved, L3):** Honeydew field, Peacock ink and tiles, with the active navigation item inverted to a Peacock chip (`app_dashboard_light.png`). Use it for document-like tools, daylight or field tablets, and client-facing portals.
- Every app ships both themes from the same tokens, with a user toggle. The app remembers the choice and follows the operating system setting on first load.
- The graphic mark sits in the navigation footer with the app name and version (for example OCEAN OPS · V 1.0), and it is the app icon and favicon.
- Shell: 240 px left navigation with icon + caps labels. The active item is inverted (field and ink swapped), matching the guide's active-tab treatment.
- Key-figure tiles: hairline Sage frame with bottom-right chamfer, a Light caps key, a Light number at display tracking and a Regular note.
- Tables: Bold caps headers at +0.25 em, row rules in ink at 20% opacity, and numbers in Bold caps with +0.12 em tracking.
- Alerts are the only place Crimson appears in an app, as the risk-flag triangle beside the affected value.

---

## 5. Presentations, reports and proposals

These stay as defined in the decisions file (P2–P7, and the reports-vs-presentations table). Additions:
- Charts follow Section 9 and icons follow Section 3.
- Deck length follows Section 8.
- A report delivered as slides uses the presentation system.

---

## 6. Formal documents: plain institutional standard

**Applies to:** contracts, EPC agreements, NDAs, MSAs, term sheets, letters, memos, board resolutions, invoices, change orders, lien waivers and transmittals. Reference renders: `f01_letter`, `f02_contract`, `f03_signature`.

**The standard:** the document should look like it came from a top-tier law firm or institutional investor. It is quiet, typographic and unbranded except for the logo. Nothing on the page should look designed.

| Element | Rule |
|---|---|
| Page | US Letter, White `#FFFFFF`, 1 in (72 pt) margins on all sides |
| Color | Blackmoss only. No second color and no tints |
| Logo | Horizontal logo, **28 pt tall (1.4 in wide) on letters, 24 pt tall on legal documents**, top-left of page 1. Continuation pages carry the **graphic mark only at 24 pt** top-left, with the document number top-right |
| Fonts (approved, L5) | **Legal documents** (contracts, EPC agreements, NDAs, MSAs, term sheets, resolutions, lien waivers): **Times New Roman** throughout, the standard business and court font every counterparty and law firm can open and redline. **Letters, memos, invoices, quotes, change orders and transmittals:** Stack Sans Headline. Liberation Serif (metric-identical) is used only where Times New Roman is not installed |
| Title | Legal: Times New Roman Bold 15 pt / 20 pt, centered. Letters: Stack Sans Medium 15 pt. Sentence case |
| Body | Legal: Times New Roman 11.5 pt / 16.5 pt. Letters: Stack Sans Regular 10.5 pt / 15.5 pt. Always **left-aligned, ragged right** (justified text creates uneven spacing) |
| Headings | Legal: Times New Roman Bold, numbered ("1.  Definitions"). Letters: Stack Sans Medium. Sentence case. No tracked caps |
| Clause numbers | Hanging indent of 28 pt. Numbered 1, 1.1, 1.1(a) |
| Defined terms | Medium inside quotation marks on first definition. Never bold-colored or underlined |
| Footer | Document number and version on the left, "Page X of Y" in the center, and initials boxes (contracts) or "Confidential" on the right, all Regular 7.5 pt |
| Signature page | Two blocks: party label (Medium), a 46 pt signature space with a hairline rule, then name, title and date |
| Forbidden | Staging header frame, tracked caps headings, textures, photos, chamfers, color fields, Crimson, charts, icons |
| Permitted micro-graphic | One Blackmoss diamond, centered, as the end-of-document mark before the signature blocks. Nothing else |
| Tables (invoices, change orders) | Hairline rules only, Regular numbers aligned right on tabular figures, and one Medium total line |

Word/Google Docs templates: Codex builds `.docx` versions with named paragraph styles (`Ocean Title`, `Ocean Heading 1`, `Ocean Body`, `Ocean Clause 1.1`, `Ocean Footer`) so legal counsel can edit them without breaking the layout. Legal templates are set in Times New Roman so they open identically on any computer.

---

## 7. Business cards and stationery

Reference renders: `card_front`, `card_back` (press-ready PDF with 0.125 in bleed).

| Element | Rule |
|---|---|
| Size | US 3.5 × 2 in, 0.125 in bleed, 0.125 in safe zone inside trim |
| Stock and finish | 16 pt or heavier uncoated, or 32 pt duplex. Matte. No gloss or foil. **Approved extras (L4): a registered emboss of the printed vertical logo on the front, and optionally an edge color in Sage** |
| Front | Blackmoss field with the wave texture and a hairline Honeydew chamfer frame. Vertical logo in Honeydew, centered, **0.9 in tall** (45% of card height). Nothing else |
| Back | Honeydew field with Blackmoss ink. Horizontal logo top-left, **16 pt tall (0.8 in wide)**. A personal QR code (0.53 in square, Blackmoss, no quiet-zone border printed beyond 1 module) sits right of the name, linking to the person's contact page on oceanrcs.com. Location and OCEAN RCS in the top-right (caps, Light key over Bold value). Name in Medium 13 pt. Title in Bold caps 4.8 pt at +0.25 em. A hairline rule. Contact details as a Light-key / Bold-value grid |
| Contact rules | Max four lines: mobile, email, web, license. Email in lowercase (the only lowercase caps-line exception). No fax or social handles. The QR code is approved (L4) and always links to an oceanrcs.com URL, never a third-party link |
| Print color | Build CMYK from tokens with a press proof. Blackmoss must not print as rich black; specify the brand mix |

The same logic extends to letterhead (identical to the formal-letter header), envelopes (logo top-left, return address Regular 8 pt) and the badge/lanyard (Blackmoss front, name Medium).

---

## 8. Deck recipes: same system at any length

Reference render: `deck_recipes.png`.

| Deck length | Required spine | Content pairings | Crimson | Dividers | Agenda |
|---|---|---|---|---|---|
| 1–4 (one-pager deck) | Cover + content | 1–2 | None, or one small accent | No | No |
| 5–7 | Cover, content, one key-number slide, close | 2 | One key-number moment | No | No |
| 8–11 | Cover, agenda, sections, key number, next steps, close | 3 | One | No | Yes |
| 12–20 | Cover, agenda, one divider per section, key number, next steps, close | 3–4 | One | Yes, one per section | Yes |
| 21–30 | As above, plus an appendix after close (White/Honeydew + Blackmoss, report-style) | 4 | One (maximum two, in different sections) | Yes | Yes |
| 30+ | Split into a presentation deck (≤20) and a report (P3) | — | — | — | — |

**Rules at every length**
- The cover and close use the same brand pairing (Sage + Honeydew by default, D6).
- Pairings are assigned per section, not per slide. Every slide in a section uses that section's pairing, and adjacent sections never share one. Bookends, the agenda, dividers and the key-number slide do not count toward the 2–4 content pairings.
- Dividers use the section's ink as a full field (for example Peacock + Honeydew for a section whose slides are Honeydew + Peacock) with a Light numeral (01, 02) and the section name.
- **Rhythm:** at least one photo-led slide in every five, no more than two dense slides (tables or long text) in a row, and one chart per slide.
- Staging-header navigation lists the deck's sections (maximum five). Decks with more sections group them.
- Numbering is continuous. The appendix restarts at A1.
- The recipe is data: `surfaces/decks/recipes.json` holds the slide order and pairing per length, so Codex generates a 5-, 10- or 15-slide deck from the same content file.

---

## 9. Charts and data graphics

Reference render: `charts/ocean-chart-system.png`. Style file: `ocean.mplstyle`. Codex also produces the same rules as a PptxGenJS chart helper and a web chart theme.

| Rule | Detail |
|---|---|
| Series color | Single series: **Sage for context, Cedar for the focus value**. On dark fields, Sprig |
| Categorical palette | Maximum four categories, in a fixed order. **On light fields:** Cedar, Sage, Citron, then Olive. **On dark fields:** Sprig, Sage, Citron, Honeydew |
| Numbers on data shapes (approved) | **Every number that sits on a bar, segment or chip is Honeydew, Bold**, on Cedar, Sage, Citron and Olive alike. Blackmoss is never used for data numbers because it reads too heavy on the mid-tones. Honeydew on Sage (3.6:1) and Citron (2.8:1) is below text contrast, so data numbers are always Bold, at least 10 pt on slides / 13 px on screen, and the same values also appear in a table or tooltip for accessibility |
| Crispness | Charts are built as vectors (SVG in decks and on the web, PDF in documents) and never pasted as screenshots. PNG exports are at least 300 dpi or 3×. There are no shadows or blurs, only flat fills. Bars have 6 px top radius and lines 2.6 px with round caps |
| Motion | On screen, charts animate in: bars grow from the baseline in a stagger of 35 ms per bar, lines draw left to right, and numbers count up and fade in only after their shape is 60% drawn. The ease-out is cubic and the total runs 1.2–1.8 s, once only (no loops). Reference: `ocean-chart-system-animated.mp4`. Printed and PDF charts show the final frame |
| Crimson | Only to flag one value (an alert, a risk, the headline number), and at most once per chart |
| Labels | Direct labels instead of legends wherever possible: numbers inside bars, and end-of-line values in rounded chips filled with the series color. Axis ticks in Cedar, Bold, 9–10 pt |
| Gridlines | Horizontal only, ink at 12% opacity, with no chart border and no top or right axis lines |
| Shapes | Forecasts use a 2-on / 3-off round dash. No 3D, pies (use a bar or a single ring), shadows or gradients. The graphic mark may sit top-right on a chart sheet or dashboard, in the ink |
| Titles | Chart titles state the finding ("Savings grow each year…"). The kicker names the chart |
| Data integrity | Every chart has a source line. Illustrative data carries the caption "ILLUSTRATIVE DATA · SAMPLE" |
| Formal documents | Charts are not allowed. Use a table |

---

## 10. Icons

Assets: `icons/svg/*.svg` (49 icons, vector outlines of the approved style) and `icons/ocean-icon-kit.png`.

- **One style only:** Material Symbols Outlined, weight 400, fill 0, grade 0, optical size 24, in the page ink. Never filled, rounded or sharp variants, and never multicolor icons or emoji.
- **Size:** icon = 50% of its cell or tile height (guide: 24 pt in a 48 pt cell). Minimum is 16 px on screen and 8 pt in print.
- **Groups** in the manifest: guide, energy, infrastructure and business. New icons must come from the same family and be added to the manifest.
- **Usage:** in navigation cells, tile headers, signage key figures and app navigation. Never inline in body text, and never in formal documents.
- **Licensing:** Material Symbols is Apache 2.0. Keep its license in `assets/fonts/`.

---

## 11. Graphics and micro-graphics

Assets: `assets/graphics/`. Every one of these comes from the guide.

| Graphic | Source in guide | Use | Never |
|---|---|---|---|
| Chamfer frame (top-left) | Guide panel and photo corners | Covers, photos, hero frames | More than one chamfer per object |
| Chamfer tile (bottom-right) | Guide data panels | Key figures, cards, signage tiles | In formal documents |
| Diamond counter (1–4) | Guide section markers | Numbering tiles in order, and as the single end-of-document mark in formal documents | As decoration or bullets |
| Double rule | Guide contents page end | Closing a list, table of contents or agenda | Mid-page dividers |
| Nav chip | Guide active tab | Active section in the staging header and app navigation | As a label or badge |
| Risk flag (Crimson triangle) | Decision D8 accent | One per risk item in reports and apps | On contracts or covers |
| Wave texture | Guide cover | Covers, closes, signage idle states, card fronts, app login | Behind body text beyond the D9 limit, and on report body or formal pages |
| Gradient map (two-color) | Guide imagery page | Mood and nature photos in the page's pairing | On evidence photos |

---

## 12. Digital signage

Reference renders: `sign_landscape` (lobby welcome, 1920×1080) and `sign_portrait` (live energy, 1080×1920).

| Element | Rule |
|---|---|
| Formats | 1920×1080 landscape and 1080×1920 portrait. Build at 1× and export 4K (3840×2160) for large panels |
| Safe area | 5% inset on every side (96 px landscape, 72 px portrait) for bezels and overscan |
| Minimum type | 26 px caps and 36 px text at 1080p for viewing from about 3 m. Scale up 1.5× for viewing from about 6 m |
| Fields | Blackmoss + Honeydew by default (screens glow, so dark fields reduce glare). Sage + Honeydew for welcome screens is allowed at large sizes |
| Photos | Full-bleed, with a left-to-right Blackmoss scrim of at least 90% behind text. Text never sits directly on a busy area |
| Live data | Key-figure tiles as in the micro-apps. Each tile shows its update time. Crimson only for a real alert. Illustrative data must be labeled |
| Motion | Loops of at least 8 seconds, cross-fades only, and the texture drifting slowly. No flashing (keep under 3 flashes per second) |
| Content | One message per screen, a maximum of three key figures, and a clock or date only on welcome screens |

---

## 13. Email signature

Assets: `email/ocean-email-signature.html` (production) and `email_signature.png` (preview).

- Table-based HTML, 600 px maximum width.
- **Font fallback:** email clients cannot load Stack Sans Headline, so Arial is the approved email fallback. It is the only permitted substitute font in the system.
- Layout: vertical logo (78 px wide, hosted PNG at 2×), a hairline divider, the name in bold, the title in caps with 2 px letter spacing, then the phone and website.
- No banners, quotes, social icons, animated images or colored backgrounds. A one-line legal notice is optional.

---

## 14. Social and digital graphics

Social and digital graphics follow the presentation rules at their own sizes: 1080×1080, 1080×1350, 1200×628 and 1920×1080. They use one pairing per post and one message, with the logo placed in a corner at 8% of the width. The Crimson moment follows the deck rule (one per campaign asset).

---

## 15. QA for every surface

1. Render to image. Inspect every page, slide, screen and card at 100% and at thumbnail size.
2. Tokens only: fail if any hex, weight or tracking value is not in `tokens/`.
3. Contrast: check every text/field pair against `contrast-matrix.json` using the D2 limits.
4. Weights: fail on SemiBold or ExtraLight anywhere.
5. Pairings: check against the approved list, the section rotation and the adjacent-section rule.
6. Crimson count per surface, as the profile allows.
7. Formal documents: fail on any color other than Blackmoss/White, any image, any icon or any tracked-caps heading.
8. Images: every image must have an entry in `image-manifest.json` with source and license, and evidence photos must be flagged as real.

---

## 16. Logo size and the graphic mark

The first renders set the logo too small. These minimums now apply everywhere; larger is always allowed.

| Surface | Lockup | Size |
|---|---|---|
| Guide (reference) | Horizontal in header | 20% of page width |
| Website header | Horizontal | 44 px tall (about 158 px wide) at 1440 px; 32 px on mobile |
| Micro-app navigation | Horizontal at top, graphic mark in footer | 40 px tall; mark 44 px |
| Deck staging header | Horizontal | 48 px tall at 1920 × 1080 (about 10% of slide width) |
| Deck cover and close | Vertical | 180 px tall at 1920 × 1080 |
| Report / proposal header | Horizontal | 16 pt tall in the header cell |
| Formal letter | Horizontal | 28 pt tall (1.4 in wide) |
| Legal page 1 / continuation | Horizontal / graphic mark | 24 pt tall / 24 pt |
| Business card front / back | Vertical / horizontal | 0.9 in tall / 16 pt tall |
| Email signature | Vertical | 78 px wide |
| Signage landscape / portrait | Horizontal | 88 px / 76 px tall at 1080p |
| Absolute minimum | Horizontal / mark | 0.5 in or 72 px wide / 0.25 in or 24 px |

**Graphic mark (the symbol without the wordmark).** Use it wherever the brand is already named on the surface, or where space is square. That covers:
- the app icon, favicon, social avatar and the micro-app navigation footer
- continuation pages of legal documents and reports, beside the page number
- the corner of photos on the website and in decks (Honeydew, 60 px, bottom-right inside the chamfered frame)
- chart sheets and dashboards (top-right, in the ink)
- signage idle states and the lower corner of portrait screens
- the key-number slide, and the envelope flap

Never use the mark as a bullet or pattern, repeat it more than once per page, or put it on the same page as a second full lockup at similar size.

## 17. Leadership decisions (approved 26 September 2026)

| # | Decision | Outcome |
|---|---|---|
| L1 | Rename the repo to `ocean-brand-system` | Approved. The old name redirects |
| L2 | Primary website theme | Approved: Honeydew + Blackmoss, which replaces the current White/Blackmoss site when it is rebuilt |
| L3 | Micro-app theme | Approved: Blackmoss + Honeydew default, **plus the Honeydew + Peacock alternative** with a user toggle |
| L4 | Card extras | Approved: registered emboss of the front logo, optional Sage edge color, and a personal QR code on the back |
| L5 | Formal document fonts | Approved: Stack Sans for letters and transactional documents; **Times New Roman for legal documents** |
| L6 | Unlicensed photos | Approved exclusion (infringement risk) |

## 18. Repository status (26 September 2026)

| Area | Status |
|---|---|
| Rules (`AGENTS.md`, `brand/*.md`) | In place and controlling |
| Tokens (`tokens/`) | In place. `brand/color-system.json` now carries the full palette for the existing code |
| Logos, icons, graphics, textures, chart style | In place under `assets/`, `charts/` and `tokens/build/` |
| Approved reference renders | `output/reference/` and `surfaces/*/` |
| `lib/ocean.js` (decks), `lib/publication.py` (reports, proposals), `lib/legal.py` (legal) | **Migrated 26 Sep 2026.** Tokens-driven; specimens regenerated in `output/pptx/` and `output/pdf/` |
| Prototype builders (`tools/prototypes/`) | HTML/Chromium scripts that produced the approved references. They use absolute sandbox paths and are kept as a record of exact coordinates, not as production code |
| Folder restructure in Section 2 | Optional. The current layout (`brand/`, `tokens/`, `assets/`, `charts/`, `surfaces/`, `lib/`) covers every role in Section 2, so existing commands keep working |
| Off-token checks | `scripts/qa.py` rejects off-palette text colors, non-approved fonts and logos under the §16 minimums; `lib/ocean.js` rejects unapproved pairings and a second Crimson moment |
