# Draft Report: Data Abstraction module page

Page: `content/tutorials/data-abstraction/index.md` (draft = true, uncommitted).

## 1. Verification list (check, don't trust)

- **Munzner's interval/ratio footnote.** I quoted it as saying the distinction "is typically not useful when designing a visual encoding" (attributed to her footnote 3, citing Stevens 1946). This comes from the AI reading-summary, not from the book directly - confirm the exact wording and that it's a footnote before publishing a direct quote.
- **Munzner's three attribute types.** I say she uses categorical / ordinal / quantitative and folds interval+ratio together. Correct per the summary; worth a sanity check against ch. 2.5.
- **NOIR cheat-sheet contents.** The operations column (=/<//+/×) and "encodings that fit" column are standard levels-of-measurement lore plus my mapping to channels; the slides give NOIR and the numbers-lie examples (student ID, department code, temperature, weight/distance/count) but do NOT spell out the operations-or-encodings table. That table is my synthesis - please read it as a claim to check, especially the "encodings that fit" cells.
- **Lecture number.** Deck slide 1 internally says "Lecture 3-M," but the brief and task both say this is 3-W (first half of the abstraction lecture). I used 3-W per the task. Confirm which is right for the genai box.
- **John Snow "deaths by position."** From slide 19 as a rotation example. I kept it to one clause; verify it reads the way you intend (the slide just says "John Snow: Deaths by position").
- **Tableau dimensions/measures = key/value.** Stated as fact; it's in the Munzner summary (2.6) and consistent with the slide's Tableau warning, but confirm you're happy equating them so directly.
- **Cross-links resolve.** I used only `/tutorials/encodings`, `/snacks/cairo-discrete-line`, `/resources/munzner`. Confirm all three pages exist so the `link` shortcode doesn't build-error (encodings and cairo I read; munzner I did not open - the encodings page links it as `{{<link munzner>}}`, so the resource page should exist).

## 2. Placeholders left

None. I did not insert any `[MIKE: ...]` markers.

Reasoning: the brief's MIKE sections (5-8: cuts, stories, contested takes, misc) were empty, and rather than fabricate a walkthrough dataset or a personal anecdote to fill them, I wrote the page to stand without one. The lecture's own examples (the daily temperature check, John Snow, market share) carried the concrete load, so no story-shaped hole was left gaping. If you want a signature worked example (the brief flags that the lecture used examples not recoverable from slides), the natural spot is the "Keys and Values" section or a new opening hook - that's where a `[MIKE: favorite example dataset?]` would go if you'd rather I mark it than leave it smooth.

## 3. Figure wishes (page currently has no images)

- **NOIR ladder diagram** next to the cheat-sheet table - the four levels as nested rings or a staircase, showing each rung inherits the operations below it. Highest value; the table implies it but a picture would land it instantly.
- **The same data shown three ways** (table / field / network) - one small triptych for the "three kinds of data sets" section, à la the encodings page's "four channels" figure.
- **Sampling turns a field into a table** - a continuous curve with sample points dropping into spreadsheet rows (slide 17 had a gif here). Lives in the expand box.
- **Diverging vs. sequential** - the elevation-around-sea-level example as a quick colorbar pair. Small, but it's the payoff the "other properties" section promises for the color module.
- **Binning changes the story** - one histogram at two bin widths, to foreshadow the future binning discussion. Optional; may belong on that future page instead.

## 4. Self-assessment: mechanical vs. authorial

Roughly 55% mechanical, 45% judgment. Mechanical: pulling the set types, keys/values, NOIR levels, conversions, and special cases straight off the slides and the Munzner summary; matching front-matter and shortcode mechanics to the encodings sibling. The judgment sat in decisions the sources didn't make for me: how much to lift the cheat-sheet into an actual table (the module page "promised" one, so I made it the centerpiece rather than prose), how to frame the "why NOIR when Munzner skips it" tension as an owned opinion rather than a correction of her, what to push into expand boxes to keep the main flow snack-length, and where to stop (the task-abstraction handoff is deliberately one paragraph). The voice - hedged opinions, the terminology-warning aside, "numbers lie about their level" - is imitation of your register from the two calibration pages, so treat tone as the thing most in need of your ear.
