# Ocean RCS brand system

This repository is the single brand source of truth for every Ocean surface:
oceanrcs.com, Ocean micro-apps, decks, reports, proposals, formal and legal
documents, business cards, email, digital signage, charts, icons and graphics.

## Controlling documents (read in this order)

1. `brand/Ocean_StyleGuide_2026.pdf`: the Brand Bible. Every word, letter
   and design element in it is intentional. It overrides everything else here.
2. `brand/decisions.md`: approved decision register (D1–D21) and document
   profiles. Approved by Ocean leadership on 26 September 2026.
3. `brand/typography.md`: the typography rules (T1–T27, Rules 1–10).
4. `brand/BRAND-SYSTEM.md`: surface-by-surface specification (web, apps,
   decks, reports, formal, print, email, signage, charts, icons, graphics,
   logo sizing, decisions L1–L6) and the repository migration status.
5. `brand/audit/`: the independent audit and page-by-page guide analysis
   (evidence, not rules).

If older text in this repo (for example `brand/REFERENCE-NOTES.md`) conflicts with
the documents above, the documents above win. Approved references for how
things must look are in `output/reference/` and `surfaces/*/`.

## Identity

- Ocean RCS means Renewable Connected Systems. Use the full name once.
  Do not position Ocean as a hyperscale data-center developer.
- "Sequoia-level" means disciplined narrative, evidence and production quality,
  not copying another company's identity or claiming its endorsement.

## Color

- Palette: Blackmoss #0B1617, Peacock #102426, Cedar #1B4039, Sage #618C7C,
  Olive #6E734C, Citron #A69856, Crimson #EB3819, Sprig #D5CCA0,
  Honeydew #F3FBF8. White #FFFFFF is for print and formal documents only.
- Tokens come from `tokens/ocean.tokens.json` (CSS and Tailwind builds in
  `tokens/build/`). Never hard-code a hex value outside tokens.
- Each page, slide or screen section uses **one approved two-color pairing**
  (field + ink) from `brand/decisions.md` Part 2. Photography, charts and a
  single Crimson accent are the permitted exceptions.
- Contrast decides use (`tokens/contrast-matrix.json`): body text needs 4.5:1;
  Sage/Honeydew (3.6:1) carries large text and graphics only.
- Crimson appears once per deck as a moment, and otherwise only to flag one
  value or an alert.

## Typography

- **Stack Sans Headline** for all brand surfaces. Four working weights:
  Light 300, Regular 400, Medium 500, Bold 700. All caps are always Bold or
  Light at +0.25 em. Display tracking follows `brand/typography.md`.
- **Legal documents** (contracts, EPC agreements, NDAs, MSAs, term sheets,
  resolutions, lien waivers, signature pages) use **Times New Roman**
  throughout (approved L5). Letters, memos, invoices, quotes and change orders
  stay in Stack Sans.
- Email signatures fall back to Arial because email clients cannot load
  Stack Sans. No other substitution is permitted.
- Never shrink to fit or split words. Edit, widen a column or split the page.
  PDF fonts must be embedded and checked.

## Logo and graphic mark

- Use the official artwork in `assets/logos/` (masters) and
  `assets/logos/variants/` (one-color versions in each palette color).
  Preserve aspect ratio and clear space; never rebuild the logo from text.
- Minimum sizes are fixed per surface in `brand/BRAND-SYSTEM.md` §16. They
  are minimums, and larger is allowed. Examples: web header 44 px, letter
  28 pt, legal page 1 24 pt, card front 0.9 in, email 78 px.
- The graphic mark alone is used for app icons, favicons, continuation pages,
  photo corners, chart sheets and signage corners. Use it at most once per page
  and never as a pattern or bullet.

## Surfaces

- **Presentations and reports are different systems.** Decks follow the
  recipes in §8 (5 to 30 slides, same spine). Reports and proposals follow the
  report profile in `brand/decisions.md`.
- **Formal documents** follow the plain institutional standard (§6): white,
  Blackmoss only, logo on page 1 and graphic mark on continuation pages, and no
  textures, photos, chamfers, icons or color.
- **Web and micro-apps** follow §4. oceanrcs.com uses Honeydew + Blackmoss
  (L2). Apps default to Blackmoss + Honeydew, with the approved Honeydew +
  Peacock alternative and a user toggle (L3).
- **Business cards, email and signage** follow §7, §12 and §13. The card
  back carries a personal QR code linking to oceanrcs.com, and the front logo
  may be embossed (L4).

## Charts, icons and graphics

- Charts follow §9 and `tokens/build/ocean.mplstyle`. Use Sage for context and
  Cedar for the focus. **Every number on a data shape is Honeydew Bold.** Output
  is vector (SVG/PDF). On screen, charts animate in with a staggered ease-out.
  Reference: `charts/ocean-chart-system.*`.
- Icons: Material Symbols Outlined, wght 400, fill 0, grade 0, opsz 24, with
  the icon at 50% of its cell. Use only the names in `assets/icons/manifest.json`.
- Micro-graphics (chamfer frames, diamond counters, double rule, risk flag,
  nav chip) are in `assets/graphics/`. Wave textures are in `assets/textures/`
  and are used only as subtle, low-contrast texture.

## Images

- Any source is allowed in any order: Ocean photos, licensed stock, or top-rated
  generators (Higgsfield and others). **Unlicensed photos are excluded (L6).**
- Record every image in `assets/images/image-manifest.json` (source, license,
  AI flag). Label AI-generated images "Representative" in client material.
- Images show real environments, people, infrastructure and natural light,
  in natural color. Overlays stay restrained, per the guide.

## Truth and editorial discipline

- Facts come from user-supplied evidence and `source/`. Specimens and
  references demonstrate design only and are not client-ready business claims.
- Never invent projects, customers, contracts, utility rights, incentives,
  equipment ownership, revenue, returns, licenses or team credentials.
- Label illustrative and forecast figures; cite sources and assumptions.
- Keep internal margins and vendor sourcing costs out of external materials.
- Distinguish contracted revenue from optionality. No guaranteed returns,
  automatic incentives or guaranteed equipment collateral value.

## Production paths

- Decks: `lib/ocean.js` (pptxgenjs), starting in `decks/_starter`. Layouts: cover, agenda,
  divider, statement, keyNumber (the one Crimson moment), twoColumn, pillars, metrics,
  timeline, table, chart, caseStudy, team, ask, appendix and back. Each takes an approved
  `pair` (for example `honeydew-peacock`); unapproved pairings and a second Crimson moment throw.
- Reports and proposals: `lib/publication.py` (JSON source in `documents/_starter`).
  Sage textured cover, staging header, running footer "Page X of Y", key/value glance
  tiles, Crimson risk flags.
- Legal documents: `lib/legal.py` (`documents/_starter/contract.json`) produces the plain
  Times New Roman PDF; `templates/ocean-legal-template.docx` is the Word template for counsel.
- Letters, cards, email, signage, web and apps: follow `surfaces/*/` and
  `tools/prototypes/`, which hold the HTML builders for the approved references.
- Logos for PPTX/PDF come from `assets/logos/png/` (rasterized from the SVG masters at 600 px tall).

## Workflow and QA

1. Read the sources and identify the audience, decision, surface and format.
2. Build from tokens and shared layouts, and keep evidence editable.
3. Run `npm test`, `npm run starter` and `npm run documents`, plus
   `scripts/qa.py` (PPTX) and `scripts/qa_pdf.py` (PDF; add `--legal` for legal documents).
4. Inspect EVERY rendered page at readable size against the guide and
   `output/reference/`. An automated PASS is not visual QA.
5. Fix, rebuild, rerender and reinspect. Deliver PDF plus editable source, with
   an honest note about any unresolved limitations.
6. Work on a branch and open a pull request with before/after renders. Do not
   merge brand-rule changes without Ocean leadership approval.

Keep rules, tokens, layout code, references, fonts and checks synchronized.
ChatGPT projects bridge through `brand/CHATGPT-PROJECT-INSTRUCTIONS.md`.
