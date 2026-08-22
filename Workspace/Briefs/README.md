# Per-Page Briefs

The unit of work between "there's a lecture about this" and "there's a draft page." One brief
per planned VisSnacks page, built from the 2025 CS765 lecture decks plus the course module
pages and the reading summaries in `../Re-Papering/`.

Moved here from `_lecture_experiment/briefs/` on 2026-08-22 — same reason re-papering moved:
these are durable working notes, and an ignored directory is one `rm -rf` from gone with no
history. The bulk course material (decks, reading PDFs, `extracted/` deck text) correctly
stays in the gitignored `_lecture_experiment/`.

## Naming

`NN-topic.md`, where `NN` is the **week of the source lecture** — an approximation of course
order, so the directory sorts roughly the way the class runs. Approximation, not provenance:
`01-tutorial-1-revision.md` draws on lectures 1-W *and* 2-M but is numbered 01 because that's
where it belongs in the sequence. Several briefs can share a week (three come from week 2).

| brief | source lecture(s) |
| --- | --- |
| `00-TEMPLATE.md` | — (the template) |
| `01-tutorial-1-revision.md` | 1-W, 2-M |
| `02-tufte-snack.md` | 2-W |
| `02-vis-basics.md` | 2-M, slides 5–38 |
| `02-why-vis.md` | 2-M, slides 39–61 |
| `03-data-abstraction.md` | 3-W, first half |
| `03-data-abstraction-draft-report.md` | — (verification list for the drafted page) |
| `03-task-abstraction.md` | 3-W, second half |
| `05-implementation.md` | 5-M |
| `05-too-much-stuff.md` | 5-W, 6-W |
| `07-evaluation.md` | 7-M |

No `04`: the encodings pages were the original pilot and predate the brief format — they were
drafted from `_lecture_experiment/lecture-experiment.md` instead. Weeks 8–15 have no briefs
yet; `_lecture_experiment/lecture-mining-plan.md` has the slide-level inventory they'd be
built from.

## How a brief works

Sections 1–4 are **agent-filled** and recoverable from materials: what the document is, course
fit (with module learning outcomes quoted), sources, and the high-value slides with numbers so
Mike doesn't dig through a deck. Sections 5–8 are **Mike's**, and are the parts no agent can
produce: what to cut, the stories, the contested takes, and constraints. Target is ~5 minutes
of his time per brief.

Two things learned the hard way and worth not re-deriving:

- **An empty §5–8 does not block drafting.** `content/tutorials/data-abstraction/` was drafted
  from a brief with §5–8 completely blank. Filling those sections makes a page better; it isn't
  a gate. The real bottleneck is *review* of finished drafts.
- **Record answers back into the brief.** When Mike settles a question, strike the question and
  write the answer where the question was, dated — otherwise the next session re-asks it. The
  resolved items in `01-tutorial-1-revision.md` and `02-why-vis.md` show the pattern.

## A note on publishing

This directory is tracked, and the repo may become public. The briefs quote Mike's own slide
text extensively (fine) but also carry in-progress editorial deliberation — tone calibration
for the Tufte page, open questions about whose research an example is, judgments about which
lecture material is weak. Worth a look before the repo goes public; nothing here is secret,
but some of it is thinking-out-loud rather than published opinion.
