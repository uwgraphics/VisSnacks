+++
title = 'Task Abstraction: A Cheat Sheet'
date = 2026-09-07T07:40:41-05:00
draft = true
+++

Task abstraction is how we discuss what the visualization is trying to help the viewer do. Typically, this is done by trying to organize the range of tasks into categories or a taxonomy.  

<!--more-->

Task is central to visualization: it's the thing that we are trying to help the viewer do. I (and others) define visualization as having a task (see {{<link "/tutorials/1-what-is-vis">}}), and define good visualizations as being effectice at those tasks. Having good ways to discuss task is important.

Even the term "task" itself is problematic. It is hard to pin down precisely. Different papers mean different things by the term "task".

The goal of task abstraction is to have a way to describe what the visualization is trying to do (or to help the viewer do) in a manner that is specific enough to be meaningful, but broad and general enough that is allows for generalized thinking and for seeing similarities in problems and solutions.

My goal is to have ways for discussing the "problems" that visualizations are trying to address so that we can choose solutions that solve them. I am much less concerned about trying to put tasks into neat little boxes.

I call it a "cheat sheet" because it's designed to be a quick summary of some of the main things you would get from reading a whole list of papers and fusing the ideas together. It's not trying to cover everything - it's just a slice across the landscape. It's the basics I think you need, and it might inspire you to read the original sources.

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
- Perspective: **Why (Objectives)** vs. **How (Actions)**

Some examples:
- Find a vaccine for HIV - concrete, big
- Identify an outlier - abstract, small, objective

Different levels of abstraction:
- Make an informed decision
- Select between options with different tradeoffs
- Choose a transport option 
- Select a train ticket between Frankfurt and Stuttgart on Aug 15

## The Problem Space: Beyond Tasks

Task is only part of the description of "the problem" that a visualization might be addressing. We (some colleagues and I) suggested the idea of a *Problem Space* for visualization that considers different dimensions of scenarios that can (or should) influence visualization design. The paper is summarized at {{<link "/papers/problem-space">}} (the summary is probably sufficient).

The problem space is defined using the 5Ws and an H from journalism (that actually dates back even farther):
- **Who** has the problem / will be the viewer
- **Why** are they using the visualization (this is the objective or task)
- **What** are they looking at (the data)
- **When** in the analysis process (what phase)
- **Where** the context
- **How** do they *expect* to be helped (not the actual solution)

## Example Task Organizing Schemes

I provide some examples (taken from the reading list above) that give examples of task description concepts. While it is organized by the source, you can mix and match the different pieces.

### Organization Schemes: Taxonomies vs. Typologies vs. Categorizations

Historically, researchers used the term taxonomy to describe schemes for organizing tasks. Technically, taxonomy is a very specific type of organizing structure - that few task taxonomies actually follow. For completeness, here are the differences - but I won't blame you if you just call everything a taxonomy. 

- **Categorization** - The broad, general term; often used to imply an informal grouping.
- **Classification** - Groups things into categories where the categories are mutually exclusive and jointly exhaustive (every item has exactly one home). Usually has strictly defined rules for each category.
- **Taxonomy** - A hierarchical classification where items are grouped based on observable characteristics into groupings with strict boundaries.
- **Typology** - A grouping based on "ideal types" or characterizations. The boundaries between the categories may not be well defined.
- **Spectrum** - A (conceptually) continuous dimension that something can be placed on.
- **Space** - for example, a "Design Space" or a "Problem Space". This refers to a set of separate dimensions, each might be a spectrum or some categorization.
- **Clustering** - a type of categorization where things are grouped by similarity.


### Schneiderman 1996: Task by Data Type Taxonomy

+ {{<reading eyeshaveit>}}

By 1996, Ben Schneiderman was already famous. This paper was an invited survey where he tried to organize a zoo of different experimental designs into a framework. 

Notably, this paper tried to separate **data abstraction** from **task abstraction**. Neither list was very rigorous, but it was an important starting point for others. 

His list of tasks:
- Overview
- Zoom
- Filter, 
- Details-on-demand
- Relate
- History
- Extract

This paper is is mainly famous for his *information seeking mantra*: **"Overview first, zoom and filter, then details-on-demand"**, which isn't strictly part of either taxonomy. However, the mantra teaches us a lesson: it isn't a universal law, it's a common pattern that he recommends considering.

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

### Munzner 2014 (Book), Brehmer&Munzner 2013 (Multi-Level Typology)

+ {{<reading multi-level-tasks>}}
+ Tamara Munzner, *Visualization Analysis and Design*, Ch 3 "Task Abstraction" ({{<link "/resources/munzner">}})

The paper was one of the first task categorizatons that acknowledged the multi-level nature of task, and tried to do things at multiple levels. It was also the first to be precise about terminology (it is a typology, not a taxonomy).

The idea of levels was made much clearer in the Task Cube paper.

One thing I like about their approach is describing tasks in terms of actions and targets (or verbs and nouns). Splitting the description of the task this way can simplify it.

The main part of actions are the "why" verbs that they organize hierarchically:

- Analyze
  - Consume
    - Discover
    - Present
    - Enjoy
  - Produce
    - Annotate
    - Record
    - Derive
- Search
  - Lookup (known target, known location)
  - Browse (unknown target, known location)
  - Locate (known target, unknown location)
  - Explore (unknown target, unknown location)
- Query
  - Identify
  - Compare
  - Summarize

There are a different set of verbs for the actions performed with a visualization.
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

### Shulz et al. 2013: Design Space of Tasks

The insight of this paper was to look at tasks not as a list (or tree), but as multiple dimensions to be considered. This creates a multi-dimensional space of tasks, which allows for a more meaningful and flexible way to organize them. 

Importantly, it is an extremely useful view for description: describe the different aspects of the tasks, rather than trying to find a single category for it.

They identify 5 different dimensions:

- **Goal:** the intent with which the task is pursued (exploratory / confirmatory / presentation), 
- **Means:** the method for reaching the goal (navigation, re-organization / relation), 
- **Characteristics:** ("the facets of the data that the task aims to reveal" (low-level vs. high-level), 
- **Target:** determines on which part of the data it is carried out (attribute vs. structural relations),
- **Cardinality:** how many instances of the chosen target are considered  (single / multiple / all).

Their list of 5 is motivated by the journalistic 5Ws and an H. This directly motivated our work in developing the Problem Space for Visualization.

## Learning More 

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