import os, sys
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(here, 'shell')); import shell

# A norm dictionary. Stated, not judged: what people (US, now) treat as okay to do, and what not.
# Headword (a verb) → what it's done to → entry, with the principle people say out loud → cases.
# A case: (verdict, the case). Verdicts in plain words:
#   expected · admired · fine · eyebrows · laughed at · frowned on · not okay · illegal · divided (the country splits)
# Where law and norm part ways, the case says so.

D = [
('Killing', '✕', [
  ('An animal', [
    ('To eat it', 'Said: “Animals shouldn’t suffer for no reason.”', [
      ('fine', 'A pig, for bacon.'),
      ('fine', 'A lobster, boiled alive.'),
      ('fine', 'A deer, with a rifle, for the freezer.'),
      ('fine', 'A rabbit, hunted in a field.'),
      ('not okay', 'A rabbit from the pet store, for dinner.'),
      ('not okay', 'A horse, for steak.'),
      ('not okay', 'A dog, for anything.'),
    ]),
    ('Because it’s in the way', 'Said: “Every creature has a right to live.”', [
      ('fine', 'Mice in the walls, with poison.'),
      ('fine', 'A mosquito, without a second thought.'),
      ('fine', 'Canada geese near an airport, by the thousand.'),
      ('frowned on', 'A squirrel eating the bird feed.'),
      ('not okay', 'A stray cat in the yard.'),
    ]),
    ('For sport', 'Said: “Killing for fun is sick.”', [
      ('fine', 'A bass, caught and kept.'),
      ('fine', 'A pheasant, shot on a guided hunt.'),
      ('divided', 'A bear, shot over bait.'),
      ('not okay', 'A lion, shot on a paid trophy hunt, then photographed.'),
    ]),
  ]),
  ('A person', [
    ('On purpose', 'Said: “Thou shalt not kill.”', [
      ('admired', 'A soldier, in a war his country is winning.'),
      ('fine', 'A homeowner, shooting an armed intruder.'),
      ('divided', 'A state, executing a convicted murderer.'),
      ('fine', 'A doctor unplugs a dying patient’s ventilator, at their request. Legal everywhere.'),
      ('divided', 'A doctor hands a dying patient pills to take themselves, at their request. Legal in about a dozen states.'),
      ('illegal', 'A doctor gives a dying patient a lethal injection, at their request. Illegal in every state.'),
    ]),
  ]),
]),

('Hitting', '!', [
  ('Another adult', [
    ('In a game', 'Said: “Violence is never the answer.”', [
      ('admired', 'A knockout, in a boxing ring.'),
      ('fine', 'A fistfight, in a hockey game. Five minutes in the box.'),
      ('not okay', 'A punch, in a basketball game. Ejected and suspended.'),
      ('fine', 'A late hit, in football. A flag.'),
      ('illegal', 'A tackle, on the sidewalk after the game.'),
    ]),
    ('Outside a game', 'Said: “Violence is never the answer.”', [
      ('fine', 'Punching someone who swung at you first.'),
      ('admired', 'Punching a bully who’s been after you for months.'),
      ('eyebrows', 'Punching a man who insulted your wife.'),
      ('not okay', 'Punching a man who insulted you.'),
    ]),
  ]),
  ('A child', [
    ('To discipline them', 'Said: “Never hit a child.”', [
      ('divided', 'A parent, spanking their own child.'),
      ('not okay', 'A grandparent, spanking a grandchild.'),
      ('not okay', 'A babysitter, spanking a child in their care.'),
      ('divided', 'A principal, paddling a student. Still legal in public schools in some states.'),
    ]),
  ]),
]),

('Keeping', '◇', [
  ('An animal', [
    ('Confined', 'Said: “Animals deserve to be free.”', [
      ('fine', 'A dog, in a crate overnight.'),
      ('fine', 'A goldfish, in a bowl, for life.'),
      ('fine', 'A hamster, in a cage, for life.'),
      ('fine', 'Thirty thousand chickens, in one barn.'),
      ('frowned on', 'An orca, in a tank, doing tricks.'),
      ('not okay', 'A dog, chained in the yard all day.'),
    ]),
  ]),
]),

('Lying', '≠', [
  ('To people you love', [
    ('To spare them', 'Said: “Honesty is the best policy.”', [
      ('expected', 'Telling a four-year-old Santa is real.'),
      ('expected', '“I love it!” About a gift you’ll return.'),
      ('fine', 'Telling a dying friend he looks good.'),
      ('eyebrows', 'Telling a friend her husband isn’t cheating, when you know he is.'),
      ('not okay', 'Telling your spouse the credit card debt is paid off.'),
    ]),
  ]),
  ('To strangers', [
    ('For an advantage', 'Said: “Liars can’t be trusted.”', [
      ('admired', 'A bluff, at a poker table.'),
      ('fine', '“That’s my final offer.” It isn’t.'),
      ('fine', 'An undercover cop, lying to a suspect for months.'),
      ('eyebrows', 'A man adds two inches to his height on a dating app.'),
      ('not okay', 'A job seeker adds a degree to his résumé.'),
      ('illegal', 'A seller says the used car was never in a crash.'),
    ]),
  ]),
]),

('Selling', '¤', [
  ('Your body', [
    ('Part by part', 'Said: “Your body is not for sale.”', [
      ('fine', 'Your plasma, twice a week, for cash.'),
      ('fine', 'Your hair, to a wig maker.'),
      ('fine', 'Your sperm, to a clinic.'),
      ('fine', 'Your eggs, to a clinic, for $10,000 or more.'),
      ('divided', 'Nine months of your womb, as a paid surrogate.'),
      ('illegal', 'One of your kidneys, to someone who’ll die without it.'),
      ('fine', 'Sex, on camera, for money.'),
      ('illegal', 'Sex, off camera, for money. Almost everywhere in the US.'),
    ]),
  ]),
  ('What people need', [
    ('When they need it most', 'Said: “Don’t take advantage of people.”', [
      ('fine', 'Rides at triple the price, because it’s raining.'),
      ('fine', 'An $8 bottle of water, at a stadium.'),
      ('fine', 'A hotel room at four times the price, the weekend of the big game.'),
      ('illegal', 'A $10 bottle of water, after a hurricane. Price gouging, in most states.'),
      ('divided', 'A loan at 400% a year, to someone who can’t make rent.'),
    ]),
  ]),
]),

('Taking', '⇄', [
  ('From work', [
    ('Little things', 'Said: “Stealing is stealing.”', [
      ('fine', 'Pens and Post-its, home.'),
      ('fine', 'An hour of the workday, on your phone.'),
      ('eyebrows', 'A $15 dinner, padded onto the expense report.'),
      ('not okay', '$15 from the register.'),
    ]),
  ]),
  ('Money you didn’t earn', [
    ('From someone else', 'Said: “You should earn what you have.”', [
      ('fine', 'Ten million dollars, inherited from your parents.'),
      ('admired', 'A hundred million, won on a lottery ticket.'),
      ('divided', 'Welfare, while able to work.'),
      ('divided', 'A billion-dollar subsidy, to a company that could pay its own way.'),
      ('fine', 'A free college ride, for being good at football.'),
    ]),
  ]),
]),

('Betting', '≈', [
  ('Money', [
    ('On chance', 'Said: “Gambling ruins lives.”', [
      ('fine', 'A state lottery ticket. The state runs it.'),
      ('illegal', 'A numbers game, run by a guy in the neighborhood, at lottery-like odds.'),
      ('fine', 'A parlay, on a phone app. Legal in most states, recently.'),
      ('admired', 'Options, on a trading app, if it works out.'),
      ('fine', 'A raffle ticket, at church.'),
    ]),
  ]),
]),

('Showing', '◯', [
  ('Skin', [
    ('In public', 'Said: “Have some decency.”', [
      ('fine', 'A bikini, at the beach.'),
      ('eyebrows', 'Underwear, covering more than a bikini, at the beach.'),
      ('fine', 'A man, shirtless, jogging.'),
      ('not okay', 'A woman, shirtless, jogging. Illegal in some places.'),
      ('fine', 'A nude statue, in a museum, on a school trip.'),
      ('divided', 'Breastfeeding, at a restaurant table.'),
    ]),
  ]),
  ('Tears', [
    ('Where people can see', 'Said: “It’s okay to cry.”', [
      ('admired', 'A man, at his father’s funeral.'),
      ('admired', 'A quarterback, after winning the Super Bowl.'),
      ('eyebrows', 'A man, after losing a pickup basketball game.'),
      ('frowned on', 'Anyone, during a performance review.'),
    ]),
  ]),
]),

('Changing', '⌁', [
  ('Your body', [
    ('On purpose', 'Said: “Love the body you were given.”', [
      ('expected', 'Braces, on a twelve-year-old.'),
      ('fine', 'Pierced ears, on a baby girl.'),
      ('not okay', 'A tattoo, on a baby.'),
      ('fine', 'A full sleeve tattoo, at 30.'),
      ('eyebrows', 'A face tattoo, at 30.'),
      ('fine', 'Testosterone, for a 55-year-old man, from his doctor.'),
      ('illegal', 'Testosterone, for a 25-year-old athlete, from his trainer.'),
      ('fine', 'A weight-loss drug, for someone with diabetes.'),
      ('eyebrows', 'A weight-loss drug, to lose fifteen pounds for a wedding.'),
    ]),
  ]),
  ('Your mind', [
    ('With a substance', 'Said: “Drugs are bad.”', [
      ('expected', 'Coffee, every morning.'),
      ('fine', 'Three glasses of wine, on a Friday.'),
      ('divided', 'A joint, legal in your state.'),
      ('frowned on', 'A cigarette, legal everywhere.'),
      ('fine', 'Adderall, prescribed to you.'),
      ('illegal', 'Adderall, from a friend, before an exam.'),
      ('illegal', 'A line of cocaine, at a party.'),
    ]),
  ]),
]),

('Leaving', '⌂', [
  ('A child alone', [
    ('For a while', 'Said: “Kids need supervision.”', [
      ('fine', 'A 12-year-old, home alone for two hours.'),
      ('fine', 'An 8-year-old, walking to the park alone, in 1985.'),
      ('not okay', 'An 8-year-old, walking to the park alone, today. Sometimes the police come.'),
      ('not okay', 'A 6-year-old, in the car for five minutes while you pay for gas.'),
      ('fine', 'A 6-year-old, in the yard for an hour while you’re inside.'),
    ]),
  ]),
]),

('Loving', '♥', [
  ('Some people more than others', [
    ('Openly', 'Said: “Every life has equal value.”', [
      ('expected', 'Your own kids, more than other people’s kids.'),
      ('not okay', 'One of your kids, more than another.'),
      ('expected', 'Leaving everything to your kids, nothing to strangers who need it more.'),
      ('expected', 'Your country, more than other countries.'),
      ('fine', 'Your dog, more than a stranger.'),
      ('eyebrows', 'Your dog, more than your brother.'),
    ]),
  ]),
]),

('Dating', '∞', [
  ('Someone older', [
    ('By ten years', 'Said: “Age is just a number.”', [
      ('fine', '50 and 60.'),
      ('fine', '30 and 40.'),
      ('eyebrows', '22 and 32.'),
      ('frowned on', '18 and 28.'),
    ]),
  ]),
  ('A relative', [
    ('By marriage, or by blood', 'Said: “Love is love.”', [
      ('fine', 'Your second cousin. Legal everywhere.'),
      ('divided', 'Your first cousin. Legal in about half the states.'),
      ('eyebrows', 'Your late wife’s sister.'),
      ('not okay', 'Your stepsister, raised with you since age five. Legal.'),
    ]),
  ]),
]),

('Mocking', '☺', [
  ('Someone’s looks', [
    ('To their face', 'Said: “Don’t judge people by their looks.”', [
      ('expected', 'A celebrity, at a roast in their honor.'),
      ('fine', 'A friend’s terrible haircut.'),
      ('fine', 'A short man’s height.'),
      ('not okay', 'A coworker’s acne.'),
      ('not okay', 'A woman’s weight.'),
    ]),
  ]),
  ('The dead', [
    ('By how long ago', 'Said: “Don’t speak ill of the dead.”', [
      ('fine', 'A dictator, the day he dies.'),
      ('not okay', 'A beloved actor, the week he dies.'),
      ('fine', 'A beloved actor, fifty years after he dies.'),
      ('fine', 'Any king, any century, on a history podcast.'),
    ]),
  ]),
]),

('Disturbing', '†', [
  ('The dead', [
    ('Their remains', 'Said: “Let the dead rest.”', [
      ('admired', 'Opening a 3,000-year-old tomb, for a museum.'),
      ('illegal', 'Opening a 1950s grave, for a look.'),
      ('fine', 'Strangers’ bodies, preserved and posed, in a ticketed exhibit.'),
      ('not okay', 'Your grandfather’s skeleton, displayed in your living room.'),
      ('fine', 'Your grandfather’s ashes, on the mantel.'),
    ]),
  ]),
  ('The neighbors', [
    ('With noise, at 7 a.m.', 'Said: “Be considerate.”', [
      ('fine', 'A church bell.'),
      ('fine', 'A crying baby.'),
      ('fine', 'A leaf blower, on a Saturday.'),
      ('not okay', 'Your music, as loud as a leaf blower.'),
    ]),
  ]),
]),

('Believing', '☉', [
  ('Something unprovable', [
    ('Out loud', 'Said: “Respect other people’s beliefs.”', [
      ('fine', 'A man rose from the dead.'),
      ('fine', 'A prophet rode a winged horse to heaven.'),
      ('eyebrows', 'Your sign explains your personality.'),
      ('laughed at', 'A galactic ruler brought souls to Earth 75 million years ago.'),
      ('laughed at', 'The moon landing was faked.'),
    ]),
  ]),
  ('For your child', [
    ('Raising them in it', 'Said: “Parents know best.”', [
      ('expected', 'Raising your child in your religion.'),
      ('eyebrows', 'Raising your child vegan.'),
      ('divided', 'Skipping your child’s vaccines, for your beliefs.'),
      ('illegal', 'Refusing your child a blood transfusion, for your beliefs. Courts step in.'),
    ]),
  ]),
]),
]

from more import MORE
from more2 import MORE2
for verb, sig, objs in MORE + MORE2:
    hw = next((x for x in D if x[0] == verb), None)
    if not hw: D.append((verb, sig, objs)); continue
    for obj, entries in objs:
        o = next((x for x in hw[2] if x[0] == obj), None)
        if not o: hw[2].append((obj, entries)); continue
        for en in entries:
            ex = next((x for x in o[1] if x[0] == en[0]), None)
            if ex: ex[2].extend(en[2])
            else: o[1].append(en)

D.sort(key=lambda x: x[0])
VORD = ['expected', 'admired', 'fine', 'laughed at', 'eyebrows', 'divided', 'frowned on', 'not okay', 'illegal']
import re
def ckey(c): return (VORD.index(c[0]), re.sub(r'^[^0-9A-Za-z]+', '', c[1]).lower())
def low(s): return s[0].lower() + s[1:]
from arch import ARCH
import collections
USED = collections.Counter()
P = []
for verb, sig, objs in D:
    e = {'n': verb, 's': low(verb), 'i': sig, 'u': [], 't': []}
    for obj, entries in objs:
        ix = []
        for entry, said, cases in entries:
            k = []
            for v, f in sorted(cases, key=ckey):
                vs = {}
                for ai, (an, _, ov) in enumerate(ARCH):
                    for key, val in ov.items():
                        if f.startswith(key): vs[ai] = VORD.index(val); USED[(ai, key)] += 1
                cp = f'{verb} {low(obj)}, {low(entry)}: '
                k.append({'q': v, 'qd': v, 'qv': VORD.index(v), 'qr': '', 'f': f, 'c': f'{cp}{f} ({v})', 'b': VORD.index(v), 'v': vs, 'cp': cp, 'sk': ckey((v, f))[1]})
            ix.append(len(e['t'])); e['t'].append({'t': entry, 's': low(entry), 'p': said, 'k': k})
        e['u'].append({'n': obj, 's': low(obj), 't': ix})
    P.append(e)

SUBTXT = ('What people in the US, today, treat as okay to do, and what not. Stated, not judged. '
          'Each entry opens with the rule people say out loud. Read down it and look for the rule they actually follow. Bottom left: see it all through someone else’s eyes.')
SUB = ('<style>#outl .okids{margin-left:46px}#outl .okids .okids{margin-left:40px}@media (max-width:760px){#outl .okids{margin-left:34px}#outl .okids .okids{margin-left:12px}}'
       '.fact .q .vd{color:var(--vc)}.vd.v0{--vc:#1d8a43}.vd.v1{--vc:#3a8a2c}.vd.v2{--vc:#5d8a1f}.vd.v3{--vc:#87881a}.vd.v4{--vc:#a6830d}.vd.v5{--vc:#b86d0c}.vd.v6{--vc:#c2560f}.vd.v7{--vc:#c43d1a}.vd.v8{--vc:#b5231e}:root[data-theme=night],:root[data-theme=ink],:root[data-theme=slate],:root[data-theme=phosphor]{--dk:1}:is(:root[data-theme=night],:root[data-theme=ink],:root[data-theme=slate],:root[data-theme=phosphor]) .vd.v0{--vc:#4fd27a}:is(:root[data-theme=night],:root[data-theme=ink],:root[data-theme=slate],:root[data-theme=phosphor]) .vd.v1{--vc:#72d468}:is(:root[data-theme=night],:root[data-theme=ink],:root[data-theme=slate],:root[data-theme=phosphor]) .vd.v2{--vc:#9cd35d}:is(:root[data-theme=night],:root[data-theme=ink],:root[data-theme=slate],:root[data-theme=phosphor]) .vd.v3{--vc:#c6d156}:is(:root[data-theme=night],:root[data-theme=ink],:root[data-theme=slate],:root[data-theme=phosphor]) .vd.v4{--vc:#e6c44e}:is(:root[data-theme=night],:root[data-theme=ink],:root[data-theme=slate],:root[data-theme=phosphor]) .vd.v5{--vc:#f0a646}:is(:root[data-theme=night],:root[data-theme=ink],:root[data-theme=slate],:root[data-theme=phosphor]) .vd.v6{--vc:#f28844}:is(:root[data-theme=night],:root[data-theme=ink],:root[data-theme=slate],:root[data-theme=phosphor]) .vd.v7{--vc:#f06a45}:is(:root[data-theme=night],:root[data-theme=ink],:root[data-theme=slate],:root[data-theme=phosphor]) .vd.v8{--vc:#ee4a4a}@media (prefers-color-scheme:dark){:root:not([data-theme]) .vd.v0{--vc:#4fd27a}:root:not([data-theme]) .vd.v1{--vc:#72d468}:root:not([data-theme]) .vd.v2{--vc:#9cd35d}:root:not([data-theme]) .vd.v3{--vc:#c6d156}:root:not([data-theme]) .vd.v4{--vc:#e6c44e}:root:not([data-theme]) .vd.v5{--vc:#f0a646}:root:not([data-theme]) .vd.v6{--vc:#f28844}:root:not([data-theme]) .vd.v7{--vc:#f06a45}:root:not([data-theme]) .vd.v8{--vc:#ee4a4a}}.subt{color:var(--dim);font-size:17px;line-height:1.45;max-width:34em;margin:-14px 0 30px;font-style:italic}</style>'
       '<script>addEventListener("DOMContentLoaded",()=>{const t=' + shell.js(SUBTXT) + ';["oh","sh"].forEach(id=>{const h=document.getElementById(id);if(!h)return;'
       'const s=document.createElement("div");s.className="subt";s.textContent=t;h.after(s);'
       'const f=()=>{s.style.display=h.textContent.trim().endsWith("…")?"":"none"};f();new MutationObserver(f).observe(h,{childList:true,subtree:true,characterData:true})})})</script>')

for ai, (an, _, ov) in enumerate(ARCH):
    for key in ov: assert USED[(ai, key)] == 1, (an, key, USED[(ai, key)])

# Perspective switch (bottom left): re-labels each case with that perspective's verdict, re-sorts, notes where it parts from most people.
PERSP = ('<style>.foot.persp{display:flex;align-items:baseline;gap:8px;flex-wrap:wrap}.persp select{font:inherit;color:var(--ink);background:transparent;border:0;'
         'border-bottom:1px solid var(--faint);padding:0 2px;cursor:pointer;-webkit-appearance:none;appearance:none}.persp select option{color:#000}'
         '.persp .pd{color:var(--dim);font-style:italic}.fact .q b{font-weight:400;color:var(--ink)}@media (max-width:760px){.persp .pd{display:none}}</style>'
         '<span class="foot persp">Seen by <select id="arch" aria-label="Seen by"></select><span class="pd" id="archd"></span></span>'
         '<script>addEventListener("DOMContentLoaded",()=>{const A=' + shell.js([[a[0], a[1]] for a in ARCH]) + ',V=' + shell.js(VORD) + ';'
         'const S=document.getElementById("arch"),D=document.getElementById("archd");A.forEach((a,i)=>{const o=document.createElement("option");o.value=i;o.textContent=a[0];S.appendChild(o)});'
         'function apply(ai,re){let diff=0;P.forEach(s=>s.t.forEach(t=>{t.k.forEach(k=>{const v=ai in k.v?k.v[ai]:k.b;k._v=v;const d=ai>0&&v!==k.b;if(d)diff++;'
         'k.qv=v;k.qd=V[v];k.qr=d?"  ·  most people: "+V[k.b]:"";k.q=k.qd+k.qr;k.c=k.cp+k.f+" ("+V[v]+(ai>0?", "+A[ai][0].toLowerCase():"")+")"});'
         't.k.sort((a,b)=>a._v-b._v||(a.sk<b.sk?-1:a.sk>b.sk?1:0))}));'
         'D.textContent=A[ai][1]+(ai>0?" "+diff+" cases differ from most people.":"");if(re)["sent","outl","stem"].forEach(m=>{try{MOD[m].filter(QRY)}catch(e){}})}'
         'let ai=0;try{ai=+localStorage.getItem("sr-arch")||0}catch(e){}if(!A[ai])ai=0;S.value=ai;apply(ai,ai>0);'
         'S.onchange=()=>{ai=+S.value;try{localStorage.setItem("sr-arch",ai)}catch(e){}apply(ai,true)}})</script>')

n = shell.build(P, os.path.join(here, '..', 'index.html'), title='Norm Dictionary', lead='So we’re fine with', key='sr',
    words=['headword', 'object', 'entry', 'case'], steps=['verb', 'what', 'entry', 'cases'], plurals={'entry': 'entries'}, foot=SUB + PERSP, theme='ink')
print('built', n, 'bytes;', len(P), 'headwords,', sum(len(e['t']) for e in P), 'entries,', sum(len(t['k']) for e in P for t in e['t']), 'cases')
