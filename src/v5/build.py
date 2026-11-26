import json,sys; import os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from shell5 import page4
P=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'normdictionary.json')))
tree=[];units=[]
for gi,g in enumerate(P):
    G={'n':g['n'],'i':g.get('i',''),'items':[]}
    for ai,a in sorted(enumerate(g['u']),key=lambda x:x[1]['n']):
        iid=f'{gi}.{ai}'; G['items'].append({'id':iid,'n':a['n'],'i':a.get('i','')})
        for ti in a['t']:
            s=g['t'][ti]; said=(s.get('p') or '').replace('Said: ','')
            for k in sorted(s['k'],key=lambda k:k['qv']):
                units.append({'it':iid,'g':s['t'],'said':said,'v':k['qv'],'f':k['f'],'mv':k.get('mv',[]),'c':k.get('c',k['f'])})
    tree.append(G)
VD=['expected','admired','fine','laughed at','eyebrows','divided','frowned on','not okay','illegal']
site={'tree':tree,'units':units,'noun':['case','cases'],'VD':VD,'by':'group','PANEL':False,'LINKS':[['Outline view →','outline.html'],['Granular view →','granular.html']],
 'INTRO':'The rule people say, and the one they follow. Hollow dots: groups who disagree (hover a row). Also as an <a href="outline.html">outline</a> and in <a href="granular.html">granular</a> detail.'}
theme=r'''
:root{--bg:#f2ead8;--fg:#251c12;--fg2:#3b2f20;--dim:#6b5b43;--line:#d8c9aa;--line2:#e4d8bf;--acc:#8b1a1a;--hov:#ebe1ca;--sel:#e7d9ba;--hl:#f3d36b;--panel:#f6efe0;--bar:#f2ead8;
--display:"IM Fell English",serif;--text:"EB Garamond",Garamond,serif;--label:"IM Fell English SC","EB Garamond",serif;
--v0:#2f6b3a;--v1:#2f6e55;--v2:#55722b;--v3:#7a6510;--v4:#8f5d10;--v5:#985020;--v6:#8f3f1d;--v7:#86251a;--v8:#560c0c}
body{font-size:16px}#say{font-size:28px}
.gh,.sub,.crumb .c,.hw h3,.hg .hgr h4{font-weight:400;letter-spacing:.03em}
.sub{font-size:16px}.sub i{font-family:var(--text);color:var(--fg2)}
.nr{display:grid;grid-template-columns:minmax(0,1fr) 260px 92px;gap:20px;align-items:center}
.nr .tx{font-size:16px;line-height:1.35}.nr .tip{font-style:italic}.nr .tip em{font-style:italic;color:var(--c)}
.nr .dis{display:block;font-size:13.5px;font-style:italic;color:var(--dim)}.nr .dis em{color:var(--c);font-style:italic}
.sc{position:relative;height:16px;display:grid;grid-template-columns:repeat(9,1fr)}
.sc i{border-left:1px solid var(--line)}.sc i:first-child{border-left:0}
.sc::before{content:"";position:absolute;left:0;right:0;top:50%;border-top:1px solid var(--line)}
.dot{position:absolute;top:50%;width:12px;height:12px;margin:-6px 0 0 -6px;border-radius:50%;background:var(--c);z-index:1}
.dot.o{background:var(--bg);border:1.5px solid var(--c);width:10px;height:10px;margin:-5px 0 0 -5px;z-index:0}
.vw{font:italic 15px var(--text);color:var(--c)}
.cols .nr{font:13px var(--label);color:var(--dim)}
.ax{position:relative;height:16px}.ax span{position:absolute;transform:translateX(-50%);white-space:nowrap}
.rng{display:grid;grid-template-columns:minmax(0,1fr) 260px;gap:20px;align-items:center;padding:8px 0;border-bottom:1px solid var(--line2);width:100%;text-align:left}
.rng:hover{background:var(--hov)}.rng .tx{font-size:15px}.rng .tx i{color:var(--dim)}
.rb{position:absolute;top:50%;height:4px;margin-top:-2px;background:var(--acc);opacity:.35}
@media (max-width:860px){.nr{grid-template-columns:minmax(0,1fr) 120px;row-gap:2px}.nr .vw{grid-column:2;text-align:right}.cols{display:none}.rng{grid-template-columns:1fr}}
'''
js=r'''
const VD=SITE.VD,pos=v=>((v+.5)/9*100)+'%';
SITE.BLOB=u=>[u.g,u.said,u.f,VD[u.v],...u.mv.map(m=>m[0]+' '+m[2])].join(' ');
SITE.GROUP=u=>u.g+' — “'+u.said.replace(/^“|”$/g,'')+'”';
SITE.SAY=(it,u,q)=>q?`Norm Dictionary: “${esc(q)}”`:!it?'Norm Dictionary':`Norm Dictionary: <b>${esc(it.n.toLowerCase())}</b>`;
const scale=(u,extra='')=>`<span class="sc">${VD.map(()=>'<i></i>').join('')}${extra}${u.mv.map(m=>`<span class="dot o" style="left:${pos(m[1])};--c:var(--v${m[1]})" title="${esc(m[0])}: ${esc(m[2])}"></span>`).join('')}<span class="dot" style="left:${pos(u.v)};--c:var(--v${u.v})" title="${VD[u.v]}"></span></span>`;
SITE.COLS=()=>`<div class="cols"><div class="nr"><span></span><span class="ax">${[0,4,8].map(v=>`<span style="left:${pos(v)}">${VD[v]}</span>`).join('')}</span><span></span></div></div>`;
SITE.ROW=(u,Q)=>`<div class="nr"><span class="tx">${hl(u.f,Q)}${cpb(u.c)}${u.mv.length?`<span class="tip">but ${u.mv.map(m=>`${esc(m[0])}: <em style="--c:var(--v${m[1]})">${esc(m[2])}</em>`).join('; ')}</span>`:''}</span>${scale(u)}<span class="vw" style="--c:var(--v${u.v})">${VD[u.v]}</span></div>`;
SITE.FEATURE=()=>{const S2={};SITE.units.forEach(u=>{const k=u.it+'|'+u.g;(S2[k]=S2[k]||{it:u.it,g:u.g,said:u.said,v:[]}).v.push(u)});
 const L=Object.values(S2).map(s=>{const vs=s.v.map(u=>u.v);return {...s,lo:Math.min(...vs),hi:Math.max(...vs)}}).sort((a,b)=>(b.hi-b.lo)-(a.hi-a.lo)).slice(0,10);
 const D=SITE.units.map(u=>({u,d:u.mv.length?Math.max(...u.mv.map(m=>Math.abs(m[1]-u.v))):0})).filter(x=>x.d).sort((a,b)=>b.d-a.d).slice(0,8);
 return `<h3>Where the rule and the practice are furthest apart</h3>${L.map(s=>`<button class="rng" data-id="${s.it}"><span class="tx">${esc(ITEMS[s.it].n)}, <i>${esc(s.g.toLowerCase())}</i>. Said: ${esc(s.said)}</span><span class="sc">${VD.map(()=>'<i></i>').join('')}<span class="rb" style="left:${pos(s.lo)};width:calc(${pos(s.hi)} - ${pos(s.lo)})"></span>${s.v.map(u=>`<span class="dot" style="left:${pos(u.v)};--c:var(--v${u.v})"></span>`).join('')}</span></button>`).join('')}`};
'''
page4('normdictionary','Norm Dictionary','family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=IM+Fell+English&family=IM+Fell+English+SC',theme,site,js)
