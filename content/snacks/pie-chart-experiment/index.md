+++
title = 'Pie Chart Experiment'
date = 2025-06-25T10:01:54-05:00
draft = true
+++

Pie charts are better than bar charts. We can even show it in an experiment. But the real lessons are that we should choose appropriate charts for the viewer's task, and if we really know the question, we might just want to give the viewer the answer. 

<!--more-->

Pie charts are much maligned: the pundits hate them. But experiments show they work remarkably well. This is worthy of a longer discussion (coming soon). The short version: pie charts are really good at what they are good for, but are often misused.

My student (Connor Bailey) and I wanted to have an experiment that showed the superiority of pie charts(*), so we ran the experiments described here. They provide empirical evidence for something that should be obvious: pie charts are really good at what they are good at, significantly better than bar charts. 

{{<expand "A Note on These Unpublished Experiments">}}
These specific experiments are not published anywhere else (yet).

These experiments aren't paper worthy by themselves. We shouldn't need to run an experiment to document we already "know". And I don't believe these experiments are novel - different versions exist in the literature (even if I can't point to them off the top of my head). The "research question" of "Pie Charts are Better Than Bar Charts" isn't interesting unto itself. 

We ran these experiments are part of a longer chain of experiments that get at more "interesting" research questions. That chain has lead us to "scientific" results (that have been conditionally accepted as of now).

You might question inpublished (and, therefore non-peer reviewed) experiments. I urge you to use your judgment as to whether you trust them. Your judgment is probably just as good as the judgment of 3 random reviewers (who were probably reading quickly since they had a big stack of reviews to do). If it gives you comfort, these experiments were detailed in a paper submission. The paper was (justifyably) not accepted because the the collection of 7 (!) experiments didn't tell a complete story. The reviews did commend the care in the individual experiments.

And, I'll admit: we ran the first experiments (described here) as practice. We knew the results we expected - and if we couldn't confirm them, I would have not trusted our experimental skills, not that the ideas were wrong.

These experiments were pre-registered.
{{</expand>}}

**Warning:** This is an informal writeup. In a paper, we would write it in a different way. 

The **hypothesis**: viewers are *better* at estimating the proportion of a part (relative to the whole) using a pie chart than a bar chart. By "better" we mean both more accurate and faster. Doing, we were honestly unsure if we could measure both (for reasons I will explain later). In the actual experiment, we considered 4 chart types (but here, I will focus on Pie Chart and Bar Charts).

Try this yourself. Here are examples of the 4 "chart" types (I consider the table a chart). Your task: estimate the proportion (percentage of whole) of the highlighted part. I'm not going to talk about the linear part-whole chart here (it's a whole story unto itself). 

I'm guessing, you got an answer very quickly by glancing at the  part-whole charts (pie and linear) and making a visual estimate of the size of the piece relative to the whole. But with the bar chart, there is no easy way to assess the whole (maybe you mentally/visually add the bars together? or try to estimate the area of the complex shape?). With the table, you probably added numbers in your head. It shouldn't suprise us that the part-whole designs are better. And, sure enough, the results bear this out.

Basically, the part-whole charts (pies and linear) are significantly better than the non-part-whole charts (bar charts and tables). Within each pairing, things are close enough that they aren't worth mentioning (even when they are significant).

{{<expand "Yes, we did the statistics...">}}
You shouldn't be convinced by the chart, you'll have to trust us that we did the statistics correctly. We'll provide a full writeup elsewhere.

We ran some simulation experiments to estimate confidence intervals in a non-parametric way. We used a 95% bootstap confidence interval as an initial check for significant differences. The non-overlap of these intervals (seen in the chart) means something. Exactly what depends on your statistical philosophy. 

The data is not normally distributed, therefore, we used non-parametric statistics (not the more common repeated measures ANOVA). We used a CHI-Square test to check that the differences between groups are significant, and then used both Mann-Whitney I (MWU) and Wilcoxon Signed Rank (WSR) tests to check pairs. 
{{</expand>}}

The details of the experiment do matter (We'll provide them elsewhere). Briefly, this was a crowd-sourced experiment run on Profilic in the web browser. Participants answered with a slider that had 5% increments, and the correct answers were always multiples of 5. But I hope that the "main effect" is big enough (and common sense enough) that you'll trust me.

## The Actual Lesson

Pie Charts (and other part-whole designs)  are good for making part-whole estimates. Bar Charts (and tables) don't provide the "whole" - which makes estimating the part/whole relationship hard. 

If you want to make it easy to see the part/whole relationship, a part whole may be a good option - since it does that.

## A Subtly Different Experiment

Here is a subtly different experiment. Everything is bascially the same, but we're going to change the charts very slightly by modifying the labels (or data in the table). We'll explicitly give the viewer the part whole relationships. 

Now, there is no estimation involved. For the table you can read the answer. Everyone gets it exactly right. For the bar chart, you simply need to estimate the height of the bar on the scale. People are good at this. The story is quite different than estimating. Not surprisingly, people are really fast and accurate with tables and bar charts. 

Of course, there are down sides to this:

1. We needed to know that the viewer wanted the part/whole proportion. But, we only would have chosen the pie chart in that case.
2. The viewer needs to know the numbers are the percentages, not the actual quantities. If you want to provide both on the bar chart, you need a dual axis chart (which brings up all kinds of issues). 
3. (this is speculation...) The pie chart signals to the viewer that you want them to appreciate the part whole relationship (not make the kinds of comparisons bar charts are good at).
4. (again, speculation...) By having the viewer do the estimate themselves (rather than reading the answer), we might help them appreciate the relationship.

