+++
title = 'Data Abstraction: Describing Data So You Can Use It'
date = 2026-07-17T18:00:00-05:00
draft = true
tags = ["data-abstraction", "building-blocks"]
+++

Before you can pick a visualization, you have to say what your data *is* - not "sales figures for the Milwaukee store," but the abstract version: a table of items with a few attributes, one of them a quantity. That abstract description is what connects to design choices, and it's the same handful of patterns over and over.

<!--more-->

## Why Bother Describing Data Abstractly?

The goal is **learn once, apply often**. Every dataset is different in its details, but the *kinds* of data - and the properties that matter for visualization - are few and recurring. If you learn to see past the domain specifics ("median household income by county") to the abstract form ("a table, with a categorical key and a ratio value"), then everything you know about that form carries over to the next dataset that shares it.

And the payoff is direct: **attributes connect directly to designs**. Whether a channel like position or color is a good fit depends on what the data can support, and that's a property of the data's abstract type, not its subject matter. This is the piece that makes the {{<link "/modules/encodings">}} page's advice - "match your channel to your data type" - actually stand up. You can't match to a data type until you can name the data type.

(There's an older reason too: the classic "chart type X for data type Y" rules. I'm wary of chart-type rules - they prevent the worst mistakes but don't help you think - but they, and modern automatic chart recommenders, both run on data abstraction under the hood.)

## Where Do You Measure? Three Kinds of Data Sets

Munzner starts with *organization*: where the data lives. Three forms cover most of it.

- **Tables** - a discrete set of objects (rows), each with measurements (attributes). The spreadsheet everyone pictures.
- **Fields** - measurements over a *continuous* domain: temperature at every point in a room, brightness at every pixel. You measure "everywhere" rather than at named objects.
- **Networks** (graphs) - two kinds of objects: items and the *links* between them, with measurements possible on both. (Trees are the special case with no cycles.)

{{<expand "A terminology warning worth pinning up">}}
The word **field** is a trap. In databases and in Tableau, a "field" means a *column* - a synonym for attribute (also called variable). In the data-abstraction sense here, a "field" is the opposite end of the spectrum: a continuous domain you sample from. Same word, nearly opposite meanings. When someone says "field," figure out which world they're in before you nod along.
{{</expand>}}

One more distinction: multidimensional here refers to the *domain* - where you measure - not what you measure there. A field can be 1D (a signal over time), 2D (an image), or 3D (a volume). At each location you might record a single number (a scalar) or something richer (a vector).

## Keys and Values

In a table, some attributes *index* the data and others are *measured*. The index attributes are **keys** (the domain); the measured ones are **values** (the range). Statisticians call these independent and dependent variables; Tableau calls them dimensions and measures. Every day I check the temperature: the day is the key, the temperature is the value.

Which attribute is the key isn't always fixed. You can **rotate** the organization: instead of "for each day, what was the temperature," ask "for each temperature, which days had it." Sometimes the non-standard rotation is the good one - John Snow's cholera map organized deaths by *position* rather than by patient, and that reframing is the whole point of the map.

{{<expand "Sampling turns fields into tables">}}
You can't measure or draw a continuous field *everywhere* - there are infinitely many positions, and often you can't observe them all anyway (you don't poll every voter, count every plankton, or inspect every phone call). So you **sample**: measure at a finite set of locations. That turns a field into a table. Sampling is either inference ("guess about the whole from a subset") or summary ("throw information away on purpose") - which is where statistics and signal processing come in. This is worth remembering because a lot of "table" data is really a sampled field wearing a table's clothes.
{{</expand>}}

## The Cheat Sheet: Attribute Types (NOIR)

What you measure - the *values* - has a type, and the type is the single most load-bearing distinction in this whole topic. The classic four levels go by the acronym **NOIR**: **Nominal**, **Ordinal**, **Interval**, **Ratio**.

| Level | What it is | Examples | What you can do | Encodings that fit |
|---|---|---|---|---|
| **Nominal** (categorical) | Names, no order | fruit, ZIP codes, student IDs | `=`, `≠`, group | hue, shape, spatial region |
| **Ordinal** | Ordered, but no arithmetic | shirt sizes, rankings, Likert, grades | `<`, `>` | ordered position, size, luminance |
| **Interval** | Numbers with meaningful differences, arbitrary zero | temperature (°C/°F), calendar dates | `+`, `−` | position, length |
| **Ratio** | Numbers with a true zero; ratios make sense | weight, distance, count, duration | `×`, `÷` ("twice as much") | length, area, position |

A few things this table is trying to teach at a glance. The levels are a ladder: each rung supports everything below it plus one more operation. **Numbers lie about their level** - a student ID is nominal, a department code is categorical, a jersey number tells you nothing you can add. So don't read "it's a number" as "it's a ratio." And a "middle" is a real property: ratio data supports division and the idea of *diverging* around a meaningful center (more on that below).

{{<expand "Why we teach NOIR when Munzner doesn't">}}
Munzner deliberately collapses this to three types - categorical, ordinal, and quantitative - folding interval and ratio together. Her footnote is explicit that the interval/ratio distinction "is typically not useful when designing a visual encoding." That's a defensible call, and if you only ever read her, you'll do fine.

I keep NOIR anyway, for two reasons. It's the vocabulary the rest of the world (and the lecture) uses, so you'll meet it constantly. And the extra rung earns its keep: the interval/ratio and ordinal distinctions are exactly what drive the "when is a line chart OK" guidance. Connecting the dots implies you can interpolate *between* the points - fine for interval/ratio, iffy for ordinal, wrong for nominal. That's the argument worked out in the {{<link "/snacks/cairo-discrete-line">}} snack, which reaches for NOIR and, until now, had nowhere to point.
{{</expand>}}

## Other Properties That Matter

The level of measurement isn't the only thing worth naming. A handful of other properties change design choices:

- **Sequential vs. diverging.** A sequence runs one way (0 up to a max); diverging data has a meaningful *middle* with distinct above and below (elevation around sea level, profit around zero). Diverging data wants a diverging encoding - this matters a lot for color, later.
- **Cyclic.** Hours, weekdays, months wrap around. The end connects back to the start.
- **Set size**, and whether values are **continuous or discrete**, **finite or infinite**.
- **Part/whole.** Sometimes the interesting property belongs to a *group* of items - market share only means something relative to the total.

Two special cases show up so often they're worth flagging:

- **Time** is nominally a 1D interval quantity, but it has cycles (daily, weekly, seasonal), periods, multiple scales, and a strong left-to-right convention. It's rarely "just a number."
- **Geographic position** is nominally 2D interval, but it drags in projections, conventions, and everyone's prior expectations about maps.

## Converting Between Types

You can move data between types, and it's often the right design move. **Down-conversions are easy** - ignore the ordering (ordinal becomes nominal), or group a big set into a small one. **Up-conversions are harder** and usually mean *imposing* structure that wasn't there (inventing an order for categories).

The most common conversions worth knowing:

- **Discretization** - turn continuous into discrete by thresholding or rounding.
- **Binning** - put like things into buckets, then decide how to **aggregate** what lands in each. The choice of bins can quietly change the whole story a chart tells, which is enough of a topic that it deserves its own discussion later on - I'll write that one up separately.
- **Interpolation** - the "connect the dots" question. Does a straight line between two measurements represent a real in-between value, or just a guess? (See the line-chart snack above - this is the same question from the other direction.)
- **Rank transformation** - throw away the intervals, keep only the order.

## And Then There's Task

Data abstraction is only half the vocabulary. The other half is **task abstraction** - describing what the viewer is trying to *do* - which shares this lecture but gets its own page. The short version: design should serve the task, and data type alone never settles a design question.

## Want More?

- Munzner's *Visualization Analysis and Design*, Chapter 2 ("What: Data Abstraction") is the required reading and covers all of this carefully - dataset types, attribute types, and the key/value semantics. One heads-up: she uses three attribute types where we use NOIR's four, so don't be thrown when interval and ratio come back merged. I describe the book at {{<link "/resources/munzner">}}.

{{<genai>}}
Drafted by Claude from Mike's CS765 lecture materials (Lecture 3-W, Fall 2025) and Munzner ch. 2; edited by Mike.
{{</genai>}}
