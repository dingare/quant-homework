# SC004 — Competing Exponential Clocks and CTMC Hitting

## Problem

A continuous-time Markov chain starts at state \(1\). From state \(1\), it jumps to
state \(0\) at rate \(1\) and to state \(2\) at rate \(3\). Stop at the first jump.
Compute the upper-exit probability, expected stopping time,
\(E[\tau\mathbf1_{\{X_\tau=2\}}]\), and \(E[\tau\mid X_\tau=2]\).

## Solution

The two independent clocks are \(T_\downarrow\sim\mathrm{Exp}(1)\) and
\(T_\uparrow\sim\mathrm{Exp}(3)\). Their minimum satisfies

\[
\tau\sim\mathrm{Exp}(1+3)=\mathrm{Exp}(4).
\]

The identity of the winning clock has probability proportional to its rate:

\[
\boxed{P(X_\tau=2)=\frac34},\qquad
\boxed{E[\tau]=\frac14}.
\]

For competing exponentials, the minimum waiting time is independent of which clock
rings first. Therefore,

\[
\boxed{E[\tau\mathbf1_{\{X_\tau=2\}}]=\frac14\frac34=\frac3{16}},
\qquad
\boxed{E[\tau\mid X_\tau=2]=\frac14}.
\]

Equivalently, the joint density of an upward jump at time \(t\) is \(3e^{-4t}\), so

\[
\int_0^\infty t\,3e^{-4t}\,dt=\frac3{16}.
\]

## Interview Takeaways

For clocks with rates \(\lambda_1,\ldots,\lambda_k\),

\[
T_{\rm next}\sim\mathrm{Exp}(\Lambda),\quad
P(J=i)=\frac{\lambda_i}{\Lambda},\quad \Lambda=\sum_i\lambda_i.
\]

The clean independence result relies on exponential waiting times.

## Finance Connection

Limit-order-book events can be modeled as competing clocks for fills, cancellations,
client flow, and adverse price moves. Event probability depends on relative intensity;
waiting time depends on total intensity.
