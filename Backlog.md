# Backlog

Unfinished topics and future note clusters.

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
| [Q1 — M/P](DailyTests/2026-10-08.md#q1--dependency-ordering) | `graph`, `topological-sort` | Model prerequisites as directed edges; implement indegrees / zero-indegree queue, explain cycle detection and O(V+E) complexity. |
| [Q2 — P/Y](DailyTests/2026-10-08.md#q2--hh-versus-ht-waiting-times) | `absorbing-markov-chains`, `state-recursion` | Choose useful suffix states; derive HH = 6 and HT = 4, then recover t = (I-Q) inverse times ones. Connect to [P019](Questions/Probability/P019_HH_vs_HTT_Pattern_Race.md), distinguishing waiting time from race probability. |
| [Q3 — P/M](DailyTests/2026-10-08.md#q3--exponential-mle-and-fisher-information) | `mle`, `fisher-information`, `asymptotic-se` | Derive the exponential rate MLE, define score and expected information, distinguish per-observation from total information, and obtain plug-in SE. Explain regularity and asymptotic versus exact variance. |
| [Q4 — P/Y](DailyTests/2026-10-08.md#q4--minimize-the-largest-group-sum) | `binary-search-on-answer` | Recognize minimize-maximum + monotone feasibility; prove greedy uses the fewest groups for a fixed limit on positive inputs, then implement first-feasible binary search. |
| [Q7 — Y](DailyTests/2026-10-08.md#q7--projection-matrices-and-psd) | `projection-matrices` | Use symmetry plus idempotence to prove the quadratic form equals the squared norm of Px; distinguish PSD from PD and explain why zero is allowed. |

Secondary review: [Q8](DailyTests/2026-10-08.md#q8--paired-strategy-return-test), positive same-day covariance reduces the variance of differences at fixed marginal variances; serial dependence requires separate treatment. Q5–Q8 were completed in **5 minutes total**. Preserve the broader, harder coverage relative to October 6–7 while scheduling targeted retests.

## October 9 Interview Knowledge Gaps

Accidental repeats are retained for auditability but excluded from new-coverage counts. Original Q4, Q8, and Q9 were accidental repeats; original Q3 was removed before an attempt and replaced.

| Question / result | Future-review tags | Gap and next retrieval check |
| --- | --- | --- |
| [Q1 — P/Y](DailyTests/2026-10-09.md#q1--dag-scheduling-with-durations) | `dag-dp`, `earliest-finish`, `topological-sort` | Keep Kahn BFS; propagate maximum parent finish time, enqueue only at indegree zero, and detect cycles with processed count. Intentional revisit of October 8 Q1. |
| [Q2 — Y/G](DailyTests/2026-10-09.md#q2--expected-waiting-time-for-hth) | `state-recursion`, `pattern-waiting-time`, `self-overlap` | Preserve the correct suffix states and audit every transition, especially fallback from HT on T. |
| [Q3 replacement — Y](DailyTests/2026-10-09.md#q3--one-sided-z-test-with-known-variance) | `sampling-distribution`, `one-sided-z-test`, `hypothesis-testing` | Write the sample-mean distribution first; known variance implies z, and `mu > 0` implies a right-tail rejection region. |
| [Q4 replacement — G](DailyTests/2026-10-09.md#q4--original-repeat-and-kth-largest-replacement) | `min-heap`, `quickselect`, `off-by-one` | Keep exactly k heap elements using `< k`; reproduce Quickselect as the expected-O(n) follow-up. |
| [Q5 — P/Y](DailyTests/2026-10-09.md#q5--time-series-validation-and-ridge) | `time-series-validation`, `ridge`, `multicollinearity` | Name temporal leakage, regime shift, and serial / overlapping dependence concretely; explain Ridge as variance reduction and coefficient stabilization. |
| [Q6(a) — M/P](DailyTests/2026-10-09.md#q6--competing-poisson-processes) | `poisson-superposition`, `merged-process-labels`, `erlang` | Use A/B labels in the merged process; do not model the second arrival as exponential. |
| [Q7 — Y](DailyTests/2026-10-09.md#q7--projection-matrix) | `projection-rank`, `column-space`, `eigenvalue-multiplicity` | Rank equals the dimension of the projected subspace; connect rank / trace to the number of eigenvalue ones. Intentional revisit of October 8 Q7. |

Repeat-control rule for future drills: compare candidate questions against the previous **2–3 Daily Stress Tests** by solution pattern. A documented weak spot may be deliberately repeated only when labeled **intentional spaced repetition**; otherwise replace it and do not count it as new coverage.

## A/B Testing — Review To-Do

Source: [October 10–11 Q3](DailyTests/2026-10-10.md#q3--exact-randomization-and-ab-testing). **Miss / K**, explicitly confirmed by the user; detailed review requested. Explanations received afterward; independent mastery unverified.

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

Requested October 12 during [Q5 of the make-up drill](DailyTests/2026-10-11.md#q5--ma1-equivalence-invertibility-and-fitting). Review remains open; explanations received are not independent mastery.

- [ ] MA(1) moment estimation: sample variance and lag-one autocovariance, invertible root, innovation variance.
- [ ] Gaussian maximum likelihood with unobserved innovations and observation covariance.
- [ ] Conditional versus exact likelihood: initialization, pre-sample shocks, state-space / Kalman methods.
- [ ] Stationarity, invertibility, and identifiability; equivalent representations and stable innovation reconstruction.
- [ ] AR/ARMA fitting: OLS applicability, likelihood estimation, parameter constraints, residual diagnostics.
- [ ] Runnable Python fitting exercise; independently explain estimates and residual autocorrelation.

## Pending Drill and Workload Preference — October 12

- [x] Resume [Q7 — confidence versus prediction intervals](DailyTests/2026-10-11.md#q7--confidence-vs-prediction-intervals): guided review October 13; independent mastery not yet checked.
- [x] Resume [Q8 — conditioning and least squares](DailyTests/2026-10-11.md#q8--conditioning-and-least-squares): guided review October 13; independent mastery not yet checked.
- Both are now Partial / Hinted following the October 13 guided continuation. New drills: 4–5 questions, 30–40 minutes; mainly core interview material, at most one stretch question. Keep breadth and repeat checks, but reduce simultaneous new-foundation teaching.

## October 13 Follow-Up Review

- [ ] Independently derive mean confidence and new-observation prediction intervals, including slope-error representation, zero covariance, t pivot, and added observation-noise term.
- [ ] Explain fixed-design response variance versus estimator variance versus repeated-sampling prediction-error variance; explain which model risks interval formulas omit.
- [ ] Revisit the [SVD / QR / conditioning / PCA card](KnowledgeCards/LinearAlgebra/SVD_QR_Conditioning_Least_Squares_and_PCA.md): dimensions, eigenvalues versus singular values, normal equations, stable least squares, and right singular vectors.
- [ ] Run PCA/SVD/QR examples and reproduce projection and explained-variance calculations without supplied code.

## October 13 Survival Drill — Pending Items and Review

Source: [October 13 session, continued October 14](DailyTests/2026-10-13.md). All five main questions Partial / Hinted. Q4 is reviewed; Q5's cost-sensitive decision/recalibration follow-up **Pending, not Miss**. Actual times unknown. Latest explicit workload request is 4–6 substantive questions and 45–60 minutes initial solving; this supersedes the earlier 30–40-minute preference for new drills.

- [x] Resume [Q4](DailyTests/2026-10-13.md#q4--ratio-of-means-inference), original 11-minute budget. Guided CLT/Slutsky, standard error, confidence interval, counterexample, and denominator-risk review completed October 14; later cold retrieval remains open.
- [ ] Finish [Q5's decision/recalibration follow-up](DailyTests/2026-10-13.md#q5--deployment-probabilities-and-decisions). Main Bayes/odds probability question reviewed October 14; original combined budget 8 minutes, actual time unknown. No solution or hint supplied for the decision follow-up.
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

- [x] **Q4 Mastered — correlation feasibility and zero-variance portfolios.** On October 16 the user confirmed an independent solve and understanding of PSD correlation matrices, determinant constraints, singular covariance matrices, null space and zero-variance portfolios. Correct range and endpoint portfolios are recorded with the unchanged original question in the daily record. No additional review or remedial practice needed; remove Q4 from the pending queue.
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

- [ ] **Priority: Q1 heap state updates (I, user-confirmed).** Maintain one current `(end, unit_id)` entry per allocated unit. Distinguish peek, pop, push and replacement. Final exact user submission left stale entries and failed `[(0,1),(1,4),(2,3)]`, assigning all tasks to one unit. Conditional-pop repair supplied; final user rewrite and independent optimality / complexity explanation remain unverified. Core sorting / earliest-end algorithm was independent; do not label code unpracticed.
- [ ] Q2: independently count long cycles by choosing labels, arranging one cycle, and permuting the remainder. Uniform permutations do not give iid uniform cycle lengths conditioned on their sum. Part 1's uniform cycle-length distribution and chain proof were Cold Solve. User reports being able to do part 3 given part 2; no submitted derivation, no inferred asymptotics gap, and no longer Pending. Terminology clarifications are not conceptual failures; K/R for counting remains unresolved.
- [ ] Q3: independently reconstruct the variance scaling and exact upper-bound coverage calculation. Part 1's maximum CDF, mean integration and unbiased coefficient were Cold Solve. Correct variance of the maximum was submitted, but the estimator's squared scaling factor and the sample-mean variance sum needed correction. Exact upper bound, mean-based alternative and sufficiency were explained; acknowledged understanding is not independent mastery. K/R unresolved.
- Q4: after the shared-signal prompt, user supplied correct gross-return / turnover objectives and recognized the beta / cost trade-off. Correlation ranking versus cost-sensitive objective ranking was understood in discussion. Preserve original covariance expressions and `sqrt(s)` as clarified typos, not evidence of conceptual gaps. The threshold and detailed economic interpretation were supplied; no cold-mastery upgrade. Equal position variance does not imply equal P&L risk, and this objective is not Sharpe.

Any near-term revisit must be labeled **intentional spaced repetition** with October 17, the exact item and gap. Keep four to five fresh interview questions, no separate retrieval/review block, and weekly topic balance across sessions.

## October 18 Drill — Evidence and Focused Review

Source: [October 18 drill](DailyTests/2026-10-18.md). All four questions discussed, overall Partial / Hinted; 55 minutes planned, all actual times unknown. No main question Pending and no Miss assigned.

- [ ] **One focused check: Q1 tree-path states and reverse processing.** Distinguish the single branch that can attach to a parent from the complete best path anywhere in a subtree. The user articulated two state arrays; traversal and full reference algorithm were supplied. Code completed by user report, exact submission unverified, not unpracticed. Later independent explanation and submitted code remain open; no I gap inferred without a submission, K/R unresolved.
- Q2: geometry and conditional normalization guided; final win-rate versus expected-return interpretation independently correct. Later check half-plane intersection and the conditional event-probability denominator; do not infer unfamiliarity from the joint-density request alone.
- Q3: coefficients, RSS and R-squared independently correct. Preserve the user's clarification that ratio discrepancies were arithmetic and genuinely independent samples add information. Exact factors and explanation supplied, so overall remains Partial / Hinted; no additional conceptual K/R gap or remedial requirement established.
- Q4: direct counting independently structured correctly; final repeat factor is k minus one, not k. Do not invent a broad counting gap. Tail-sum method already known by user report; expectation question reflected uncertainty about further simplification, not inability to use that method. Collision-scale approximation guided; final rearrangement error alone is not a knowledge gap.

Near-term retests must name October 18, the item and the gap, and be labeled **intentional spaced repetition**. Keep code verification separate from self-reported practice, preserve arithmetic/wording clarifications, and do not add a dedicated review block.

## October 20 Drill — Stopped with Original Questions Preserved

Source: [October 20 drill](DailyTests/2026-10-20.md). Q1 and Q2 parts 1–2 **Partial / Hinted**. Planned initial solving: 54 minutes; all actual times Not recorded. No Miss assigned.

- [ ] **Resume Q2 part 3 first:** conditional variance of wins in the next ten trades versus an independent-trade risk engine. Original prompt preserved; no attempt, hint or solution for part 3 supplied.
- [ ] **Then Q3:** pooled versus within-sector regression and stock-selection interpretation. Pending, original full prompt retained, no hints or solution supplied.
- [ ] **Then Q4:** calibrated probability forecasts, squared probability loss and cutoff accuracy. Pending, original full prompt retained, no hints or solution supplied.
- Q1: augmented-state analogy to weighted coupon shortest paths independently recognized; two distance grids proposed. FIFO operations, resource transition and visited-per-state logic guided. Exact submitted code has implementation errors (I); full BFS reference supplied on request, no corrected independent user submission. This is practiced but flawed code, not unpracticed work. Heap/pile terminology and the meaning of grid value 1 are clarifications, not conceptual failures.
- Q2 parts 1–2: likelihood independently correct; 3/4 is a valid MLE point estimate but not the requested posterior density. Bayes evidence denominator/density notation guided. User correctly evaluated the normalizer and predictive integrals after setup; conditional-on-P versus conditional-on-data independence and the two-win integral were supplied. K/R unresolved; numerical correction is separate from the independence assertion.
- [ ] One later focused check: Q1 FIFO and state-specific discovery/update implementation. Reproduce without reference and submit code; do not interrupt the pending questions with a separate retrieval block.

The user asked to stop for now and preserve the remaining questions. Continue this set from Q2 part 3 before proposing a replacement set unless instructed otherwise. Any near-term revisit of completed parts must be labeled **intentional spaced repetition**, naming October 20, the item and the specific gap. Pending work is not a Miss; no elapsed time inferred.
