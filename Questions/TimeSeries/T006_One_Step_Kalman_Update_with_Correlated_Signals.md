# T006 — One-Step Kalman Update with Correlated Signals

## Problem

Let $x_t=0.9x_{t-1}+w_t$, with $\mathrm{Var}(w_t)=1$, and suppose
$x_{t-1}\mid\mathcal F_{t-1}\sim N(2,4)$. Observe

$$
y=Hx_t+v,quad H=(1,2)^\top,quad y=(3,5)^\top,quad
R=\begin{pmatrix}1&1\\1&4\end{pmatrix}.
$$

Perform one Kalman prediction and update. Can the observations be processed sequentially?

## Solution

Prediction:

$$
m^-=0.9(2)=1.8,qquad P^-=0.9^2(4)+1=4.24.
$$

Innovation and its covariance:

$$
\nu=y-Hm^-=\begin{pmatrix}1.2\\1.4\end{pmatrix},qquad
S=HP^-H^\top+R=\begin{pmatrix}5.24&9.48\\9.48&20.96\end{pmatrix}.
$$

Since $\det(S)=19.96=499/25$,

$$
K=P^-H^\top S^{-1}
=\boxed{\left(\frac{212}{499},\frac{106}{499}\right)}
\approx(0.42485,0.21242).
$$

Therefore,

$$
m=m^-+K\nu=\boxed{\frac{1301}{499}\approx2.60721},
$$

and

$$
P=(1-KH)P^-=\boxed{\frac{318}{499}\approx0.63727}.
$$

Hence

$$
x_t\mid\mathcal F_t\sim
N\left(\frac{1301}{499},\frac{318}{499}\right).
$$

## Sequential Processing

Naively treating the measurements as independent is wrong because $R_{12}=1$.
Sequential processing becomes valid after decorrelation. For example,

$$
\widetilde y_2=y_2-y_1=x_t+(v_2-v_1),
$$

and $\mathrm{Cov}(v_1,v_2-v_1)=1-1=0$. Gaussianity then makes the
transformed measurement errors independent.

## Finance Connection

Cash, futures, and swap signals often share liquidity or macro noise. A joint update
prevents the filter from double-counting that shared information.
