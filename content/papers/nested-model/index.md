+++
title = "The Nested Model(s): A Reader's Guide"
date = 2026-10-24T12:43:59-05:00
draft = false
tags = ["evaluation", "nested-model"]
+++

Munzner's **nested model** is a way of thinking about visualization validation that leads to processes for design and evaluation. It divides visualization design into four levels, each affecting the ones below (or inside) it (hence "nested"). While it was originally framed as a way to validate visualization research, it generalizes to practical visualization design and beyond.

<!--more-->

Munzner's nested model is one of the most important concepts in visualization. I view it as one of the most insightful and elegant ideas in the field. However, it can be a little tricky to learn about because it has multiple sources, and its origins belie its general utility. 

I wanted to write a tutorial summarizing the idea - but it isn't a paper summary, because there isn't a single paper to summarize. Instead, I worked with Claude to write this summary that tries to explain the various versions. In particular, to show how the original concepts focused on visualization research can be generalized to apply to visualization design in general.  I hope this summary not only conveys the basic ideas, but gives you a sense of the versions, and inspires you to read the original sources.

This document also describes the version I try to teach in class that I haven't tried to pin down in writing before.

## What is this?

The nested model has three "official" sources, all from Tamara Munzner and her collaborators:

+ Tamara Munzner. 2009. A Nested Model for Visualization Design and Validation. *IEEE Transactions on Visualization and Computer Graphics* 15, 6 (2009), 921–928. [(web)](http://www.cs.ubc.ca/labs/imager/tr/2009/NestedModel/) [(doi)](https://doi.org/10.1109/TVCG.2009.111)
+ Tamara Munzner. 2014. *Visualization Analysis and Design*, Chapter 4: "Analysis: Four Levels for Validation." CRC Press. (See {{<link "/resources/munzner">}}.)
+ Miriah Meyer, Michael Sedlmair, P. Samuel Quinan, and Tamara Munzner. 2015. The nested blocks and guidelines model. *Information Visualization* 14, 3 (2015), 234–249. [(doi)](https://doi.org/10.1177/1473871613510429)

The 2009 paper introduced the idea. The book chapter came later, explains it better, and uses the vocabulary of the rest of the book; it is the version I recommend. The 2015 paper (an earlier version appeared at a workshop in 2013) adds the idea of "blocks" and "guidelines," some of which the book picked up.

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

Importantly: validation of an inner layer says nothing about an outer layer. A great encoding design or algorithm won't help the user if you're solving the wrong problem.

This figure is the summary of the whole idea (it is Figure 2 in the paper and Figure 4.5 in the book). Each box is a level. Inside each box, the validations above the inner box are immediate; the ones below it are downstream. That's the point of drawing them as nested boxes: each level wraps around everything inside it, so it can be checked both before (immediate, upstream) and after (downstream) the work inside it is done.

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
.nm-fig.nm-wide .nm-k{flex-basis:7em;}
@media (max-width:600px){.nm-fig.nm-wide .nm-k{flex-basis:6.3em;}.nm-fig{font-size:0.85rem;}.nm-fig .nm-l{padding:0.3rem 0.25rem 0.3rem 0.4rem;}.nm-fig .nm-k{flex-basis:4.6em;}}
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

A key lesson is the importance of *matching validation*: the evidence has to be at the level of the claim. If a paper claims a new encoding is better, timing the algorithm doesn't support that. If it claims to solve a real user's problem, a lab study where the experimenter chose the tasks doesn't support that either. No single project can validate everything at every level, so the point is to know which level you are claiming something about, and pick evidence that fits.

Finally, the levels are a way to *analyze* a design, not a required order for doing it. Real design goes back and forth between the levels. However, starting from the outside in is the "standard" process.

## How the idea changed: paper, book, and beyond

The paper and the chapter share the core: the four levels, the threats, immediate versus downstream, matching validation method to level, and nearly the same worked examples. But the book makes some changes worth knowing about, especially if you read both.

**The vocabulary changed.** The paper's "domain problem characterization" became "domain situation"; "data/operation abstraction" became "task and data abstraction"; and "encoding/interaction technique" became "idiom." The abstraction level and the idiom level line up with the "what/why" and "how" questions the rest of the book is organized around.

**The book adds blocks.** A **block** is the outcome of design at one level. Some blocks are *identified* (e.g., you discover the situation and the tasks by studying the users) and some are *designed* (e.g., you choose the data abstraction, the idiom, and the algorithm). Treating the data abstraction as a choice, rather than something you are handed, is the most useful addition: transforming the data is part of the design.

**The book adds "angles of attack."** Problem-driven work starts at the top (a real user's problem) and works down. Technique-driven work starts at the idiom or algorithm level with a new idea. For the second kind, the advice is to state your assumptions about the level just above the one you are working on.

**The book drops some things.** The paper has a short list of recommendations for *visualization research* (authors and venues), and an unusually candid section on its own limitations: the model "errs on the side of oversimplifying the situation," and its assumption that complex sensemaking can be broken into low-level pieces "is unlikely to be completely true." The book leaves these out. I think the caveat is worth keeping.

## Beyond research papers: my version

As much as I value and am inspired by Munzner's nested model, its emphasis on validating visualization research has always felt a little off, especially as I've tried to teach people to evaluate visualizations. Therefore, I have come up with my own. You may have seen it in {{<link "/tutorials/2-building-blocks">}}. My nested model has evolved over the years, and here I try to pin it down.

<div class="nm-fig nm-wide" role="figure" aria-label="My version of the nested model: Scenario, Abstraction, Design, Details, with the threat at each level">
<div class="nm-l nm-l1">
<p><span class="nm-k">Scenario</span><span>What is the problem? Who, why (the task), what (resources, such as data), when, and where. <span class="nm-tag">(Munzner: domain situation)</span></span></p>
<p><span class="nm-k">Threat</span><span>You're solving the wrong problem.</span></p>
<div class="nm-l nm-l2">
<p><span class="nm-k">Abstraction</span><span>What is the generalized form? <span class="nm-tag">(Munzner: task and data abstraction)</span></span></p>
<p><span class="nm-k">Threat</span><span>Your abstractions are excessive, insufficient, or incorrect.</span></p>
<div class="nm-l nm-l3">
<p><span class="nm-k">Design</span><span>What is the strategy for solving it? What are the key high-level choices? <span class="nm-tag">(Munzner: encoding/interaction idiom)</span></span></p>
<p><span class="nm-k">Threat</span><span>Your key choices don't work for the scenario.</span></p>
<div class="nm-l nm-l4">
<p><span class="nm-k">Details</span><span>How do we make the design real? Implementation and smaller choices. <span class="nm-tag">(Munzner: algorithm)</span></span></p>
<p><span class="nm-k">Threat</span><span>You executed it poorly, or missed chances to get the details right.</span></p>
</div>
</div>
</div>
</div>
</div>

*My version of the nested model, with the threat at each level. The Munzner level each one replaces is in parentheses.*

**Scenario** is the problem itself. The task is the key part, but who it is for, what resources they have (data, most of all), and when and where they will use it all matter as well. These are the axes of the {{<link "/papers/problem-space">}}, which also has a sixth, "how (does the audience expect to be helped)," that I leave out here because it confuses things. The scenario can place constraints on every level inside it. The threat is the same as Munzner's: you can do everything else well and still be solving the wrong problem.

**Abstraction** restates the problem in a generalized form. That is what lets us apply design principles: the principles are written for abstract tasks and data types, not for your particular situation. There are three main ways to get it wrong. The abstraction can be *excessive*, simplifying away something that matters. It can be *insufficient*, staying so specific that the problem seems unique and no principle applies. Or it can be *incorrect*, generalizing to the wrong thing, like Munzner's example of the "family tree" that is really a more general graph.

In {{<link "/tutorials/task-abstraction">}}, we distinguish *composition* (how big a task is) from *abstraction* (how generic it is). Both apply in this step: abstracting well means correctly breaking the problem into pieces and finding generic ways to describe and think about it.

**Design** and **Details** are where my version differs most from Munzner's. Design is the strategy: the key, high-level choices about how to solve the abstract problem. The choice to use a color encoding is a design choice, the specific colors are a detail. The threat is that those key choices don't work for the scenario (especially task and data).

**Details** is everything it takes to make the design real: the smaller choices and the implementation. Implementation is a detail: the user won't appreciate your nice implementation if you've implemented the wrong thing. Small choices like specific colors, the visual style, or the wording of labels are similar. Poor details can sink things downstream: a poor implementation or color choices may mean that the abstractions don't help or the system doesn't satisfy the users. But details only matter if the outer layers are right. The threat has two parts: you can execute poorly, but you can also miss chances. Details are a place to fail, and also a place to excel.

Each level has to serve every level outside it, not just the one directly above. A design can be a fine solution to the abstract problem and still fail the scenario; a single detail can break the whole thing.

The lines between my levels are fuzzy. Whether something is a key choice or a detail depends on the visualization: a color can be a detail in one design and the whole point of another. That doesn't make the model less useful. It is a lens for asking "what kind of decision is this, and what kind of evidence would tell me it's right?"

**The recipe is not the model.** In {{<link "/tutorials/2-building-blocks">}} I give a four-step recipe: Task, Data, Design, Details. It came from the nested model, and it looks like the nested model, and I have been known to mix the two up. But they do different jobs. The recipe is the order you *work* in (with lots of going back). The model is the structure you *check* against: each level has its own threat and its own evidence. Data gets its own step in the recipe because gathering resources is a step. In the model, understanding the data is part of the scenario and the abstraction.

{{<expand "What I wrote in a 2018 paper">}}
The closest I came to writing my version down was in {{<link "/papers/comparison">}}. The paper's four considerations for comparison each fit a phase of design: identify the comparison's targets and actions (task), identify what makes it hard to scale (data abstraction), choose a strategy for handling the scale (design), and choose a visual design (details). A footnote says "My visualization class terms this Task, Data, Design, Details, but the names from Munzner's nested model also apply."

Looking at it now, that version puts the line between Design and Details higher than I would today: the design is the strategy (scan, subset, or summarize), and even the encodings are details. It is a snapshot of my thinking at the time, and focused on comparison.
{{</expand>}}

## Using it

The most practical way to use the nested model is to turn the threats into questions. For any visualization (yours or someone else's), ask at each level: is this the right problem? Is the abstraction right? Do the key design choices work? Were the details done well? Then ask what evidence you have for each answer, and whether that evidence is at the right level. A careful critique at each level is a form of validation (see {{<link "/tutorials/4-critique">}}).

Two lessons carry over from the research setting. First, match your evidence to your claim: a chart where people can tell the colors apart has passed a test, but it says nothing about whether color was the right encoding in the first place. Second, you can validate a lot before you build anything. Most of the immediate validations (talking to the people with the problem, justifying your design choices against what we know about perception) cost far less than building a tool and testing it, and they catch the most expensive mistakes early.

{{<expand-boxed "Try it: 8 places">}}
Each of the four levels has an immediate validation and a downstream validation, so there are 8 places where something can go wrong, and 8 places where you can check. (Munzner's diagram is missing one.) Pick a visualization project (your own is best). For each of the 8 places, name a specific threat you might encounter, and what you would do to check for it. For the downstream ones, you may have to imagine that you've already built the thing.

You will probably be asked to do this in class.
{{</expand-boxed>}}

## Do you still need to read the originals?

I recommend reading the book chapter as they get the ideas across more completely. The examples at the end are worth skimming, if only for a taste of some historical visualization research.

The 2009 paper: if you plan to work in the field, you should see the original since it is seminal. For class, it is mostly redundant with the chapter, although its limitations section is worth a look.

{{<genai>}}
Claude drafted this page from Mike's notes, course materials, and lecture slides, and from AI summaries of the Munzner paper and chapter, through a long conversation with Mike about what his version of the model actually is. Mike revised, substantially.
{{</genai>}}
