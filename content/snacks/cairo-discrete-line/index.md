+++
title = 'Cairo Discrete Line'
date = 2024-10-09T13:24:31-05:00
draft = true
+++

Line charts can be used (with caution) even when the X axis is neither interval or continuous.

<!--more-->

We were discussing "rules" around line charts in class, and a student brought me a nice example. That shows the principles in action.

I hesitate to give "rules," especially in terms of chart types. But the guidance on "bar/dot vs. line" chart is pretty common. The principle is that connecting the dots implies the interpolation between the end points and emphasizes the slope; if interpolation and/or slope isn't meaningful, connecting the dots should be done with caution. It still may be useful (because it can help with connection).

(Using the NOIR levels of measurements: Rational, Interval, Ordinal, Nominal/Categorical).

So the "rules" suggest that line designs are good when the X axis is continuous and interval, acceptible if the X axis is interval, can be used with caution if it is ordered, and should be avoided for nominal categorical.

A student brought this example from Cairo's book:
{{< rimage src="cairo-discrete-lines.png" width=400 caption="A line graph with a discrete axis." attr="Figure 5.17 of Cairo's *The Truthful Art*, p. 140." >}}

The student asked why connecting the dots was a valid choice (at first, he didn't realize it was ordinal).

1. It's Cairo and presented in his published work - so if he does flaunt a rule, he probably did it intentionally. 

2. The axis is definitely (at least) ordinal (life stages/generations in order). 

3. To emphasize that the lines are there to connect discrete things, there are dots. Notice that Cairo is using the edges for connection and making the discrete points very salient. 

4. I might argue it is an interval/continuous axis – if we think of it as “life stages” – it is totally sensible to think about being halfway between stage 1 and stage 2, or even the slope as "the rate of decrease in influence as we move between life stages".

One thing that strikes me in the image: my eye does follow the slopes. For example, the trend in the red line (Television) as we go from Xers, to Boomers, to Mature (3,4,5) is a pretty constant slope. Is this the wrong thing being easy to see? In this graph, I think that slopes could be meaningful - the rate at which things decrease as we move through life stages. It is not an unreasonable thing to think about (at least qualitatively).
