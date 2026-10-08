# Random Points, Order Statistics, and Spacings

## Purpose

Group the completed random-point problems around one reusable method: sort the
points, express the event through gaps or extrema, account for boundaries, and
choose between an analytic calculation and a simulation.

This card connects the random-point material in P001 and P016 with continuous and
discrete order statistics, Beta and Beta-binomial derivations, and the October 7 interview examples. Unfinished extensions
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

## 7. Continuous Order Statistics and the Beta Distribution

For iid continuous observations $X_1,\ldots,X_n$ with CDF F and density f, $X_{(r)}$ is the r-th smallest observation, $1\le r\le n$. The event $X_{(r)}\le x$ means at least r observations are at most x. Thus

$$
P(X_{(r)}\le x)=\sum_{j=r}^n\binom nj F(x)^j[1-F(x)]^{n-j}.
$$

For the density, place one observation in a small interval of width dx at x, r-1 below x, and n-r above x. There are $n!/[(r-1)!(n-r)!]$ assignments, giving

$$
f_{X_{(r)}}(x)
=\frac{n!}{(r-1)!(n-r)!}
F(x)^{r-1}[1-F(x)]^{n-r}f(x).
$$

For a Uniform(0,1) sample, F(u)=u and f(u)=1. Comparing with the Beta density gives

$$
U_{(r)}\sim\mathrm{Beta}(r,n+1-r).
$$

For a general continuous F, the probability integral transform gives
$F(X_{(r)})\sim\mathrm{Beta}(r,n+1-r)$; the untransformed order statistic need not be Beta. See the [order-statistics reference](https://faculty.cc.gatech.edu/~jx/8803DS08/order_statistics.pdf) for the general density and uniform special case.

### Deriving the Mean and Variance

Define the normalizing integral

$$
B(a,b)=\int_0^1 u^{a-1}(1-u)^{b-1}\,du
=\frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}.
$$

If $U\sim\mathrm{Beta}(a,b)$, multiplying the density by u or $u^2$ shifts the first exponent:

$$
E[U]=\frac{B(a+1,b)}{B(a,b)}=\frac{a}{a+b},
\qquad
E[U^2]=\frac{B(a+2,b)}{B(a,b)}
=\frac{a(a+1)}{(a+b)(a+b+1)}.
$$

Subtracting the squared mean gives

$$
\operatorname{Var}(U)=\frac{ab}{(a+b)^2(a+b+1)}.
$$

Therefore

$$
E[U_{(r)}]=\frac{r}{n+1},
\qquad
\operatorname{Var}(U_{(r)})
=\frac{r(n+1-r)}{(n+1)^2(n+2)}.
$$

On Uniform(A,B), the expected r-th order statistic is
$A+(B-A)r/(n+1)$. For arbitrary F, do not move expectation through its inverse:
$E[X_{(r)}]$ is generally not $F^{-1}(r/(n+1))$.

### Why the Spacing Result Gives the Same Answer

In Section 2, $U_{(r)}=D_0+\cdots+D_{r-1}$. Aggregating the first r coordinates of a Dirichlet(1,...,1) vector gives a Beta(r,n+1-r) variable. Each of the n+1 exchangeable gaps has mean $1/(n+1)$, so their first r sum to $r/(n+1)$ in expectation. This connects positions, gaps, and the Beta density.

## 8. Discrete Order Statistics Without Replacement

Choose a uniform k-element subset of $\{1,\ldots,N\}$, with $1\le k\le N$, and sort it as $X_{(1)}\lt\cdots\lt X_{(k)}$. These are distinct positions, not iid draws with replacement.

### Distribution by Counting

For $X_{(r)}=x$, choose r-1 selected positions below x and k-r above x; x itself must be selected:

$$
P(X_{(r)}=x)
=\frac{\binom{x-1}{r-1}\binom{N-x}{k-r}}{\binom Nk},
\qquad r\le x\le N-k+r.
$$

A complementary CDF view uses $H_x$, the number selected among positions 1 through x. It is hypergeometric with population size N, x marked positions, and k draws:

$$
P(X_{(r)}\le x)=P(H_x\ge r).
$$

The fixed-position count is hypergeometric; the random position has the order-statistic law above.

### Deriving the Expected Position from Gaps

Count unselected positions in the k+1 gaps:

$$
G_0=X_{(1)}-1,\quad
G_i=X_{(i+1)}-X_{(i)}-1,\quad
G_k=N-X_{(k)}.
$$

The nonnegative integers $G_0,\ldots,G_k$ sum to N-k. Each k-subset corresponds to exactly one such weak composition, and vice versa, so all these gap vectors are equally likely. Permuting gap coordinates preserves this uniform law; hence

$$
E[G_i]=\frac{N-k}{k+1}.
$$

The r-th selected position includes r selected points and the unselected points in the first r gaps:

$$
X_{(r)}=r+\sum_{i=0}^{r-1}G_i,
\qquad
E[X_{(r)}]=r+r\frac{N-k}{k+1}
=\boxed{\frac{r(N+1)}{k+1}}.
$$

This explains both the N+1 and k+1: include the gaps at both ends, and remember that each selected position contributes one unit.

## 9. Why the Discrete Law Is a Shifted Beta-Binomial

Use the convention $Y\sim\mathrm{BetaBinomial}(m,a,b)$ when

$$
P\sim\mathrm{Beta}(a,b),
\qquad
Y\mid P=p\sim\mathrm{Binomial}(m,p).
$$

Integrating out p yields

$$
P(Y=y)=\int_0^1\binom my p^y(1-p)^{m-y}
\frac{p^{a-1}(1-p)^{b-1}}{B(a,b)}\,dp
=\binom my\frac{B(y+a,m-y+b)}{B(a,b)}.
$$

This is the parameterization used by [SciPy's Beta-binomial documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.betabinom.html). Here m is the number of binomial trials.

### Exact Link to the r-th Selected Position

Set $m=N-k$, $a=r$, $b=k+1-r$, and $Y=X_{(r)}-r$. Then y counts unselected positions before the r-th selected one. For integer parameters, $B(a,b)=(a-1)!(b-1)!/(a+b-1)!$, so

$$
\binom{N-k}{y}
\frac{B(y+r,N-k-y+k+1-r)}{B(r,k+1-r)}
=
\frac{\binom{y+r-1}{r-1}\binom{N-y-r}{k-r}}{\binom Nk}.
$$

The right side is exactly the discrete order-statistic PMF at x=y+r. Therefore

$$
\boxed{X_{(r)}-r\sim\mathrm{BetaBinomial}(N-k,r,k+1-r)}.
$$

It is the shifted variable, not $X_{(r)}$ itself, that has support 0 through N-k.

### A Construction That Explains the Mixture

Give k selected objects and N-k unselected objects independent Uniform(0,1) keys and sort all N objects. Their ranks form a uniform random permutation, so the selected ranks form a uniform k-subset.

Let P be the r-th smallest key among the k selected objects. By Section 7,
$P\sim\mathrm{Beta}(r,k+1-r)$. Conditional on P=p, each unselected key falls below p independently with probability p. Their count is therefore Binomial(N-k,p). Adding the r selected objects at or below P gives the rank $X_{(r)}=r+Y$.

This is an exact probabilistic representation of sampling without replacement. It does not assert that the original selected ranks are independent Bernoulli trials.

### Moments via Conditional Expectation and Variance

Write s=a+b. Since $E[Y\mid P]=mP$,

$$
E[Y]=m\frac as.
$$

Also $E[P(1-P)]=ab/[s(s+1)]$, so

$$
\begin{aligned}
\operatorname{Var}(Y)
&=E[mP(1-P)]+\operatorname{Var}(mP)\\
&=\frac{mab}{s(s+1)}+\frac{m^2ab}{s^2(s+1)}
=\frac{mab(s+m)}{s^2(s+1)}.
\end{aligned}
$$

Substituting the discrete order-statistic parameters recovers the gap-based mean and gives

$$
E[X_{(r)}]=\frac{r(N+1)}{k+1},
\qquad
\operatorname{Var}(X_{(r)})
=\frac{(N-k)r(k+1-r)(N+1)}{(k+1)^2(k+2)}.
$$

When N=k, every position is selected and the variance is zero. For fixed k as N grows, the mixture construction gives
$X_{(r)}/N\Rightarrow\mathrm{Beta}(r,k+1-r)$: conditional binomial noise divided by N vanishes. The finite-N law remains discrete.

## 10. Interview Examples and Retrieval Checklist

### October 7: Conditional Red Positions

Given the third red at draw 8, the first two red positions are a uniform two-subset of 1 through 7. Thus

$$
P(\text{both in first four})=\frac{\binom42}{\binom72}=\frac27,
\qquad
E[X_{(1)}]=\frac83,
\qquad
X_{(1)}-1\sim\mathrm{BetaBinomial}(5,1,2).
$$

The condition fixes the number of reds in the first seven positions; exchangeability makes their locations uniform.

### October 7: Median of Three Distinct Integers

For N=10, k=3, r=2,

$$
P(X_{(2)}=6)=\frac{\binom51\binom41}{\binom{10}{3}}=\frac16,
\qquad
E[X_{(2)}]=\frac{2(11)}4=5.5,
\qquad
X_{(2)}-2\sim\mathrm{BetaBinomial}(7,2,2).
$$

For the expectation alone, reflection $x\mapsto11-x$ pairs each median with 11 minus itself, so its mean is 5.5.

Review record: **2026-10-07 — order statistics reviewed; cold retrieval succeeded.** [Daily drill Q2 and Q5](../../DailyTests/2026-10-07.md) retain the performance details: Q5 answers took one minute, and its expectation derivation was explained afterward. This expanded derivation is a follow-up note, not a retroactive claim of an independent proof during the drill.

### Connection to First-Ace Positions

In [P018 — First Ace Position and Conditioning on a Face Card](../../Questions/Probability/P018_First_Ace_Position_and_Conditioning_on_a_Face_Card.md), N=52, k=4, r=1:

$$
X_{(1)}-1\sim\mathrm{BetaBinomial}(48,1,4),
\qquad E[X_{(1)}]=\frac{53}{5}.
$$

This is also the count of non-Aces before the first Ace in a finite population, a negative-hypergeometric interpretation. State whether a waiting-time variable counts failures only or all draws including the success.

| Sampling model / variable | Distribution or key result |
| --- | --- |
| r-th of n iid Uniform(0,1) draws | Beta(r,n+1-r) |
| Continuous general F | F applied to the r-th order statistic is Beta(r,n+1-r) |
| r-th of a uniform k-subset of 1,...,N | Position minus r is BetaBinomial(N-k,r,k+1-r) |
| Number selected in a fixed prefix | Hypergeometric |
| Discrete sampling with replacement | Ties possible; the distinct-subset formulas above do not apply |

Retrieval sequence: specify sampling and support → translate rank into a count or gaps → derive by counting / density → identify the distribution → check shifts and endpoints.

