# P022 — Discrete Median and Symmetry

## Metadata

- Category: Probability
- Tags: Combinatorics, Symmetry, Order Statistics
- Date Added: 2026-10-22
- Original drill dates: 2026-10-07
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-07 Q5

Source and assessment: [2026-10-07 Q5](../../DailyTests/2026-10-07.md#q5--discrete-median-and-symmetry). The reference material below does not change that attempt’s recorded result.

### Question

Choose three distinct integers uniformly from $`\{1,\ldots,10\}`$ and sort them as $`X_{(1)}\lt X_{(2)}\lt X_{(3)}`$. Find $`P(X_{(2)}=6)`$ and $`E[X_{(2)}]`$ without brute-force enumeration.

### Recorded solution

```math
P(X_{(2)}=6)=\frac{\binom51\binom41}{\binom{10}{3}}=\frac16.
```

The bijection $`x\mapsto11-x`$ maps median m to 11-m and preserves sample probabilities, so $`E[X_{(2)}]=11/2`$. More generally, a uniform k-element subset of $`\{1,\ldots,N\}`$ has $`E[X_{(r)}]=r(N+1)/(k+1)`$.

### Related Notes

- [Random Points, Order Statistics, and Spacings](../../KnowledgeCards/Probability/Random_Points_Order_Statistics_and_Spacings.md): related order-statistics and symmetry framework.
- [P018 — First Ace Position and Conditioning on a Face Card](P018_First_Ace_Position_and_Conditioning_on_a_Face_Card.md): discrete positions and exchangeable gaps.

## Assessment history

- [2026-10-07 Q5 — assessment](../../DailyTests/2026-10-07.md#q5--discrete-median-and-symmetry)

## Related questions and knowledge

- [P021 — Conditional Red-Ball Positions](P021_Conditional_Red_Ball_Positions.md) — Discrete order statistics, exchangeability and symmetry.
- [Random Points Order Statistics and Spacings](../../KnowledgeCards/Probability/Random_Points_Order_Statistics_and_Spacings.md) — Knowledge card.
