# P021 — Conditional Red-Ball Positions

## Metadata

- Category: Probability
- Tags: Conditioning, Sampling Without Replacement, Order Statistics
- Date Added: 2026-10-22
- Original drill dates: 2026-10-07
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-07 Q2

Source and assessment: [2026-10-07 Q2](../../DailyTests/2026-10-07.md#q2--conditional-red-ball-positions). The reference material below does not change that attempt’s recorded result.

### Question

Draw without replacement from 5 red and 7 blue balls. Given that the third red ball appears on draw 8, find:

1. The probability of exactly two red balls among the first four draws.
2. The expected draw number of the first red ball under the same condition.

Explain what the condition implies about the first seven positions, then derive both answers.

### Recorded solution

Condition first, then work with exchangeable positions:

```math
P=\frac{\binom42}{\binom72}=\frac27,
\qquad E[X_{(1)}]=\frac{7+1}{2+1}=\frac83.
```

### Related Notes

- [P018 — First Ace Position and Conditioning on a Face Card](P018_First_Ace_Position_and_Conditioning_on_a_Face_Card.md): related discrete position conditioning.
- [Random Points, Order Statistics, and Spacings](../../KnowledgeCards/Probability/Random_Points_Order_Statistics_and_Spacings.md): shared order-statistics / exchangeability framework; the main card's geometric examples use continuous positions.

## Assessment history

- [2026-10-07 Q2 — assessment](../../DailyTests/2026-10-07.md#q2--conditional-red-ball-positions)

## Related questions and knowledge

- [P018 — First Ace Position and Conditioning on a Face Card](P018_First_Ace_Position_and_Conditioning_on_a_Face_Card.md) — Conditional positions in sampling without replacement.
- [P022 — Discrete Median and Symmetry](P022_Discrete_Median_and_Symmetry.md) — Discrete order statistics, exchangeability and symmetry.
- [P027 — Dice Conditioned on a Sum](P027_Dice_Conditioned_on_a_Sum.md) — Conditioning first to identify the correct finite sample space.
- [Random Points Order Statistics and Spacings](../../KnowledgeCards/Probability/Random_Points_Order_Statistics_and_Spacings.md) — Knowledge card.
