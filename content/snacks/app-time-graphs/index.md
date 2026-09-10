+++
title = 'Phone App Time Graphs'
date = 2024-09-09T13:10:36-05:00
draft = false
resourcethumb = "garmin-steps.png"
tags = []
principles = []
+++

In this snack, we look at "value over time" graphs in two different iPhone apps. It's a good opportunity to connect design and task with a comparative critique.

<!--more-->

{{<lesson 1 "Tasks are important for design decisions. Maybe more important than data types." "Task first">}}

Here is a graph from the app from my water heater (yes, water heaters have apps nowadays):

{{<rimage src="water-heater-energy-usage.png" caption="Energy usage from my water heater." attr="Screenshot from the AOSmith app on my iPhone.">}}

Hopefully, the message is obvious: after a month of not using much energy, it started using a crazy amount. Yes, something is broken (the plumber has already ordered a new one).

Of course, there's a Vis lesson here...

My question (or task) is "when did the problem start?" This visualization is not very helpful. To use [critique format]({{<relref "4-critique">}})... if the goal is to help the viewer localize events, having a clear labeling of the axis and easy connection to events would help the user identify the time of events and their specific times.

This graph is the standard choice: we have a measurement over time, so we pick a line graph. But not all apps make this same choice. Here is a graph from the activity monitor in the Garmin connect app (for my watch):

{{<rimage src="garmin-steps.png" caption="Steps per day from my Garmin watch." attr="Screenshot from the Garmin Connect app on my iPhone.">}}

Had the water heater folks chosen this design, it would have been much easier for me to see which day the problem started. There are many different choices in the apps - the Garmin app chose to discretize time, it chose a dark theme, and it chose to encode another variable in the color of the bars. The discretization makes it better suit my task.

Of course, the water heater folks may have had different tasks in mind. 

This is a good opportunity for comparative visualization (comparing visualizations - as opposed to visualization of comparison). What tasks are each visualization good for? What are the different choices in each design, and how do they affect the effectiveness for different tasks?

Arguably, these are different data types: the step counts are discrete (so they need to be binned over periods of time), electric usage could be the rate (instantaneous usage) which is a continuous signal, and therefore the line graph is more appropriate. But the units on the graph are kilowatt hours (which are amounts, not rates) - it could be the per day usage. 

{{<expand "The discrete vs. continuous time question">}}
In the step count case, time is **discrete** - for each day there is one count. It doesn't make sense to say "what is the count at 10am vs 4pm" or "what is the count between 12 and 13.

If the units were kilowatts - the amount of energy being used at a given time, then time is **continuous**. We can ask for the value at any instant. Even if we averaged over the day - we could say it is discrete (each day has one average), but time is continuous (we could ask "what is the average between two days" - thinking of the 24 hours centered at midnight).

The actual graph is "kilowatt-hours", which is the amount of energy used in a period of time. And it does change over the course of a day. So, I assume it is "the number of kWh in each hour" (or some unit of time).

See {{<link data-abstraction-cheat-sheet>}} for a discussion.
{{</expand>}}

There are pros and cons to both designs (binned vs. continuous). The decision should really consider task, not just data type. 