# T005 — Two-Factor Kalman Update for Level and Slope

## Metadata

- Category: Time Series
- Secondary: Linear Algebra, Bayesian Filtering, Rates
- Difficulty: ★★★★☆
- Tags: Kalman Filter, State Space Model, Level, Slope, Innovation, Matrix Gain
- Review Priority: High
- Date Added: 2026-07-23
- Status: Final

## Core Question

A latent rates state is

$$
x_t=(L_t,S_t)^\top,
$$

with transition

$$
x_t=Ax_{t-1}+w_t,\qquad
A=\begin{pmatrix}1&0\\0&0.8\end{pmatrix},
\qquad
Q=\begin{pmatrix}0.04&0\\0&0.09\end{pmatrix}.
$$

At time $t-1$,

$$
\hat x_{t-1|t-1}=\begin{pmatrix}2\\-1\end{pmatrix},
\qquad
P_{t-1|t-1}=
\begin{pmatrix}0.25&0.10\\0.10&0.36\end{pmatrix}.
$$

The observations satisfy

$$
y_t=Hx_t+v_t,\qquad
H=\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad
R=\begin{pmatrix}0.16&0\\0&0.25\end{pmatrix},
$$

and

$$
y_t=\begin{pmatrix}1.8\\3.0\end{pmatrix}.
$$

Compute the prediction, innovation, innovation covariance, Kalman gain, and filtered state.

## Solution

### Prediction

$$
\boxed{
\hat x_{t|t-1}=A\hat x_{t-1|t-1}
=\begin{pmatrix}2\\-0.8\end{pmatrix}
}.
$$

$$
\boxed{
P_{t|t-1}=AP_{t-1|t-1}A^\top+Q
=\begin{pmatrix}
0.29&0.08\\
0.08&0.3204
\end{pmatrix}
}.
$$

### Innovation

The predicted observation is

$$
H\hat x_{t|t-1}
=\begin{pmatrix}1.2\\2.8\end{pmatrix}.
$$

Hence

$$
\boxed{
\nu_t=y_t-H\hat x_{t|t-1}
=\begin{pmatrix}0.6\\0.2\end{pmatrix}
}.
$$

The innovation covariance is

$$
\boxed{
S_t=HP_{t|t-1}H^\top+R
=\begin{pmatrix}
0.9304&-0.0304\\
-0.0304&0.7004
\end{pmatrix}
}.
$$

The off-diagonal entry is nonzero even though $R$ is diagonal: uncertainty in the latent state makes the two observation surprises correlated.

### Gain and Filtered State

$$
K_t=P_{t|t-1}H^\top S_t^{-1}
\approx
\boxed{
\begin{pmatrix}
0.4082&0.3176\\
0.4198&-0.3250
\end{pmatrix}
}.
$$

Therefore

$$
\hat x_{t|t}
=\hat x_{t|t-1}+K_t\nu_t
\approx
\boxed{
\begin{pmatrix}
2.308\\
-0.613
\end{pmatrix}
}.
$$

The observation raises the estimated level and makes the slope less negative.

## Intuition

The update is

$$
\text{posterior}
=\text{prior}
+\text{covariance-adjusted forecast error}.
$$

The first observation is less noisy because $R_{11}=0.16\lt R_{22}=0.25$, but the weights cannot be read from $R$ alone. Each observation loads differently on level and slope, and the prior state covariance also matters.

The negative entry $K_{22}$ is natural: the second observation loads on $L-S$, so a positive surprise tends to push $S$ downward.

## Important Knowledge Points

- Prediction uncertainty is $APA^\top+Q$, not merely $AP$.
- Innovation covariance includes both latent-state uncertainty and measurement noise.
- A diagonal $R$ does not imply a diagonal innovation covariance.
- Kalman gain entries can be negative because observations are linear combinations of several states.
- In implementation, solve systems involving $S_t$; do not explicitly form $S_t^{-1}$.

## Common Mistakes

- Updating level and slope as two unrelated scalar filters.
- Interpreting a negative gain entry as an error.
- Comparing observation variances without considering their loadings.
- Forgetting the process noise $Q$ in the prediction step.

## Interview Follow-Ups

- Compute the posterior covariance using both the simple and Joseph forms.
- What changes when observation errors are correlated?
- What happens as $R\to0$?
- Derive the steady-state gain from the discrete Riccati equation.

## Finance Connection

Level and slope can represent latent yield-curve factors, while the observations are noisy Treasury, futures, or swap quotes. The standardized innovation

$$
z_t=S_t^{-1/2}\nu_t
$$

is a covariance-adjusted measure of curve dislocation.

## What to Remember

$$
\boxed{
\nu=y-H\hat x^-,
\quad
S=HP^-H^\top+R,
\quad
K=P^-H^\top S^{-1},
\quad
\hat x^+=\hat x^-+K\nu
}
$$

