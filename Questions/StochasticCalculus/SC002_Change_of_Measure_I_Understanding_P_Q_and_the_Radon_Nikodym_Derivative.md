# SC002 — Change of Measure I: Understanding P, Q and the Radon-Nikodym Derivative

## Metadata

- Category: Stochastic Calculus
- Secondary: Probability, Derivatives Pricing, Asset Pricing
- Difficulty: ★★★★★
- Tags: Change of Measure, Radon-Nikodym Derivative, Risk-Neutral Measure, Exponential Tilting, MGF
- Review Priority: High
- Date Added: 2026-07-05
- Status: Draft
- Personal Note: Keep the intuition front and center: the world stays the same, only the probability weights change.

## Core Question

Suppose

```math
X\sim N(0,1)
```

under the physical measure $\mathbb P$, and define a new measure $\mathbb Q$ by

```math
\frac{d\mathbb Q}{d\mathbb P}
=
e^{\theta X-\frac12\theta^2}.
```

What does this change of measure mean, what is the Radon-Nikodym derivative doing, and what is the distribution of $X$ under $\mathbb Q$?

## Why This Topic Matters

Modern pricing theory repeatedly changes measure:

- physical to risk-neutral,
- money-market measure to forward measure,
- one numeraire to another.

The technical notation can look intimidating, but the main idea is simple: keep the same outcomes and reweight their probabilities.

## My Current Understanding

Changing measure does not change the sample space. It changes the probability assignment on that same sample space.

The Radon-Nikodym derivative

```math
\frac{d\mathbb Q}{d\mathbb P}
```

is the state-by-state weight conversion factor from old probabilities to new probabilities.

For any integrable random variable $Y$,

```math
E_{\mathbb Q}[Y]
=
E_{\mathbb P}\left[Y\frac{d\mathbb Q}{d\mathbb P}\right].
```

## Why the Exponential Term Is Valid

To define a probability measure, the density ratio must integrate to one:

```math
E_{\mathbb P}\left[e^{\theta X-\frac12\theta^2}\right]
=
e^{-\frac12\theta^2}E_{\mathbb P}[e^{\theta X}].
```

Since $X\sim N(0,1)$ under $\mathbb P$,

```math
E_{\mathbb P}[e^{\theta X}]=e^{\frac12\theta^2},
```

so

```math
E_{\mathbb P}\left[e^{\theta X-\frac12\theta^2}\right]=1.
```

The term $-\frac12\theta^2$ is just the normalization that makes total probability stay equal to one.

## Distribution of X Under Q

Compute the moment generating function under $\mathbb Q$:

```math
E_{\mathbb Q}[e^{tX}]
=
E_{\mathbb P}\left[e^{tX}\frac{d\mathbb Q}{d\mathbb P}\right]
=
E_{\mathbb P}\left[e^{(t+\theta)X-\frac12\theta^2}\right].
```

Using the Gaussian MGF under $\mathbb P$:

```math
E_{\mathbb P}[e^{(t+\theta)X}]
=
e^{\frac12(t+\theta)^2},
```

so

```math
E_{\mathbb Q}[e^{tX}]
=
e^{-\frac12\theta^2}e^{\frac12(t+\theta)^2}
=
e^{\theta t+\frac12 t^2}.
```

This is the MGF of a normal random variable with mean $\theta$ and variance $1$, hence

```math
\boxed{X\sim N(\theta,1)\text{ under }\mathbb Q.}
```

## Intuition

The factor

```math
e^{\theta X}
```

tilts probability toward larger values of $X$ when $\theta>0$ and toward smaller values when $\theta<0$.

So under the new measure, the same random variable looks like it has shifted mean.

## Why This Matters for Pricing

Pricing often becomes tractable under a measure chosen so that discounted tradable asset prices are martingales. The measure is chosen for valuation convenience and no-arbitrage consistency, not because the underlying physical dynamics have literally changed.

## Common Mistakes

- Thinking the sample space changes under a new measure.
- Treating the Radon-Nikodym derivative like an ordinary calculus derivative.
- Forgetting the normalization term.
- Confusing state-price weights, risk-neutral probabilities, and physical probabilities.

## Interview Follow-Ups

- How does this connect to exponential tilting and Esscher transforms?
- Why is the risk-neutral measure not usually the real-world measure?
- How does a numeraire change induce a measure change?
- What does Girsanov add in continuous time?

## What to Remember

Changing measure means reweighting the same world.

The Radon-Nikodym derivative converts expectations from $\mathbb P$ to $\mathbb Q$, and in this Gaussian example it shifts the mean from $0$ to $\theta$ while leaving the variance unchanged.
