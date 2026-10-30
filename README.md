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
- Write math using protected inline notation and fenced math blocks as described below.

### GitHub Math Compatibility (Required)

Follow [GitHub's official mathematical-expression syntax](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions):

- Use GitHub's protected inline form (dollar sign, backtick, expression, backtick, dollar sign) for inline equations.
- Use fenced `math` blocks for displayed equations. This protects TeX punctuation escapes from Markdown parsing and is supported by the Pages renderer.
- See [Math Markdown Guide](Tools/MathMarkdownGuide.md) for examples. Mathematical notation belongs in math markup, not ordinary text or code spans unless it is actual program syntax.
- Do not use `\(...\)` or `\[...\]`; they are not the repository's supported Markdown delimiters.
- Do not place raw `<` or `>` inside math. Write `\lt` and `\gt` instead. For example, use `\sum_{i\lt j}` rather than `\sum_{i<j}`.
- Do not use `\operatorname`, `\#`, or other macros already known to fail in the repository's GitHub rendering path. Prefer simple notation such as `Var`, `Cov`, set cardinality with `\left|\cdot\right|`, and ordinary text outside the formula.
- Before committing, verify that inline dollar delimiters, display `$$` delimiters, and braces are balanced; search changed Markdown files for standalone equals lines, forbidden macros, and raw angle brackets inside formulas.
- Run `python3 Tools/check_math_markdown.py <changed-markdown-files>` before committing math-heavy notes. The checker enforces these repository-specific compatibility rules.

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
├── DailyTests/
│   └── INDEX.md
├── KnowledgeCards/
├── Connections/
│   └── KnowledgeGraph.md
└── Templates/
    └── SubjectTemplate.md
```

### Subject Template

Each subject should be saved as one Markdown file using [SubjectTemplate](Templates/SubjectTemplate.md). Drill notes keep canonical question content here and dated performance in DailyTests:

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

## Assessment History

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

- `DailyTests/`: [Dated interview results](DailyTests/INDEX.md), canonical question links, related concepts and assessment evidence. Keep ratings, timing, hints, specific gaps and verification here; use [the daily-test template](Templates/DailyTestTemplate.md). Full prompts and solutions belong in Questions.
- `Questions/`: Canonical prompts, solutions, reference code and reusable discussions by category. Reuse existing notes for exact repeats; retain meaningful dated variants together. Link back to every assessment and to related questions / knowledge cards.
- `Backlog.md`: Unfinished topics, future note clusters, and idea inventory.
- `KnowledgeCards/`: Short-form review cards for later use.
- `Connections/`: Cross-topic links and concept graph.
- `Templates/`: Standard templates for new entries.

## Workflow Rules

- Only finalized content provided by the user should be added as subject notes.
- Do not invent or draft mathematical content in this knowledge base.
- Preserve existing notes unless explicitly asked to revise them.
- Add cross-links when relationships are clear.
- Use protected inline formulas and fenced math blocks, following the GitHub Math Compatibility rules above.
- Do not commit generated HTML files; GitHub Actions builds the public website from Markdown.
- Before working from another device, run `git pull`.
- After updating notes, commit meaningful checkpoints automatically.
- Do not ask for confirmation before committing; commit by default after completing the change.
- Do not ask for confirmation before pushing; push by default after committing unless the user explicitly says not to push.
- Keep commits small and descriptive, ideally one note or one cleanup per commit.
- Do not commit local app settings, generated files, or OS-specific files.
- For new subject drafts, wait for finalized content. An explicitly requested archive of an existing drill may retain Pending questions/follow-ups with that status clear; do not invent their missing solutions or mark them mastered.

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

### Website Maintenance

- Maintain the website alongside the notes. After changing notes or website tools, install `Tools/requirements-site.txt`, run `python3 -m unittest discover -s Tools -p 'test_*.py'`, and run `python3 Tools/build_site.py` before committing and pushing.
- The build checks math markup in all Questions and DailyTests, plus all generated local page and section links. It includes the backlog, dated review summaries, and math-formatting guide as well as the question notes and daily tests.
- Keep build dependencies in `Tools/requirements-site.txt` so local previews and GitHub Actions use the same versions.
- After pushing, check the matching [Pages workflow run](https://github.com/dingare/quant-homework/actions/workflows/pages.yml) and confirm deployment succeeds.
- One-time repository setup: in **Settings → Pages → Build and deployment → Source**, select **GitHub Actions**. This was enabled on 2026-10-16. The workflow token can deploy to an enabled site but cannot perform the initial administrative setup; a `Configure Pages` error saying `Not Found` or `Resource not accessible by integration` calls for checking this setting.

## Latest Additions

- 2026-10-30: Reorganized [SC007 — Call Replication, Threshold Trading, and Local Time](Questions/StochasticCalculus/SC007_Call_Replication_Threshold_Trading_and_Local_Time.md) into an English subject note: Core Question, Hint, Intuition, Geometry, progressive Solution, common mistakes, follow-ups, connections, assessment history, and a short interview answer. The original knowledge card remains a reading map. The recorded interview completion remains at most about 20%; post-interview derivations do not establish mastery.

- 2026-10-30: 补充 [option replication 面试作答复盘](KnowledgeCards/StochasticCalculus/Call_Payoff_Threshold_Trading_Tanaka_and_Local_Time.md#interview-assessment--2026-10-30)：最新完成度自评最多约 20%，当场已提出临近到期向下穿越 100 的情形；明确离散调仓例子与连续模型完整论证的区别。仅更新题目相关复盘，未新增题目或知识卡，未计为独立掌握。

- 2026-10-30: Added [Call Payoff vs Threshold Trading: Tanaka and Local Time](KnowledgeCards/StochasticCalculus/Call_Payoff_Threshold_Trading_Tanaka_and_Local_Time.md), a Chinese study card on the stop-loss/start-gain paradox, finite variation versus Brownian paths, self-financing, local-time funding, and why uniform path approximation does not preserve Itô trading gains. Includes a hand-checkable example and explicit review questions; understanding remains provisional, with no new question attempt or mastery claim.

- 2026-10-30: Added two bus-waiting examples to existing notes: [P029 — random arrival on a 10/20-minute loop](Questions/Probability/P029_Random_Inspection_and_Residual_Wait.md#bus-variant--2026-10-30) derives length bias and the general stopping-probability formula; [SC006 — two independent Poisson routes](Questions/StochasticCalculus/SC006_Competing_Exponentials_and_Time_Dependent_Hazards.md#bus-variant--2026-10-30) derives the product survival function and distinguishes first-arrival competition from choosing a route with equal probability. Guided review; question counts and dated assessments are unchanged.

- 2026-10-30: Extended [P024 — Bayesian Coin Selection and Prediction](Questions/Probability/P024_Bayesian_Coin_Selection_and_Prediction.md) with Chinese notes from the ten-heads discussion: why the exact confidence lower bound uses the 1/10 power of 0.025, integrating over a uniform unknown bias, the 98.94% unfair-model posterior under equal model priors, and why the conditional parameter posterior is Beta(11, 1). Linked to P035; question counts and assessment records are unchanged.

- 2026-10-26: Added [Regularized Regression: Ridge, Lasso, Elastic Net, and LAR](KnowledgeCards/Statistics/Regularized_Regression_Ridge_Lasso_Elastic_Net_and_LAR.md) beside the OLS card, covering prediction and bias–variance, Bayesian Ridge, effective df, penalty geometry, sparsity, grouping, and qualified path / df comparisons. Existing OLS and L001 notes are linked; question counts and assessment records are unchanged.

- 2026-10-25: Added the [Dynamic Programming review pack](KnowledgeCards/Coding/DynamicProgramming/README.md): Chinese explanations, seven classic Medium / Hard problems, a 90–120 minute core plan, separate practice and solutions, runnable Python, and independent small-case verification. This is review material; question counts and assessment records are unchanged.

- 2026-10-25: Completed discussion of the [October 23 drill](DailyTests/2026-10-23.md). Added the [S024 multiple-testing / independent-confirmation derivation](Questions/Statistics/S024_Multiple_Testing_and_Independent_Confirmation.md) and [O010 proportional-cost position reference](Questions/Optimization/O010_Single_Asset_Position_with_Proportional_Trading_Costs.md). Q1–Q3 Partial / Hinted; Q4 Cold Solve by user report, exact written working unverified. The user clarified that displaying Q4's answer was for typing convenience, not inability to solve. No main question remains Pending; counts and actual-time records are unchanged.

- 2026-10-24: Archived the [October 23 drill](DailyTests/2026-10-23.md). Filed worked notes for [C020 — minimum deletions / LIS](Questions/Coding/C020_Minimum_Deletions_for_a_Strictly_Increasing_Subsequence.md) and [P036 — live Poisson arrivals](Questions/Probability/P036_Live_Orders_with_Poisson_Arrivals_and_Exponential_Lifetimes.md). Both are Partial / Hinted; Q1 exact user code is verified. At that archive point, Q3 / S024 and Q4 / O010 were Pending with prompts only; the October 25 completion entry above supersedes that status. All actual times unknown. Four canonical files were added, including two unattempted prompts; this does not imply four completed questions.

- 2026-10-23: Added [OLS: Expectation, Variance, Residuals, and Prediction](KnowledgeCards/Statistics/OLS_Expectation_Variance_Residuals_and_Prediction.md), an English knowledge card with the OLS flowchart, step-by-step matrix derivations, degrees of freedom, CI / PI, and LLN / CLT / normality conditions. Formulas and assumptions reviewed; question counts and assessment records are unchanged.

- 2026-10-22: Audited formula rendering across all 113 question notes, standardized math delimiters, repaired three corrupted matrix commands, and extended publication checks to the full question library. See the [math audit](Tools/MathMarkdownGuide.md#october-22-question-library-audit).

- 2026-10-22: Reorganized all 12 [DailyTests](DailyTests/INDEX.md) into linked assessment logs. Filed 50 additional canonical entries in the [question library](INDEX.md), reused existing notes for earlier questions and repeated variants, and retained all 73 item records, ratings, timing, pending follow-ups and old item anchors. Added reciprocal question / knowledge-card links. This is archival filing, not 50 new attempts or newly mastered topics.

- 2026-10-18: Recorded the [four-question interview drill](DailyTests/2026-10-18.md): tree-path states, Gaussian sign geometry, duplicated-data inference and first-collision timing. Preserved user-reported code completion, arithmetic clarifications and the already-known tail-sum method; subject-note counts unchanged.

- 2026-10-17: Recorded the [four-question interview drill](DailyTests/2026-10-17.md), including heap implementation evidence, independent cycle-length / endpoint-estimator derivations, exact confidence-bound review, and signal smoothing versus turnover costs. Updated review backlog; subject-note counts unchanged.

- 2026-10-12: Added [R001 — French OAT: Sovereign Spread, Repo Funding & Liquidity Risk](Questions/RatesResearch/R001_French_OAT_Spread_Repo_Funding_and_Liquidity_Risk.md), connecting sovereign repricing, repo margin and funding liquidity; recent market claims remain explicitly unverified.

- 2026-10-09: Added [P020 — Uniform Sum: Half-Threshold Overshoot Probability](Questions/Probability/P020_Uniform_Sum_Half_Threshold_Overshoot_Probability.md) with the full conditional-distribution derivation, simplex geometry, the atom at zero, and the infinite-sequence assumption.

- 2026-10-06: Added worked drill answers in C005, C006, P019, S010, and T007; extended P018, L001, and O002 with the exact drill variants. All answers are linked from [the daily test](DailyTests/2026-10-06.md#questions-and-worked-answers), with time-capped attempt context preserved.

- 2026-10-06: Added [daily interview testing results](DailyTests/2026-10-06.md) and a [daily-tests index](DailyTests/INDEX.md); recorded all seven questions, user-reported timings, ratings, and retrieval notes.

- 2026-10-02: Added [P018 — First Ace Position and Conditioning on a Face Card](Questions/Probability/P018_First_Ace_Position_and_Conditioning_on_a_Face_Card.md) on the first Ace distribution, exchangeable gaps, beta-binomial variance, and conditioning on a face card.

- 2026-09-27: Added [C004 — NeetCode Sliding Window Maximum](Questions/Coding/C004_NeetCode_Sliding_Window_Maximum.md) with segment tree, block DP, monotonic deque, and heap solutions, plus time/space comparisons.
- 2026-09-27: Added [P015](Questions/Probability/P015_Dice_Coupon_Collector_See_Every_Face_At_Least_Twice.md) on collecting every die face twice using a two-variable first-step recurrence.
- 2026-09-27: Added [Random Points, Order Statistics, and Spacings](KnowledgeCards/Probability/Random_Points_Order_Statistics_and_Spacings.md), summarizing completed P001 and P016 material; recorded unfinished extensions in the [To-Do List](Backlog.md#random-points-and-spacings--to-do-list).
- 2026-09-27: Added [P016](Questions/Probability/P016_Mutual_Nearest_Neighbors_on_a_Line.md) on mutual nearest neighbors, efficient simulation, indicator expectations, and uniform spacings.
- 2026-08-25: Added the [first-hitting parity, coverage, and alternating ownership framework](KnowledgeCards/Probability/First_Hitting_Parity_Coverage_and_Alternating_Ownership.md), connecting gambler's ruin, parity-augmented recursion, path/cycle coverage, linearity of expectation, and repeated-root difference equations to P011, with a staged review path.
- 2026-08-20: Added [P011](Questions/Probability/P011_Parity_of_First_Hitting_Times_on_an_Odd_Cycle.md) on first-hitting-time parity, odd-cycle ownership, linearity of expectation, and why optional stopping needs parity augmentation; added the related [second-order difference-equation knowledge card](KnowledgeCards/Probability/Second_Order_Difference_Equations_for_Random_Walk_Hitting_Problems.md).
- 2026-08-17: Added [O007](Questions/Optimization/O007_Turnover_Constrained_Mean_Variance_Portfolio_and_KKT_Active_Set.md) from the final Daily Quant problem generated before the source schedule paused on 2026-08-14; completed and corrected the active-set/KKT solution for the $L^1$ turnover constraint.
- 2026-08-13: Added the [Waiting Time and Competing Risks Cookbook](KnowledgeCards/Probability/Waiting_Time_and_Competing_Risks_Cookbook.md), organizing exponential races, Gamma / Weibull hazards, Poisson arrivals, execution queues, inspection bias, and phase-type CTMC models; linked it bidirectionally with SC004 and SC006 without increasing the daily-question count.
- 2026-08-13: Reviewed “Quant Prep Chat Organization” for 2026-08-03 through 2026-08-13 and added six missing daily problems: [L006](Questions/LinearAlgebra/L006_Factor_Neutral_Alpha_in_Eigenfactor_Space.md), [P010](Questions/Probability/P010_Bayesian_Signal_Selection_under_Multiple_Testing.md), [O006](Questions/Optimization/O006_Hedge_Constrained_Execution_with_Position_Limits.md), [C003](Questions/Coding/C003_Online_Median_with_Two_Heaps.md), [SC005](Questions/StochasticCalculus/SC005_Brownian_Hitting_Probability_with_Drift.md), and [SC006](Questions/StochasticCalculus/SC006_Competing_Exponentials_and_Time_Dependent_Hazards.md); deduplicated the correlated-noise Kalman and measurement-error/IV variants against T006 and S006.
- 2026-08-13: Added [P009](Questions/Probability/P009_Uniform_Sum_Stopping_Time_and_Overshooting_Draw.md) on uniform partial sums, the survival/tail-sum derivation of $E[N]=e$, and the expected overshooting draw.
- 2026-08-01: Added the [Indicator Random Variables Cookbook](KnowledgeCards/Probability/Indicator_Random_Variables_Cookbook.md), a reusable reference for indicator sums, covariance, overlap classification, factorial moments, and common counting patterns; linked it to P006 and P008 without increasing the daily-question count.
- 2026-07-19: Added [C001](Questions/Coding/C001_Count_of_Range_Sums_with_Prefix_Sums_and_Fenwick_Tree.md) on prefix sums, coordinate compression, Fenwick trees, and $O(n\log n)$ range-sum counting; expanded the recent review from five to six topics.
- 2026-07-18: Added [recent quant-prep review](Recent_Quant_Prep_Review_2026-07-18.md), linking canonical notes without duplicating topics already filed; expanded to six topics on 2026-07-19.
- 2026-07-18: Added [S005](Questions/Statistics/S005_HAC_Newey_West_Inference_for_Persistent_Trading_Signals.md) on HAC/Newey–West inference, score dependence, and persistent trading signals.
- 2026-07-18: Added [SC003](Questions/StochasticCalculus/SC003_Ornstein_Uhlenbeck_First_Hitting_Time.md) on OU first hitting times, generator ODEs, and mean-reversion holding periods.
- 2026-07-15: Added [L003](Questions/LinearAlgebra/L003_Woodbury_Identity_for_Low_Rank_Covariance_Inversion.md) on the Woodbury identity, low-rank covariance inversion, and factor-model computation.
- 2026-07-15: Added [P004](Questions/Probability/P004_Two_Out_of_Three_Gaussian_Signal_Triggers_and_Correlation.md) on two-out-of-three Gaussian trigger rules, threshold calibration, and correlation effects.
- 2026-07-13: Added [O003](Questions/Optimization/O003_Primal_vs_Dual_Optimization_and_When_the_Dual_Is_Easier.md) on primal vs dual optimization, KKT conditions, dimension reduction, and shadow-price interpretation.
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
