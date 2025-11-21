+++
title = 'A Framework of Interaction Costs in Information Visualization'
date = 2025-11-21T17:06:14-06:00
draft = false
+++

We often think of interaction as a solution to visualization problems as it has many upsides. However, there are costs to the user (beyond the obvious costs in terms of design, implementation and deployment). The paper "A Framework of Interaction Costs in Information Visualization" by Heidi Lam gives a nice way to think about these costs. It's an adaptation of earlier work in HCI, but she shows how appropriate it is. She validates the framework by applying it in a broad survey of visualization papers. 

The framework has three "top level" categories of costs: costs to form goals, costs to plan and execute to achieve goals, and costs to evaluate how the goals are met. The seven interaction costs identified in the framework are (1) Decision costs to form goals; (2) System-power costs to form system operations; (3) Multiple input mode costs to form physical sequences; (4) Physical-motion costs to execute sequences; (5) Visual-cluttering costs to perceive state; (6) View-change costs to interpret perception; and (7) State-change costs to evaluate interpretation.

## What is this paper?

This paper provides a framework for how we can think about interactions in terms of the "costs" to the user - what might be difficult for them, and where they might need to spend effort on the interaction. It is a good reminder that there arw downsides to interaction.

+ Heidi Lam. **A Framework of Interaction Costs in Information Visualization**. _IEEE Transactions on Visualization and Computer Graphics_, 14(6), 1149–1156. [(doi)](http://doi.org/10.1109/TVCG.2008.109) [(UW Library)](https://ieeexplore-ieee-org.ezproxy.library.wisc.edu/document/4658124)

Most of the paper is a survey that tries to validate that the framework is an appropriate and useful tool for thinking about visualization. Basically, she surveyed a large number of papers and found examples of all the costs. 

## The Key Idea

In order to use something that is interactive you need to (1) figure out what you want to do, (2) figure out how to make the system to it, (3) execute that plan, and (4) check that the system actually did what you wanted. Each part of these can pose challenges for the user.

The paper is a reminder that we need to consider all of these costs. In particular, it is easy to forget that it takes effort to figure out how to achieve goals using a system's capabilities.

The HCI literature (most famously seminal work by Don Norman - that I mainly know through his popular press book "The Design of Everyday Things") describes this as the "Gulf of Execution" (a user needs to figure out how to make the system do what they want and execute the plan) and the "Gulf of Evaluation" (the user needs to figure out if they succeeded). This paper adds a third "Gulf" which is that the user needs to figure out what they want. 

The paper breaks the process into smaller steps, each is identified as a "cost":

1.  **Decision costs to form goals**: The user needs to figure out what they want.
2.  **System-power costs to form system operations**: The user needs to figure out how to use the system's features to do what they want.
3.  **Multiple input mode costs to form physical sequences**: The user needs to figure out how to actually operate the interface. This is a bit of a left-over from the HCI origins. In most cases for Vis this is just "I need to move the mouse".
4.  **Physical-motion costs to execute sequences**: The user actually has to perform the physical actions (like moving the mouse). Costs 2, 3, and 4 cover the **Gulf of Execution**.
5.  **Visual-cluttering costs to perceive state**: The user needs to interpret the resulting display.
6.  **View-change costs to interpret perception**: Interactions cause the displays to change - the user needs to figure out what those changes are and what they mean.
7.  **State-change costs to evaluate interpretation**: Once the displays are "read" the user has to figure out what the data they just got means. Costs 5, 6, and 7 cover the **Gulf of Evaluation**.


## Do you need to read the paper?

The main point of the paper is the framework of 7 costs (organized into 3 gulfs). Most of the paper is the survey showing examples of the costs in circa-2007 systems. You probably don't need to see the paper - seeing the costs is likely to be good enough.
 
## What does an LLM say?

This is what NotebookLM has to say about the paper...

> The source introduces a framework of seven interaction costs in information visualization, aiming to address the lack of focus on usability problems related to interaction design. Inspired by Norman’s Seven Stages of Action, the researchers collected 61 usability problems from 32 user studies across 484 papers to categorize these costs, including factors like Decision costs and various Physical-motion costs. The framework expands upon Norman's concepts by proposing a gulf of goal formation alongside the gulfs of execution and evaluation, specifically to account for the cognitive effort in establishing analytical focus. Ultimately, this work seeks to guide visualization designers by highlighting areas where interaction costs impact usability and suggesting design considerations to mitigate these issues.

It provides a summary of the costs:

The framework of interaction costs identifies the following seven costs, inspired by Norman’s Seven Stages of Action:

1.  **Decision costs to form goals**: Costs incurred when users need to decide on ~~a subset of data or interface options to focus on, especially as interfaces become more powerful and display more data points.~~ This is associated with the newly proposed Gulf of Goal Formation. *IMHO this is more about determining the question*
2.  **System-power costs to form system operations**: Costs associated with translating a user's question into the correct sequences of system operations, which can be difficult in powerful systems offering a large set of operations.
3.  **Multiple input mode costs to form physical sequences**: Costs that arise when the input device offers multiple modes, making it difficult to translate system operations into device operations due to issues like inconsistent mode operations across multiple views, imperceptible mode changes, or overloaded input controls.
4.  **Physical-motion costs to execute sequences**: Costs related to the physical execution of sequences, such as mouse positioning (modeled by Fitts’ Law) and mouse dragging, where even low-cost motions can cumulatively create usability problems. Costs 2, 3, and 4 cover the **Gulf of Execution**.
5.  **Visual-cluttering costs to perceive state**: Costs associated with interaction causing visual distraction or occlusion, making perception of the system state difficult, such as when visual highlights occlude selected lines or mouse hovering causes unwanted visual disturbance.
6.  **View-change costs to interpret perception**: Costs incurred when users must associate objects between the old view and the new view following an interaction that changes the display, especially concerning temporal object association (e.g., zooming), spatial object association (e.g., view coordination), or local/global object association (e.g., navigation).
7.  **State-change costs to evaluate interpretation**: Costs associated with evaluating the outcome of an interaction or analysis, often requiring reflection on multiple data views or analysis states, necessitating support for refinding previously viewed data projections. Costs 5, 6, and 7 cover the **Gulf of Evaluation**.

{{<genai>}}
I loaded the paper into NotebookLM and used its summary for the What does an LLM say?. I also asked it to generate an SVG version of the figure, which wasn't that useful.
{{</genai>}}