# Ocean Product Kit

Status: proposed product guidance on the review branch, added 4 Oct 2026; approval and merge are pending. Applies to oceanrcs.com, Vault, Wave, portals, dashboards, calculators, micro-apps and app-like website screens. Use with `web-kit/` and `brand/AI-APP-BUILDER-INSTRUCTIONS.md`.

## 1. Build mobile first

Design the phone screen first, then expand to tablet and desktop. Do not shrink a desktop dashboard into a phone.

- Phone: one primary task per screen, bottom navigation or compact top bar, stacked cards, sticky action when useful.
- Tablet: split panes for list/detail, persistent filters where space allows, two-column evidence and pro-forma review.
- Desktop: full navigation, dense tables, side panels, compare views and multi-column dashboards.
- Every app state must work at phone, tablet and desktop widths before it is considered complete.

## 2. Product color modes

Use one mode per screen or workflow. Do not mix modes inside one small component.

| Mode | Pairing | Use |
|---|---|---|
| Default workspace | Honeydew field, Blackmoss ink, Sage rules, Cedar secondary text | oceanrcs.com, ordinary forms, reading, content management, client-friendly workspaces |
| Command / dark | Blackmoss field, Honeydew ink, Sprig highlights, Sage hairline tiles | live monitoring, operating consoles, low-glare dashboards, urgent workflows |
| Asset / site | Honeydew field, Olive or Cedar structure, Blackmoss text | Vault records, project profiles, field evidence, site galleries, audit trails |
| Financial / pro-forma | Honeydew or White field, Blackmoss text, Peacock headers | revenue, pricing, sensitivity tables, capital stacks, investor financial screens |

Crimson is semantic in every mode. It may mark total revenue, critical impact, investor-decision figures, missing required inputs, stale data, real alerts, risks and deadlines. Use at most one Crimson emphasis per screen state, consistent with AGENTS.md.

## 3. Vault

Vault is the evidence and project-record product. It should feel calm, searchable and trustworthy.

- Default to asset/site mode.
- Use real Ocean project photos for case studies, site evidence and audit trails.
- Every file, photo, claim and number should show source, date, owner and status.
- Key states: verified, pending, missing, stale, superseded, confidential, draft, do-not-use.
- Mobile screens prioritize search, recent records, required actions and one-tap capture.
- Tablet and desktop add side-by-side preview, metadata, comments and issue resolution.

## 4. Wave

Wave includes workflow and action surfaces. The local audit records WavePro proposals and estimating, WaveTech, WaveSign and service-network entry points. Reconcile these existing workflows before redesigning its navigation. Monitoring, impact and financial signal screens are proposed kit examples; their presence must not be assumed to prove a live product capability.

- Use command/dark mode for live operations and financial/pro-forma mode for revenue and investor review.
- Highlight totals, deltas, critical thresholds and unresolved inputs with semantic accents.
- Charts must have direct labels, source lines and final-frame PDF exports.
- Mobile screens show the current state, top metric, active alert and next action.
- Tablet and desktop add trends, comparisons, scenario toggles and evidence drawers.

## 5. Public site

The public site starts in default workspace mode: Honeydew + Blackmoss with sparse Sage accents and real photography. It may use alternate section pairings when the content changes job.

- The first viewport should clearly identify Ocean RCS and the offer.
- Use real or licensed imagery. Do not use AI backgrounds, decorative grids, glows or fake dashboards.
- Case studies use real Ocean project photos and verified facts only.
- Calls to action use ink-filled buttons, not pills or gradients.

## 6. Components

- Navigation: icon plus caps label. Phone may use bottom navigation; tablet and desktop may use left navigation.
- Cards: hairline frame, bottom-right chamfer, one key, one value, one note.
- Tables: Bold caps headers, row rules at 20% ink, tabular numbers, sticky header on mobile when useful.
- Charts: Sage context, Cedar focus, Crimson only for the flagged semantic value.
- Reports inside apps: export to PDF using the document or pro-forma kit, not screenshots.
- Images: object-fit cover; crop, never stretch.

## 7. Mockup set

Every product-kit update should include these mockups or renders:

- Phone, tablet and desktop for Vault.
- Phone, tablet and desktop for Wave.
- Public site first viewport and one content section.
- Financial/pro-forma screen with totals, assumptions and sensitivity.
- Component sheet for cards, tables, charts, report blocks, notices and semantic accents.
