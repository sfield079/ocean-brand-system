# Reusable Ocean publication prompts

## Presentation

Follow AGENTS.md and brand/BRAND-SYSTEM.md. Create an editable presentation for
[audience] to support [decision], using the supplied verified sources. Use the
shared layout library, tokens, Stack Sans Headline, the deck recipe for the
chosen length (§8), one approved pairing per slide and original logos at §16
sizes. Match output/reference/examples/Ocean_Example_Presentation.pdf. Choose
the length the content needs. Build, validate, inspect every page, fix defects and deliver
PPTX plus a PDF with embedded fonts. Clearly identify missing facts.

## Customer proposal

Use the Ocean publication system to create a readable Letter PDF proposal for
[customer/project]. Use the verified scope, pricing and terms supplied here.
Include decision summary, scope, assumptions, exclusions, schedule dependencies
and next steps. Use lib/publication.py and preserve the editable JSON source.
Match output/reference/examples/Ocean_Example_Report.pdf and the report profile in brand/decisions.md.
Verify embedded fonts and inspect every page before delivery.

## Report

Create an Ocean report for [audience] using [sources]. Separate observations,
measurements, interpretation and recommendations. Identify source dates and
limitations. Use the Letter/A4 document layout, not slide typography. Keep
tables readable, repeat headers and preserve useful evidence. Deliver verified
PDF plus editable source after inspecting every page.

## System validation

Run npm test, npm run starter and npm run documents. Inspect every rendered page
and verify font embedding. These are design specimens, so draft placeholders
are permitted only in the layout reference. Report failures honestly. Do not
publish sample business claims or create a fictional project to fill a layout.

## Migrate the production libraries (next Codex task)

Follow AGENTS.md. The approved brand system (brand/BRAND-SYSTEM.md,
brand/decisions.md, brand/typography.md, tokens/) is now controlling, but
`lib/ocean.js` and `lib/publication.py` still produce the superseded white
editorial style. On a new branch `refine/ocean-brand-system-libraries`:

1. Read colors, weights, tracking, radius and chamfer from
   `tokens/ocean.tokens.json`, and remove hard-coded values.
2. Rebuild the deck layouts to match `output/reference/examples/
   Ocean_Example_Presentation.pdf` and the recipes in
   `surfaces/decks/deck_recipes.png`: Sage cover with texture, the framed
   staging header, pairing per slide, chamfer tiles, diamond counters, logo
   sizes per §16 and one Crimson moment.
3. Rebuild the report and proposal layouts to match
   `output/reference/examples/Ocean_Example_Report.pdf`.
4. Add a formal/legal document path matching `surfaces/formal/`. Legal
   documents use Times New Roman 11.5/16.5; letters use Stack Sans. Produce a
   .docx template with named styles.
5. Port the chart style (`tokens/build/ocean.mplstyle`, `charts/build_charts.py`)
   into native PPTX charts where possible: Sage for context, Cedar for the focus,
   and Honeydew Bold numbers on every data shape.
6. Extend `scripts/qa.py` and `scripts/qa_pdf.py`: fail on off-token hex values,
   on more than one field/ink pairing per slide (excluding photos, charts and
   the Crimson accent), on logos below the §16 minimums, and on any font other
   than Stack Sans (or Times New Roman in legal documents).
7. Regenerate `output/pptx/` and `output/pdf/` specimens. Render every page and
   compare it with `output/reference/`.
8. Open a pull request with before/after renders and a page-level changelog.
   Do not merge automatically.
