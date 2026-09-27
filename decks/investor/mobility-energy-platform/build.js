// node decks/investor/mobility-energy-platform/build.js  -> output/pptx/ocean-mobility-energy-investor.pptx (15-slide recipe)
// Then: python3 scripts/qa.py output/pptx/ocean-mobility-energy-investor.pptx --draft
//       bash scripts/render.sh output/pptx/ocean-mobility-energy-investor.pptx --draft
const {buildFromRecipe} = require('../../../lib/recipe');
buildFromRecipe(require('./content'), process.argv[2] || '15', 'ocean-mobility-energy-investor')
  .catch(e => { console.error(e); process.exit(1); });
