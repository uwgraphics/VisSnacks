# Re-Papering Summaries: Status and Resume Plan

**Also on disk (don't re-extract):** `_lecture_experiment/extracted/` has full slide text for 04-M and 03-W plus titles/key-slides for all other week 1–7 decks; `Workspace/Tools/` has the extraction scripts (python-pptx, tracked).

Updated 2026-08-15. This file lets a future session resume without rediscovery.

**Two different things get called "done" in this project — keep them separate:**

- an **AI reading summary** (the raw "here's what an AI said about it" material, format spec at the top of `ai-summaries.md`) being finished, vs.
- an actual **re-papering post** (a page under `content/`, Mike's voice + the AI summary) being written.

Having the summary does not mean the post exists. The three sections below reflect that distinction.

## 1. Repapering complete (post written)

None yet. The only post in progress is the Problem Space paper — `content/papers/problem-space/index.md` (draft:true), started from the Gleicher et al. summary but explicitly not finished (see `content/papers/problem-space/todo.md`: "Finish the Problem space re-papering"). Also unresolved there: whether to write the rant page (`content/rants/repapering/index.md`, draft:true) and link it to the papers before or after the first real re-papering goes up.

## 2. Summary complete (ready to write post)

35 readings have a finished AI summary and just need Mike's-voice drafting.

**Munzner, *Visualization Analysis and Design*** — all 14 chapters, in `summaries-munzner.md`:
ch. 1 (What's Vis), 2 (Data Abstraction), 3 (Task Abstraction), 4 (Four Levels for Validation), 5 (Marks and Channels), 6 (Rules of Thumb), 7 (Arrange Tables), 8 (Arrange Spatial Data), 9 (Arrange Networks and Trees), 10 (Map Color and Other Channels), 11 (Manipulate View), 12 (Facet into Multiple Views), 13 (Reduce Items and Attributes), 14 (Embed: Focus+Context). Chapters 4, 6, 8–14 also have a "Figures worth borrowing" field.

**Cairo** — all 10 chapters covered so far, in `summaries-cairo.md`:
*The Functional Art*: Preface+ch. 1 (Why Visualize), ch. 2 (Forms and Functions), ch. 3 (The Beauty Paradox), ch. 4 (The Complexity Challenge), ch. 5 (The Eye and the Visual Brain), ch. 6 (Visualizing for the Mind).
*The Truthful Art*: Introduction (Island of Knowledge), ch. 1 (What We Talk About When We Talk About Visualization), ch. 2 (The Five Qualities of Great Visualizations), ch. 5 (Basic Principles of Visualization).

**Papers & posts**, in `summaries-papers.md`:
Cleveland & McGill 1984 (JASA), Cleveland & McGill 1985 (Science), Shneiderman 1996 (The Eyes Have It), Amar/Eagan/Stasko 2005 (Low-Level Components), Gleicher et al. 2023 (Problem Space — post already started, see §1), Mackinlay 1986, Bertini 2022 (Beyond Precision — flagged as maybe-a-resource-page rather than a re-papering), North 2006 (Toward Measuring Visualization Insight), Rind et al. 2016 (Task Cube — not from the original 15-reading batch; added 2026-08-15 from a directly-supplied local PDF, not yet cross-checked against the course reading list).

**Other books**, in `summaries-books-other.md`:
Tufte, *VDQI* ch. 1 (Graphical Excellence); Wexler/Shaffer/Cotgreave, *Data Visualization: A Primer* (*Big Book of Dashboards* ch. 1).

## 3. Summary needed

**Module 4 paper, local PDF ready:**

- Card, Mackinlay & Shneiderman, intro chapter (*Readings in Information Visualization*, ch. 1) — `CS765-25 Readings/Other Vis Books/InfoVis-CardMackinlaySchneid-Chap1.pdf` (first 17 pages required; "How Visualization Amplifies Cognition" + Table 1.3 flagged as particularly important). A prior agent got cut off with this file loaded in context but produced no summary — the PDF is ready, just needs a fresh agent to actually read and summarize it.

**Statistics pair** (readings not yet fetched locally — no local PDF found in `CS765-25 Readings/`):

- Shmueli, "To Explain or to Predict?" (*Statistical Science* 2010) — [projecteuclid.org link](https://projecteuclid.org/journals/statistical-science/volume-25/issue-3/To-Explain-or-to-Predict/10.1214/10-STS330.full). Instruct the agent to extract the conceptual message (explanation vs. prediction, why the distinction changes practice), not the statistics.
- Leek & Peng, "What is the question?" (*Science* 2015) — [aaas.org PDF](https://www.aaas.org/sites/default/files/Stats_What_Question_2015.pdf) (unverified link, untried).
- Zgraggen et al., "Multiple Comparisons Problem in Visual Analysis" (CHI 2018) — [dspace.mit.edu link](https://dspace.mit.edu/handle/1721.1/137892) — optional add-on, first half only (skip the experiment section).

**Possible future batch (not requested yet, lower priority — used in Modules 5+):**

- Remaining Tufte chapters, all local in `CS765-25 Readings/Tufte - Book Chapters/`: VDQI ch. 2 (Graphical Integrity), EI ch. 3 (Layering & Separation), EI ch. 5 (Color and Information), VE ch. 2 (Visual & Statistical Thinking), BeautEvid ch. 5 (Fundamental Principles), BeautEvid ch. 6 (Corruption), PowerPoint chapter.
- Ware, *Visual Thinking for Information Design*, all local in `CS765-25 Readings/Ware - Visual Thinking.../`: ware01–ware10 (ware11 is just the index).
- Possible: averages/visual-proxies papers, scagnostics, embedding-guidance papers — surfaced by `lecture-mining-plan.md`; verify which are actually needed before spending an agent on them.

## Process rules (carry forward to any future summarizing batch)

Lessons from a burned allocation (a Module-4 agent spent 22 tool calls in a retry spiral on a dead URL, producing nothing):

1. **Use a cheaper model for summarizing.** Launch summary agents with `model: sonnet` — faithful summarization to the fixed format doesn't need the strong model. Reserve the strong model for voice-drafting and judgment work.
2. **Hard fetch-failure policy in every agent prompt:** try each URL at most twice; if it fails, SKIP the document and say so in the report. No mirror-hunting, no Wayback, no extractor services unless an alternate URL was explicitly provided.
3. **Eliminate web flakiness up front:** best of all, Mike drops the web-paper PDFs into `CS765-25 Readings/Old Papers/` (Shmueli, Leek & Peng, Zgraggen still need this) so agents only read local files.
4. **Agents save as they go:** each agent appends every finished summary to a scratch file before starting the next document, so a cutoff loses at most one document, not the batch.
5. **Run a summarizing batch from a fresh session** that reads only this file — an old session's context is enormous, and every tool call reprocesses all of it.

## File layout (for orientation)

Re-papering lives in `Workspace/Re-Papering/` (this directory) and **is git-tracked**.

- `ai-summaries.md` — index only, points to the four per-source files below.
- `summaries-munzner.md`, `summaries-cairo.md`, `summaries-papers.md`, `summaries-books-other.md` — the actual summaries, one `##` heading per reading.
- `queue.md` (repo root) — the page backlog; its "Re-paperings" section should track §1/§2 above (it currently still lists everything as unchecked, including readings that already have summaries ready).
- `content/papers/`, `content/rants/repapering/` — where the finished re-papering posts go (see §1).

### Why this moved here (2026-08-15)

These files used to live in `_lecture_experiment/`, which is **gitignored** — so none of this work was under version control. That was never a deliberate choice: the ignore rule (`.gitignore`, commit c2bf43a, 2026-07-17) was added to keep ~2 GB of copyrighted course material (`Lectures 25/`, `CS765-25 Readings/`) out of the repo, and these summaries — written the *next* day — were simply born into an already-ignored directory and inherited the ignore.

Re-papering and the lecture-to-tutorial experiment are **related but different projects**: the lecture experiment is a bounded experiment (turn 2025 lectures into snack tutorials), while re-papering is a standing editorial line of the site with its own section (`content/papers/`) and its own rant page. They overlapped only because both needed the same readings summarized.

Still in `_lecture_experiment/` (correctly — it's bulk course material and lecture-experiment-specific working files): the reading PDFs, lecture decks, `extracted/` deck text, briefs, and the lecture-mining plan.

**Caution:** this directory is under source control and the repo may some day be made public. The book-chapter digests in particular (all 14 Munzner chapters, 10 Cairo chapters) are detailed enough to warrant a second thought before publishing — and note that git history is permanent, so deleting them later does not remove them from a published repo.
