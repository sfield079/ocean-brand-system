# Ocean RCS brand system

The single brand source of truth for every Ocean surface: oceanrcs.com, micro-apps,
decks, reports, proposals, formal and legal documents, business cards, email,
signage, charts, icons and graphics. Read `AGENTS.md`, then `brand/BRAND-SYSTEM.md`.

| Folder | Contents |
|---|---|
| `brand/` | Style guide (Brand Bible), decisions, typography rules, full spec, audit |
| `tokens/` | Color, type, shape and contrast tokens; CSS, Tailwind and chart builds |
| `assets/` | Logos and one-color variants, icons, fonts, micro-graphics, textures, images |
| `charts/` | Chart system builder, SVG/PNG reference and animation reference |
| `surfaces/` | Approved references per surface (web, apps, decks, formal, print, email, signage) |
| `output/reference/` | Approved example deck, report, contract and overview boards |
| `lib/`, `decks/`, `documents/`, `scripts/` | Production pipelines: decks (`ocean.js`), reports and proposals (`publication.py`), legal (`legal.py`) |
| `tools/prototypes/` | Builders that produced the approved references |

## Cloud setup

Use repository `sfield079/ocean-brand-system` (formerly `ocean-deck-system`), branch `main`, image `universal`.
Set the Codex environment setup script to:

```bash
bash scripts/setup.sh
```

Keep agent internet off. Setup installs npm/Python packages, LibreOffice,
Poppler, fontconfig and bundled fonts. No secrets or environment variables are
needed. When changing the setup script, rebuild the environment cache.

## Commands

```bash
npm ci
python3 -m pip install -r scripts/requirements.txt
python3 scripts/install_fonts.py
npm test
npm run starter
npm run documents
```

`starter` needs Bash, LibreOffice and Poppler. It builds the 5-, 10- and 15-slide recipe decks and the layout catalog from `decks/_starter/content.js`,
checks the PPTX, exports the PDF, verifies embedded fonts and renders PNGs.
`documents` builds the proposal, report and legal contract specimens from structured JSON
with embedded fonts, plus the Word legal template. No office renderer needed.
On Windows, use your Python executable in place of `python3`; document commands
and `node decks/_starter/build.js` work natively. Use the Linux cloud pipeline
for full deck rendering when Bash/LibreOffice tools are not on your PATH.

## New publications

Copy a starter into `decks/<category>/<name>/` or `documents/<name>/`.
Adjust relative imports when moving the starter to a deeper folder. Set
`draft:false` for release; replace all template content with verified inputs.
For documents call `lib.publication.build(source_json, output_pdf)`.
Supported document formats are Letter (default) and A4 (`"format":"A4"`).

All text and chart data in the PPTX remain editable. Document JSON is the
editable source; the PDF retains selectable live text. No claim of editable DOCX
output is made. Use the document path for reports, not miniature slide text.

## Quality gates

```bash
python3 scripts/qa.py output/pptx/example.pptx
bash scripts/render.sh output/pptx/example.pptx
python3 scripts/qa_pdf.py output/pdf/example.pdf
```

Only specimens use `--draft`. Release QA rejects unresolved placeholders.
PPTX QA checks fonts, font minimums, bounds, text overlap and text colors,
including table/chart XML. PDF QA verifies actual font use, font embedding,
selectable text, bounds and likely text overprint. The layout engine also
measures glyph widths before writing. These checks are not a substitute for
visual review. Inspect every rendered page and fix all visible problems.

GitHub Actions runs regression checks and builds all specimens on each change.
Download the `ocean-publication-specimens` artifact for PDFs, PPTX and renders.
Successful Actions means automated validation passed, not design approval.

## Fonts and assets

`brand/fonts/` includes the Google Fonts variable source, five static weights
(Light, Regular, Medium, SemiBold, Bold) and the OFL license. `brand/fonts/legal/` holds
Liberation Serif (metric-identical to Times New Roman) for legal PDFs when Times is absent. No fallback is permitted. Installer is idempotent and per-user.
Original logo SVGs and a transparent PNG are in `assets/logos/`.
The source guide is `brand/Ocean_StyleGuide_2026.pdf`. Reference decisions and
source links are recorded in `brand/REFERENCE-NOTES.md`.

## ChatGPT project bridge

ChatGPT project chats do not automatically load GitHub AGENTS.md. Add
`brand/CHATGPT-PROJECT-INSTRUCTIONS.md` to the Ocean RCS project's sources and
reference the repository in its instructions. Keep existing business context.
The approved brand system (26 September 2026) supersedes older chat
instructions about white-only pages, excluded palette colors and backgrounds.

See CODEX-PROMPTS.md for reusable task briefs. Reference specimens are not
external business deliverables and do not assert project results or returns.
