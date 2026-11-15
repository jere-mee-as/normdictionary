import os, sys
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(here, 'shell')); import shell
import build  # reuse the subtitle styling

# Threshold version: one act between one pair, one dial turned step by step.
# Each step: (where the dial is, what happens: corrected / ignored / encouraged / split, what gets said out loud)
# act → pair → dial (with a setup line) → steps

D = [
('Pushing', '✕', [
  ('From a girl to a boy', [
    ('As he gets older', 'A girl pushes a boy off the swing. A parent sees it.', [
      ('He’s 3 years younger', 'corrected', '“We don’t push. Ever.”'),
      ('Same age', 'corrected', '“Hey. Hands to yourself.”'),
      ('He’s 2 years older', 'ignored', 'Nothing.'),
      ('He’s 4 years older', 'encouraged', '“Ha! She got you.”'),
      ('He’s 4 years older and pushes her back', 'corrected', '“You never put your hands on a girl.”'),
    ]),
  ]),
]),
('Joking about weight', '◯', [
  ('From a comedian on stage', [
    ('As the target changes', 'Mid-set, the comedian does a minute on how fat somebody is.', [
      ('Himself', 'encouraged', 'The biggest laugh of the night.'),
      ('A heckler in the front row', 'encouraged', 'Laughter, and “He asked for it.”'),
      ('A senator', 'encouraged', 'Laughter, from half the room.'),
      ('His wife, who’s in the audience', 'ignored', 'Nervous laughter, then nothing.'),
      ('A woman picked at random from the crowd', 'corrected', '“Too far. You don’t comment on anyone’s body.”'),
    ]),
  ]),
]),
('Punching', '!', [
  ('From a stranger to a man on the street', [
    ('As we learn who he is', 'A man walks up to another man and punches him in the face. It’s filmed.', [
      ('Nobody in particular', 'corrected', '“Violence is never the answer.”'),
      ('A wealthy CEO who just laid off 4,000 people', 'split', 'Laughing emojis, and “Violence is never the answer.”'),
      ('A cop in uniform', 'corrected', '“Assault on an officer.” From most of the country.'),
      ('A man wearing a swastika armband', 'split', '“Good.” From one half. “Violence is never the answer,” from the other.'),
      ('A masked antifa protester', 'split', '“Good.” From the other half. “Violence is never the answer,” from the first.'),
      ('A man everyone in town knows is a convicted child molester', 'encouraged', 'Nothing. Maybe a nod.'),
    ]),
  ]),
]),
('Yelling at a kid', '⌂', [
  ('From a mother to her 8-year-old', [
    ('As the audience grows', 'She loses it and screams at him for spilling juice on the couch.', [
      ('Nobody’s home', 'ignored', 'Nothing.'),
      ('Her own mother is visiting', 'ignored', '“He’ll survive. You turned out fine.”'),
      ('In a Target aisle', 'ignored', 'Looks. Nobody says anything.'),
      ('A stranger films it and posts it', 'corrected', '“This is abuse. No child deserves this.” 30,000 times.'),
    ]),
  ]),
]),
('Saying “men are trash”', '∀', [
  ('From a woman', [
    ('As the listener changes', 'She says it, half joking, after a bad week of dates.', [
      ('Her girlfriends at brunch', 'encouraged', '“Literally.”'),
      ('Her boyfriend', 'ignored', '“Lol. Present company excluded, right?”'),
      ('Her 12-year-old son', 'corrected', '“Not in front of him.”'),
      ('Her coworkers, in a meeting', 'corrected', 'HR: “We don’t make generalizations about any group here.”'),
    ]),
  ]),
]),
('Dating someone younger', '♥', [
  ('From a man', [
    ('As the gap grows', 'A man, 40, starts dating someone younger. His friends meet her.', [
      ('She’s 36', 'ignored', 'Nothing.'),
      ('She’s 30', 'ignored', 'Nothing, and one raised eyebrow.'),
      ('She’s 24', 'split', '“Good for you, man.” And, out of earshot, “Midlife crisis.”'),
      ('She’s 21', 'corrected', '“Age gaps like that are always about power.”'),
      ('She’s 21 and he’s a billionaire', 'corrected', 'Aimed at her: “Gold digger.”'),
    ]),
  ]),
  ('From a woman', [
    ('As the gap grows', 'A woman, 40, starts dating someone younger. Her friends meet him.', [
      ('He’s 36', 'ignored', 'Nothing.'),
      ('He’s 30', 'encouraged', '“Get it.”'),
      ('He’s 24', 'encouraged', '“Cougar!” Toasts.'),
      ('He’s 21', 'split', '“Good for her.” And, out of earshot, “What do they even talk about?”'),
      ('He’s 21 and she’s a billionaire', 'ignored', 'Aimed at him, if anyone: “Lucky.”'),
    ]),
  ]),
]),
('Doing an accent', '≈', [
  ('From an American at a party', [
    ('As the accent changes', 'He tells a story and does the voices.', [
      ('British', 'encouraged', 'Laughter.'),
      ('Southern', 'encouraged', 'Laughter.'),
      ('French', 'encouraged', 'Laughter.'),
      ('Russian', 'encouraged', 'Laughter.'),
      ('Indian', 'corrected', '“Not okay. You don’t mock how anyone talks.”'),
      ('Mexican', 'corrected', '“Not okay. You don’t mock how anyone talks.”'),
      ('Chinese', 'corrected', '“Not okay. You don’t mock how anyone talks.”'),
    ]),
  ]),
]),
('Hugging a kid', '◇', [
  ('From an adult to a 7-year-old girl', [
    ('As the adult changes', 'She’s crying after falling off her bike. An adult crouches down and hugs her.', [
      ('A grandmother from down the street', 'encouraged', '“That’s so sweet.”'),
      ('Her female teacher', 'ignored', 'Nothing.'),
      ('Her male teacher', 'corrected', 'The principal: “Side hugs only. We have a no-touch policy for all staff.”'),
      ('A male neighbor, 25', 'corrected', '“Why is he touching her?”'),
      ('A male stranger', 'corrected', 'Someone takes out a phone.'),
    ]),
  ]),
]),
]

def low(s): return s[0].lower() + s[1:]
P = []
for act, sig, pairs in D:
    e = {'n': act, 's': low(act), 'i': sig, 'u': [], 't': []}
    for pair, dials in pairs:
        ix = []
        for dial, setup, steps in dials:
            k = [{'q': f'{at} · {how}', 'f': said, 'c': f'{setup}\n{at}: {said}'} for at, how, said in steps]
            ix.append(len(e['t'])); e['t'].append({'t': dial, 's': low(dial), 'p': setup, 'k': k})
        e['u'].append({'n': pair, 's': low(pair), 't': ix})
    P.append(e)

SUBTXT = ('One act, one dial, turned a notch at a time. Watch where the rule changes, and where the universal words come out. '
          'Below each step is what someone actually says out loud. Observations, not studies.')
SUB = build.SUB.replace(shell.js(build.SUBTXT), shell.js(SUBTXT))
n = shell.build(P, os.path.join(here, '..', 'dials.html'), title='Same rule for…', lead='Same rule for', key='sr',
    words=['act', 'pair', 'dial', 'step'], steps=['act', 'between', 'dial', 'steps'], plurals={}, foot=SUB, theme='ink')
print('dials built', n, sum(len(t['k']) for e in P for t in e['t']), 'steps')
