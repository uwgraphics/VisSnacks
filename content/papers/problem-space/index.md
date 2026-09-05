+++
title = 'A Problem Space for Designing Visualizations'
date = 2026-09-04T13:21:00-06:00
draft = false
+++

The "Problem Space" paper describes a way to think about the problem a visualization is trying to solve, rather than the solution. It proposes six aspects to consider, named for the "5Ws and an H" from journalism: Who, What, Where, Why, When, and How. 

<!--more-->

+ Michael Gleicher, Maria Riveiro, Tatiana von Landesberger, Oliver Deussen, Remco Chang and Christina Gillman. **A Problem Space for Designing Visualizations.** *IEEE Computer Graphics and Applications,* 43 (4), 111-120, July 2023. [https://doi.org/10.1109/MCG.2023.3267213](https://doi.org/10.1109/MCG.2023.3267213) [(UW Paper Page)](https://graphics.cs.wisc.edu/Papers/2023/GRVDCG23/).

This is my paper. The idea is valuable, although the paper may not be essential. Think about the **problem** that a visualization is trying to solve separately from the **solution** the visualization provides. To organize thinking about the problem, we suggest considering 6 aspects (or axes of the space of problems). 

Read the summary to get the main ideas. You might want to read the paper to see the examples, but these aren't essential. The AIs do a good job. I recommend reading the Claude summary, and then one of the NotebookLM summaries (these were done back when it was called NotebookLM - now it's called Gemini Notebook).

## From Claude (told to focus on class)

**What it is:** A viewpoint article proposing a **problem space** for visualization design: six axes — the journalistic **5 Ws and How** — for describing the *problem* a visualization must solve, deliberately kept independent of any solution.

**AI summary:** The core tenet, borrowed from design and product-development literature, is the **separation of problem from solution**: articulating needs independently of how they'll be met focuses work on the right problems, frees the search for solutions from preconceptions, and enables communication and checking. The authors even note that presuming the answer will be "a visualization" already conflates problem and solution — "it might be better to call this a problem space of data analysis and communication problems." The framework adapts Schulz et al.'s "Design Space of Visualization Tasks" (which also used the 5Ws+H) but shifts the focus from formalizing *task* to broadly characterizing *the problem*.

The six axes: **Who** has the problem (audience characteristics — expertise, motivation, spatial ability, accessibility — plus other stakeholders like developers and maintainers); **Why** do they need it (the goal — the axis that "most closely aligns with the common notion of task"); **What** is the data (form, but also semantics, scale, time-dependence); **When** in the analysis process (exploration vs. communication vs. justification suggest different designs); **Where** is the context (physical place, display, social setting, time pressure, stakes); and **How** do they expect to be helped — carefully defined as the users' *pre-conceived expectations* of a solution (design constraints or biases to acknowledge), not the solution itself. A useful practical trick appears under Why: asking "Why?" of an over-specific task description moves you up the abstraction ladder; asking "How?" moves you down — but risks smuggling the solution back in.

The framework is grounded in three worked use cases — **keyhole surgery planning** (the running example), **hospital infection-pathway tracing**, and **investigative-journalism document exploration** — each walked through axis by axis. A self-assessment section evaluates the space against Kerracher and Kennedy's criteria (relevant, independent, thorough, complete, orthogonal, precise), with honest concessions: the axes are "ultimately inter-twined or at least correlated," and precision was not a goal. A sidebar surveys the task-abstraction literature (Wehrend & Lewis through Brehmer & Munzner and Schulz et al.), positioning task as "one of many aspects that must be considered." The intended uses: a **checklist** for design, evaluation, and documentation, and a **vocabulary** for articulating problems consistently.

**What a student/VisSnacks reader should get out of it:**
- The six questions — Who, Why, What, When, Where, How — as a checklist you can actually run before designing anything.
- The module's headline point: **task (the Why) is just one axis of six**. Task abstraction, the subject of the other readings, characterizes the goal but not the audience, context, process phase, data realities, or user expectations.
- The discipline of separating problem from solution — and the specific trap that "How" names: users and designers arrive with preconceptions that should be surfaced as constraints or biases, not silently baked in.
- The "Why?/How?" laddering trick for finding the right level of task abstraction.
- Uncertainty *about* the problem specification (unknown users, unknown display) is itself design-relevant information, distinct from uncertainty *in* the data.

**Skim/skip guidance:** Read carefully: the introduction, Table 1, and the six axis sections (short, with the surgery example threaded through). The sidebar on task abstractions is an efficient map of this whole module's literature — worth careful reading as orientation. Skim the two additional use cases (they repeat the pattern) and the "Is the Problem Space Useful or Good?" self-evaluation, though note its candor about non-orthogonality.

**Memorable specifics:**
- Table 1, the six axes: **WHO** (who has the problem / will use it), **WHY** (objective), **WHAT** (data), **WHEN** (phase of analysis), **WHERE** (context), **HOW** (how they *expect* to be helped).
- The one-sentence version: "a visualization is intended to help someone (the who) do something (the why) with the data (the what) in some phase of the analysis process (the when) and in some context (the where) using some method (the how)."
- The Aristotle hook: the 5Ws trace back at least to Aristotle's rhetoric, who "argued that ignorance of any of these elements can lead to faulty reasoning."
- The three use-case figures: surgery-planning multi-view tool (Fig. 1), infection-tracing dashboard (Fig. 2), journalism document-exploration dashboard (Fig. 3).

**Caveats:** It's a viewpoint/position piece, not an empirical result — the framework is justified by the authors' design experience and post-hoc application to already-completed projects, which they acknowledge. The mapping onto the 5Ws is admitted to be "a little contrived," and the axes aren't truly orthogonal or precise (also admitted). It offers a checklist, not a method: it tells you what to consider, not how to get answers or convert them into a design. Readers sometimes expect a taxonomy with categories to fill in; deliberately, there isn't one.

## From NotebookLM focused on Class

When I asked NotebookLM to connect this paper to class, it went a little too far... but I think it is helpful...

> Provide a summary of the problem space paper that is at most one page that is targeted towards the students in the class described in the "what is this class and why" paper

For students in CS765 Data Visualization 2024, a class focused on the **principles and design of data visualization** rather than implementation, the "Problem Space for Designing Visualizations" paper offers a foundational conceptual tool. This class aims to teach you **"what pictures to make"** to understand data, emphasizing effective communication. The core idea of the problem space aligns perfectly with the class's philosophy: **"don't bother solving the wrong problem well"**.

The paper introduces a **"problem space"** as a way to think about the needs a visualization is meant to solve, **independently from the specific solution**. This crucial separation helps designers focus on solving the *correct* problems, encourages more creative solutions by not being limited by preconceived ideas, and improves communication about user needs. While the term "visualization" is used, the authors take a broad view, acknowledging that the best solution to a problem might not even involve a visualization at all; it's more accurately a **"problem space for data analysis and communication problems"**.

The problem space is structured around **six key aspects, or "axes,"** derived from the journalistic "5 Ws and How" framework (Who, Why, What, When, Where, How). These axes serve as a **checklist** and a **vocabulary** for you to consistently articulate problems, identify similar challenges, and assess how well a design addresses the stated needs.

Here’s how each axis guides your thinking in the context of effective visualization design:

*   **WHO: Who has the problem? Who will use the visualization?**
    *   This focuses on the **intended audience** or users. You'll consider their analytic sophistication, motivation, background knowledge, visual abilities, and accessibility needs. It also includes various stakeholders beyond the end-user, like developers, decision-makers, or even patients.
    *   *Example:* For keyhole surgery planning, the "who" is primarily the clinician (a medical expert). This understanding led to a system using familiar multi-views that resonated with their existing knowledge.

*   **WHY: Why do they need a visualization? What is the objective?**
    *   This is the **goal or purpose**—"what the viewer is trying to do with the data". It most closely aligns with the concept of "task" in visualization literature, but unlike some definitions, it is kept separate from other aspects. Asking "Why?" can help you generalize an overly specific problem statement, ensuring you're addressing the fundamental need.
    *   *Example:* The "why" for keyhole surgery planning is to **determine the safest and most suitable surgery path**, minimizing damage to healthy tissue while reaching a tumor.

*   **WHAT: What is the data?**
    *   This axis considers the **data itself**, from low-level details (like data type) to higher-level characteristics such as its semantics, distribution, value ranges, and relationships. Factors like data quantity or time-dependence also influence design.
    *   *Example:* In keyhole surgery, the "what" is a Computed Tomography (CT) scan of the patient's head, the known tumor location, and potential surgery paths.

*   **WHEN: When in the analysis will they use the visualization?**
    *   This acknowledges that data analysis is often an **iterative process** (e.g., gathering, defining, analyzing, communicating). Understanding *when* in this process the visualization will be used impacts design choices; for instance, initial data exploration might require different views than communicating final findings.
    *   *Example:* The keyhole surgery visualization is specifically used **before the surgery** for planning and exploration.

*   **WHERE: Where will they use the visualization? What is the context?**
    *   This covers the **context** of use, including the physical location (e.g., office vs. on a bus), the user's focus, the social environment (e.g., solitary vs. collaborative), the display type (e.g., large monitor vs. cell phone), and the computing environment. It also includes the scenario (e.g., business decision, scientific evaluation) and pressures like time or the need for justification.
    *   *Example:* Keyhole surgery planning happens on a **computer in a surgeon's office** during a dedicated planning session, acknowledging factors like clinical context, data privacy, and potentially older hardware.

*   **HOW: How do they expect to be helped?**
    *   This is unique: it focuses on the user's **expectations or pre-conceived notions of a solution**, rather than the ultimate solution itself. These expectations can act as design constraints or biases that you, as a designer, need to acknowledge. This helps avoid solving a problem in a way that, while technically sound, goes against how the user *expects* to interact with the solution.
    *   *Example:* For keyhole surgery, the design combined views already familiar to physicians (like CT scans) with new displays, leveraging existing mental models while introducing novel elements.

The problem space is considered **relevant** (each axis makes a meaningful distinction), **independent** of solutions, aiming for **thoroughness** and **completeness** (any data problem will involve these aspects), and striving for **orthogonality** (aspects are largely independent, though some correlation exists). While it doesn't provide formalisms for precision, it guides designers to consider the full range of possibilities for each axis.

In this class, you won't bring your own data or spend time learning specific tools, because the goal is to equip you with the **principles needed to design solutions for problems in the future**. This problem space framework provides those foundational skills, akin to a doctor learning to diagnose symptoms based on fundamental understanding before prescribing a treatment. By thoroughly understanding the "who, why, what, when, where, and how" of a problem, you'll be able to make informed "prescriptions" for effective visualizations, whether it's "two scatterplots" or a more complex design.

Think of the problem space as your **diagnostic toolkit** in visualization design. Just as a physician needs to thoroughly understand a patient's symptoms (who, what, why, when, where, and how they feel) before prescribing a treatment, you, as a visualization designer, must thoroughly understand the facets of a data problem before you can design an effective visualization.

## From NotebookLM

> Summarize the selected paper (the "problem space" paper)

The "Problem Space for Designing Visualizations" paper introduces a **conceptual tool called a "problem space"** for thinking about the needs a visualization is meant to solve, independently from the specific solution. This approach separates the problem to be addressed (the needs) from the solution that will address it, which proponents argue helps in focusing on correct problems, fostering creative solutions, and improving communication about needs. The authors view "visualization" broadly, acknowledging that the ideal solution might not even require a visualization at all, and suggest it could be considered a problem space for data analysis and communication problems.

The core of this problem space is defined by **six aspects or "axes"**, which are based on the journalistic "5 Ws and How" framework (Who, Why, What, When, Where, How). These axes serve as a checklist and vocabulary for designers to articulate problems consistently, identify similar problems and solutions, and assess how a design considers the stated needs.

Here's a breakdown of the six axes:

*   **WHO**
    *   **Focus**: The **intended audience or users** of the visualization, the people who have a need to see something in the data.
    *   **Considerations**: User's analytic sophistication, motivation, spatial reasoning abilities, background knowledge, visual acuity, and accessibility (e.g., color vision deficiency).
    *   **Stakeholders**: Also includes other stakeholders beyond the ultimate users, such as developers, maintainers, analysts, decision-makers, writers, and readers.
    *   **Example**: In keyhole surgery planning, the "who" includes the clinician (medical expert) and potentially the patient. This led to a multi-view system familiar to clinicians. For infection tracing, users are infection control experts who expect familiar views like line charts and patient timelines. Journalists, working under time pressure and unwilling to learn complex new tools, were supported by popular dashboard designs and interactive filters.

*   **WHY**
    *   **Focus**: The **goal or objective** of the visualization, "what the viewer is trying to do with the data".
    *   **Alignment**: This aspect most closely aligns with the common notion of "task" in visualization literature, differentiating it from other factors often conflated with "task". It aims to focus on the problem without presupposing a solution.
    *   **Abstraction levels**: The "Why?" question can help generalize a too-specific description, while "How?" can refine an overly general goal.
    *   **Example**: For keyhole surgery, the "why" is to **determine the safest and most suitable surgery path** by minimizing damage to healthy tissue while reaching the tumor. For infection tracing, goals include detecting outbreaks, identifying pathways and locations, quantifying duration, and identifying potentially infected patients. Journalists aim to identify newsworthy information in large document sets.

*   **WHAT**
    *   **Focus**: The **data** that is being worked with.
    *   **Impact**: Data characteristics influence solutions at various levels, including low-level details (type/form) and higher-level factors like semantics, distribution, value ranges, and relationships.
    *   **Issues**: Quantity (e.g., very large datasets) and time-dependence can influence design. Data may also be transformed or thought of in different ways during analysis.
    *   **Example**: For keyhole surgery, the "what" is a Computed Tomography (CT) scan of the patient's head, tumor location, and potential surgery paths. Infection tracing involved complex and large datasets of patient locations and infection statuses over time, leading to a focus on single patients and their contacts. Journalists work with millions of documents from which named entities and relationships are extracted.

*   **WHEN**
    *   **Focus**: The **phase in the analysis process** when the visualization will be used.
    *   **Process**: Data work is an iterative process that can include gathering information, defining questions, analysis, drawing conclusions, communication, or justification.
    *   **Design implications**: Different phases suggest different design choices; e.g., initial data examination might favor overview and exploration, while communicating findings later in the process might require different designs.
    *   **Example**: The keyhole surgery visualization is used **before the surgery** for planning and exploration. Infection tracing is for retrospective analysis after a hypothesis about an outbreak, occurring in the analytical phase before reporting or taking measures. Journalistic exploration happens in the **early phase of investigation** to identify interesting facts.

*   **WHERE**
    *   **Focus**: The **context** in which the problem occurs.
    *   **Elements**: This includes the literal place (e.g., lab vs. bus), user's activity (focused attention?), social environment (sharing?), display (large monitor vs. cell phone), computing environment (available computation), and the visualization's placement (newspaper, stand-alone system).
    *   **Scenario**: Also considers the scenario (e.g., business decision, scientific evaluation), time available, pressure, and need to justify choices.
    *   **Example**: The keyhole surgery planning occurs **in a surgeon's office** on a computer during a dedicated planning session, considering clinical context, data privacy, and older hardware. Infection control experts also use standard desktop PCs in their office. Journalists similarly work in an office setting with standard hardware.

*   **HOW**
    *   **Focus**: The user's **expectations of a solution** or pre-conceived notions of how the problem should be addressed, rather than the ultimate solution itself.
    *   **Separation**: The problem space aims to separate "how" from other aspects defining the problem, but acknowledges that expectations can act as design constraints or biases.
    *   **Example**: In keyhole surgery, the design combined views familiar to physicians (CT scans) with novel displays, addressing expectations while introducing new elements. Infection control experts expected specific line-charts and patient timelines, which were integrated into the design. Journalists expected to be able to closely read articles, meaning summary views alone were insufficient.

The authors built this problem space based on their experience and motivate it from work by Schulz et al. and Rind et al., distinguishing their broader focus on the problem from existing task abstractions. They highlight that Aristotle's rhetoric, specifically the "5Ws and H," has historical roots in organizing key information, and this advice applies to visualization designers as well.

The paper asserts that the problem space is a useful conceptual tool for design, analysis, organization, and evaluation of visualizations. It can serve as a **checklist** to ensure all relevant aspects are considered during design and evaluation, helping to articulate problems independently of solutions. The authors discuss properties like relevance, independence, thoroughness, completeness, orthogonality, and precision, acknowledging that while they aimed for these, some aspects like orthogonality can be intertwined in practice. Uncertainty in problem specification (e.g., unknown users) is also addressed, suggesting it can either prompt clarification or influence inclusive design choices.

In essence, the problem space acts like a **compass for visualization designers**, guiding them to thoroughly understand the landscape of a problem (who, why, what, when, where, how) before embarking on the journey of creating a solution. Just as a navigator studies a map to understand the terrain, destination, obstacles, and conditions, a designer uses this problem space to map out the user's needs and context, ensuring the eventual design effectively addresses the true problem.

{{<genai>}}
The AI generated summaries were generated by the AI tools I credited. The tools had a lot of context about my class and philosophy for teaching visualization.
{{</genai>}}