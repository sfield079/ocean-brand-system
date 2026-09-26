# Ocean RCS Deck System

Code-driven production system for Ocean RCS investor, proposal, and capabilities decks.
Codex reads `AGENTS.md` automatically; that file is the rulebook.

## Setup (one time)
1. Create a private GitHub repo named `ocean-deck-system` and upload this folder's contents.
2. In Codex (chatgpt.com/codex), connect GitHub and select this repo; create an environment.
   Setup script for the environment: `npm install && apt-get update && apt-get install -y libreoffice poppler-utils && pip install python-pptx`
3. Drop real assets into `assets/` (logos, Higgsfield images, site photos) and facts into `source/`.

## Local use
```
npm install
pip install python-pptx          # QA script
npm run starter                  # builds + renders + QAs the 13-layout reference deck
```
Requires LibreOffice (`soffice`) and poppler (`pdftoppm`) for rendering.

## Make a new deck
```
cp -r decks/_starter decks/investor/<deck-name>
# edit content in decks/investor/<deck-name>/build.js, change the save() name
node decks/investor/<deck-name>/build.js
bash scripts/render.sh output/pptx/<deck-name>.pptx
python3 scripts/qa.py output/pptx/<deck-name>.pptx
```

## Layouts in lib/ocean.js
cover · divider · statement · twoColumn · pillars · metrics · timeline · table · chart · caseStudy · team · ask · appendix

The library refuses text that doesn't fit its box (it throws an error rather than shrinking type).
That is intentional: shorten or split the slide.

## Fonts
Default is Arial so files render identically everywhere. To use Stack Sans, install it on every
machine that opens the PPTX, then change `fonts` in `brand/color-system.json`. PDF is always the
safe delivery format.

See `CODEX-PROMPTS.md` for copy-paste prompts.
