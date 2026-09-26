// Layout catalog: the shared layouts the recipes do not use, plus the investor notice.
// Design specimen. Figures are illustrative.
const {OceanDeck} = require('../../lib/ocean');
(async () => {
  const d = new OceanDeck({title: 'Ocean RCS layout catalog', draft: true, notice: 'investor', recipient: 'the named investor',
    sections: ['Company', 'Team'], kind: 'Layout catalog', client: 'Ocean RCS'});
  d.cover({kicker: 'Investor briefing', title: 'Layout\nCatalog', date: 'Layout catalog', subtitle: 'Investor name',
    meta: [['Date', '26 Sep 2026'], ['Status', 'Specimen']], pair: 'peacock-honeydew', background: 'environment'});
  d.statement({section: 'Company', eyebrow: '01  Company', headline: 'Emphasis without noise', pair: 'honeydew-cedar',
    support: 'Use **Bold** for the words that carry the point, ==a chip== for the one fact that must pop, and a bottom line for the conclusion.',
    bottomLine: {label: 'Bottom line', text: 'One emphasis device per idea. Never all three on one line.'}});
  d.twoColumn({section: 'Company', eyebrow: '01  Company', headline: 'Presentations and reports\nserve different readers', lede: 'Same brand, different systems.', pair: 'honeydew-cedar',
    left: {label: 'Presentation', points: ['One idea per slide', 'A concise narrative for a **meeting**', 'Editable charts and an appendix']},
    right: {label: 'Report or proposal', points: ['Enough detail to **decide**', 'Flowing text with scope and evidence', 'Readable Letter pages for PDF']}});
  d.team({section: 'Team', eyebrow: '02  Team', headline: 'Credibility comes from\nspecific responsibilities', pair: 'sprig-peacock',
    people: [{name: 'Leadership', role: 'Commercial responsibility', bio: 'Use a verified name, role and concise record of relevant experience.'},
      {name: 'Operations', role: 'Delivery responsibility', bio: 'Explain the work this person owns. Avoid inflated descriptions.'},
      {name: 'Technical', role: 'Technical responsibility', bio: 'Include confirmed qualifications. Use a supplied headshot or none.'}]});
  d.appendix({title: 'Keep useful detail\naccessible', header: ['Record', 'Include', 'Purpose'], colW: [3, 5.5, 3.633],
    rows: [['Source register', 'Document, date and owner', 'Trace each important claim'], ['Assumptions', 'Input, basis and limitation', 'Show what remains uncertain'],
      ['Technical detail', 'Relevant scope and specifications', 'Support diligence'], ['Commercial terms', 'Verified inclusions and exclusions', 'Make boundaries explicit']]});
  d.back();  // adds the investor disclaimer slide automatically, then the close in the cover pairing
  await d.save('ocean-layout-catalog');
})().catch(e => { console.error(e); process.exit(1); });
