// Distribution notices: one classification + one status, shown together (brand/notices.json, decisions.md Part 10).
const fs = require('fs');
const path = require('path');
const N = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'brand/notices.json')));
function resolveNotice({notice, classification, status, recipient, validity = '30 days', client = 'Ocean RCS'} = {}) {
  if (notice && N.statuses[notice]) status = status || notice;          // legacy: notice: 'draft' | 'specimen'
  else if (notice) classification = classification || notice;
  classification = classification || N.defaults.classification;
  status = status || N.defaults.status;
  const c = N.classifications[classification], s = N.statuses[status];
  if (!c) throw new Error(`Unknown notice ${classification}. Classifications: ${Object.keys(N.classifications).join(', ')}`);
  if (!s) throw new Error(`Unknown notice status ${status}. Statuses: ${Object.keys(N.statuses).join(', ')}`);
  const fill = t => t && t.replace('{recipient}', recipient || client).replace('{validity}', validity);
  return {classification, status, label: [c.label, s.label].filter(Boolean).join(' · '),
    line: [fill(c.line), s.line].filter(Boolean).join(' '), disclaimer: fill(c.disclaimer), required: !!c.requiresDisclaimer,
    withStatus(st) { return resolveNotice({classification, status: st, recipient, validity, client}); }};
}
module.exports = {resolveNotice, NOTICES: N};
