# Agent instructions for VisSnacks

Hugo site disseminating visualization knowledge (Mike Gleicher). Read `STYLE-GUIDE.md` before drafting or editing any page — it has voice, mechanics, and workflow rules (draft=true, leave uncommitted, verification list, genai disclosure).

Working material for the lecture-to-tutorial project lives in `_lecture_experiment/` (gitignored — it holds ~2 GB of copyrighted lecture decks and reading PDFs): plans and deck extractions (`extracted/`). Check `_lecture_experiment/0718-Summary.md` for project state before redoing work.

**Per-page briefs live in `Workspace/Briefs/` (git-tracked)** — see its README. They're named `NN-topic.md`, where `NN` is the source lecture's week, so the directory sorts in course order. A brief is the unit of work before drafting: an agent fills §1–4 from the decks and course pages, Mike fills §5–8 (stories, cut/keep, contested takes). Read the brief before drafting its page, and record answers back into it when Mike settles a question.

Working material for the **re-papering** project lives in `Workspace/Re-Papering/` (git-tracked): the AI reading summaries plus `status.md`, which is the resume file — read it before starting any summarizing or re-papering work. Re-papering is a separate, longer-lived project from the lecture experiment; the finished posts go in `content/papers/`.

`Workspace/` generally is the tracked home for notes and in-process work that isn't part of the Hugo site. Since the repo may become public, don't put anything there you wouldn't publish — git history is permanent.

`MODULE-DOCS-PLAN.md` (root) is the document plan; `queue.md` (root) is the page backlog.

## Efficiency rules (portable — copy to other project CLAUDE.md files, e.g. the course web)

1. **Match model to task.** Faithful summarization, extraction, and format-following: spawn subagents with `model: sonnet`. Reserve the strong model for judgment work (drafting in Mike's voice, planning, critique).
2. **Fetch-failure budget.** Try any URL at most twice. On failure: skip, and report the dead link so it can be fixed at the source (readings list, course page) — never silently hunt mirrors, Wayback, or extractor services unless an alternate URL was explicitly provided. A dead link is a bug to report, not an obstacle to route around.
3. **Save as you go.** Write each unit of work (a summary, a draft section, an extraction) to disk the moment it's done. Session limits hit without warning; work in context or in /tmp dies with the session.
4. **Bias toward visible files over hidden scratch.** Put intermediate work (extractions, staged inputs, reports) in the project's designated working directory, not /tmp or the session scratchpad. Tradeoff: truly disposable junk (one-off scripts mid-debug, downloaded archives) may start in /tmp, but promote anything with reuse value immediately. Pick the directory by *how long the work should live*: durable notes and anything feeding a site page go in `Workspace/` (tracked); lecture-experiment scratch and anything derived from the bulk course material go in `_lecture_experiment/` (ignored). When in doubt, prefer tracked — an ignored directory silently means "one `rm -rf` from gone, no history."
5. **Stage inputs before spawning agents.** Give subagents exact file paths to pre-staged local inputs and a closed reading list; forbid wandering. Have them write outputs to named files, not just their final message.
6. **Fresh sessions for batch work.** Long sessions reprocess their whole context on every call. When a batch is planned, write the plan to a file and run it from a new session whose only instruction is "resume per <file>".
7. **Long-running batches: split across agents, run in parallel, one topic-cluster each** — a failure then costs one cluster, not the batch.
8. **Hugo shortcode spacing.** Write `{{<foo ...>}}` / `{{%foo ...%}}` — no space touching the opening `{{<`/`{{%` or the closing `>}}`/`%}}`. (Space between the shortcode name and its args is normal and expected.) Semantically identical to the spaced form, but the no-space form gets correct syntax highlighting in VSCode. Check with `hugo-shortcode-spacing` (in `~/bin`; bare invocation reports violations, `--fix` rewrites, `--diff` previews).

## Site-specific notes

- Internal links: use full logical paths in the `link` shortcode (`{{<link "/snacks/foo">}}`); bare names have failed to resolve for new/draft pages. Pages that cross-link must be published together (the shortcode errors on missing pages and breaks the build).
- I can't run Hugo in the Cowork sandbox (no network for the binary); ask Mike to run `build.sh` / `hugo serve -D`, or run it directly when in Claude Code with local shell access.
- pip in the sandbox needs `--break-system-packages`; python-pptx and matplotlib are the workhorses (see `Workspace/Tools/` — deck-mining and figure scripts, with a README). Locally, use the `p314` conda env. Note `tools/` at the repo root is a different thing: the site build/diff scripts.
