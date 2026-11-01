# P037 — Nonnegative Bridges and the Reflection Bijection

## Metadata

- Category: Probability
- Tags: Conditional Path Counting, Reflection, First Passage, Fixed Totals
- Date Added: 2026-11-01
- Original drill: October 31, 2026, Q2
- Status: Reference explanation supplied; independent contributions and question-meaning clarifications are preserved in the dated assessment.

## Core Question

Independent trade outcomes are +1 with probability p and -1 with probability 1 - p, with p strictly between zero and one. Let:

```math
S_0=0,\qquad S_j=\sum_{i=1}^jX_i.
```

Given that the strategy finishes flat after exactly 2n trades, with n at least one:

1. Derive the probability that cumulative P&L is nonnegative at every intermediate time. Give a counting argument rather than quoting a named formula.
2. Does this conditional probability depend on p? Justify the answer.
3. Does conditioning on finishing flat leave the individual outcomes independent?

Original budget: 14 minutes; actual time not recorded.

## Interpret the event

The first question concerns the entire path simultaneously:

```math
P\left(\bigcap_{j=0}^{2n}\{S_j\ge0\}\,\middle|\,S_{2n}=0\right).
```

It does not ask for the nonnegative probability at one fixed time j. The path `+--+` finishes flat and is nonnegative at time 2, but fails the whole-path event at time 3. Clarification of this wording is not by itself a conceptual failure.

## Solution

### Conditional uniformity

Every flat-ending path has n up moves and n down moves, so every such path has the same unconditioned probability. For a particular balanced path:

```math
P(\text{path}\mid S_{2n}=0)
=\frac{p^n(1-p)^n}{\binom{2n}{n}p^n(1-p)^n}
=\frac1{\binom{2n}{n}}.
```

Thus p affects how likely a flat ending is, but disappears from the conditional distribution of its orderings.

### Reflect bad paths

A bad balanced path must first reach -1 at some time tau. Reverse the sign of every increment up to and including that time; leave the suffix unchanged. The prefix sum changes from -1 to +1, increasing the full endpoint from 0 to +2.

```text
Original increments:     +1 -1 -1 | +1
Original cumulative:   0   1  0 -1   0
Reflected increments:    -1 +1 +1 | +1
Reflected cumulative:  0  -1  0  1   2
```

Before tau, the original cumulative values are nonnegative; after reflection they are nonpositive. Therefore tau becomes the first time the reflected path reaches +1. Conversely, every path ending at +2 must reach +1; reflect the prefix through its first +1 to recover exactly one bad balanced path. This is a bijection. Reflected paths may go negative; only their endpoint is constrained to +2.

A length-2n path ending at +2 has n + 1 up moves and n - 1 down moves. Hence:

```math
\mathrm{Count}\{\text{bad balanced paths}\}=\binom{2n}{n+1},
\qquad
P(\text{nonnegative bridge}\mid S_{2n}=0)
=1-\frac{\binom{2n}{n+1}}{\binom{2n}{n}}
=\frac1{n+1}.
```

### Dependence after conditioning

Each position has conditional up probability one half, but conditioning fixes the total number of up moves. For example:

```math
P(X_2=1\mid X_1=1,S_{2n}=0)
=\frac{n-1}{2n-1}\ne\frac12.
```

The outcomes therefore are not independent conditional on the flat ending. This reference was displayed; an independent user answer to part 3 was not assessed.

## User-proposed alternative: classify by the first visit to -1

The user independently proposed summing over first-hit times 1, 3, ..., 2n - 1. This is a valid partition into disjoint events. If the first hit is at time 2m + 1, the preceding 2m steps must be balanced and must never have gone below zero. Merely having equal up/down counts would include paths that hit -1 earlier and double-count them.

Let A_m count nonnegative bridges of length 2m, with A_0 = 1. After the forced down move at time 2m + 1, the remaining steps must rise from -1 to 0. Thus:

```math
\mathrm{Count}\{\text{bad balanced paths}\}
=\sum_{m=0}^{n-1}A_m\binom{2n-2m-1}{n-m}.
```

This method requires the smaller nonnegative-bridge counts, so it naturally leads to a recurrence. The reflection construction obtains the bad-path count directly. For four steps, the first-hit-at-1 paths are `--++`, `-+-+`, `-++-`; the first-hit-at-3 path is `+--+`, giving four bad paths in total.

## Connections

- [P008 — Runs in a Conditioned Coin-Toss Sequence](P008_Runs_in_a_Conditioned_Coin_Toss_Sequence.md): fixing totals creates dependence, but this problem counts a whole-path barrier event rather than adjacent-change indicators.
- [P012 — Random-Walk Stopping](P012_Random_Walk_Stopping_Hit_Plus3_Before_Minus2.md): first passage is shared language; a fixed-horizon bridge differs from stopping at one of two absorbing barriers.

## Assessment History

- [October 31 drill, continued through November 1 — Q2](../../DailyTests/2026-10-31.md#q2--nonnegative-bridges).
