# Granular version: the same act, by who does it, judged by who it's done to.
# Headword → action (with the rule people say) → who does it → (verdict, who it's done to)
G = [
('Hitting', '✕', [
  ('A slap, in an argument', 'Said: “Never hit anyone.”', [
    ('From a man', [('eyebrows', 'To a man.'), ('not okay', 'To a woman.'), ('not okay', 'To a child.'),
                    ('not okay', 'To his elderly father.'), ('illegal', 'To a cop.')]),
    ('From a woman', [('fine', 'To a man.'), ('eyebrows', 'To a woman.'), ('not okay', 'To a child.'),
                      ('not okay', 'To her elderly mother.'), ('illegal', 'To a cop.')]),
    ('From an 8-year-old', [('laughed at', 'To a grown man.'), ('laughed at', 'To a grown woman.'), ('eyebrows', 'To another 8-year-old.'),
                            ('frowned on', 'To a parent.'), ('frowned on', 'To a grandparent.')]),
    ('From an 85-year-old man', [('laughed at', 'To a grown man.'), ('eyebrows', 'To his nurse.'), ('eyebrows', 'To a woman.'), ('not okay', 'To a child.')]),
  ]),
  ('A punch, in a fight they didn’t start', 'Said: “Violence is never the answer.”', [
    ('From a man', [('fine', 'To a man.'), ('not okay', 'To a teenage boy.'), ('not okay', 'To a woman.'), ('illegal', 'To a cop.')]),
    ('From a woman', [('admired', 'To a man.'), ('fine', 'To a woman.'), ('illegal', 'To a cop.')]),
    ('From a teenage boy', [('admired', 'To a grown man.'), ('fine', 'To another teenage boy.'), ('not okay', 'To a girl.'), ('not okay', 'To a teacher.')]),
  ]),
]),
('Insulting', '≠', [
  ('“You’re an idiot,” to their face', 'Said: “Treat everyone with respect.”', [
    ('From a boss', [('eyebrows', 'To another boss.'), ('not okay', 'To an employee.'), ('not okay', 'To an intern.')]),
    ('From an employee', [('frowned on', 'To a coworker.'), ('not okay', 'To the boss. Fired.')]),
    ('From a parent', [('fine', 'To a referee.'), ('frowned on', 'To their spouse.'), ('not okay', 'To their child.')]),
    ('From a 10-year-old', [('fine', 'To a 15-year-old brother.'), ('frowned on', 'To a 5-year-old brother.'), ('not okay', 'To a parent.'), ('not okay', 'To a teacher.')]),
    ('From a stranger', [('expected', 'To a referee.'), ('fine', 'To a politician, on TV.'), ('not okay', 'To a cashier.'), ('not okay', 'To a waiter.')]),
  ]),
]),
('Joking about', '☺', [
  ('A group, by its stereotype', 'Said: “Don’t stereotype people.”', [
    ('From a comedian, on stage', [('fine', 'About Americans.'), ('fine', 'About the French.'), ('fine', 'About men.'), ('fine', 'About old people.'),
                                   ('fine', 'About rural Southerners.'), ('fine', 'About short men.'), ('fine', 'About white people.'), ('fine', 'About Christians.'),
                                   ('eyebrows', 'About women.'), ('frowned on', 'About fat people.'), ('not okay', 'About Black people.'),
                                   ('not okay', 'About gay people.'), ('not okay', 'About Jews.'), ('not okay', 'About Mexicans.'), ('not okay', 'About Muslims.')]),
    ('From a member of that group, on stage', [('expected', 'About their own group, whichever it is.')]),
    ('From a coworker, at the office', [('fine', 'About boomers.'), ('fine', 'About Gen Z.'), ('fine', 'About lawyers.'), ('fine', 'About millennials.'),
                                        ('eyebrows', 'About Christians.'), ('eyebrows', 'About men.'), ('eyebrows', 'About white people.'),
                                        ('not okay', 'About Black people.'), ('not okay', 'About Muslims.'), ('not okay', 'About women.')]),
  ]),
]),
('Complimenting', '♥', [
  ('“You look great,” from a stranger', 'Said: “Everyone likes a compliment.”', [
    ('From a man', [('fine', 'To a man.'), ('fine', 'To a much older woman.'), ('eyebrows', 'To a woman his age.'), ('not okay', 'To a much younger woman.')]),
    ('From a woman', [('admired', 'To a man.'), ('fine', 'To a much younger man.'), ('fine', 'To a woman.')]),
    ('From an old man', [('fine', 'To a young man.'), ('frowned on', 'To a young woman.')]),
    ('From an old woman', [('admired', 'To a young man. “Cute.”'), ('admired', 'To a young woman.')]),
  ]),
  ('A hand on the lower back, at work', 'Said: “Keep it professional.”', [
    ('From a man', [('eyebrows', 'To a man.'), ('not okay', 'To a woman.')]),
    ('From a woman', [('fine', 'To a woman.'), ('eyebrows', 'To a man.')]),
    ('From a boss', [('not okay', 'To an employee, of any sex.')]),
  ]),
]),
('Hugging', '⊹', [
  ('Someone you barely know', 'Said: “Ask before you touch.”', [
    ('From an old woman', [('admired', 'To a child.'), ('fine', 'To a man.'), ('fine', 'To a woman.')]),
    ('From a woman', [('fine', 'To a child.'), ('fine', 'To a man.'), ('fine', 'To a woman.')]),
    ('From a man', [('eyebrows', 'To a man.'), ('eyebrows', 'To a woman.'), ('not okay', 'To a child.')]),
    ('From a politician', [('fine', 'To a voter.'), ('fine', 'To a voter’s baby.')]),
  ]),
]),
('Yelling', '!', [
  ('In public, red in the face', 'Said: “Use your inside voice.”', [
    ('From a coach', [('expected', 'At a referee.'), ('fine', 'At a player.'), ('eyebrows', 'At a parent.')]),
    ('From a parent', [('fine', 'At a referee.'), ('fine', 'At a teenager.'), ('eyebrows', 'At a toddler.'), ('not okay', 'At a spouse.'), ('not okay', 'At a waiter.')]),
    ('From a customer', [('laughed at', 'At a self-checkout machine.'), ('frowned on', 'At a manager.'), ('not okay', 'At a cashier.')]),
    ('From a protester', [('fine', 'At a politician.'), ('divided', 'At a cop.'), ('frowned on', 'At someone walking by.')]),
  ]),
]),
('Staring', '◉', [
  ('For a long, long time', 'Said: “It’s rude to stare.”', [
    ('From a child', [('fine', 'At a man in a wheelchair.'), ('fine', 'At a stranger.'), ('fine', 'At a woman in a hijab.')]),
    ('From a woman', [('fine', 'At a baby.'), ('fine', 'At a celebrity.'), ('fine', 'At a handsome man.'), ('eyebrows', 'At a woman.'), ('not okay', 'At a man in a wheelchair.')]),
    ('From a man', [('fine', 'At a baby.'), ('fine', 'At a celebrity.'), ('eyebrows', 'At a man.'), ('frowned on', 'At a beautiful woman.'), ('not okay', 'At a man in a wheelchair.')]),
  ]),
]),
('Asking', '?', [
  ('“So when are you having kids?”', 'Said: “It’s just a question.”', [
    ('From a parent', [('expected', 'To their married daughter.'), ('fine', 'To their married son.'), ('eyebrows', 'To their son-in-law.')]),
    ('From a coworker', [('eyebrows', 'To a man.'), ('not okay', 'To a woman.')]),
    ('From a boss', [('frowned on', 'To a man.'), ('illegal', 'To a woman, in a job interview.')]),
  ]),
]),
('Giving', '◈', [
  ('$20, unasked', 'Said: “It’s better to give than to receive.”', [
    ('From a grandparent', [('expected', 'To a grandchild.'), ('fine', 'To a stranger’s child.'), ('fine', 'To a waiter.')]),
    ('From a man', [('admired', 'To a homeless man.'), ('fine', 'To a nephew.'), ('eyebrows', 'To a coworker.'), ('eyebrows', 'To a nurse.'),
                    ('not okay', 'To a stranger’s child.'), ('not okay', 'To a cop.')]),
    ('From a boss', [('fine', 'To an employee, as a bonus.'), ('eyebrows', 'To one employee, in front of the others.')]),
  ]),
]),
('Dating', '∞', [
  ('Someone much younger', 'Said: “Age is just a number.”', [
    ('From a man, 50', [('fine', 'To a man, 35.'), ('fine', 'To a woman, 35.'), ('frowned on', 'To a woman, 25.'), ('not okay', 'To a woman, 19.')]),
    ('From a woman, 50', [('admired', 'To a man, 35.'), ('fine', 'To a woman, 35.'), ('fine', 'To a man, 25.'), ('eyebrows', 'To a man, 19.')]),
    ('From a billionaire, 70', [('eyebrows', 'To a woman, 30. Aimed at her.'), ('eyebrows', 'To a man, 30. Aimed at him.')]),
  ]),
]),
('Swearing', '#', [
  ('At someone, to their face', 'Said: “Watch your language.”', [
    ('From a parent', [('fine', 'At another driver.'), ('frowned on', 'At their spouse.'), ('not okay', 'At their child.')]),
    ('From a coach', [('fine', 'At a player.'), ('fine', 'At a referee.')]),
    ('From a teenager', [('fine', 'At a friend.'), ('frowned on', 'At a sibling.'), ('not okay', 'At a parent.'), ('not okay', 'At a teacher.')]),
  ]),
]),
]
