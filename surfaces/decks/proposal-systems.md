# Proposal deck systems

These helpers keep client proposals varied, client-safe and aligned with the Ocean deck rules.

## Theme presets

Theme presets live in `surfaces/decks/proposal-themes.json`. Each preset defines approved Ocean pairings for:

- bookends: cover and close, which must match
- agenda and key-number moments
- section body slides
- section divider slides

Use `proposalTheme(name, sectionNames)` from `lib/proposals.js` to resolve a reviewed preset into section-pair maps:

```js
const {proposalTheme} = require('../../lib/proposals');
const theme = proposalTheme('financial-focus', ['Roof scope', 'Investment', 'Next steps']);
```

This gives each proposal a different color rhythm without inventing pairings or bypassing the rule that each section keeps one pairing.

## Client-facing pricing breakdowns

Use `OceanDeck.pricingBreakdown()` for preliminary proposal pricing. It uses the lighter `ask` composition instead of a dense table, which helps avoid repeated table slides and keeps the total prominent.

```js
d.pricingBreakdown({
  section: 'Investment',
  total: '$5.65M',
  categories: [
    {label: 'Roof replacement work', value: '$4.35M'},
    {label: 'Tear-off and roof preparation', value: '$0.50M'},
    {label: 'Edges, drains and weatherproofing', value: '$0.45M'},
    {label: 'Site access and protection', value: '$0.35M'},
  ],
  pair: theme.sectionPairs.Investment,
});
```

Use plain category names that a client can understand. Do not expose internal unit costs, margin, markup, vendor quotes or estimate build-up.

## Client-safety language scan

Rules live in `brand/client-safe-language.json`. Run the scanner against generated decks or PDFs before client release:

```bash
python3 scripts/check_client_safe_language.py output/pptx/proposal.pptx
python3 scripts/check_client_safe_language.py output/pdf/proposal.pdf
```

The rule file itself contains the protected words by design, so do not treat `brand/client-safe-language.json` as a client-facing scan target.
