---
name: summarize-paper
description: Add a new paper or web post to the VisSnacks re-papering AI-summary list. Use when Mike gives a paper PDF (or URL) and asks to summarize it, add it to the summaries, or queue it for re-papering. Writes one file to Workspace/Re-Papering/PapersSummary/ and updates the checklist and index. Not for book chapters (those go in BookSummaries/).
---

# Summarize a paper for the re-papering list

Project background: `Workspace/Re-Papering/status.md` ("Process rules"). This skill is those rules as steps. If they disagree, `status.md` wins; tell Mike so the skill can be fixed.

## Book chapters: stop and warn

If the document is a book chapter (a chapter of Munzner, Cairo, Tufte, Ware, Wexler, etc.), do not proceed. Tell Mike: "This looks like a book chapter. This skill is for papers only; use the instructions in `Workspace/Re-Papering/BookSummaries/README.md` (and the process rules in `status.md`) instead." Then stop and let Mike decide. Book chapters use a different filename pattern (`author-book-chNN.md`) and directory, and some carry extra sections such as "Figures worth borrowing".

## Input

A local PDF path (preferred) or a URL.

- **Local PDF:** if it isn't already in `Workspace/Re-Papering/Papers to summarize/` or another local folder, leave it where it is. Don't copy it into the repo (copyrighted; repo may go public).
- **URL:** try it at most twice. On failure, skip, report the dead link, and ask Mike for a PDF. Never hunt mirrors, Wayback, or extractor services unless Mike supplied an alternate URL.

## Steps

0. **Establish the citation before anything else.** The filename, the H1 and the checklist row all need the full author list, title, venue, volume/issue/pages and publication year. Check the PDF's first page (`pdftotext -l 1`) and its metadata (`pdfinfo`).
   - **Official or HAL/cover-page version:** the citation is usually printed there. Use it.
   - **Author's/preprint version with the byline stripped** (no authors, volume, or pages; "omitted for review"; only a DOI and a copyright line): the document can't give you the citation. Ask Mike for the DOI if none is printed, or for the authors and venue directly. If a DOI is printed, one Crossref lookup is allowed (`https://api.crossref.org/works/<doi>` via WebFetch; counts toward the two-try rule). Say in the report that the citation came from Crossref, not the PDF.
   - **No DOI, no byline:** stop and ask Mike. Don't guess authors or the year from memory, and don't write placeholder filenames.
   - Pass the confirmed citation to the agent in step 2, and have the H1 state it plainly. Don't put "unverified" notes in the H1.
1. **Pick the filename.** `author-year.md` (one author), `author1-author2-year.md` (two), `author-et-al-year.md` (three or more), lowercase, in `Workspace/Re-Papering/PapersSummary/`. Check `ls` there for collisions and pattern-match the existing names. The year is the publication year, not the preprint year.
2. **Spawn one agent with `model: sonnet`** (faithful summarization to a fixed format doesn't need the strong model). Give it:
   - the exact PDF path (or URL plus the two-try rule) and the exact output path;
   - a closed reading list: that document and `Workspace/Re-Papering/PapersSummary/sarikaya-gleicher-2018.md` as the format exemplar. No wandering;
   - the format below;
   - an instruction to write the finished file directly to its real path, not just report it, and to note any read problems inline in the file.
3. **Update trackers yourself, only after the agent confirms the file was written and the citation is settled** (small edits, no agent):
   - `Workspace/Re-Papering/checklist.md`: add a row under "## Papers" as `- [/] Authors — Title (Venue, Year)`, using the existing rows' style.
   - `Workspace/Re-Papering/ai-summaries.md`: add the paper to the `PapersSummary/` list in the index.
4. **Report** the output path, anything the agent flagged (read problems, quotes it couldn't verify), and anything you decided that Mike didn't ask for.

Do not draft a re-papering post. An AI summary (`[/]`) and a post (`[!]`/`[x]`) are different things; the post is Mike's-voice work.

## Output format

File starts with an H1 giving the full citation, then bold-labelled sections, in this order:

```markdown
# Author, "Title" (Venue, vol/no, Year)

**What it is:** one paragraph: kind of paper (empirical, framework, survey, system...), what it claims, where it sits in the literature.

**AI summary:** the substance, section by section, as flowing prose. Faithful to the paper; no outside knowledge presented as the paper's.

**What a student/VisSnacks reader should get out of it:**
- bullets

**Skim/skip guidance:** what to read, what to skip, which figures and tables matter.

**Memorable specifics:**
- concrete numbers, figure descriptions, named examples, quotable lines (transcribed from the source, not recalled)

**Caveats:** (only if there are any: paper's limits, what the PDF lacked, claims that look dated)
```

Rules for the agent: read the actual document and summarize nothing from memory; transcribe quotes exactly; keep it the AI's voice (Mike's take is added separately); markdown-lint clean (blank lines around headings and lists).
