# Round three. Same shape; merged by headword, object and entry (cases appended to an existing entry).
MORE2 = [
('Killing', '✕', [
  ('An animal', [
    ('To eat it', '', [
      ('fine', 'A chicken, raised in a barn, for nuggets.'),
      ('fine', 'A tuna, for a can.'),
      ('divided', 'A calf, for veal.'),
      ('eyebrows', 'Your backyard chicken, the one with a name, for soup.'),
      ('not okay', 'A dolphin, for anything.'),
    ]),
    ('Because it’s in the way', '', [
      ('fine', 'A spider, with a shoe.'),
      ('eyebrows', 'A butterfly, with a shoe.'),
      ('fine', 'A snake, in the yard, with a shovel.'),
    ]),
  ]),
]),
('Lying', '≠', [
  ('To people you love', [
    ('To spare them', '', [
      ('expected', '“You haven’t aged a day.”'),
      ('fine', '“No, it’s not a bother at all.”'),
    ]),
  ]),
]),
('Showing', '◯', [
  ('Skin', [
    ('In public', '', [
      ('expected', 'A swimmer, in a Speedo, at the Olympics.'),
      ('eyebrows', 'A dad, in a Speedo, at the town pool.'),
      ('fine', 'A wrestler, in a singlet.'),
    ]),
  ]),
]),
('Cutting in line', '⇥', [
  ('Ahead of others', [
    ('By who you are or what you pay', '', [
      ('fine', 'A celebrity, past the velvet rope.'),
      ('fine', 'A man with one item, waved ahead at the grocery store.'),
      ('not okay', 'A man with one item, who waves himself ahead.'),
    ]),
  ]),
]),
('Changing', '⌁', [
  ('Your mind', [
    ('In public', 'Said: “Stand by your convictions.”', [
      ('admired', 'A scientist, after new data comes in.'),
      ('admired', 'An old racist, who apologizes on TV.'),
      ('frowned on', 'A politician, after the polls move. “Flip-flopper.”'),
      ('laughed at', 'A fan, switching teams after a losing season.'),
    ]),
  ]),
]),
('Giving', '◈', [
  ('Your seat', [
    ('On a bus', 'Said: “First come, first served.”', [
      ('expected', 'To a pregnant woman.'),
      ('expected', 'To a man on crutches.'),
      ('expected', 'To an old woman.'),
      ('fine', 'To a mother holding a toddler.'),
      ('divided', 'To a young woman, from a young man. Polite, or patronizing.'),
      ('eyebrows', 'To a young man, from a young man.'),
    ]),
  ]),
]),
('Breaking', '⚠', [
  ('A promise', [
    ('Once it’s inconvenient', 'Said: “A promise is a promise.”', [
      ('fine', 'Cancelling dinner plans, because you’re tired.'),
      ('expected', 'A politician’s campaign promise, after the election.'),
      ('frowned on', 'Skipping a friend’s wedding you RSVP’d yes to.'),
      ('not okay', 'Skipping your kid’s recital, for golf.'),
      ('not okay', 'Wedding vows.'),
    ]),
  ]),
  ('The rules of a game', [
    ('To win', 'Said: “Play fair.”', [
      ('admired', 'A “smart foul,” to stop the clock.'),
      ('fine', 'A flop, in soccer, that draws a penalty.'),
      ('fine', 'Counting cards at blackjack. Legal; the casino throws you out anyway.'),
      ('not okay', 'Sticky stuff on a pitcher’s hand.'),
      ('not okay', 'Steroids.'),
    ]),
  ]),
]),
('Asking', '?', [
  ('Personal questions', [
    ('To someone you just met', 'Said: “There are no stupid questions.”', [
      ('expected', '“What do you do?”'),
      ('fine', '“Where are you from?” To a white guy from Ohio.'),
      ('eyebrows', '“Where are you from? No, where are you really from?”'),
      ('fine', '“So when are you two having kids?” To a 30-year-old man.'),
      ('frowned on', '“So when are you two having kids?” To a 30-year-old woman.'),
      ('eyebrows', '“How much do you make?”'),
      ('not okay', '“When are you due?” To a woman who isn’t pregnant.'),
    ]),
  ]),
]),
('Making noise', '♫', [
  ('In a crowd', [
    ('At an event', 'Said: “Be respectful.”', [
      ('expected', 'Screaming, at a football game.'),
      ('expected', 'Heckling the umpire, at a baseball game.'),
      ('fine', 'Singing along, at a concert.'),
      ('not okay', 'Cheering mid-point, at a tennis match.'),
      ('not okay', 'Talking, at a movie theater.'),
      ('not okay', 'Clapping between movements, at a symphony.'),
    ]),
  ]),
  ('To strangers', [
    ('Small talk', 'Said: “Be friendly.”', [
      ('fine', 'With a cashier.'),
      ('fine', 'With a stranger, at a bar.'),
      ('fine', 'With the person next to you, on a plane, for five minutes.'),
      ('eyebrows', 'With the person next to you, on a plane, for five hours.'),
      ('frowned on', 'With a stranger, on the subway.'),
      ('not okay', 'At the next urinal.'),
    ]),
  ]),
]),
('Wearing', '⌘', [
  ('Clothes', [
    ('To a wedding or a funeral', 'Said: “Wear whatever makes you comfortable.”', [
      ('expected', 'Black, to a funeral.'),
      ('fine', 'A bright dress, to a funeral, if she asked for color.'),
      ('eyebrows', 'Jeans, to a funeral.'),
      ('not okay', 'White, to someone else’s wedding.'),
    ]),
    ('Meant for someone else', 'Said: “Clothes don’t have a gender.”', [
      ('fine', 'A woman, in a man’s suit.'),
      ('fine', 'A Scotsman, in a kilt.'),
      ('eyebrows', 'A man, in a dress, to the office.'),
      ('fine', 'A pirate costume, for Halloween.'),
      ('not okay', 'A Native American headdress, for Halloween.'),
    ]),
  ]),
]),
('Being late', '⌛', [
  ('By who’s waiting', [
    ('On whom', 'Said: “Be on time. Other people’s time matters.”', [
      ('expected', 'You, thirty minutes late, to a house party.'),
      ('expected', 'A bride, twenty minutes late, to her own wedding.'),
      ('fine', 'A doctor, forty minutes late, to your appointment.'),
      ('fine', 'The cable guy, “sometime between 8 and 2.”'),
      ('not okay', 'You, ten minutes late, to the same doctor. They cancel and charge you.'),
      ('not okay', 'You, ten minutes late, to a job interview.'),
    ]),
  ]),
]),
('Posting', '⊡', [
  ('Other people', [
    ('Online, without asking', 'Said: “Respect people’s privacy.”', [
      ('expected', 'Your own baby, daily, since birth.'),
      ('fine', 'A stranger’s meltdown at the airport, for millions to see.'),
      ('eyebrows', 'A friend’s kid.'),
      ('divided', 'Your 14-year-old’s embarrassing photo, as a joke.'),
      ('not okay', 'A screenshot of a friend’s private text.'),
    ]),
  ]),
]),
('Praying', '✧', [
  ('Where others can see', [
    ('In a shared space', 'Said: “Keep religion out of the public square.”', [
      ('admired', 'A quarterback, pointing to the sky after a touchdown.'),
      ('fine', 'A moment of silence, before a game.'),
      ('eyebrows', 'A prayer, out loud, before a business meeting.'),
      ('divided', 'A coach, praying on the field after a public school game.'),
    ]),
  ]),
]),
('Spending', '¢', [
  ('On yourself', [
    ('A lot', 'Said: “Live within your means.”', [
      ('fine', '$1,500, on a phone.'),
      ('fine', '$40,000, on a wedding.'),
      ('fine', '$300, on concert tickets.'),
      ('eyebrows', '$300, on a bottle of wine.'),
      ('frowned on', '$300, on lottery tickets.'),
      ('laughed at', '$40,000, on a dog’s wedding.'),
    ]),
  ]),
]),
('Copying', '©', [
  ('Someone’s work', [
    ('And using it', 'Said: “Be original.”', [
      ('admired', 'A cover of a famous song.'),
      ('fine', 'A recipe, off someone’s blog.'),
      ('fine', 'A cheap brand, knocking off a runway look.'),
      ('fine', 'A tech giant, copying a rival app’s best feature.'),
      ('illegal', 'The famous song, released as yours.'),
      ('not okay', 'A classmate’s homework.'),
    ]),
  ]),
]),
('Starting', '↺', [
  ('Late in life', [
    ('Something people do young', 'Said: “It’s never too late.”', [
      ('admired', 'College, at 60.'),
      ('admired', 'A marathon, at 70.'),
      ('fine', 'Running a company, at 75.'),
      ('divided', 'Running the country, at 80.'),
      ('eyebrows', 'Fatherhood, at 65.'),
      ('frowned on', 'Motherhood, at 55, through IVF.'),
    ]),
  ]),
]),
]
