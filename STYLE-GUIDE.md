# VisSnacks Style Guide (for agent-drafted pages)

This file is for agents (and humans) drafting pages for this site. It is not site content — Hugo only publishes `content/`, so this stays out of the build.

## What this site is

VisSnacks provides visualization knowledge in small, easily accessible pieces — for students in Mike's class (CS765) and for anyone who wants help with Vis but won't take a class or read a textbook. The site's job is **connective tissue**: Mike's framing, his examples, his "why this matters" voice. It is *not* to re-derive or summarize textbooks and papers — those stay external and get pointed to. If a draft starts reading like a chapter summary, it has drifted from the site's role.

The whole site is "snacks" in spirit: **prefer short and punchy**. Get the main idea across quickly; details and background come after, or go in a collapsible aside. "The why follows the what."

## Voice

Write as Mike: first person, conversational, direct address to the reader. Calibrate against real pages before drafting — the best single reference for voice is `content/tutorials/4-critique/index.md`; for the compact snack form, `content/snacks/cairo-discrete-line/index.md`.

Traits to hit:

- **Lessons, not rules.** Mike is anti-dogmatic: "I hesitate to give 'rules,' especially in terms of chart types." Guidance is framed as principles with reasons, and rules come with the reasoning that lets you know when to break them.
- **Task-first framing.** Design choices are evaluated against the viewer's task, not chart-type convention. "The decision should really consider task, not just data type."
- **Opinions owned as opinions.** He states preferences freely but flags them: "Notice I didn't say it was the best, I said it was my favorite." "I can't be objective on this one. I like this paper!"
- **Honest hedging.** "(this is speculation...)", "with caution", "I am not sure the scales are the same." Uncertainty is stated, not hidden.
- **Parenthetical asides**, often wry or self-deprecating: "(yes, water heaters have apps nowadays)", "(OK, having great students is a not-so-secret weapon)".
- **The reader participates.** Rhetorical questions, "Try this yourself," "I'll bet without much effort you can figure out what it is showing you."
- **Personal and concrete.** Real examples from his life, class, and research — a student's question, his broken water heater, a map he wants for his wall.
- **Bold key terms** on first definition: "**Critique** is the practice of..."
- Conversational fragments are fine. "Yuck." Sentences can start with And, But, So.

### What agents must NOT do

- **Never fabricate Mike's experiences, anecdotes, opinions, or preferences.** The personal voice comes from real material (source decks, notes, conversation). If a spot wants an anecdote or opinion you don't have, leave a clearly marked placeholder: `[MIKE: personal example here?]`.
- **Never invent citations, dates, attributions, or study findings.** Flag gaps instead of filling them confidently.
- No AI-prose tells: no "delve," "crucial," "it's important to note," breathless enthusiasm, or marketing tone. No bullet-point-itis — Mike writes in prose and uses lists only to enumerate actual lists (advice, reasons, steps).
- Don't over-structure. Short pages often need no headers at all. Headers appear when a page genuinely has parts.
- Don't formalize the informality. This is intentionally not academic writing (see `content/rants/repapering/index.md` for why).

## Page anatomy

Every page opens with a **teaser**: 1–3 sentences giving the main point, then `<!--more-->`, then the body. The teaser should stand alone — it's what shows in listings, and it's the "what" that the "why" follows. Good example (cairo-discrete-line): "Line charts can be used (with caution) even when the X axis is neither interval or continuous."

After the teaser, typical flow: the concrete example or hook → the examination/reasoning → connection to principles → takeaway. Many pages end with an explicit lesson ("The Takeaways", "The Actual Lesson").

Optional depth goes in `expand` / `expand-boxed` collapsibles (e.g., statistics details, library-access instructions) so the main flow stays short.

Cross-link generously to other pages with `{{< link >}}` — connecting ideas across the site is part of the job.

## Section types

All sections share the voice; they differ in form.

**Sections are deliberately few, because folders are expensive** (they set URLs, and outside pages link to them) **while front matter is free.** So *length and reader-intent* decide the section; everything else — is it a critique? is it about encodings? — is a tag. Restructured 2026-08-22; don't add a section without a strong reason.

- **Snacks** (`content/snacks/`) — the core stylized form: one idea, quick consumption, main message in the teaser, background after. Shortest. This is the site's default home for a lesson, and it holds several *kinds* of lesson (see tags below).
- **Tutorials** (`content/tutorials/`) — longer written "documents." Two groups in one collection: the **core sequence** (`1-what-is-vis` … `4-critique`, `weight` 1–4) which teaches *how to think* about visualization and is meant to be read in order; and an unordered **tail** (`weight` 30+) of deeper single-topic pages — the de-lectured class material — which teach *what to know* and build on the core. Tableau class-support pages sit between them (`weight` 10–20). Don't put sequence numbers in *titles* of tail pages; ordering lives in `weight`.
- **Papers** (`content/papers/`) — "I read it so you don't have to": informal summaries/discussions of papers, often Mike's own, with the story the paper couldn't tell. Include full citations with (web) and (doi) links. Kept separate because it answers a different question ("what should I read") rather than "teach me something."
- **Resources** (`content/resources/`) — descriptions of books and other helpful things, with honest assessments ("Is the book perfect? Not by a long shot.") and practical access notes.
- **Rants** (`content/rants/`) — opinionated essays. Most opinion-forward; still constructive.

**Kinds are tags, not sections.** A page can be several at once, which is exactly why they aren't folders:

- `critique` — close examination of a specific visualization *to learn from it* (not just criticize). Lives in `content/snacks/`, folder date-prefixed `YYMMDD-short-name/`. Use the stylized critique form from Tutorial 4: "If **objective** then **decision** could be informed by **principle**." The tag's landing page is hand-authored at `content/tags/critique/_index.md`, and "Critiques" keeps its top-nav slot pointing there.
- `with-data` — the data is provided so readers can re-design it themselves.
- Topic tags (`encodings`, `data-abstraction`, `building-blocks`, …) are how a reader finds everything on a subject across sections.

To hand-author a tag's landing page, add `content/tags/<tag>/_index.md` (see `critique` and `books` for the pattern). `{{<link "/tags/critique">}}` resolves — the `link` shortcode handles taxonomy term pages.

**Lecture-replacement pages** (the tutorials tail, drawn from a CS765 lecture *and* its readings) differ from other pages in one way: they **lean self-sufficient**. Students aren't expected to do the other readings, so the page carries the key content itself, with readings as "want more" pointers. Still snack-spirit: brief, key points first.

**Sidebars and sub-snacks.** When a page wants a multi-paragraph digression, three options in order of preference: (1) if the digression stands alone, make it its own short snack and replace it in the main page with one sentence of the key idea plus a link ("for more, see..."); (2) if it doesn't stand alone, put it in an `expand` box (a style cheat Mike uses a lot); (3) leave it inline only if it's short. Use the spin-off-snack move sparingly — links break flow — but remember the multi-paragraph digression breaks flow too.

## Mechanics

**Page bundles.** Each page is a folder with `index.md` plus its images: `content/<section>/<slug>/index.md`.

**Front matter** is TOML (`+++`). A few older pages use YAML; use TOML for new pages. Fields:

```toml
+++
title = 'Phone App Time Graphs'
date = 2024-09-09T13:10:36-05:00   # real timestamp; hugo new generates it
draft = true                        # agent drafts: always true
tags = []                           # underused sitewide, but populate sensibly
resourcethumb = "some-image.png"    # image in the bundle, used as listing thumbnail
weight = 5                          # numbered tutorials only
+++
```

**Shortcodes** actually in use (theme: `themes/559Theme/layouts/_shortcodes/`, plus site-local `layouts/shortcodes/`):

- `rimage` — page-bundle image with click-to-zoom. Args: `src`, `caption`, `attr` (credit), `attrlink`, `width`. Images always get caption + attribution.
- `quote` — attributed block quote: `{{< quote "Discussing Design, p. xi" >}}...{{< /quote >}}`
- `expand` / `expand-boxed` — collapsible asides: `{{< expand "Yes, we did the statistics..." >}}...{{< /expand >}}`
- `link` — internal cross-reference by page name or path: `{{< link "/tags/critique" >}}`, `{{< link "/tutorials/4-critique" >}}`
- `anchorlink` — link to a heading on the same page.
- `tooltip` — hover footnote: `{{< tooltip element="(I believe)" >}}...text...{{< /tooltip >}}`
- `genai` — AI-disclosure box at the end of a page (see below).
- `dimbox` — dimmed callout box (`{{% dimbox %}}` paired form).
- `comment` — content hidden from output.
- `lesson` (site-local) — numbered principle callout: `{{< lesson 1 "Tasks are important for design decisions." "Task first" >}}`
- `visclass` (site-local) — inline reference to Mike's class.

Image credit matters: everything not made by Mike gets `attr`/`attrlink`, and questionable use gets acknowledged (see the About page's copyright stance).

## Workflow rules for agent drafts

1. **Always `draft = true`.** Mike flips it when it's ready.
2. **Leave changes uncommitted** so Mike can review the diff before deciding to keep them. Don't touch or restructure other existing pages.
3. **End every draft session with a verification list**: specific claims, attributions, dates, named studies, and placeholder-marked spots that Mike should check rather than trust. Put it in the chat/report, not in the page.
4. **Disclose AI involvement with `{{< genai >}}`** at the bottom of the page, describing what the AI actually did (e.g., "Claude drafted this page from Mike's 2025 lecture deck; Mike edited."). Match the pattern at the end of `content/tutorials/4-critique/index.md`.
5. `queue.md` at the repo root tracks the writing backlog; worth a glance for context on what's planned.

## More commentary from Mike (not Claude)

- prefer pictures and examples; use visualization to teach visualization
- encourage the reader to "see it themself" in a visualization
  