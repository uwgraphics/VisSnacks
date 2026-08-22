# VisSnacks Queue

Unordered todo list. Pointers: **(PLAN)** = `MODULE-DOCS-PLAN.md` · **(BRIEF)** = starter brief in `Workspace/Briefs/` · **(MINE)** = analyzed in `_lecture_experiment/lecture-mining-plan.md` (slide refs, figure candidates) · **(SUMM)** = AI reading summary ready in `Workspace/Re-Papering/summaries-*.md` · **(DRAFT)** = draft page exists, needs review.

## Mike's ordering - Claude doesn't touch - Things detailed below

Order by importance for class.
- [ ] Look at 0718 - it has a "next steps for mike"

From 0718
- [ ] Review encodings
- [ ] Review data abstraction
- [ ] Review charts-are-encodings
- [ ] Try looking at briefs

Useful at start of class
- [ ] Tutorial 0
- [ ] Tutorial 1 Split
- [ ] Critique Tutorial (pull in more book stuff, ready for class)
- [ ] Re-papering rant
- [ ] Favorite visualization

Building Blocks pages
- [ ] Abstraction definition from 765-25
- [ ] Data Abstraction tutorial
- [ ] Task Abstraction
- [ ] Repapering Task Cubes
- [ ] Repapering Munzner Tasks
- [ ] Repapering Problem Space
- [ ] Encodings Tutorial
- [ ] Charts are encodings
- [ ] Graphical Perception Tutorial (C&M repapering might be separate)
- [ ] Low-level tasks


## Finish what's started

- [ ] Encodings tutorial — review draft; pending edits: real terms for "Pareto mapping" + genai credit line; publish together with charts-are-encodings (cross-linked) (DRAFT, PLAN) — `content/tutorials/encodings/index.md`
- [ ] Charts Are Just Encodings in Disguise — review draft; decide merge-vs-differentiate with the old "Chart Typologies" idea. **New evidence** (`Workspace/Briefs/02-vis-basics.md`): the real argument is in lecture 2-M slides 5–38 (the LLM chart-naming experiment + the unemployment walkthrough), not 4-M — a tutorial's worth, which would swamp this 682-word snack. The compressed version here is the thin one and should probably become a pointer (DRAFT) — `content/snacks/charts-are-encodings/index.md`
- [ ] Data Abstraction tutorial — review draft; verify NOIR cheat-sheet table; decide if NOIR splits into its own snack; wants figures (DRAFT, BRIEF, report in Workspace/Briefs/) — `content/tutorials/data-abstraction/index.md`
- [ ] Pie Chart Experiment — long-standing draft snack; the perception/evaluation pages will want to link it (DRAFT) — `content/snacks/pie-chart-experiment/index.md`
- [ ] My Favorite Visualization: rivers & mountains comparison — draft critique (DRAFT) — `content/snacks/260520-compare-rivers/index.md`
- [ ] Re-Papering rant — draft explains the whole re-papering section; publish when first re-paperings do (DRAFT) — `content/rants/repapering/index.md`
- [ ] Problem Space paper page — replace the NotebookLM notes with a real page (DRAFT, SUMM) — `content/papers/problem-space/index.md`

## Core tutorial sequence (cleanup + the missing front door)

- [ ] Tutorial 0: the prime directive — "make visualizations to address tasks." Working framing: what is vis? — and why the answer tells you how to do it and how to learn it. (The run-on-ness of that sentence is exactly Tutorial 1's disease; Tutorial 0 is the cure: one idea, short.) Stub exists at tutorials/0-how-to-vis (DRAFT stub) — `content/tutorials/0-how-to-vis/index.md`
- [ ] Split Tutorial 1 — 6,700 words → some goes into Tutorial 0; keep a tightened core (definition, effectiveness); spin out pieces below; best done AFTER other tutorials exist to absorb material (PLAN, BRIEF: tutorial-1-revision) — `content/tutorials/1-what-is-vis/index.md`
  - [ ] Why Visualize? — **brief written** (`Workspace/Briefs/02-why-vis.md`): the four whys as the skeleton, "what are your alternatives?" is the slide nothing on the site covers, four-authors summary is the closer. Checked: Tutorial 1 poses this question in its "Now What?" list and never answers it, so redundancy risk is low — this is a real page, not Tutorial-1 leftovers. Needs §5–8 + the Tutorial 0 collision decision (BRIEF, MINE)
  - [ ] Is a stop sign a visualization? — definition-edges snack; the brief argues it may belong *in* Why Visualize instead (definition judged by usefulness, not correctness) (BRIEF, MINE)
- [ ] Most important principles — "if you read only one page" snack; relation to Tutorial 0 needs deciding — may be the same page
- [ ] "Vis Basics" / What Different Charts Make Easy to See — 2-M slides 5–38: LLM chart-naming experiment, gallery critique, unemployment-by-state walkthrough. **Destination undecided on purpose: own page, the body of Tutorial 3 (1,061 words — it has the thesis and one example; this is the missing practice), or stay a lecture.** The fork is whether the LLM experiment gets published — as a lecture it's re-runnable yearly and improves; as a page it spoils a flagship exercise and dates. §1–4 done (BRIEF: vis-basics)
- [ ] **"Start here" prose in `content/tutorials/_index.md` — MIKE writes this.** No longer blocked: the structure is settled (2026-08-22). The collection is one `tutorials/` section — core sequence 1–4 (`weight` 1–4) reads in order, unordered deeper tail at `weight` 30+, Tableau class-support between. What's needed is the framing paragraph plus the ordered "start here" list; a tag can't carry order or "why this one next," so it's prose. Currently one sentence long — `content/tutorials/_index.md`
- [ ] Give Tutorial 0 a `weight` when it's written (no weight today, so it sorts *last* in the collection — presumably wants 0) — `content/tutorials/0-how-to-vis/index.md`

## Lecture-derived tutorials, weeks 1–7 (briefs exist — fill §5–8 to unblock)

- [ ] Task Abstraction — highest leverage; "task first" has no home page (PLAN, BRIEF)
- [ ] Too Much Stuff (scale) — strategies + throwing-information-away-wisely; connects to comparison paper page (PLAN, BRIEF; Munzner ch. 13/14 SUMM)
- [ ] Evaluation — nested model + "Convince [ ] that your [ ] is [ ]" (PLAN, BRIEF; Munzner ch. 4 + North + Cairo TT2 SUMM)
- [ ] Implementation: choosing tools — timeless space-of-tools, expressiveness vs. ease (PLAN, BRIEF)
- [ ] Learning from Tufte (carefully) / How to Read Tufte — snack; needs tone calibration (PLAN, BRIEF; Tufte VDQI ch. 1 + Cairo FA3 SUMM)

## Lecture-derived tutorials, weeks 8–15 (MINE has slide refs; briefs not yet made)

- [ ] Perception for Vis: the fast and the slow — pop-out, attention, "design to use the fast mechanisms" (MINE; Munzner ch. 5/6 + Cairo FA5/FA6 SUMM)
- [ ] Why Vis Works (cognition) — Card/Mackinlay/Shneiderman amplify-cognition material; overlaps Why Visualize — decide ownership (MINE; CMS summary pending)
- [ ] Vis & Statistical Thinking — descriptive vs. generalization, multiple comparisons, model-vis (MINE; Leek&Peng/Shmueli/Zgraggen summaries pending)
- [ ] Color crash course — physics→perception→systems→use; LAB is why theory matters (MINE; Munzner ch. 10 SUMM)
- [ ] Too Many Dimensions — glyphs, parallel coords, SPLOMs, scan/subset for dimensions (MINE; Munzner ch. 13 SUMM)
- [ ] Embeddings & Dimensionality Reduction — PCA to UMAP; "is it meaningful?"; timely beyond class (MINE)
- [ ] Graphs Are Not (Just) Node-Link Diagrams — matrices, reordering, tasks; links route-maps critique (MINE; Munzner ch. 9 SUMM)
- [ ] How Node-Link Layout Actually Works — heuristics→objectives→force-directed (MINE)
- [ ] Interaction (and its costs) — builds around existing interaction-costs paper page (MINE; Munzner ch. 11/12 SUMM)
- [ ] The Third Dimension (a taste) — "we sense 2D, we infer 3D"; depth cues (MINE; Munzner ch. 6/8 SUMM)
- [ ] Fields, contours, volumes — MIKE'S CALL whether the site needs it (MINE; Munzner ch. 8 SUMM)
- [ ] The Talk on Talks (presentations) — The List + its origin story; job-talk history section is Mike's call (MINE)
- [ ] Design School in a Day — contrast/repetition/hierarchy; links design books resource (MINE)
- [ ] Uncertainty: what it is before how to draw it — uncertainty vs. distributions; "uncertainty vis == model vis?" (MINE)

## Snack candidates (self-contained sidebars; mostly from MINE with slide refs)

- [ ] Find the red dot (pop-out demo)
- [ ] The eye is not a camera (retina bandwidth, computer-systems framing)
- [ ] Can you see the average? (visual proxies — verify whose studies)
- [ ] Stream graph aggregation gotcha (from a real student question)
- [ ] Why the rainbow colormap misleads ("use order for order!")
- [ ] Metamers, or how displays fake out your eyes
- [ ] How many colors can you actually use?
- [ ] Parallel coordinates: order really matters
- [ ] Radar charts vs. star coordinates
- [ ] What does distance mean in an embedding?
- [ ] Scagnostics: finding the interesting scatterplots
- [ ] Reorder the matrix, reveal the structure (Bertin tie-in)
- [ ] Venn diagrams don't scale (UpSet does)
- [ ] Animation: use with caution ("How you will die")
- [ ] Why does the light come from above?
- [ ] The Curse of Knowledge
- [ ] What do slides actually do?
- [ ] The weather forecast problem (conveying a prediction)
- [ ] Where you put the bins changes the story (spin-off of Too Much Stuff) (PLAN)
- [ ] Overdraw (spin-off of Too Much Stuff) (PLAN)
- [ ] Expressiveness vs. ease of use (spin-off of Implementation) (PLAN)
- [ ] NOIR levels of measurement (possible split from Data Abstraction)
- [ ] Composing designs: the 2-numbers exercise (only if split from encodings page) (PLAN)
- [ ] Tableau is the theory, embodied (someday)
- [ ] Bates Cairn (concept)
- [ ] How to critique experiments (concept — pairs with pie-chart-experiment and Evaluation)

## Re-paperings (AI summary sections ready unless marked pending)

- [ ] Cleveland & McGill (both papers, probably one page) (SUMM)
- [ ] Shneiderman, The Eyes Have It (SUMM)
- [ ] Amar/Eagan/Stasko low-level tasks (SUMM)
- [ ] Mackinlay 1986 (SUMM)
- [ ] Bertini, Beyond Precision (SUMM — maybe resource page rather than re-papering)
- [ ] North, Toward Measuring Visualization Insight (SUMM)
- [ ] Card/Mackinlay/Shneiderman intro; Leek & Peng; Shmueli; Zgraggen (summaries pending — see `Workspace/Re-Papering/status.md`)
- [ ] Possible: averages/visual-proxies papers, scagnostics, embedding-guidance papers (surfaced by MINE; verify which)

## Things I want to do

- [ ] Terrible Treemap (started - in critiques) https://www.insidehighered.com/news/students/academics/2025/08/29/survey-college-students-views-ai#
- [ ] The Unreasonable Effectiveness of Pie Charts
- [ ] Are tables visualizations? (Yes. and it is useful to think of them that way. And to think of other vis as tables (bar charts, matrices))

## Done

- [x] NYT map critique
- [x] Yeping's Graph critique
- [x] Cairo Lines snack
- [x] Chart Typologies → absorbed into Charts Are Just Encodings in Disguise (pending the merge decision above)
