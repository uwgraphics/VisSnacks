# Brief: Why Visualize?

*Source lecture: `02-M-Why.pptx` (Lecture 2-1, Monday 9/8/2025), 61 slides. Full text extracted to `_lecture_experiment/extracted/02M-why-deck-text.txt`; the Wednesday companion to `_lecture_experiment/extracted/02W-whythisvis-deck-text.txt`.*

**Read this first:** the deck is two documents, not one. It says so itself — slide 5 is "A Change of Topic…" and slide 39 is "Resume Regularly Scheduled Lecture," and slide 4 has the reason in your own words: *"Changed my mind! Decided on a new plan (Vis Basics). A different inspiration this morning."* Slides 5–38 are a prepended segment on the chart-typology approach; slides 39–61 are the "Why Vis?" lecture the title promises. **This brief covers slides 39–61.** The first half is a different page — see the appendix, which needs a decision from you before it gets a brief of its own.

## 1. The document (agent-filled)

Tutorial-weight page, ~1,200–1,800 words. Working title: **"Why Visualize?"** Destination: `content/tutorials/why-vis/` (the tutorials tail, alongside the drafted `encodings/` and `data-abstraction/`).

**Why this isn't redundant with Tutorial 1.** Tutorial 1 (6,700 words) answers *what* visualization is and *how* to do it. Its closing "Now What?" list, item 1, is verbatim:

> We need to understand **why** we use visualization. Why can (well designed) pictures help people do things?

Tutorial 1 poses this page's question and does not answer it. Grepping Tutorial 1 confirms it: no alternatives-to-vis discussion, no Cairo/Tufte/Ware/Card material, no "kinds of why." So the redundancy risk here is low — much lower than the plan assumed when it filed "Why Visualize?" as a sub-item of the Tutorial-1 split.

Structural bonus worth noticing: Tutorial 1's "Now What?" list is *the plan for this whole project*. Item 1 is this page, item 3 is data-abstraction (drafted), item 4 is encodings (drafted), item 5 is evaluation, item 6 is perception + color, item 7 interaction, item 8 scale, item 9 graphs/volumes. That list is a ready-made structure for the tutorials landing page (open question #1) — see §8.

The skeleton is already on the slide: **the four whys** (slide 48, deliberately repeated at slide 55 as a signpost). Use it.

Not in scope: the stop-sign snack (already planned in `01-tutorial-1-revision.md` — but see §5, the slides make a bigger point than that brief credits).

## 2. Course fit (agent-filled)

Module 1, "Visualizations and Effectiveness" (Sep 3–10). Lecture 2-M.

Module 1 learning outcomes, quoted from <https://pages.graphics.cs.wisc.edu/765-25/modules/1/>:

1. "To understand our broad definition of visualization as the solution to 'data problems' (tasks) and the notion of effectiveness"
2. "To get some intuitions about 'what is easy to see' (as a way to appreciate effective visualizations)"
3. "To get some exposure to design process"
4. "Be set with class mechanics"

This page serves outcome #1 — specifically the part of #1 that Tutorial 1 leaves implicit. Outcome #2 belongs to Tutorial 3; #3 to the critique/design material; #4 is class mechanics and stays off the site.

Arc: Tutorials 1/2/3 are assigned before this lecture → this lecture → 2-W's reverse-engineering exercise → Module 2's building blocks (data abstraction, task abstraction, encodings — all drafted or briefed).

**This is the reading-frame page for Module 1's largest reading cluster** — required: Cairo *Functional Art* ch. 2 "Forms and Functions" and ch. 3 "The Beauty Paradox," Tufte *VDQI* ch. 1 "Graphical Excellence"; optional-recommended: Munzner ch. 1 "What's Vis, and Why Do It?", Cairo FA preface + ch. 1, Wexler ch. 1. Of every page in the plan, this one most directly serves project goal #2 ("give the main points of the readings, so the assigned readings can be focused or optional").

## 3. Sources (agent-filled)

Not 1-to-1 with the lecture — the lecture's first 38 slides are a different topic entirely.

- **Primary:** `02-M-Why.pptx` slides 39–61.
- **Secondary:** `02-W.pptx` slide 3 (repeats the four-authors summary), slides 29–35 (Cairo's dimensions, explore-vs-explain, author-vs-audience, "exploratory vis is still a task").
- **Reading summaries already on disk** (use these, don't re-read the books): `Workspace/Re-Papering/summaries-cairo.md` — FA preface+ch.1, ch.2 "Forms and Functions," ch.3 "The Beauty Paradox"; `summaries-munzner.md` — ch. 1; `summaries-books-other.md` — Tufte ch. 1, Wexler ch. 1.
- **Reading summary missing and wanted:** Card/Mackinlay/Shneiderman intro — the "your brain needs help" leg of the four-authors slide, and the whole vis-amplifies-cognition argument. Queued in re-papering batch 2 (`Workspace/Re-Papering/status.md` §3). Ware is not summarized and is not assigned; `content/resources/visual-thinking/` is the existing pointer.
- **Existing VisSnacks neighbors:** `tutorials/1-what-is-vis` (poses the question), `tutorials/0-how-to-vis` (draft stub — overlap risk, see §8), **`snacks/app-time-graphs` (already publishes the water-heater story — see §4)**, `resources/cairo`, `resources/tufte`, `resources/visual-thinking`, `papers/problem-space` (draft).

## 4. High-value material in the slides (agent-filled)

**The definition, in three passes** — slides 40, 44, 45. Same two lines each time, with an accreting gloss:

> Visualization: A picture designed to help some one do some thing. / A Good Visualization: Is effective at helping the viewer achieve the task.

- 44 adds: "**Conscious choices toward a goal**" (the design gloss).
- 45 adds: "Why? **Because we think that a picture will help!** (be effective) — *(but why do we think that?)*" ← this parenthetical is the pivot into the whole page. It's the best sentence on the deck.

**Slide 41 — the operational alternate definition.** Framed explicitly as old-vs-new: "Old definition: A picture designed to help some one do some thing. New (operational) definition: **A picture designed to make some things easier to see.**" Tutorial 1 uses the old one throughout. → question in §7.

**Slides 42–43 — the stop sign.** More interesting than the snack brief credits. The answer isn't yes or no: *"If it helps us, then yes! Does it help us: Design a better stop sign? Learn to design better?"* The definition is judged by **usefulness, not correctness** — that's a real methodological stance, and it's the same move as "use formalisms when they're useful, don't get stuck on their details" in the task-abstraction brief. Slide 42 also asks the class "What is your answer? What do you think my answer would be?" and cites a Fall-21 discussion.

**Slide 46 — two senses of "why."** (a) *Why are you doing it?* → tasks / goals / audience. (b) *Reasons why vis may be effective* → why use vis (not something else)? why do it well? why does a particular design work?

**Slide 47 — why ask why.** Tasks/goals/audience: "so we can make sure we're solving the right problem." Reasons-it's-effective: "so we can design to achieve them."

**Slide 48, repeated verbatim at 55 — THE FOUR WHYS.** The page's skeleton:

> Why visualize? — *what kinds of tasks/goals/domains?*
> Why visualization? — *and not something else*
> Why does visualization "work"? — *that makes it unique*
> Why good visualization? — *since it's hard*

**Slides 49–53 — "A Story (from 2024)": the water heater.** *Resolved:* this is the AO Smith water-heater app, and **it is already a published VisSnacks page** — `content/snacks/app-time-graphs/` (2024-09-09, `draft = false`), which pairs it against the Garmin steps graph. This answers open question #3 in `MODULE-DOCS-PLAN.md` and the §6 question in `01-tutorial-1-revision.md`. **Link to that snack; don't re-tell it.** But slides 51–53 have material the snack doesn't: "Last Year And This Year," an "Is this effective? Can I achieve my task / Does the basic design work? Could the details be better?" frame, and a two-image "Comparison of Visualizations." → question in §6.

**Slide 54 — the deck already points students at VisSnacks** ("Some of these examples I've written up as web pages… The VisSnacks web site (work in progress)"). Confirmation the lecture is already delegating to the site; this project is finishing a move you started.

**Slide 56 — "What are your Alternatives?"** The highest-value slide on the deck for this page, because **nothing on the site covers it**:

> Narrative (verbal/written)? Tables / numbers? Statistical Summaries? Database query?
> These have a visual component. Methods work together.
> There are cognitive and perceptual differences.

That's the entire "why visualization and not something else" why, and the "methods work together" line pre-empts the obvious objection. (Note the pleasant tension with Tutorial 1's "yes, in my mind a table is a visualization" — the alternatives list treats tables as an alternative *to* vis.)

**Slide 57 — "Pictures can do lots of things."** Six answers to "why visualize," and they map onto the four authors nicely:

> Deliver different kinds of messages / Deliver a message powerfully / Put information together so we can explore / Summarize a lot of information to expose patterns / Provide more information for context / Serve as a cognitive aid / (and lots more)

**Slides 58–59 — "Example: It's Spring!"** followed by one full-bleed image, no text. Can't tell what it is from the extraction. → §5.

**Slide 61 (repeated as 2-W slide 3) — the four-authors summary.** The gem, quoted exactly:

> Cairo (journalist / designer) — because it works if you do it right; because it gives you options – to serve situations
> Tufte (historian / pundit) — Because I told you to do it; Because people will die if you don't
> Ware (perceptual scientist) — Because your eyes are visual system is good!
> Card et al (psychologist / cognitive scientist) — Because your brain needs help!
>
> We didn't read these yet — Which is more reason to discuss them!

Four disciplines, four incompatible answers, none wrong. That's the page's closing move, and it's also the argument for *why the readings are assigned* rather than replaced. (Note the typo in the Ware line; and `02-tufte-snack.md` §4 also claims this slide — decide which page owns it, §7.)

**From 2-W, available as support if the page wants it:**

- Slide 30 — Cairo's six dimensions (abstraction–figuration, functionality–decoration, density–lightness, multi–unidimensional, originality–familiarity, novelty–redundancy), with "**Visualization gives us choices!**" and "Connect to why: Situations where these properties are useful! (reasons for vis)."
- Slides 31–32 — explore vs. explain, "**Not a simple dichotomy!** Often have elements of both"; known vs. unknown message ("Does the author know? Does the viewer know?").
- Slide 33 — the author/audience table (goals, interests, abilities, familiarity with topic, familiarity with data, specificity of message — for each), with "Interaction blurs the distinction."
- Slides 34–35 — "Tasks / Questions / Stories: all get at the same point"; and the signature sentence: "**Exploratory Visualization: What if you don't know what is there? That is still a task!** Choose visualizations that would show something if it was there."

## 5. What to cut / what must survive (MIKE)

- Confirm the split: slides 5–38 are **not** this page (see appendix). Yes/no?
- Slides 58–59, "It's Spring!" — what is that example, and does it survive?
- **ICE call:** the only exercise in this lecture (the chart-naming experiment) is in the *other* half, so the default for this page is "skip" — no try-it box, no mention of class. Confirm? (The stop sign is arguably a try-it: "what's your answer? what do you think mine would be?")
- Does the stop sign stay a separate snack, or does it belong here as the definition-is-judged-by-usefulness section? (I lean *here*, with the snack as the fun expansion — but that's your call and it changes both pages.)
- How much of the 2-W material (Cairo's dimensions, explore/explain, author/audience) belongs on this page vs. staying with 2-W's own document?

## 6. The stories (MIKE)

- Slides 51–53, "**Last Year And This Year**" — what changed between 2024 and 2025 for the water heater? Is that an update to the existing `app-time-graphs` snack rather than material for this page? (And what's the second image in the "Comparison of Visualizations" pair?)
- Slide 42's **Fall-21 discussion** — what did the class actually say about the stop sign? The deck preserves that there *was* a discussion but not its content, and the discussion sounds more interesting than the answer.
- The gap the decks can't fill: for slide 56 ("what are your alternatives?"), **a time you talked someone out of a visualization** — or reached for a table, a number, or a sentence instead — would anchor that section better than anything else. Nothing in any deck has one.

## 7. Contested takes (MIKE)

- **Munzner ch. 1 vs. you.** Her answer to "why vis" is systems-and-human-in-the-loop; yours is "because we think a picture will help — but why do we think that?" Where does your framing actually differ from hers, and is that difference worth stating on the page?
- ~~**The operational definition (slide 41).** Replacement or second definition?~~ **ANSWERED (Mike, 2026-08-22):** *"The two definitions of visualization are intentional — and both useful. I plan to use both. And to acknowledge there are two (which might be confusing) — but one is more operational."*

  So: not a correction. The page **presents both and names the operational one as operational**, and the acknowledgment is itself content — a short aside saying "yes, there are two, here's why that's on purpose, here's when each one earns its keep." Consequences: (1) Tutorial 1 keeps "help some one do some thing" — its revision inherits nothing here, which de-risks that page; (2) this page is where the two-definition fact gets stated, so it's the canonical place both later pages point at; (3) worth working out per-definition *when to reach for which* — "help some one do some thing" is the one that makes you ask about task and audience, "make some things easier to see" is the one you can actually apply to a picture in front of you. Tutorial 3 is built entirely on the second one without calling it a definition ("Ask: what does this visualization make easy to see?"), so the operational definition already has a page depending on it.
- **The Tufte line.** "Because I told you to do it / Because people will die if you don't" is the sharpest sentence in either deck. Publishable as written, or does it need the careful framing that `02-tufte-snack.md` is being built around? Related: **which page owns the four-authors slide** — that brief claims it too, and it can't be the punchline of both.
- **2-W slide 27: "Principles, not rules (this class!)"** — with the worked example ("the obvious problem is axis truncation; the principle is *don't make the wrong thing easy to see*"). Does that live here, as part of "why *good* visualization," or with Tufte?

## 8. Anything else (MIKE)

- **Tutorial 0 collision — decide before drafting.** `queue.md` has *both* "Tutorial 0: the prime directive — make visualizations to address tasks" (stub exists, 126 words) *and* "Most important principles — if you read only one page," and notes those two may be the same page. Add this one and there are three short, overlapping front-door pages in flight. Which is it: is "Why Visualize?" a sibling of Tutorial 0, the content that fills it, or a third thing?
- **The landing-page structure is free.** Tutorial 1's "Now What?" list (9 items) maps almost exactly onto the planned tutorials. Using it as the landing page's spine would make the new collection read as the payoff of Tutorial 1 rather than a parallel set — which might also settle the naming question.
- The four-authors slide characterizes four living authors in one line each, bluntly and by discipline. Fine in a classroom; worth a beat before it goes on the open web under your name.
- Cheap win available regardless: `snacks/app-time-graphs` is published and this lecture uses it. Whatever else happens, this page should link it.

---

## Appendix: the sibling document in this deck (slides 5–38)

**Now has its own brief: `02-vis-basics.md`.** Short version: slides 5–38 are the "what does this
make easy to see, using basic charts" segment — the LLM chart-naming experiment, the
gallery-of-chart-types critique, and the unemployment-by-state walkthrough. Its destination is
deliberately open (own page / the body of Tutorial 3 / stay a lecture), and it carries the
evidence for `queue.md`'s `charts-are-encodings` merge question.
