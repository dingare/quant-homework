# Backlog

Unfinished topics and future note clusters.

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
