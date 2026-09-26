// Starter / reference deck: demonstrates every Ocean layout.
// Copy this folder to decks/<category>/<deck-name>/ and replace the content.
// All numbers below are [TBD] placeholders — never replace them with invented figures.

const path = require("path");
const { OceanDeck } = require("../../lib/ocean");
const A = (p) => path.join(__dirname, "..", "..", "assets", p);

(async () => {
  const d = new OceanDeck({ title: "Ocean RCS — Layout Reference" });

  d.cover({
    title: "Connected infrastructure for commercial sites",
    subtitle: "Ocean RCS — Renewable Connected Systems",
    date: "Investor overview  |  [TBD: month year]",
    image: A("higgsfield-images/cover.jpg"),
    imageLabel: "Higgsfield: aerial commercial energy + mobility hub, late afternoon, 16:9, no text",
    notes: "Cover. Replace image with approved Higgsfield hero visual.",
  });

  d.divider({
    number: 1,
    title: "The opportunity",
    subtitle: "Commercial sites need power, resilience, and charging at the same time.",
    image: A("higgsfield-images/divider-opportunity.jpg"),
    imageLabel: "Higgsfield: commercial rooftop solar at dusk, credible, no neon",
  });

  d.statement({
    eyebrow: "Investment thesis",
    headline: "One qualified site can support several infrastructure revenue streams",
    support: "Solar, storage, EV charging, and electrical upgrades share the same site, interconnection, and customer relationship.",
    image: A("site-photos/hero-site.jpg"),
    imageLabel: "Real Ocean RCS site photo",
  });

  d.twoColumn({
    eyebrow: "Market problem",
    headline: "Commercial owners buy energy infrastructure piecemeal and pay for it twice",
    left: {
      label: "Today",
      points: ["Separate vendors for solar, storage, and charging", "Service upgrades scoped after the fact", "No single owner of performance"],
    },
    right: {
      label: "With Ocean RCS",
      points: ["One EPC integrates the full site stack", "Service and interconnection planned once", "Single accountable delivery partner"],
    },
  });

  d.pillars({
    eyebrow: "Platform",
    headline: "Three integrated service lines built on one electrical core",
    pillars: [
      { title: "Solar + storage", text: "Commercial rooftop and carport solar paired with battery storage for demand and resilience value." },
      { title: "EV charging + mobility", text: "DC fast and Level 2 charging for fleets, retail sites, and public mobility hubs." },
      { title: "Connected infrastructure", text: "Electrical upgrades, water systems, and selective modular compute where power already exists." },
    ],
  });

  d.metrics({
    eyebrow: "Traction",
    headline: "Execution capacity already in place",
    metrics: [
      { value: "[TBD]", label: "MW installed or under contract", note: "Source: approved-metrics.md" },
      { value: "[TBD]", label: "Active commercial proposals", note: "As of [TBD]" },
      { value: "[TBD]", label: "Charging ports deployable", note: "Subject to diligence" },
    ],
    footnote: "All figures to be populated from source/approved-metrics.md only.",
  });

  d.timeline({
    eyebrow: "Deployment roadmap",
    headline: "A staged rollout that de-risks capital at every gate",
    phases: [
      { label: "Phase 1", title: "Qualify sites", text: "Roof, service, and interconnection screening before capital commitment." },
      { label: "Phase 2", title: "Anchor projects", text: "Deliver solar + storage on the strongest sites first." },
      { label: "Phase 3", title: "Add charging", text: "Layer EV charging where utility capacity and incentives are confirmed." },
      { label: "Phase 4", title: "Scale platform", text: "Replicate the site model across the regional pipeline." },
    ],
    footnote: "Timing illustrative; to be validated per site.",
  });

  d.table({
    eyebrow: "Why Ocean wins",
    headline: "Integrated delivery beats a stack of single-product vendors",
    header: ["Capability", "Ocean RCS", "Single-product installer", "Utility program"],
    colW: [3.2, 2.98, 2.98, 2.973],
    rows: [
      ["Solar + storage design", "Yes", "Partial", "No"],
      ["EV charging deployment", "Yes", "Rarely", "Incentives only"],
      ["Service upgrade and interconnection", "Yes", "Subcontracted", "Utility-side only"],
      ["Single point of accountability", "Yes", "No", "No"],
    ],
    footnote: "Illustrative comparison; validate against named competitors before external use.",
  });

  d.chart({
    eyebrow: "Platform economics",
    headline: "Revenue layers stack as each site matures",
    type: "bar",
    categories: ["Year 1", "Year 2", "Year 3", "Year 4", "Year 5"],
    series: [
      { name: "Solar + storage", values: [1, 2, 3, 4, 5] },
      { name: "EV charging", values: [0, 1, 2, 3, 4] },
    ],
    takeaway: "Illustrative only. Replace with approved model outputs before any external use.",
    footnote: "ILLUSTRATIVE — placeholder values, not a forecast.",
  });

  d.caseStudy({
    eyebrow: "Commercial proof",
    headline: "[TBD: project name] — solar, TPO roof, and storage",
    image: A("site-photos/case-study.jpg"),
    imageLabel: "Real project photo",
    facts: [
      { label: "Location", value: "[TBD]" },
      { label: "System size", value: "[TBD] kWdc" },
      { label: "Storage", value: "[TBD] kWh" },
      { label: "Status", value: "[TBD]" },
    ],
    summary: "Only publish once facts are confirmed in source/project-facts.md.",
  });

  d.team({
    eyebrow: "Team",
    headline: "Field-proven operators who build what they sell",
    people: [
      { name: "[TBD: Name]", role: "FOUNDER & CEO", bio: "[TBD: two-line verified bio]" },
      { name: "[TBD: Name]", role: "ENGINEERING", bio: "[TBD: two-line verified bio]" },
      { name: "[TBD: Name]", role: "OPERATIONS", bio: "[TBD: two-line verified bio]" },
    ],
  });

  d.ask({
    headline: "Capital to convert a qualified pipeline into operating assets",
    amount: "[TBD]",
    amountLabel: "Target raise",
    uses: [
      { label: "Project equipment", value: "[TBD]%" },
      { label: "Site development", value: "[TBD]%" },
      { label: "Working capital", value: "[TBD]%" },
    ],
    nextSteps: ["Review qualified site pipeline", "Confirm diligence data room access", "Agree on term-sheet timeline"],
  });

  d.appendix({
    title: "Equipment summary",
    header: ["Component", "Description", "Manufacturer / SKU", "Compliance"],
    colW: [2.4, 4.0, 3.2, 2.533],
    rows: [
      ["Modules", "[TBD]", "[TBD]", "[TBD: FEOC / domestic content]"],
      ["Inverters", "[TBD]", "[TBD]", "[TBD]"],
      ["Battery storage", "[TBD]", "[TBD]", "[TBD]"],
      ["DC fast chargers", "[TBD]", "[TBD]", "[TBD]"],
    ],
    footnote: "Detailed SKUs live in the appendix only. No internal margins.",
  });

  await d.save("ocean-layout-reference");
})().catch((e) => {
  console.error(e.message);
  process.exit(1);
});
