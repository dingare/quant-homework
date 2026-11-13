# P018 — First Ace Position and Conditioning on a Face Card

## Problem

In a uniformly shuffled 52-card deck, let $`T`$ be the position of the first Ace. Find its distribution, mean, and variance. Then condition on the top card being a face card and recompute the expected position. A face card means a Jack, Queen, or King, so it cannot be an Ace.

## Distribution

The four Ace positions are a uniformly chosen four-element subset of the 52 positions. If the first Ace is at $`k`$, the other three Aces must be among positions $`k+1,\ldots,52`$. Therefore,

```math
P(T=k)=\frac{\binom{52-k}{3}}{\binom{52}{4}},
\qquad k=1,\ldots,49.
```

This is the negative hypergeometric waiting time through the first success, or equivalently the minimum of the four Ace positions.

## Mean

The four Aces split the 48 non-Aces into five exchangeable gaps. If $`G_1`$ is the gap before the first Ace, then $`T=G_1+1`$. Each gap has mean $`48/5`$, so

```math
E[T]=1+\frac{48}{5}=\boxed{\frac{53}{5}=10.6}.
```

## Variance

The first gap $`G_1=T-1`$ has a beta-binomial count distribution with $`n=48`$, $`\alpha=1`$, and $`\beta=4`$. Adding one does not change variance. Hence,

```math
\begin{aligned}
Var(T) &= \frac{n\alpha\beta(n+\alpha+\beta)}{(\alpha+\beta)^2(\alpha+\beta+1)} \\
&= \frac{48\cdot1\cdot4\cdot53}{5^2\cdot6} \\
&= \boxed{\frac{1696}{25}=67.84}.
\end{aligned}
```

## Conditioning on a Face Card at the Top

Given that the top card is a Jack, Queen, or King, it is known to be a non-Ace. Remove it. The remaining 51 cards contain all four Aces and 47 non-Aces. Let $`T'`$ be the position of the first Ace in this remaining deck. The gap argument gives

```math
E[T']=1+\frac{47}{5}=\frac{52}{5}.
```

The original top card adds one to the position, so

```math
\begin{aligned}
E[T\mid\text{top card is a face card}] &= 1+E[T'] \\
&= \boxed{\frac{57}{5}=11.4}.
\end{aligned}
```

The identity of the particular face card does not matter: conditional on any particular face card being on top, the remaining 51 cards are uniformly shuffled. Thus the same expectation holds when conditioning only on the top card being a face card.

## Common Mistakes

- Dividing 52 by four gives 13, but the four Aces create five exchangeable gaps. The first Ace occurs after the first gap, with mean position $`53/5`$.
- A geometric model with fixed Ace probability $`4/52`$ assumes replacement and gives the wrong expectation.
- Conditioning on a face card fixes the first position as a non-Ace. Count that position when returning from the 51-card deck to the original position.

## Connections

- P017 — Second Ace and the Negative Hypergeometric Distribution (not yet filed) — the second Ace position uses the first two gaps.
- [P016 — Mutual Nearest Neighbors on a Line](P016_Mutual_Nearest_Neighbors_on_a_Line.md) — order statistics and exchangeable spacings.

## Interview Drill — Second Ace Before Position 20

### Question

In a 52-card deck with 4 Aces, given that the first Ace is at position 10, what is the probability that the second Ace appears before position 20?

### Solution

Positions 1–9 are non-Aces, position 10 is an Ace, and the remaining three Ace positions form a uniformly chosen three-element subset of the 42 positions 11–52. “Before 20” means positions 11–19: nine eligible positions.

Use the complement: no remaining Ace in those nine positions means all three remaining Aces lie among positions 20–52, which contain 33 positions.

```math
\begin{aligned}
P(T_2\lt20\mid T_1=10)
&=1-\frac{\binom{33}{3}}{\binom{42}{3}}\\
&=\frac{753}{1435}\approx0.5247.
\end{aligned}
```

An equivalent disjoint count sums over exactly j Aces in the nine eligible positions:

```math
\frac{\sum_{j=1}^{3}\binom{9}{j}\binom{33}{3-j}}{\binom{42}{3}}.
```

Choosing “an Ace in the first nine remaining positions” and then freely choosing the others overcounts outcomes with two or three Aces there. These nine positions are 11–19 in the original deck, not its original positions 1–9.

### Timed Attempt

[2026-10-06 Q2](../../DailyTests/2026-10-06.md#q2--conditional-ace-positions): Y, about 12 minutes; stopped at the recommended time limit. Conditioning was understood, but the count overcounted. The worked answer above was added after the attempt.

## Citadel Q54: First Ace and First King

Discussion date: 2026-11-12. Source: user-supplied Citadel interview-preparation PDF, page 4, Q54.

### Question

Reveal cards from a uniformly shuffled standard 52-card deck, without replacement, until at least one Ace and at least one King have appeared. What is the expected number of cards revealed?

Count the card that completes the requirement. Let $`T_A`$ and $`T_K`$ be the positions of the first Ace and first King. The stopping time is

```math
T=\max(T_A,T_K).
```

### Solution: replace a maximum by a sum minus a minimum

Use the pathwise identity

```math
\max(T_A,T_K)=T_A+T_K-\min(T_A,T_K).
```

For $`m`$ target cards uniformly placed among $`n`$ positions, the mean first target position is

```math
E[T_{\rm first}]=\frac{n+1}{m+1}.
```

This follows from the same exchangeable-gap argument used above: the target cards split the $`n-m`$ non-target cards into $`m+1`$ exchangeable gaps. The expected number before the first target is $`(n-m)/(m+1)`$; add the target card itself.

There are four Aces and four Kings, so

```math
E[T_A]=\frac{53}{5},\qquad E[T_K]=\frac{53}{5}.
```

The minimum is the first position containing either an Ace or a King. These are eight distinct target cards, hence

```math
E[\min(T_A,T_K)]=\frac{53}{9}.
```

Taking expectations in the identity gives

```math
\boxed{
E[T]=\frac{53}{5}+\frac{53}{5}-\frac{53}{9}
=\frac{689}{45}\approx15.31\text{ cards}.
}
```

### What to remember

- Waiting for both types means the maximum of their first-appearance times.
- Waiting for either type means the minimum, which pools the eight target cards.
- The max-plus-min identity avoids deriving the full joint distribution.
- The two first-appearance times are dependent. Linearity of expectation does not require independence.
- Do not use a geometric distribution with a fixed success probability: cards are drawn without replacement.
- This is the same first-target-position formula used in the earlier Q50 door discussion, applied to four targets and then eight targets.

### Connections and discussion record

- [Random Points, Order Statistics, and Spacings](../../KnowledgeCards/Probability/Random_Points_Order_Statistics_and_Spacings.md): exchangeable gaps give the mean first position; the current deck problem uses discrete positions without replacement.
- [Waiting Time and Competing Risks Cookbook](../../KnowledgeCards/Probability/Waiting_Time_and_Competing_Risks_Cookbook.md): distinguish waiting for either event from waiting for both, and check the independence assumptions before multiplying probabilities.

The assistant supplied the solution on 2026-11-12, and the user requested GitHub archival. No independent derivation, timed rating, elapsed time or mastery claim is inferred. The earlier October 6 assessment below remains unchanged.

## Assessment history

- [2026-10-06 Q2 — assessment](../../DailyTests/2026-10-06.md#q2--conditional-ace-positions)

## Related questions and knowledge

- [P021 — Conditional Red-Ball Positions](P021_Conditional_Red_Ball_Positions.md) — Conditional positions in sampling without replacement.
