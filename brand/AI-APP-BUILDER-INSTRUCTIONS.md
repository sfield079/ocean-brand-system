# Ocean RCS brand rules for AI app and site builders

Paste this whole file into the builder's custom instructions or knowledge (Base44, Lovable,
Bolt, v0, Replit, Cursor and similar tools). It is kept under 10,000 characters so tools that
cut long instructions receive all of it. Source of truth: https://github.com/sfield079/ocean-brand-system
(`AGENTS.md`, `brand/BRAND-SYSTEM.md` §4, `brand/decisions.md`). The Ocean Style Guide 2026 is binding.

## Setup (do this first)

1. Copy the repository's `web-kit/` folder into the app, for example `src/brand/ocean/` or
   `public/brand/ocean/`. Do not rebuild the colors, fonts or logos by hand.
2. Import `web-kit/ocean.css` once at the app root. It self-hosts Stack Sans Headline and
   Material Symbols and defines every approved pairing.
3. With Tailwind, add `web-kit/tailwind.preset.js` to `presets` and use the `ocean-*` colors.
4. Use the logo SVGs in `web-kit/logos/` (for example `logo_horizontal_blackmoss.svg` on light
   fields, `logo_horizontal_honeydew.svg` on dark fields). Never type the word OCEAN as a logo.

## Color

- Palette: Blackmoss #0B1617, Peacock #102426, Cedar #1B4039, Sage #618C7C, Olive #6E734C,
  Citron #A69856, Crimson #EB3819, Sprig #D5CCA0, Honeydew #F3FBF8. White #FFFFFF is for print.
- Every section uses one approved two-color pairing: `data-pair="<field>-<ink>"` on the section.
  Adjacent sections use different pairings. Never invent a color, tint, gradient or shadow.
- Text-safe pairings for body copy: Honeydew + Blackmoss (site default), Honeydew + Peacock,
  Honeydew + Cedar, Honeydew + Olive, Sprig + Blackmoss, Sprig + Peacock, Sprig + Cedar,
  Blackmoss + Citron, Peacock + Citron, Blackmoss + Sage.
- Large text only (24 px and up): Sage + Honeydew, Blackmoss + Crimson, Peacock + Sage,
  Cedar + Citron, Peacock + Crimson, Honeydew + Crimson, Blackmoss + Olive, Peacock + Olive,
  Sprig + Olive, Cedar + Sage.
- Display only (44 px+ headlines and graphics): Sage + Sprig, Sprig + Crimson, Citron + Honeydew,
  Cedar + Olive. Tonal pairs (Citron + Sprig, Citron + Olive, Blackmoss + Cedar, Honeydew +
  Sprig, Cedar + Peacock, Blackmoss + Peacock) carry no text.
- Never pair Sage + Crimson, Olive + Crimson, Sage + Citron, Sage + Olive, Citron + Crimson or
  Cedar + Crimson.
- Leadership priorities: Olive + Honeydew for earthy content (economics, land, sustainability);
  Sage + Sprig for calm statement bands and quotes; Sprig + Crimson for one urgent moment
  (deadline, action required).
- Crimson is rare: one key moment per page at most, or the risk-flag triangle in apps.

## Type

- Stack Sans Headline only, in Light 300, Regular 400, Medium 500 and Bold 700.
- All caps are always Bold or Light with 0.25 em letter spacing (`.ocean-caps`,
  `.ocean-caps-light`). Hero type is Light with -0.04 em tracking (`.ocean-hero`).
- Body 16–18 px with 1.5–1.6 line height. Body contrast at least 4.5:1.
- Emphasis: Bold words, one inverted chip (`.ocean-chip`) or a bottom-line band
  (`.ocean-bottom-line`). One device per idea.

## Components

- Header: a 2 px framed bar with cells for the logo, Bold caps navigation (12 px), one filled
  call-to-action cell and icon cells. On mobile: logo, CTA and menu.
- Buttons: primary `.ocean-btn` (ink fill, 12 px chamfer, Bold caps); secondary
  `.ocean-btn-secondary` (2 px outline, trailing `arrow_forward` icon). No pill buttons.
- Cards: `.ocean-card` (hairline frame, bottom-right chamfer), 32 px icon, caps key, Regular text.
- Icons: Material Symbols Outlined, weight 400, fill 0, at 50% of their cell.
- Motion: fades and short moves of 150–250 ms. Respect reduced motion. No parallax, bounce or glow.
- Focus: 2 px outline in the section ink.

## Sites and apps

- oceanrcs.com: Honeydew field with Blackmoss ink by default; sections may switch pairings.
- Micro-apps (dashboards, portals, calculators): default dark theme (Blackmoss field, Honeydew
  ink, Sage hairline tiles) with an approved light theme (Honeydew field, Peacock ink). Ship both
  with a user toggle on `<html data-theme="dark|light">`, remember the choice and follow the OS
  setting on first load. 240 px left navigation with icon + caps labels; the active item is
  inverted. The graphic mark and app name + version sit in the navigation footer, and the
  graphic mark is the favicon.
- Tables: Bold caps headers, row rules at 20% ink, numbers in Bold.
- Charts: Sage for context, Cedar for the focus, every number on a bar in Honeydew Bold.

## Images

- Sources: Ocean project photos, licensed stock or top-rated AI generators. No unlicensed photos.
- Case studies and "our work" use real Ocean project photos only. Label stock and AI images
  "Representative image" wherever a reader could mistake them for an Ocean project.
- Crop images to their frame (`object-fit: cover`); never stretch them.
- Real environments, people, infrastructure and natural light; restrained overlays only.

## Notices

- Anything confidential or not final shows its notice in the page or screen footer, with
  classification and status together, for example "Ocean RCS · Confidential · Draft · Do not use"
  (`.ocean-notice`). Wording lives in `web-kit/notices.json`.

## Truth

- Never invent projects, customers, metrics, savings, incentives, credentials or testimonials.
  Use placeholders the user can see, such as [TBD], and list what is missing.
- Keep internal margins and vendor pricing out of anything customer-facing.
