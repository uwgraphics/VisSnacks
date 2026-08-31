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