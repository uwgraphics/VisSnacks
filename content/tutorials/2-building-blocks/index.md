+++
title = 'Tutorial 2: How to Think about Visualization: Building Blocks'
date = 2026-08-30T17:23:23-05:00
draft = false
weight = 2
+++

This tutorial argues for thinking about visualizations in terms of a set of building blocks, rather than the conventional approach of chart types and rules. 

<!--more-->

**TODO: Need some opening**

**TODO: Premise - can derive charts/rules from building blocks**

**TODO: setup (at least example), chart types and example**


## Motivating the Building Blocks Approach

**TODO: switch to bar chart example (snow)?**

To continue with the example, in the previous section I called the TreeMap by a standard name used for that design. And I made statements about what TreepMaps were (and were not) good for. 

This suggests a strategy for learning Visualization: learn a long list of chart types, learn what they are good for, learn how to make each one well. I think this is a terrible way to learn visualization. Instead, I prefer to teach visualization by understanding the principles (such as the importance of task) rather than as a long list of chart types. 

Notice that I did not name the other chart. I would have called it a "bar chart" or maybe even a "vertical bar chart". But Excel uses the term "bar chart" for something else - it calls the thing above a "column chart." Amazingly, it works the same no matter what you call it. We might not agree what to name it, but we probably can agree on what it is good for.

 We can think of these charts not as their "types", but rather in terms of the building blocks that make them up. An example of a useful kind of building block is **encoding** - how a data element is translated to visual elements. Whether you call it a "vertical bar chart" or a "column chart", that chart encoded the values (in minutes) by the position of the top of the rectangle along the Y axis measured from X axis (a "common baseline"). For reasons we'll learn about later, we prefer to say "position on common baseline" rather than "height of rectangle" or even "area of rectangle" - even though, in this case, all three of these are actually proportional to the data.

Some advantages to thinking in terms of encodings:

- We can understand how the encodings communicate, which help us reason about whether using a particular encoding is likely to be effective for a particular task.
- We can use these understandings for many different possible charts.
- We can mix and match encodings. (notice that in both charts, I encode "topic" with color)

Once we learn that position along a common axis encodings are good for reading precise values and seeing the largest / smallest, then I will know that many different visualizations based on this will be good for those tasks. Color is good for showing a small set of categories and can be added to many kinds of charts (combined with other encodings).

Here are 9 different visualizations of this same data with "position on common axis" encodings:

{{<rimage src="students-9-ai.png" width="700" caption="9 visualizations that use position-on-common-axis encodings to encode the same Fake Data. The left two on the bottom row were generated with AI fill in Adobe Illustrator and distorted the data. The amount of the distortion of the bottom center is shown by the bottom right visualization.">}}

The key building block of the designs - position on common axis encodings - makes it possible for us to know what tasks they are all well suited for. For example, they are all good for quickly finding the biggest, or comparing two individuals. The differences in the visualizations do matter (e.g., the ones that don't correctly encode the data are problematic, the big circles create some ambiguity in values, etc.). Details are important, but only if you get the basics right. And those details can also be driven by principles (like, be careful about distorting the data).

And, to add one more point about naming: here is another visualization of that same fake data:

{{<rimage width="250" src="students-table.png" caption="A Chart made from (the same) Fake Data">}}

Yes, in my mind a table is a visualization. They are very good for some tasks. See {{<link "obsolete/old-t2-table-example">}} for an example of how the ideas discussed below can be applied to a table.

But, the point... my "method" is to think in terms of building blocks and principles, not chart types. It doesn't matter what we call things, it matters that we make choices that serve the viewer's tasks.

### The building blocks of designs

**TODO: need to smooth over that we introduced encodings first**

A design is the plan for how you are going to turn the data into a "picture" that helps with the task. This is why it's so important to understand task and data before trying to make a design.

One you know your task and your data, you can try to design a solution. I say "design" to explicitly separate the act of coming up with the idea and actually building it (implementation). Design is the act of making conscious choices to solve a problem.

In terms of the class, a big part of what we’ll do is focus on design. What are the choices you can make, and how can you make good choices.

There are four main categories of things that we consider in designing a visualization. You can think of these as the kinds of choices you can make, or the kinds of building blocks you can build a visualization out of.

1. **Data Transformations** - we compute some derived thing about the data that will be useful in one of the other steps.
2. **Layout** - we decide where things go. Technically, this is a position encoding (see encodings below), but position is such an important thing, it gets it's own special category.
3. **Encodings** - an encoding is how we choose to map a data variable to some "visual variable" (an attribute of what we see - like color). Position is a visual variable, but it's special enough that it becomes its own category (see layout).
4. **Interaction** - taking user input is another thing you can do in a visualization. Often, input can be thought of as mapping input actions to changes in the visualization.

Another way to think about this is as "re-design" rather than design. We start with some visualization (a design), pick one of its choices (one of the 4 kinds of building blocks), and change it. I like to think of these like moves in a turn-based game, at each step I pick one of these things to either add (or change, if I am doing redesign).

For a simple example of applying these four design elements in a redesign see {{<link "old-t2-table-example">}}.

Much of designing a visualization turns out to be making one of those 4 kinds of choices. Almost every visualization can be thought of in terms of these 4 building blocks.

I find this list to be a useful way to organize the larger list of more specific things you might do. Most things fit into one category or another. I won’t waste time arguing this is the best categorization – but it's good enough to give you a sense of the kinds of things that you can think about.

We'll learn how to choose these different components, and use them together. We will look at visualizations and try to understand them in terms of these four components. We'll think about redesigning visualizations by changing the choices. We'll try to develop a sense of how to map tasks and user goals onto these kinds of choices.

## How do we make good choices for design?

Creating a visualization is about making those choices for a design so that the result is effective for the task... but how can you choose wisely?

Part of it is trial and error. Sorry. We learn by examples. Reflecting on examples that we make (prototyping), and examining examples of others carefully (critique).

But there are things we can use that can hopefully help us make better choices. Some examples (which are, of course, things we'll study in class):

+ *Principles of Visualization* - Over time, people in the field have gotten some ideas about what works and what doesn't. Sometimes, this folklore is made up and may not be true. Other times, it comes from experience or has been proven by experiments.
+ *Principles of Perception* - Understanding how people see (as in how the visual system works and how the brain interprets images) provides a lot of useful clues as to what designs will (and won't) work.
+ *Principles of Visual Design* - General ideas on how to make things that are "nice" visually and communicate effectively. These principles are the same if you're designing a visualization, a web page, your resume, ... - so they are good principles to learn!
+ *Examples* - Looking at existing examples - both good and bad - can help us. Sometimes, we can gain intuitions so we can make new designs. Other times, standard solutions provide us with answers, or at least a starting point.



## Abstraction - A Key Building Block

### How do we think about tasks and data?

The better that you understand what the visualization is trying to achieve (what will it help the viewer do), the more likely you will come up with a good solution. In the end, everything serves the tasks.

Note the plural: you may have a set of tasks. Often, there isn’t just one at a time. There are a set of things that a set of someones may want to do for a set of reasons. And maybe your solution will address many of these.

I was going to say “it starts with the tasks,” but sometimes you start someplace else (like you have some data and say “I’d like to do something with it” – but even then, I would probably say you have a task: figure out what the right questions to ask are!). However, in those cases, it’s really important to remember that task is key: the sooner you get to “what is this thing going to do for someone,” the better off you are.

This is also not to say that you need to fully understand the task at the beginning. Sometimes, your understanding of the task is hazy, or changes as you learn more (from later stages).

Task is an informal, fuzzy notion. It doesn’t always get explicitly written down or defined. But the clearer you are about it, the better off everything else will be. You can’t succeed unless you have something to succeed at.

One other detail on task: there is a range of kinds of tasks. There are abstract tasks and concrete application tasks. This is actually a spectrum/continuum.

While task is the most central thing, it’s also hard to talk about. We lack good, rigorous ways to talk about it.  For the longest time, it meant that it didn’t get discussed enough (in the literature, in my class, in my work, ...). The fact that it is hard shouldn’t get in the way of us trying to get better at thinking about it. We particularly lack good ways to talk about different levels of task abstraction.

**TODO: requires set up - maybe move doctor example here**

## How to Design and Make Visualizations (Process)

The description above leads to a pretty simple **recipe**. Basically, there are three things to think about (that come from the definition):

1. *Why* are you making this visualization? Who are you trying to help? What are you trying to help them do? I refer to the latter as the "task" - and it's usually more important than the who part.
2. *What* data are you trying to use to achieve this task?
3. *How* are you going to use the data to help achieve the task?

I split question 3 into two parts. There's a planning part, and a part where you make the plan more concrete by filling in the details. Which leads to **the four step recipe.**

1. Task
2. Data / Resources
3. Design
4. Details

In the ideal world, you start at the top, and work your way down through the list.
The steps are iterative: at the end of each step (ideally) you do some evaluation (e.g., critique) and maybe go back to a previous step.

Sometimes the steps don't happen in order. For example, you really want to use a particular tool, try out a new algorithm, or make things a particular color, so you go looking for something to make with these details.

Sometimes, the process seems to start with #2 (Data): one gets some data and needs to figure out what to do with it. But this is actually an initial task: find what is interesting in the data. Often there is an iterative cycle - as the designer understands the data more, they can refine the task.

In a little more detail...

1. **Task** - understand what the purpose of the visualization. Who is it meant to help? What is it meant to help them do?
2. **Data** - what resources are available to help achieve the task? The main thing is (usually) the data.
3. **Design** - what is the strategy for mapping the data into something visual?
4. **Details** - how will you make this strategy into a specific picture / system that produces pictures? What are the specific choices (e.g., colors, implementation, ...)

Later in class, we'll see that this parallels Tamara Munzner's nested model for validation. (We'll read about it in her book, but was a [great paper first](https://www.cs.ubc.ca/nest/imager/tr/2009/NestedModel/ "The Nested Model Paper")). I think in terms of visualization design, not just validation (but evaluation is so important to design that it might not matter), so I adjusted the layers a bit.

If all goes according to plan, you'll understand these 4 steps in the first few weeks of class.

### Collaborative Process 

**TODO: modernize or discard**

Where I start...

When I talk to a new (potential) domain collaborator, I always start with the question "tell me about your science." I want to know the big picture (the why) – because without it, it’s hard to have context.

My first goal is to identify the problem that needs to be solved – it won’t help anyone if we solve the wrong problem. Don't spend time solving the wrong problem well.

Usually people come thinking they want specific help – they want to start with the data, or worse, with the way they are looking at their data (can you make a better chart for me? not without understanding what you are trying to do, so I know what “better” means!) We will get to that, but I think its important to identify the task.

I’ll stress this: if you want to be a visualization scientist (or more generally, a data scientist or computer scientist), one of the best skills you can have is to be able to help people identify their problems. I think it’s hard for people to identify their problems. Part of this is that people get so caught up in the details, that they lose sight of the big picture. Or that they are so set in how they do things that they lose the ability to imagine alternatives.

And, as computer scientists (and/or mathematicians), we have a secret weapon: **abstraction.** This is something that we value/stress much more than other disciplines. For this task phase of visualization, abstraction is a key tool. If we can recognize the abstract task for which the real problem is an instance of, the path to solving it becomes much clearer.

At one level each situation is different. Everyone thinks their problem is unique and special. The challenge is to have ways to think about visualization (data understanding) problems in a way that lets us see how they are similar to other problems. We need to hide the details of the specific problem. This is where abstraction comes in.

## But what about implementation?

**TODO: reevaluate this**

Actually realizing the design is the last part. Well, not really, since usually the process of making a visualization is iterative: once you make something, you learn from it, and refine some of your earlier work, and try again.

If you were thinking “this is a CS class, we should focus on implementation,” you will be disappointed. As I’ve said, this class is more about how to figure out what the right picture to make is (e.g. the design) than how to make it. It's a waste of energy to spend time making the wrong picture.

In the ideal world, you can think about implementation last – it’s an afterthought. In practice, the constraints of having to implement things will probably influence the kinds of designs you will want to consider. A design becomes less attractive if it's too hard to build. In practice, there’s often a tradeoff between the practical issues of implementation and having the best design.

Even within implementation, there is a spectrum of levels. I like to think of this as "fidelity of prototypes." In a sense, you can think of a back-of-the-napkin sketch as an implementation of a design. Most likely an incomplete, non-final one, but an concrete instantiation. It might be a good enough implementation that you can evaluate your design and decide if you want to pursue the design further (and make a higher-fidelity prototype). If you’re lucky, a crude prototype might just solve the actual problem.

One thing I like to stress is the importance of prototyping to explore designs. It’s best to try out lots of ideas, and see if you can figure out their problems before investing a lot in implementing them. Good "Designers" (graphic designers, industrial designers, ...) usually like to explore an entire space of designs – by using very crude "implementations" (e.g. sketches).

Data analysis tools – things like Excel (yes, Excel will turn out to be my favorite visualization tools) or Tableau or … – often let you prototype lots of different things with your data. This “playing” with data – re-ordering it, making various kinds of pictures with it, looking at it all kinds of different ways – is actually a form of rapid prototyping. You can explore a lot of designs easily – often to decide that they don’t solve your problem – but sometimes to see that some of the simple elements actually can help. This “playing with data” (if you can do it) is a lot like sketching a lot of visual designs.

Having a good toolbox so that you can implement your designs is useful. If you don’t have one, you will be limited in what designs you can explore, and won’t be able to choose designs that you can’t realize (that’s not quite true: if you can come up with a great design, you may be able to get someone else to implement it). Part of my premise for this class (or at least this instantiation of it) is that we can all have different toolboxes – some students might be wizard programmers, some might be fabulous artists – but we all can have some common basic tools (e.g. sketching), and we can all explore designs using our respective toolboxes.

Now, if you’re saying "but I want visualization to be about writing fancy programs using complex data analysis methods and algorithms and spiffy programming things ..." let me give you a bit of caution.

Building a custom visualization solution by programming should be a last resort. You should really believe that your problem cannot be solved by some easier method. Going back to the medical analogy, writing a program for a new design is like inventing a completely new (and therefore untested) treatment. Yes, if your patient has a mysterious disease and is going to die you want to take these drastic measures. Or, you might do an experiment if you believe that you can afford the risk on this patient in order to learn something to save the next ones (this is the excuse we use as researchers).

That said, all too often there are other factors that make us want to take the extreme measure. Sometimes, we just want to practice our inventive skills. Sometimes our "customers" think they want to have something novel (don’t make it look too easy!). Sometimes we really want to try out some implementation idea, or show off some challenging design idea. And sometimes, it might just be easier to re-implement a standard design than to figure out how to make an "easy" tool do what we want. (You’d be amazed how often I’ve found myself writing Python code for scatterplots because I wasn’t in the mood to wrestle with Excel). Sometimes, it’s hard to find a decent “easy” tool for something that should be easy (like graph layout).

## Now What?

To give you a sense of where this goes into my class (not necessarily in this order) ...

1. We need to understand **why** we use visualization. Why can (well designed) pictures help people do things?
2. We need to be prepared with **critique** and **redesign** techniques that we can use to explore the ideas by examining examples.
3. We need to discuss **abstraction** so we can talk about tasks, data, and designs.
4. We need to learn about **encodings** which are the building blocks that we use to make visualizations, so we can take designs apart and put them back together.
5. We need to think about **evaluation** so we can assess whether or not we are making good visualizations.
6. We need to learn about **perception** (how we see), since it helps us understand what is and isn't easy to see. **Color** is an important part of this.
6. We need to consider **interaction** because it is a useful tool in designs.
7. We need to think about some **core challenges** like scalability.
8. We need to consider some examples of **challenging data types** (such as graphs and volumes)

{{%genai%}}
I used Generative Fill in Adobe Illustrator to create two of the position-on-common-axis charts (the ones that have clocks).
{{%/genai%}}