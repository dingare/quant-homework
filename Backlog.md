# Backlog

Unfinished topics and future note clusters. Canonical prompts and solutions are in the [question library](INDEX.md); [DailyTests](DailyTests/INDEX.md) preserves dated assessment evidence. The October 22 filing migration does not close any outstanding independent check or Pending follow-up.

## Random Points and Spacings — To-Do List

Status: Core topic completed and summarized in the [Random Points, Order Statistics, and Spacings](KnowledgeCards/Probability/Random_Points_Order_Statistics_and_Spacings.md) Knowledge Card. P001 covers interval and semicircle coverage; P016 covers mutual neighbors, simulation, expectation, and spacing laws.

**Future problems for the next session**

- Derive the variance of the mutual-neighbor car count by classifying overlapping local-gap events; compare it with simulation uncertainty.
- Derive the nearest-neighbor distance distribution for an endpoint rank, an interior rank, and a uniformly selected car; distinguish these from a fixed adjacent spacing.
- Work out mutual-neighbor counts on a circle with geodesic distance and with cars fixed at segment endpoints; state the changed boundary comparisons.
- Analyze one explicit nonuniform position model and check which gap-symmetry arguments and expectation formulas survive.
- Develop the existing Part X broken-stick item into minimum- and maximum-spacing questions, distinguishing internal gaps from all gaps including boundaries.

These are unfinished extensions, not completed question notes. The simulation,
mean, and Dirichlet/Beta results already in P016 do not need to be redone.

## Probability Patterns

Goal: organize probability interview problems by **thinking patterns**, not by probability distributions. Each chapter should focus on the intuition, common solution techniques, and representative interview questions.

### Part I. Elimination Tournaments / Random Brackets ⭐⭐⭐⭐⭐

Status: Completed via `P003`.

**Core idea**

Random bracket + deterministic strength + subtree counting.

**Key techniques**

- Random binary tree
- Counting
- Hypergeometric distribution
- Conditional probability

**Representative problems**

- Probability players 1 and 2 meet in the final
- Player k reaches Top 4 / Final
- Which round do players i and j meet?
- Expected meeting round
- General player i vs. player k

### Part II. One-Round Random Matching ⭐⭐⭐⭐⭐

Status: Completed via `P005`. Any subsequent Part II patterns should still be added to the same question file.

**Core idea**

Random perfect matching on 2n people.

**Key techniques**

- Symmetry
- Indicator variables
- Counting

**Representative problems**

- A and B matched together
- Couples matching problem
- Expected number of matched pairs
- Random pairing variants

### Part III. Random Permutations ⭐⭐⭐⭐⭐

Status: Started via `P006` (inversion counts) and `P008` (runs in a conditioned random ordering); other permutation patterns remain.

**Core idea**

Uniform random permutations.

**Key techniques**

- Symmetry
- Inclusion-Exclusion
- Counting

**Representative problems**

- Hat Check (Derangement)
- Secret Santa
- Relative order
- Records / inversions

### Part IV. Occupancy (Balls into Bins) ⭐⭐⭐⭐⭐

**Core idea**

Random allocation into bins.

**Key techniques**

- Indicator variables
- Poisson approximation
- Linearity of expectation

**Representative problems**

- Empty bins
- Maximum load
- Hash collisions
- Coupon occupancy

### Part V. Birthday and Collision ⭐⭐⭐⭐

**Core idea**

Collisions under random sampling.

**Key techniques**

- Complement rule
- Approximation
- Occupancy arguments

**Representative problems**

- Birthday paradox
- Hash collisions
- Duplicate detection

### Part VI. Coupon Collector ⭐⭐⭐⭐⭐

**Core idea**

Collecting all types.

**Key techniques**

- Geometric random variables
- Linearity of expectation

**Representative problems**

- Expected time to collect all coupons
- Partial collection
- Multiple copies

### Part VII. Random Walk and Markov ⭐⭐⭐⭐⭐

Status: Started via `P007` (unequal jumps, overshoot, and first-step analysis); other Markov patterns remain.

**Core idea**

First-step analysis.

**Key techniques**

- Recursion
- Markov property
- Dynamic programming

**Representative problems**

- Gambler's Ruin
- Consecutive Heads
- Hitting time
- Absorption probability

### Part VIII. Conditional Probability and Bayes ⭐⭐⭐⭐

**Core idea**

Condition on hidden information.

**Key techniques**

- Bayes' theorem
- Conditioning
- Law of total probability

**Representative problems**

- Monty Hall
- Boy or Girl
- Medical testing
- Prisoners problem

### Part IX. Optimal Stopping ⭐⭐⭐⭐⭐

**Core idea**

Stop now or continue?

**Key techniques**

- Bellman equation
- Dynamic programming
- Threshold policy

**Representative problems**

- Secretary problem
- Dice stopping
- Card stopping
- Prophet inequality

### Part X. Expectation Tricks ⭐⭐⭐⭐⭐

**Core idea**

Compute expectations without computing full distributions.

**Key techniques**

- Indicator variables
- Linearity of expectation
- LOTUS
- Symmetry

**Representative problems**

- Broken stick
- Expected maximum
- Expected inversions
- Random BST statistics

### Part XI. Symmetry Arguments ⭐⭐⭐⭐⭐

**Core idea**

Exploit invariance to avoid unnecessary computation.

**Key techniques**

- Exchangeability
- Symmetry
- Coupling intuition

**Representative problems**

- Random chord
- Relative ordering
- Random graphs
- Random tournaments

### Part XII. Advanced Counting ⭐⭐⭐

**Core idea**

Combinatorial structures.

**Key techniques**

- Catalan numbers
- Lattice paths
- Recurrence
- Generating functions

**Representative problems**

- Dyck paths
- Catalan counting
- Random BST
- Parentheses problems

## Future Template for Each Part

Each chapter should eventually contain:

1. Intuition
2. Core Pattern(s)
3. General Formula(s)
4. Representative Problems
5. Common Interview Follow-ups
6. Generalizations
7. Common Mistakes
8. Cheat Sheet

## Covariance-Weighted Estimation Themes

Goal: organize the recurring mathematical idea behind `S004` and related topics. The main theme is that covariance is used to remove redundancy before combining information.

### Part A. Efficient IV and GMM Weighting ⭐⭐⭐⭐⭐

Status: Started via `S004`, but still incomplete conceptually.

**Core idea**

Choose moment or instrument weights using inverse covariance, so redundant information is downweighted.

**Key techniques**

- Rayleigh quotient
- Inverse covariance weighting
- GMM efficiency
- Signal-to-noise optimization

**Topics to revisit**

- Efficient IV versus basic IV
- Why optimal IV weights are proportional to `Q^{-1}q`
- Efficient GMM weighting matrix
- Weak instruments and near-collinearity

### Part B. GLS and Mahalanobis Geometry ⭐⭐⭐⭐

**Core idea**

Euclidean weighting is wrong when errors or signals are correlated; the correct geometry is covariance-adjusted.

**Key techniques**

- GLS
- Mahalanobis distance
- Whitening
- Covariance metric

**Topics to revisit**

- Why GLS uses `\Sigma^{-1}`
- Mahalanobis distance as covariance-scaled distance
- Whitening and decorrelation
- Relation to OLS under spherical errors

### Part C. Kalman Gain as Covariance Weighting ⭐⭐⭐⭐⭐

Status: Started via `T004`, but worth revisiting as part of the same family.

**Core idea**

Kalman filtering is dynamic covariance-weighted signal combination.

**Key techniques**

- Gaussian conditioning
- Innovation covariance
- Kalman gain
- Bayesian updating

**Topics to revisit**

- Why `K = PH^\top (HPH^\top + R)^{-1}`
- Why gain entries can be negative
- Relation to static GLS / IV weighting
- Innovation-space versus state-space geometry

### Part D. Mean-Variance and Projection Under Covariance ⭐⭐⭐⭐

**Core idea**

Portfolio construction also combines signals under a covariance metric rather than Euclidean geometry.

**Key techniques**

- Mean-variance optimization
- Quadratic forms
- Projection
- Shadow prices

**Topics to revisit**

- Relation between `Q^{-1}q` and `\Sigma^{-1}\mu`
- Projection under covariance metric
- Constraints as signal adjustment
- Connection to factor neutralization

## October 8 Interview Knowledge Gaps

Source: [2026-10-08 Daily Interview Test](DailyTests/2026-10-08.md). Status: Open review items; explanations received, independent retrieval not yet verified. These are gap notes, not new finalized subject notes.

| Question / result | Future-review tags | Gap and next retrieval check |
| --- | --- | --- |
| [Q1 — M/P](DailyTests/2026-10-08.md#q1--dependency-ordering) · [C008 — Dependency Ordering and DAG Scheduling](Questions/Coding/C008_Dependency_Ordering_and_DAG_Scheduling.md) | `graph`, `topological-sort` | Model prerequisites as directed edges; implement indegrees / zero-indegree queue, explain cycle detection and O(V+E) complexity. |
| [Q2 — P/Y](DailyTests/2026-10-08.md#q2--hh-versus-ht-waiting-times) · [P023 — Coin Pattern Waiting Times](Questions/Probability/P023_Coin_Pattern_Waiting_Times.md) | `absorbing-markov-chains`, `state-recursion` | Choose useful suffix states; derive HH = 6 and HT = 4, then recover t = (I-Q) inverse times ones. Connect to [P019](Questions/Probability/P019_HH_vs_HTT_Pattern_Race.md), distinguishing waiting time from race probability. |
| [Q3 — P/M](DailyTests/2026-10-08.md#q3--exponential-mle-and-fisher-information) · [S011 — Exponential MLE and Fisher Information](Questions/Statistics/S011_Exponential_MLE_and_Fisher_Information.md) | `mle`, `fisher-information`, `asymptotic-se` | Derive the exponential rate MLE, define score and expected information, distinguish per-observation from total information, and obtain plug-in SE. Explain regularity and asymptotic versus exact variance. |
| [Q4 — P/Y](DailyTests/2026-10-08.md#q4--minimize-the-largest-group-sum) · [C009 — Minimize Maximum Contiguous Group Sum](Questions/Coding/C009_Minimize_Maximum_Contiguous_Group_Sum.md) | `binary-search-on-answer` | Recognize minimize-maximum + monotone feasibility; prove greedy uses the fewest groups for a fixed limit on positive inputs, then implement first-feasible binary search. |
| [Q7 — Y](DailyTests/2026-10-08.md#q7--projection-matrices-and-psd) · [L007 — Projection Matrices, Eigenvalues, and Rank](Questions/LinearAlgebra/L007_Projection_Matrices_Eigenvalues_and_Rank.md) | `projection-matrices` | Use symmetry plus idempotence to prove the quadratic form equals the squared norm of Px; distinguish PSD from PD and explain why zero is allowed. |

Secondary review: [Q8](DailyTests/2026-10-08.md#q8--paired-strategy-return-test) · [S012 — Paired Return Tests and Dependence](Questions/Statistics/S012_Paired_Return_Tests_and_Dependence.md), positive same-day covariance reduces the variance of differences at fixed marginal variances; serial dependence requires separate treatment. Q5–Q8 were completed in **5 minutes total**. Preserve the broader, harder coverage relative to October 6–7 while scheduling targeted retests.

## October 9 Interview Knowledge Gaps

Accidental repeats are retained for auditability but excluded from new-coverage counts. Original Q4, Q8, and Q9 were accidental repeats; original Q3 was removed before an attempt and replaced.

| Question / result | Future-review tags | Gap and next retrieval check |
| --- | --- | --- |
| [Q1 — P/Y](DailyTests/2026-10-09.md#q1--dag-scheduling-with-durations) · [C008 — Dependency Ordering and DAG Scheduling](Questions/Coding/C008_Dependency_Ordering_and_DAG_Scheduling.md) | `dag-dp`, `earliest-finish`, `topological-sort` | Keep Kahn BFS; propagate maximum parent finish time, enqueue only at indegree zero, and detect cycles with processed count. Intentional revisit of October 8 Q1. |
| [Q2 — Y/G](DailyTests/2026-10-09.md#q2--expected-waiting-time-for-hth) · [P023 — Coin Pattern Waiting Times](Questions/Probability/P023_Coin_Pattern_Waiting_Times.md) | `state-recursion`, `pattern-waiting-time`, `self-overlap` | Preserve the correct suffix states and audit every transition, especially fallback from HT on T. |
| [Q3 replacement — Y](DailyTests/2026-10-09.md#q3--one-sided-z-test-with-known-variance) · [S013 — One-Sided Normal Mean Test](Questions/Statistics/S013_One_Sided_Normal_Mean_Test.md) | `sampling-distribution`, `one-sided-z-test`, `hypothesis-testing` | Write the sample-mean distribution first; known variance implies z, and `mu > 0` implies a right-tail rejection region. |
| [Q4 replacement — G](DailyTests/2026-10-09.md#q4--original-repeat-and-kth-largest-replacement) · [C010 — Kth Largest: Heap and Quickselect](Questions/Coding/C010_Kth_Largest_Heap_and_Quickselect.md) | `min-heap`, `quickselect`, `off-by-one` | Keep exactly k heap elements using `< k`; reproduce Quickselect as the expected-O(n) follow-up. |
| [Q5 — P/Y](DailyTests/2026-10-09.md#q5--time-series-validation-and-ridge) · [T007 — Random Forest Rates Signals and Time-Series Validation](Questions/TimeSeries/T007_Random_Forest_Rates_Signals_and_Time_Series_Validation.md) | `time-series-validation`, `ridge`, `multicollinearity` | Name temporal leakage, regime shift, and serial / overlapping dependence concretely; explain Ridge as variance reduction and coefficient stabilization. |
| [Q6(a) — M/P](DailyTests/2026-10-09.md#q6--competing-poisson-processes) · [SC006 — Competing Exponentials and Time-Dependent Hazards](Questions/StochasticCalculus/SC006_Competing_Exponentials_and_Time_Dependent_Hazards.md) | `poisson-superposition`, `merged-process-labels`, `erlang` | Use A/B labels in the merged process; do not model the second arrival as exponential. |
| [Q7 — Y](DailyTests/2026-10-09.md#q7--projection-matrix) · [L007 — Projection Matrices, Eigenvalues, and Rank](Questions/LinearAlgebra/L007_Projection_Matrices_Eigenvalues_and_Rank.md) | `projection-rank`, `column-space`, `eigenvalue-multiplicity` | Rank equals the dimension of the projected subspace; connect rank / trace to the number of eigenvalue ones. Intentional revisit of October 8 Q7. |

Repeat-control rule for future drills: compare candidate questions against the previous **2–3 Daily Stress Tests** by solution pattern. A documented weak spot may be deliberately repeated only when labeled **intentional spaced repetition**; otherwise replace it and do not count it as new coverage.

## A/B Testing — Review To-Do

Source: [October 10–11 Q3](DailyTests/2026-10-10.md#q3--exact-randomization-and-ab-testing) · [S014 — Exact Randomization and A/B Testing](Questions/Statistics/S014_Exact_Randomization_and_AB_Testing.md). **Miss / K**, explicitly confirmed by the user; detailed review requested. Explanations received afterward; independent mastery unverified.

- [ ] Experimental design: random assignment, treatment/control groups, randomization units, and interference.
- [ ] Potential outcomes, individual and average treatment effects, and difference-in-means estimation.
- [ ] Sharp null versus zero-average-effect null.
- [ ] Exact randomization tests: assignment distributions, two-sided p-values, and ties.
- [ ] When to use randomization tests, Welch t tests, or two-proportion tests; assumptions and limitations.
- [ ] Confidence intervals, effect size, and statistical versus practical significance.
- [ ] Power, minimum detectable effect, and sample-size planning.
- [ ] Prespecified metrics, multiple testing, and repeated peeking / optional stopping.
- [ ] Practice a small exact randomization example and an end-to-end A/B test design.

## October 10–11 Interview Review Priorities

Source: [eight-question Survival Mode drill](DailyTests/2026-10-10.md). User requested keeping the broader coverage despite many unfamiliar or unretrieved ideas. K = knowledge, R = retrieval, I = implementation; do not force K/R classification where prior familiarity was not established.

Question references: [Q1 / C011](Questions/Coding/C011_Incremental_Connectivity_and_Connected_Pairs.md) · [Q2 / P025](Questions/Probability/P025_Permutation_Fixed_Points_and_Dependent_Indicators.md) · [Q3 / S014](Questions/Statistics/S014_Exact_Randomization_and_AB_Testing.md) · [Q4 / C012](Questions/Coding/C012_Edit_Distance.md) · [Q5 / T008](Questions/TimeSeries/T008_Tree_Extrapolation_and_Deployment.md) · [Q6 / P026](Questions/Probability/P026_Finite_Horizon_Optimal_Stopping.md) · [Q7 / S015](Questions/Statistics/S015_Interaction_and_Recentering.md) · [Q8 / O009](Questions/Optimization/O009_Gradient_Descent_and_Spectral_Contraction.md).

| Question | Status and next independent check |
| --- | --- |
| Q1 — connectivity / DSU | Partial / Hinted; I plus unresolved K/R. Maintain global pair count; union roots unconditionally when different; compare component sizes, not root IDs; explain path halving. Initial attempt 12 min. |
| Q2 — derangements / indicators | Partial / Hinted; R/K. Complete inclusion-exclusion through k=6; explain expectation linearity without independence and derive pair covariance. Initial 9 min covered only part 1; conditional-expectation identity independently proposed later. |
| Q3 — randomization / A-B | Miss / K, user-confirmed. Follow the A/B checklist above; distinguish assignment-based exactness from normal/sample-variance reasoning and sharp from weak nulls. |
| Q4 — edit distance | Partial / Hinted; state setup prompted, I in dimensions/bounds/transitions/return. Rebuild from prefix-length state; handle empty strings. DP direction and boundaries were independently correct. |
| Q5 — extrapolation | Partial / Hinted. Tree limitation and OLS were independent; test on the deployment feature range and evaluate test rather than training error. |
| Q6 — optimal stopping | Partial / Hinted. Reconstruct backward induction, remaining option value, net cost, conditional mean, and probabilities of reaching each draw. |
| Q7 — recentering | Partial. Correct slope and invariant fit; fix Z=W+10 substitution and variance of a coefficient combination. The user correctly understood that old/new coefficient-zero tests are different hypotheses. |
| Q8 — gradient descent | Miss / K. Begin with negative gradient and one-dimensional quadratic stability; then eigen-direction multipliers and minimax step size. Three minutes was a retrieval budget, not a reasonable first-learning budget. |

- [ ] Gradient-descent foundations: local linear approximation, step-size overshoot, and the quadratic gradient.
- [ ] Re-derive the strict stability bound from absolute multiplier less than one; distinguish an upper bound from a selected step.
- [ ] Explain why the best worst-direction contraction balances a decreasing and an increasing endpoint magnitude.
- [ ] Retest selected misses after review, explicitly labeled intentional spaced repetition; continue new structures in other slots.

No final independently verified rewrite was submitted for Q1 or Q4. Do not mark these skills mastered based only on supplied solutions or acknowledgments. Keep the A/B checklist open; the session did not complete that review curriculum.

## Time-Series Fitting — Review To-Do

Requested October 12 during [Q5 of the make-up drill](DailyTests/2026-10-11.md#q5--ma1-equivalence-invertibility-and-fitting) · [T009 — MA(1) Equivalence, Invertibility, and Fitting](Questions/TimeSeries/T009_MA1_Equivalence_Invertibility_and_Fitting.md). Review remains open; explanations received are not independent mastery.

- [ ] MA(1) moment estimation: sample variance and lag-one autocovariance, invertible root, innovation variance.
- [ ] Gaussian maximum likelihood with unobserved innovations and observation covariance.
- [ ] Conditional versus exact likelihood: initialization, pre-sample shocks, state-space / Kalman methods.
- [ ] Stationarity, invertibility, and identifiability; equivalent representations and stable innovation reconstruction.
- [ ] AR/ARMA fitting: OLS applicability, likelihood estimation, parameter constraints, residual diagnostics.
- [ ] Runnable Python fitting exercise; independently explain estimates and residual autocorrelation.

## Pending Drill and Workload Preference — October 12

- [x] Resume [Q7 — confidence versus prediction intervals](DailyTests/2026-10-11.md#q7--confidence-vs-prediction-intervals) · [S017 — Confidence and Prediction Intervals](Questions/Statistics/S017_Confidence_and_Prediction_Intervals.md): guided review October 13; independent mastery not yet checked.
- [x] Resume [Q8 — conditioning and least squares](DailyTests/2026-10-11.md#q8--conditioning-and-least-squares) · [L008 — Conditioning and Least Squares](Questions/LinearAlgebra/L008_Conditioning_and_Least_Squares.md): guided review October 13; independent mastery not yet checked.
- Both are now Partial / Hinted following the October 13 guided continuation. New drills: 4–5 questions, 30–40 minutes; mainly core interview material, at most one stretch question. Keep breadth and repeat checks, but reduce simultaneous new-foundation teaching.

## October 13 Follow-Up Review

- [ ] Independently derive mean confidence and new-observation prediction intervals, including slope-error representation, zero covariance, t pivot, and added observation-noise term.
- [ ] Explain fixed-design response variance versus estimator variance versus repeated-sampling prediction-error variance; explain which model risks interval formulas omit.
- [ ] Revisit the [SVD / QR / conditioning / PCA card](KnowledgeCards/LinearAlgebra/SVD_QR_Conditioning_Least_Squares_and_PCA.md): dimensions, eigenvalues versus singular values, normal equations, stable least squares, and right singular vectors.
- [ ] Run PCA/SVD/QR examples and reproduce projection and explained-variance calculations without supplied code.

## October 13 Survival Drill — Pending Items and Review

Source: [October 13 session, continued October 14](DailyTests/2026-10-13.md). All five main questions Partial / Hinted. Q4 is reviewed; Q5's cost-sensitive decision/recalibration follow-up **Pending, not Miss**. Actual times unknown. Latest explicit workload request is 4–6 substantive questions and 45–60 minutes initial solving; this supersedes the earlier 30–40-minute preference for new drills.

Question references: [Q1 / C015](Questions/Coding/C015_Arithmetic_Expressions_and_Nested_State.md) · [Q2 / P029](Questions/Probability/P029_Random_Inspection_and_Residual_Wait.md) · [Q3 / P030](Questions/Probability/P030_Product_Distribution_and_Event_Conditioning.md) · [Q4 / S018](Questions/Statistics/S018_Ratio_of_Means_Inference.md) · [Q5 / T010](Questions/TimeSeries/T010_Deployment_Probabilities_and_Decisions.md).

- [x] Resume [Q4](DailyTests/2026-10-13.md#q4--ratio-of-means-inference) · [S018 — Ratio-of-Means Inference](Questions/Statistics/S018_Ratio_of_Means_Inference.md), original 11-minute budget. Guided CLT/Slutsky, standard error, confidence interval, counterexample, and denominator-risk review completed October 14; later cold retrieval remains open.
- [ ] Finish [Q5's decision/recalibration follow-up](DailyTests/2026-10-13.md#q5--deployment-probabilities-and-decisions) · [T010 — Deployment Probabilities and Decisions](Questions/TimeSeries/T010_Deployment_Probabilities_and_Decisions.md). Main Bayes/odds probability question reviewed October 14; original combined budget 8 minutes, actual time unknown. No solution or hint supplied for the decision follow-up.
- [x] Q1 user rewrite: apply whitespace pointer advancement, digit-to-int conversion, and continue after reading a number. User explicitly confirmed completion during recording. Assistant verified the corresponding minimal repair; final exact user submission not re-read.
- [ ] Q1 later cold retest: stack invariant, unary/binary signs, pointer movement, nested and whitespace tests. Original multiplication follow-up remains unattempted.
- [ ] Q2 later retest: random-time length bias plus conditional residual position. First probability, mean (4.5 typo clarified), and completion-start follow-up were independently correct.
- [ ] Q3 later retest: clipped integration bounds, event-weighted moment numerator divided by event probability, and conditional dependence/covariance. Reversed inequality was a reading slip. User's u-first integration order and numerator 1/8 were correct by clarification; do not misrecord them as errors.

Resume Q5's pending follow-up before replacing it with another full set unless instructed otherwise. Near-term Q1–Q5 retests must be explicitly labeled intentional spaced repetition; guided completion is not Cold Solve.

## October 14 Follow-Up Review

- [ ] Q4: independently reconstruct W_i=X_i-rY_i, centered CLT, denominator convergence, and Slutsky scaling.
- [ ] Q4: distinguish the variance of the limiting sqrt(n) fluctuation from the estimator's approximate variance; derive the paired residual plug-in SE and asymptotic CI.
- [ ] Q4: reproduce the Uniform(1,3) mean-of-ratios counterexample, including density normalization and the reciprocal of the mean; explain integrability requirements and denominator-relative uncertainty.
- [ ] Q5: distinguish prior, likelihood, posterior, probability, and odds; independently derive label-shift adjustment and convert odds back to probability.
- [ ] Q5: attempt the original cost-sensitive decision/recalibration follow-up without an initial solution. It remains Pending, not Miss.

All seven dated DailyTests were audited October 14 for mathematical content and GitHub rendering. Blocked macros and Markdown-consumed TeX escapes were repaired; the checker and Pages renderer now support protected math syntax. Historical attempts, typo clarifications, scores, and recorded times are preserved.

## October 14 Interview Session — Evidence and Spaced Review

Source: [October 14 session](DailyTests/2026-10-14.md). All actual times unknown. Initial solving/review discussed; dedicated reading block and final independent reproduction **Pending**.

Question references: [R1 / P025](Questions/Probability/P025_Permutation_Fixed_Points_and_Dependent_Indicators.md) · [R2 / P029](Questions/Probability/P029_Random_Inspection_and_Residual_Wait.md) · [Q1 / C011](Questions/Coding/C011_Incremental_Connectivity_and_Connected_Pairs.md) · [Q2 / S019](Questions/Statistics/S019_Weighted_Common_Mean_Inference.md) · [Q3 / T007](Questions/TimeSeries/T007_Random_Forest_Rates_Signals_and_Time_Series_Validation.md).

- [ ] **Priority: R1**, intentional spaced repetition of October 10–11 Q2. Review [indicator cookbook](KnowledgeCards/Probability/Indicator_Random_Variables_Cookbook.md), then independently reconstruct fixed-point indicators, marginal/joint probabilities, covariance and variance. Generic setup needed assistance; K/R unresolved. This is the ONE selected focused gap.
- R2: user reports independently solving the residual-service question before seeing the answer. Exact working not submitted, timing unverified. Supersedes initial Partial / Hinted classification; do not invent a fresh gap or treat it as a Miss.
- Q1: independent DSU structure and pair-count identity recovered. Root-link typo explicitly clarified and corrected submission verified by assistant tests, including 1,000 randomized comparisons. Do not treat typo as conceptual DSU failure or leave the code unverified. Overall Partial / Hinted because complexity required assistance.
- [ ] Q1 later independent check: distinguish node count from edge count, amortized inverse-Ackermann find cost from single-call worst case, and auxiliary from output space. K/R unresolved; no substantive implementation gap established by the typo.
- [ ] Q2 later intentional spaced repetition: derive weighted residual scale estimate, mean-estimator SE and exact t pivot; prove optimality and justify degrees of freedom/independence. Weights and minimum variance were independent; notation ambiguity is not an error. Numerical part was supplied, not independently submitted.
- [ ] Q3 later intentional spaced repetition: specify training/refit/selection/final-test chronology and fit preprocessing only on available training data. Valid discussion of optional standardization for flags and model dependence is preserved. Lag features can be standardized with training-fitted parameters; blanket rejection of lag scaling was clarified. K/R unresolved.
- Q3 held-out test reasoning independently correct after English wording clarification; no knowledge gap from translation. Distribution shift/overfit/regime concerns independently correct. Replacement Q3 repeated older validation patterns without advance repetition labeling; exclude from new coverage.
- Original ratio-of-means and deployment-probability prompts were withdrawn at user request as just completed elsewhere. Preserve the existing October 13/14 continuation and its pending decision follow-up; do not score these as fresh failures.

Future near-term retests must name the originating date/item and be labeled **intentional spaced repetition**. The format at that time was two retrieval checks or one derivation, only 2–3 timed questions, at most one new structure (none each third completed session), one review gap with reading, then independent reproduction. **That format is superseded by the October 15–16 preference below.** Weekly 35/30/20/10/5 targets apply across sessions, not forced into every night. Pending work is not a Miss; no elapsed times inferred.

## October 15–16 Drill — Q4 Mastered, Evidence and Current Preferences

Source: [October 15 drill, continued October 16](DailyTests/2026-10-15.md). Q1–Q3 discussed; Q4 initially deferred and subsequently independently completed. This is one study set across the date boundary.

Question references: [Q1 / C016](Questions/Coding/C016_Median_of_Two_Sorted_Arrays.md) · [Q2 / P031](Questions/Probability/P031_Exact_Uniform_Sampling_from_a_Biased_Coin.md) · [Q3 / S020](Questions/Statistics/S020_Most_Powerful_Normal_Variance_Test.md) · [Q4 / L009](Questions/LinearAlgebra/L009_Feasible_Correlations_and_Zero_Variance_Portfolios.md).

- [x] **Q4 Mastered — correlation feasibility and zero-variance portfolios.** On October 16 the user confirmed an independent solve and understanding of PSD correlation matrices, determinant constraints, singular covariance matrices, null space and zero-variance portfolios. Correct range and endpoint portfolios are recorded with the unchanged original question in [L009 — Feasible Correlations and Zero-Variance Portfolios](Questions/LinearAlgebra/L009_Feasible_Correlations_and_Zero_Variance_Portfolios.md); dated mastery evidence remains in DailyTests. No additional review or remedial practice needed; remove Q4 from the pending queue.
- Q1: user independently chose partial merging, initial attempt approximately 22–23 minutes. Guided boundary repairs followed. Last exact submission still used floating-point division for an even midpoint: 1,194/1,224 small cases passed, with 30 slice-index exceptions. Assistant's one-line integer-midpoint fix passed all 1,224. Supplied binary-partition solution also passed all cases and input-mutation checks; independent reproduction remains unverified. I gap: ranks versus indices, suffix skip, loop bounds, preserving accumulated results and integer indices; K/R for partition search unresolved.
- Q2: independently constructed a valid rejection sampler using seven selected six-flip patterns with three heads and three tails, and gave the correct termination intuition. The 15-versus-20 count was explicitly a typo, not a combinatorics gap. Expected-cost reasoning omitted seven acceptable patterns and six raw flips per block; corrected with explanation. Full independent cost/independence derivation remains unverified; K/R unresolved.
- Q3: Neyman–Pearson / most-powerful testing explicitly new to the user: **K gap**, not retrieval failure. Full solution and conceptual explanations supplied. User reported emerging understanding; no independent derivation verified. Keep Partial / Hinted. Treat this as an intermediate-priority stretch extension; interview frequency of the lemma itself was not established. Do not treat the 11-minute familiar-topic budget as first-learning time.
- Original LRU-cache prompt: withdrawn as too engineering-oriented, answer supplied before attempt. Exclude from independent coverage and do not infer a gap or assign Miss.

**Current preferences, superseding older format instructions:**

- 4–5 high-quality English interview questions; genuinely new problems and solution patterns, not superficial variations. Review the latest 2–3 DailyTests and linked continuations before selection.
- No separate retrieval/review block; user handles revision. No initial hints or solutions. Give explanations/assessment after an attempt or when explicitly requested.
- Prefer coding centered on algorithms and reasoning over engineering-heavy data-structure implementation. Mainly core interview content, with at most one clearly labeled stretch question and realistic budgets; approximately 45–60 minutes planned initial solving.
- Maintain weekly Coding 35%, Probability 30%, Statistics 20%, ML/Time Series 10%, Linear Algebra/Optimization 5% across sessions. Planned budgets are not measured time. Q4 now contributes completed linear-algebra coverage; its actual duration remains unrecorded.
- Track Cold Solve / Partial / Hinted / Miss / Pending with evidence. Distinguish K/R/I only when supported; preserve typo clarifications and separate exact user submissions from assistant repairs or supplied solutions. Record actual time only when reported.
- Later retests of this session's Q1–Q3 must name the original item/date and be labeled intentional spaced repetition. Acknowledgment of an explanation is not independent mastery.


## October 17 Drill — Evidence and Focused Review

Source: [October 17 drill](DailyTests/2026-10-17.md). All four questions discussed; 54 minutes was the planned initial budget, not actual elapsed time. All actual times unknown. No Miss assigned; overall Partial / Hinted preserves independently correct subparts.

Question references: [Q1 / C017](Questions/Coding/C017_Minimum_Units_for_Overlapping_Tasks.md) · [Q2 / P032](Questions/Probability/P032_Cycles_of_a_Uniform_Random_Permutation.md) · [Q3 / S021](Questions/Statistics/S021_Uniform_Endpoint_Estimation_and_Exact_Bounds.md) · [Q4 / T011](Questions/TimeSeries/T011_Signal_Smoothing_Correlation_and_Trading_Costs.md).

- [ ] **Priority: Q1 heap state updates (I, user-confirmed).** Maintain one current `(end, unit_id)` entry per allocated unit. Distinguish peek, pop, push and replacement. Final exact user submission left stale entries and failed `[(0,1),(1,4),(2,3)]`, assigning all tasks to one unit. Conditional-pop repair supplied; final user rewrite and independent optimality / complexity explanation remain unverified. Core sorting / earliest-end algorithm was independent; do not label code unpracticed.
- [ ] Q2: independently count long cycles by choosing labels, arranging one cycle, and permuting the remainder. Uniform permutations do not give iid uniform cycle lengths conditioned on their sum. Part 1's uniform cycle-length distribution and chain proof were Cold Solve. User reports being able to do part 3 given part 2; no submitted derivation, no inferred asymptotics gap, and no longer Pending. Terminology clarifications are not conceptual failures; K/R for counting remains unresolved.
- [ ] Q3: independently reconstruct the variance scaling and exact upper-bound coverage calculation. Part 1's maximum CDF, mean integration and unbiased coefficient were Cold Solve. Correct variance of the maximum was submitted, but the estimator's squared scaling factor and the sample-mean variance sum needed correction. Exact upper bound, mean-based alternative and sufficiency were explained; acknowledged understanding is not independent mastery. K/R unresolved.
- Q4: after the shared-signal prompt, user supplied correct gross-return / turnover objectives and recognized the beta / cost trade-off. Correlation ranking versus cost-sensitive objective ranking was understood in discussion. Preserve original covariance expressions and `sqrt(s)` as clarified typos, not evidence of conceptual gaps. The threshold and detailed economic interpretation were supplied; no cold-mastery upgrade. Equal position variance does not imply equal P&L risk, and this objective is not Sharpe.

Any near-term revisit must be labeled **intentional spaced repetition** with October 17, the exact item and gap. Keep four to five fresh interview questions, no separate retrieval/review block, and weekly topic balance across sessions.

## October 18 Drill — Evidence and Focused Review

Source: [October 18 drill](DailyTests/2026-10-18.md). All four questions discussed, overall Partial / Hinted; 55 minutes planned, all actual times unknown. No main question Pending and no Miss assigned.

Question references: [Q1 / C018](Questions/Coding/C018_Maximum_Sum_Path_in_a_Tree.md) · [Q2 / P033](Questions/Probability/P033_Gaussian_Sign_Prediction_and_Conditional_Return.md) · [Q3 / S022](Questions/Statistics/S022_Duplicating_Regression_Observations.md) · [Q4 / P034](Questions/Probability/P034_First_Repeated_Label.md).

- [ ] **One focused check: Q1 tree-path states and reverse processing.** Distinguish the single branch that can attach to a parent from the complete best path anywhere in a subtree. The user articulated two state arrays; traversal and full reference algorithm were supplied. Code completed by user report, exact submission unverified, not unpracticed. Later independent explanation and submitted code remain open; no I gap inferred without a submission, K/R unresolved.
- Q2: geometry and conditional normalization guided; final win-rate versus expected-return interpretation independently correct. Later check half-plane intersection and the conditional event-probability denominator; do not infer unfamiliarity from the joint-density request alone.
- Q3: coefficients, RSS and R-squared independently correct. Preserve the user's clarification that ratio discrepancies were arithmetic and genuinely independent samples add information. Exact factors and explanation supplied, so overall remains Partial / Hinted; no additional conceptual K/R gap or remedial requirement established.
- Q4: direct counting independently structured correctly; final repeat factor is k minus one, not k. Do not invent a broad counting gap. Tail-sum method already known by user report; expectation question reflected uncertainty about further simplification, not inability to use that method. Collision-scale approximation guided; final rearrangement error alone is not a knowledge gap.

Near-term retests must name October 18, the item and the gap, and be labeled **intentional spaced repetition**. Keep code verification separate from self-reported practice, preserve arithmetic/wording clarifications, and do not add a dedicated review block.

## October 20 Drill, Continued October 21–22 — All Questions Discussed

Source: [October 20 drill, continued October 21–22](DailyTests/2026-10-20.md). Q1–Q4 **Partial / Hinted** overall, with independent subparts preserved; Q3 part 1 numerical answers/method Cold Solve, full moment working not submitted. One study set across all three dates. All four main questions discussed; none Pending. Planned initial solving: 54 minutes; all actual times Not recorded. No Miss assigned.

Question references: [Q1 / C019](Questions/Coding/C019_Shortest_Grid_Route_with_One_Blocked_Entry.md) · [Q2 / P035](Questions/Probability/P035_Shared_Unknown_Win_Probability_and_Predictive_Risk.md) · [Q3 / S023](Questions/Statistics/S023_Pooled_and_Within_Sector_Signal_Evaluation.md) · [Q4 / T012](Questions/TimeSeries/T012_Probability_Forecasts_Calibration_and_Evaluation.md).

- [x] Q2 part 3 discussed October 21: user supplied correct 320/63 after the covariance-sum setup was given. Conditional-on-P versus conditional-on-data independence, risk-engine variance 20/9, parameter-uncertainty intuition and Bayesian evaluation implications explained. Correct guided calculation, not a full independently submitted derivation. No longer Pending; K/R unresolved.
- [x] Q3 discussed October 21: pooled beta 3/10 and R-squared 9/40 independently correct; sector dummy wording clarified without scoring an error. Normal equations, within-sector demeaning / beta -1/2, total-covariance derivation and numeric omitted-variable shift 0.8 supplied on request. User correctly interpreted removal of sector means and rejected pooled positive beta as proof of within-sector value. Overall Partial / Hinted, no longer Pending; K/R unresolved.
- [x] **Q4 completed October 22.** A/B calibration, E[Y] = 0.6, A/B losses 0.24/0.15, identical classifications and the limitation of accuracy were independently identified. C's correct formula and arithmetic-error clarification preserved; corrected 0.1825 supplied. The 0.6 accuracy answer was clarified as a writing slip; 0.8 and calculation supplied. Overall Partial / Hinted, no new K/R/I gap established; no longer Pending.
- Q1: augmented-state analogy to weighted coupon shortest paths independently recognized; two distance grids proposed. FIFO operations, resource transition and visited-per-state logic guided. Exact submitted code has implementation errors (I); full BFS reference supplied on request, no corrected independent user submission. This is practiced but flawed code, not unpracticed work. Heap/pile terminology and the meaning of grid value 1 are clarifications, not conceptual failures.
- Q2 parts 1–2: likelihood independently correct; 3/4 is a valid MLE point estimate but not the requested posterior density. Bayes evidence denominator/density notation guided. User correctly evaluated the normalizer and predictive integrals after setup; conditional-on-P versus conditional-on-data independence and the two-win integral were supplied. K/R unresolved; numerical correction is separate from the independence assertion.
- Q3 follow-up: retain the distinction between the omitted-effect error term (which can correlate with X) and the fitted pooled OLS residual (orthogonal to X). The user's residual wording was refined; do not invent a fitted-residual misconception or a knowledge gap solely from requests for derivations. Pooled 0.3 is a correct projection coefficient; omitted-variable bias is relative to the within-sector target. Sector-allocation and stock-selection claims differ, and controlling for sector does not alone establish causality.
- Q4 discussion recorded: calibration versus information content; confident probability errors versus unchanged classifications; Brier/log loss, calibration bins with sample counts/uncertainty, chronological out-of-sample evaluation and fixed-policy decision backtests. Probability-bin hit-rate curves are calibration diagnostics; threshold-versus-selected-hit-rate curves measure screening behavior. These requested explanations are not evidence of independent derivation or a new knowledge gap. Questions about population loss, n observations, cutoff meaning and known group membership were setup clarifications.
- [ ] One later focused check: Q1 FIFO and state-specific discovery/update implementation. Reproduce without reference and submit code; retain the user's no-separate-retrieval-block preference. This outstanding independent check does not reopen the completed main-question queue.

The user initially stopped October 20 after Q2 parts 1–2, continued October 21 through Q3, and finished Q4 plus practical discussion October 22. This supersedes all old Q2/Q3/Q4 Pending entries for this set. All four main questions are discussed; independent mastery of assisted portions is not established. Any near-term revisit must be labeled **intentional spaced repetition**, naming October 20 (including the October 21–22 continuations), the item and the specific gap. Do not add Q4 remediation based on clarified arithmetic/writing or terminology. No elapsed time inferred; no reminder requested or scheduled.

## October 23 Drill — Paused After Q2, Archived October 24

Source: [October 23 session](DailyTests/2026-10-23.md). **Next session: continue Q3, then Q4.** Q1 and Q2 are discussed, both Partial / Hinted. Q3 and Q4 remain Pending, not Miss, with no hints or solutions supplied. User requested continuing tomorrow; no reminder was requested or created. Actual elapsed times are not recorded.

- [C020 / Q1](Questions/Coding/C020_Minimum_Deletions_for_a_Strictly_Increasing_Subsequence.md): retention/LIS reframing, equal-length ending dominance, tails ordering and lower-bound update were explained. The user then independently wrote correct code; exact submission passed seven edge cases, 5,000 seeded DP-oracle comparisons, input preservation and three 200,000-element cases. No I error observed. Independent state discovery/proof remains unverified, K/R unresolved. Do not label the code unsubmitted or unpracticed.
- [P036 / Q2](Questions/Probability/P036_Live_Orders_with_Poisson_Arrivals_and_Exponential_Lifetimes.md): correct intended arrival/survival model clarified. Conditional-count thinning, why the result is Poisson, old-survivor/new-arrival transition and long-run law supplied on request. No independent full derivation submitted, K/R unresolved. Do not score the clarified wording as a confirmed lifetime-sign or arrival-time misconception.
- [ ] Resume [S024 / Q3](Questions/Statistics/S024_Multiple_Testing_and_Independent_Confirmation.md), original 11-minute budget, without initial hints or solution.
- [ ] Then [O010 / Q4](Questions/Optimization/O010_Single_Asset_Position_with_Proportional_Trading_Costs.md), original 8-minute budget, without initial hints or solution.

Optional later focused check: independently reconstruct Q2's conditioning/thinning proof. Keep the user's no-separate-review-block preference; this is not automatically added to the next session. Any near-term Q1/Q2 retest must name October 23, the item and assisted step, and be labeled intentional spaced repetition.
