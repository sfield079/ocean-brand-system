// Proposal deck starter: the 10-slide client-presentation recipe with the proposal notice.
//   node decks/proposals/_starter/build.js      -> output/pptx/ocean-proposal-deck-reference.pptx
// Copy this folder to decks/proposals/<client>/, replace the content with verified inputs, then set:
//   classification: 'proposal' (footer "Confidential proposal"), recipient: the client, validity: the pricing window,
//   status: 'draft' while under review ("· Draft · Do not use"), 'final' when issued. Released proposal decks must
//   name the recipient; a specimen status cannot be released. See brand/decisions.md Part 10.
const {buildFromRecipe} = require('../../../lib/recipe');
const base = require('../../_starter/content');
const content = {
  ...base,
  deck: {...base.deck, title: 'Ocean RCS proposal deck reference', kind: 'Proposal', classification: 'proposal', status: 'specimen',
    recipient: 'Client name', validity: '30 days'},
};
buildFromRecipe(content, process.argv[2] || '10', 'ocean-proposal-deck-reference')
  .catch(e => { console.error(e.message); process.exit(1); });
