+++
title = 'Task Abstraction: A Cheat Sheet'
date = 2026-09-07T07:40:41-05:00
draft = false
weight = 33
tags = ["task-abstraction", "building-blocks"]
+++

Task abstraction is how we discuss what the visualization is trying to help the viewer do. Typically, this is done by trying to organize the range of tasks into categories or a taxonomy.  

<!--more-->

Task is central to visualization: it's the thing that we are trying to help the viewer do. I (and others) define visualization as having a task (see {{<link "/tutorials/1-what-is-vis">}}), and define good visualizations as being effective at those tasks. Having good ways to discuss task is important.

Even the term "task" itself is problematic. It is hard to pin down precisely. Different papers mean different things by the term "task".

The goal of task abstraction is to have a way to describe what the visualization is trying to do (or to help the viewer do) in a manner that is specific enough to be meaningful, but broad and general enough that is allows for generalized thinking and for seeing similarities in problems and solutions.

My goal is to have ways for discussing the "problems" that visualizations are trying to address so that we can choose solutions that solve them. I am much less concerned about trying to put tasks into neat little boxes.

**One objection to get out of the way up front:** *"I don't have a task - I just want to look at my data."* That is still a task. Usually it means you haven't articulated a better description yet, and sometimes the honest description is "my task is to figure out what the right task is." Either way, you are better off saying so than deciding task doesn't apply to you. I make this point in {{<link "/tutorials/2-building-blocks">}} as well - it's worth repeating.

I call it a "cheat sheet" because it's designed to be a quick summary of some of the main things you would get from reading a whole list of papers and fusing the ideas together. It's not trying to cover everything - it's just a slice across the landscape. It's the basics I think you need, and it might inspire you to read the original sources.

 In class, I try to connect these with examples from my own work.

## The Cheat Code: Flexible Tools not Rigid Rules

Don't worry about pinning down the terms precisely, or having formal structures to organize and group different tasks. View task abstraction as a toolbox - many different ways to describe and analyze what the viewer might want to do (or what we, as visualization designers, want to make a visualization to help the viewer do).

View all of the previous task organization schemes as providing *vocabulary* for discussing what we are trying to do with a visualization, or what the visualization is meant to do. Each provides some tools that we can use in describing and analyzing "tasks". The better our toolbox, the better able we can be at describing and understanding the different scenarios that we want visualizations for, designing visualizations that fit them, and assessing whether or not our solutions work.

- It is important to be able to talk about task.
- It may or may not be important to have formalism for talking about tasks.
- Use formalisms when they are useful. Don’t get stuck on their details.


## Why is this hard? The Dimensions of Task Abstraction

The challenge of task is that there are many different things it can mean, and many different levels to look at it. The TaskCube paper by Rind et. al articulated this well. Understanding the different ways we might view tasks provides an interesting set of perspectives we can apply.

They make a series of distinctions:

- Level of Abstraction: **Abstract** vs. **Concrete** - How generic is the description? Is it specific, or could it apply to many things.
- Level of composition: **High-Level** vs. **Low-Level** - How "big" is the task? Is it some long-scale, multi-step process, or is it a small quick thing that is likely to be a step in a longer process.
- Perspective: **Why (Objectives)** vs. **How (Actions)** - objectives are questions on data (desired results), actions are steps towards objectives

This is a 3 dimensional grid (hence, task cube). Here are examples of all of the combinations:

|  |  | Low-level | High-level |
|---|---|---|---|
| **Objectives** *(why)* | Concrete | Which quarter had Google's largest revenue? | Find a vaccine for HIV |
|  | Abstract | Find the maximum | Make an informed decision |
| **Actions** *(how)* | Concrete | Drag the date slider to 2014 | Search a term, narrow by date, read the word cloud |
|  | Abstract | Filter | Overview first, zoom and filter, then details-on-demand |


## Levels of Abstraction and Composition

Abstraction and composition are *scales* - you can slide a description along either one.

For example:
- Take an abstract task and give a more concrete example
- Take a composed task and break it into smaller steps
- Take a concrete task and find a general (abstract) problem it is an instance of
- Group a set of small tasks into a single operation

Different levels of abstraction. Note how with each, things become less abstract and lower level:
- Make an informed decision 
- Select between options with different tradeoffs
- Choose a transport option 
- Select a train ticket between Frankfurt and Stuttgart on Aug 15
- Compare the prices between two tickets

Example: "Make an informed decision" is an abstract, compound task. I can decompose it into steps: identify choices, get data about choices, make comparisons, ... I can pick a concrete example, e.g., decide how to get between two cities. 

We often try to describe tasks at a level of abstraction and composition that makes the task match common patterns for which we have some design experience. If the task is too specific, it might seem unique and without precedent to inform our design. However, if we abstract incorrectly, we might throw away important features of the problem.

## Actions and Targets

I often find it useful to think of tasks in terms of a pairing of an action (a verb) and a target (a noun, the object of the verb). Many task descriptions naturally have this form - e.g., "identify an outlier" or "choose a transport option". Munzner's chapter (below) emphasized thinking about these two pieces independently, and this strongly influenced my work (see {{<link "/papers/comparison">}}).

One piece of advice: try to understand both action and target. Either one can be made more or less abstract. 

### What do you want to do with the target?

The task lists from papers (below) often have lists of actions. Here is one that I made up that I phrase as "what to do with targets". It differs from the lists below (especially the Amar 2005 list) in that its centers on what the viewer does (or can do perceptually), rather than the result that they want. 

- **Absolute judgment** - read a value off the display
- **Relative judgment** - compare two things to each other
- **Identify / find / match against a key** - pick out a specific thing
- **Form groups / regions** - see what belongs with what
- **Count / quantify** - how many are there
- **Average / estimate statistics** - get a sense of a summary value

## The Problem Space: Beyond Tasks

Task is only part of the description of "the problem" that a visualization might be addressing. We (some colleagues and I) suggested the idea of a *Problem Space* for visualization that considers different dimensions of scenarios that can (or should) influence visualization design. The paper is summarized at {{<link "/papers/problem-space">}} (the summary is probably sufficient).

The problem space is defined using the 5Ws and an H from journalism (that actually dates back even farther):
- **Who** has the problem / will be the viewer
- **Why** are they using the visualization (this is the objective or task)
- **What** are they looking at (the data)
- **When** in the analysis process (what phase)
- **Where** the context
- **How** do they *expect* to be helped (not the actual solution)

Takeaway: task is only one aspect of what we need to consider in designing visualizations. It's an important one, but it is one of many.

## Example Task Organizing Schemes

I provide some examples (drawn from the readings listed at the end of this page) that give examples of task description concepts. While it is organized by the source, you can mix and match the different pieces.

### Organization Schemes: Taxonomies vs. Typologies vs. Categorizations

Historically, researchers used the term taxonomy to describe schemes for organizing tasks. Technically, taxonomy is a very specific type of organizing structure - that few task taxonomies actually follow. For completeness, here are the differences - but I won't blame you if you just call everything a taxonomy. 

- **Categorization** - The broad, general term; often used to imply an informal grouping.
- **Classification** - Groups things into categories where the categories are mutually exclusive and jointly exhaustive (every item has exactly one home). Usually has strictly defined rules for each category.
- **Taxonomy** - A hierarchical classification where items are grouped based on observable characteristics into groupings with strict boundaries.
- **Typology** - A grouping based on "ideal types" or characterizations. The boundaries between the categories may not be well defined.
- **Spectrum** - A (conceptually) continuous dimension that something can be placed on.
- **Space** - for example, a "Design Space" or a "Problem Space". This refers to a set of separate dimensions, each might be a spectrum or some categorization.
- **Clustering** - a type of categorization where things are grouped by similarity.


### Shneiderman 1996: Task by Data Type Taxonomy

+ {{<reading eyeshaveit>}}

By 1996, Ben Shneiderman was already famous. This paper was an invited survey where he tried to organize a zoo of different experimental designs into a framework. 

Notably, this paper tried to separate **data abstraction** from **task abstraction**. Neither list was very rigorous, but it was an important starting point for others. 

His list of tasks:
- Overview
- Zoom
- Filter
- Details-on-demand
- Relate
- History
- Extract

This paper is mainly famous for his *information seeking mantra*: **"Overview first, zoom and filter, then details-on-demand"**, which isn't strictly part of either taxonomy. However, the mantra teaches us a lesson: it isn't a universal law, it's a common pattern that he recommends considering.

### Amar, Eagan and Stasko: Low-Level Components of Analytic Activity

+ {{<reading lowleveltasks>}}

This paper was one of the first *rigorous* task categorizations. They explicitly focused on the "low level" of tasks, creating a set of primitives that could be built into more complex operations. This list stands up well over time. It gets referred to a lot, and is often used as an organization scheme (for example, the paper [A Survey of Perception-Based Visualization Studies by Task](https://doi.org/10.1109/TVCG.2021.3098240) uses it to organize their survey).

- Retrieve Value
- Filter
- Compute Derived Value
- Find Extremum
- Sort
- Determine Range
- Characterize Distribution
- Find Anomalies
- Cluster
- Correlate

Real questions often require *composing* primitives. Their own example: "Who starred in the most films in 1978?" decomposes into *Retrieve Value* (which films are from 1978), *Compute Derived Value* (count the films per actor), and *Find Extremum* (whose count is largest). 

### Munzner 2014 (Book), Brehmer&Munzner 2013 (Multi-Level Typology)

+ {{<reading multi-level-tasks>}}
+ Tamara Munzner, *Visualization Analysis and Design*, Ch 3 "Task Abstraction" ({{<link "/resources/munzner">}})

The paper was one of the first task categorizations that acknowledged the multi-level nature of task, and tried to do things at multiple levels. It was also the first to be precise about terminology (it is a typology, not a taxonomy).

The idea of levels was made much clearer in the Task Cube paper.

One thing I like about their approach is describing tasks in terms of actions and targets (or verbs and nouns). Splitting the description of the task this way can simplify it.

#### Actions: the "why" verbs

The main part of actions are the "why" verbs, which they organize hierarchically. The three groups are three *independent* levels, not steps in a sequence: you can say something at all three at once.

- **Analyze** - the highest level: what are you doing with the visualization at all?
  - **Consume** - using information that is already there
    - **Discover** - find something you didn't know (either to generate a hypothesis or to verify one)
    - **Present** - communicate something you already understand to someone else
    - **Enjoy** - a casual encounter, with no external goal
  - **Produce** - the output of the work is something new, not just understanding in the viewer's head
    - **Annotate** - the goal is to end up with commentary attached to the data
    - **Record** - the goal is to end up with a saved state or history of the analysis
    - **Derive** - the goal is to end up with *new data*: attributes or values generated during the analysis, which become the input to whatever comes next
- **Search** - the middle level: how do you find the thing? The four cases are a 2x2 on whether you know *what* you're looking for and whether you know *where* it is.
  - **Lookup** (known target, known location)
  - **Browse** (unknown target, known location)
  - **Locate** (known target, unknown location)
  - **Explore** (unknown target, unknown location)
- **Query** - the lowest level: once you've found it, what do you ask? The three cases are really about *how many* things you're asking about.
  - **Identify** - one target
  - **Compare** - a few targets
  - **Summarize** - all of them (Munzner's synonym: *overview*)

#### Targets: the nouns

Actions are only half of it. **Targets** are what the action is directed *at* - the aspect of the data the viewer is after. Munzner organizes them by what kind of data they require:

| Available for | Targets |
|---|---|
| Any data | **Trends**, **Outliers**, **Features** |
| One attribute | individual **Values**, **Extremes**, **Distribution** |
| Multiple attributes | **Dependency**, **Correlation**, **Similarity** |
| Networks | **Topology**, **Paths** |
| Spatial data | **Shape** |

(*Features* is deliberately open-ended - it means whatever pattern happens to matter for the task at hand. That vagueness is a bit of a cheat, but a useful one.)

The pairing is the part I actually use. "Compare distributions," "identify an outlier," "summarize a trend" - a verb plus a noun is usually enough to be designable, where either one alone isn't. An action with no target is too vague to make a design decision from; a target with no action doesn't say what the viewer has to *do* with it.

Notice also that the table's left column is a data abstraction: which targets are even on the menu depends on what kind of data you have. This is one of the cleanest places where the two abstractions meet.

#### The "how" verbs are a different axis

There is a separate set of verbs for what the viewer *does with the visualization* - Munzner's **how**, which is the subject of most of the rest of her book. These are not more task verbs; they are the methods a design offers.

- encode
- manipulate
  - select
  - navigate
  - arrange
  - change
  - filter
  - aggregate
- introduce
  - annotate
  - import
  - derive
  - record

Confusingly, **annotate**, **record** and **derive** appear in *both* lists. That is deliberate rather than sloppy: in the "why" list they are goals (I am using this thing in order to end up with derived data), and in the "how" list they are methods (this thing gives me a way to derive). Same word, two different questions - so it's worth saying which list you are quoting from.

Munzner's refrain about these two lists is worth keeping: **why doesn't dictate how.** Wanting to *present* doesn't mean the result has to be static; wanting to *discover* doesn't imply any particular idiom. Keeping the goal and the design choice in separate boxes is most of the value of the split.

### Schulz et al. 2013: Design Space of Tasks

The insight of this paper was to look at tasks not as a list (or tree), but as multiple dimensions to be considered. This creates a multi-dimensional space of tasks, which allows for a more meaningful and flexible way to organize them. 

Importantly, it is an extremely useful view for description: describe the different aspects of the tasks, rather than trying to find a single category for it.

They identify 5 different dimensions:

- **Goal:** the intent with which the task is pursued (exploratory / confirmatory / presentation), 
- **Means:** the method for reaching the goal (navigation, re-organization / relation), 
- **Characteristics:** ("the facets of the data that the task aims to reveal" (low-level vs. high-level), 
- **Target:** determines on which part of the data it is carried out (attribute vs. structural relations),  *(careful: this is not the same as Munzner's "target" above - hers is the aspect of the data you're after, this is which part of the data you're operating on)*
- **Cardinality:** how many instances of the chosen target are considered  (single / multiple / all).

Their list of 5 is motivated by the journalistic 5Ws and an H. This directly motivated our work in developing the Problem Space for Visualization, described above.

### The Scatterplots Task Taxonomy

There are many examples of task taxonomies for specific data types or chart types. I use the one we created for scatterplots because it is representative, but also has some general lessons that work for other data types.

+ {{<reading scatterplots>}}

Our task list was:

- **Object-centric tasks** - about one specific point (or a few)
  - *Identify object* - what are the attributes of this point?
  - *Locate object* - where is the point for this object?
  - *Verify object* - does this point have the value I expect it to?
  - *Object comparison* - how does this point compare to that one?
- **Browsing tasks** - about looking around a region
  - *Explore neighborhood* - what is near this point?
  - *Search for known motif* - is the pattern I am expecting (a cluster, a correlation) actually there?
  - *Explore data* - is there anything unusual or interesting in here?
- **Aggregate-level tasks** - about the collection as a whole
  - *Characterize distribution* - what shape is this?
  - *Identify anomalies* - what doesn't fit the pattern?
  - *Identify correlation* - do the two dimensions relate?
  - *Numerosity comparison* - which region has more points in it?
  - *Understand distances* - what does "close together" actually mean?

While the list was derived for (and makes most sense for) scatterplots and scatterplot data, the tasks can be thought of in a more generalized way. Some general lessons:

- The **extent** of the data: how much data do the tasks consider? **Object-centric** (about specific points) vs. **aggregate** (about properties of groups). Andrienko &amp; Andrienko call this *elemental* vs. *synoptic*. 
- **Relations** among items - e.g., distances between pairs, similarity among groups, etc. Are often important in tasks. Sometimes these compound objects are targets themselves.
- Problems and solutions are separate: the Scatterplots paper contains both, and shows how different tasks (problems) may be addressed by different design choices (solutions). 

## Putting It to Use

If you take one thing from this page, it's the cheat code at the top: these schemes are vocabulary, not rules. 

Here's a summary:

| Ask | The vocabulary | Where it's from |
|---|---|---|
| What is the **verb**? | analyze / search / query; or a low-level primitive | Munzner, Amar |
| What is the **target** (noun)? | trends, outliers, values, distribution, correlation, topology, shape | Munzner |
| How **abstract**? | concrete ↔ abstract | Task Cube |
| How **big**? | low-level ↔ high-level; compose or decompose to move | Task Cube |
| **Why or how**? | objective (the end) vs. action (the means) | Task Cube |
| **How many** things at once? | single / multiple / all | Schulz |
| How much data at once? | elemental (objects) ↔ synoptic (aggregates) | Andrienko, Scatterplots |
| What is the work **for**? | exploratory / confirmatory / presentation | Schulz |
| And **besides** task? | who, what, when, where, how | Problem Space |

Each of these questions is a tool that you can use in understanding and describing tasks. 

## Learning More 

Elsewhere on this site:

- {{<link "/tutorials/data-abstraction-cheat-sheet">}} - the other half of this vocabulary. Task and data abstraction are meant to be used together; neither one picks a design on its own.
- {{<link "/papers/problem-space">}} - the summary of the Problem Space paper, if the section above left you wanting the examples.
- {{<link "/snacks/app-time-graphs">}} - task-first critique in action: two "value over time" graphs, where the better one is better *because of* the task, not because of the data type.
- {{<link "/snacks/250624-routemap">}} - a longer worked example of task (and data) driving an unusual design.

{{<expand "The Readings - and what you might get from them">}}

In a roughly recommended order...

- {{<reading "taskcube">}}<br>
  *Read this to get the perspective on why task abstraction is  tricky.*
- Tamara Munzner, *Visualization Analysis and Design*, Ch 3 "Task Abstraction" ({{<link "/resources/munzner">}})<br>*Read this to get a perspective on why task abstraction is  useful. The actual scheme she describes comes from a paper - but the book chapter is better at the "why is this useful to most people."*
- {{<reading lowleveltasks>}}<br>*Read this to see a concrete scheme that has stood the test of time.*
- {{<reading eyeshaveit>}}<br>*An early and influential paper. It is best known for the "Information Seeking Mantra" but also gets at the idea that there are common patterns for tasks and data.*
- {{<reading problem-space>}}<br>*Shows that task isn't the only thing to consider. As an author, I can say this is one where reading the {{<link link="/papers/problem-space" text="summary">}} might be good enough.*
- {{<reading "tasks:space">}}<br>*A paper that gets at the multi-faceted nature of task descriptions. This inspired the Problem Space paper above.*
- {{<reading "scatterplots">}}<br>*An example of a task taxonomy that is specific to a type of data/chart. I am an author, so I am biased.*

There are many others. 
{{</expand>}}



{{<genai>}}
I wrote an initial draft, and then had Claude help me fill it in and complete it. I also used Claude to generate summaries of many of the sources so I could review them quickly.
{{</genai>}}