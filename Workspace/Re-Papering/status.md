# Re-Papering Summaries: Status and Resume Plan

**Also on disk (don't re-extract):** `_lecture_experiment/extracted/` has full slide text for 04-M and 03-W plus titles/key-slides for all other week 1–7 decks; `Workspace/Tools/` has the extraction scripts (python-pptx, tracked).

Updated 2026-08-22. This file lets a future session resume without rediscovery.

**Per-document status now lives in `checklist.md`** — one line per reading, checkbox state (`[ ]` nothing / `[/]` summary / `[!]` drafted / `[x]` published). Keep that file current as documents move through the pipeline; don't duplicate its contents here.

**Two different things get called "done" in this project — keep them separate:**

- an **AI reading summary** (the raw "here's what an AI said about it" material, format spec at the top of `ai-summaries.md`) being finished, vs.
- an actual **re-papering post** (a page under `content/`, Mike's voice + the AI summary) being written.

`checklist.md`'s `[!]`/`[x]` rows are the second kind; `[/]` rows are the first. The only post currently in progress (`[!]`) is the Problem Space paper — `content/papers/problem-space/index.md` (draft:true), started from the Gleicher et al. summary but explicitly not finished (see `content/papers/problem-space/todo.md`: "Finish the Problem space re-papering"). Also unresolved there: whether to write the rant page (`content/rants/repapering/index.md`, draft:true) and link it to the papers before or after the first real re-papering goes up.

## Summary needed

Nothing currently queued. The statistics pair (Shmueli; Leek & Peng; Zgraggen et al.) was summarized 2026-08-22 from local PDFs Mike placed in `_lecture_experiment/26Readings/`. The remaining Tufte chapters (VDQI ch. 2, EI ch. 3 & 5, VE ch. 2, Beautiful Evidence ch. 5 & 6, the PowerPoint essay) and all 10 chapters of Ware's *Visual Thinking for Information Design* were also summarized that same day — see `BookSummaries/tufte-*.md` and `BookSummaries/ware-*.md`.

**Possible future batch (not requested yet, lower priority — used in Modules 5+):**

- Possible: averages/visual-proxies papers, scagnostics, embedding-guidance papers — surfaced by `lecture-mining-plan.md`; verify which are actually needed before spending an agent on them.

## Process rules (carry forward to any future summarizing batch)

Lessons from a burned allocation (a Module-4 agent spent 22 tool calls in a retry spiral on a dead URL, producing nothing):

1. **Use a cheaper model for summarizing.** Launch summary agents with `model: sonnet` — faithful summarization to the fixed format doesn't need the strong model. Reserve the strong model for voice-drafting and judgment work.
2. **Hard fetch-failure policy in every agent prompt:** try each URL at most twice; if it fails, SKIP the document and say so in the report. No mirror-hunting, no Wayback, no extractor services unless an alternate URL was explicitly provided.
3. **Eliminate web flakiness up front:** best of all, Mike drops the web-paper PDFs into a local folder first (this is how the Shmueli/Leek & Peng/Zgraggen statistics pair got done — placed in `_lecture_experiment/26Readings/`) so agents only read local files.
4. **One file per document, written directly — no scratch file.** Each summary is its own file: a paper/post goes in `PapersSummary/`, a book chapter in `BookSummaries/` (or `BookSummaries/other/` for a book we only have one chapter of) — see each directory's `README.md` for the naming convention (`author-year.md` / `author-book-chNN.md`) and pick the next name by pattern-matching the existing files. Write the finished summary straight to its real file the moment it's done, before starting the next document, so a cutoff loses at most one document, not the batch. Then flip its row in `checklist.md` from `[ ]` to `[/]`.
5. **Run a summarizing batch from a fresh session** that reads only this file — an old session's context is enormous, and every tool call reprocesses all of it.

## File layout (for orientation)

Re-papering lives in `Workspace/Re-Papering/` (this directory) and **is git-tracked**.

- `checklist.md` — the per-document status tracker; check here first for what's done and what isn't.
- `ai-summaries.md` — index only, points into the two directories below.
- `PapersSummary/` — one file per paper/post (`author-year.md`); see `PapersSummary/README.md`.
- `BookSummaries/` — one file per chapter (`author-book-chNN.md`), plus a `BookSummaries/other/` for books we only have a single chapter for; see `BookSummaries/README.md`. (Restructured 2026-08-28 from six monolithic `summaries-*.md` files, one `##` heading per reading, into one file per document — the papers file alone had grown to 451 lines / 15 readings.)
- `queue.md` (repo root) — the page backlog; its "Re-paperings" section should track `checklist.md` (it currently still lists everything as unchecked, including readings that already have summaries ready).
- `content/papers/`, `content/rants/repapering/` — where the finished re-papering posts go.

### Why this moved here (2026-08-15)

These files used to live in `_lecture_experiment/`, which is **gitignored** — so none of this work was under version control. That was never a deliberate choice: the ignore rule (`.gitignore`, commit c2bf43a, 2026-07-17) was added to keep ~2 GB of copyrighted course material (`Lectures 25/`, `CS765-25 Readings/`) out of the repo, and these summaries — written the *next* day — were simply born into an already-ignored directory and inherited the ignore.

Re-papering and the lecture-to-tutorial experiment are **related but different projects**: the lecture experiment is a bounded experiment (turn 2025 lectures into snack tutorials), while re-papering is a standing editorial line of the site with its own section (`content/papers/`) and its own rant page. They overlapped only because both needed the same readings summarized.

Still in `_lecture_experiment/` (correctly — it's bulk course material and lecture-experiment-specific working files): the reading PDFs, lecture decks, `extracted/` deck text, and the lecture-mining plan. (The per-page **briefs** moved out to `Workspace/Briefs/` on 2026-08-22, for the same reason re-papering did — they're durable working notes, not bulk course material.)

**Caution:** this directory is under source control and the repo may some day be made public. The book-chapter digests in particular (all 14 Munzner chapters, 10 Cairo chapters, 10 Ware chapters, and 8 Tufte pieces) are detailed enough to warrant a second thought before publishing — and note that git history is permanent, so deleting them later does not remove them from a published repo.
