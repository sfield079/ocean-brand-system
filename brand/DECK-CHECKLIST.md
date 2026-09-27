# Ocean deck checklist

Every Ocean deck must pass every line below. Decks are built only with `lib/ocean.js` and
`lib/recipe.js` from a content file (AGENTS.md, Build rule), which enforce most of these in code.
A deck drawn any other way (ChatGPT or Codex drawing slides with ReportLab or python-pptx, PowerPoint,
Keynote, Google Slides) fails `scripts/qa.py` / `scripts/qa_pdf.py` and must be rebuilt. Use this
checklist to review the rendered PDF by eye. Sources: `brand/decisions.md` Parts 9–13,
`brand/BRAND-SYSTEM.md` §8, `surfaces/decks/recipes.json`.

## Structure (recipe)

- [ ] Size is 16:9, 13.333 × 7.5 in.
- [ ] The spine matches the recipe for the length (BRAND-SYSTEM.md §8):
  - 5 slides: cover, situation, solution, key number, close.
  - 10 slides: cover, agenda, Site ×2, System ×2, Economics chart, key number, next steps, close.
  - 15 slides: the 10-slide spine plus dividers for Site, System and Economics, a schedule and an economics table.
  - Over 20 slides: add an appendix; over 30, split into a deck and a report.
- [ ] Every section uses one pairing on all of its content slides, and adjacent sections differ.
- [ ] At most four content pairings in the deck.
- [ ] Dividers reverse their section's pairing or share one of its colors, on an environment background or a photo.
- [ ] No more than four slides in a row without a photo or environment background, and no more than two dense slides (tables, timelines, appendix) in a row.

## Cover and close

- [ ] The close uses exactly the same pairing and background as the cover.
- [ ] The close carries the vertical Ocean logo only: no words, address, website or "Thank you".
- [ ] The cover carries the full notice sentence above the meta line.

## Color

- [ ] Every slide uses one approved two-color pairing (field + ink). Photos, and the footer on display pairings, are the only exceptions.
- [ ] Content slides use text- or large-tier pairings only. Sage + Sprig, Sprig + Crimson, Citron + Honeydew and Cedar + Olive carry 44 pt type and up only (dividers, pull quotes, key moments).
- [ ] Olive + Honeydew, Sage + Sprig and Sprig + Crimson are used where decisions.md Part 12 assigns them.
- [ ] Crimson appears as one key moment per deck at most, only on Blackmoss, Peacock, Honeydew or Sprig. Emphasis does not need Crimson.

## Emphasis (Part 9)

- [ ] One emphasis device per idea: **Bold** words, an inverted chip, one highlighted metric tile, or a bottom-line band.
- [ ] Bottom-line bands: "BOTTOM LINE" in Light caps, the statement in Bold, in the section ink.

## Notices (Part 10)

- [ ] Every slide except the cover and close has a footer that shows classification and status together, for example `OCEAN RCS · CONFIDENTIAL · DRAFT · DO NOT USE`. That includes the agenda, dividers and the key-number slide.
- [ ] Proposal decks read `CONFIDENTIAL PROPOSAL`, name the recipient and give the pricing validity on the cover.
- [ ] Investor decks read `CONFIDENTIAL · FOR DISCUSSION ONLY` and have the "Important notice" slide before the close.
- [ ] Anything not approved says `DRAFT · DO NOT USE`.

## Type and logo

- [ ] Stack Sans Headline only (Light, Regular, Medium, Bold). Caps are Bold or Light at +0.25 em. Nothing under 9 pt.
- [ ] The official logo files from `assets/logos/`, never retyped, at the §16 minimums or larger.
- [ ] Staging header on content slides: logo cell, page cell, section navigation, client cell, section numbers.

## Images

- [ ] Photos are cropped to their frame and never stretched.
- [ ] Sources follow Part 6: Ocean project photos for case studies and site evidence; licensed stock or AI images labeled "Representative image". No unlicensed photos.

## Before delivery

- [ ] Render every slide to an image and look at each one. An automated PASS is not visual review.
