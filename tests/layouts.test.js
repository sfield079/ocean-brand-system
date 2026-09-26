const assert=require('node:assert/strict');
const {OceanDeck,wrap,CW}=require('../lib/ocean');
const d=new OceanDeck();
assert.throws(()=>d.cover({title:'[TBD]'}),/placeholder/);
assert.throws(()=>wrap('UnbreakableLongWord',0.2,32),/Unbreakable/);
assert.throws(()=>d.statement({headline:'Test',support:'A lengthy sentence. '.repeat(200)}),/does not fit/);
assert.throws(()=>d.table({headline:'Test',header:['A','B'],rows:[['1','2']],colW:[1,1]}),/widths/);
assert.throws(()=>d.table({headline:'Test',header:['A','B'],rows:[['only one']],colW:[CW/2,CW/2]}),/count/);
assert.throws(()=>d.chart({headline:'Test',categories:['A'],series:[{name:'S',values:[1,2]}]}),/match/);
assert.throws(()=>d.image(d.page(),'missing.jpg',1,2,3,3),/Missing/);
const lines=wrap('A clear statement about evidence',3,17);
assert.ok(lines.length>=1 && lines.join(' ')==='A clear statement about evidence');
console.log('PASS: release placeholders, glyph fit, overflow, table geometry, chart data and missing images');
// Brand-system rules (26 Sep 2026)
const {pairing}=require('../lib/ocean');
assert.throws(()=>pairing('sage-citron'),/not an approved/);
assert.ok(pairing('honeydew-blackmoss').F==='F3FBF8');
const d2=new OceanDeck({draft:true});
d2.keyNumber({kicker:'K',value:'1',text:'Once'});
assert.throws(()=>d2.keyNumber({kicker:'K',value:'2',text:'Twice'}),/Crimson appears once/);
console.log('PASS: approved pairings and one Crimson moment per deck');
// Recipe rules (26 Sep 2026 revision)
{
  const {OceanDeck: D} = require('../lib/ocean');
  const a = new D({draft: true, sections: ['A', 'B']});
  a.cover({title: 'T', pair: 'olive-honeydew'});
  assert.throws(() => a.back({pair: 'sage-honeydew'}), /cover pairing/);
  const b = new D({draft: true, sections: ['A']});
  b.statement({section: 'A', headline: 'H', support: 'S', pair: 'honeydew-peacock'});
  assert.throws(() => b.statement({section: 'A', headline: 'H', support: 'S', pair: 'honeydew-cedar'}), /shares one pairing/);
  assert.throws(() => new D({notice: 'secret'}), /Unknown notice/);
  const c = new D({draft: true, notice: 'investor'});
  c.cover({title: 'T'}); c.back();
  assert.strictEqual(c.log.map(k => k.kind).join(','), 'cover,notice,close');
  assert.strictEqual(c.log[2].pair, c.log[0].pair);
  console.log('PASS: close matches cover, section pairings, notices and investor disclaimer');
}
