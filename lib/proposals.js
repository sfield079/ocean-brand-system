const fs = require('fs');
const path = require('path');
const {APPROVED} = require('./ocean');

const ROOT = path.join(__dirname, '..');
const PROPOSAL_THEMES = JSON.parse(fs.readFileSync(path.join(ROOT, 'surfaces/decks/proposal-themes.json')));
const CLIENT_SAFE_LANGUAGE = JSON.parse(fs.readFileSync(path.join(ROOT, 'brand/client-safe-language.json')));

function assertApprovedPair(name, context) {
  const [field, ink] = String(name).split('-');
  if (!field || !ink || !APPROVED.has([field, ink].sort().join('+'))) {
    throw new Error(`${context || 'Pairing'} uses ${name}, which is not an approved Ocean pairing`);
  }
}

function proposalTheme(name, sectionNames = []) {
  const theme = PROPOSAL_THEMES[name];
  if (!theme) throw new Error(`Unknown proposal theme "${name}". Available: ${Object.keys(PROPOSAL_THEMES).join(', ')}`);
  ['bookend', 'agenda', 'keyNumber'].forEach(role => assertApprovedPair(theme[role], `${name}.${role}`));
  [...theme.sections, ...(theme.dividers || [])].forEach((pair, i) => assertApprovedPair(pair, `${name}.pair[${i}]`));
  for (let i = 1; i < theme.sections.length; i++) {
    if (theme.sections[i] === theme.sections[i - 1]) throw new Error(`${name} repeats adjacent section pairing ${theme.sections[i]}`);
  }
  const sections = Object.fromEntries(sectionNames.map((section, i) => [section, theme.sections[i % theme.sections.length]]));
  const dividers = Object.fromEntries(sectionNames.map((section, i) => [section, (theme.dividers || [])[i % theme.dividers.length] || theme.sections[i % theme.sections.length].split('-').reverse().join('-')]));
  return {...theme, name, close: theme.bookend, sectionPairs: sections, dividerPairs: dividers};
}

function scanClientSafeText(text, {includeSensitiveTools = true, allow = []} = {}) {
  const allowed = allow.map(x => String(x).toLowerCase());
  const rules = [...CLIENT_SAFE_LANGUAGE.blocked, ...(includeSensitiveTools ? CLIENT_SAFE_LANGUAGE.sensitiveTools : [])];
  const hits = [];
  for (const rule of rules) {
    const rx = new RegExp(rule.pattern, 'ig');
    let match;
    while ((match = rx.exec(String(text))) !== null) {
      const found = match[0];
      if (allowed.includes(found.toLowerCase()) || allowed.includes(rule.label.toLowerCase())) continue;
      hits.push({label: rule.label, match: found, index: match.index, reason: rule.reason || 'Sensitive term should be reviewed before client release.'});
    }
  }
  return hits;
}

function assertClientSafeText(text, opts) {
  const hits = scanClientSafeText(text, opts);
  if (hits.length) throw new Error(`Client-facing text contains protected language: ${hits.map(h => `${h.match} (${h.label})`).join(', ')}`);
}

function parseMoney(value) {
  if (typeof value === 'number') return value;
  const s = String(value).trim().replace(/[$,\s]/g, '').toUpperCase();
  const multiplier = s.endsWith('M') ? 1000000 : s.endsWith('K') ? 1000 : 1;
  return Number(s.replace(/[MK]$/, '')) * multiplier;
}

function assertPricingBreakdown({total, categories}) {
  if (!Array.isArray(categories) || categories.length < 2 || categories.length > 4) throw new Error('Pricing breakdown needs 2 to 4 client-facing categories');
  categories.forEach(cat => {
    if (!cat.label || cat.value === undefined) throw new Error('Each pricing category needs label and value');
    assertClientSafeText(cat.label, {includeSensitiveTools: false});
  });
  const expected = parseMoney(total);
  const actual = categories.reduce((sum, cat) => sum + parseMoney(cat.value), 0);
  if (!Number.isFinite(expected) || !Number.isFinite(actual)) throw new Error('Pricing breakdown contains a non-numeric amount');
  if (Math.abs(expected - actual) > Math.max(1, expected * 0.002)) throw new Error(`Pricing categories total ${actual}, not ${expected}`);
}

module.exports = {PROPOSAL_THEMES, CLIENT_SAFE_LANGUAGE, proposalTheme, scanClientSafeText, assertClientSafeText, assertPricingBreakdown, parseMoney};
