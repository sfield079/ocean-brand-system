# Base44 Ocean App Audit

Status: read-only discovery snapshot, 4 Oct 2026. This file records what was visible through the connected Base44 account during the product-kit rule update. It is evidence for future app design work, not a replacement for `brand/PRODUCT-KIT.md`.

## Apps found

| App | Base44 name | App id | Role |
|---|---|---|---|
| Ocean / Vault / public site | `Ocean ` | `690fe9219910b72e92dadea9` | Main Ocean app with public site, Vault, project records, proposals, service network, Wave access fields and many internal operations screens |
| Wave | `Wave` | `6a08eea86eb86429e0143787` | Separate Wave app with rail navigation, scene routing, service-company experience, agreement authoring and Wave modules |

Vault is inside the `Ocean` Base44 app. It is not a separate Base44 app in this account. Treat `Ocean` as the app to inspect and update for Vault, public-site and shared operations work.

The Ocean-email Base44 connection required reauthentication during this audit. The second linked Base44 account allowed read-only access to the apps above. No Base44 app files were changed.

## Shared findings

- Both apps already include an embedded `src/brand/ocean/` kit with `ocean.css`, `ocean.tokens.json`, `notices.json` and `tailwind.preset.js`.
- The embedded kit predates the new product modes and semantic Crimson helpers added in this repository on 4 Oct 2026.
- Both apps should receive the refreshed web kit after the repository changes are reviewed.
- Both apps still contain direct hex usage and local styling. The redesign should migrate active surfaces toward product-mode classes and tokens rather than continuing page-by-page color choices.

## Ocean app findings

- `src/Layout.jsx` separates public pages, paper pages and standalone app pages. `OceanVault`, `VaultSettings`, `Projects`, `ProjectDetails`, `VaultDocuments`, `ProjectPhotos`, `ServiceNetwork`, `PublicSiteStyling`, `FinanceDashboard` and many agreement/proposal tools are standalone pages.
- The public home page (`src/pages/Home.jsx`) currently uses a white page, Blackmoss text and Sage accents, with large marketing statistics such as "16", "1,000+", "50%" and "25". Those claims must be verified before being treated as reusable facts in brand-system deliverables.
- `PublicSiteStyling.jsx` allows runtime editing of brand colors and includes a "Pill" button-radius option. That conflicts with the product kit rule that Ocean buttons are chamfered or squared, not pill-shaped.
- `OceanVault.jsx` exists as a major page, and the app schemas confirm Vault-like records: Projects, service work orders, project photos, workspace resource links, notifications, brand kit versions, Wave access fields and service-company access.

## Wave app findings

- `src/Layout.jsx` uses a fixed Sage rail for navigation, with Home, Solutions, Play, Estimator, About and service-company variants.
- `src/App.jsx` routes Wave scenes including WaveTech, WavePro, WavePay, WaveSign, WaveManage, WaveCommand, WaveGuide, WaveStore and service-company surfaces.
- `src/pages/Hero.module` includes rounded 24 px tiles, green `#00A86B`, shadows, hover scale and product-image cards. That is outside the Ocean product kit direction and should be replaced by the mobile-first product modes.
- Agreement authoring screens already use Blackmoss/Sage/Honeydew-style instrument UI. They should be brought into the pro-forma/product states and tokenized where they show pricing, signatures, status or financial details.

## Design direction from the new rules

- Ocean / Vault should move to asset/site mode for records, evidence, files, project profiles and audit trails.
- Wave should use command/dark mode for live operational surfaces and financial/pro-forma mode for revenue, impact, pricing and investor-review surfaces.
- Public site pages should use default workspace mode: Honeydew + Blackmoss, sparse Sage accents, real/verified imagery and no AI backgrounds, glows or fake dashboards.
- Crimson should appear only for semantic emphasis: total revenue, critical impact, stale data, missing inputs, risk, alert, deadline or investor-decision figures.
- Mobile screens should be designed first, then expanded to tablet split panes and desktop dashboards.

## Next Base44 work

1. Copy the refreshed `web-kit/` into both apps under `src/brand/ocean/`.
2. Remove or block pill button options in public-site styling.
3. Replace legacy rounded/shadowed product tiles in Wave with Ocean card geometry.
4. Produce phone, tablet and desktop mockups for Vault, Wave, public site and financial/pro-forma screens.
5. Build component examples for cards, tables, charts, report blocks, notices and semantic accents.
