# T001 — Kalman Filter I: Recursive Bayesian Estimation for Noisy Market Signals

## Metadata

- Category: Time Series
- Secondary: Statistics, Linear Algebra, Bayesian Inference, Rates Research
- Difficulty: ★★★★★
- Tags: Kalman Filter, State Space Model, Bayesian Estimation, Latent Variables, Innovation, Market Microstructure
- Review Priority: High
- Personal Note: Focus on matrix intuition, correlated observations, and the geometric meaning of the gain.

## Core Question

How should I think about the Kalman filter for buy-side QR interviews?

Not as another time series model, but as recursive Bayesian estimation of a latent state from noisy market signals.

## Why This Topic Matters

Kalman filtering appears everywhere in quant finance because many economically important objects are latent:

- fair value,
- curve factors,
- funding pressure,
- permanent price component,
- rich / cheap dislocation.

What we actually observe is noisy:

- quotes,
- prints,
- basis,
- repo signals,
- auction outcomes,
- yields contaminated by market microstructure noise.

So the real problem is not just forecasting. It is extracting signal from noise in real time.

That is why Kalman filtering matters:

- latent variables,
- noisy observations,
- recursive estimation,
- dynamic fair value,
- market microstructure.

## My Current Understanding

The state equation describes how the hidden object evolves through time before new market information arrives.

The observation equation describes how the market gives noisy measurements of that hidden object.

The prediction step means: carry yesterday's posterior forward into today's prior.

The update step means: compare what the model expected to observe with what the market actually showed, then revise the hidden-state estimate using the size and reliability of that surprise.

So the filter is:

1. predict the hidden state,
2. observe the market,
3. compute the surprise,
4. update by a reliability-weighted correction.

## Matrix Formulation

State equation:

$$
x_t = F x_{t-1} + w_t
$$

Observation equation:

$$
y_t = H x_t + v_t
$$

with

$$
x_t \in \mathbb{R}^n,\qquad y_t \in \mathbb{R}^m
$$

State vector:

- dimension: $n \times 1$
- meaning: latent economic object
- why it appears: what we want is hidden

Observation vector:

- dimension: $m \times 1$
- meaning: noisy market measurements
- why it appears: the market reveals the state imperfectly

Transition matrix $F$:

- dimension: $n \times n$
- meaning: state dynamics
- why it appears: latent states evolve over time

Observation matrix $H$:

- dimension: $m \times n$
- meaning: maps hidden state into observable signals
- why it appears: each signal sees some linear projection of the state

State covariance $P$:

- dimension: $n \times n$
- meaning: uncertainty of the state estimate
- why it appears: update size must depend on uncertainty

Observation covariance $R$:

- dimension: $m \times m$
- meaning: noise level and correlation of observed signals
- why it appears: correlated signals should not be double counted

Innovation covariance $S$:

$$
S = HPH^\top + R
$$

- dimension: $m \times m$
- meaning: total uncertainty of the observation surprise
- why it appears: surprise comes from both state uncertainty and observation noise

Kalman gain $K$:

$$
K = PH^\top(HPH^\top + R)^{-1}
$$

- dimension: $n \times m$
- meaning: maps observation surprise back into latent-state correction
- why it appears: innovation lives in observation space, but the update must occur in state space

## Matrix Derivation

Prediction:

$$
\hat{x}_{t|t-1}=F\hat{x}_{t-1|t-1}
$$

Prediction covariance:

$$
P_{t|t-1}=FP_{t-1|t-1}F^\top+Q
$$

Predicted observation:

$$
\hat{y}_{t|t-1}=H\hat{x}_{t|t-1}
$$

Innovation:

$$
\nu_t=y_t-H\hat{x}_{t|t-1}
$$

Innovation covariance:

$$
S_t=HP_{t|t-1}H^\top+R
$$

Kalman gain:

$$
K_t=P_{t|t-1}H^\top(HP_{t|t-1}H^\top+R)^{-1}=P_{t|t-1}H^\top S_t^{-1}
$$

Posterior update:

$$
\hat{x}_{t|t}=\hat{x}_{t|t-1}+K_t(y_t-H\hat{x}_{t|t-1})
$$

Posterior covariance:

$$
P_{t|t}=(I-K_tH)P_{t|t-1}
$$

For the one-dimensional latent state with two observations:

$$
H=
\begin{bmatrix}
1\\
1
\end{bmatrix},
\qquad
H^\top=
\begin{bmatrix}
1&1
\end{bmatrix}
$$

If $P$ is scalar, then:

$$
PH^\top=
P
\begin{bmatrix}
1&1
\end{bmatrix}=
P(1,1)
$$

Also:

$$
HPH^\top=
\begin{bmatrix}
1\\
1
\end{bmatrix}
P
\begin{bmatrix}
1&1
\end{bmatrix}=
P
\begin{bmatrix}
1&1\\
1&1
\end{bmatrix}
$$

So if

$$
S=HPH^\top+R
$$

then:

$$
K=PH^\top S^{-1}=P(1,1)S^{-1}
$$

This matters because two observation surprises are being aggregated into one latent-state correction.

## Bayesian Interpretation

Kalman filtering is recursive Bayesian estimation.

The prior is the predicted state before seeing the new observation.

The likelihood describes how plausible the observation is for each candidate state.

The posterior is the revised belief after combining the two.

The most important mental model is:

$$
\text{Posterior}=\text{Prior}+\text{Gain}\times\text{Surprise}
$$

If surprise is zero, nothing changes.
If surprise is large but noisy, update modestly.
If surprise is large and precise, update aggressively.

## Geometry

The latent state lives in state space.
The noisy measurements live in observation space.

$H$ projects the latent state into observation space.
Innovation is the gap between actual observation and projected prediction.
Kalman gain maps that gap back into state space.

If one latent state is observed by two signals, then:

$$
(1,1)
$$

is the informative direction because both coordinates move together when the latent state moves.

By contrast:

$$
(1,-1)
$$

mostly reflects disagreement between the two observations, which is usually observation noise rather than real state movement.

## Why This Initially Felt Confusing

What exactly Kalman gain represents:

- resolved by viewing it as the conversion rate from observation surprise to state correction

Why innovation is observation minus prediction:

- resolved by realizing that the prior already contains all past information, so only forecast error is new

Why inverse covariance appears:

- resolved by seeing inverse covariance as precision weighting

Why correlated observations should not be double counted:

- resolved by recognizing that duplicated noise is not duplicated information

Why $\rho\to1$ makes the second signal contribute almost no extra information:

- resolved by seeing that the second signal becomes mostly the same noisy direction as the first

## Linear Algebra Connections

This topic connects directly to:

- projection,
- least squares,
- covariance matrices,
- positive definite matrices,
- matrix inversion,
- precision matrices,
- orthogonal decomposition.

The strongest interview takeaway is that Kalman filtering tests whether matrix formulas are intuitive objects rather than memorized symbols.

## Market / Rates Application

Kalman filters are widely used in rates research for:

- latent fair value estimation,
- SOFR signal extraction,
- repo funding pressure,
- Treasury rich / cheap estimation,
- yield curve factors,
- market microstructure noise filtering,
- auction signal interpretation.

Why the framework is so useful:

- hidden state can evolve through time,
- multiple noisy signals can be combined coherently,
- correlated noise can be handled explicitly,
- uncertainty is tracked rather than ignored.

## Interview Follow-ups

- What is the intuition behind the Kalman gain?
- Why is the update based on innovation?
- How does correlation between observations change the update?
- Why is the filter Bayesian?
- What is the geometry of $(1,1)$ versus $(1,-1)$?
- How is Kalman filtering related to recursive least squares?

## Common Mistakes

- Treating Kalman filtering as only a smoothing tool
- Forgetting that covariance is updated together with the state
- Double counting correlated observations
- Memorizing the gain formula without understanding precision weighting
- Missing the difference between state space and observation space

## What To Learn Next

- Bayesian Linear Regression
- Hidden Markov Models
- Particle Filters
- Rauch-Tung-Striebel Smoother
- EM algorithm for parameter estimation
- Dynamic Factor Models
- State-space Yield Curve Models
- Dynamic PCA

## What to Remember

$$
\boxed{\text{Kalman filter = recursive Bayesian estimation for latent state extraction from noisy signals.}}
$$

$$
\boxed{\text{Gain tells you how much to move; innovation tells you why to move.}}
$$

$$
\boxed{\text{Correlated signals must be precision-weighted, not naively averaged.}}
$$

## Connections

Recursive Least Squares, Bayesian Updating, Projection Geometry, Market Microstructure Noise, Yield Curve Factor Models
