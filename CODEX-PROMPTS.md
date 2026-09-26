# Reusable Ocean publication prompts

## Presentation

Follow AGENTS.md and brand/BRAND-SYSTEM.md. Create an editable presentation for
[audience] to support [decision], using the supplied verified sources. Use the
shared layout library, tokens, Stack Sans Headline, the deck recipe for the
chosen length (§8), one approved pairing per section and original logos at §16
sizes. Build it with lib/recipe.js or lib/ocean.js; never hand-build slides.
Set the notice: classification (confidential, proposal, investor, internal or
public) and status (draft until approved). Match
output/reference/examples/Ocean_Example_Presentation.pdf and check every item in
brand/DECK-CHECKLIST.md. Choose the length the content needs. Build, validate, inspect every page, fix defects and deliver
PPTX plus a PDF with embedded fonts. Clearly identify missing facts.

## Customer proposal

Use the Ocean publication system to create a readable Letter PDF proposal for
[customer/project]. Use the verified scope, pricing and terms supplied here.
Include decision summary, scope, assumptions, exclusions, schedule dependencies
and next steps. Copy documents/_starter/proposal.json, set classification
"proposal", the recipient, the pricing validity and status "draft" until Ocean
approves it (footer: "Confidential proposal · Draft · Do not use"). Mark any
section that is not cleared, such as unapproved pricing, with "status":
"do-not-use". Use lib/publication.py and preserve the editable JSON source.
Match output/reference/examples/Ocean_Example_Proposal.pdf and profile P2 in brand/decisions.md.
For a proposal deck, start from decks/proposals/_starter/.
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

## Extend the system

Follow AGENTS.md. The production libraries were migrated on 26 September 2026.
When adding a layout, surface or template: read tokens only, use an approved pairing,
match the relevant file in `output/reference/` or `surfaces/`, add a test in `tests/`,
regenerate the specimens, render every page, and open a pull request with
before/after renders. Do not merge brand-rule changes without Ocean leadership approval.

## Legal document

Use `lib/legal.py` and a JSON source like `documents/_starter/contract.json`, or the Word
template `templates/ocean-legal-template.docx`. Times New Roman throughout, plain
institutional layout, logo on page 1 and graphic mark on continuation pages. Run
`python3 scripts/qa_pdf.py <file> --legal`. Never draft legal terms; use counsel's text.
