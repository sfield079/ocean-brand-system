# Ocean RCS Deck Production System

## Purpose

This repository produces premium, investor-grade, client-ready, and lender-ready
presentation decks for Ocean RCS (Renewable Connected Systems).

Ocean RCS is an integrated energy-infrastructure platform. Its work may include
commercial solar, battery energy storage, electrical infrastructure, EV charging,
fleet and mobility hubs, water and connected infrastructure, and selective modular
compute deployment.

Do not position Ocean RCS as a hyperscale data-center developer.

## How This Repo Works (read first)

- `lib/ocean.js` is the component library. Every slide MUST be built by calling a
  layout function from this file (cover, divider, statement, twoColumn, pillars,
  metrics, timeline, table, chart, caseStudy, team, ask, appendix).
  Do not hand-place text boxes with ad-hoc coordinates in deck scripts.
- Each deck lives in its own folder: `decks/<category>/<deck-name>/build.js`.
  Copy `decks/_starter/build.js` as the starting point.
- Content comes from `source/` files. Facts and numbers may only come from
  `source/project-facts.md` and `source/approved-metrics.md` or files the user supplies.
- Build: `node decks/<category>/<deck-name>/build.js`
- QA: `bash scripts/render.sh output/pptx/<file>.pptx` then
  `python3 scripts/qa.py output/pptx/<file>.pptx`
- The library throws an error when text exceeds its box budget. When that happens,
  shorten or split the content. Never lower the font size to make it fit.

## Core Principle

Do not create generic AI slides.

Every deck must look like a high-quality institutional infrastructure presentation:
sharp, credible, restrained, visual, readable, and commercially practical.

Use native editable PowerPoint elements unless a slide is explicitly designated as
an image-native cinematic slide.

## Brand System

Use only these colors (defined in `brand/color-system.json`):

| Color | Hex | Approved use |
|---|---:|---|
| Blackmoss | #0B1617 | Primary dark backgrounds, body text on light slides, cover slides |
| Peacock | #102426 | Secondary dark backgrounds, structured visual blocks, table headers |
| Cedar | #1B4039 | Primary accent, diagrams, charts, dividers, callout borders |
| Sage | #618C7C | Secondary accent, muted chart series, supporting highlights |
| White | #FFFFFF | Light slide backgrounds and high-contrast dark-slide text |

Light-slide neutral tints derived from these colors (e.g., `#EEF2F0`, `#D5DED9`)
are allowed for table striping and card backgrounds only.

Do not use generic blue, neon green, bright red, orange, purple, gradients,
futuristic glows, random stock icons, or decorative AI patterns.

Use approved Ocean RCS logos from `assets/logos/` only. Do not recreate, distort,
recolor, stretch, or add effects to a logo.

## Typography

Font is set in `brand/color-system.json` (`fonts.heading`, `fonts.body`).
Target font: Stack Sans. Default fallback: Arial (renders identically everywhere).
Only switch to Stack Sans once it is installed on every machine that will open
the PPTX, or deliver PDF.

Minimum typography standards:

| Element | Minimum size |
|---|---:|
| Cover title | 38 pt |
| Section divider title | 32 pt |
| Standard slide headline | 26 pt |
| Supporting subhead | 18 pt |
| Body copy | 16 pt |
| Chart labels and tables | 13 pt |
| Legal footnotes | 10 pt |

Never shrink text simply to fit content.

If text does not fit:
1. Rewrite it more concisely.
2. Move detail to speaker notes or the appendix.
3. Split the content into multiple slides.

## Layout Standards

- 16:9 widescreen (13.333 x 7.5 in).
- 0.6 in safe margin on every edge; nothing except full-bleed images crosses it.
- 12-column grid defined in `lib/ocean.js`; align everything to it.
- One central message per slide.
- Maximum three supporting points on a standard content slide.
- 25–40 words on a typical slide. No dense paragraphs.
- Headlines: one to two lines, stating the takeaway.
- Never overlap objects unless intentionally designed and visually checked.

## Visual Direction

Preferred visuals:
- Ocean RCS site photographs
- Commercial solar, BESS, EV charging, mobility, electrical, and infrastructure photography
- Approved Higgsfield-generated visuals (`assets/higgsfield-images/`)
- Clean native diagrams, simplified maps, timelines, process flows
- Native editable financial charts and metric cards
- Equipment and site imagery when commercially relevant

Avoid:
- Generic futuristic cities, neon circuit patterns, fake dashboards
- Unrelated smiling stock-photo people
- Repetitive solar-panel imagery on every slide
- AI-generated text inside images
- Visuals implying projects, contracts, results, or capabilities that are not documented

Use Higgsfield visuals for covers, section dividers, opening problem/opportunity
slides, select full-bleed slides, and closing slides only. Never as a substitute
for charts, diagrams, tables, schedules, or commercial proof.

Target visual mix: ~35% imagery, ~30% diagrams/maps, ~20% charts/tables, ~15% text.

## Slide Narrative Rules

Each slide answers one question. Headlines state the takeaway, not the topic.

Weak: "Business Model"
Strong: "Multiple recurring-revenue paths compound at each qualified site"

Presentation-first, not document-first. Put equipment SKUs, technical specs,
underwriting assumptions, incentive research, legal detail, and diligence material
in the appendix. Plain-language equipment descriptions on main slides; detailed
SKUs in the appendix. Never show internal margins on customer or investor slides.

## Data and Claims Rules

Never invent: customers, project awards, contracts, incentives, utility approvals,
equipment ownership, utilization rates, revenue, returns, valuations, market share,
case-study outcomes, team credentials, partner relationships, or regulatory approvals.

When information is incomplete, use a visible placeholder in the form
`[TBD: description]` or label it Illustrative / Preliminary / Subject to diligence /
Targeted / Projected / To be validated.

Financial slides: native editable charts and tables, labeled assumptions, state
whether figures are historical, forecast, illustrative, or preliminary. Never imply
guaranteed returns.

## Mandatory Production QA

1. Build the editable PPTX into `output/pptx/`.
2. Run `bash scripts/render.sh <pptx>` (creates PDF in `output/pdf/` and PNGs in `output/renders/<deck>/`).
3. Run `python3 scripts/qa.py <pptx>` (checks font minimums, off-slide/margin
   violations, off-palette colors, overlaps, and `[TBD` placeholders).
4. Open and visually inspect EVERY rendered PNG for: clipped text, overflow,
   overlaps, bad line breaks, unreadable type, inconsistent spacing, misalignment,
   poor crops, low contrast, off-palette color, empty/unbalanced compositions,
   broken charts, tables, logos, or footnotes.
5. Fix every issue, rebuild, re-render, re-inspect.
6. Deliver final PPTX and PDF.

## Final Deliverables

- Editable `.pptx` and final `.pdf`
- Rendered slide previews in `output/renders/`
- Brief production note: slide count, audience and purpose, template used,
  image sources, open placeholders/assumptions, content moved to appendix

## Default Deck Lengths

| Deck type | Standard length |
|---|---:|
| Investor teaser | 10–13 slides |
| Full investor deck | 12–16 slides plus appendix |
| Commercial sales proposal | 8–14 slides |
| Customer feasibility presentation | 8–12 slides |
| Capabilities deck | 10–15 slides |

## Working Style

1. Review source files and approved assets.
2. Identify the audience and the decision the deck must support.
3. Propose a slide-by-slide outline (title, takeaway, max 3 points, layout type,
   visual) and list every missing fact or asset. Wait for approval.
4. Build with `lib/ocean.js` layouts only.
5. Run the mandatory QA loop.
6. Deliver PPTX, PDF, renders, and production note.

When requirements are ambiguous, ask focused questions before inventing facts.
