# Ocean RCS publication system

These rules apply to every presentation, proposal, report, company overview,
one-pager and appendix in this repository. Read `brand/DESIGN-SYSTEM.md` and
`brand/REFERENCE-NOTES.md` before authoring. Current user instructions override
older reference chats and generated advice.

## Identity and design

- Ocean RCS means Renewable Connected Systems. Use the full name once.
  Do not position Ocean as a hyperscale data-center developer.
- "Sequoia-level" means disciplined narrative, evidence and production quality,
  not copying another company's identity or claiming its endorsement.
- Default to white pages, Blackmoss text, sparse Sage accents, thin rules and
  open editorial columns. Keep covers light; Sage is an optional cover treatment.
- No AI backgrounds, generated decoration, watermark logos, grids behind text,
  gradients, glows, fake dashboards or repeated oversized cards.
- Use real supplied photography when useful. Preserve natural color. No image
  quota, no automatic hero image and no mandatory image on covers.
- Use original `assets/logos/` artwork. Preserve aspect ratio and clear space.
  Never recreate a logo with text, recolor it or place it over a busy background.

## Fonts and fit

- The exact approved family is **Stack Sans Headline**, from style-guide page 8.
  Use it for headings, body, tables, charts, numbers and footers.
- No silent Arial, Helvetica, Calibri or Inter substitution. Install bundled
  fonts with `python scripts/install_fonts.py` when absent. Cloud setup must
  run `bash scripts/setup.sh`. Fonts work offline once setup finishes.
- Slides: 48 pt cover, 32 pt headline, 16–18 pt body, 13–16 pt tables,
  9–10 pt footer. Statements and metrics can use larger type.
- Letter/A4 documents: 30 pt title, 18 pt section, 11 pt prose, 10 pt tables,
  9 pt footer. Do not force presentation typography onto long documents.
- Never shrink to fit or split words. Edit, widen a column or split the page.
- PDF fonts must be embedded and checked, not merely named in the source.

## Truth and editorial discipline

- Facts come from user-supplied evidence and `source/`. Reference proposals and
  the website establish design, not verified current commercial claims.
- Never invent projects, customers, contracts, utility rights, incentives,
  equipment ownership, revenue, returns, licenses or team credentials.
- Label illustrative and forecast figures; cite sources and assumptions.
- Keep internal margins and vendor sourcing costs out of external materials.
- Distinguish contracted revenue from optionality. No guaranteed returns,
  automatic incentives or guaranteed equipment collateral value.
- Prefer direct headings and concise prose. No inflated adjectives or forced
  three-part slogans. Preserve useful details in an appendix.

## Shared production paths

- 16:9 editable slides use `lib/ocean.js`. Extend shared layouts when needed;
  do not scatter custom coordinates through every deck. Start in `decks/_starter`.
- Proposals and reports use `lib/publication.py` and structured JSON, starting
  in `documents/_starter`. Keep the editable source alongside the PDF.
- Specimens demonstrate design only. They are not client-ready business claims.
- Draft mode may show placeholders. Release mode must fail on missing assets
  and unresolved placeholders. Never deliver a draft as final.

## Workflow and QA

1. Read sources and identify audience, decision and format.
2. Outline, then build. A complete-build or system-revision request authorizes
   proceeding without an extra outline approval. Ask only for blocking facts.
3. Use shared colors, fonts and layouts; keep evidence editable.
4. Run `npm run starter`, `npm run documents` and relevant `npm test` checks.
5. Run PPTX `scripts/qa.py` and PDF `scripts/qa_pdf.py`. Release checks fail on
   missing/unembedded fonts, text overflow, overlap and unresolved placeholders.
6. Inspect EVERY rendered page at readable size. Automated PASS is not visual QA.
7. Fix, rebuild, rerender and reinspect. Deliver PDF plus editable source, with
   an honest note about any unresolved limitations. Renders go in output/renders.

Keep rules, tokens, layout code, examples, fonts and checks synchronized. A
ChatGPT project does not automatically inherit a GitHub repo. Its bridge is
`brand/CHATGPT-PROJECT-INSTRUCTIONS.md`; keep project references current.
