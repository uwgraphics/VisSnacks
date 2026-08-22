# Brief: Encodings Practice — Taking Designs Apart and Putting Them Together

*Sources: `04-W-Encodings-Tableau.pptx` slides 4–19 (Lecture 4-W, Wednesday 9/24/2025) and `04-2-AbstractionEncodings.pptx` slides 3–68 (Lecture 4-2, "Encodings Practice," 9/28). Full text in `_lecture_experiment/extracted/04-W-Encodings-Tableau-deck-text.txt` and `…/04-2-AbstractionEncodings-deck-text.txt`, both extracted 2026-08-22.*

## 1. The document (agent-filled)

Tutorial-weight, ~1,200–1,700 words, `content/tutorials/encodings-practice/` at `weight` 32 (immediately after `encodings` 30 and `data-abstraction` 31).

**The thesis is on a slide.** 04-2 slide 60, titled "Lessons," verbatim:

> Even complex visualizations can be broken into encodings
> These building blocks are useful in understanding
> **Design by choosing encodings**
> **Re-Design by changing choices**

That's a page. The encodings tutorial establishes *that* designs decompose; this one is the **practice** — and it runs the move in both directions, which is what makes it a document rather than an exercise:

- **Compose** (04-W 4–19, 04-2 30–50): start from a data abstraction, generate designs. 2 numbers per row → scatterplot → labelled scatterplot → parallel coordinates → add a category (R,R,C) → multi-class scatterplot / nested axis → 3 continuous → 3D and its discontents.
- **Decompose** (04-2 51–68): take famous complex visualizations apart. Playfair 1786, Minard's Napoleon march, then a real design problem with Cairo's published solution.

Compose and decompose are the same skill run in opposite directions, and the deck already pairs them. Don't split them.

**Relationship to what exists.** `MODULE-DOCS-PLAN.md` item 6 proposed "Snack: Composing designs (the 2-numbers exercise)" as a possible split from the encodings tutorial's "Try It Yourself" box, to be decided after review. **The decks change that calculus:** the 2-numbers material isn't a box's worth, it's a two-lecture progression with a worked answer at each step, and it's only *half* of this page. My read: this is a tutorial, not a snack, and the encodings page's "Try It Yourself" box becomes a pointer to it. See §8 for the alternative.

**Not in scope:** 04-W slides 20–29 (Tableau) — sibling brief `04-tableau-embodied.md`.

## 2. Course fit (agent-filled)

Module 2, "Building Blocks of Visualizations" (Sep 15–26). Lectures 4-W and 4-2.

Serves Module 2 outcome #4, quoted from the module page: **"be able to describe a range of different visual encodings and describe visualizations in terms of these building blocks."** The encodings tutorial covers the first clause; *this* page is the second clause — describing actual visualizations in terms of building blocks is exactly what slides 51–68 do. The module description also promises students "engage in pen-and-paper design work," which is what the compose half is.

Arc: encodings (4-M) → **this** (4-W first half, 4-2) → Tableau as the tool that embodies it (4-W second half) → Module 3.

**Provenance oddity worth resolving (§5):** 04-2 is dated "September 28th," six days after 4-M and four after 4-W, and Module 2 ends Sep 26 — so it falls in Module 3's window. Sept 28 2025 was also a *Sunday*. And 04-2 duplicates large stretches of both earlier decks. It reads like a consolidated re-run or a prep deck, not a third delivered lecture. **[MIKE: was 4-2 actually delivered, and if so when?]**

## 3. Sources (agent-filled)

- **Primary:** `04-W-Encodings-Tableau.pptx` 4–19; `04-2-AbstractionEncodings.pptx` 3–68 (the tail, 51–68, is unique to this deck).
- **Existing VisSnacks pages this builds on:** `tutorials/encodings` (drafted — the concepts), `tutorials/data-abstraction` (drafted — the data types this page starts *from*; the compose half is literally "given this abstraction, what designs?"), `snacks/charts-are-encodings` (drafted — one worked decomposition), `tutorials/2-table-example` (**the structural model: one dataset, four design moves, lessons at the end** — this page is the same shape with a harder dataset).
- **Readings, all summarized on disk:** Munzner ch. 5 and ch. 7 (`summaries-munzner.md`) — ch. 7 "Arrange Tables" is the direct support for the compose half; Cairo *TT* ch. 5 (`summaries-cairo.md`); Mackinlay 1986 (`summaries-papers.md`) — 04-2 opens on him, and the automation question ("given the data type, can you automatically design the chart?") is his.
- **Tufte:** `summaries-tufte.md` now has "Visual and Statistical Thinking" (the Minard/Snow chapter) — relevant to the decompose half, and it's an optional Module 2 reading.
- **Attribution to check:** 04-2 slides 51 and 54 credit **Dominik Moritz** for the Tufte-example decompositions ("Tufte Examples from Dominik Moritz", "From Dominik Moritz – originally from Tufte?"). Borrowed teaching material with an uncertain chain — needs sorting before publication. → §8.

## 4. High-value material in the slides (agent-filled)

### The compose half

**The setup — 04-W slide 4 / 04-2 slide 30.** "A First (easy) challenge… Table: 2 numbers per row," then the data characterized aloud: "Continuous / Limited range / Interval/ratio (?) / Non-diverging," plus "May help to know more: Implied nominal / Discrete set of rows / **Row number is 'name'**" and the note "May help to make this explicit." That last move — noticing the row index is itself an attribute — is the good bit, and it's the payoff of having done data abstraction first.

**Slide 5 — "Example data: Useful to make concrete. Don't worry about exact values (we're sketching)."** Sets the working mode for the whole page.

**The progression**, each slide stating its mapping explicitly:

| slide (4-W / 4-2) | design | the mapping, verbatim |
|---|---|---|
| 6 / 32 | "Scatterplot" | Var 1 → X axis; Var 2 → Y axis; each row is a dot |
| 7 / 33 | labelled | "What if we cared about names?" → label elements, could be interactive; "if we cared about precise reading… could give numbers" |
| — / 34 | *the constraint* | "**Swapping X and Y is not a new design!** Not another table. Sketch!" + "Consider: different encodings / different uses of position" |
| — / 38–40 | the pivot | "Some thoughts on Layout: **Axes are orthogonal. Do they have to be?**" → "Parallel Coordinates?" → "Side by side? What does this show? What doesn't this show?" |
| 9 / 41 | parallel coords | Var 1 → Y; Var 2 → Y; **Axis → X**; Rows → Marks. "Takes some getting used to. Scales well to more dimensions **(?)**" |
| 11 / 43 | + derived color | "Interval → Color — **Derive!**" |
| 13 | exercise | "Same data (rational, rational) – but add a categorical value… (R,R,C), assume C is binary. Come up with a few different designs" |
| 14 / 45 | multi-class | "Multi-class scatterplot. Other ideas? Different glyphs (shape, …) Different layouts?" |
| 15 / 46 | nested axis | "Two class scatterplot / Nested Axis (shows 2 variables)" |
| 16–17 / 47–48 | 3 continuous | "N × R × R × R" → "3D? Use 3 orthogonal axes, project into 2D" → "**Rarely a right answer**" |
| 18 / 49 | exercise 2 | "Come up with other designs (quickly — 2–3). **What are they good for (or not)**" |

Two things carry the page. First, **"Axes are orthogonal. Do they have to be?"** is the whole move — parallel coordinates arrive as the *answer to a question*, not as a chart type to be memorized. Second, **"Swapping X and Y is not a new design"** is the rule that makes the exercise teach anything, and it's the kind of constraint a reader inventing designs alone would never impose on themselves.

Note also the hedges you left in: "Interval/ratio **(?)**", "Scales well to more dimensions **(?)**", "**Rarely** a right answer." Worth preserving — they're the anti-dogmatic voice, on the slide.

### The decompose half (04-2 only)

**Slide 3 — the frame:** Mackinlay 1986, "What task(s) is each of these good for?"

**Slides 51–59 — "More Decompositions."** Playfair 1786, decomposed on slide 53: "X-axis: year (Q) / Y-axis: currency (Q) / Color: imports/exports (N, O)". Then Minard 1869, Napoleon's march (slide 54). Both credited to Dominik Moritz. Historical, famous, and decomposing them is the strongest possible demonstration that the building blocks are general.

**Slide 60 — "Lessons."** The thesis; quoted in §1.

**Slides 61–68 — the authors design problem.** "Authors / Years lived / How old when wrote each 'major work'" → "What? What is the data? What is the encoding/design?" → "**You can do better!** Come up with other designs. Come up with a task, and a design? *When do authors write their first masterpieces? When do authors write their second (third…) masterpieces?*" → "**Cairo's Solution**."

That ending is the best structure in either deck: a real published design, an invitation to beat it, task-shaped questions to aim at, and then the professional's answer to compare against. It's Tutorial 2's shape at a harder difficulty, and it closes the loop back to a required reading.

## 5. What to cut / what must survive (MIKE)

- **Which deck is the source of record?** 4-W and 4-2 overlap heavily (see §2's dating oddity). If 4-2 was never delivered, its unique tail (51–68) is unpublished material rather than a re-run — which makes it *more* valuable, not less.
- **ICE call, and it's the big one here.** This material is *entirely* exercises — "Design Exercise 1," "Design Exercise 2," "Exercise," "What did we get?", "You can do better!". `lecture-mining-plan.md` protects flagship recurring exercises from being spoiled, but per the plan's default, exercises convert to "Try it yourself" boxes. A page made of nothing but try-it boxes is either the best thing on the site or a spoiler. Which?
- Slides 36–37, 62–63, 55–59 are image-only ("What did we get?" and the answer galleries). Are those student answers from class? If so they're on the do-not-publish list and the page needs its own worked answers.
- Does the authors/Cairo problem survive, given it's Cairo's published example and solution? (Reproducing his figure is a rights question; describing the problem and pointing at the book is not.)

## 6. The stories (MIKE)

- **"Cairo's Solution"** — what do you actually think of it? The page needs your verdict, not just the reveal. Do you prefer one of the class's designs?
- The 3D section lands on "rarely a right answer" — is there a specific 3D design that burned you, or one that genuinely worked?
- Parallel coordinates: you write "takes some getting used to." Did *you* get used to them, and do you reach for them in real work? (This also settles the encodings page's "best of a bad lot" edit.)

## 7. Contested takes (MIKE)

- **"Swapping X and Y is not a new design."** Defensible as stated? A reader could argue orientation changes what's easy to see (and your own Pareto-mapping point is that *ordering* is a real design choice, so why isn't orientation?). Worth either sharpening or qualifying.
- **The automation question** — "Given the data type, can you automatically design the chart?" Mackinlay says largely yes; the whole 2-M typology critique says the catalog can't "generate new alternatives." Where do you land? This is the same tension as `02-vis-basics.md` §7, from the other side.
- 04-2 slide 45 offers "different glyphs (shape, …)" as an idea to generate. Munzner ranks shape poorly. Is the exercise deliberately letting people propose weak designs so they can discover why?

## 8. Anything else (MIKE)

- **Decide with `04-encodings-review.md`, not separately.** If this page exists, the encodings tutorial's "Try It Yourself" box becomes a pointer, and `MODULE-DOCS-PLAN.md` item 6 ("Composing designs" as a snack) is answered — it's a tutorial, not a snack. Alternative if you'd rather stay small: publish only the compose half as the snack item 6 imagined, and hold the Playfair/Minard/Cairo decompose half for later. That leaves slide 60's "Lessons" homeless, which is why I don't prefer it.
- **Dominik Moritz attribution** needs sorting before publishing — slides 51/54 credit him for the decompositions, with "originally from Tufte?" as an open question in your own deck. Either re-derive the decompositions from the original images (Playfair and Minard are public domain) or get his OK.
- Figures: the compose progression is all sketchable with matplotlib on fake data, the way `Workspace/Tools/figs.py` already does for the encodings pages — cheap, and it avoids reusing class images of unclear provenance.
