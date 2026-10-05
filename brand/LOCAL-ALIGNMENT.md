# Local and GitHub alignment

As of 5 October 2026.

## Authority

The active repository is sfield079/ocean-brand-system. Main holds approved releases.
The review branch codex/brand-rules-product-kits contains proposed product-kit and
repository alignment changes; it must be merged before a main-based cloud environment
receives those changes. Local work should identify its branch and commit.

Use tokens/ocean.tokens.json for color values, the original logo assets for identity,
and the bundled Stack Sans Headline fonts. Follow AGENTS.md's document hierarchy.

## Copies found

| Copy | Role | Action |
|---|---|---|
| ocean-brand-system | Active Git checkout | Build here; publish changes through a pull request |
| Ocean Presentations | Older publication system; no configured remote | Retain evidence and outputs; entry instructions now redirect to active checkout |
| Ocean Presentations/ecosystem-brand | Snapshot of main at 75fb66e with local outputs | Retain for recovery; entry instructions now redirect |
| Ocean Presentations/ecosystem | Internal audit, financial workbook and draft mockups | Retain locally as review evidence; do not treat as approved brand rules |

The local copies' original entry instructions are preserved in
Ocean Presentations/migration-backup-2026-10-05. No source material or outputs
were deleted. Snapshot code is not copied over the current builders.

## Outstanding review work

Vault is within Ocean. Existing audit evidence describes Wave as a workflow/action
product with proposals, field work and signatures; the earlier monitoring-only
mockup is incomplete. Reconcile the product brief with that evidence before
continuing screen design. The rejected mockups remain drafts and are excluded
from approved references. No live Base44 changes are authorized by this cleanup.

## Repeatable checks

Run python3 scripts/check_brand_alignment.py and npm test. Regenerate web-kit
with python3 scripts/build_web_kit.py after token changes. Keep ChatGPT project
instructions and downloaded project kits aligned with the merged main release.
Local redirect files do not update ChatGPT project settings automatically.
