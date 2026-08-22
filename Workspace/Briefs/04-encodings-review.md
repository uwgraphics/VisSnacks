# Brief: Encodings (already drafted) — review consolidation

*Sources: `04-M-Encodings.pptx` (Lecture 4-M, Monday 9/22/2025) and `04-2-AbstractionEncodings.pptx` (Lecture 4-2, "Encodings Practice," dated 9/28). Full text in `_lecture_experiment/extracted/04M-encodings-deck-text.txt` and `…/04-2-AbstractionEncodings-deck-text.txt` (the latter extracted 2026-08-22).*

## 0. Why this brief exists (it's not for a new page)

Two pages are already drafted and have been sitting unreviewed since 2026-07-17:

- `content/tutorials/encodings/` — 1,636 words, `draft = true`, `weight = 30`
- `content/snacks/charts-are-encodings/` — 682 words, `draft = true`

They were the **pilot**, drafted from `_lecture_experiment/lecture-experiment.md` before the brief format existed — so they're the only planned pages with no brief, and §5–8 was never asked. They are also items #1 and #2 in `queue.md`'s "Finish what's started," and review is the one step no agent can do.

**This brief's job is to make that review cheap:** consolidate every open edit in one place, and add what the decks say that the drafts didn't use. One of the open questions turns out to be answered by a deck nobody had extracted.

## 1. The documents (agent-filled)

Unchanged from what exists — this brief proposes no new page. The pair is deliberately split: the tutorial carries the concept (marks, channels, expressiveness, position-is-special), the snack carries one worked idea (chart types decompose into encoding bundles). They **cross-link**, so per CLAUDE.md they must publish together or the `link` shortcode breaks the build.

Open structural question, from `MODULE-DOCS-PLAN.md` item 6: whether "Composing designs (the 2-numbers exercise)" splits out of the tutorial's "Try It Yourself" section. **The week-4 Wednesday deck makes that a much bigger question than it looked** — see the sibling brief `04-encodings-practice.md`.

## 2. Course fit (agent-filled)

Module 2, "Building Blocks of Visualizations" (Sep 15–26). Lecture 4-M.

Module 2 learning outcomes, quoted from <https://pages.graphics.cs.wisc.edu/765-25/modules/2/>:

1. "have practice with critique to enable learning from examples going forward."
2. "have a vocabulary for describing data (data abstraction) to help us connect it to visual representations."
3. "understand the many different ways that we might talk about task, in ways that help us design visualizations that address tasks."
4. **"be able to describe a range of different visual encodings and describe visualizations in terms of these building blocks."**

Outcome #4 is this pair's outcome, and note its two halves — *describe a range of encodings* (the tutorial does this) and *describe visualizations in terms of these building blocks* (the snack does this, once; `04-encodings-practice.md` does it properly). Module description: "We will look at how we can consider visualizations in terms of the building blocks of data and task abstractions and visual encodings."

Arc: data abstraction (3-M) → **encodings (4-M)** → encodings practice + Tableau (4-W) → encodings practice again (4-2) → Module 3.

## 3. Sources (agent-filled)

- **Primary (used by the draft):** `04-M-Encodings.pptx`.
- **Primary (NOT used by the draft — nobody had extracted it):** `04-2-AbstractionEncodings.pptx`. `lecture-experiment.md` guessed it was "a possible alternate/earlier framing" and told the pilot agent to skim it; its slide 1 actually dates it **9/28, six days *after* 4-M**, so it is a *later* practice deck, not an earlier draft. It contains material the pilot never saw. → §4.
- **Module 2 required encodings readings**, all now summarized on disk: Munzner ch. 5 "Marks and Channels" and ch. 7 "Arrange Tables" (`summaries-munzner.md`); Cairo *The Truthful Art* ch. 5 "Basic Principles of Visualization" (`summaries-cairo.md`); Cleveland & McGill 1984 *and* 1985 (`summaries-papers.md`).
- **Optional, summarized:** Mackinlay 1986 (`summaries-papers.md`); Tufte "Visual and Statistical Thinking" (`summaries-tufte.md`).
- **Optional, NOT summarized — and the most relevant gap:** **McColeman et al., "Rethinking the Ranks of Visual Channels."** That paper is about exactly this page's central claim (channel rankings), and the page currently hedges the rankings in an expand box without citing anything that complicates them. Also unsummarized: Heer & Bostock "Crowdsourcing Graphical Perception," Sarikaya & Gleicher "Scatterplots."

## 4. What the decks say that the drafts didn't use (agent-filled)

**⚑ The "Pareto mapping" question is answered by 04-2, slide 27.** `queue.md` and `0718-Summary.md` both carry a pending edit: *give real terms for "Pareto mapping" ("value-based sorting" / "data-driven ordering") then "I call it a Pareto mapping."* The deck already does this, and better than the snack does. Verbatim:

> **Pareto mapping** (mike's term ?)
> Redundantly use a dependent variable as an independent variable. (rank ordering)
> Exposes trends
> Enables close comparisons
> Search by value (min, max, …)

Two things fall out. (1) *You flagged your own uncertainty about the term in your own slides* — "(mike's term ?)" — so the snack's hedge ("I'm not sure anyone else does") is faithful, not a guess. (2) The three benefits are a **better payoff than the snack currently gives**; the snack says sorting "exposes the overall distribution, puts similar values next to each other, and makes min/max/rank questions trivial," which is the same list in weaker words. Consider lifting yours.

**Mackinlay frames the whole deck.** 04-2 slide 3 opens on Mackinlay 1986 with "What task(s) is each of these good for?" The tutorial never mentions Mackinlay, though he's an optional Module 2 reading with a summary on disk. This is the natural "Want More?" addition.

**The automation thread, which the drafts drop entirely.** 04-2, consecutive slides: *"Automate this? Given the data type, can you automatically design the chart?"* → *"Where is this going? Principles for choosing / Types suggest encodings."* This is the payoff of decomposition (it's what makes automatic design *possible*), it's the Mackinlay connection, and it's one sentence of work.

**04-2 slide 13 — "Aside… Interval vs. nominal/ordinal: Not interval, we could… / Interval, we need to keep."** The snack's line-vs-dot argument turns on exactly this and derives it from scratch; the deck has the compressed version, and it's the direct hook to the data-abstraction page's NOIR material.

**04-2 slides 22–29 walk Categorical × Ratio through five designs**, each annotated with the mapping *and* the open question — "Categorical → X position (mapping? Imposed order)," "Ratio → Color (color encoding)," "Ratio → Size / Area (mapping / ramp)." The repeated parenthetical "(mapping?)" is doing real teaching work: choosing the channel doesn't finish the job, you still owe a mapping. Neither draft makes that point.

**⚑ A contradiction between two required readings that the page should probably own.** The reading summary for Cairo flags it (`summaries-cairo.md`): Cairo folds Cleveland & McGill's two data types into a *single* linear ranking with **hue at the bottom**, whereas Munzner (and the course) keep separate rankings for magnitude vs. identity channels — where hue ranks *well* for categorical data. Students read both in the same module. The tutorial's "Which Channel Is Best?" section is where that reconciliation belongs, and right now it isn't there.

## 5. What to cut / what must survive (MIKE)

Carried over from `0718-Summary.md`, still open — these are edits you already approved, not new questions:

- **Pareto mapping** — see §4; the deck gives you the words. Keep the hedge?
- **The genai box on the snack** needs to credit the framing: your note was *"Claude came up with a framing that I like"* about "a chart type is a bundle of encoding choices that someone found useful enough to name." Currently the box says only that Claude drafted the page.
- **The parallel-coordinates claim.** The tutorial's expand box says parallel coordinates keep working with ten dimensions; your note was **"best of a bad lot."** Needs rewording. (Supporting evidence for your version: 04-W slide 9 and 04-2 slide 41 both write "Scales well to more dimensions **(?)**" — with the question mark.)
- **Image provenance spot-check** (`0718-Summary.md` item 9): the Cleveland & McGill and Bertin images came out of your deck with citations baked in, but styling that suggests they may have originated in *someone else's* slides. Worth a look before anything publishes.
- ICE call: 4-M's exercises are the 2-numbers design sequence, which belongs to the sibling brief. Does the tutorial keep its "Try It Yourself" box, or hand off?

## 6. The stories (MIKE)

- The tutorial has no personal material at all — it's the most textbook-like page in the drafted set, which is the failure mode `STYLE-GUIDE.md` warns about ("if a draft starts reading like a chapter summary, it has drifted"). One anecdote would fix it. Candidate slot: "Position Is Special" — is there a design where you *spent* position badly and regretted it?
- Do you have a first-hand read on the Cleveland & McGill experiments beyond the papers — anything from having taught them for years that isn't in either paper?

## 7. Contested takes (MIKE)

- **The Cairo/Munzner ranking conflict (§4).** Which is right, in your view — or is the answer "they're answering different questions"? This is the highest-value unwritten sentence on the page, because a student reading both required chapters *will* hit it.
- The tutorial hedges the channel rankings in an expand box ("a warning about experiments"). How hard do you want to push? McColeman et al. is on your own optional list and argues the rankings need rethinking; nobody has summarized it yet.
- "Position is special" is stated firmly. Is there a case where you'd spend position on something other than the most important variable?

## 8. Anything else (MIKE)

- **Publish together or delink** — the two pages cross-link, and the `link` shortcode build-errors on a missing page.
- Both are now at `content/tutorials/encodings/` (moved from `content/modules/` on 2026-08-22) and `content/snacks/charts-are-encodings/`. `Workspace/Tools/figs.py` regenerates their figures and writes into those bundles — it will overwrite the committed PNGs, and a different matplotlib version produces byte-different files.
- The queue's merge/differentiate question for the snack is now informed by `02-vis-basics.md`: the real chart-typology argument lives in lecture **2-M**, not here. Deciding that first may shrink this snack's job.
