# Workspace Tools

Small helper scripts written while building pages — deck mining and figure generation.
They aren't part of the Hugo site or its build.

**Not to be confused with `tools/` at the repo root**, which holds the *site build*
scripts (`baseline.sh`, `compare.sh` — snapshot `public/` and diff a rebuild against it).
Those run the site; these make raw material for pages.

## The scripts

All four are short, single-purpose, and take file arguments (they glob fine:
`python titles.py "decks/"*.pptx`).

| script | what it does |
| --- | --- |
| `extract.py` | Dumps one deck's full text — every text frame, picture placeholders, and speaker notes — slide by slide. The heavyweight one; use when you need everything. |
| `titles.py` | Lists just the slide titles (plus a slide count) for one or more decks. The fast way to find which deck covers a topic. |
| `keyslides.py` | Scans decks for the slides that probably carry the point — matches `lesson\|takeaway\|summary\|key point\|warning\|advice\|main strateg\|important\|remember` and prints the first 500 chars of each hit. |
| `figs.py` | Regenerates the matplotlib figures for the encodings pages: `four-channels.png` (same 5 numbers in position/length/area/luminance), `line-vs-dot.png`, `dot-lollipop-bar.png`, `alpha-vs-sorted.png`. |

## Running them

Needs `python-pptx` (the first three) and `matplotlib` + `numpy` (`figs.py`), both
present in the `p314` conda env:

```sh
conda run -n p314 python Workspace/Tools/titles.py "_lecture_experiment/Lectures 25"/*.pptx
```

**If `conda run` fails**, call the env's interpreter directly — it needs no conda
machinery and works the same:

```sh
/opt/anaconda3/envs/p314/bin/python Workspace/Tools/titles.py "_lecture_experiment/Lectures 25"/*.pptx
```

(Seen 2026-08-22 in a sandboxed Claude Code session: `conda run` died in conda's own
argument parsing — the rattler solver plugin panics with `Attempted to create a NULL
object` when it can't reach the network/system configuration. Nothing to do with these
scripts, and the direct-interpreter form sidesteps it entirely.)

The lecture decks and reading PDFs these read live in `_lecture_experiment/`, which is
gitignored (~2 GB of copyrighted course material). The scripts are tracked; their inputs
are not.

## Notes

- **`figs.py` writes into tracked page bundles** (`content/modules/encodings/`,
  `content/snacks/charts-are-encodings/`) and will overwrite the committed PNGs. A
  different matplotlib version renders byte-different files, so expect image diffs after
  running it — check `git status` before committing. Paths resolve relative to the repo
  root, so it can be run from anywhere.
- `titles.py` reads a python-pptx internal (`_sldIdLst`) just to get the slide count; it
  works today but is the thing most likely to break on a python-pptx upgrade.
- Verified working 2026-08-15 against `01-W-WhatIsVis.pptx` with python-pptx 1.0.2 and
  matplotlib 3.11.1.
