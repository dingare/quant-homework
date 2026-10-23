# P034 — First Repeated Label

## Metadata

- Category: Probability
- Tags: Collision Time, Tail Sum, Birthday Scale
- Date Added: 2026-10-22
- Original drill dates: 2026-10-18
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-18 Q4

Source and assessment: [2026-10-18 Q4](../../DailyTests/2026-10-18.md#q4--first-repeated-label). The reference material below does not change that attempt’s recorded result.

### Question

Draw labels independently and uniformly from 1 through m, with m at least two. Stop at the first draw whose label has already appeared. T counts all draws, including the repeated draw.

Derive the tail probability for every nonnegative integer k, including boundaries. Give an exact expression for the expectation; a finite sum is acceptable. For large m, derive the leading approximation to the median, including its constant, justify the approximation and explain the scale of the first repeat.

### Key solution

Survival means all first k labels are different:

```math
P(T\gt k)=
\begin{cases}
\displaystyle\frac{m!}{(m-k)!\,m^k}
=\prod_{j=0}^{k-1}\left(1-\frac jm\right),
&0\le k\le m,\\
0,&k\ge m+1.
\end{cases}
```

The empty product at zero is one; survival at one is also one. The support of T is 2 through m plus one.

The user's direct-counting route is equally valid: choose and order the first k minus one distinct labels, then repeat one of those k minus one labels:

```math
P(T=k)
=\frac{\binom m{k-1}(k-1)!(k-1)}{m^k},
\qquad 2\le k\le m+1.
```

```math
P(T\gt k)=1-\sum_{j=2}^kP(T=j).
```

The cumulative upper bound depends on k. Do not sum survival probabilities as if they were point probabilities.

For a positive integer random variable, count the number of surviving integer thresholds and take expectations:

```math
T=\sum_{k=0}^{\infty}\mathbf1_{\{T\gt k\}},
\qquad
E[T]=\sum_{k=0}^{m}P(T\gt k)
=\sum_{k=0}^{m}\frac{m!}{(m-k)!\,m^k}.
```

This finite sum satisfies the question; no simpler elementary form was required.

The conditional chance of a repeat on the next draw, after k distinct labels, is k/m, not a fixed success probability. For the large-m median, take logarithms and use the small-argument logarithm approximation:

```math
\log P(T\gt k)
=\sum_{j=0}^{k-1}\log\left(1-\frac jm\right)
\approx-\frac{k(k-1)}{2m}
\approx-\frac{k^2}{2m}.
```

Setting survival approximately to one half gives:

```math
-\frac{k^2}{2m}\approx-\ln2
\quad\Longrightarrow\quad
k_{\rm median}\sim\sqrt{2m\ln2}.
```

The collision scale is square root of m. At that scale, k/m tends to zero, consistent with the small per-factor arguments used above.

## Assessment history

- [2026-10-18 Q4 — assessment](../../DailyTests/2026-10-18.md#q4--first-repeated-label)

## Related questions and knowledge

- [P015 — Dice Coupon Collector: See Every Face at Least Twice](P015_Dice_Coupon_Collector_See_Every_Face_At_Least_Twice.md) — Repeated labels versus full coverage; different stopping scales.
- [Indicator Random Variables Cookbook](../../KnowledgeCards/Probability/Indicator_Random_Variables_Cookbook.md) — Knowledge card.
- [Waiting Time and Competing Risks Cookbook](../../KnowledgeCards/Probability/Waiting_Time_and_Competing_Risks_Cookbook.md) — Knowledge card.
