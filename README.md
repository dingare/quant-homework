# Buyside Quant Handbook

Local Markdown knowledge base for daily buy-side quant interview preparation.

## Maintenance Instructions

This repository should be maintained using the following rules:

### Scope

- This is a long-term knowledge base, not a scratchpad.
- Keep formatting consistent.
- Preserve previous notes unless explicitly asked to revise them.
- Make the folder easy to search and review.
- Add cross-links when obvious.
- Do not invent math content.
- Only use finalized content provided by the user from ChatGPT.
- Keep Markdown as the single source of truth; generated website HTML is disposable.
- Write math in GitHub-compatible form: `$...$` for inline math and fenced `math` blocks for display math.

### Folder Structure

```text
homework/
├── README.md
├── INDEX.md
├── Progress.md
├── Backlog.md
├── Questions/
│   ├── LinearAlgebra/
│   ├── Probability/
│   ├── Statistics/
│   ├── TimeSeries/
│   ├── Optimization/
│   ├── Coding/
│   ├── StochasticCalculus/
│   └── RatesResearch/
├── KnowledgeCards/
├── Connections/
│   └── KnowledgeGraph.md
└── Templates/
    └── SubjectTemplate.md
```

### Subject Template

Each daily subject should be saved as one Markdown file using this structure:

```md
# {ID} — {Subject Title}

## Metadata

- Category:
- Difficulty:
- Interview Relevance:
- Tags:
- Date Added:
- Status:

## Core Question

## Hint

## Solution

## Key Knowledge Points

## Intuition

## Geometry

## Common Mistakes

## Interview Follow-ups

## Market / Rates Application

## Connections

## What to Remember
```

### ID Rules

- `L001`, `L002`, ... for Linear Algebra
- `P001`, `P002`, ... for Probability
- `S001`, `S002`, ... for Statistics
- `T001`, `T002`, ... for Time Series
- `O001`, `O002`, ... for Optimization
- `C001`, `C002`, ... for Coding
- `SC001`, `SC002`, ... for Stochastic Calculus
- `R001`, `R002`, ... for Rates Research

When adding a new subject, choose the next available ID in that category.

### Filing Rules

Save each subject under:

`Questions/{Category}/{ID}_{Short_Title}.md`

Example:

`Questions/Statistics/S001_Leave_One_Out_OLS.md`

### Update Workflow

Whenever a new subject is added:

1. Update `README.md` with a short project overview and latest additions.
2. Update `INDEX.md` with a categorized list of all questions.
3. Update `Progress.md` with counts by category.
4. Update `Connections/KnowledgeGraph.md` with related concepts.
5. Commit the Markdown updates automatically after the changes are complete.
6. Push the updates automatically after the commit is complete.

### ChatGPT-to-GitHub Checklist

When the user provides a finalized ChatGPT prompt/answer to save:

1. Run `git pull` first if this machine may not have the latest remote changes.
2. Save only finalized Markdown content under the correct `Questions/{Category}/` folder.
3. Use the next available category ID and the standard filename format.
4. Update `INDEX.md`, `Progress.md`, and `Connections/KnowledgeGraph.md`.
5. Update `README.md` latest additions when a new note is added.
6. Do not commit generated HTML files; the website is generated automatically by GitHub Actions.
7. Review with `git status --short` and commit a meaningful checkpoint automatically.
8. Push automatically after the commit unless the user explicitly says not to push.

## Purpose

- Store finalized interview prep notes by subject in a consistent, searchable structure.
- Track progress across core quant interview domains.
- Maintain explicit links between related concepts for review and synthesis.

## Structure

- `Questions/`: Canonical question and subject notes by category.
- `Backlog.md`: Unfinished topics, future note clusters, and idea inventory.
- `KnowledgeCards/`: Short-form review cards for later use.
- `Connections/`: Cross-topic links and concept graph.
- `Templates/`: Standard templates for new entries.

## Workflow Rules

- Only finalized content provided by the user should be added as subject notes.
- Do not invent or draft mathematical content in this knowledge base.
- Preserve existing notes unless explicitly asked to revise them.
- Add cross-links when relationships are clear.
- Use `$...$` for inline formulas and fenced `math` blocks for display formulas.
- Do not commit generated HTML files; GitHub Actions builds the public website from Markdown.
- Before working from another device, run `git pull`.
- After updating notes, commit meaningful checkpoints automatically.
- Do not ask for confirmation before committing; commit by default after completing the change.
- Do not ask for confirmation before pushing; push by default after committing unless the user explicitly says not to push.
- Keep commits small and descriptive, ideally one note or one cleanup per commit.
- Do not commit local app settings, generated files, or OS-specific files.
- If a note is incomplete, leave it out of the knowledge base until the user marks it finalized.

## Local Editing Checklist

When working locally on this repo:

1. Edit the relevant Markdown note under `Questions/`, `Connections/`, or `Templates/`.
2. If you add or change a subject note, update `INDEX.md`, `Progress.md`, `Connections/KnowledgeGraph.md`, and `README.md` latest additions when needed.
3. Build the website with `python3 Tools/build_site.py` only if you want a local preview; do not commit `_site/`.
4. Review with `git status --short`.
5. Commit the Markdown changes automatically.
6. Push automatically after the commit unless the user explicitly says not to.

## Mobile Access

- Preferred reading site: https://dingare.github.io/quant-homework/
- Use the GitHub mobile app for quick browsing, search, and commit history.
- Use mobile Safari or Chrome for the public website when formula preview matters.
- Star or pin `dingare/quant-homework` in GitHub so it is easy to find.
- Use mobile editing only for small typo fixes. For new notes or formula-heavy edits, use a laptop and then `git push`.

## Website Publishing

- `Tools/build_site.py` builds a mobile-friendly static site into `_site/`.
- `_site/` is ignored and should not be committed.
- GitHub Actions deploys the site to GitHub Pages after each push to `main`.
- The public website is generated from the Markdown source files, so update Markdown first, then commit and push by default unless the user explicitly says not to.

## Latest Additions

- 2026-07-12: Updated workflow rules so this repo now auto-commits and auto-pushes by default unless explicitly told not to.
- 2026-07-12: Added [T004](Questions/TimeSeries/T004_Kalman_Filtering_II_Covariance_Weighted_Bayesian_Updating.md) on Kalman gain, innovation covariance, and covariance-weighted Bayesian updating.
- 2026-07-12: Merged Econometrics into Statistics and refiled [S003](Questions/Statistics/S003_Cointegration_Trading_Equilibrium_Rather_Than_Correlation.md) and [S004](Questions/Statistics/S004_Efficient_IV_Rayleigh_Quotient_and_Covariance_Weighted_Signal_Combination.md).
- 2026-07-10: Added [O002](Questions/Optimization/O002_Constrained_Mean_Variance_Optimization_and_the_Meaning_of_Lagrange_Multipliers.md) on constrained mean-variance optimization, dollar neutrality, and the meaning of Lagrange multipliers.
- 2026-07-10: Added [T003](Questions/TimeSeries/T003_AR1_First_Passage_Time_and_Why_Persistence_Changes_Waiting_Time.md) on AR(1) first passage time, stationary scale, and why persistence changes waiting time.
- 2026-07-08: Added [L002](Questions/LinearAlgebra/L002_PCA_Covariance_Geometry_and_Why_Butterfly_Trades_Curvature.md) on PCA covariance geometry, yield-curve risk directions, and why butterfly trades primarily isolate curvature.
- 2026-07-06: Added [Backlog](Backlog.md) to track unfinished topics and future note clusters.
- 2026-07-06: Added [P003](Questions/Probability/P003_Deterministic_Tournament_Brackets_Survival_and_Meeting_Probabilities.md) on deterministic tournament brackets, survival, and meeting probabilities.
- 2026-06-29: Added [T001](Questions/TimeSeries/T001_Kalman_Filter_I_Recursive_Bayesian_Estimation_for_Noisy_Market_Signals.md) on Kalman filtering as recursive Bayesian estimation for noisy market signals.
- 2026-06-29: Added [O001](Questions/Optimization/O001_Convex_Duality_I_No_Arbitrage_Pricing_through_Primal_and_Dual_Optimization.md) on convex duality and no-arbitrage pricing through primal and dual optimization.
- 2026-06-27: Added [SC001](Questions/StochasticCalculus/SC001_Itos_Lemma_and_Discounted_Price_Martingale.md) on Itô's lemma and the discounted price martingale.
- 2026-06-26: Added [L001](Questions/LinearAlgebra/L001_Ridge_Regression_as_PCA_Shrinkage.md) on ridge regression as PCA shrinkage.
- 2026-06-25: Added [P001](Questions/Probability/P001_Fixed_vs_Exists_Probability_Patterns.md) on fixed-vs-exists probability patterns.
- 2026-06-25: Added [S001](Questions/Statistics/S001_OLS_Bias_vs_Variance_with_Correlated_Regressors.md) on OLS bias vs variance with correlated regressors.
- 2026-06-25: Added [S002](Questions/Statistics/S002_Leave_One_Out_OLS_via_Sherman_Morrison.md) on leave-one-out OLS via Sherman-Morrison.
- Initial project scaffold created on 2026-06-25.
- Base index, progress tracker, knowledge graph, and subject template added.
