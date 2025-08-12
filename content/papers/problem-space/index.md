+++
title = 'A Problem Space for Designing Visualizations'
date = 2025-07-20T13:04:00-06:00
draft = true
+++

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