+++
title = 'Considerations for Visualizing Comparison'
date = 2025-09-28T17:44:54-05:00
draft = false
+++

Many (if not all) visualizations are about making comparisons in the data. I've spent a lot of effort to come up with ways of thinking about comparisons, or (if you prefer) to think about visualization in terms of comparison. These were summarized in a 2017 paper (it has a 2018 publication data) "Considerations for Visualizing Comparison". 

The paper gives a "process" for developing a visualization in terms of comparison: first identify what the comparison problem is, figure out what the abstract comparative challenge is (number of items, size of items, complexity of relationships), choose a scalability strategy to address the challenge (scan sequentially, select subset, summarize somehow), and choose a comparative design (juxtaposition, superposition, explicit encoding). I call these last 3 the "three threes" and they give a categorization of comparative challenges and strategies.

<!--more-->

## What is this paper?

It's hard for me to write about this paper - it's a big deal for me. But the actual paper dulls the story (in order to fit into the review process). 

This paper is the result of a 10 year journey (more, because I've continued) to think about visualization in terms of comparison. I started trying to understand how to visualize comparisons. I quickly discovered that this was a good way to think about most visualization (or to put it differently, most visualization problems can be thought of as comparison).

The basic "theory" (the three threes) was pretty much established in 2010 - there is a picture of me explaining it in a lecture in my 2010 class. It took me 7 more years to figure out how to get it into a paper. The ideas, and how I explained them, did evolve a bit. And I added the "Comparative Elements" piece (based on Munzner's ideas on describing tasks).

+ Michael Gleicher. 2018. Considerations for Visualizing Comparison. *IEEE Transactions on Visualization and Computer Graphics* 24, 1 (January 2018), 413–423. Proceedings InfoVis 2017. [(web)](https://graphics.cs.wisc.edu/Papers/2018/Gle18/) [(doi)](https://doi.org/10.1109/TVCG.2017.2744199)

Note: We had a previous comparison paper (a 2011 survey) that is much more highly cited. As I will explain in a moment, it is only part of the story (it's a survey of InfoVis examples organized by the third of the three-threes).

## The Key Idea(s)

If you are trying to help someone visualize a comparison (and I would argue that you should - even if the "problem" is not obviously comparison), I recommend the following steps:

0. Identify the comparison problem in terms of its **elements**.
1. Identify the comparative challenge (what makes it hard). I categorize the challenges into 3 categories - based on how the comparison problem **scales** (a problem may have multiple challenges):
    - too many items to compare
    - items that are too big to compare
    - the relationships between items are too complex
2. Once you have identified the scalability challenge(s), you need to pick a solution. I categorize solutions into 3 categories:
    - scan sequentially
    - select a subset
    - summarize somehow (at the time, I didn't realize subsetting was a form of summarization)
3. Then use this in a comparative design. Again, I categorized these into 3 buckets:
    - juxtaposition (different coodinate systems)
    - superposition (same coordinate system)
    - explicit encoding (figure out the relationship and show it directly)

Yes, I start at zero to make the "three threes" stand out as different.

I find that understanding things in terms of the categories of the three-threes is very useful. 

The paper uses some examples that we were working on at the time (taken from papers I wrote with students). It really was the case that the comparison strategy was a "secret weapon" for coming up with good solutions to hard problems. (OK, having great students is a not-so-secret weapon).

## Do you still need to read the paper?

I can't be objective on this one. I like this paper!

I feel like the paper does a decent job of explaining why and how to use the three threes. I find this to be a useful way to think. And our success at applying these ideas to actually build systems speaks to its success. 

## The "Other Comparison Paper"

In 2011, soon after I started talking about the three threes, some colleagues challenged me on it: do all designs fit neatly into the design categories? To test this, we (well, the students/post-docs at the time) did a survey to find all the comparison visualizations we could, and see if they fell into the categories. They did.

We wrote this up as a paper:
- M. Gleicher, D. Albers, R. Walker, I. Jusufi, C. D. Hansen, and J. C. Roberts. 2011. Visual comparison for information visualization. *Information Visualization* 10, 4 (October 2011), 289–309. [(web)](https://graphics.cs.wisc.edu/Papers/2011/GAWJHR11/) [(doi)](https://doi.org/10.1177/1473871611416549)

While this paper gets cited a lot, I recommend the newer paper. I believe that the reason this paper gets cited so much is for the basic idea (which is described better in later papers). It is only part of the story (the third of the three-threes), and the examples are old.

To make matters worse: of all of the three-threes, the designs are the most problematic. The papers (even the 2017 ones) define the categories in a problematic way - which some other papers have pointed out. I don't think it is wrong - just don't get too hung up on the precise definitions. It doesn't matter if you call something "juxtaposition" or "superposition" - it's more about the concepts.

If you are going to read one, read the later comparison paper. I really believe it ("Considerations of comparisons") completely supercedes this one (the 2011 InfoVis journal survey).

## The Summaries Paper

Just as we tried to validate the design categories with a survey in the 2011 paper, we tried to to see if the three scalability strategies help up (was there something I missed?). I challenged my (former) students to find a counter-example (they didn't). Instead, we wrote a survey paper further organizing things.

- Alper Sarikaya, Michael Gleicher, and Danielle Albers Szafir. 2018. Design Factors for Summary Visualization in Visual Analytics. *Computer Graphics Forum* 37, 3 (June 2018), 145–156. (Proc. EuroVis 2018) [(web)](https://graphics.cs.wisc.edu/Papers/2018/SGA18/) [(doi)](https://doi.org/10.1111/cgf.13408)

This paper isn't specific to comparison. It also focused on summarization (and considers subsets as a type of summarization). I like the framework a lot. The statistics of what they found in the survey was interesting too.

## What does an LLM say?

Here is what Gemini gave me when I gave it the PDF and asked it "Summarize this paper concisely".  (it provided citations into the text, which was handy - but hard to translate onto this page)

Based on the paper provided, here is a concise summary:

The paper "Considerations for Visualizing Comparison" by Michael Gleicher presents a conceptual framework to aid in the design of visualization tools that support comparison tasks. The author posits that while comparison is a common challenge in data analysis, existing design frameworks offer little specific guidance for creating effective solutions.

The proposed framework consists of four sequential considerations to help designers abstract a comparison problem, identify its challenges, and map them to potential solutions:

1.  **What are the Comparative Elements?** This initial step involves identifying the core components of the comparison: the *targets* (the set of items being compared) and the *action* the user wishes to perform on the relationships between those targets (e.g., identify, measure, or dissect similarities and differences).

2.  **Why is it a Difficult Comparison?** This step analyzes the factors that make the comparison challenging, which are categorized into three types of scalability problems: the number of items being compared, the size or complexity of the individual items, and the complexity of the relationships between them.

3.  **What is the Strategy?** To address the identified scaling challenges, designers can choose from three broad strategies. These are allowing the user to *scan sequentially* through items, *select a subset* for focused examination, or view an abstraction that can *summarize* the items or their relationships.

4.  **Which Visual Design?** The final consideration is to select a visual design that aligns with the chosen strategy. The paper classifies visual designs for comparison into three primary categories: *juxtaposition* (placing items side-by-side), *superposition* (layering items in the same space), and *explicit encoding* (creating a new visualization of the relationships themselves).

The paper uses case studies, including the Sequence Surveyor and LayerCake visualization tools, to illustrate how this four-part framework can be practically applied to create and evaluate solutions for complex comparison problems.

{{<genai>}}
I asked Gemini to write the summary that I attributed to it. I used GitHub Copilot to remove the citatons.
{{</genai>}}