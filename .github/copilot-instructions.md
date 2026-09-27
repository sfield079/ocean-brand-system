# Copilot instructions

Read `AGENTS.md` first; it is the master rule file for this repository and overrides anything here.
The Ocean Style Guide 2026 (`brand/Ocean_StyleGuide_2026.pdf`) is binding. Details: `brand/decisions.md`, `brand/BRAND-SYSTEM.md`.

Rules most often missed:
- Decks: build with `lib/recipe.js` / `lib/ocean.js` from a content file like `decks/_starter/content.js`; never hand-draw slides. Follow `surfaces/decks/recipes.json` and check `brand/DECK-CHECKLIST.md`.
- The close slide repeats the cover pairing and background and carries the logo only, no words.
- One approved two-color pairing per section (`tokens/ocean.tokens.json` → `pairing.detail`). Sage + Sprig and Sprig + Crimson carry 44 pt type and up only.
- Every interior slide and page footer shows classification and status together, e.g. "Confidential · Draft · Do not use" (`brand/notices.json`). Proposals use the proposal notice and name the recipient and pricing validity.
- Stack Sans Headline only (Times New Roman for legal documents). Caps are Bold or Light at +0.25 em.
- Photos are cropped, never stretched. Case studies use real Ocean photos; label stock and AI images "Representative image".
- Web apps and sites use `web-kit/` (see `brand/AI-APP-BUILDER-INSTRUCTIONS.md`).
- Never invent facts, metrics or credentials. Run `npm test`, `npm run starter`, `npm run documents`, and look at every rendered page before delivery.
