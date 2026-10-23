# T004 — Kalman Filtering II: Covariance-Weighted Bayesian Updating

## Metadata

- Category: Time Series
- Secondary: Bayesian Inference, Linear Algebra, State Space Models
- Difficulty: ★★★★★
- Tags: Kalman Filter, Kalman Gain, Gaussian Conditioning, Innovation, Covariance Weighting, State Space Model
- Review Priority: High
- Date Added: 2026-07-12
- Status: Draft
- Personal Note: The goal is not to memorize the equations, but to see the gain as covariance-weighted Bayesian updating.

## Core Question

Suppose a latent state

```math
x=(L,S)^\top
```

has prior distribution

```math
x\sim N(m,P),
```

and observations satisfy

```math
y=Hx+\varepsilon,
\qquad
\varepsilon\sim N(0,R).
```

How should we think about:

1. the innovation,
2. the innovation covariance,
3. the Kalman gain,
4. the posterior mean and covariance,
5. the one-step prediction step?

## Why This Topic Matters

The hard part of Kalman filtering is usually not the matrix multiplication. It is understanding why the update has this exact structure.

This matters because the same covariance-weighted logic appears in:

- Bayesian updating,
- GLS,
- signal combination,
- mean-variance weighting,
- Gaussian conditioning.

Kalman filtering is one of the cleanest dynamic versions of that idea.

## My Current Understanding

The innovation

```math
y-Hm
```

is just observation minus prediction.

The filter then asks: how much of this surprise should be interpreted as real signal about the hidden state, and how much should be interpreted as measurement noise?

That tradeoff is exactly what the Kalman gain encodes.

## Core Update Equations

Innovation:

```math
\nu=y-Hm
```

Innovation covariance:

```math
S=HPH^\top+R
```

Kalman gain:

```math
K=PH^\top(HPH^\top+R)^{-1}=PH^\top S^{-1}
```

Posterior mean:

```math
m_{\text{new}}=m+K(y-Hm)=m+K\nu
```

Posterior covariance:

```math
P_{\text{new}}=(I-KH)P
```

One-step prediction:

```math
m_{t+1|t}=F m_{t|t},
\qquad
P_{t+1|t}=F P_{t|t}F^\top+Q
```

## Why Covariance Determines Trust

The gain

```math
K=PH^\top(HPH^\top+R)^{-1}
```

balances two uncertainty sources:

- prior state uncertainty `P`,
- observation noise `R`.

If

```math
R
```

is large, observations are noisy, so we trust them less.

If

```math
P
```

is large, the prior is uncertain, so we trust the prior less.

So the Kalman filter is not "averaging" in a naive sense. It is averaging after adjusting for covariance structure.

## Why Can Entries of the Kalman Gain Be Negative?

Negative entries are completely natural.

If two latent components are correlated, then an observation that pushes one component up may imply the other should move down. The filter updates the full joint distribution, not each coordinate independently.

So a negative entry in the gain is not a bug. It is a direct expression of cross-covariance.

## Why Posterior Covariance Does Not Depend on Today’s Observation

The posterior mean depends on the realized

```math
y.
```

The posterior covariance does not.

In linear-Gaussian models, the amount of uncertainty reduction depends only on:

- prior covariance `P`,
- observation map `H`,
- noise covariance `R`.

It does not depend on whether today’s surprise happened to be large or small.

## Geometry

The prior is an uncertainty ellipse in state space.

The observation provides another Gaussian piece of information.

Kalman filtering combines them into a posterior that is:

- shifted,
- smaller,
- possibly rotated.

The gain determines how far the posterior center moves in response to the innovation.

## Unifying Perspective

This is another covariance-adjusted projection problem.

- Mean-variance optimization weights signals by inverse covariance.
- GLS weights moments by inverse covariance.
- Kalman filtering weights observation surprises by inverse innovation covariance.

The recurring principle is:

```math
\text{remove redundancy first, then combine information.}
```

## Common Mistakes

- Memorizing the gain without understanding what uncertainty it balances.
- Thinking negative gain entries are wrong.
- Treating observations as independent when `R` is correlated.
- Forgetting that innovation covariance includes both state uncertainty and measurement noise.

## Interview Follow-Ups

- How does the Kalman filter relate to Gaussian conditioning?
- Why is the gain covariance-weighted rather than Euclidean?
- What changes when observation errors are correlated?
- Why does the covariance update not depend on the realized observation?
- How does this connect to GLS or mean-variance weighting?

## Market / Rates Application

In rates and macro trading, several noisy signals may all point to the same latent object:

- level and slope estimates,
- fair value versus market quote,
- auction information,
- liquidity-sensitive basis signals.

The Kalman filter is the natural way to update those hidden objects over time without double counting correlated evidence.

## Connections

- Gaussian conditioning
- Bayesian updating
- Kalman gain as covariance weighting
- GLS and Mahalanobis geometry
- State-space models
- Signal combination under dependence

## What to Remember

- Innovation:

```math
\nu=y-Hm
```

- Innovation covariance:

```math
S=HPH^\top+R
```

- Kalman gain:

```math
K=PH^\top(HPH^\top+R)^{-1}
```

- The gain tells us how much of today’s surprise is signal after accounting for covariance and measurement noise.
