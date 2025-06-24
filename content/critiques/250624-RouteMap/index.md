+++
title = '250624 RouteMap'
date = 2025-06-24T07:19:35-05:00
draft = true
+++

Let's look at the "Airline Route Maps" (the ones that are in the back of an airline magazine) as a way to explore the importance of task and how understanding task and data can lead to novel designs. It will show us a different way to think about node link diagrams more generally.

<!--more-->

In the back of airline magazines (these seemed to have gone away), there was always a map that showed where the airline flew. For a big airline, with lots of cities and flights, these maps were usually total hairballs - and I used them as an example for that in class. Almost all of them were very similar in design. (avoid peeking at the radically different design below).

Note: all these maps are circa 2013, and most come from actual in-flight magazines (or the online versions). My circa 2013 cell phone camera wasn't up to today's standards.

Here is the one from Delta (circa 2013):

The one from United isn't that different (the details and data are different):

## Basic Critique

Let's look at these "standard" examples to "critique" and get the basic ideas.

The data is node (city) and links (flight routes). The design is a node-link diagram where the positions of the nodes are fixed based on the position of the city on the map. The links are drawn as "direct" routes (generally arced - unclear if these are actual great circle routes, or some artistic license to make it nicer, and maybe a little less congested, than straight lines). Because the map was meant to be printed in an airline magazine, it is not possible to use interaction.

Let's use the United one...

Before we start, try to critique a bit yourself. What do you notice? What do you think this visualization makes easy to see (or not)? What can you do with this map? What might you want to do with this map that would be difficult?

Let me try this in "stylized critique form" (see {{<lnk "4-critique">}})...

- If the goal is to show that the airline has a lot of flights to a lot of places, the overwhelmingness of the hairball really emphasizes that.

- If the goal is to show the hub and spoke topology on the airlines network, the high densities around the main hubs make that clear. The arced paths, which generally avoid flying over hubs, help this be more clear.

- If the goal is to help the viewer identify specific routes, the large amount of overdraw makes it difficult to follow any individual path, so specific path tracing is likely to be difficult - especially for routes in congested areas.

- If the goal is to remind the viewer of the airline's identity, using the airline's color scheme in the map helps.

Note how these critiques relate to task (obviously). There are things this map is good for, and not good for. Try to use this map to figure out "where can I fly to directly from Madison" or "what are good routes between Madison and Oklahoma City." A better critique practice: try to identify tasks this map is good or bad at, and think about why.

I'd like to think the designer was conscious of this: they were trying to make a map to emphasize the richness of the network by conveying overwhelm. They weren't trying to make a practical route planning tool.

Task is one important factor... but the data is also an important factor. Part of the reason this design works (to the extent it does) are properties of the data. The airline does go to a lot of places. It does have a rich network with lots of flights. It has a hub-and-spoke organization that dominates the patterns.

## An Alternative?

I lacked the creativity to come up with a solution that addressed the focus tasked. For years, I used the example in class - usually the answer was interaction (or something that didn't meet the original design constraints). But then, one day, hiding in the back of an airline magazine, I saw a solution that opened my eyes.

This is a route map for a small airline that specialized in taking people from (Northern) European cities to (Southern) European tourist destinations. Take a minute to figure out how it works on its own. What tasks can you do or not do? 

Let's think about some tasks...

- Where can I get to from Hub X? Somewhat easy: just look for where there there are dots of that color - in theory, this is a "pre-attentive" task (focus on a specific color). In practice, it's a hard as the colors might not be distinct enough.

- If the goal is to make something that is instantly recognizable and usable, the novel design may not be a good idea because it takes a bit of effort to figure out for the first time. However, this novelty might create engagement, and the determined viewer will be able to address some complex tasks.

- If the goal is to make something robustly color-safe (both for color vision deficient viewers, but also resillience to color reproduction issues), the maps reliance on having a relatively large set of distinct colors (one per hub) may be problematic.

- If the goal is to scale to a larger number of hubs, the use of a distinct color per hub might put a constraint on how big the design can get. Also, the viewer has to remember the colors for each hub.

- If the goal is to scale to a larger number of cities, the need to put a cluster of dots at each city might make the map dense. 