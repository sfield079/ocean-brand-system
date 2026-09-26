// Build a deck of any recipe length from one content file (surfaces/decks/recipes.json, BRAND-SYSTEM.md §8).
// Content supplies slides by id; the recipe supplies order and one pairing per section.
const {OceanDeck, RECIPES} = require('./ocean');

async function buildFromRecipe(content, length, outName) {
  const recipe = RECIPES.recipes[String(length)];
  if (!recipe) throw new Error(`No recipe for ${length} slides. Available: ${Object.keys(RECIPES.recipes).join(', ')}`);
  const roles = RECIPES.roles;
  const ids = recipe.slides;
  const used = ids.map(id => id.startsWith('divider:') ? id.slice(8) : content.slides[id]?.section).filter(Boolean);
  const sections = content.sections.map(sec => sec.name).filter(n => used.includes(n));
  const d = new OceanDeck({...content.deck, sections});
  for (const id of ids) {
    if (id.startsWith('divider:')) {
      const name = id.slice(8), sec = content.sections.find(x => x.name === name);
      const [f, i] = recipe.sections[name].split('-');
      d.divider({number: sections.indexOf(name) + 1, title: sec.title, subtitle: sec.subtitle, section: name, pair: `${i}-${f}`});
      continue;
    }
    const slide = content.slides[id];
    if (!slide) throw new Error(`Content has no slide "${id}" required by the ${length}-slide recipe`);
    const {layout, ...args} = slide;
    if (layout === 'cover') d.cover({...args, pair: roles.bookend, ...(recipe.cover || {})});
    else if (layout === 'back') d.back({notes: args.notes});
    else if (layout === 'agenda') d.agenda({...args, pair: roles.agenda,
      items: args.items.filter(it => sections.includes(it.key))});
    else if (layout === 'keyNumber') d.keyNumber({...args, pair: roles.keyNumber});
    else {
      if (!recipe.sections[args.section]) throw new Error(`Recipe ${length} has no pairing for section ${args.section}`);
      const eyebrow = args.eyebrow && `${String(sections.indexOf(args.section) + 1).padStart(2, '0')}  ${args.eyebrow}`;
      d[layout]({...args, eyebrow, pair: recipe.sections[args.section]});
    }
  }
  return d.save(outName);
}
module.exports = {buildFromRecipe};
