# Style guide and trimming strategy

## Macros in assets/template.tex

| Macro | Use |
|-------|-----|
| `\sect{1.1 Title}` | coloured section bar (one per lecture section) |
| `\sub{Name}` | light sub-bar inside a section |
| `\B{}` `\R{}` `\G{}` | blue formula/key, red trap, green definition |
| `\Eg{Example 1}` | orange highlighted example label |
| `\why{question}{answer}` | explain-why item: English question, answer text |
| `Y{20mm}` | wrapping p-column for tabulars |
| `\FS`, `\LH` | font size / line height injected by build.py |

## Table template

```latex
{\setlength{\tabcolsep}{1pt}\begin{tabular}{|Y{12mm}|Y{30mm}|Y{40mm}|}
\hline\rowcolor{cb!12}\B{Symbol}&\B{English name}&\B{Meaning / formula}\\\hline
$\omega_0$&natural frequency&$\omega_0=\sqrt{k/m}$\\\hline
\end{tabular}}
```

## Example template

```latex
\Eg{Example 1} Given: ... Find: ...
Solution: $E_k=\tfrac12mv^2$ $=\tfrac12\cdot2\cdot3^2$ $=9$ J.
```

## What to cut (in this order)

1. Descriptive paragraphs that restate slides without a formula, number or trap.
2. Second and third examples of the same method; keep the one whose table shape appears in the exam.
3. Explain-why items whose answer is a single definition already in a table.
4. Detailed arithmetic: replace with a summary table of intermediate results.
5. Only then reduce the font (never below 3.7pt).

## Coverage audit

For every section's Learning objectives, mark each bullet as: covered in table / covered in example / covered in explain-why / missing. Add missing ones as one line in the closest section (units, trade-offs, practical limits are typical gaps). Re-run the fit afterwards; a few lines of extra content usually still fit if a column had slack.
