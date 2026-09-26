# Ocean RCS Brand Guide — Page-by-Page Forensic Analysis

Source: `Ocean_StyleGuide_2026.pdf` from `Ocean_StyleGuide_2026.zip` (byte-identical to the copy audited in turn 1), plus the logo masters in the same package (SVG, PDF, EPS).
Method: every page rendered at 144–150 dpi and inspected in quarter-page bands; every text string extracted with its position and point size; ink colors sampled from pixels (every UI color matched a palette hex exactly, with 0 deviation); rules, frames and grid lines measured from the rendered pixels to the nearest 0.5 pt.
Scope: analysis only. No repository or file changes were made.

Page numbering: "Guide nn" is the number printed in the page header; "PDF n" is the physical page. Cover = PDF 1, Contents = PDF 2 (Guide 00), Guide 01–08 = PDF 3–10, Back cover = PDF 11.

---

## Part A — The system underneath the pages

These are the rules the guide follows but never writes down. They are as binding as the written rules, because every page obeys them.

### A1. Format and grid

| Property | Measured value | Notes |
|---|---|---|
| Page | 1080 × 1920 pt (9:16 portrait) | A "small format" (the header says so), i.e. a screen or mobile-native manual, not a print letter page |
| Outer margin | 64 pt on all four sides | Header top edge sits exactly at y = 64. Content spans x 64 → 1016 (952 pt) |
| Column grid | 12 columns, 50 pt columns, 32 pt gutters (col n starts at 64 + (n−1)×82) | Col 5 = x 392, col 7 = x 556, col 11 ends at ~x 934–936 |
| Two-up grid | 64–524 and 556–1016 (460 pt columns, 32 pt gutter) | Measured on the imagery page; the palette cards, the lockup containers and the DO NOT columns sit on the same lines |
| Text column (standard pages) | Lede and body start at x 556 (col 7) and end at ~x 936 (col 11). Col 12 is left empty | The right-hand text block never reaches the right margin; the 80 pt of air is intentional |
| Text column (imagery pages 07–08) | Starts at x 392 (col 5), ends ~x 935 | Wider measure, because these pages carry more running copy and no containers |
| Title block | Kicker baseline y ≈ 271; title lines at y 296 and 335 (35 pt); full-width rule at y 393 (1 pt); body at y 415 | Same on every interior page |

### A2. The staging header (identical on Guide 01–08)

| Element | Measurement / content |
|---|---|
| Frame | x 64–1016, y 64–226, 2 pt stroke in the page accent color |
| Rows | Top row 64–178 (114 pt), bottom row 180–226 (46 pt), divided by a 2 pt rule |
| Vertical divider | x 678–680. The logo cell is 616 pt wide (≈ 64.7% of the frame) |
| Logo cell | Horizontal graphic + type lockup, left-aligned, in the accent color |
| Meta cell | "SMALL FORMAT" / "VISUAL IDENTITY MANUAL" in Light 300, tracked caps, 11 pt; "OCEAN RCS" in Bold, tracked caps. Three stacked lines at y 100 / 116 / 132 |
| Page cell | "PAGE" Light 300 above the number (e.g. "01") in Bold, 11 pt, tracked |
| Navigation | "LOGO SYSTEM — COLOR — TYPOGRAPHY — MEDIA", 11 pt Bold tracked caps, separated by em dashes. The active section is reversed out in a filled chip (accent fill, field-color type) |
| Icon strip | Seven square cells, exactly 48 pt each, from x 680 to 1016 (7 × 48 = 336). One icon per contents item: 01 layers, 02 grid, 03 crossed square, 04 palette, 05 paint bucket, 06 "TT", 07 image with bars. The cell of the current page is filled with the accent color and its icon is reversed |

Intent: the header works like an instrument panel. Where you are is shown three ways at once: the page number, the chapter chip and the filled icon cell. Pages do not float; each is placed within the system.

### A3. Type scale, weights and tracking

Superseded by the companion file "Ocean Brand Bible — Typography, Weight and Text-System Rules", which records all 27 text styles with their measured size, weight, case, tracking and line pitch. In short: weight falls as size rises (Light display, Medium headings, Regular reading text, Bold tracked-caps labels); every caps label is tracked +0.25 em; labels pair a light key with a bold value; the contents page is the only Bold display. Earlier weight guesses in this section (a Regular cover title, a Regular 25 pt subhead) were wrong: both are Light 300.

### A4. Color adjacency: the actual two-color rule

Every UI color on every page is an exact palette hex. Each interior page has one field color and one ink/accent color, and that pair is always one of the approved pairings (except the two specimen pages, which use White).

| Page | Field | Ink / accent (header, title, rules, body, logo) | Contrast | In approved list? |
|---|---|---|---|---|
| Cover | Blackmoss | Citron (logo, 2026, subtitle); Honeydew title; Cedar rule and chapter list | 6.35 (Citron) | Yes |
| 00 Contents | Honeydew | Blackmoss | 17.49 | Yes |
| 01 Lockups | Honeydew | Sage (UI, text); Cedar logo specimens | 3.60 | Yes |
| 02 Spacing | Citron | Cedar (text, header); Olive containers; Sprig diagram lines | 3.94 | Yes (all four touching pairs are approved) |
| 03 Usage | Blackmoss | Citron | 6.35 | Yes |
| 04 Palette | White | Olive | 4.98 | White is not a palette color. Specimen page only |
| 05 Pairings | White | Crimson | 4.11 | White is not a palette color. Specimen page only |
| 06 Typography | Sprig | Peacock (type); Citron oversized mark | 9.96 | Yes |
| 07 Imagery 1 | Honeydew | Peacock | 15.33 | Yes |
| 08 Imagery 2 | Blackmoss | Crimson | 4.48 | Yes (the pair mislabeled "Blackmoss + Citron" on Guide 05) |
| Back cover | Cedar / Olive / Blackmoss gradient | Citron frame and logo | — | Tonal family |

What this shows:
1. The rule is not "two colors on the page." It is **one field color plus one ink color, and every foreground/background pair that touches must be an approved pairing.** Extra colors are allowed only as tonal tiers (Cedar on the cover, Olive containers on Guide 02) and only where each adjacency is itself approved.
2. **The manual never repeats a pairing** across its nine interior pages. It is a live demonstration that the palette is meant to rotate from page to page, not to settle on one "safe" combination.
3. **Blackmoss is not the only ink.** Peacock carries all text on two pages, Cedar on one, Sage on one, Citron on one and Crimson on one.
4. **The guide sets 11 pt body text in its own "large-text" pairs**: Sage on Honeydew (3.60), Cedar on Citron (3.94), Crimson on White (4.11) and Crimson on Blackmoss (4.48). The designer accepts roughly 3.6:1 and above for small text. That is looser than WCAG AA (4.5:1). Whether Ocean's production documents should follow the guide or WCAG for body copy is a leadership decision (see Part D).
5. White appears only behind the two color-specimen pages, where colors must be judged against a neutral. It is never a general content canvas.

### A5. Geometry vocabulary

| Device | Where | Reading |
|---|---|---|
| Rounded rectangle with one 45° chamfer | Lockup containers (chamfer bottom-right), palette cards, pairing tiles, DO NOT tiles, photo masks and the back-cover frame (chamfer top-left) | Taken directly from the mark: its rounded frame plus its sharp intersecting X. The written rule (Guide 07): "The logo's rounded corners and sharp intersecting geometry can be extrapolated to shape image containers or guide layout structure" |
| Filled diamond (45° square) | Beside the container chamfers on Guides 01–02; bullet before each weight label on Guide 06 | **The diamonds count.** Container 1 has one diamond, container 2 has two, container 3 has three. On Guide 06 a single diamond marks each weight. They are index marks, not decoration |
| Tab label that breaks a border | Container titles on Guides 01–02 | Tracked caps in an outlined box that interrupts the top border line, centered. Square corners on Guide 01, rounded on Guide 02 (see errata) |
| Outlined label box | Weight labels, "LETTERFORMS", "NUMBERS & PUNCTUATION" (Guide 06) | Square-cornered 1 pt box; weight labels 11 pt Bold +0.25 em, glyph-set labels 12 pt Bold +0.125 em |
| Circle vs square | Guide 02 padding diagram: squares (Citron) at corners, circles (Sprig outline) on sides | Mirrors the mark: circle = rounded, square = sharp |
| Four-square crosshair | Center of each padding diagram (Guide 02) | Precision/registration symbol |
| Circled plus | Between color names on each pairing label (Guide 05) | "A + B" made into a glyph; echoes the crosshair |
| Circle-slash | Before each "DO NOT" chip (Guide 03) | Prohibition sign |
| Crimson warning triangle in a Honeydew circle | The "too close" DO NOT example | Crimson carries an alert meaning in the system |
| Three stacked 45° pills | Before "Small Format / Core Visual Identity Manual" on the cover (Citron) and contents page (Blackmoss) | A small signature glyph for the manual itself: stacked layers, like the layers icon of item 01 |
| Closing rule | Bottom of Cover, 00–06 | Varies deliberately: thin + thick double rule on 00; thick single rule on 01 and 06; Sprig rule on 02. Imagery pages 07–08 have no closing rule; the image grid runs to the bottom margin instead |

### A6. Copy voice

The guide's words are part of the design. Four voices appear:

1. **Specification voice** (body copy): plain, instructive, second-person implied. "must be entirely surrounded by a clear space", "must never be physically altered".
2. **Brand-statement voice** (ledes): one confident sentence in tracked caps. "The ocean color system is designed for flexibility, contrast, and clarity." "Our visuals should reflect the energy we work with."
3. **Specimen voice** (Guide 06): six sentences that are, in fact, the brand's copy exemplars. Each one pairs something natural with something built: "Bright beams cut clean lines across quiet rooftops" (sun + rooftop), "Gold panels rise with quiet strength each morning" (solar + calm), "Steel and sunlight shape tomorrow's world today" (steel + sun), "Workers build beneath a blazing yellow sky" (people + sun), "The power of structure meets the warm sun" (structure + sun), "Lines are clean, angles are sharp, energy flows" (the design philosophy itself). The word "quiet" appears twice. The voice is physical, calm and concrete. It never uses hype, superlatives or abstract tech language. The weights also match the meaning: the lightest weight carries "bright beams… quiet rooftops"; the heaviest carries "angles are sharp, energy flows".
4. **Nature-grounding voice** (Guide 04): "warm, earthy green and brown tones that feel rooted to the strength and beauty of the natural world."

The key words the guide keeps repeating: clean, precision, clarity, structure, natural, warm, energy, purpose, directional. These are the words a deck or proposal should earn visually and use verbally.

### A7. Image vocabulary

- **Primary (real):** ocean wave barrel (the name), residential rooftop solar on terracotta tile against blue sky with contrails, aerial misty forest river, electrical field worker in white hard hat and hi-vis vest holding cabling and a tablet, fog over conifers, overhead shot of two installers laying panels on a dark standing-seam metal roof.
- The six photos alternate nature and industry diagonally across the two columns, so no two adjacent tiles have the same subject type. This is the written rule ("nature… on top of industry-relevant imagery") expressed as layout.
- **Color names are grounded in photos:** on Guide 04 each color card carries a nature photo in that color (Blackmoss = aerial ocean rapids, Peacock = misty forested hills, Cedar = forest canopy, Sage = alpine lake with conifers, Honeydew = sky and sea, Sprig = clear shallow water over sand, Olive = olive grove from above, Citron = sun rays through a forest, Crimson = red earth). Every color is a place, not a hex.
- **Secondary (abstract, Guide 08):** city at night with cyan network arcs over a highway (warm Olive-toned sky), a Sage gradient-mapped marble/smoke texture, a neon data-light skyline and a low-contrast Citron particle wave. The cover's particle wave and the back cover's beam of light through a Cedar/Blackmoss field are the same family. The back-cover light shaft reads as an abstracted version of the Citron "sun rays in forest" photo.

---

## Part B — Page by page

### Cover (PDF 1)

Field: Blackmoss. Upper ~62%: abstract particle wave in Peacock/Cedar, with Citron connected-node lines (a "connected systems / energy flow" motif), fading into the field.

| Element | Detail | Intent |
|---|---|---|
| Vertical lockup | Citron, at the left margin, above the title | Vertical lockup is the "full display" format |
| "2026" | 30 pt, Citron, right-aligned to x 1016, y 1235 | The edition year as a design element |
| Chapter list | "Logo System / Color / Typography / Media", 14 pt, right-aligned to 1016, stacked | Previews the four chapters of the navigation; the case varies in the text layer but renders consistently |
| Title | "Brand / Guidelines", 191 pt Light 300, Honeydew, from x 64 | Honeydew, not white: even the brightest type on the cover is a palette color |
| Rule and subtitle | Cedar rule; three stacked 45° pills + "Small Format / Core Visual Identity Manual" and "Ocean RCS", 30 pt | Cedar is a quiet tonal tier against Blackmoss |
| Possible defect | A faint horizontal seam in the background image near y ≈ 1189 on the right | Verify in the source file |

### Contents — Guide 00 (PDF 2)

Field: Honeydew. Ink: Blackmoss only — the strictest two-color page in the guide.

- Header present, but no icon cell is filled and no chapter chip is active: this page sits above the chapters.
- "Table of / Contents", 191 pt Bold, tight.
- Seven rows at a 121 pt pitch between 1 pt full-width rules (y 1000, 1121, 1242, 1363, 1484, 1605, 1726, 1847). Each row: 90 pt numeral at x 64; 12 pt tracked kicker at x 392; 35 pt title at x 392.
- Entries: 01 LOGO SYSTEM Brandmark Lockup Variations; 02 LOGO SYSTEM Spacing & Padding; 03 LOGO SYSTEM General Usage Guidelines; 04 **LOGO SYSTEM** Core Brand Palette; 05 COLOR Palette Harmony & Usage; 06 TYPOGRAPHY Brand Typeface; 07 MEDIA Brand Imagery & Styling.
- Erratum: entry 04's kicker says "LOGO SYSTEM", but Guide 04's own header marks COLOR, and its page kicker says "COLOR". It should read "COLOR".
- Closing: thin rule plus a heavier rule (double rule), Blackmoss.
- Three stacked pills glyph in Blackmoss (the cover's glyph, in the page's ink).

### Guide 01 — Brandmark Lockup Variations (PDF 3)

Field: Honeydew. Ink: Sage. Logo specimens: Cedar.

- Kicker "LOGO SYSTEM"; title "Brandmark / Lockup Variations".
- Lede (2 lines, bottom-aligned): "The ocean logo can be displayed in three possible formats, as shown below."
- Body: graphic/text versions are used "in all cases where the full logo must be displayed, or there is ample staging space"; graphic-only is "better suited for smaller scale applications where staging space is limited" and "can also be used as a branded decorative graphical element."
- Three containers: one full-width (vertical lockup) and two half-width (horizontal; graphic-only). Sage hairline rounded rectangles, chamfered bottom-right, with 1 / 2 / 3 diamonds beside the chamfer.
- Tab labels: "VERTICAL GRAPHIC & TYPE LOCKUP", "HORIZONTAL GRAPHIC + TYPE LOCKUP", "GRAPHIC-ONLY LOCKUP" — Cedar tracked caps in a square Sage outline box breaking the top border.
- Closing: thick Cedar rule.
- Copy errata: "the  graphic/text" (double space); "element ." (space before the period). Tabs use "&" for vertical but "+" for horizontal; the text layer also has a double space in "graphic + type  Lockup".

### Guide 02 — Spacing & Padding (PDF 4)

Field: Citron. Ink: Cedar. Containers: Olive. Diagram lines: Sprig. Every touching pair (Citron/Cedar, Citron/Olive, Olive/Sprig, Olive/Cedar) is on the approved list.

- Lede (4 lines): "The ocean logo must be entirely surrounded by a clear space to ensure visibility against backing elements or in proximity to other graphics or text."
- Body: "To properly stage the logo in any of it's lockup formats, a minimum clearance… must be maintained as shown in the following diagrams:" — erratum "it's" → "its".
- Same three-container layout as Guide 01, with the same 1 / 2 / 3 diamonds. Tabs here have rounded corners (square on 01) — an inconsistency between sister pages.
- Diagram: Citron squares at corners, Sprig outline circles on the sides, dashed Sprig bounds, and a Sprig four-square crosshair at the center.
- Legend: circle icon + "PADDING" (small, Sprig) + value in Cedar Bold tracked. Values: vertical "0.5x full asset height", horizontal "1x full asset height", graphic-only "0.5x full asset height". The measured clearances in the diagrams match these ratios.
- Inconsistency: "1x full asset height" is 11 pt while both "0.5x" labels are 14 pt.
- Alignment: every text anchor on this page starts at x 65 / 557 instead of 64 / 556 — a 1 pt shift not seen on any other page.
- Closing: Sprig rule.

### Guide 03 — General Usage & Guidelines (PDF 5)

Field: Blackmoss. Ink: Citron.

- Lede (5 lines): "In order to ensure a consistent and recognizable brand identity, all formats of the ocean logo must never be physically altered or made to look different by means of color changes, image fill, skewing, etc."
- Body: rules "apply to all versions of the Ocean logo and are not limited to the specific lockups used in the individual examples below."
- Nine DO NOT tiles in a 3 × 3 grid. Each has a Citron circle-slash + "DO NOT" chip (Citron fill, Blackmoss Bold tracked type), a 14 pt Citron sentence-case caption without end punctuation, and Citron hairlines above and below each column. Tiles are chamfered top-left.
- Row 1: rotate the logo relative to surrounding elements; change the lockup orientation (a rearranged vertical lockup on Sage); distort or skew (a stretched graphic on Citron).
- Row 2: place too close to other elements (Crimson warning triangles in Honeydew circles; "see previous page for spacing/padding guidelines"); place on backgrounds that obscure legibility or clash with the palette (off-brand fields such as #2A1933 purple, a blue/magenta abstract); change to unapproved, non-brand colors (#DFD80B yellow, #FF4C16 orange).
- Row 3: change the typeface or recreate/manipulate the wordmark or graphic; mix and match undesignated brand colors within the logo (a Citron graphic with a Blackmoss wordmark on Crimson); use low-quality or low-resolution versions (a blurred logo on Honeydew).
- Every tile field that is not a deliberate violation is an approved brand color, so even the "wrong" examples are staged on the brand's own palette.
- Interpretation of the lede: the guide itself shows the logo in Citron, Sage, Cedar, Olive, Crimson and Peacock. So "color changes" means non-brand colors and mixed colors within one logo, not a single brand color. The logo masters in the zip support this: the PDF and EPS masters are pure black and the SVGs white, i.e. one-color masters built to be recolored. (EPS metadata: prepared for Michael Gartsman, created 23 April 2026 in Adobe Illustrator 30.3; file title "Ocean_LOGO_P1_NOTES".)

### Guide 04 — Core Brand Palette (PDF 6)

Field: White. Ink: Olive.

- Lede: "The ocean brand color palette conveys a spectrum of warm, earthy green and brown tones that feel rooted to the strength and beauty of the natural world." (Text layer has a double space after "brown".)
- Nine cards (3 × 3), top-left chamfer. Each card: field in the color, graphic-only logo + 35 pt name + "HEX" / "RGB" labels (11 pt tracked) + values (14 pt Bold tracked), all in a partner color; three hairline rules that extend over a photo strip on the right under a translucent color overlay.
- Values exactly as printed (no "#"; RGB with slashes): Blackmoss 0B1617 11/22/23 · Peacock 102426 16/36/38 · Cedar 1B4039 27/64/57 · Sage 618C7C 97/140/124 · Honeydew F3FBF8 243/251/248 · Sprig D5CCA0 213/204/160 · Olive 6E734C 110/115/76 · Citron A69856 166/152/86 · Crimson EB3819 235/56/25.
- Card partners: Blackmoss/Citron, Peacock/Sage, Cedar/Sprig, Sage/Blackmoss, Honeydew/Crimson, Sprig/Olive, Olive/Honeydew, Citron/Cedar, Crimson/Sprig.
- Order is intentional: row 1 darks (Blackmoss → Peacock → Cedar), row 2 lights and mid (Sage → Honeydew → Sprig), row 3 warm accents (Olive → Citron → Crimson). Crimson is last, the only hot color.
- Photo strip = each color's place in nature (see A7).

### Guide 05 — Palette Harmony & Usage (PDF 7)

Field: White. Ink: Crimson (UI). Tile labels: Blackmoss.

- Lede: "The ocean color system is designed for flexibility, contrast, and clarity."
- 25 pt subhead, left: "Approved General-Use / 2-Color Pairings".
- Body: "**Not all brand colors play nicely together.** Avoid pairings that clash in temperature or lack sufficient contrast. Please refer to this document or existing designed materials for viable examples of usable brand color pairings." The first sentence is the only bold sentence in any body copy in the guide.
- 31 tiles in 8 rows of 4 (last row 3). Each is two overlapping chamfered tiles; each carries the logo in the other's color, so every pair is shown both ways (reciprocal). Tonal pairs (e.g. Blackmoss + Peacock) show deliberately low-contrast logos: tonal pairs are for atmosphere, not legibility.
- Labels: Blackmoss 11 pt tracked caps with a circled-plus glyph between the names.
- Errata: row 2's fourth tile is labeled "BLACKMOSS + CITRON" (a duplicate of the third) but shows Blackmoss + Crimson. Guide 08 uses exactly this pairing for a whole page, which confirms it is approved. "SPRIG + CITRON" appears twice (row 7 and row 8). Net: 30 unique approved pairs.
- The six pairs not approved: Cedar + Crimson, Sage + Olive, Sage + Citron, Sage + Crimson, Olive + Crimson, Citron + Crimson. All involve either temperature clashes with Crimson or muddy mid-tones — exactly the two reasons the body copy gives.
- Note "Please refer to… existing designed materials": the guide names its own layouts as a reference. The page designs are part of the specification.

### Guide 06 — Brand Typeface (PDF 8)

Field: Sprig. Ink: Peacock (measured exactly; not Blackmoss). Decorative mark: oversized graphic-only logo in Citron, running off the right and bottom edges behind the type. Rules and text sit above it.

- Kicker "TYPOGRAPHY" moved down to y 310 because the title is one line: "Brand Typeface".
- Lede: "Our primary typeface, Stack Sans Headline, is a clean and modern geometric sans-serif that reflects the clarity and precision at the core of our work." "Primary" implies a secondary face could exist, but none is named.
- Body: "Stack Sans is a sans serif font family rooted in modernist inspiration, striking a balance between timelessness and innovation. Its distinctive notched detailing, inspired by the building process, creates a recognizable signature that is unique to Stack Sans." (Justified.)
- Specimen "Stack Sans / Headline", 142 pt; "Google Fonts" 30 pt on the baseline of "Headline".
- "LATIN - 6 WEIGHTS (STANDARD), VARIABLE INTEGRATION"; then the six weights in three columns (·EXTRA LIGHT 200 ·LIGHT 300 / ·REGULAR 400 ·MEDIUM 500 / ·SEMIBOLD 600 ·BOLD 700) between rules.
- Six specimen sentences, 40 pt, each labeled by a diamond + outlined weight box (see A6 for their meaning).
- "LETTERFORMS" (A–Z, a–z, 40 pt) and "NUMBERS & PUNCTUATION" (0–9, !@#$?/|\^&*()_-+={}[]<>,.) in outlined boxes. The ampersand is the distinctive Stack Sans form; the titles that use "&" (Spacing & Padding, General Usage & Guidelines, Palette Harmony & Usage, Brand Imagery & Styling) show it off at 35 pt.
- Closing: thick Peacock rule.

### Guide 07 — Brand Imagery & Styling pt.1 (PDF 9)

Field: Honeydew. Ink: Peacock.

- Lede (at x 392): "Our visuals should reflect the energy we work with. clean, directional, and full of purpose." The lede renders in caps, so this reads as a deliberate fragment, not an error.
- Body, first paragraph: "Focus on real environments and real people in action, lit by natural sun or warm industrial tones. Imagery of mountains, bodies of water, and general nature settings can also be used on top of industry-relevant imagery to represent the connection between the natural world and the renewable energy and conservation aspects of the Ocean brand and services. The logo's rounded corners and sharp intersecting geometry can be extrapolated to shape image containers or guide layout structure. This geometry adds subtle cohesion and reinforces the brand without drawing too much attention to itself."
- Second paragraph: "Use designated harmonies of brand colors to overlay or gradient map imagery alongside unaltered photography to establish contrast and brand character. Avoid generic staged scenes or overly polished edits and let the layout and UI staging elements compliment clean and natural photography." Erratum: "compliment" → "complement".
- Six photos in two 460 pt columns, all chamfered top-left and rounded elsewhere (see A7 for content and the nature/industry alternation). The right column's fog-forest photo is double height.
- Alignment defect: the misty-river photo (left column, second) sits at x 68–528 instead of 64–524, a 4 pt shift right of the grid. Every other image is exactly on the column lines.
- The fog photo's sky has a faint lavender cast, which is outside the palette. It is an unaltered photo, which the guide allows.
- No closing rule.

### Guide 08 — Brand Imagery & Styling pt. 2 (PDF 10)

Field: Blackmoss. Ink: Crimson.

- Same lede as Guide 07. Title "Brand Imagery / & Styling pt. 2" — "pt.1" vs "pt. 2" spacing is inconsistent.
- Body: "In addition to showcasing real images of nature, industry, workers or clients pertaining to the various services performed by Ocean, abstract renders or edited photography representing brand goals and ideological motifs can be used in the Ocean brand as textural background elements and secondary visuals. These elements should have a modern-futurist stylization and are best utilized in lower-contrast, as to not pull too much attention away from brand messaging, information, UI elements or relevant photography." Note "clients" — client photos are explicitly allowed. "as to not" should read "so as not to".
- Four images: full-width night city with cyan network arcs over a highway (Olive-warm sky, chamfered); half-width Sage gradient-mapped marble/smoke texture (a direct example of "gradient map… designated harmonies"); half-width neon data-light skyline; full-width Citron particle wave at very low contrast with soft, faded edges.
- Tension: the neon skyline is high-saturation magenta, green and orange, which contradicts both the palette and the "lower-contrast" instruction in the same page's copy. Treat it as the edge of what is allowed, not a model.
- No closing rule.

### Back cover (PDF 11)

- Full-bleed abstract: a diagonal beam of Olive/Citron light through a Cedar-to-Blackmoss field. The image is placed far larger than the page (3413 pt wide, offset −1154 pt), so only a crop of the light is shown.
- Citron hairline frame inset exactly at the 64 pt margins, rounded corners with a single top-left chamfer: the brand container at page scale.
- Citron vertical lockup centered horizontally.
- No text. The page closes on mark, frame and light only.

---

## Part C — Errata and inconsistencies in the guide

| # | Location | Issue | Suggested fix |
|---|---|---|---|
| 1 | Contents, entry 04 | Kicker "LOGO SYSTEM" | "COLOR" |
| 2 | Guide 05, row 2 tile 4 | Labeled "Blackmoss + Citron"; shows Blackmoss + Crimson | Relabel "Blackmoss + Crimson" |
| 3 | Guide 05 | "Sprig + Citron" appears twice | Remove one; the matrix is 30 unique pairs |
| 4 | Guide 01 | "the  graphic/text" (double space); "element ." | Single space; "element." |
| 5 | Guide 01–02 | Tabs: "Graphic & Type" vs "graphic + type"; double space before "Lockup" | Pick one connector |
| 6 | Guide 01 vs 02 | Tab corners square on 01, rounded on 02 | Pick one |
| 7 | Guide 02 | "it's lockup formats" | "its" |
| 8 | Guide 02 | "1x full asset height" at 11 pt vs "0.5x" at 14 pt | Same size |
| 9 | Guide 02 | All text anchors 1 pt right of the grid (65/557) | 64/556 |
| 10 | Guide 04 | Double space after "brown" | Single space |
| 11 | — | Withdrawn. "The ocean logo" appears only in ledes, which render in ALL CAPS | — |
| 12 | — | Withdrawn. The lede renders in caps; "CLEAN, DIRECTIONAL, AND FULL OF PURPOSE." is a deliberate fragment | — |
| 13 | Guide 07 | "compliment" | "complement" |
| 14 | Guides 07–08 | "pt.1" vs "pt. 2" | Match |
| 15 | Guide 08 | "as to not pull" | "so as not to pull" |
| 16 | Guide 07 | Misty-river photo 4 pt off the column | Snap to x 64 |
| 17 | Guide 08 | Neon skyline contradicts "lower-contrast" and the palette | Replace, or gradient-map it into a brand harmony |
| 18 | Guide 06 | "Primary typeface" with no secondary defined | State "sole typeface" or name the secondary |
| 19 | Cover | Possible faint seam in the background image near y ≈ 1189 | Verify in the source file |

None of these changes the rules. They matter because Codex will copy literal strings and could turn errata into rules (for example, treating "Blackmoss + Citron" twice as a signal, or "LOGO SYSTEM" as the palette's chapter).

---

## Part D — Corrections to the turn-1 audit

| Turn-1 statement | Correction from this pass |
|---|---|
| Guide 02 ink is "Peacock/Cedar"; logo "Peacock on Citron" | The ink is Cedar (exact #1B4039) |
| Guide 06 type is Blackmoss; logo "Blackmoss on Sprig" | Peacock (exact #102426). The oversized mark is Citron |
| Guide 07 accent is Blackmoss; light pages are "Honeydew plus Blackmoss on 00 and 07" | Guide 07 is Honeydew + Peacock. Only 00 is Honeydew + Blackmoss |
| The repo's black PNG logo "violates the guide" | The official masters in the zip are one-color black (PDF/EPS) and white (SVG) files, meant to be recolored. The defect is that the repo never applies a brand color, not that it started from black |
| "All header lines are hairlines" | The header frame and its row divider are 2 pt; the title rule is 1 pt; closing rules are heavier. Only containers and tile rules are hairlines |
| "Logo cell about 60% width" | 616 pt of 952 (64.7%); the icon strip is exactly 7 × 48 pt |
| "Title left ~45%, text right ~50%" | Text column starts on column 7 of a 12-column grid (x 556) and ends at column 11 (~x 936); imagery pages start on column 5 (x 392) |
| "Container tabs are thin-outline pills" | Square outlined boxes on Guide 01, rounded on 02 |
| "Diamonds: one or two per container" | They count the containers: 1, 2, 3 |
| "Heavier closing rule on every page" | Not on the imagery pages 07–08 |
| Contrast classes: pairs under 4.5 labeled "Large text only" | Correct against WCAG, but the guide itself sets 11 pt body copy in pairs from 3.6:1 upward. That is a leadership choice (below) |
| "Strict one dominant field plus one accent" | Refined: one field plus one ink, with optional tonal tiers, provided every touching pair is approved (Cover, Guide 02) |

---

## Part E — What this means for the repository rules

These add to or refine the turn-1 Section 4 rules. Nothing below has been implemented.

1. **Pairing rule (replace).** "Each page or slide has one field color and one ink color, chosen from the 30 approved pairings. A third or fourth brand color may appear only as a tonal tier, and only if every foreground/background pair that touches is itself approved. White is allowed only for color-specimen or print-proof pages."
2. **Rotation rule (new).** "Across a document, rotate pairings by section, the way the guide never repeats a pairing on its nine interior pages. Do not build a whole deck on one pairing."
3. **Ink rule (new).** "Any approved partner can be the ink: Blackmoss, Peacock, Cedar, Sage, Citron or Crimson. Do not hard-code Blackmoss as the only text color."
4. **Grid tokens (new).** For a 9:16 page: 64 pt margins; 12 columns (50/32); text column at column 7; header 2 pt frame, 616 pt logo cell, 7 × 48 pt icon cells. For 16:9 slides and Letter pages, scale the same proportions (margin ≈ 5.9% of the short side; text column starting at 7/12 of the width).
5. **Staging header (new component).** Logo cell + meta cell + page number + chapter navigation with an inverted active chip + an icon strip with the active cell filled.
6. **Title block (new component).** Tracked Bold kicker, two-line 35 pt-scale Medium title, tracked Bold caps lede bottom-aligned to the title, full-width 1 pt rule, justified Regular body.
7. **Type scale (replace).** Use only the guide's steps (ratioed to the canvas): display, specimen, numeral, 40, 35, 30, 25, 14, 12, 11 equivalents. No intermediate sizes, no italics, uppercase only as tracked labels (+0.25 em). Weights per the typography file.
8. **Markers (new).** Diamonds count items (1, 2, 3…); chamfers go top-left on cards and images, bottom-right on logo containers; the circled plus joins pairs; Crimson triangles are reserved for warnings.
9. **Copy voice (new).** Headlines and callouts should pair a natural element with a built one, in calm, concrete language ("quiet strength", "clean lines"), and avoid hype and superlatives. The six specimen sentences are the tone reference.
10. **Imagery (refine).** Alternate nature and industry across adjacent images; real Ocean crews and client sites first; abstract images only low-contrast and gradient-mapped to a brand harmony; do not copy the neon skyline treatment.
11. **Logo files (refine).** Use the official one-color masters and recolor them to the page ink. Never use the black or white master as-is on a brand field.
12. **String hygiene (new QA).** A text-lint check for the errata patterns above (double spaces, "it's" as a possessive, "compliment", space before a period).

### Leadership decisions needed

1. **Body-text contrast.** Follow the guide (allow 11 pt body in pairs from about 3.6:1, like Sage on Honeydew), or require WCAG AA 4.5:1 for body copy in customer documents and use the guide's lower-contrast pairs only for large type. I recommend the second for proposals, reports and lender or investor materials, and the guide's practice for brand pieces.
2. **Deck and document type sizes.** Approve the scaled type ladder in the typography file (Rule 9).
3. **Whether to send the errata list to the guide's designer** (the EPS metadata names Michael Gartsman) so a corrected v2026.1 becomes the controlling file before Codex encodes it.
4. **White canvas for print.** The guide confines White to specimen pages. Decide whether printed proposals may use White for paper economy or must use Honeydew.
