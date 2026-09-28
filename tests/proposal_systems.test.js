const assert = require('node:assert/strict');
const {OceanDeck} = require('../lib/ocean');
const {proposalTheme, scanClientSafeText, assertClientSafeText, assertPricingBreakdown, parseMoney} = require('../lib/proposals');

const theme = proposalTheme('financial-focus', ['Roof scope', 'Investment', 'Next steps']);
assert.strictEqual(theme.bookend, 'blackmoss-sprig');
assert.strictEqual(theme.close, theme.bookend);
assert.strictEqual(theme.sectionPairs.Investment, 'honeydew-olive');
assert.throws(() => proposalTheme('missing-theme'), /Unknown proposal theme/);

assert.ok(scanClientSafeText('This line mentions margin and vendor quote detail.').length >= 2);
assert.throws(() => assertClientSafeText('Internal estimate with margin'), /protected language/);
assert.doesNotThrow(() => assertClientSafeText('Roof replacement work and site access protection.'));
assert.strictEqual(parseMoney('$5.65M'), 5650000);
assertPricingBreakdown({total: '$5.65M', categories: [
  {label: 'Roof replacement work', value: '$4.35M'},
  {label: 'Tear-off and roof preparation', value: '$0.50M'},
  {label: 'Edges, drains and weatherproofing', value: '$0.45M'},
  {label: 'Site access and protection', value: '$0.35M'},
]});
assert.throws(() => assertPricingBreakdown({total: '$5.65M', categories: [
  {label: 'Roof replacement work', value: '$4.35M'},
  {label: 'Planning reserve', value: '$1.30M'},
]}), /protected language/);
assert.throws(() => assertPricingBreakdown({total: '$5.65M', categories: [
  {label: 'Roof replacement work', value: '$4.35M'},
  {label: 'Site access and protection', value: '$0.35M'},
]}), /not 5650000/);

const d = new OceanDeck({draft: true, sections: ['Investment']});
d.cover({title: 'Proposal', pair: theme.bookend});
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
d.back();
assert.strictEqual(d.log.map(x => x.kind).join(','), 'cover,content,close');
assert.throws(() => new OceanDeck({draft: true, sections: ['Investment']}).pricingBreakdown({
  section: 'Investment',
  total: '$1.0M',
  categories: [
    {label: 'Roof replacement work', value: '$0.8M'},
    {label: 'Planning reserve', value: '$0.2M'},
  ],
}), /protected client-facing language/);
console.log('PASS: proposal themes, client-safe language and pricing breakdown helpers');
