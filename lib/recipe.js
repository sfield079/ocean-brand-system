// Build a deck of any recipe length from one content file (surfaces/decks/recipes.json, BRAND-SYSTEM.md §8).
// Content supplies slides by id; the recipe supplies order and one pairing per section.
// Recipe section names (Site, System, Economics, Next steps) are slots. A content file may use its own
// section names (for example Platform, Deployment, Investment): each takes the slot named in its `slot`
// field, or the slot in the same position.
const {OceanDeck, RECIPES} = require('./ocean');

async function buildFromRecipe(content, length, outName) {
  const recipe = RECIPES.recipes[String(length)];
  if (!recipe) throw new Error(`No recipe for ${length} slides. Available: ${Object.keys(RECIPES.recipes).join(', ')}`);
  const roles = RECIPES.roles;
  const ids = recipe.slides;
  const slots = Object.keys(recipe.sections);
  const slotOf = new Map(content.sections.map((sec, i) => [sec.name, sec.slot || (recipe.sections[sec.name] ? sec.name : slots[i])]));
  const nameOf = slot => content.sections.find(sec => slotOf.get(sec.name) === slot)?.name;
  const pairOf = name => recipe.sections[slotOf.get(name)];
  const used = ids.map(id => id.startsWith('divider:') ? nameOf(id.slice(8)) : content.slides[id]?.section).filter(Boolean);
  const sections = content.sections.map(sec => sec.name).filter(n => used.includes(n));
  const d = new OceanDeck({...content.deck, sections});
  for (const id of ids) {
    if (id.startsWith('divider:')) {
      const slot = id.slice(8), name = nameOf(slot), sec = content.sections.find(x => x.name === name);
      if (!sec) throw new Error(`Content has no section for the ${slot} slot required by the ${length}-slide recipe`);
      const [f, i] = pairOf(name).split('-');
      d.divider({number: sections.indexOf(name) + 1, title: sec.title, subtitle: sec.subtitle, image: sec.image, imageFocus: sec.imageFocus, section: name,
        pair: (recipe.dividers || {})[slot] || `${i}-${f}`});
      continue;
    }
    const slide = content.slides[id];
    if (!slide) throw new Error(`Content has no slide "${id}" required by the ${length}-slide recipe`);
    const {layout, ...args} = slide;
    if (layout === 'cover') d.cover({...args, pair: roles.bookend, ...(recipe.cover || {})});
    else if (layout === 'back') {
      // Optional investor notice text (content.slides.notice); otherwise back() adds the standard one.
      if (content.slides.notice) d.disclaimer({...content.slides.notice, pair: roles.notice});
      d.back({notes: args.notes});
    }
    else if (layout === 'agenda') d.agenda({...args, pair: roles.agenda,
      items: args.items.filter(it => sections.includes(it.key))});
    else if (layout === 'keyNumber') d.keyNumber({...args, pair: recipe.keyNumber || roles.keyNumber});
    else {
      if (!pairOf(args.section)) throw new Error(`Recipe ${length} has no pairing for section ${args.section}`);
      const eyebrow = args.eyebrow && `${String(sections.indexOf(args.section) + 1).padStart(2, '0')}  ${args.eyebrow}`;
      d[layout]({...args, eyebrow, pair: pairOf(args.section)});
    }
  }
  return d.save(outName);
}
module.exports = {buildFromRecipe};
