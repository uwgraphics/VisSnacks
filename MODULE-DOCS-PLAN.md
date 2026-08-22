# Plan: Lecture-Replacement Tutorials for Weeks 1–7 (CS765 Modules 1–4)

Working plan for the lecture-replacement writing project. Not site content. Revised 2026-07-17 after Mike's feedback. Sources: 2025 lecture decks, course module pages (https://pages.graphics.cs.wisc.edu/765-25/modules/), existing VisSnacks content.

Per-page briefs (template + pre-filled starters) live in `Workspace/Briefs/`.

## Guiding distinctions (decided)

**VisSnacks vs. class.** VisSnacks is the textbook: timeless resources for everyone, that the class happens to be built around. The test for content: *is this useful to a reader who isn't in CS765?* Semester-specific material (schedules, assignments, this-year's-data walkthroughs, tool links that rot) stays on the course web; the knowledge goes in VisSnacks. Some redundancy between pages is acceptable, especially for the "why" backbone.

**One collection, not two. — SETTLED 2026-08-22, and executed.** The new documents are *tutorials* in the existing collection. `content/modules/` is gone; the two drafts now live at `content/tutorials/encodings/` and `content/tutorials/data-abstraction/` at `weight` 30/31 — an unordered tail after the core sequence (1–4) and the Tableau class-support pages (10–20). Rationale: "module" is a *course* word, and the course is redesigned yearly; publishing it would have baked one year's class structure into permanent URLs. Ordering lives in `weight`, not in titles — so the tail stays additive. The "start here" framing for 1–4 is prose Mike writes in `content/tutorials/_index.md` (still to do), not a tag: a tag can't express order or *why this one next*.

**In-class exercises.** Default: convert to short "Try it yourself" boxes. Use "in class, we often do this as an exercise" sparingly — it risks stealing the class's thunder. Per-page call, recorded in the brief.

**The goal of the project.** Two things: (1) get the material that exists *only* in lectures into writing, so lecture time can be spent on better things; (2) give the main points of the readings, so the assigned readings can be focused (or optional).

## Proposed documents

Ordered by the course arc. ★ = drafting priority.

### Module 1: Visualizations and Effectiveness

1. **Revise Tutorial 1 (What is Vis)** — *revision, not new.* 6,700 words; more meal than snack. Candidate extractions: "Is a stop sign a visualization?" (definition edges) as a snack; possibly "why visualize" as its own page. "Why" is the backbone of the class, so redundancy across pages is OK; how this falls depends on seeing the whole set — do this revision *last*. Tutorials 2 and 3 look right-sized.
2. **Snack: Learning from Tufte (carefully)** — confirmed, do regardless. What to take from Tufte, what to filter, Cairo as counterweight. Tone challenge: harder to be critical on the open web than in class — frame as "how to read Tufte," critique-the-work applied to Tufte himself. See brief.

### Module 2: Building Blocks

3. ★ **Tutorial: Data Abstraction** — types of data (tables/fields/networks), attributes, NOIR, conversions. The course module page already promises a "data abstraction cheat sheet." NOIR may be the spin-off snack.
4. ★ **Tutorial: Task Abstraction** — why task matters, the space of task descriptions, action×target, low-level tasks; "use formalisms when they are useful, don't get stuck on their details." Hardest without Mike; highest leverage. Related: finish **papers/problem-space** (assigned reading, currently a notes draft).
5. **Tutorial: Encodings** — DRAFTED (`content/tutorials/encodings/`), plus drafted snack charts-are-encodings. Pending merge/differentiate decision vs. queue.md's "Chart Typologies" idea. Retro-brief now exists (`Workspace/Briefs/04-encodings-review.md`) consolidating every open review edit — these were the pilot pages and never got a brief.
6. ~~**Snack: Composing designs (the 2-numbers exercise)** — split only if the encodings page needs shortening.~~ **REFRAMED 2026-08-22** after extracting 4-W and 4-2: this isn't a Try-It box's worth of material, it's a two-lecture progression (2 numbers → scatterplot → parallel coordinates → +categorical → 3D), and it's only *half* a document — the other half decomposes Playfair, Minard, and a Cairo design problem. Proposed as a tutorial, not a snack: `Workspace/Briefs/04-encodings-practice.md`. If it exists, the encodings page's "Try It" box becomes a pointer.
7. **(No doc for the walkthrough)** Tableau lecture — the how-to is class-support, not VisSnacks-timeless, and two walkthrough tutorials already cover it. But the *someday-snack* now has a brief (`Workspace/Briefs/04-tableau-embodied.md`): "Tableau is the theory, embodied" isn't about Tableau, it's the argument that the encodings framework is real enough that a commercial product runs on it. Keep it UI-free and it doesn't rot. Smallest genuinely-new week-4 document.

### Module 3: Implementation and Scale

8. **Tutorial: Implementation (choosing tools)** — kinds of tools, level of abstraction, expressiveness vs. ease-of-use. Deliberately timeless: the *space* of tools, not the tools (those rot; they stay on the course page).
9. ★ **Tutorial: Too Much Stuff (scale)** — challenges (many/big/complex) and strategies (scan/subset/summarize); "you are throwing information away — do it wisely." Connects to, doesn't repeat, papers/comparison. Spin-off snacks: **"Where you put the bins changes the story"** and **"Overdraw."**
10. **(Defer)** Comparison design — papers/comparison + the rivers-map critique carry it for now.

### Module 4: Evaluation

11. ★ **Tutorial: Evaluation** — why evaluation is hard, evaluating what ("visualizations vs. systems vs. research"), the "Convince [who] that your [what] is [good how]" frame, the nested model, what can be measured. Connects to papers/algebraic.

### Cross-cutting

12. **Landing page** for wherever the new tutorials live — what these documents are, for students and outsiders. Blocked on the section-naming decision.

## Process (decided)

- **Batching:** draft 2–3 documents per session, review together.
- **Briefs:** before drafting, Mike spends ~5 minutes per brief in `Workspace/Briefs/`. The agent pre-fills everything recoverable from materials (module fit, learning goals, source mapping, notable slides); Mike fills the parts only he has (stories, cut/keep calls, contested takes).
- **Order:** Data Abstraction → Task Abstraction → Too Much Stuff → Evaluation → Implementation → Tufte snack → Tutorial-1 revision.
- Standard guardrails from STYLE-GUIDE.md: draft=true, uncommitted, verification list, genai disclosure.

## Remaining open questions

1. ~~Where do the new tutorials ultimately live, and do they get numbers?~~ **ANSWERED 2026-08-22 and executed** — `content/tutorials/`, `weight` 30+, no numbers in titles. See "One collection, not two" above. Remaining sliver: Mike writes the "start here" prose in `content/tutorials/_index.md`, and Tutorial 0 (draft stub) has no `weight` yet, so it currently sorts last.
2. Merge or differentiate: charts-are-encodings snack vs. queue.md's "Chart Typologies - it works no matter what you call it."
3. ~~The 2024 story in lecture 2-M (slides 49–53) — what is it, and which page does it belong to?~~ **ANSWERED (2026-08-22, via `Workspace/Briefs/02-why-vis.md`):** it's the AO Smith water-heater app, and it's already a published page — `content/snacks/app-time-graphs/` (2024-09-09), paired against the Garmin steps graph. New pages should link it, not re-tell it. Still open, smaller: slides 51–53's "Last Year And This Year" has material the snack doesn't (needs Mike).
