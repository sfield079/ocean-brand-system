# Ocean RCS brand system: ChatGPT project instructions

Paste this file into the ChatGPT project instructions. Upload `brand/DECK-CHECKLIST.md`,
`brand/decisions.md`, `brand/BRAND-SYSTEM.md`, `brand/notices.json`, `surfaces/decks/recipes.json`,
`output/reference/examples/Ocean_Example_Presentation.pdf` and `Ocean_Example_Proposal.pdf` as
project files, and connect https://github.com/sfield079/ocean-brand-system if available. Never
claim to have read a file you could not open. The master rule file is `AGENTS.md`; this file
repeats what ChatGPT needs most.

## How decks get built

The brand rules are enforced by code in the repository (`lib/ocean.js`, `lib/recipe.js`,
`scripts/qa.py`). ChatGPT chat cannot run that code, so a deck drawn by ChatGPT directly will
drift from the rules. Therefore:

1. **Preferred:** build every deck in Codex from this repository. In ChatGPT, write the content
   as a `content.js` file in the shape of `decks/_starter/content.js` (sections, slides by id,
   layouts, notice settings), then hand it to Codex with the Presentation prompt in
   `CODEX-PROMPTS.md`.
2. **If you must produce a PPTX here:** follow `brand/DECK-CHECKLIST.md` line by line, state
   which lines you could not verify, render every slide and look at it, and tell the user to run
   `python3 scripts/qa.py <deck>.pptx` before using it. Never describe a hand-built deck as
   compliant.

## Rules that are most often missed

- **Recipe:** follow `surfaces/decks/recipes.json` for 5, 10 or 15 slides. One pairing per
  section, used on every content slide in that section; adjacent sections differ.
- **Close:** same pairing and background as the cover, vertical logo only, no words.
- **Notice:** every slide except the cover and close shows classification and status together
  in the footer, for example "OCEAN RCS · CONFIDENTIAL · DRAFT · DO NOT USE". Proposals read
  "CONFIDENTIAL PROPOSAL" and name the recipient and pricing validity. Investor decks read
  "CONFIDENTIAL · FOR DISCUSSION ONLY" and end with an Important notice slide before the close.
- **Pairings:** one approved two-color pairing per slide. Olive + Honeydew is the earthy
  content pairing; Sage + Sprig and Sprig + Crimson carry 44 pt type and up only (dividers,
  pull quotes, key moments). Tonal pairings carry no text. See decisions.md Part 12.
- **Emphasis:** Bold words, an inverted chip, one highlighted tile or a bottom-line band.
  Crimson is optional and appears once per deck at most.
- **Images:** crop, never stretch. Ocean project photos for case studies and site evidence;
  stock and AI images labeled "Representative image". No unlicensed photos.
- **Type:** Stack Sans Headline only, four weights, caps at +0.25 em, nothing under 9 pt.
  Legal documents use Times New Roman.

## Everything else

The Ocean Style Guide 2026 is the Brand Bible and is binding. Presentations and reports are
different systems. Web apps and sites use `web-kit/` and `brand/AI-APP-BUILDER-INSTRUCTIONS.md`.
Proposals start from `documents/_starter/proposal.json` (Letter PDF) or
`decks/proposals/_starter/` (deck). Formal documents are plain and institutional. Never invent
facts, metrics or promises, and compare every page with `output/reference/examples/` before
delivery.
