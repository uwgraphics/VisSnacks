# Shneiderman, "The Eyes Have It: A Task by Data Type Taxonomy for Information Visualizations" (IEEE Symposium on Visual Languages, 1996)

**What it is:** A short conference paper that states the **Visual Information Seeking Mantra** and organizes the (then-exploding) zoo of infovis prototypes into a **task by data type taxonomy (TTT)**: seven data types crossed with seven tasks.

**AI summary:** Shneiderman opens by arguing that information exploration "should be a joyous experience," and that visual displays exploit under-used human perceptual abilities — scanning, recognizing, and detecting changes in size, color, shape, movement, or texture. His organizing principle is the mantra: **"Overview first, zoom and filter, then details-on-demand"** — printed ten times in a row in the paper, with the explanation that each line represents a project in which he found himself rediscovering the principle. He is explicit that the mantra is "only a starting point."

The core contribution is the taxonomy. He assumes users view **collections of items with multiple attributes**, and proposes seven **data types** — **1-dimensional** (linear: text, source code, lists), **2-dimensional** (maps, floorplans), **3-dimensional** (real-world objects), **temporal** (items with start and finish times that may overlap — deliberately separated from 1-D), **multi-dimensional** (relational/statistical data as points in n-space), **tree** (hierarchies), and **network** (arbitrary links). Crossed with these are seven **tasks**: **overview, zoom, filter, details-on-demand, relate, history, extract**. Each data type gets a paragraph on characteristic user problems (e.g., adjacency and paths for 2-D; parent/child/sibling relationships for trees) plus a tour of period systems (treemaps, cone trees, hyperbolic trees, starfield displays/FilmFinder, LifeLines, parallel coordinates).

The task discussion doubles as a critique of the field circa 1996: overviews should support zoom factors of 3–30; filtering should update displays in under 100 ms (dynamic queries); details-on-demand is usually a pop-up; and *history* and *extract* are called out as tasks that "most prototypes fail to deal with." A final section on advanced filtering describes the filter-flow metaphor for graphical Boolean queries, with usability-study evidence. The summary predicts that successful commercial products will need to handle several data types and the full task list — a prediction that reads well in hindsight (Spotfire, descended from FilmFinder, is cited in the paper itself).

**What a student/VisSnacks reader should get out of it:**
- The mantra, verbatim, and — just as important — Shneiderman's own framing of it as a *starting point*, not a complete design theory.
- The idea of abstracting tasks and data types separately, so a technique built for one dataset can be recognized as applicable to another. This is the seed of "abstraction as a building block."
- The seven tasks as a vocabulary for *interaction-level* activity — note these are things a user does with an interface (zoom, filter, extract), not analytic questions. Contrast with Amar et al.
- The observation that a taxonomy "is useful only if it facilitates discussion and leads to useful discoveries" — a good standard for judging any scheme in this module.
- A sense of the 1996 landscape: treemaps, dynamic queries, fisheye views, starfields — many of which survived.

**Skim/skip guidance:** Read carefully: the abstract, Section 2 (the mantra), the framing paragraphs of Section 3, and the per-task discussion (especially the neglected *history* and *extract*). Skim the per-data-type example inventories (a tour of 1990s systems, useful mostly as historical color). Section 4 (advanced filtering / filter-flow Boolean queries) can be skipped for this module's purposes — it's a separate research thread.

**Memorable specifics:**
- The mantra: **"Overview first, zoom and filter, then details-on-demand"** — repeated ten times, each line "one project in which I found myself rediscovering this principle."
- Seven data types: **1-D, 2-D, 3-D, temporal, multi-dimensional, tree, network**.
- Seven tasks: **Overview, Zoom, Filter, Details-on-demand, Relate, History, Extract**.
- "Information exploration should be a joyous experience."
- Concrete engineering numbers: <100 ms filter feedback; overview zoom factors of 3–30; users take "10–20 minutes to accommodate to complex treemaps."
- Opens with a Gombrich (*Art and Illusion*) epigraph about needing "a developed system of schemata" to describe the visible world.

**Caveats:** The paper is often reduced to the mantra alone, and the mantra is often over-claimed as a universal design law — Shneiderman himself flags it as a starting point, and later literature has qualified it ("overview first" doesn't fit every scenario, monolithic large data, or search-first workflows). The "tasks" are interface actions, not analytic goals, so it doesn't tell you *what the user is trying to learn* — exactly the gap Amar et al. address. The system survey is thoroughly dated. Also, despite "task by data type taxonomy" in the title, the paper never actually presents the crossed matrix as a filled-in table — it's two lists plus discussion.
