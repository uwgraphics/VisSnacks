# Agent instructions for VisSnacks

Hugo site disseminating visualization knowledge (Mike Gleicher). Read `STYLE-GUIDE.md` before drafting or editing any page — it has voice, mechanics, and workflow rules (draft=true, leave uncommitted, verification list, genai disclosure).

Working material for the lecture-to-tutorial project lives in `_lecture_experiment/` (gitignored): plans, briefs, deck extractions (`extracted/`), scripts (`tools/`), reading summaries. Check `_lecture_experiment/0718-Summary.md` and `repapering-status.md` for project state before redoing work.

`MODULE-DOCS-PLAN.md` (root) is the document plan; `queue.md` (root) is the page backlog.

## Efficiency rules (portable — copy to other project CLAUDE.md files, e.g. the course web)

1. **Match model to task.** Faithful summarization, extraction, and format-following: spawn subagents with `model: sonnet`. Reserve the strong model for judgment work (drafting in Mike's voice, planning, critique).
2. **Fetch-failure budget.** Try any URL at most twice. On failure: skip, and report the dead link so it can be fixed at the source (readings list, course page) — never silently hunt mirrors, Wayback, or extractor services unless an alternate URL was explicitly provided. A dead link is a bug to report, not an obstacle to route around.
3. **Save as you go.** Write each unit of work (a summary, a draft section, an extraction) to disk the moment it's done. Session limits hit without warning; work in context or in /tmp dies with the session.
4. **Bias toward visible files over hidden scratch.** Put intermediate work (extractions, staged inputs, reports) in the project's designated working directory (here: `_lecture_experiment/`), not /tmp or the session scratchpad. Tradeoff: truly disposable junk (one-off scripts mid-debug, downloaded archives) may start in /tmp, but promote anything with reuse value immediately.
5. **Stage inputs before spawning agents.** Give subagents exact file paths to pre-staged local inputs and a closed reading list; forbid wandering. Have them write outputs to named files, not just their final message.
6. **Fresh sessions for batch work.** Long sessions reprocess their whole context on every call. When a batch is planned, write the plan to a file and run it from a new session whose only instruction is "resume per <file>".
7. **Long-running batches: split across agents, run in parallel, one topic-cluster each** — a failure then costs one cluster, not the batch.

## Site-specific notes

- Internal links: use full logical paths in the `link` shortcode (`{{< link "/snacks/foo" >}}`); bare names have failed to resolve for new/draft pages. Pages that cross-link must be published together (the shortcode errors on missing pages and breaks the build).
- I can't run Hugo in the Cowork sandbox (no network for the binary); ask Mike to run `build.sh` / `hugo serve -D`, or run it directly when in Claude Code with local shell access.
- pip in the sandbox needs `--break-system-packages`; python-pptx and matplotlib are the workhorses (see `_lecture_experiment/tools/`).
