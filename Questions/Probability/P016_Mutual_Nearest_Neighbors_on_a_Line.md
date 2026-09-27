# P016 — Mutual Nearest Neighbors on a Line

## Problem

Model 100 cars as points with independent $\mathrm{Uniform}(0,1)$ positions on a
straight line segment. The endpoints are not cars, and distances are ordinary
absolute differences, with no wraparound. For car $i$, let $N(i)$ denote the
nearest other car. Coincident positions and distance ties have probability zero.
Let

$$
M=\sum_{i=1}^{100}\mathbf1\{N(N(i))=i\}
$$

count the cars belonging to mutual-nearest-neighbor pairs; each pair contributes
two cars.

1. Write a simulation algorithm and use repeated trials to estimate $E[M]$.
2. Identify and justify an efficient computational approach. Exploit the sorted
   order in one dimension, compare its time and space complexity with all-pairs
   distance calculations, and consider whether simulation can avoid sorting.
3. Derive $E[M]$ mathematically.
4. Determine the distribution of the distance between adjacent cars. Describe
   the joint spacing law and explain how boundaries and the random-position
   model affect the answer.

## Simulation by Sorting

For each trial, draw $n=100$ independent uniform positions and sort them as
$X_{(1)}\lt\cdots\lt X_{(n)}$. Define the internal gaps

$$
D_i=X_{(i+1)}-X_{(i)},\qquad i=1,\ldots,n-1.
$$

Only adjacent cars can be mutual nearest neighbors. The first gap gives a mutual
pair if $D_1\lt D_2$, and the last if $D_{n-1}\lt D_{n-2}$. An interior gap gives
a mutual pair precisely when it is smaller than both neighboring gaps.

```python
import random
from statistics import mean, stdev


def mutual_cars(gaps):
    pairs = int(gaps[0] < gaps[1]) + int(gaps[-1] < gaps[-2])
    pairs += sum(
        gaps[i] < gaps[i - 1] and gaps[i] < gaps[i + 1]
        for i in range(1, len(gaps) - 1)
    )
    return 2 * pairs


def trial(rng, n=100):
    positions = sorted(rng.random() for _ in range(n))
    gaps = [positions[i + 1] - positions[i] for i in range(n - 1)]
    return mutual_cars(gaps)


rng = random.Random(100)
trials = 100_000
counts = [trial(rng) for _ in range(trials)]
print(mean(counts), stdev(counts) / trials**0.5)
```

The reported values are the estimated expectation and its Monte Carlo standard
error. With the seed above, 100,000 trials give an estimate of $66.67524$ cars
with standard error approximately $0.01335$. The gap-counting function assumes $n\ge3$; with exactly two cars the count
is always two.

## Computational Complexity

Sorting takes $O(n\log n)$ time per trial, followed by an $O(n)$ scan. The code
uses $O(n)$ working space per trial and stores $O(B)$ counts for $B$ trials;
online accumulation of the mean and variance avoids storing those counts.
All-pairs comparisons take $O(n^2)$ time and are unnecessary; a full distance
matrix also uses $O(n^2)$ space. For already sorted positions, the scan takes
$O(n)$ time and can use $O(1)$ extra space.

For this simulation, sorting can be avoided entirely. Generate $n+1$ independent
rate-one exponential variables $Z_0,\ldots,Z_n$. Dividing each by their sum gives
the exact uniform spacing law described below. The common denominator cancels
from every gap comparison, so only $Z_1,\ldots,Z_{n-1}$ need be generated to
simulate $M$:

```python
def fast_trial(rng, n=100):
    return mutual_cars([rng.expovariate(1.0) for _ in range(n - 1)])
```

This is an exact $O(n)$ simulation per trial, with $O(n)$ space as written or
$O(1)$ working space using a rolling window of three gaps. It is optimal in order
among methods that generate and inspect each gap. If only the expectation is
needed, the formula below gives it directly in $O(1)$ time.

## Expected Number of Cars

The uniform spacings are exchangeable and continuous. Each of the two end gaps
is smaller than its sole neighboring internal gap with probability $1/2$.
Each of the $n-3$ interior gaps is smallest among itself and its two neighbors
with probability $1/3$. Independence is not required for linearity of expectation.
Thus, for $n\ge3$,

$$
E[M]
=2\left(\frac12+\frac12+\frac{n-3}{3}\right)
=\frac{2n}{3}.
$$

For 100 cars,

$$
\boxed{E[M]=\frac{200}{3}\approx66.67\text{ cars}}.
$$

The boundary gaps from the segment endpoints to the outermost cars do not enter
the nearest-neighbor comparisons, because the endpoints are not cars.

## Distribution of Adjacent Spacings

Include the two boundary spacings $D_0=X_{(1)}$ and $D_n=1-X_{(n)}$. Then

$$
(D_0,D_1,\ldots,D_{n-1},D_n)
\sim\mathrm{Dirichlet}(1,\ldots,1),
\qquad \sum_{i=0}^{n}D_i=1.
$$

Equivalently, this vector has the distribution of
$(Z_0,\ldots,Z_n)/\sum_{j=0}^{n}Z_j$ for independent rate-one exponentials.
Each fixed-rank adjacent spacing has marginal distribution

$$
D_i\sim\mathrm{Beta}(1,n),\qquad
f_{D_i}(d)=n(1-d)^{n-1},\quad 0\lt d\lt1,
\qquad E[D_i]=\frac1{n+1}.
$$

For 100 cars, the marginal is $\mathrm{Beta}(1,100)$ with mean $1/101$.
The spacings are dependent because they sum to one; they are not independent
exponentials. Selecting a gap by a different rule, such as taking the smallest
gap, also changes its distribution.

On a segment of length $L$, each spacing divided by $L$ has the same beta law.
If cars are fixed at both endpoints and the other $n-2$ cars are independent
uniform points, there are instead $n-1$ Dirichlet spacings, each with marginal
$\mathrm{Beta}(1,n-2)$ on a unit segment. For a homogeneous Poisson process on a
line, successive interarrival gaps are independent exponentials; conditioning
on a fixed number of points in a bounded interval gives the uniform model used
here. Nonuniform position distributions generally change physical gap laws and
can change the mutual-neighbor expectation. The random-position model must
therefore be specified, not just the absence of ties.

## Connections

- [Indicator Random Variables Cookbook](../../KnowledgeCards/Probability/Indicator_Random_Variables_Cookbook.md) — count local events using indicators and linearity of expectation.
- [P008 — Runs in a Conditioned Coin-Toss Sequence](P008_Runs_in_a_Conditioned_Coin_Toss_Sequence.md) — adjacent-event counts under a global constraint.
