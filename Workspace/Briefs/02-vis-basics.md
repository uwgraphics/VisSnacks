# Brief: What Different Charts Make Easy to See ("Vis Basics")

*Source: `02-M-Why.pptx` slides 5–38 (Lecture 2-1, Monday 9/8/2025). Full text in `_lecture_experiment/extracted/02M-why-deck-text.txt`. Sibling brief: `02-why-vis.md` covers slides 39–61 of the same deck.*

**Provenance worth keeping:** this segment was improvised. Slide 4 says *"Changed my mind! Decided on a new plan (Vis Basics). A different inspiration this morning."* Slide 5 is "A Change of Topic…" and slide 39 is "Resume Regularly Scheduled Lecture" — you wrote a new opening act that morning and bolted it onto the front of the Why lecture. Mike, 2026-08-22: *"I think I liked it at the time."*

## 0. Destination undecided — on purpose (read this first)

**This might be a lecture, not a page.** That's fine, and it doesn't change §1–4: the brief is an outline of an argument with slide references and open questions, which is a lecture plan and a page plan equally. Only §5 forks. The three candidate destinations:

- **(A) A page of its own.** Tutorial-weight, ~1,200–1,600 words.
- **(B) The body of Tutorial 3.** See §1 — this is the option I didn't see the first time, and I now think it's the strongest.
- **(C) Stay a lecture.** Keep it as the opening act, and let the brief serve as its plan. The LLM experiment is a live exercise that gets better every year, which is a real argument for this (see §5).

Nothing below assumes one of these. Pick after §5.

## 1. The document (agent-filled)

**The lesson, in Mike's words (2026-08-22):** *"different types of charts help you see different things"* — which carries the data-appropriateness and task-appropriateness questions, the need for task, and the motivation for the whole building-blocks approach. And: *"The VisBasics gets at 'what does this make easy to see' in a low entry way (using basic charts)."*

That framing is better than the one I reached for first, and the difference matters. My initial read was **negative** — "chart typologies don't work." Mike's is **positive** — different charts show you different things, therefore you need to know what you're trying to see, therefore task, therefore building blocks. The typology critique is the *consequence*, not the thesis. Lead with the positive version: it's low-entry (everyone already knows what a bar chart is), it earns the critique instead of asserting it, and it doesn't open by telling a beginner that the thing they know is wrong.

**The finding that argues for option (B).** `content/tutorials/3-easy-to-see/index.md` is 1,061 words — small — and it already makes exactly this move, in a section called "Comparing Visualizations":

> The "what does this make easy to see" becomes easier when you have two different visualizations of the same data.

It then does it *once*, with a bar chart and a treemap of the fake student data. That's the whole section. Meanwhile slides 25–35 run the same move five times on one real dataset, with the answers worked out. **The middle of lecture 2 is the missing body of Tutorial 3.** Tutorial 3 has the thesis, the shortcut, and one example; this has the practice. Tutorial 3 also uses the operational definition throughout without ever calling it one — which ties this back to `02-why-vis.md` §7.

Course evidence for the same conclusion: Module 1 learning outcome #2 is *"To get some intuitions about 'what is easy to see' (as a way to appreciate effective visualizations)"* — which is Tutorial 3's outcome, not the encodings pages'. This material serves outcome #2.

**What this is *not*:** an encodings page. `content/modules/encodings/` (drafted) and `content/snacks/charts-are-encodings/` (drafted, 682 words) handle decomposition-into-channels. This is upstream of that — the motivation you'd want a reader to have *before* decomposition looks worth the trouble. Slide 38 is literally the handoff: "Think about charts in terms of pieces — Encodings, Layouts, Transformations, (Interaction)."

## 2. Course fit (agent-filled)

Module 1, "Visualizations and Effectiveness" (Sep 3–10), lecture 2-M, first half. Module 1 outcomes quoted in full in `02-why-vis.md` §2; this material serves **#2** ("intuitions about what is easy to see") and sets up **#1**'s effectiveness half.

Arc: Tutorials 1/2/3 assigned before the lecture → **this** → the Why lecture (same day, second half) → 2-W's reverse-engineering exercise → Module 2's building blocks (data abstraction, task abstraction, encodings — all drafted or briefed). The placement is ideal: it's the argument for why Module 2 exists, delivered one week before Module 2.

Note the neat accident: the lecture assigns Tutorial 3, then opens with an unplanned segment that is Tutorial 3's missing exercise section. Worth deciding whether the page/lecture acknowledges that or just quietly fixes it.

## 3. Sources (agent-filled)

- **Primary:** `02-M-Why.pptx` slides 5–38.
- **Existing VisSnacks neighbors — read all four before drafting, the overlap is real:**
  - `tutorials/3-easy-to-see` (1,061 words) — the thesis this is the body of. "Comparing Visualizations" section is the seam.
  - `tutorials/2-table-example` (1,415 words) — the *same pedagogical shape already executed*: one dataset, four design moves, lessons at the end. If this becomes a page, that page is its structural model. It also says "I usually do this example in lecture" — precedent for publishing a lecture example.
  - `modules/encodings/` + `snacks/charts-are-encodings/` (drafts) — downstream; must not duplicate. The 682-word snack currently carries a compressed version of the typology argument.
  - `tutorials/1-what-is-vis` — the 4-design-moves recipe and "yes, in my mind a table is a visualization."
- **Reading summaries on disk** (`Workspace/Re-Papering/`): Mackinlay 1986 in `summaries-papers.md` — directly relevant to slide 21's "automatic guidance?" open question. Munzner ch. 5/7 in `summaries-munzner.md`. Cairo FA ch. 2 "Forms and Functions" in `summaries-cairo.md`.
- **Not a source:** lecture 4-M. The typology argument in the drafted encodings pages came from there and is thinner; this deck is where it actually lives.

## 4. High-value material in the slides (agent-filled)

**The setup — slides 7–8.** "How do we think about visualizations? *Before you've taken a class on them.*" Then the strawman, stated fairly: "The 'standard' approach: learn a set of standard charts; standard rules for appropriate choices (based on data); standard rules for detail choices." Naming the reader's existing mental model before touching it is what makes this low-entry.

**The experiment — slides 9–15.** Students name 5–10 common chart types from memory ("preferred: just list the names"; "each person – by themselves"; "please do not use your computer"), then compare in table groups (slide 12: "How similar are your lists? What comes up often? What unusual ones came up? … Sketch what they look like — **do you agree on the name?**"). Then the reveal: slide 11 has the verbatim LLM prompts, slide 13 has both answers (ChatGPT's 10, Gemini's 8 — both lists in the extraction), slide 14 the generated cheat-sheet images, slide 18 the annotated versions. Payoff, slide 15: **"Inconsistency in naming. Names don't mean much."**

The LLM-as-third-participant structure is good: it's not "AI is wrong," it's "here are three independent attempts at a supposedly standard vocabulary — compare them." → §5, this slide group is the whole page-vs-lecture fork.

**The gallery critique — slides 16–20.** Repeated twice (16 and 17, once with the image), framed as four questions a gallery can't answer:

> Catalog a lot of different charts / Rules/guidance where each apply
> **Remember these names? (agree on names?) · Compare options? · Generate new alternatives?**

"Generate new alternatives?" is the one that does the real work — it's the whole case for building blocks in two words. Exhibits: slide 19 Excel's chart menu ("What can you do in excel? (Chart Typology)"), slide 20 "And a growing list…".

**Slide 21 — the steelman.** "Standard Designs: Library of designs · Fixed choices · Automate details (well chosen). **Open Questions: More flexibility? Automatic guidance?**" Worth keeping — it concedes that typologies *work*, and that automating good defaults is a real research direction, not a mistake. Mackinlay territory; summary is on disk.

**Slide 22 — the thesis under examination, stated so it can be tested:** "**Charts are appropriate for data types (task second).**"

**Slides 25–35 — the walkthrough. This is the spine.** One dataset (unemployment by state: "Table (discrete set) / States / Continuous value per State"), run through six designs, each annotated with what it encodes:

| slide | design | the deck's annotation |
|---|---|---|
| 26 | bar chart | discrete axis × continuous axis |
| 27 | dot plot (?) | same axes — "**Choice of Mark**" |
| 28 | — | "Building intuitions: compare" |
| 29 | line chart (?) | continuous × continuous |
| 30–31 | inappropriate line chart | crime types per state |
| 32 | the rescue | "Line charts 'inappropriate'? **not so fast…** Lines for connections, not to convey continuity → Parallel Coordinates (not lines for discrete)" |
| 33 | packed bubble | "Continuous value → Size; Position to create packing" + "(bubble can mean scatter)" |
| 34 | bubble, judged | "**Appropriate for data type. Ineffective for task (?)**" |
| 35 | — | "Is a bar chart effective?" |

Slide 34 is the kill shot on slide 22's thesis, and slide 32 is the better move: the "inappropriate" verdict gets **reversed** one slide after it's delivered, which teaches that the rule was never the point. The question marks in "Dot Plot (?)" and "Line Chart (?)" are doing work too — the names are being held at arm's length as they're introduced.

Note this is the *same* dataset-through-many-designs structure as Tutorial 2's four design moves, and the same compare-two-views structure as Tutorial 3's bar-vs-treemap. Three pages, one pedagogical move. That's a house style, and it's worth naming as one.

**Slides 36–38 — the landing.** "Choices Matter…" → "Tell a story / Design for a task" → the forward pointer: "Reverse engineer charts (Wednesday) — think about tasks. Think about charts in terms of pieces: Encodings, Layouts, Transformations, (Interaction)."

**Slides 23–24 — the two-slide preview** of data and task abstraction ("next week"). Class-schedule scaffolding; drop it on a page, keep it in a lecture.

## 5. What to cut / what must survive (MIKE)

**The one decision that settles everything: does the LLM experiment (slides 9–15) get published?**

- **As a lecture** it's the best part and it stays. It's a flagship recurring exercise, it's re-runnable every year, and it gets *better* each year as the models change. `lecture-mining-plan.md` puts flagship exercises on the do-not-spoil list for exactly this reason.
- **As a page** it has a shelf-life problem in both directions: slide 13's ChatGPT/Gemini lists are a dated 2025 artifact (charming as a snapshot, stale as a claim), and publishing the setup spoils the classroom version. A page could keep the *finding* ("ask three sources for the standard chart names and you get three different lists — try it") as a try-it box without printing the 2025 answers.

That fork is most of the page-vs-lecture question. Everything else is smaller:

- Slides 23–24 (next-week preview) — cut for a page, keep for a lecture.
- Slide 19's Excel screenshots — dated and rot-prone; the Excel menu changes. Redraw, or make the point without the screenshot?
- Does the walkthrough keep the real unemployment data, or move to fake data? (The drafted encodings pages use generated fake data throughout, and say so.) Real data is more convincing and dates faster.
- If this becomes Tutorial 3's body: does Tutorial 3 keep its NYT clean-energy example and bar-vs-treemap pair, or do those give way to the unemployment sequence? (My read: keep both — NYT is the critique-a-real-thing practice, unemployment is the compare-many-designs practice. They're different exercises.)

## 6. The stories (MIKE)

- Slide 4 says a "different inspiration this morning." **What was the inspiration?** The story of *why you decided to open the course this way* is the kind of thing only you have, and it would justify the segment's existence better than any argument I can construct for it.
- The unemployment dataset — is there a reason it's that one? A real question you had about it?
- Slide 32's reversal ("not so fast…") — is there a case where you actually got talked out of an "inappropriate chart type" verdict, or talked someone else out of one? That reversal is the segment's best teaching moment and it currently has no anecdote attached.

## 7. Contested takes (MIKE)

- **How much credit do typologies get?** Slide 21 concedes real value (libraries of designs, well-chosen defaults, automatic guidance as a live research question) — and you list Excel as your favorite visualization tool in Tutorial 1. Where exactly is the line between "typologies are a fine tool" and "typologies are the wrong way to *think*"?
- **"Names don't mean much" vs. Cairo FA ch. 2 "Forms and Functions"**, which is required for this module and is fairly comfortable with taxonomy. Is there a disagreement to state, or do they just have different jobs?
- Slide 22's "charts are appropriate for data types (**task second**)" — is "task second" your characterization of the conventional view, or a fair description of what Munzner ch. 7 actually does? Worth being precise, since this material will be read by people who've just read her.
- Anything to say about using LLM output as *classroom evidence* rather than as a tool? That's a small methodological stance and it's implicit in slides 11–18.

## 8. Anything else (MIKE)

- **Pick a destination** (§0: own page / Tutorial 3's body / stay a lecture). If Tutorial 3, this stops being a new page and becomes a revision — which changes how it interacts with the Tutorial-1 split, since Tutorial 3 was previously assessed as "right-sized" and would no longer be.
- **The merge decision this unblocks:** `queue.md` asks whether `charts-are-encodings` (drafted) merges with the old "Chart Typologies" idea. Whatever happens here, the compressed typology argument in that 682-word snack is the *thin* version of this material and should probably give way to a pointer.
- The one-dataset-many-designs structure now appears in three places (Tutorial 2's four moves, Tutorial 3's bar-vs-treemap, this walkthrough). Naming it as a house move — and cross-linking the three — might be worth more than any one of the pages.
- If it stays a lecture: this brief is its plan, and nothing else in the project needs to change. Say so and I'll mark it that way in `queue.md` rather than leaving it in the page backlog.
