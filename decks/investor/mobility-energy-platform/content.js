// Ocean RCS Mobility & Energy Platform investor deck (draft). Wording comes from the deck Ocean leadership
// reviewed on 27 Sep 2026; nothing here is a new claim. Values marked [TBD] need verified figures before release.
// DJI_0482 is a real Ocean project, confirmed by Ocean leadership on 27 Sep 2026.
// Concept imagery remains labeled Representative image. See images/manifest.json.
const path = require('path');
const IMG = f => path.join(__dirname, 'images', f);
module.exports = {
  deck: {title: 'Ocean RCS Mobility & Energy Platform', draft: true, classification: 'investor', status: 'draft',
    kind: 'Investor deck', client: 'Ocean RCS'},
  // Our own section names; each takes the recipe slot in the same position (lib/recipe.js).
  sections: [
    {name: 'Platform', title: 'Connected infrastructure,\ndisciplined capital',
      subtitle: 'Energy, mobility, storage, smart sites and qualified compute share one integration platform.'},
    {name: 'Pipeline', title: 'Parallel lanes,\nprotected stages', subtitle: 'Mobility hubs, parallel pipelines and capital gates.'},
    {name: 'Capital', title: 'Contracted revenue first,\noptionality second',
      subtitle: 'Base-case underwriting depends on customer contracts, site-specific models and confirmed economics.'},
    {name: 'Next steps', title: 'Milestone-based capital', subtitle: 'Mandate, first funded asset and diligence.'},
  ],
  slides: {
    cover: {layout: 'cover', kicker: 'Investor presentation', title: 'Mobility\n& Energy', date: 'Renewable Connected Systems',
      meta: [['Date', '27 Sep 2026'], ['Status', 'Draft']]},
    agenda: {layout: 'agenda', items: [
      {key: 'Platform', title: 'One platform and its revenue logic'},
      {key: 'Pipeline', title: 'Mobility hubs and capital gates'},
      {key: 'Capital', title: 'Underwriting and monetization'},
      {key: 'Next steps', title: 'Milestone-based capital'}]},
    // Platform
    site: {layout: 'caseStudy', section: 'Platform', eyebrow: 'Platform', headline: 'Three systems,\none platform',
      lede: 'Ocean RCS develops infrastructure for electrified mobility, distributed energy and selective modular compute.',
      image: IMG('solar-carport-campus.jpg'), imageLabel: 'Ocean project photo', imageFocus: [0.35, 0.55],
      summary: 'Ocean project photo: solar parking structures, DJI_0482',
      notes: 'Ocean leadership confirmed on 27 Sep 2026 that the supplied drone photo is a real Ocean project. No project size, customer or performance claim is inferred from it.',
      facts: [{label: 'Renewable energy', value: 'Solar, storage, electrical, controls'},
        {label: 'Connected mobility', value: 'Charging, fleet energy, site operations'},
        {label: 'Qualified compute', value: 'Power, fiber, liquid cooling, partners'}]},
    siteData: {layout: 'pillars', section: 'Platform', eyebrow: 'Platform', headline: 'Develop, build\nand operate',
      pillars: [
        {title: 'Develop', text: 'Site screening, utility review and customer strategy.'},
        {title: 'Build', text: 'Solar, storage, EVSE and site infrastructure.'},
        {title: 'Operate', text: 'Monitoring, O&M, billing and reporting. **Ocean controls the integration layer.**'}]},
    // Deployment
    systemPhoto: {layout: 'caseStudy', section: 'Pipeline', eyebrow: 'Pipeline', headline: 'A mobility hub is\nmore than charging',
      lede: 'Site formats can combine energy, mobility, retail, fleet and service revenue.',
      image: IMG('mobility-hub.jpg'), imageLabel: 'Representative image', imageFocus: [0.5, 0.5],
      summary: 'Representative image: infrastructure concept, not an Ocean site.',
      facts: [{label: 'Charging', value: 'Public DC fast charging'}, {label: 'Fleet', value: 'Charging and staging'},
        {label: 'Energy', value: 'Solar canopy and BESS'}, {label: 'Services', value: 'Retail, amenities, wash'}]},
    systemDetail: {layout: 'table', section: 'Pipeline', eyebrow: 'Pipeline', headline: 'Several project lanes\nmove at once',
      lede: 'Ocean does not wait to complete one lane before advancing another.',
      header: ['Lane', 'What governs advancement'], colW: [3.6, 8.533],
      rows: [['Energy EPC', 'Screen · control · validate · fund · build · operate · monetize'],
        ['Third-party EVSE', 'The same evidence-based gates, applied independently'],
        ['Mobility hubs', 'Site readiness'],
        ['Fleet and car wash hubs', 'Customer demand and operating requirements'],
        ['Modular compute', 'Qualified power, fiber and demand']],
      footnote: 'Each asset receives capital only after technical, commercial, utility and financing gates clear.'},
    schedule: {layout: 'timeline', section: 'Pipeline', eyebrow: 'Pipeline', headline: 'Capital is deployed\nin protected stages',
      lede: 'Investor protections and asset-level controls are in place before project funding.',
      phases: [{label: '01 · Control', title: 'Site or customer control', text: 'Secure the site or the customer before spending capital.'},
        {label: '02 · Validate', title: 'Utility and permits', text: 'Confirm the utility path and the permits.'},
        {label: '03 · Approve', title: 'Financing and collateral', text: 'Approve financing and collateral.'},
        {label: '04 · Execute', title: 'Build and operate', text: 'Build, operate and expand.'}],
      footnote: 'Opportunistic equipment: title, condition, serviceability and site fit verified before purchase.'},
    // Investment
    econChart: {layout: 'pillars', section: 'Capital', eyebrow: 'Capital', headline: 'Revenue begins with\ncontracted work',
      pillars: [
        {title: 'Base revenue', text: 'EPC margin, O&M, monitoring, solar and BESS value.'},
        {title: 'Contracted expansion', text: 'Fleet charging, site services and memberships.'},
        {title: 'Optionality', text: 'Advertising, compute and future fleet services. **Excluded from the base case.**'}]},
    econTable: {layout: 'table', section: 'Capital', eyebrow: 'Capital', headline: 'Qualified sites\nrequire evidence',
      lede: 'Physical, utility, commercial and operating conditions must support deployment.',
      header: ['Test', 'Evidence required'], colW: [3.6, 8.533],
      rows: [['Physical site', 'Access, parking, setbacks and a safe service area'], ['Power and utility', 'Load, interconnection and the utility path'],
        ['Commercial demand', 'Charging, fleet, tenant or compute use'], ['Construction scope', 'Civil, electrical and site-cost clarity'],
        ['Operating model', 'O&M, billing, access and support plan']],
      footnote: 'Forward-looking and subject to diligence; not a guarantee of returns.'},
    // Key number: the deck's thesis is disciplined capital. Its one firm, countable figure is the eight
    // portfolio stage gates every opportunity passes before and after funding (ChatGPT draft, slide 9).
    key: {layout: 'keyNumber', kicker: 'Capital', value: '8', text: 'stage gates from origination to monetization',
      meta: [['Basis', 'Portfolio process'], ['Status', 'Draft']],
      notes: 'Gates: originate, screen, control, validate, fund, build, operate, monetize.'},
    // Next steps
    nextSteps: {layout: 'ask', section: 'Next steps', eyebrow: 'Next steps', headline: 'Milestone-based capital',
      lede: 'Monetization follows stabilization: refinance, sell, recapitalize or form joint ventures.',
      amount: '[TBD]', amountLabel: 'Capital sought', uses: [{label: 'First funded asset', value: '[TBD]'}, {label: 'Terms', value: '[TBD]'}],
      nextSteps: ['Confirm investor mandate', 'Define first funded asset', 'Complete diligence package', 'Approve stage-gated capital']},
    notice: {text: 'This presentation is confidential and is provided for discussion purposes only. It is not an offer to sell or a solicitation of an offer to buy any security. Any project, equipment acquisition, incentive, utility service, fleet relationship, charging utilization, compute deployment, financial return or exit transaction is subject to final diligence, written agreements and applicable law.\n\nOcean RCS is the market-facing operating brand for the platform. Project-specific legal entities may be formed at equipment acquisition, property closing, financing or operations launch. Forward-looking statements, projections and estimates are not guarantees. Do not copy, forward or distribute without the written consent of Ocean RCS.'},
    close: {layout: 'back'},
  },
};
