+++
title = "The Nested Model, Broadly Viewed"
date = 2026-10-24T12:43:59-05:00
draft = true
tags = ["evaluation", "nested-model"]
+++

Munzner's **nested model** splits visualization design into four levels, each with its own way of going wrong and its own kind of evidence that you got it right. It is one of the most important ideas in the field. But it isn't one paper: it's a paper, a book chapter, a follow-up paper, and (in my class) a version of my own that has drifted from all of them.

<!--more-->

[MIKE: note to the reader that we wrote this together.]

[MIKE: commentary on how core the idea is, and how profound/impactful it has been (on you, at least). Foreshadow "my version" at the end.]

## What is this?

The nested model has three "official" sources, all from Tamara Munzner and her collaborators:

+ Tamara Munzner. 2009. A Nested Model for Visualization Design and Validation. *IEEE Transactions on Visualization and Computer Graphics* 15, 6 (2009), 921–928. [(web)](http://www.cs.ubc.ca/labs/imager/tr/2009/NestedModel/) [(doi)](https://doi.org/10.1109/TVCG.2009.111)
+ Tamara Munzner. 2014. *Visualization Analysis and Design*, Chapter 4: "Analysis: Four Levels for Validation." CRC Press. (See {{<link "/resources/munzner">}}.)
+ Miriah Meyer, Michael Sedlmair, P. Samuel Quinan, and Tamara Munzner. 2015. The nested blocks and guidelines model. *Information Visualization* 14, 3 (2015), 234–249. [(doi)](https://doi.org/10.1177/1473871613510429)

The 2009 paper introduced the idea. The book chapter came later, explains it better, and uses the vocabulary of the rest of the book; it is the one to read. The 2015 paper (an earlier version appeared at a workshop in 2013) adds the idea of "blocks" and "guidelines," some of which the book picked up.

One thing to know going in: the model was built for evaluating visualization *research*. The original paper is addressed to people writing and reviewing visualization papers. That is still a useful perspective, but it isn't the only one, and the last part of this page is about using the model more broadly.

## The key idea

The model splits the design of a visualization into four levels. Each one takes the output of the level above as its input:

| Level | What gets decided | The threat (what goes wrong) |
| --- | --- | --- |
| **Domain situation** | who the users are, what they need to do, with what data | *Wrong problem:* you misunderstood their needs. |
| **Task and data abstraction** | the domain problem restated in generic terms (abstract tasks, data types) | *Wrong abstraction:* you're showing them the wrong thing. |
| **Visual encoding and interaction idiom** | how the abstract data is shown and manipulated | *Wrong idiom:* the way you show it doesn't work. |
| **Algorithm** | how the computer carries out the idiom | *Wrong algorithm:* your code is too slow. |

(The threat slogans are Munzner's, from the book.)

The levels are **nested**: a mistake at an outer level cascades to everything inside it. If you picked the wrong abstraction, a perfect encoding and a fast algorithm won't save you. Or, more bluntly: don't bother solving the wrong problem well.

The part of the model that makes it about *validation* is that each level has a different threat, so each level needs a different kind of evidence. A user study can't tell you whether your algorithm is fast enough; a timing benchmark can't tell you whether your encoding works. Munzner separates two kinds of validation:

+ **Immediate (upstream)** validation can happen at a level before anything inside it exists. You can interview users before you design anything. You can justify an encoding against perceptual principles before you build it.
+ **Downstream** validation requires the inner levels to be done first. You can't measure adoption of a tool nobody has built.

The catch is that most of the convincing evidence for the outer levels is downstream. To learn whether you understood the problem, you need a working system in the hands of real users, and by then a poor result might be the fault of any level inside. (A bad encoding can make a perfectly good abstraction look wrong.)

This figure is the summary of the whole idea (it is Figure 2 in the paper and Figure 4.5 in the book). Each box is a level. Inside each box, the validations above the inner box are immediate; the ones below it are downstream.

<style>
.nm-fig{font-size:0.95rem;line-height:1.35;max-width:40rem;margin:1rem 0;}
.nm-fig .nm-l{border:1px solid #888;border-radius:4px;padding:0.4rem 0.4rem 0.4rem 0.6rem;margin:0.3rem 0;}
.nm-fig .nm-l1{background:#fbe3d4;}
.nm-fig .nm-l2{background:#f6efc9;}
.nm-fig .nm-l3{background:#d6ecd9;}
.nm-fig .nm-l4{background:#e8dcef;}
.nm-fig .nm-impl{background:#eee;border:1px dashed #888;padding:0.3rem 0.5rem;margin:0.3rem 0;font-weight:bold;}
.nm-fig p{margin:0.15rem 0;color:#222;display:flex;gap:0.4em;}
.nm-fig .nm-k{font-weight:bold;flex:0 0 5.5em;}
@media (max-width:600px){.nm-fig{font-size:0.85rem;}.nm-fig .nm-l{padding:0.3rem 0.25rem 0.3rem 0.4rem;}.nm-fig .nm-k{flex-basis:4.6em;}}
.nm-fig .nm-note{font-style:italic;}
.nm-fig .nm-tag{font-size:0.8em;color:#555;}
</style>
<div class="nm-fig" role="figure" aria-label="The nested model: threats and validations at each of the four levels">
<div class="nm-l nm-l1">
<p><span class="nm-k">Threat</span><span>Wrong problem</span></p>
<p><span class="nm-k">Validate</span><span>Observe and interview target users <span class="nm-tag">(immediate)</span></span></p>
<div class="nm-l nm-l2">
<p><span class="nm-k">Threat</span><span>Wrong task/data abstraction</span></p>
<div class="nm-l nm-l3">
<p><span class="nm-k">Threat</span><span>Ineffective encoding/interaction idiom</span></p>
<p><span class="nm-k">Validate</span><span>Justify encoding/interaction design <span class="nm-tag">(immediate)</span></span></p>
<div class="nm-l nm-l4">
<p><span class="nm-k">Threat</span><span>Slow algorithm</span></p>
<p><span class="nm-k">Validate</span><span>Analyze computational complexity <span class="nm-tag">(immediate)</span></span></p>
<div class="nm-impl">Implement system</div>
<p><span class="nm-k">Validate</span><span>Measure system time/memory <span class="nm-tag">(downstream)</span></span></p>
</div>
<p><span class="nm-k">Validate</span><span>Qualitative/quantitative result image analysis <span class="nm-tag">(downstream)</span></span></p>
<p class="nm-note"><span class="nm-k"></span><span>Test on any users, informal usability study (not counted as validation)</span></p>
<p><span class="nm-k">Validate</span><span>Lab study, measure human time/errors for task <span class="nm-tag">(downstream)</span></span></p>
</div>
<p><span class="nm-k">Validate</span><span>Test on target users, collect anecdotal evidence of utility <span class="nm-tag">(downstream)</span></span></p>
<p><span class="nm-k">Validate</span><span>Field study, document human usage of deployed system <span class="nm-tag">(downstream)</span></span></p>
</div>
<p><span class="nm-k">Validate</span><span>Observe adoption rates <span class="nm-tag">(downstream)</span></span></p>
</div>
</div>

*Threats and validation at each of the four levels. Redrawn as text from Munzner, Visualization Analysis and Design, Figure 4.5 (originally Figure 2 of the 2009 paper); the "immediate/downstream" labels are added.*

Two things in the figure are easy to miss. First, the abstraction level has no immediate validation at all: the only way to know you abstracted correctly is to give the finished thing to real users doing their own work. Second, informal usability testing is in the figure but deliberately not called validation. Munzner (quoting Andrews) puts it there because you should do it *before* a real study, not instead of one.

The other big lesson is about **mismatches**: the evidence has to be at the level of the claim. If a paper claims a new encoding is better, timing the algorithm doesn't support that. If it claims to solve a real user's problem, a lab study where the experimenter chose the tasks doesn't support that either. No single project can validate everything at every level, so the point is to know which level you are claiming something about, and pick evidence that fits.

Finally, the levels are a way to *analyze* a design, not a required order for doing it. Real design goes back and forth between the levels.

## How the idea changed: paper, book, blocks

The paper and the chapter share the core: the four levels, the threats, immediate versus downstream, mismatches, and nearly the same worked examples. But the book makes some changes worth knowing about, especially if you read both.

**The vocabulary changed.** The paper's "domain problem characterization" became "domain situation"; "data/operation abstraction" became "task and data abstraction"; and "encoding/interaction technique" became "idiom." The abstraction level and the idiom level line up with the "what/why" and "how" questions the rest of the book is organized around.

**The book adds blocks.** A **block** is the outcome of design at one level. Some blocks are *identified* (you discover the situation and the tasks by studying the users) and some are *designed* (you choose the data abstraction, the idiom, and the algorithm). Treating the data abstraction as a choice, rather than something you are handed, is the most useful addition: transforming the data is part of the design.

**The book adds "angles of attack."** Problem-driven work starts at the top (a real user's problem) and works down. Technique-driven work starts at the idiom or algorithm level with a new idea. For the second kind, the advice is to state your assumptions about the level just above the one you are working on.

**The book drops some things.** The paper has a short list of recommendations for authors and venues, and an unusually candid section on its own limitations: the model "errs on the side of oversimplifying the situation," and its assumption that complex sensemaking can be broken into low-level pieces "is unlikely to be completely true." The book leaves these out. I think the caveat is worth keeping.

[TODO: Meyer et al. 2015, what the blocks-and-guidelines paper adds beyond what the book uses. Waiting on the AI summary of the paper; don't write this from memory.]

## Beyond research papers: my version

[MIKE: check this section's framing. It's drawn from what you said while we planned the page.]

I have my own version of the nested model. It didn't come from a single decision. It drifted, slowly, as I tried to adapt Munzner's "how to evaluate visualization research" into what I needed: a way to think about *designing* visualizations, and evaluating visualizations rather than research contributions. Along the way I ended up with several versions, and I conflate them, so they get remixed. This is my attempt to pin one down.

| Munzner | My version | What changes |
| --- | --- | --- |
| Domain situation | **Scenario** | broadened to the whole problem space, including the resources available |
| Task and data abstraction | **Abstraction** | the same idea |
| Encoding and interaction idiom | **Design** | the *key* choices |
| Algorithm | **Details** | everything else: specific design choices, and implementation |

**Scenario** is the concrete situation: who, why, what data, when, where, and how they expect to be helped. That is the {{<link "/papers/problem-space">}}. The scenario can also place constraints on every layer inside it. "It has to work in Excel" is part of the scenario, even though what it constrains is a detail.

**Design** and **Details** are where my version differs most from Munzner's. Her inner level is the algorithm, which matters if you are building systems, and often doesn't if you are making a chart. My inner level is everything below the key choices. The choice to use a color encoding is design; the choice of the specific colors is a detail. So are the titles, the labels, the annotations, and the code. Details is a much bigger level than Algorithm, and for most of the visualizations you will make, it is where a lot of the work (and a lot of the failures) happen.

The lines between my levels are fuzzy. So are Munzner's. Whether something is a key choice or a detail depends on the visualization: a color can be a detail in one design and the whole point of another. That doesn't make the model less useful. It is a lens for asking "what kind of decision is this, and what kind of evidence would tell me it's right?"

[OPTIONAL: One related distinction: how *big* a task is (its composition level) is a different question from how *generic* its description is (its abstraction). Only the second is the step from Scenario to Abstraction. See {{<link "/tutorials/task-abstraction">}}.]

**The recipe is not the model.** In {{<link "/tutorials/2-building-blocks">}} I give a four-step recipe: Task, Data, Design, Details. It came from the nested model, and it looks like the nested model, and I have been known to mix the two up. But they do different jobs. The recipe is the order you *work* in (with lots of going back). The model is the structure you *check* against: each level has its own threat and its own evidence. Data gets its own step in the recipe because gathering resources is a step. In the model, understanding the data is part of the scenario and the abstraction.

{{<expand "What I wrote in a 2018 paper">}}
The closest I came to writing my version down was in {{<link "/papers/comparison">}}. The paper's four considerations for comparison each fit a phase of design: identify the comparison's targets and actions (task), identify what makes it hard to scale (data abstraction), choose a strategy for handling the scale (design), and choose a visual design (details). A footnote says "My visualization class terms this Task, Data, Design, Details, but the names from Munzner's nested model also apply."

Looking at it now, that version puts the line between Design and Details higher than I would today: the design is the strategy (scan, subset, or summarize), and even the encodings are details. It is a snapshot of my thinking at the time, and arguably a misremembering of Munzner's model.
{{</expand>}}

## Using it

The most practical way to use the nested model is to turn the threats into questions. For any visualization (yours or someone else's), ask at each level: is this the right problem? Is the abstraction right? Do the key design choices work? Were the details done well? Then ask what evidence you have for each answer, and whether that evidence is at the right level. A careful critique at each level is a form of validation (see {{<link "/tutorials/4-critique">}}).

Two lessons carry over from the research setting. First, match your evidence to your claim: a chart where people can tell the colors apart has passed a test, but it says nothing about whether color was the right encoding in the first place. Second, you can validate a lot before you build anything. Most of the immediate validations (talking to the people with the problem, justifying your design choices against what we know about perception) cost far less than building a tool and testing it, and they catch the most expensive mistakes early.

{{<expand-boxed "Try it: 8 places">}}
Each of the four levels has an immediate validation and a downstream validation, so there are 8 places where something can go wrong, and 8 places where you can check. Pick a visualization project (your own is best). For each of the 8 places, name a specific threat you might encounter, and what you would do to check for it. For the downstream ones, you may have to imagine that you've already built the thing.

You will probably be asked to do this in class.
{{</expand-boxed>}}

## Do you still need to read the originals?

The book chapter: yes. It is the best explanation, and Figure 4.5 gets the key idea across. The examples at the end are worth skimming, if only for a taste of some historical visualization research.

The 2009 paper: if you plan to work in the field, you should see the original. For class, it is mostly redundant with the chapter, although its limitations section is worth a look.

The blocks paper: optional. [TODO: revisit after summarizing.]

{{<genai>}}
[MIKE: adjust.] Claude drafted this page from Mike's notes, course materials, and lecture slides, and from AI summaries of the Munzner paper and chapter, through a long conversation with Mike about what his version of the model actually is. Mike edited.
{{</genai>}}
