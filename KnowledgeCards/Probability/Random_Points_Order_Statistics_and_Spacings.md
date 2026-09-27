# Random Points, Order Statistics, and Spacings

## Purpose

Group the completed random-point problems around one reusable method: sort the
points, express the event through gaps or extrema, account for boundaries, and
choose between an analytic calculation and a simulation.

This card summarizes completed material in P001 and P016. Unfinished extensions
are tracked in the [next-session To-Do List](../../Backlog.md#random-points-and-spacings--to-do-list).

## 1. Completed Problems

| Source | Completed question | Main technique |
| --- | --- | --- |
| [P001, Solution 1](../../Questions/Probability/P001_Fixed_vs_Exists_Probability_Patterns.md) | Uniform circle points fit in some semicircle | Choose a candidate endpoint and use symmetry |
| [P001, Solution 2](../../Questions/Probability/P001_Fixed_vs_Exists_Probability_Patterns.md) | Uniform points on a segment fit in a moving interval | Range of order statistics and boundary correction |
| [P016](../../Questions/Probability/P016_Mutual_Nearest_Neighbors_on_a_Line.md) | Count cars in mutual-nearest-neighbor pairs | Local gap minima, indicator expectations, and efficient simulation |

Only the random-point sections of P001 belong to this family. Its coin-streak
and occupancy sections address different models.

## 2. Model and Spacing Law

For $n$ independent $\mathrm{Uniform}(0,1)$ positions, write the sorted values as
$X_{(1)}\lt\cdots\lt X_{(n)}$. With the endpoints excluded as cars, define

$$
D_0=X_{(1)},\qquad
D_i=X_{(i+1)}-X_{(i)}\quad(1\le i\le n-1),\qquad
D_n=1-X_{(n)}.
$$

The completed spacing result in P016 is

$$
(D_0,\ldots,D_n)\sim\mathrm{Dirichlet}(1,\ldots,1),
\qquad
D_i\sim\mathrm{Beta}(1,n),
\qquad
E[D_i]=\frac1{n+1}.
$$

The spacings sum to one and are dependent. Independent rate-one exponentials
$Z_0,\ldots,Z_n$, normalized by their sum, generate this joint law exactly.
Unnormalized exponentials preserve gap comparisons but are not the actual
finite-interval distances.

## 3. Nearest Neighbors and Local Gap Minima

In one dimension, a car's nearest neighbor must be adjacent in sorted order.
An interior adjacent pair is mutual precisely when its gap is smaller than both
neighboring gaps. At either end, there is only one competing internal gap.
Distance ties have probability zero under the stated model.

Exchangeability gives end-pair probabilities $1/2$ and interior-pair
probabilities $1/3$. Each mutual pair contributes two cars, so P016 obtains

$$
E[M]=2\left(\frac12+\frac12+\frac{n-3}{3}\right)
=\frac{2n}{3},\qquad n\ge3.
$$

For 100 cars the answer is $200/3\approx66.67$. The completed 100,000-trial
simulation estimates $66.67524$, with Monte Carlo standard error about $0.01335$.
The [Indicator Random Variables Cookbook](Indicator_Random_Variables_Cookbook.md)
provides the general expectation and covariance toolkit; independence is not
needed for the expectation above.

## 4. Coverage, Range, and Boundaries

P001's segment problem asks whether the range fits inside length $a$:

$$
P(X_{(n)}-X_{(1)}\le a)
=na^{n-1}-(n-1)a^n,\qquad 0\le a\le1.
$$

Its circle problem asks whether some semicircle covers all points, giving
$n/2^{n-1}$. A movable interval or semicircle requires considering possible
endpoints rather than fixing a candidate in advance.

The geometry matters: a segment has endpoints; a circle permits wraparound.
P016 also distinguishes scaled segments, fixed endpoint cars, and Poisson
interarrival gaps from the fixed-count uniform model. These distinctions are
already completed; further calculations for changed models remain in the backlog.

## 5. Simulation and Computation

| Task | Completed approach | Time |
| --- | --- | --- |
| Count mutual neighbors in unsorted positions | Sort, then scan adjacent gaps | $O(n\log n)$ |
| Count with positions already sorted | Scan local gap comparisons | $O(n)$ |
| Simulate the count under the uniform model | Compare independent exponential variables; normalization cancels | $O(n)$ per trial |
| Compute the expectation only | Evaluate $2n/3$ for $n\ge3$ | $O(1)$ |

The gap scan can use a rolling window with $O(1)$ extra space. Generating a full
all-pairs distance matrix is unnecessary. Simulation checks the analytic answer;
the exact expectation avoids Monte Carlo error when only the mean is requested.

## 6. Review Checklist

- State the distribution, domain, boundary rules, and sampling rule for a gap.
- Sort points and identify whether the event uses extrema or neighboring gaps.
- Distinguish a fixed gap, a selected gap, and a nearest-neighbor distance.
- Count cars versus pairs explicitly.
- Use exchangeability for comparisons and linearity for expected counts.
- Keep dependent Dirichlet spacings distinct from their exponential generators.
- Refer to the [To-Do List](../../Backlog.md#random-points-and-spacings--to-do-list) for unfinished extensions.
