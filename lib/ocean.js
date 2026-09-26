// Shared Ocean editorial layouts. All evidence remains native/editable.
const fs = require('fs');
const path = require('path');
const PptxGenJS = require('pptxgenjs');
const opentype = require('opentype.js');
const ROOT = path.join(__dirname, '..');
const BRAND = JSON.parse(fs.readFileSync(path.join(ROOT, 'brand/color-system.json')));
const C = {...BRAND.colors, ...BRAND.tints};
const T = BRAND.typeScale;
const W = 13.333, H = 7.5, M = 0.6, CW = W - M * 2;
const BODY = 2.55, BOTTOM = 6.35;
const FONT = BRAND.fonts.heading;
const faces = Object.fromEntries(['Regular','Bold'].map(weight => [weight,
  opentype.parse(fs.readFileSync(path.join(ROOT, `brand/fonts/StackSansHeadline-${weight}.ttf`)))]));

function wrap(text, width, pt, bold = false) {
  const font = faces[bold ? 'Bold' : 'Regular'];
  const lines = [];
  for (const para of String(text).split('\n')) {
    let line = '';
    for (const word of para.split(/\s+/).filter(Boolean)) {
      if (font.getAdvanceWidth(word, pt) > width * 72)
        throw new Error(`Unbreakable word does not fit: ${word}. Widen the column.`);
      const candidate = line ? `${line} ${word}` : word;
      if (line && font.getAdvanceWidth(candidate, pt) > width * 72) { lines.push(line); line = word; }
      else line = candidate;
    }
    lines.push(line);
  }
  return lines;
}
function count(label, items, max) {
  if (!Array.isArray(items) || !items.length || items.length > max)
    throw new Error(`${label}: requires 1–${max} items. Split the content.`);
}
class OceanDeck {
  constructor({title='Ocean RCS', confidential=true, footer='Ocean RCS', draft=false}={}) {
    this.pptx = new PptxGenJS();
    this.pptx.defineLayout({name:'OCEAN', width:W, height:H});
    this.pptx.layout = 'OCEAN';
    this.pptx.title = title; this.pptx.company = 'Ocean RCS';
    this.pptx.theme = {headFontFace:FONT, bodyFontFace:FONT};
    this.footer = footer; this.confidential = confidential; this.draft = draft; this.n = 0;
  }
  text(s, text, x, y, w, h, {pt=T.body, bold=false, color=C.blackmoss, role='body', align='left'}={}) {
    if (text === undefined || text === null || text === '') return;
    text = String(text);
    if (!this.draft && /\[TBD|\[IMAGE|\[PLACEHOLDER/i.test(text)) throw new Error('Unresolved placeholder in release output');
    // Extra breathing room beyond measured glyph advance; never shrink or split words.
    const lines = wrap(text, w - 0.08, pt, bold);
    if (lines.length * pt * 1.24 / 72 > h - 0.025)
      throw new Error(`Text does not fit ${role}: ${text.slice(0,80)}. Edit or split; do not shrink.`);
    s.addText(lines.join('\n'), {x,y,w,h,fontFace:FONT,fontSize:pt,bold,color,
      margin:0,breakLine:false,valign:'top',align,lineSpacingMultiple:1.12,
      objectName:`ocean:${role}`,paraSpaceAfterPt:0});
  }
  rule(s,x,y,w,color=C.fog) {s.addShape('line',{x,y,w,h:0,line:{color,width:0.7}});}
  logo(s) {
    const logo = path.join(ROOT,'assets/logos/Ocean_LOGO_Horizontal.png');
    if (!fs.existsSync(logo)) throw new Error('Approved horizontal logo missing');
    s.addImage({path:logo,x:M,y:0.52,w:1.5,h:0.32,sizing:{type:'contain',w:1.5,h:0.32},objectName:'ocean:logo'});
  }
  page(notes) {
    const s = this.pptx.addSlide(); this.n++;
    s.background = {color:C.white}; this.logo(s);
    this.rule(s,M,6.87,CW);
    this.text(s,`${this.footer}${this.confidential ? '   Confidential' : ''}${this.draft ? '   Design specimen' : ''}`,
      M,6.98,10,0.2,{pt:10,color:C.cedar,role:'footer'});
    this.text(s,String(this.n).padStart(2,'0'),W-M-0.5,6.98,0.5,0.2,{pt:10,color:C.cedar,role:'footer',align:'right'});
    if(notes) s.addNotes(notes);
    return s;
  }
  head(s,eyebrow,headline) {
    if(eyebrow) this.text(s,eyebrow.toUpperCase(),4,0.58,CW-3.4,0.25,{pt:13,color:C.cedar,role:'label',align:'right'});
    this.text(s,headline,M,1.22,CW,1.15,{pt:T.headline,bold:true,role:'headline'});
  }
  note(s,text) {this.text(s,text,M,6.48,CW,0.3,{pt:10,color:C.cedar,role:'footnote'});}
  image(s,img,x,y,w,h,label) {
    if(img && fs.existsSync(img)) {
      s.addImage({path:img,x,y,w,h,sizing:{type:'cover',w,h},objectName:'ocean:photo'}); return;
    }
    if(!this.draft) throw new Error(`Missing supplied image: ${img || label}`);
    this.rule(s,x,y,w);
    this.text(s,'[IMAGE: supplied photograph required]',x,y+0.2,w,0.7,{pt:13,color:C.cedar,role:'label'});
  }
  cover({title,subtitle,date,image,notes}) {
    const s = this.page(notes);
    const width = image ? 7.2 : CW;
    this.text(s,title,M,2.02,width,2.7,{pt:T.coverTitle,bold:true,role:'cover'});
    this.rule(s,M,4.96,image ? 6.8 : 8.4,C.sage);
    this.text(s,subtitle,M,5.22,width,0.8,{pt:18,color:C.cedar,role:'subhead'});
    this.text(s,date,M,6.3,CW,0.3,{pt:13,color:C.cedar,role:'label'});
    if(image) this.image(s,image,8.6,1.6,4.13,4.8,'Cover photograph');
    return s;
  }
  divider({number,title,subtitle,image,notes}) {
    const s=this.page(notes);
    this.text(s,String(number||1).padStart(2,'0'),M,1.5,2,1.2,{pt:54,bold:true,color:C.sage,role:'metric'});
    this.text(s,title,M,3.1,image?6.8:CW,1.5,{pt:T.dividerTitle,bold:true,role:'headline'});
    this.text(s,subtitle,M,5.05,image?6.8:9.5,1,{pt:18,color:C.cedar,role:'subhead'});
    if(image) this.image(s,image,8.3,1.45,4.43,4.85,'Section photograph');
    return s;
  }
  statement({eyebrow,headline,support,image,notes}) {
    const s=this.page(notes); this.head(s,eyebrow,headline);
    const w=image?5.6:9.4;
    this.rule(s,M,BODY,w,C.sage);
    this.text(s,support,M,BODY+0.4,w,2.8,{pt:24,color:C.cedar,role:'statement'});
    if(image) this.image(s,image,7.25,BODY,5.48,3.8,'Evidence photograph');
    return s;
  }
  twoColumn({eyebrow,headline,left,right,notes}) {
    const s=this.page(notes); this.head(s,eyebrow,headline);
    const w=(CW-0.65)/2;
    [left,right].forEach((col,i)=>{
      const x=M+i*(w+0.65); count(col.label,col.points,3); this.rule(s,x,BODY,w,C.sage);
      this.text(s,col.label,x,BODY+0.25,w,0.5,{pt:20,bold:true,role:'section'});
      col.points.forEach((p,j)=>this.text(s,p,x,BODY+1+j*0.87,w,0.75));
    }); return s;
  }
  pillars({eyebrow,headline,pillars,notes}) {
    count('Pillars',pillars,3); const s=this.page(notes); this.head(s,eyebrow,headline);
    const w=(CW-(pillars.length-1)*0.5)/pillars.length;
    pillars.forEach((p,i)=>{
      const x=M+i*(w+0.5); this.rule(s,x,BODY,w);
      this.text(s,String(i+1).padStart(2,'0'),x,BODY+0.22,w,0.4,{pt:16,color:C.cedar,role:'label'});
      this.text(s,p.title,x,BODY+0.85,w,0.85,{pt:22,bold:true,role:'section'});
      this.text(s,p.text,x,BODY+1.95,w,1.65);
    }); return s;
  }
  metrics({eyebrow,headline,metrics,footnote,notes}) {
    count('Metrics',metrics,4); const s=this.page(notes); this.head(s,eyebrow,headline);
    const w=(CW-0.5*(metrics.length-1))/metrics.length;
    metrics.forEach((m,i)=>{
      const x=M+i*(w+0.5); this.rule(s,x,BODY+0.1,w);
      this.text(s,m.value,x,BODY+0.5,w,1.0,{pt:40,bold:true,role:'metric'});
      this.text(s,m.label,x,BODY+1.75,w,0.9,{bold:true});
      this.text(s,m.note,x,BODY+2.9,w,0.7,{pt:13,color:C.cedar,role:'label'});
    }); this.note(s,footnote); return s;
  }
  timeline({eyebrow,headline,phases,footnote,notes}) {
    count('Phases',phases,5); const s=this.page(notes); this.head(s,eyebrow,headline);
    const w=(CW-0.4*(phases.length-1))/phases.length;
    this.rule(s,M,BODY+0.55,CW,C.sage);
    phases.forEach((p,i)=>{
      const x=M+i*(w+0.4);
      this.text(s,p.label,x,BODY,w,0.4,{pt:13,color:C.cedar,role:'label'});
      this.text(s,p.title,x,BODY+0.95,w,0.85,{pt:20,bold:true,role:'section'});
      this.text(s,p.text,x,BODY+2,w,1.7);
    }); this.note(s,footnote); return s;
  }
  table({eyebrow,headline,header,rows,footnote,notes,colW,appendix=false}) {
    count('Rows',rows,appendix?10:6); const s=this.page(notes); this.head(s,eyebrow,headline);
    const widths=colW||header.map(()=>CW/header.length);
    if(widths.length!==header.length || Math.abs(widths.reduce((a,b)=>a+b,0)-CW)>0.02)
      throw new Error('Table column widths must sum to content width');
    const pt=appendix?13:15;
    const data=[header,...rows];
    const heights=data.map((row,ri)=>{
      if(row.length!==header.length) throw new Error('Table row column count mismatch');
      return Math.max(0.48,...row.map((cell,ci)=>wrap(String(cell),widths[ci]-0.26,pt,ri===0).length*pt*1.24/72+0.18));
    });
    if(heights.reduce((a,b)=>a+b,0)>BOTTOM-BODY) throw new Error('Table too tall; split across pages');
    s.addTable(data.map((row,ri)=>row.map(cell=>({text:String(cell),options:{bold:ri===0,
      color:ri===0?C.white:C.blackmoss,fill:{color:ri===0?C.peacock:C.white}}}))),
      {x:M,y:BODY,w:CW,colW:widths,rowH:heights,fontFace:FONT,fontSize:pt,margin:[0.07,0.12,0.07,0.12],
       border:{type:'solid',color:C.fog,pt:0.5},valign:'middle',autoPage:false,objectName:'ocean:table'});
    this.note(s,footnote); return s;
  }
  chart({eyebrow,headline,type='bar',categories,series,takeaway,footnote,valueFormat='#,##0',notes}) {
    if(!['bar','line'].includes(type)) throw new Error('Supported charts: bar, line');
    count('Series',series,4);
    if(!categories?.length || series.some(sr=>sr.values.length!==categories.length || sr.values.some(v=>!Number.isFinite(v))))
      throw new Error('Chart categories and finite values must match');
    const s=this.page(notes); this.head(s,eyebrow,headline); const cw=takeaway?8:CW;
    s.addChart(this.pptx.ChartType[type],series.map(sr=>({name:sr.name,labels:categories,values:sr.values})),{
      x:M,y:BODY,w:cw,h:3.65,barDir:'col',chartColors:[C.cedar,C.sage,C.peacock,C.sageLight],
      catAxisLabelFontFace:FONT,valAxisLabelFontFace:FONT,legendFontFace:FONT,dataLabelFontFace:FONT,
      catAxisLabelFontSize:13,valAxisLabelFontSize:13,legendFontSize:13,dataLabelFontSize:13,
      catAxisLabelColor:C.blackmoss,valAxisLabelColor:C.blackmoss,legendColor:C.blackmoss,
      dataLabelColor:C.blackmoss,showLegend:series.length>1,legendPos:'b',
      showValue:series.length===1,valAxisLabelFormatCode:valueFormat,
      valGridLine:{color:C.fog,size:0.5},catGridLine:{style:'none'},showBorder:false,
      showCatName:false,lineSize:2,lineDataSymbolSize:5});
    if(takeaway) {this.rule(s,9.15,BODY,3.58,C.sage); this.text(s,takeaway,9.15,BODY+0.3,3.58,3.1,{pt:18,color:C.cedar});}
    this.note(s,footnote); return s;
  }
  caseStudy({eyebrow,headline,image,imageLabel,facts,summary,notes}) {
    count('Facts',facts,4); const s=this.page(notes); this.head(s,eyebrow,headline);
    const x=image?7.25:M,w=image?5.48:CW;
    if(image) this.image(s,image,M,BODY,5.95,3.8,imageLabel);
    facts.forEach((f,i)=>{
      const y=BODY+i*0.67;
      this.text(s,f.label,x,y,w*0.4,0.5,{pt:13,color:C.cedar,role:'label'});
      this.text(s,f.value,x+w*0.43,y,w*0.57,0.5,{pt:17,bold:true}); this.rule(s,x,y+0.56,w);
    });
    this.text(s,summary,x,BODY+facts.length*0.67+0.25,w,1.0,{pt:17}); return s;
  }
  team({eyebrow,headline,people,notes}) {
    count('People',people,3); const s=this.page(notes); this.head(s,eyebrow,headline);
    const w=(CW-0.5*(people.length-1))/people.length;
    people.forEach((p,i)=>{
      const x=M+i*(w+0.5); this.rule(s,x,BODY,w);
      // No supplied headshot means a typographic layout, never a fake avatar.
      if(p.photo) this.image(s,p.photo,x,BODY+0.2,1.0,1.0,'Verified headshot');
      const y=BODY+(p.photo?1.4:0.4);
      this.text(s,p.name,x,y,w,0.85,{pt:22,bold:true,role:'section'});
      this.text(s,p.role,x,y+0.95,w,0.65,{pt:13,color:C.cedar,role:'label'});
      this.text(s,p.bio,x,y+1.75,w,BOTTOM-(y+1.75),{pt:17});
    }); return s;
  }
  ask({eyebrow='Next steps',headline,amount,amountLabel,uses=[],nextSteps=[],notes}) {
    count('Uses',uses,4); count('Next steps',nextSteps,4);
    const s=this.page(notes); this.head(s,eyebrow,headline);
    this.text(s,amount,M,BODY,5.1,1.1,{pt:48,bold:true,role:'metric'});
    this.text(s,amountLabel,M,BODY+1.25,5.1,0.5,{pt:17,color:C.cedar});
    uses.forEach((u,i)=>{
      this.text(s,u.label,M,BODY+2+i*0.45,3.8,0.4,{pt:16});
      this.text(s,u.value,4.5,BODY+2+i*0.45,1.2,0.4,{pt:16,bold:true,align:'right'});
    });
    this.rule(s,7,BODY,5.73,C.sage);
    nextSteps.forEach((st,i)=>this.text(s,`${i+1}. ${st}`,7,BODY+0.35+i*0.82,5.73,0.7));
    return s;
  }
  appendix({title,...args}) {return this.table({...args,eyebrow:'Appendix',headline:title,appendix:true});}
  async save(name) {
    if(!/^[a-z0-9][a-z0-9-]*$/.test(name)) throw new Error('Use a lowercase hyphenated output name');
    const out=path.join(ROOT,'output/pptx',`${name}.pptx`); fs.mkdirSync(path.dirname(out),{recursive:true});
    await this.pptx.writeFile({fileName:out}); console.log(`Saved ${out} (${this.n} slides)`); return out;
  }
}
module.exports={OceanDeck,BRAND,C,T,W,H,M,CW,wrap};
