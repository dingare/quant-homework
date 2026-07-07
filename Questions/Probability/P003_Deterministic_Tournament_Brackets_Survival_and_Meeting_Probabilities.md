# P003 — Deterministic Tournament Brackets: Survival and Meeting Probabilities

## Metadata

- Category: Probability
- Secondary: Combinatorics, Random Trees, Counting
- Difficulty: ★★★☆☆
- Tags: Tournament Bracket, Random Binary Tree, Hypergeometric Probability, Survival Probability
- Review Priority: Medium
- Date Added: 2026-07-06
- Status: Finalized
- Personal Note: The right mental model is the bracket tree, not the sequence of matches.

## Core Question

Suppose there are

```math
N=2^n
```

players with deterministic strength ranking

```math
1>2>3>\cdots>N.
```

The bracket is drawn uniformly at random, and the stronger player always wins.

How do we compute:

1. the probability that players 1 and 2 meet in the final,
2. the probability that player `k` reaches Top `T`,
3. the distribution of the round in which players 1 and 2 meet,
4. the meeting probability for player 1 and player `k`?

## Hint

Treat the bracket as a random binary tree:

1. Fix one player's position.
2. Identify the relevant subtree.
3. Exclude stronger players from that subtree.
4. Count placements, then add survival if needed.

## Solution

### 1. Players 1 and 2 Meet in the Final

Fix player 1.

Hence

```math
\boxed{
P(\text{1 and 2 meet in the final})
=
\frac{N/2}{N-1}
=
\frac{2^{n-1}}{2^n-1}
}
```

### 2. Player k Reaches Top T

Player `k` loses only to players

```math
1,2,\dots,k-1.
```

So player `k` reaches a given stage exactly when the relevant subtree contains no stronger player.

If the goal is to finish in Top `T`, where `T` is a power of 2, then the relevant subtree size is

```math
s=\frac{N}{T}.
```

Therefore

```math
\boxed{
P(\text{player }k\text{ reaches Top }T)
=
\frac{\binom{N-k}{s-1}}{\binom{N-1}{s-1}}
=
\frac{\binom{N-k}{N/T-1}}{\binom{N-1}{N/T-1}}
}
```

Example: if `N=16`, then the probability that player 5 reaches Top 4 is

```math
\frac{\binom{11}{3}}{\binom{15}{3}}
=
\frac{33}{91}.
```

### 3. Champion

```math
P(\text{player 1 is champion})=1
```

and for every `k>1`,

```math
P(\text{player }k\text{ is champion})=0.
```

### 4. Which Round Do Players 1 and 2 Meet?

Fix player 1.

```math
\boxed{
P(R=r)=\frac{2^{r-1}}{N-1}
}
\qquad r=1,2,\dots,n.
```

Also,

```math
E[R]
=
\sum_{r=1}^n r\frac{2^{r-1}}{N-1}.
```

Using

```math
\sum_{r=1}^n r2^{r-1}=(n-1)2^n+1,
```

we obtain

```math
\boxed{
E[R]=\frac{(n-1)2^n+1}{2^n-1}
}.
```

As `n\to\infty`,

```math
E[R]\approx n-1.
```

### 5. General Pair: Player 1 and Player k

Unlike player 2, player `k` may be eliminated before meeting player 1. The placement factor and survival factor must both be included.

Thus

```math
\boxed{
P(\text{1 and }k\text{ meet in round }r)
=
\frac{2^{r-1}}{N-1}
\cdot
\frac{\binom{N-k}{2^{r-1}-1}}{\binom{N-2}{2^{r-1}-1}}
}
\qquad r=1,2,\dots,n.
```

Summing over all rounds gives

```math
\boxed{
P(\text{1 and }k\text{ meet})
=
\sum_{r=1}^n
\frac{2^{r-1}}{N-1}
\cdot
\frac{\binom{N-k}{2^{r-1}-1}}{\binom{N-2}{2^{r-1}-1}}
}.
```

If needed, the conditional expected meeting round is

```math
\boxed{
E[R\mid \text{meet}]
=
\frac{\sum_{r=1}^n r\,P(\text{meet in round }r)}
{P(\text{meet})}
}.
```

## Key Knowledge Points

- A deterministic tournament with random seeding is naturally a random binary tree problem.
- Reaching a stage is equivalent to requiring that a specific subtree contain no stronger player.
- This leads to hypergeometric counting formulas.
- For player 2, survival to meet player 1 is automatic once placement is fixed.
- For player `k>2`, survival is not automatic and must be included explicitly.

## Intuition

The bracket matters through local subtrees. A player survives until a given round if stronger players are kept outside the subtree that controls that round.

## Geometry

The tournament bracket is a complete binary tree. Meeting in round `r` corresponds to an opposing subtree of size `2^{r-1}`, and reaching Top `T` corresponds to surviving inside a subtree of size `N/T`.

## Common Mistakes

- Treating subtree sizes like `2,4,8,N` as universal. Those values occur only when `N=16`.
- Forgetting that player `k` may be eliminated before meeting player 1.
- Counting the geometric placement of player `k` but forgetting the survival factor.
- Thinking about the tournament only round by round instead of as a bracket tree.

## Interview Follow-ups

- How would these formulas change if match outcomes were probabilistic rather than deterministic?
- What is the probability that players 2 and 3 meet before either faces player 1?
- What is the probability that player `k` reaches the semifinal?

## Market / Rates Application

The broader lesson is general: many path-dependent problems become easier once the right geometry is chosen.

## Connections

- Hypergeometric probability
- Random tree viewpoint
- Conditional survival arguments
- Occupancy-style counting
- Fixed-vs-exists reasoning in probability

## What to Remember

- Fix one player and analyze the relevant subtree.
- Ask which stronger players are allowed inside that subtree.
- Reaching Top `T` gives a hypergeometric formula.
- Player 1 and player 2 meeting is pure placement.
- Player 1 and player `k` meeting requires both placement and survival.
