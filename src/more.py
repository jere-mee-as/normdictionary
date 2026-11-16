# Round two. Same shape as D in build.py; merged in by headword and object.
MORE = [
('Killing', '✕', [
  ('An animal', [
    ('To end its suffering', 'Said: “Life is sacred.”', [
      ('expected', 'A horse with a shattered leg, at the track.'),
      ('fine', 'Your 15-year-old dog, at the vet, with you holding him.'),
      ('fine', 'A healthy shelter cat nobody adopted, after enough weeks.'),
      ('not okay', 'Your healthy dog, because you’re moving to an apartment.'),
    ]),
  ]),
  ('A person', [
    ('Without meaning to', 'Said: “A life is a life.”', [
      ('illegal', 'A drunk driver hits and kills a pedestrian. Years in prison.'),
      ('frowned on', 'A sober driver, texting, hits and kills a pedestrian. Often probation.'),
      ('fine', 'A sober driver, not texting, hits and kills a pedestrian. Usually no charges.'),
      ('fine', 'A surgeon’s mistake kills a patient. A settlement, paid by insurance.'),
    ]),
  ]),
]),
('Hitting', '!', [
  ('An animal', [
    ('To make it obey', 'Said: “Never hit an animal.”', [
      ('fine', 'A jockey whips a racehorse down the final stretch. There are rules on how many times.'),
      ('fine', 'A rider spurs a bucking bronco, at a rodeo.'),
      ('frowned on', 'A rolled-up newspaper, to a puppy that peed on the rug. Normal a generation ago.'),
      ('not okay', 'A kick, to your dog, for barking.'),
    ]),
  ]),
]),
('Keeping', '◇', [
  ('A secret', [
    ('From someone close', 'Said: “Secrets destroy trust.”', [
      ('expected', 'A surprise party, from your wife, for a month.'),
      ('expected', 'A friend’s diagnosis, from everyone, because she asked.'),
      ('fine', 'Your salary, from your friends.'),
      ('eyebrows', 'Your salary, from your spouse.'),
      ('divided', 'An adoption, from the adopted child.'),
      ('not okay', 'A pregnancy, from the father.'),
    ]),
  ]),
]),
('Lying', '≠', [
  ('To children', [
    ('For their own good', 'Said: “Don’t lie to kids.”', [
      ('expected', 'The tooth fairy pays a dollar a tooth.'),
      ('fine', 'The old dog went to live on a farm.'),
      ('fine', '“This won’t hurt a bit.” Before a shot.'),
      ('eyebrows', 'Daddy’s away on a long work trip. He’s in prison.'),
    ]),
  ]),
  ('To the government', [
    ('On paperwork', 'Said: “Follow the rules.”', [
      ('fine', 'Rounding up the business miles on your taxes.'),
      ('divided', 'Using grandma’s address to get into a better school district.'),
      ('eyebrows', 'Cash tips, never reported.'),
      ('not okay', 'A dead parent’s Social Security checks, still cashed.'),
    ]),
  ]),
]),
('Selling', '¤', [
  ('Your time', [
    ('For less than minimum wage', 'Said: “Everyone deserves a fair wage.”', [
      ('fine', 'An unpaid internship, at a magazine in New York.'),
      ('illegal', 'An unpaid “internship,” at a restaurant, washing dishes.'),
      ('fine', 'A waiter, for $2.13 an hour plus tips. Legal under federal law.'),
      ('fine', 'A 13-year-old, babysitting for $10 an hour.'),
      ('admired', 'A volunteer firefighter, for nothing.'),
    ]),
  ]),
  ('Your vote', [
    ('Or your influence', 'Said: “Democracy isn’t for sale.”', [
      ('illegal', '$20, for your vote.'),
      ('fine', 'A free ride to the polls, from a campaign that hopes you’ll vote for it.'),
      ('fine', '$20 million in ads, for a candidate, from one donor.'),
      ('fine', 'A $500,000 speaking fee, for a former senator.'),
    ]),
  ]),
]),
('Taking', '⇄', [
  ('From a business', [
    ('Without paying', 'Said: “Stealing is stealing.”', [
      ('fine', 'A fistful of ketchup packets.'),
      ('fine', 'The hotel shampoo.'),
      ('eyebrows', 'The hotel towels.'),
      ('fine', 'A second free sample, at Costco.'),
      ('divided', 'A pirated movie.'),
      ('not okay', 'A candy bar, in your pocket.'),
    ]),
  ]),
  ('Credit', [
    ('For someone else’s work', 'Said: “Give credit where it’s due.”', [
      ('expected', 'A CEO, for a record quarter.'),
      ('fine', 'A president, for a speech a speechwriter wrote.'),
      ('fine', 'A celebrity, for a memoir a ghostwriter wrote.'),
      ('fine', 'A professor, first author on a paper her student wrote.'),
      ('divided', 'A student, for an essay an AI wrote.'),
      ('not okay', 'A student, for an essay his roommate wrote.'),
    ]),
  ]),
]),
('Betting', '≈', [
  ('On people', [
    ('On their lives', 'Said: “Don’t profit from tragedy.”', [
      ('expected', 'A life insurance policy, on your spouse.'),
      ('fine', 'A life insurance policy, on your employees, paid to the company. Legal; often they don’t know.'),
      ('fine', 'Fantasy football, where an injured star costs you the week.'),
      ('not okay', 'An office pool, on which month grandma dies.'),
    ]),
  ]),
]),
('Showing', '○', [
  ('Wealth', [
    ('Where people can see', 'Said: “Don’t flaunt it.”', [
      ('admired', 'A sports car, if you built the company.'),
      ('fine', 'A big diamond, on an engagement ring.'),
      ('eyebrows', 'A sports car, if your father built the company.'),
      ('frowned on', 'Stacks of cash, on Instagram.'),
      ('not okay', 'A Rolex, at a fundraiser for the homeless.'),
    ]),
  ]),
  ('Affection', [
    ('In public', 'Said: “Get a room.”', [
      ('fine', 'Holding hands, anywhere.'),
      ('admired', 'A long kiss, at the airport arrivals gate.'),
      ('eyebrows', 'A long kiss, on a morning train.'),
      ('not okay', 'A long kiss, at a funeral.'),
    ]),
  ]),
]),
('Changing', '⌁', [
  ('Your name', [
    ('When you marry, move or perform', 'Said: “Be proud of where you come from.”', [
      ('expected', 'A woman, taking her husband’s last name.'),
      ('eyebrows', 'A man, taking his wife’s last name.'),
      ('fine', 'An actor, picking a stage name.'),
      ('divided', 'An immigrant, anglicizing his name to get callbacks.'),
      ('fine', 'Anyone, giving a fake name at Starbucks.'),
    ]),
  ]),
]),
('Leaving', '⌂', [
  ('A spouse', [
    ('For a reason', 'Said: “Marriage is for life.”', [
      ('fine', 'After they cheated.'),
      ('fine', 'After twenty years of being unhappy.'),
      ('eyebrows', 'After they gained sixty pounds.'),
      ('divided', 'For someone younger.'),
      ('not okay', 'After their cancer diagnosis.'),
    ]),
  ]),
  ('A job', [
    ('Or a worker', 'Said: “Loyalty matters.”', [
      ('fine', 'Quitting for a 10% raise somewhere else.'),
      ('frowned on', 'Quitting without two weeks’ notice.'),
      ('fine', 'A company laying off 4,000 people by email, effective immediately.'),
      ('fine', 'A company firing you for no reason. Legal in nearly every state.'),
    ]),
  ]),
  ('An aging parent', [
    ('In someone else’s care', 'Said: “Family takes care of family.”', [
      ('expected', 'Moving across the country for a job.'),
      ('fine', 'A good nursing home, close by.'),
      ('eyebrows', 'A good nursing home, and no visits for a year.'),
      ('not okay', 'No care at all, and no visits.'),
    ]),
  ]),
]),
('Loving', '♥', [
  ('Animals', [
    ('Some more than others', 'Said: “All creatures great and small.”', [
      ('expected', 'A dog, asleep in your bed.'),
      ('fine', 'A pig, as smart as a dog, as bacon.'),
      ('fine', 'A $9,000 surgery, for a 12-year-old dog.'),
      ('laughed at', 'A $900 surgery, for a goldfish.'),
      ('laughed at', 'Your fortune, left to your cat.'),
    ]),
  ]),
]),
('Dating', '∞', [
  ('A coworker', [
    ('By rank', 'Said: “Don’t mix work and love.”', [
      ('admired', 'You met at work and got married.'),
      ('fine', 'Someone at your level, in another department.'),
      ('eyebrows', 'Someone on your own team.'),
      ('not okay', 'Your boss.'),
      ('not okay', 'Your intern.'),
    ]),
  ]),
  ('A friend’s ex', [
    ('After a while', 'Said: “Loyalty comes first.”', [
      ('fine', 'Five years after they broke up.'),
      ('eyebrows', 'A year after.'),
      ('not okay', 'A month after.'),
      ('not okay', 'Your sibling’s ex, any time.'),
    ]),
  ]),
  ('More than one person', [
    ('At once', 'Said: “To each their own.”', [
      ('fine', 'A few people, before anyone says “exclusive.”'),
      ('eyebrows', 'An open marriage, both agreeing.'),
      ('not okay', 'A secret second partner.'),
      ('illegal', 'Two spouses, all three agreeing. Bigamy, in every state.'),
    ]),
  ]),
]),
('Mocking', '☺', [
  ('Someone’s job', [
    ('As a punchline', 'Said: “Every job deserves respect.”', [
      ('fine', 'Lawyers.'),
      ('fine', 'Politicians.'),
      ('fine', 'Telemarketers.'),
      ('fine', 'A CEO.'),
      ('not okay', 'A janitor.'),
      ('not okay', 'A nurse.'),
    ]),
  ]),
  ('Someone’s beliefs', [
    ('To their face', 'Said: “Respect other people’s beliefs.”', [
      ('fine', 'A flat-earther.'),
      ('fine', 'A friend who reads her horoscope.'),
      ('eyebrows', 'A coworker who prays before lunch.'),
      ('not okay', 'A grieving widow who says he’s in heaven now.'),
    ]),
  ]),
]),
('Disturbing', '†', [
  ('Nature', [
    ('For your own use', 'Said: “Leave no trace.”', [
      ('fine', 'Clearing forty acres of forest, for a subdivision.'),
      ('fine', 'A golf course, watered daily, in the desert.'),
      ('fine', 'A lawn, mowed every week, where a meadow was.'),
      ('not okay', 'Your initials, carved into a tree.'),
      ('illegal', 'A handful of wildflowers, picked in a national park.'),
    ]),
  ]),
]),
('Eating', '⊚', [
  ('What others won’t', [
    ('Depending on the name', 'Said: “Don’t knock it till you try it.”', [
      ('admired', 'Escargot, at a French restaurant.'),
      ('eyebrows', 'Snails, from your garden.'),
      ('fine', 'Oysters, alive, on the half shell.'),
      ('eyebrows', 'Crickets, roasted.'),
      ('fine', 'A hot dog, made of the parts nobody asks about.'),
      ('eyebrows', 'Tongue, by name.'),
    ]),
  ]),
  ('In front of others', [
    ('With your hands', 'Said: “Mind your manners.”', [
      ('expected', 'Pizza.'),
      ('expected', 'Ribs.'),
      ('fine', 'Sushi.'),
      ('eyebrows', 'Spaghetti.'),
      ('not okay', 'From someone else’s plate, uninvited.'),
    ]),
  ]),
  ('What’s left over', [
    ('Or thrown away', 'Said: “Don’t waste food.”', [
      ('fine', 'Throwing out your leftovers.'),
      ('fine', 'A bakery, throwing out the day’s unsold bread.'),
      ('eyebrows', 'Day-old bread, taken from a bakery’s dumpster.'),
      ('not okay', 'Finishing a stranger’s fries, at the next table, after they leave.'),
    ]),
  ]),
]),
('Swearing', '#', [
  ('Out loud', [
    ('By who’s listening', 'Said: “Watch your language.”', [
      ('expected', 'When you stub your toe.'),
      ('fine', 'With friends, at a bar.'),
      ('fine', 'On a cable TV show.'),
      ('illegal', 'On broadcast TV, in prime time. The FCC fines it.'),
      ('eyebrows', 'In front of your parents.'),
      ('not okay', 'In front of someone else’s kids.'),
    ]),
  ]),
]),
('Watching', '◉', [
  ('Strangers', [
    ('Or recording them', 'Said: “Mind your own business.”', [
      ('fine', 'People-watching, at a café.'),
      ('eyebrows', 'Staring at one person, on the subway.'),
      ('admired', 'Street photography, hung in a gallery.'),
      ('fine', 'A car that photographs every house in America, for a map.'),
      ('fine', 'A doorbell camera that films everyone who walks by.'),
      ('not okay', 'Photographing a stranger’s kid at the park.'),
    ]),
  ]),
  ('People you know', [
    ('Their private messages', 'Said: “Respect people’s privacy.”', [
      ('fine', 'Googling a date before you meet.'),
      ('fine', 'An employer, reading your work email.'),
      ('divided', 'A parent, reading a 15-year-old’s texts.'),
      ('not okay', 'A spouse, reading the other’s texts.'),
    ]),
  ]),
]),
('Giving', '◈', [
  ('Money', [
    ('To someone who serves you', 'Said: “It’s better to give than to receive.”', [
      ('expected', '20%, to a waiter.'),
      ('fine', '$20, to a hotel housekeeper.'),
      ('eyebrows', '$20, to a nurse.'),
      ('not okay', '$20, to a cop.'),
      ('illegal', '$20,000, to a building inspector.'),
    ]),
    ('To a cause', 'Said: “Every bit helps.”', [
      ('admired', '$500, to a stranger’s GoFundMe for surgery.'),
      ('admired', '$50 million, to a university, with your name on the building.'),
      ('fine', '$5, to a man asking for change.'),
      ('eyebrows', '$5, to a man asking for change, after he tells you it’s for beer.'),
    ]),
  ]),
  ('A gift', [
    ('To a teacher', 'Said: “It’s the thought that counts.”', [
      ('expected', 'A $25 gift card, at Christmas.'),
      ('eyebrows', 'A $500 bag, at Christmas.'),
      ('not okay', 'An envelope of cash, the week before grades close.'),
    ]),
  ]),
]),
('Touching', '⊹', [
  ('Strangers', [
    ('Their bodies', 'Said: “Keep your hands to yourself.”', [
      ('fine', 'Pressed against them, on a rush-hour train.'),
      ('expected', 'A handshake, on meeting.'),
      ('fine', 'A pat-down, at airport security.'),
      ('fine', 'Their scalp, while washing their hair at a salon.'),
      ('eyebrows', 'A hug, on meeting.'),
      ('not okay', 'Their hair, because it looks interesting.'),
    ]),
  ]),
  ('Coworkers', [
    ('In the office', 'Said: “Keep it professional.”', [
      ('expected', 'A handshake.'),
      ('fine', 'A high-five, after a win.'),
      ('eyebrows', 'A hug, at someone’s retirement.'),
      ('not okay', 'A shoulder rub, at their desk.'),
    ]),
  ]),
]),
('Cutting in line', '⇥', [
  ('Ahead of others', [
    ('By who you are or what you pay', 'Said: “Wait your turn.”', [
      ('fine', 'A pregnant woman, at the bathroom line.'),
      ('fine', 'A $78 fee, for the shorter airport security line.'),
      ('fine', 'A credit card with priority boarding.'),
      ('fine', 'A paid pass, for the short line at Disney.'),
      ('not okay', '$20, handed to the person at the front of the deli line.'),
      ('not okay', 'Just walking to the front of the coffee line.'),
    ]),
  ]),
]),
('Punishing', '⚖', [
  ('A whole group', [
    ('For one person', 'Said: “Punish the guilty, not the innocent.”', [
      ('fine', 'A teacher, keeping the whole class in from recess.'),
      ('fine', 'A coach, making the whole team run laps.'),
      ('divided', 'Sanctions on a country, felt by everyone who lives there.'),
      ('not okay', 'A boss, docking everyone’s pay for one person’s theft.'),
    ]),
  ]),
]),
('Breaking', '÷', [
  ('The law', [
    ('A little', 'Said: “The law is the law.”', [
      ('expected', 'Nine over the speed limit.'),
      ('fine', 'Jaywalking, on an empty street.'),
      ('fine', 'Weed, legal in your state, illegal under federal law.'),
      ('eyebrows', 'Rolling through a stop sign.'),
      ('divided', 'Sitting in at a lunch counter, or blocking a highway, for a cause.'),
      ('not okay', 'A pack of gum, shoplifted.'),
    ]),
  ]),
]),
]
