# Math in GitHub Notes

Use fenced math blocks for display equations and GitHub's protected inline form for inline equations. These preserve TeX punctuation escapes through Markdown parsing, including integral spacing, literal set braces, matrix row separators, and percent signs. The October 14 audit confirmed that unprotected spacing escapes became literal commas and that GitHub rejected the operatorname macro.

Display source example (shown as source, not rendered):

````text
```math
F_Z(y)=\int_0^y 1\,du+\int_y^1\frac{y}{u}\,du.
```
````

Inline source example: `$` followed by a backtick, the TeX expression, a backtick, and `$`.

- For upright function names, use the mathrm macro with Var, Cov, SE, or plim in braces. GitHub currently rejects operatorname in these notes.
- Do not put mathematical expressions into ordinary code spans unless showing source code is intentional.
- Keep bounds, variance versus standard deviation, density normalizations, conditioning events, and denominator assumptions explicit.
- Questions contains the canonical prompts, solutions and reusable discussions. DailyTests retains their links and essential assessment evidence. Preserve meaningful typo/wording clarifications and never turn guided work into a cold solve.
- A checker can catch known syntax failures; it cannot prove that a derivation is correct or replace a rendered-page review.

Run `python Tools/check_math_markdown.py Questions DailyTests` and `python -m unittest discover -s Tools -p 'test_*.py'` (the latter needs the existing mistune build dependency). The checker defaults to both Questions and DailyTests, and the Pages build rejects math-format errors in either directory. After publishing, inspect rendered pages for macro errors, literal punctuation, missing delimiters, and integral/interval readability.

Reference: [GitHub's official mathematical-expression documentation](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions).

## October 14 audit scope

All seven dated logs from October 6 through October 13 were read for mathematical content. The repaired source contains 64 display formulas and 73 inline formulas; the index is checked separately. Fourteen blocked macro occurrences were replaced with supported upright names. Twenty-six independent exact-enumeration or numerical checks covered conditioned positions, medians, Bayesian prediction, competing events, permutation moments, randomization p-values, stopping values, dice counts, branching recursion, MA moments, residual waiting, product-conditioned moments, and posterior odds. The remaining derivations, assumptions, matrix identities, asymptotic standard errors, and interval formulas were reviewed directly.

This audit preserves historical attempted answers and grades. Incorrect attempted answers remain explicitly labeled as attempts; a check of corrected reference formulas must not rewrite history as independent success. Q5's unattempted decision follow-up has no published solution.

## October 22 question-library audit

All 113 question notes were checked after the DailyTests migration. Legacy inline/display notation was normalized to the protected forms above, preserving formula bodies and code examples. Three matrix-opening commands in O007 contained a backspace control character instead of a TeX backslash; these produced visible “Math input error” messages and were repaired. The plain K in C002's title is now ordinary text so navigation labels display cleanly.

The audit checks every formula through Markdown-to-HTML conversion and MathJax 3.2.2 CHTML, the major version used by the website. The current library has 2,568 mathematical expressions. Source checks also reject invisible control characters and improperly nested or escaped environment commands. Regression coverage ensures broken question math blocks publication. Formula rendering checks do not regrade attempts or establish mathematical correctness of historical answers.
