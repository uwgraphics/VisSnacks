+++
title = 'Data Abstraction: A Cheat Sheet'
date = 2026-09-06T11:00:00-05:00
draft = true
weight = 32
tags = ["data-abstraction", "building-blocks"]
+++

The vocabulary for describing data abstractly defined concisely. These are the terms that come up most often in describing data for visualization. 

<!--more-->

Munzner's chapter 2 makes the case for why you'd want to describe data abstractly. The short version is that the *kinds* of data are few and recurring, so what you learn about a kind carries to the next dataset that shares it. These are the terms I like to use - and some of the quirks in how I like to use them.

## Where the data lives: dataset types

*one sentence: where the data lives / where we measure*

- **Table** - a discrete set of items (rows), each with measured attributes (columns). Munzner counts **geometry** as a separate type, although it is a table where each item has a position.
- **Field** - measurements over a *continuous* domain: temperature at every point in a room, brightness at every position on the screen. You measure "everywhere," not at named objects. *pixels are wrong since they are the discrete sampling*
- **Network** (graph) - two kinds of object: items, and the *links* between them. Either can carry attributes. A **tree** is the acyclic special case.

*Note about tables: because it is discrete, it can always be unrolled into 1D. Sometimes there is structure to the discrete set (e.g., a grid). This is sometimes called a lattice.*

The **dimensionality** of a field is its *domain* - where you measure - not what you measure there. A field can be 1D (a signal over time), 2D (an image), or 3D (a volume); at each location you might record one number (**scalar**), a direction and magnitude (**vector**), or more (**tensor**).

{{<expand "Terminology warning: 'field' means two opposite things">}}
In databases and in Tableau, a **field** is a *column* - a synonym for attribute or variable. In the data-abstraction sense above, a field is the other end of the spectrum: a continuous domain you sample from. 
{{</expand>}}

### Keys and values

Some attributes *index* the data; others are *measured*.

| | Indexes the data | Measured at each index |
|---|---|---|
| Munzner | **key** | **value** |
| Statistics | independent variable | dependent variable |
| Math | domain | range |
| Tableau | dimension | measure |

- A **flat table** has at most one key. A **multidimensional table** needs several keys jointly.
- Not every column can be a key - it has to actually identify a row uniquely. (Munzner's Table 2.1 makes this point with two people named Amy.)
- In a field, **spatial position is the key**, and it's a quantitative one.
- **Time-varying** data has time as a *key*; if time is a *value*, it isn't.

**Rotation** - which attribute you treat as the key is a choice, not a property of the data. "For each day, what was the temperature" can become "for each temperature, which days." The non-standard rotation is sometimes the good one: John Snow's cholera map indexes deaths by *position* rather than by patient, and that reframing is the whole map.

*hard to mention snow's example since the reader doesn't know it - also, snow's insight was to ignore time (most plots were time vs. death, he did place vs. deaths) - unclear if we want the whole aside here* 

### Sampling

*the concept of sampling is important because it gets at domain - in either tables (reduce size) or fields (makes discrete). get rid of the clothes thing. and it's not a lot. in the opposite direction - usually we represent continuous fields as a sampled table*

*maybe use the pixel example from above: brightness can be measured anywhere, but we represent it as a sampled grid*

{{<expand "Sampling turns a field into a table">}}
You can't measure a continuous field everywhere, and often you couldn't observe every location anyway - you don't poll every voter or inspect every phone call. So you **sample**: measure at a finite set of locations, which turns the field into a table. Sampling is either inference (guess about the whole from a subset) or summary (throw information away on purpose). Worth remembering because a lot of "table" data is a sampled field wearing a table's clothes.
{{</expand>}}


## Describing Attributes

*describe attribute description as the set of possible values that an attribute might have. levels of measurement describe the types of set by the operations on them*

### Levels of measurement (NOIR)

What you measure has a **level of measurement**. The four classic levels go by the acronym **NOIR**.

| Level | What it is | Operations | Examples |
|---|---|---|---|
| **Nominal** | Names. No order. | `=`, `≠`, group | ZIP codes, student IDs, movie genres |
| **Ordinal** | Ordered, but no arithmetic. | `<`, `>`, rank, median | shirt sizes, Likert scales, letter grades |
| **Interval** | Differences are meaningful; zero is arbitrary. | `+`, `−`, mean | temperature in °C/°F, calendar dates |
| **Ratio** | True zero, so ratios are meaningful. | `×`, `÷` ("twice as much") | weight, distance, count, duration |

Some points:
- **The levels are a ladder.** Each rung supports every operation below it, plus one more.
- **Numbers lie about their level.** A student ID, a ZIP code, a jersey number, a department code - all stored as numbers, all nominal. "It's a number" is not "it's a ratio."
- **The level is a property of the data, not the column type.** It's what you know about the values, not how they're stored. *not sure what you mean by this*
- Interval and Ratio are sometimes grouped as **Quantitative**. Munzner Ch2 does this.

### Categorical: nominal with a small closed set

I use **categorical** more narrowly than most people do. For me it's a *subset* of nominal: a nominal attribute whose possible values form a **compact, finite, known set**.

- **Nominal** says only "these are names, with no order." Names can be anything - free text, IDs, values you haven't seen yet.
- **Categorical** adds that you can *enumerate* the possibilities. 

*i sometimes include cases where you don't know what they are, but you know the set is closed. the set of counties*

The distinction is worth a separate word because the small closed set is what makes a whole set of moves available. You can give every value its own hue or shape, build a legend that fits on the page, facet one panel per value, or put them all on an axis. None of that survives contact with a nominal attribute of ten thousand distinct values, even though the *level* is identical. **Categorical implies set size; nominal doesn't.**

{{<expand "Is this a real definition? Partly.">}}
The distinction is real and standard; my *name* for it isn't. The usual term for the underlying property is **cardinality** - the number of distinct values - and the split shows up implemented all over the place under other names: R's `factor` (a declared, finite set of levels) versus `character` (arbitrary strings); SQL's `ENUM` versus `TEXT`; the way feature engineering separates ordinary categorical features from "high-cardinality" or identifier-like columns.

*I think this is wrong - cardinality is the measure of the set size (AFAIK). A set can have large or infinite cardinality*

What's nonstandard is the nesting. Some statistical writing uses **categorical** as a synonym for nominal, or as the umbrella over nominal *and* ordinal - Munzner does the former, listing nominal as a margin synonym for categorical. So when you read "categorical" elsewhere, assume the broad meaning unless the author says otherwise, and don't expect anyone else to carry the set-size implication.
{{</expand>}}

### Other properties worth naming

Other properties of attributes (and the sets of values they may take).

*does cardinality come in here? the number of possible values/set size - we already mentioned in above*

- **Sequential vs. diverging.** A sequence runs one way (zero up to a max). Diverging data has a meaningful *middle* with distinct sides - elevation around sea level, profit around zero. The middle is a real property of the data.
- **Cyclic.** Hours, weekdays, months, compass bearings. The end connects back to the start.
- **Cardinality and set size.** How many distinct values, and is the set finite or open-ended.
- **Continuous vs. discrete.** Separate from the level of measurement, and from whether the *domain* is continuous.
- **Part/whole.** Sometimes the meaningful quantity belongs to a *group* - market share only means something against a total.
- **Hierarchical structure.** Some attributes aggregate: days into weeks into years, cities into states.

Two cases carry enough extra baggage to be worth flagging:

- **Time** is nominally a 1D interval quantity, but it has cycles at several scales, irregular units, and a strong left-to-right convention. Rarely "just a number."
- **Geographic position** is nominally 2D interval, but drags in projections, conventions, and every reader's prior expectations about maps.

## Conversions

Moving data between types is often the right design move, not a compromise.

- **Down-conversions are easy.** Discard the ordering (ordinal → nominal), or collapse a large set into a small one.
- **Up-conversions are hard**, because they mean *imposing* structure that wasn't in the data - inventing an order for categories.

| Conversion | What it does | The catch |
|---|---|---|
| **Discretization** | Continuous → discrete, by thresholding or rounding | Where you cut is a decision |
| **Binning** + **aggregation** | Group like values into buckets, then summarize each | Bin choice can quietly change the story |
| **Interpolation** | Invent values between measurements | Only if an in-between value is real |
| **Rank transformation** | Keep the order, discard the intervals | Ratio/interval → ordinal is lossy |

## What this buys you, and what it doesn't

The levels tell you which **operations are meaningful** on the values - which is what tells you whether a display's claim is honest.

They do not give you a lookup from data type to chart. Type *constrains* the space of honest designs without picking one out of it; what the viewer is trying to **do** usually does more of that work. (Munzner's 2.6 makes a version of this point: type and semantics are crosscutting, and neither dictates the other.) Task abstraction is the other half of this vocabulary, and gets its own page.

## Want more?

- Munzner, *Visualization Analysis and Design*, chapter 2 ("What: Data Abstraction") - the required reading, and where the motivation this page skips lives. Read 2.1-2.5 carefully; 2.5, on attribute types, is the most important handful of pages in the book for this material. Interval and ratio come back merged. I describe the book at {{<link "/resources/munzner">}}.

{{<genai>}}
Condensed by Claude into cheat-sheet form from the longer data-abstraction draft, which came from Mike's CS765 abstraction lecture and Munzner ch. 2; the categorical/nominal distinction and the anti-lookup-table framing are Mike's. Edited by Mike.
{{</genai>}}
