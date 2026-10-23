# P028 — Branching Process Extinction

## Metadata

- Category: Probability
- Tags: Generating Functions, Fixed Points, Extinction
- Date Added: 2026-10-22
- Original drill dates: 2026-10-11
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-11 Q6

Source and assessment: [2026-10-11 Q6](../../DailyTests/2026-10-11.md#q6--branching-process-extinction). The reference material below does not change that attempt’s recorded result.

### Question

Start with $`Z_0=1`$. Each individual independently has offspring count $`K`$ with probabilities $`(0.4,0.2,0.4)`$ for $`K=0,1,2`$, then disappears. Find extinction by generation 2, eventual extinction and root selection, $`E[Z_n]`$, and expected total progeny. Repeat eventual extinction for probabilities $`(0.25,0.25,0.50)`$.

### Key solution

```math
P(T\le2)=0.4+0.2(0.4)+0.4(0.4)^2=0.544.
```

Extinction is the smallest fixed point in $`[0,1]`$ of the offspring generating function, obtained by iterating from zero:

```math
q=0.4+0.2q+0.4q^2\quad\Longrightarrow\quad q=1.
```

```math
E[K]=1,\qquad E[Z_n]=1,\qquad
E\!\left[\sum_{n=0}^{\infty}Z_n\right]=\sum_{n=0}^{\infty}1=\infty.
```

For the alternative probabilities the roots are $`1/2`$ and 1, so extinction probability is $`1/2`$.

## Assessment history

- [2026-10-11 Q6 — assessment](../../DailyTests/2026-10-11.md#q6--branching-process-extinction)

## Related questions and knowledge

- [P023 — Coin Pattern Waiting Times](P023_Coin_Pattern_Waiting_Times.md) — First-step recursion and boundary/root selection.
- [Waiting Time and Competing Risks Cookbook](../../KnowledgeCards/Probability/Waiting_Time_and_Competing_Risks_Cookbook.md) — Knowledge card.
