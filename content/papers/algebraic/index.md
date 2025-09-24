+++
title = 'Paper: An Algebraic Process for Visualization Design'
date = 2025-09-24T10:29:57-05:00
draft = false
+++

The paper *An Algebraic Process for Visualization Design* by Gordon Kindlmann and Carlos Scheidegger is something that influenced my thinking a lot. It is a great example of visualization formalism that has a big and practical payoff in how we think about visualizations. It came back to mind recently. 

The paper has a concise message that fits well in the "re-papering" format: changes to the data should correspond/correlate to changes in the visualization. The paper holds up well to time (it is from 2014). 

<!--more-->

Gordon Kindlmann and Carlos Scheidegger. 2014. An Algebraic Process for Visualization Design. *IEEE Transactions on Visualization and Computer Graphics* 20, 12 (December 2014), 2181–2190. [(doi)](https://doi.org/10.1109/TVCG.2014.2346325) 

## The Key Idea(s)

There is a wonderfully simple and elegant idea here. I am going to over-simplify it for our purposes.

> The amount of difference in the visualization should be correlated to the amount of difference in the data.

Visualization can be viewed as a process/function that translates "data" into a visualization (or even beyond - what the viewer actually sees in the visualization). This might include many steps (measuring the world, organizing the obversations, transforming the data, making pictures, the viewers vision and interpretation, ...).

We can write this as a simple "equation" where D is the data, V is the visualization, and f is "the process

> V = f(D)

We can express properties that we care about (of f, our visualization process) in terms of changes (deltas or derivatives) to V and D.

Specifically:

- A change in D should cause a corresponding change in V. If there's a meaningful difference in the data, there should be a meaningful (visible) change in V.
- A change in V should only come from a corresponding change in D.
- The size of change should be proportional... small changes in D should lead to small changes in V; big changes in D should lead to big changes in V.

They break this into three cases:

- Representation Invariance: For the "same" (or equivalent) data, the same visualization should be produced.
- Unambiguity: For a given visualization, there should be only one set of data that could have produced it.
- Visual Data Correspondence: The amount of change in the visualization should be proportional to the amount change in the visualization. 

In retrospect, these may seem like obvious properties to seek - but the Algebraic Framework gives a nice formalism to state them and assess them.

## The Rest of The Paper

The paper gives these ideas in a clear and formal way. It's impressive to have both. They give more nuance to the definitions.

The paper has a set of simple examples, drawn from many different types of visualizations, that make the different types of problems clear. The examples often provide solutions: if you identify this problem, here's a design alternative that doesn't have the same issue.

## Do you still need to read this paper?

The basic idea is simple - and you probably get it from my one sentence summary "visual changes should be proportional to data changes". However, the paper does such a nice job of expressing this concept with a formalism that I recommend reading it. The formalism allows the authors to get at nuance beyond my over-simplification. And they have good examples.

And it is a great example of an application of formalism for visualization.

## What does the AI say...

NotebookLM summarizes the paper as:

> The academic paper by Gordon Kindlmann and Carlos Scheidegger introduces an algebraic model for visualization design based on three key principles to guide evaluation and creation of visual encodings. The Principle of Representation Invariance asserts that the visual impression should not be determined by arbitrary choices in data representation, while the Principle of Unambiguous Data Depiction demands that changes in the underlying data must result in noticeable changes in the visualization. Finally, the Principle of Visual-Data Correspondence focuses on ensuring that meaningful changes in data correspond with analogously meaningful changes in the visual impression, which is mathematically grounded in their core equation relating data symmetries ($\alpha$) and visualization symmetries ($\omega$). The authors illustrate how these principles help diagnose failures in existing visualizations, such as "hallucinators" for invariance failures and "confusers" for ambiguity, offering a structured, mathematical approach for designing more effective visualizations. The paper concludes by suggesting that this framework can inform future research, particularly in understanding dimensionality reduction and enhancing visualization pedagogy.

If I ask for the key takeaways:

> The main takeaway for students is to adopt the **algebraic visualization design process**, which relies on describing the relationships between **Data (D)**, **Representation (R)**, and **Visualization (V)** mathematically. Students should rigorously apply the three core design principles—**Representation Invariance** (ensuring visualizations are not affected by arbitrary choices, avoiding **hallucinators**), **Unambiguous Data Depiction** (ensuring data changes are visible, avoiding **confusers**), and **Visual-Data Correspondence** (matching important data transformations ($\alpha$) to clear visual changes ($\omega$))—to systematically evaluate visualizations, clarify tradeoffs, and improve their designs. This approach provides **explicit, unambiguous descriptions** that enrich pedagogy beyond traditional design maxims.

In my mind, the 3 categories are all special cases of the third (representation invariance and Unamiguity are special cases of Correspondence), and I view data representation as part of the process. To me, this is nuance - which you will get from the paper.

{{<genai>}}
I used [NotebookLM](https://notebooklm.google.com) to generate the summaries I said come from NotebookLM.
{{</genai>}} 