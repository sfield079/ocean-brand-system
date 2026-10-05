# Ocean Repository Migration

Status: controlling migration note, added 4 Oct 2026.

`sfield079/ocean-brand-system` is the current source of truth for Ocean RCS brand rules, deck generation, proposals, reports, product kits, pro-forma kits, app-builder instructions and generated web-kit assets.

Older Ocean deck or presentation repositories are deprecated for new work. They may be used only as historical reference or to recover old artifacts. Do not start a new deck, proposal, report, contract, web page, Vault screen, Wave screen or app kit from an older repository.

When an AI tool, ChatGPT project, Base44 app, local checkout or prompt refers to `ocean-deck-system`, `Ocean Presentations` or another older Ocean publication repo, update it to:

- repository: `sfield079/ocean-brand-system`
- branch: `main`
- setup script: `bash scripts/setup.sh`
- controlling files: `AGENTS.md`, `brand/BRAND-SYSTEM.md`, `brand/decisions.md`, `brand/PRODUCT-KIT.md`, `brand/PROFORMA-KIT.md`

If an older repo must remain on disk, add a top-level note that it is deprecated and point back to this file.

Local copy reconciliation and pending release status: `brand/LOCAL-ALIGNMENT.md`.
