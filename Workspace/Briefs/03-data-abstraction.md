# Brief: Data Abstraction

## 1. The document (agent-filled)

Tutorial. Working title: "Data Abstraction: Describing Data So We Can Use It." Placeholder location `content/tutorials/data-abstraction/`. Snack-tutorial length (shorter than Tutorial 4). Likely spin-off snack: NOIR levels of measurement (cairo-discrete-line already reaches for NOIR and has nowhere to point).

The course module page explicitly says: "A plan to make a 'data abstraction cheat sheet' - but I haven't yet." Decide: is the cheat sheet a section of this page, or the page's whole personality?

**SETTLED 2026-09-06 (Mike): the cheat sheet is the whole personality.** It became a *second, separate* page — `content/tutorials/data-abstraction-cheat-sheet/` (tutorial, weight 32) — derived from the long draft. The long draft at `content/tutorials/data-abstraction/` stays in place, untouched, so Mike can choose between them later. Either form (tutorial or snack) is acceptable for the cheat sheet; tutorial chosen for now. Motivation is *deliberately* not carried by the page: for class Mike leans on Munzner ch. 2 and the lecture, so the page has ~100 words of setup that defers to Munzner and nothing more.

## 2. Course fit (agent-filled)

Module 2 (Building Blocks), lecture 3-W first half. Module outcome #2: "have a vocabulary for describing data (data abstraction) to help us connect it to visual representations." Sits between critique (3-M) and encodings (4-M); the encodings page already leans on data types ("match your data type"), so this page is what makes that lean stand up.

## 3. Sources (agent-filled)

- Lecture 3-W-Abstraction.pptx, slides ~9–33 (data half).
- Munzner ch. 2 (Data Abstraction) — required reading; this page gives its main points.
- The Scribbr levels-of-measurement page (module page recommends it for NOIR, which Munzner skips).
- Existing neighbors: {{<link "/tutorials/encodings">}}, cairo-discrete-line (NOIR), future Too-Much-Stuff page (binning/conversions).

## 4. High-value material in the slides (agent-filled)

- Slide 13: the three set types (tables / fields / networks) **plus the terminology warning** that "field" means something else in databases/Tableau — very site-voice.
- Slides 16–17: sampling turns fields into tables.
- Slide 18: keys and values (domain and range).
- Slide 20: "rotate" time into space — compelling reframing.
- Slide 23: NOIR levels of measurement.
- Slide 26: "Having a 'middle' is useful" (diverging).
- Slides 27–28: special cases — time ("1D interval, but... cycles, periods"), geo-position; part/whole as a group property.
- Slides 29–33: conversions between types (discretization, binning, interpolation, "some useful conversions").
- Slide 71 (deck summary): "Attributes connect directly to designs" — candidate closing lesson.

## 5. What to cut / what must survive (MIKE)

Settled 2026-09-06, for the cheat-sheet page:

- **Cut the motivation.** The long draft's "Why Bother Describing Data Abstractly?" section is gone. Munzner ch. 2 and the lecture carry the argument for class; the page defers to her in three sentences.
- **Cut the data-type → encoding story.** See §7 — this is a stance, not just a trim.
- **Must survive:** the "field" terminology warning; keys/values with the cross-field alias table; NOIR with the numbers-lie-about-their-level point; rotation (John Snow); the conversions list. All present.

## 6. The stories (MIKE)

- (e.g., a favorite example dataset for the walkthrough? The lecture uses examples I can't fully recover from slides.)

## 7. Contested takes (MIKE)

Three, all now marked on the cheat-sheet page:

1. **NOIR's four levels vs. Munzner's three types.** Pre-existing supplement; she folds interval+ratio (footnote 3, citing Stevens 1946). Kept in an expand box, framed as an owned choice, justified by the interpolation/"connect the dots" argument that `cairo-discrete-line` needs.

2. **Categorical is a *subset* of nominal, defined by set size** (a nominal attribute whose possible values form a compact, finite, known set — "categorical implies set size; nominal doesn't"). Mike explains this in class and was unsure whether it's his invention. **Findings:** the *distinction* is real and widely implemented — the standard name for the underlying property is **cardinality**, and the split appears as R's `factor` vs. `character`, SQL's `ENUM` vs. `TEXT`, and feature engineering's separation of ordinary categoricals from high-cardinality/identifier columns. The **nesting is nonstandard**: most statistical writing uses "categorical" as a synonym for nominal or as the umbrella over nominal + ordinal. Munzner does the former — per the ch. 2 summary, nominal appears only as a margin synonym for categorical. So the concept is borrowed, the name is Mike's. Page states it that way, with the caveat in an expand box that mirrors the "field" warning. **Still unverified:** whether any published source defines categorical this narrowly on purpose.

3. **No data-type → encoding lookup.** Mike is actively trying to get away from "ratio data, so use a bar chart," because the choice usually needs *task*. Consequences for the page: the long draft's "Encodings that fit" column was **removed** from the NOIR table (replaced by an "Operations" column, which is the intrinsic property and the honest reason the levels matter); the closing section says type *constrains* the space of honest designs without picking one out of it, backed by Munzner 2.6 (type and semantics are crosscutting); and the forward link to `/tutorials/encodings` was **dropped entirely**. Rationale: class order puts data abstraction before encodings, and "how this connects to encodings" is its own separate piece, not this page's job.

## 8. Anything else (MIKE)

-
