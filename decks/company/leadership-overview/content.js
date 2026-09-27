// Source: Ocean_RCS_Company_Leadership_Overview_Redesigned.pdf supplied 27 Sep 2026.
// Source page references are retained in notes. Draft preserves supplied leadership claims;
// no independent credential verification is implied. Shared layouts only.
const path = require('path');
const PHOTO = path.join(__dirname, '../../investor/mobility-energy-platform/images/solar-carport-campus.jpg');
module.exports = {
  deck: {title: 'Ocean RCS Company & Leadership Overview', draft: true,
    classification: 'confidential', status: 'draft', kind: 'Company overview', client: 'Ocean RCS'},
  sections: [{name: 'Platform'}, {name: 'Team'}, {name: 'Partners'}, {name: 'Contact'}],
  slides: {
    cover: {layout: 'cover', kicker: 'Company overview', title: 'Company &\nLeadership',
      date: 'Renewable Connected Systems', meta: [['Date', '27 Sep 2026'], ['Status', 'Draft']],
      notes: 'Source PDF page 1. Ocean RCS means Renewable Connected Systems.'},
    agenda: {layout: 'agenda', items: [
      {key: 'Platform', title: 'Services and operating model'}, {key: 'Team', title: 'Leadership and responsibilities'},
      {key: 'Partners', title: 'Specialist execution network'}, {key: 'Contact', title: 'Company contact details'}]},
    site: {layout: 'caseStudy', section: 'Platform', eyebrow: 'Platform', headline: 'Connected infrastructure,\none commercial layer',
      lede: 'Four operating pillars share commercial strategy and execution standards.',
      image: PHOTO, imageFocus: [0.35, 0.55], imageLabel: 'Ocean project photo',
      summary: 'Ocean project photo: solar parking structures, DJI_0482',
      facts: [{label: 'Energy', value: 'Solar, storage, electrical, controls'},
        {label: 'Mobility', value: 'EV charging, fleets, smart sites'},
        {label: 'Water', value: 'Treatment, wells, conservation'},
        {label: 'Compute', value: 'Power, fiber, cooling, partners'}],
      notes: 'Source page 2. Energy includes efficiency. Water includes atmospheric water. Compute is partner-enabled deployment, not hyperscale development. DJI_0482 confirmed by Ocean leadership as a real Ocean project.'},
    siteData: {layout: 'pillars', section: 'Platform', eyebrow: 'Operating model', headline: 'Develop, build\nand operate',
      lede: 'A lean core team coordinates AI-enabled operations and specialist partners.',
      pillars: [{title: 'Develop', text: 'Commercial strategy, customer relationships and project integration.'},
        {title: 'Build', text: 'Qualified partners support licensed and project-specific execution.'},
        {title: 'Operate', text: 'Ocean retains standards and accountability across the operating model.'}],
      notes: 'Source pages 2-3. The fourth operating function, Integrate, connects strategy, standards and accountability across these three stages.'},
    systemPhoto: {layout: 'team', section: 'Team', eyebrow: 'Leadership', headline: 'Commercial, operating\nand technical leadership',
      people: [
        {name: 'Stansfield Thomas', role: 'Founder', bio: 'Leads strategy, commercial development, partnerships, capital relationships and market expansion. Background spans technology commercialization, direct sales, connected technologies, operations, marketing and renewable-energy financial strategy.'},
        {name: 'Sierra Zymola', role: 'Director of Operations', bio: 'Supports organizational strategy, executive operations, communications, project coordination and stakeholder alignment across energy, construction, water and infrastructure initiatives.'},
        {name: 'Mark Greene', role: 'Electrical director', bio: 'Director of Electrical & Infrastructure. Master Electrician with 30+ years in commercial and industrial electrical systems, renewables, EV charging, fiber, data-center infrastructure, commissioning and field delivery.'}],
      notes: 'Source pages 4-5. Names, titles, credential and experience are supplied claims retained for Ocean approval. No stock or generated portraits.'},
    systemDetail: {layout: 'caseStudy', section: 'Team', eyebrow: 'Execution', headline: 'Ocean retains\nproject accountability',
      lede: 'Specialists support delivery within Ocean commercial and operating standards.',
      image: PHOTO, imageFocus: [0.65, 0.5], imageLabel: 'Ocean project photo',
      summary: 'Ocean project photo: DJI_0482; no performance figures inferred',
      facts: [{label: 'Commercial', value: 'Customer relationship and strategy'},
        {label: 'Integration', value: 'Project coordination and standards'},
        {label: 'Execution', value: 'Qualified specialist partners'}],
      notes: 'Source pages 2, 3 and 6. Same verified project photograph reused for continuity, with a different crop.'},
    econChart: {layout: 'table', section: 'Partners', eyebrow: 'Partners', headline: 'Specialist support\nfor project execution',
      header: ['Function', 'Support'], colW: [3.6, 8.533],
      rows: [['Legal / risk', 'Counsel, insurance and risk specialists'], ['Finance / tax', 'CPA, controller and incentive professionals'],
        ['Engineering', 'Licensed engineering partners'], ['Construction', 'Contractors, trades and commissioning resources'],
        ['Technology', 'EV, storage, water, fiber and controls partners'], ['Capital', 'Investors, lenders and strategic capital']],
      notes: 'Source page 6. These are support categories, not representations of signed partner agreements.'},
    key: {layout: 'keyNumber', kicker: 'Platform', value: '4', text: 'operating pillars share one integration layer',
      meta: [['Basis', 'Operating model'], ['Status', 'Draft']],
      notes: 'Source page 2: Energy, Mobility, Water and Compute. The figure counts supplied categories, not projects or customers.'},
    nextSteps: {layout: 'twoColumn', section: 'Contact', eyebrow: 'Contact', headline: 'Company contact\n& capabilities',
      left: {label: 'Company', points: ['www.oceanrcs.com', 'info@oceanrcs.com']},
      right: {label: 'Capabilities', points: ['Energy, mobility and water', 'Construction and qualified compute']},
      notes: 'Source page 7. Contact information retained from the supplied PDF.'},
    close: {layout: 'back'}
  }
};
