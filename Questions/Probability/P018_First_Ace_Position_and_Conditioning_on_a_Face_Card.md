# P018 — First Ace Position and Conditioning on a Face Card

## Problem

In a uniformly shuffled 52-card deck, let $T$ be the position of the first Ace. Find its distribution, mean, and variance. Then condition on the top card being a face card and recompute the expected position. A face card means a Jack, Queen, or King, so it cannot be an Ace.

## Distribution

The four Ace positions are a uniformly chosen four-element subset of the 52 positions. If the first Ace is at $k$, the other three Aces must be among positions $k+1,\ldots,52$. Therefore,

$$
P(T=k)=\frac{\binom{52-k}{3}}{\binom{52}{4}},
\qquad k=1,\ldots,49.
$$

This is the negative hypergeometric waiting time through the first success, or equivalently the minimum of the four Ace positions.

## Mean

The four Aces split the 48 non-Aces into five exchangeable gaps. If $G_1$ is the gap before the first Ace, then $T=G_1+1$. Each gap has mean $48/5$, so

$$
E[T]=1+\frac{48}{5}=\boxed{\frac{53}{5}=10.6}.
$$

## Variance

The first gap $G_1=T-1$ has a beta-binomial count distribution with $n=48$, $\alpha=1$, and $\beta=4$. Adding one does not change variance. Hence,

$$
\begin{aligned}
Var(T) &= \frac{n\alpha\beta(n+\alpha+\beta)}{(\alpha+\beta)^2(\alpha+\beta+1)} \\
&= \frac{48\cdot1\cdot4\cdot53}{5^2\cdot6} \\
&= \boxed{\frac{1696}{25}=67.84}.
\end{aligned}
$$

## Conditioning on a Face Card at the Top

Given that the top card is a Jack, Queen, or King, it is known to be a non-Ace. Remove it. The remaining 51 cards contain all four Aces and 47 non-Aces. Let $T'$ be the position of the first Ace in this remaining deck. The gap argument gives

$$
E[T']=1+\frac{47}{5}=\frac{52}{5}.
$$

The original top card adds one to the position, so

$$
\begin{aligned}
E[T\mid\text{top card is a face card}] &= 1+E[T'] \\
&= \boxed{\frac{57}{5}=11.4}.
\end{aligned}
$$

The identity of the particular face card does not matter: conditional on any particular face card being on top, the remaining 51 cards are uniformly shuffled. Thus the same expectation holds when conditioning only on the top card being a face card.

## Common Mistakes

- Dividing 52 by four gives 13, but the four Aces create five exchangeable gaps. The first Ace occurs after the first gap, with mean position $53/5$.
- A geometric model with fixed Ace probability $4/52$ assumes replacement and gives the wrong expectation.
- Conditioning on a face card fixes the first position as a non-Ace. Count that position when returning from the 51-card deck to the original position.

## Connections

- P017 — Second Ace and the Negative Hypergeometric Distribution (not yet filed) — the second Ace position uses the first two gaps.
- [P016 — Mutual Nearest Neighbors on a Line](P016_Mutual_Nearest_Neighbors_on_a_Line.md) — order statistics and exchangeable spacings.
