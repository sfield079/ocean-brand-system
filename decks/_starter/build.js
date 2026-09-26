// Builds the layout reference from the deck recipes: 15 slides by default, or pass 5 or 10.
//   node decks/_starter/build.js            -> output/pptx/ocean-layout-reference.pptx (15-slide recipe)
//   node decks/_starter/build.js 5          -> output/pptx/ocean-deck-recipe-5.pptx
const {buildFromRecipe} = require('../../lib/recipe');
const content = require('./content');
const length = process.argv[2] || '15';
buildFromRecipe(content, length, length === '15' ? 'ocean-layout-reference' : `ocean-deck-recipe-${length}`)
  .catch(e => { console.error(e); process.exit(1); });
