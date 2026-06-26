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
- Keep Markdown as the single source of truth.
- Write math in GitHub-compatible form: `$...$` for inline math and `$$...$$` for display math.

### Folder Structure

```text
homework/
├── README.md
├── INDEX.md
├── Progress.md
├── Questions/
│   ├── LinearAlgebra/
│   ├── Probability/
│   ├── Statistics/
│   ├── Econometrics/
│   ├── TimeSeries/
│   ├── Optimization/
│   ├── Coding/
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
- `E001`, `E002`, ... for Econometrics
- `T001`, `T002`, ... for Time Series
- `O001`, `O002`, ... for Optimization
- `C001`, `C002`, ... for Coding
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
5. Commit and push the Markdown updates to GitHub.

### ChatGPT-to-GitHub Checklist

When the user provides a finalized ChatGPT prompt/answer to save:

1. Run `git pull` first if this machine may not have the latest remote changes.
2. Save only finalized Markdown content under the correct `Questions/{Category}/` folder.
3. Use the next available category ID and the standard filename format.
4. Update `INDEX.md`, `Progress.md`, and `Connections/KnowledgeGraph.md`.
5. Update `README.md` latest additions when a new note is added.
6. Do not create, regenerate, or commit HTML files.
7. Review with `git status --short`, commit a meaningful checkpoint, then run `git push`.

## Purpose

- Store finalized interview prep notes by subject in a consistent, searchable structure.
- Track progress across core quant interview domains.
- Maintain explicit links between related concepts for review and synthesis.

## Structure

- `Questions/`: Canonical question and subject notes by category.
- `KnowledgeCards/`: Short-form review cards for later use.
- `Connections/`: Cross-topic links and concept graph.
- `Templates/`: Standard templates for new entries.

## Workflow Rules

- Only finalized content provided by the user should be added as subject notes.
- Do not invent or draft mathematical content in this knowledge base.
- Preserve existing notes unless explicitly asked to revise them.
- Add cross-links when relationships are clear.
- Use `$...$` for inline formulas and `$$...$$` for block formulas.
- Do not generate or commit HTML files; GitHub Markdown rendering is the canonical preview.
- Before working from another device, run `git pull`.
- After updating notes, commit meaningful checkpoints and run `git push`.
- Keep commits small and descriptive, ideally one note or one cleanup per commit.
- Do not commit local app settings, generated files, or OS-specific files.
- If a note is incomplete, leave it out of the knowledge base until the user marks it finalized.

## Latest Additions

- 2026-06-26: Added [L001](Questions/LinearAlgebra/L001_Ridge_Regression_as_PCA_Shrinkage.md) on ridge regression as PCA shrinkage.
- 2026-06-25: Added [P001](Questions/Probability/P001_Fixed_vs_Exists_Probability_Patterns.md) on fixed-vs-exists probability patterns.
- 2026-06-25: Added [S001](Questions/Statistics/S001_OLS_Bias_vs_Variance_with_Correlated_Regressors.md) on OLS bias vs variance with correlated regressors.
- 2026-06-25: Added [S002](Questions/Statistics/S002_Leave_One_Out_OLS_via_Sherman_Morrison.md) on leave-one-out OLS via Sherman-Morrison.
- Initial project scaffold created on 2026-06-25.
- Base index, progress tracker, knowledge graph, and subject template added.
