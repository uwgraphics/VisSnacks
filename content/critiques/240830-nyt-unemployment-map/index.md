+++
title = 'Unemployment Changes Across The Country (NYT Aug 28, 2024) (CoW 240830)'
date = 2024-08-28T08:20:39-05:00
draft = true
basedon = "https://www.nytimes.com/interactive/2024/08/27/business/economy/jobs-election-county.html"
resourcethumb = "jobs-counties-country.png"
+++

Core lesson: think about what a visualization makes easy to see. Different representations make some things easier, and harder.

<!-- more -->

This comes from a New York Times story [title](https://www.nytimes.com/interactive/2024/08/27/business/economy/jobs-election-county.html). Curiously, this page doesn't show up well in my web browser, the images are from the mobile app (on an iPad).

Here is the "headline" (what appeared in the app that intrigued me):

{{<rimage width=500 src="waj-headline.png" attr="from the NYTimes" caption="A New York Times headline that appeared on my iPad" attrlink="https://www.nytimes.com/interactive/2024/08/27/business/economy/jobs-election-county.html">}}

What caught my eye (from a visualization perspective) was how the irregular nature of counties made it difficult for me to really see what was going on. That isn't {{<link "4-critique" "critique">}}. Let's see what I can learn from it.

What does this make easy to see? One thing that jums out at me: Georgia has a lot of small counties, whereas Arizona has a few big counties. This kind of makes it had to tell how significant the changes are. And because these changes are *percentage* changes, a small county (where a few people can make a big difference).

So, what this visualization helps me see is how many counties have positive or negative trends. Picking out the size of those trends can be difficult (try to find the big arrows in the mix). But, since the number of counties in a state varies widely (it is more about how the state structured itself).

This can be even more misleading because the counties may have different numbers of people - independent of their size. For example, in Nevada, about 3/4 of the population lives in one county (Clark county, where Las Vegas is). So, the small blue arrow in the lower right part of the Nevada map probably represents more jobs than the rest of the state.



- If the viewer wants to see places with no change (or small change), these are not directly encoded - it is only the absence of an arrow. The absence of an arrow might also be part of the "sparsity pattern" (if there are big counties).
- Areas of high density could 

## Alternatives to the design

Coincidentally, I was making a similar picture with a more conventional design for my class. The data isn't exactly the same, but it is per-county unemployment data in two different years, so we can try to make designs with similar intents.