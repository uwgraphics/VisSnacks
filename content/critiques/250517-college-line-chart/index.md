+++
title = '250517 College Line Chart'
date = 2025-05-17T08:52:47-05:00
draft = true
+++

This is a lesson on Axis Truncation for Line Graphs. It was inspired by a graph in 
today's [New York Times](https://www.nytimes.com/2025/05/13/upshot/boys-falling-behind-data.html). 
I like the example because (1) Axis Trucation was on my mind (from {{<lnk "240830-yeping-axis" "a previous critique">}}), (2) this seems to be a reasonable use of Axis Truncation, and (3) the data (and an alternate plot) were easily available, so we can do comparative critique and try some redesign variants ourselves.

First, here's the line graph from the New York Times, this is a screenshot from my phone:
{{<rimage src="250517-women-outpace-nyt-phone.png" caption="A line graph comparing college attendance rates for men and women over time." attr="from the New York Time" attrlink="https://www.nytimes.com/2025/05/13/upshot/boys-falling-behind-data.html">}}

> *(generic critique advice)* Take a minute to look at this chart - click on it to see it at full size. It might be harder to interpret out of context (but this was a "teaser" image on my front page). What does it make easy to see? What might we learn from it's choices?

Note: I do not want to talk about the specific message conveyed in this chart (although, that might come up), or why this is the right or wrong statistic to show (it is the rate of college attendance of high school graduates - it doesn't consider differences in the rates of high school graduation, or success rates once these students get to college). The choice of data is an important point, but requires too much context (which the [article](https://www.nytimes.com/2025/05/13/upshot/boys-falling-behind-data.html) should give).

This is a simple chart - comparing two time series (women and men) over a series of years 1960-2020 for a continuous measure (rate of high school seniors attending college). 

Here is a very similar chart - it's effectively the same data (over a shorter range of time). It comes from the U.S. Bureau of Labor Statistics (BLS), and on their [web page](https://www.bls.gov/opub/ted/2024/61-4-percent-of-recent-high-school-graduates-enrolled-in-college-in-october-2023.htm) it (1) is interactive and (2) allows downloading the [data]({{<resource-link "college-enrollment-rates-bls.csv">}}) (so we can experiment). 

{{<rimage src="college-enrollment-rates-bls.svg" caption="A version of the line chart from the BLS." attr="Bureau of Labor Statistics (BLS)" attrlink="https://www.bls.gov/opub/ted/2024/61-4-percent-of-recent-high-school-graduates-enrolled-in-college-in-october-2023.htm">}}

> *(generic critique advice)* Take a moment to compare these similar charts. What are the (meaningful) differences? What can you learn from the different choices?

{{<genai>}}
I used [Perplexity](https://www.perplexity.ai/) to search for the data and find links.
{{</genai>}}
