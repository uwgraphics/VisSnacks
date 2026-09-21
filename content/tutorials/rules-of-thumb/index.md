+++
title = 'Slogans: Rules of Thumb'
date = 2026-09-19T09:38:27-05:00
draft = true
+++

These are "slogans" - concise, hopefully memorable statements of commonly useful guidance. Each concept might deserve a whole book to discuss its nuances, special cases, exceptions, arguments, counter-arguments, empirical support, applications, ... None of that here.

<!--more-->

Don't think of these as universal laws. Think of them as "things I think are usually true/useful."

Some people call these "guidelines" or principles, or rules of thumb - but that term makes others cringe. I'll go with "slogans to think about when designing or critiquing visualizations."

I am just dumping some here. This is the order I typed them, not necessarily their importance. 

1. **Task first: Know your purpose.** - Who, What, Where, Why, When, and then How (but Why first).
2. **Match designs to data.** But remember #1: data is, at best, second. However, so many "unforced errors" are mismatches of data and design.
3. **The opposite of "designed" is "not designed."** (not necessarily bad design) - Make choices consciously.
4. **Use part-whole designs (only) for part-whole tasks with part-whole data.**
5. **Guide attention deliberately.**
6. **Choose Color Carefully.** - Color is complicated. Every "rule" has exceptions. But many are true most of the time. *Use color with intent, not just for decoration.* Although, decoration can be an intent. 
7. **Use ordered encodings for ordered things.** - This is a special case of #2, but comes up a lot with colors.
8. **Be mindful of clutter.** - It's OK to add things to a visualization, just be aware that everything you add has a cost: make sure it is worth it. Simplification isn't necessarily improvement.
9. **Prefer effective encodings.** - In general, precise encodings are effective for many tasks. Use good encodings first.
10. **Beware unintentional distortions, especially illusions.**
11. **Be careful with Axis Truncation.** - Axis truncation should be used with care: sometimes it is important to expose detail, sometimes it is misleading. While there are general patterns (e.g., avoid truncating bar charts since it messes up their redundant length encoding), there are exceptions.
12. **Facilitate Comparisons.**
13. **Use titles, labels, captions, and annotations appropriately.**
14. **Reduce demands on memory.** - Eyes beat memory.
15. **Respect the viewer's expectations.** 
16. **Accessibility.** - You should care.
17. **Be consistent, or be intentionally inconsistent.**
18. **Avoid unjustified 3D.** - Generally, 3D is only worthwhile for cases where there is a physical 3D structure that is important. 
19. **Encode Data (avoid encoding non-data).**
20. **Avoid making the view do math.** - 
21. **Beware biases and heuristics.** - Your viewers might not read the chart the way you expect.
22. **Avoid ambiguous encodings.** - If there are multiple ways to read something and they give different answers, your viewers will pick the wrong one.
23. **Don't Dump Data.** - Avoid just giving a pile of data to the viewer - give a large number of things when the design can make it support the task, for example by focusing on parts of interest or allowing for visual summarization. Don't just give the viewer a pile of data and say "good luck".
24. **Standard charts are standards for a reason.** - If you have a standard problem, consider a standard solution. They are time-tested, readers are familiar with them, implementations are available, etc. 
25. **Don't solve the wrong problem well.**