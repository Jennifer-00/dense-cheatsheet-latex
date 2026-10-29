---
name: dense-cheatsheet-latex
description: Builds dense, colour-coded, multi-column A4 landscape cheat sheets in LaTeX (xelatex, Chinese/English) for STEM midterm or final exams from lecture notes, homework and slides, then auto-fits the font size to a page budget. Use when the user wants a cheat sheet, formula sheet, exam summary, 小抄, 备忘单, or asks to condense course material onto few pages.
---

# Dense cheat sheet (LaTeX)

Turns material of any quantitative course (maths, physics, engineering, CS, statistics, ...) into a 1-3 page, 4-column, A4-landscape sheet. It is course-agnostic: nothing here depends on a specific subject or exam. Content quality comes from the workflow below; layout comes from `assets/template.tex`; fitting comes from `scripts/build.py`.

## Workflow

Copy this checklist and track progress:

```
- [ ] 1. Inventory: list topics/sections, the "Learning objectives" of each section, homework, past questions
- [ ] 2. Agree constraints with the user (pages, language, font floor, what to drop)
- [ ] 3. Copy assets/template.tex to the project, write one \sect per lecture section
- [ ] 4. Fill each section in the fixed order (see below)
- [ ] 5. Fit: python scripts/build.py cheat.tex --pages 2
- [ ] 6. Visual check: render PNG, look for clipped text, empty columns, orphan headings
- [ ] 7. Coverage audit against Learning objectives; add gaps, refit
```

1. **Inventory.** Extract text from slides/PDF (`pdftotext` or PyMuPDF). Grep every "Learning objectives" block; they are the coverage checklist for step 7.
2. **Constraints.** Ask (AskQuestion) for: page limit (or "content first, pages later"), language mix, minimum readable font (3.8pt is already tiny; below ~3.7pt is not readable when printed), whether answers to "explain why" questions are wanted.
3. **Per-section order (always the same):**
   1. Concepts and symbols (one row per symbol: name, English name, formula/meaning).
   2. Formulas and comparison tables.
   3. Worked examples (`\Eg`), then
   4. "Explain why" questions.
4. **Worked examples** use "已知 / 求 / 解" (Given / Find / Solution). Every calculation line is **formula = substitution = value → result**; never show only the final number. Show intermediate tables (e.g. algorithm traces, iteration tables, truth tables) in the same shape as the lecture so they match what the exam expects.
5. **Explain-why items:** English question, answer in Chinese (or the user's language), with the hard technical term in parentheses inline (e.g. 过阻尼 (overdamped)). Do not write full English answers unless asked.
6. **Style rules:** colour bars instead of boxes; flowing layout (no forced column breaks, let `multicols*` balance); delete descriptive filler; no source tags like "HW1 P3a" or "lecture 5"; blue `\B` = formula/key, red `\R` = trap, green `\G` = definition, orange `\Eg` = example label.
7. **Tables:** use ruled tables (`\hline`) with a shaded header row; use `Y{width}` p-columns so text wraps. Tables cannot split across columns, so large ones leave gaps; split them into two small ones if a column is short.

## Fitting

```bash
python scripts/build.py cheat.tex --pages 2 --sizes 4.4,4.2,4.0,3.9,3.8,3.7
```

The script compiles once per size through `xelatex "\def\FS{..}\def\LH{..}\input{cheat.tex}"`, keeps the largest size that fits the page budget, and prints per-page column fill (fraction of page height used by each of the 4 columns). Interpret the fill:

- last page columns all about 0.95-0.99: well packed
- one column far below the others: free space; add content or enlarge font
- more pages than budget at the smallest size: cut content (see `references/style-guide.md`, "What to cut")

If the PDF is locked by a viewer, the script writes to `<name>_fit.pdf` automatically.

## Gotchas

- Needs xelatex (MiKTeX/TeX Live) with `ctex`, `multicol`, `xcolor`, `tcolorbox` not required. PyMuPDF (`pip install pymupdf`) for fill measurement and PNG render.
- A trailing `\\` or `\par\vskip` at the very end of the body can create a blank extra page; end the body with plain text.
- When editing with PowerShell, avoid `String.Replace` on text with `$` or backslashes; use the editor's exact-replace tool or Python.
- Keep a generator script (like `make_*.py`) only if transforming an older source; otherwise edit the `.tex` directly.
- When the user asks a concept question mid-way ("what is X?"), answer in chat; change the sheet only if asked.

## More

- Layout/macro reference and trimming strategy: [references/style-guide.md](references/style-guide.md)
- Starter file: [assets/template.tex](assets/template.tex)
