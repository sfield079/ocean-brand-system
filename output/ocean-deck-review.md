# Ocean deck regeneration review

Date: 27 September 2026. Branch: `deck/mobility-energy-investor`. All deliverables remain draft. Do not merge or distribute as final.

## Deliverables and evidence

| Deck | Recipe / rendered pages | Editable content | Supplied source |
| --- | --- | --- | --- |
| Mobility & Energy investor | 15-slide recipe + investor notice = 16 | `decks/investor/mobility-energy-platform/content.js` | `Ocean_RCS_Mobility_Energy_Platform_Investor_Deck_Redesigned.pdf` |
| Company & Leadership overview | 10 | `decks/company/leadership-overview/content.js` | `Ocean_RCS_Company_Leadership_Overview_Redesigned.pdf` |
| Confidential Internal Diligence Appendix | 10 | `decks/internal/diligence-appendix/content.js` | `Ocean_RCS_Confidential_Internal_Diligence_Appendix_Redesigned.pdf` |

Each deck is built by `lib/recipe.js` and `lib/ocean.js`; no independently drawn slides or shared-layout changes. Companion decks adapt the supplied material into the repository's 10-slide spine. Detailed source references and some supporting detail are retained in PPTX speaker notes. Supplied leadership claims are not independently verified credentials.

Investor sections remain Platform, Pipeline, Capital and Next steps. Classification remains investor and status draft. The appendix is internal/confidential; the overview is confidential. Every interior page carries classification and draft status together. The close repeats the cover's background and pairing and carries the official vertical logo only.

The user confirmed DJI_0482 is a real Ocean project. It is labeled Ocean project photo; no project size, customer, ownership or performance is inferred. The investor mobility-hub concept remains labeled Representative image. Photo crops preserve aspect ratio, as do the official logos. Image metadata retains the release rights-confirmation requirement.

## Required missing inputs

Investor slide 14 intentionally retains exactly three `[TBD]` items:

- Capital sought
- First funded asset
- Terms

No financial figures, customers, assets or commitments were invented. The key figures 8, 4 and 5 count the supplied process stages or operating categories, not commercial results.

## Verification

Linux GitHub Actions runs `bash scripts/setup.sh`, the three native `build.js` files, `python3 scripts/qa.py <pptx> --draft`, and `bash scripts/render.sh <pptx> --draft`. The rendering script also runs PDF QA, including embedded-font checks. The existing Publication QA workflow runs `npm test`, `npm run starter` and `npm run documents`.

Every PNG was opened individually and reviewed against `brand/DECK-CHECKLIST.md`: investor 1–16, company 1–10 and appendix 1–10. No visible text clipping, accidental overlaps, stretched photos or distorted logos were found. The approved recipe controls pairing, section sequence and photo/background rhythm. Stack Sans Headline is used throughout. Only the investor deck contains unresolved placeholders, as explicitly requested.

Final artifacts come from [successful deck build 36312480777](https://github.com/sfield079/ocean-brand-system/actions/runs/36312480777), source commit `0254d9b4e60c59962ba57dc7f806dc908c5515c0`. The downloaded ZIP's SHA-256 matched the Actions artifact digest: `0360d88387014a8148da8f97dc7390ef96a01ceb6bc15e77d28b810b2b7d1baa`. The four changed investor PNGs (7, 9, 11 and 14) were reopened and inspected; the other 32 final PNGs are byte-identical to those already inspected. [Publication QA 36312480767](https://github.com/sfield079/ocean-brand-system/actions/runs/36312480767) also passed, including regression tests, starter builds and document builds.

Content review added the required forward-looking caveat to investor slides 9, 11 and 14; slide 12 already had it. Slide 9 uses the native footnote field. The pillars and ask layouts have no footnote field, so slides 11 and 14 show the exact caveat in their existing lede region. The displaced equipment and monetization detail remains in speaker notes. The concept caption's terminal period was removed.

## Shared-builder checklist exceptions

Automated PASS is not a claim of full checklist compliance. These existing shared-builder differences were left unchanged to respect the content-only scope:

- Investor slides 4, 5, 7–9, 11, 12 and 14; company and appendix slides 3–7 and 9: the staging logo is 44 px high on the 1920 × 1080 design grid. BRAND-SYSTEM.md §16 specifies at least 48 px. Aspect ratio is correct.
- The same staging headers use navigation tracking of 0.12 em (and number tracking 0.10 em), versus the checklist's 0.25 em caps rule.
- Investor slides 11 and 14 display the financial caveat in the lede, rather than a bottom footnote, because their shared layouts do not expose a footnote field.

These require a separate shared-builder change to resolve strictly; no brand rules, QA checks or layout code were weakened for this regeneration.
