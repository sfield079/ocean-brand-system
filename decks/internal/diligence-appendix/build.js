// Content only; all layout and rendering comes from the approved shared builders.
const {buildFromRecipe} = require('../../../lib/recipe');
buildFromRecipe(require('./content'), '10', 'ocean-internal-diligence-appendix')
  .catch(e => { console.error(e); process.exit(1); });
