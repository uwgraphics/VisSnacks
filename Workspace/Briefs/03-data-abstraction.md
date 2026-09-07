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
- **John Snow — cut from the cheat sheet 2026-09-06, but don't lose this.** Mike's correction: Snow's insight was to *ignore time*. The other cholera plots of the day were time vs. deaths; he did place vs. deaths. (My draft had described it as "indexes deaths by position rather than by patient," which misses the point.) Cut from the cheat sheet because the reader doesn't arrive knowing the example and it needs more setup than a cheat sheet can spend. This is really material for its own snack — the notes file already lists "John Snow / Rotations / Modern John Snow" in the 3-Abstractions**Unused** deck.

## 7. Contested takes (MIKE)

Three, all now marked on the cheat-sheet page:

1. **NOIR's four levels vs. Munzner's three types.** She folds interval+ratio (footnote 3, citing Stevens 1946). **Revised 2026-09-06:** the original expand box justified keeping four levels with the interpolation / "connect the dots" argument, and *that was wrong* — the boundary that argument needs is ordinal vs. interval, which Munzner's three types have too. Mike deleted the box; the justification is now a single bullet resting on the real distinction: a true zero is what licenses "twice as much," proportions, and a bar starting at zero, none of which are meaningful for °C. The `cairo-discrete-line` link moved to **Interpolation** under Conversions, where the ordinal/interval boundary is the right one.

2. **Categorical is a *subset* of nominal, defined by set size** (a nominal attribute whose possible values form a compact, finite, known set — "categorical implies set size; nominal doesn't"). Mike explains this in class and was unsure whether it's his invention. **Findings:** the *distinction* is real and widely implemented — the standard name for the underlying property is **cardinality**, and the split appears as R's `factor` vs. `character`, SQL's `ENUM` vs. `TEXT`, and feature engineering's separation of ordinary categoricals from high-cardinality/identifier columns. The **nesting is nonstandard**: most statistical writing uses "categorical" as a synonym for nominal or as the umbrella over nominal + ordinal. Munzner does the former — per the ch. 2 summary, nominal appears only as a margin synonym for categorical. So the concept is borrowed, the name is Mike's. Page states it that way, with the caveat in an expand box that mirrors the "field" warning. **Correction 2026-09-06 (Mike was right):** my first draft said "the usual term for the underlying property is cardinality." That's wrong — cardinality is just the *size* of a set, and a set can have enormous or infinite cardinality, so the word alone doesn't carry the meaning. The page now says the property is *small and finite* cardinality **plus** a closed set of possibilities. Also refined per Mike: the values need not be *known/listable* — the set of US counties counts — only **closed**, so a brand-new value is a surprise. **Still unverified:** whether any published source defines categorical this narrowly on purpose.

3. **No data-type → encoding lookup.** Mike is actively trying to get away from "ratio data, so use a bar chart," because the choice usually needs *task*. Consequences for the page: the long draft's "Encodings that fit" column was **removed** from the NOIR table (replaced by an "Operations" column, which is the intrinsic property and the honest reason the levels matter); the closing section says type *constrains* the space of honest designs without picking one out of it, backed by Munzner 2.6 (type and semantics are crosscutting); and the forward link to `/tutorials/encodings` was **dropped entirely**. Rationale: class order puts data abstraction before encodings, and "how this connects to encodings" is its own separate piece, not this page's job.

## 8. Anything else (MIKE)

-
