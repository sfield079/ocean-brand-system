# Copy-paste Codex prompts

## New investor deck (outline first)
Follow AGENTS.md. Read everything in source/ and list what is in assets/. Build a [12]-slide
investor deck for [OPPORTUNITY]. First give me a slide-by-slide outline as a table: slide #,
layout function from lib/ocean.js, headline (takeaway, max 2 lines), max 3 points, visual/asset.
Then list every fact, metric, and image you still need from me. Do not build until I approve.

## Build after approval
Approved. Copy decks/_starter to decks/investor/[deck-name], build with lib/ocean.js layouts only,
save as [deck-name]. Run scripts/render.sh and scripts/qa.py, open every PNG in output/renders,
fix every issue, re-render, and give me the production note from AGENTS.md.

## Customer solar + storage proposal
Follow AGENTS.md. Using source/project-facts.md for [SITE], build a 10-slide customer feasibility
deck in decks/solar-bess/[site]. Plain-language equipment on main slides, SKUs in the appendix,
no internal margins. Mark anything unconfirmed as [TBD]. Run the full QA loop.

## Revise one slide
Change only slide [N] of decks/[path]/build.js: [CHANGE]. Keep all other slides identical.
Rebuild, re-render, inspect slide [N] and its neighbors.

## Add a new layout
Add a new layout function `[name]` to lib/ocean.js following the existing pattern (brand colors
only, fit() guards on every text box, 0.6 in margins, footer). Add an example to
decks/_starter/build.js, run `npm run starter`, and inspect the render.
