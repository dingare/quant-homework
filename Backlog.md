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

- [ ] Experimental design: random assignment, treatment/control groups, randomization units, and interference.
- [ ] Potential outcomes, individual and average treatment effects, and difference-in-means estimation.
- [ ] Sharp null versus zero-average-effect null.
- [ ] Exact randomization tests: assignment distributions, two-sided p-values, and ties.
- [ ] When to use randomization tests, Welch t tests, or two-proportion tests; assumptions and limitations.
- [ ] Confidence intervals, effect size, and statistical versus practical significance.
- [ ] Power, minimum detectable effect, and sample-size planning.
- [ ] Prespecified metrics, multiple testing, and repeated peeking / optional stopping.
- [ ] Practice a small exact randomization example and an end-to-end A/B test design.
