// Design specimen, not a statement of Ocean's commercial performance.
// Shows every shared layout in the approved Ocean brand system. Images are AI-generated representative images.
const path = require('path');
const {OceanDeck} = require('../../lib/ocean');
const IMG = f => path.join(__dirname, '../../assets/images', f);
(async () => {
  const d = new OceanDeck({title: 'Ocean RCS brand system', draft: true, confidential: false,
    sections: ['Site', 'System', 'Economics', 'Next steps'], kind: 'Layout reference', client: 'Ocean RCS'});
  d.cover({kicker: 'Commercial energy', title: 'Rooftop Solar\n+ Storage', date: 'Layout reference',
    subtitle: 'Client name', meta: [['Date', '26 Sep 2026'], ['Status', 'Specimen']]});
  d.agenda({items: [{key: 'Site', title: 'What the roof and service can carry'}, {key: 'System', title: 'Solar, storage and interconnection'},
    {key: 'Economics', title: 'Savings, incentives and payback'}, {key: 'Next steps', title: 'Decisions and schedule'}]});
  d.divider({number: 1, title: 'Clarity starts with the site', subtitle: 'Roof, structure, service and the constraints that shape the array.'});
  d.caseStudy({section: 'Site', eyebrow: '01  Site', headline: 'The roof can carry about\n412 kW of solar', lede: 'A new TPO roof, clear array zones and an existing 2,000 A service.',
    image: IMG('rooftop.jpg'), imageLabel: 'Representative image', summary: 'Representative image of a comparable rooftop array.',
    facts: [{label: 'Array size', value: '412 KW DC'}, {label: 'Usable roof', value: '68,400 FT²'}, {label: 'Service', value: '2,000 A · 480 V'}]});
  d.statement({section: 'Site', eyebrow: '01  Site', headline: 'The evidence leads the page', image: IMG('worker.jpg'),
    support: 'Make the important information easy to find. Scale, spacing and one clear hierarchy guide the reader.'});
  d.twoColumn({section: 'System', eyebrow: '02  System', headline: 'Presentations and reports\nserve different readers', lede: 'Same brand, different systems.',
    left: {label: 'Presentation', points: ['One idea per slide', 'A concise narrative for a meeting', 'Editable charts and an appendix']},
    right: {label: 'Report or proposal', points: ['Enough detail to make a decision', 'Flowing text with scope and evidence', 'Readable Letter pages for PDF']}});
  d.pillars({section: 'System', eyebrow: '02  System', headline: 'One system with room\nfor the content', lede: 'Typography, color and evidence work together.',
    pillars: [{title: 'Typography', text: 'Stack Sans Headline in four weights sets the hierarchy.'},
      {title: 'Color', text: 'One approved pairing per slide. Crimson appears once per deck.'},
      {title: 'Evidence', text: 'Tables, charts and real photographs explain something specific.'}]});
  d.metrics({section: 'System', eyebrow: '02  System', headline: 'Key figures sit in\nchamfered tiles', lede: 'Light numbers, caps keys, counting diamonds.',
    metrics: [{value: '412 kW', label: 'Array size', note: 'After keep-outs'}, {value: '1.2 MWh', label: 'Storage', note: 'Two cabinets'},
      {value: '2,000 A', label: 'Service', note: 'To be confirmed'}, {value: '100 days', label: 'Schedule', note: 'From notice to proceed'}],
    footnote: 'Illustrative figures · specimen'});
  d.timeline({section: 'System', eyebrow: '02  System', headline: 'A repeatable path from\nbrief to handover',
    phases: [{label: '01 · Brief', title: 'Define the decision', text: 'Identify the audience and the evidence needed.'},
      {label: '02 · Design', title: 'Build the system', text: 'Engineer the array, storage and service.'},
      {label: '03 · Verify', title: 'Commission on site', text: 'Test, torque and log every cabinet.'},
      {label: '04 · Deliver', title: 'Hand over', text: 'Provide records, training and support.'}]});
  d.keyNumber({kicker: '03  Economics', value: '38%', text: 'Lower grid electricity spend from the first year',
    meta: [['Basis', '12-month interval data'], ['Status', 'Illustrative']]});
  d.chart({section: 'Economics', eyebrow: '03  Economics', headline: 'Savings grow each year\nas utility rates rise', lede: 'Annual bill savings, years 1–10, $K. Year 10 highlighted.',
    categories: ['Y01', 'Y02', 'Y03', 'Y04', 'Y05', 'Y06', 'Y07', 'Y08', 'Y09', 'Y10'],
    series: [{name: 'Annual savings', values: [62, 66, 70, 75, 79, 84, 88, 93, 98, 104]}],
    takeaway: '10-year total $819K. Payback 6.4 years.', footnote: 'Illustrative figures · specimen'});
  d.table({section: 'Economics', eyebrow: '03  Economics', headline: 'System summary and\nopen items',
    header: ['Item', 'Specification', 'Status'], colW: [3.4, 5.2, 3.533],
    rows: [['Solar array', '412 kW DC', 'Confirmed layout'], ['Battery storage', '1.2 MWh', 'Pending utility'], ['Interconnection', '2,000 A line-side tap', 'Application due'], ['Roof', 'New TPO, 20-year warranty', 'Complete']],
    footnote: 'Illustrative figures · specimen'});
  d.team({section: 'Next steps', eyebrow: '04  Next steps', headline: 'Credibility comes from\nspecific responsibilities',
    people: [{name: 'Leadership', role: 'Commercial responsibility', bio: 'Use a verified name, role and concise record of relevant experience.'},
      {name: 'Operations', role: 'Delivery responsibility', bio: 'Explain the work this person owns. Avoid inflated descriptions.'},
      {name: 'Technical', role: 'Technical responsibility', bio: 'Include confirmed qualifications. Use a supplied headshot or none.'}]});
  d.ask({section: 'Next steps', eyebrow: '04  Next steps', headline: 'Close with the decision\nand its next steps', amount: '[TBD]', amountLabel: 'Verified project amount',
    uses: [{label: 'Approved scope', value: '[TBD]'}, {label: 'Terms', value: '[TBD]'}],
    nextSteps: ['Review the evidence', 'Resolve open assumptions', 'Confirm the agreed next action'],
    notes: 'Draft layout placeholder. Release mode blocks unresolved values.'});
  d.appendix({section: 'Next steps', title: 'Keep useful detail\naccessible', header: ['Record', 'Include', 'Purpose'], colW: [3, 5.5, 3.633],
    rows: [['Source register', 'Document, date and owner', 'Trace each important claim'], ['Assumptions', 'Input, basis and limitation', 'Show what remains uncertain'],
      ['Technical detail', 'Relevant scope and specifications', 'Support diligence'], ['Commercial terms', 'Verified inclusions and exclusions', 'Make boundaries explicit']]});
  d.back();
  await d.save('ocean-layout-reference');
})().catch(e => { console.error(e); process.exit(1); });
