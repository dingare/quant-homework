# SC004 — Competing Exponential Clocks and CTMC Hitting

## Problem

A continuous-time Markov chain starts at state $`1`$. From state $`1`$, it jumps to
state $`0`$ at rate $`1`$ and to state $`2`$ at rate $`3`$. Stop at the first jump.
Compute the upper-exit probability, expected stopping time,
$`E[\tau\mathbf1_{\{X_\tau=2\}}]`$, and $`E[\tau\mid X_\tau=2]`$.

## Solution

The two independent clocks are $`T_\downarrow\sim\mathrm{Exp}(1)`$ and
$`T_\uparrow\sim\mathrm{Exp}(3)`$. Their minimum satisfies

```math
\tau\sim\mathrm{Exp}(1+3)=\mathrm{Exp}(4).
```

The identity of the winning clock has probability proportional to its rate:

```math
\boxed{P(X_\tau=2)=\frac34},\qquad
\boxed{E[\tau]=\frac14}.
```

For competing exponentials, the minimum waiting time is independent of which clock
rings first. Therefore,

```math
\boxed{E[\tau\mathbf1_{\{X_\tau=2\}}]=\frac14\frac34=\frac3{16}},
\qquad
\boxed{E[\tau\mid X_\tau=2]=\frac14}.
```

Equivalently, the joint density of an upward jump at time $`t`$ is $`3e^{-4t}`$, so

```math
\int_0^\infty t\,3e^{-4t}\,dt=\frac3{16}.
```

## Interview Takeaways

For clocks with rates $`\lambda_1,\ldots,\lambda_k`$,

```math
T_{\rm next}\sim\mathrm{Exp}(\Lambda),\quad
P(J=i)=\frac{\lambda_i}{\Lambda},\quad \Lambda=\sum_i\lambda_i.
```

The clean independence result relies on exponential waiting times.

## Finance Connection

Limit-order-book events can be modeled as competing clocks for fills, cancellations,
client flow, and adverse price moves. Event probability depends on relative intensity;
waiting time depends on total intensity.

## Citadel Q41 and Stopping-Rule Variants — 2026-11-12

Source: user-supplied Citadel interview-preparation PDF, page 3, Q41, followed by the user's fixed-deadline and repeated-event questions. This section archives the completed discussion; it is not a new timed drill or a claim of independent mastery.

### 1. Original question: stop at the first event

A hedge arrives at rate $`\lambda`$ and pays +1 if it arrives first. A market move arrives at rate $`\mu`$ and pays -1 if it happens first. Find the win probability and expected P&L, and determine whether observing no event so far changes them.

Assume independent waiting times $`T_H\sim\mathrm{Exp}(\lambda)`$ and $`T_M\sim\mathrm{Exp}(\mu)`$, with positive constant rates. The exponential parameters here are rates, not mean durations. The trade ends at $`\tau=\min(T_H,T_M)`$; no fixed deadline is specified.

The win probability follows by integrating over the hedge arrival time while requiring the market clock to survive:

```math
P(T_H\lt T_M)
=\int_0^\infty \lambda e^{-\lambda t}e^{-\mu t}\,dt
=\frac{\lambda}{\lambda+\mu}.
```

Write $`Y`$ for the terminal P&L. Then

```math
\boxed{P(Y=1)=\frac{\lambda}{\lambda+\mu}},\qquad
\boxed{E[Y]=\frac{\lambda-\mu}{\lambda+\mu}}.
```

The total rate determines the time to the first event; each rate's share determines which event wins:

```math
\tau\sim\mathrm{Exp}(\lambda+\mu),\qquad E[\tau]=\frac{1}{\lambda+\mu}.
```

### 2. Why the original question has no fixed time horizon

The payoff rule ends the trade when the first clock rings. An unbounded allowed waiting time does not mean accumulating every future event: only the first event counts.

If a deadline $`t`$ is imposed instead, the payoff for neither event occurring by that deadline must also be specified. In the version discussed here, that payoff is zero. Define $`Y_t`$ as the first-event payoff if the race finishes by $`t`$, and zero otherwise. Then

```math
P(Y_t=1)=\frac{\lambda}{\lambda+\mu}
\left(1-e^{-(\lambda+\mu)t}\right),
```

```math
P(Y_t=-1)=\frac{\mu}{\lambda+\mu}
\left(1-e^{-(\lambda+\mu)t}\right),\qquad
P(Y_t=0)=e^{-(\lambda+\mu)t}.
```

Consequently,

```math
\boxed{E[Y_t]=\frac{\lambda-\mu}{\lambda+\mu}
\left(1-e^{-(\lambda+\mu)t}\right)}.
```

Taking $`t\to\infty`$ recovers the original terminal expectation. A different timeout settlement rule would change this deadline calculation.

### 3. No event yet: conditioning is different from imposing a deadline

Given $`\tau\gt s`$, the two remaining waits are still independent exponentials with their original rates. Thus

```math
\tau-s\mid\tau\gt s\sim\mathrm{Exp}(\lambda+\mu),
```

```math
P(Y=1\mid\tau\gt s)=\frac{\lambda}{\lambda+\mu},\qquad
E[Y\mid\tau\gt s]=\frac{\lambda-\mu}{\lambda+\mu}.
```

These concern the eventual outcome after waiting without an event. They do not turn elapsed time into a settlement deadline. Memorylessness applies to the remaining wait, not to total elapsed time plus the remaining wait.

### 4. Repeated events: count every occurrence without stopping

The user asked what happens if each event can occur many times over an infinite horizon. This changes the payoff rule: every hedge event adds +1 and every market event adds -1, with no stopping at the first event.

Assume independent homogeneous Poisson streams: within each stream, successive interarrival times are independent exponentials with the same constant rate. The waiting times are exponential; the event counts over a fixed interval are Poisson:

```math
N_H(t)\sim\mathrm{Poisson}(\lambda t),\qquad
N_M(t)\sim\mathrm{Poisson}(\mu t),\qquad
X(t)=N_H(t)-N_M(t).
```

Independence gives

```math
\boxed{E[X(t)]=(\lambda-\mu)t},\qquad
\boxed{\mathrm{Var}(X(t))=(\lambda+\mu)t}.
```

Means subtract, while variances add. This cumulative process differs from the first-event payoff with a deadline: later events continue to count.

There is generally no finite terminal cumulative payoff at infinite time. The meaningful long-run quantity is the average payoff per unit time:

```math
\boxed{\frac{X(t)}{t}\longrightarrow\lambda-\mu
\quad\text{almost surely as }t\to\infty}.
```

- If $`\lambda\gt\mu`$, cumulative P&L tends to positive infinity.
- If $`\lambda\lt\mu`$, cumulative P&L tends to negative infinity.
- If $`\lambda=\mu\gt0`$, the expectation is zero at every fixed time, but cumulative P&L does not converge to zero. It fluctuates without a finite limit, and its standard deviation is $`\sqrt{2\lambda t}`$. Its time average still tends to zero.

One can also view each event in the merged stream as a new round. The mean payoff per round and average number of rounds per unit time give the same expected payoff rate:

```math
\frac{\lambda-\mu}{\lambda+\mu}\,(\lambda+\mu)=\lambda-\mu.
```

### 5. When to add rates, multiply probabilities, or add waiting times

For independent $`T_1\sim\mathrm{Exp}(\lambda_1)`$ and $`T_2\sim\mathrm{Exp}(\lambda_2)`$, the event that neither has occurred by time $`t`$ is an intersection. Independence makes its probability a product:

```math
P(\min(T_1,T_2)\gt t)
=P(T_1\gt t)P(T_2\gt t)
=e^{-(\lambda_1+\lambda_2)t}.
```

This is why the minimum has the sum of the rates. It does not say the sum of the waiting times has that exponential distribution.

| Question | Quantity to calculate | Rule |
| --- | --- | --- |
| Wait until either independent clock rings | Minimum waiting time | Exponential with rate $`\lambda_1+\lambda_2`$ |
| Wait until both clocks have rung, starting together | Maximum waiting time | Multiply the two completion probabilities; generally not exponential |
| Complete one waiting stage, then another | Sum of waiting times | Add the means; do not directly add or multiply the rates |
| Retain each Poisson arrival independently with probability $`p`$ | Thinned arrival stream | Poisson with rate $`\lambda p`$ |
| Require independent events to both hold | Intersection probability | Multiply the probabilities |
| Require either of two mutually exclusive events | Union probability | Add the probabilities |

For the maximum and sum, respectively,

```math
P(\max(T_1,T_2)\le t)
=(1-e^{-\lambda_1t})(1-e^{-\lambda_2t}),\qquad t\ge0,
```

```math
E[T_1+T_2]=\frac{1}{\lambda_1}+\frac{1}{\lambda_2}.
```

Adding expectations does not require independence. Multiplying probabilities of intersections generally does; otherwise use conditional probabilities. Adding probabilities of a union directly requires disjoint events:

```math
P(A\cap B)=P(A)P(B\mid A),\qquad P(A)\gt0,
```

```math
P(A\cup B)=P(A)+P(B)-P(A\cap B).
```

The thinning rule connects to Q39: independently marking each swap and FX-forward RFQ as large with probability $`u`$ gives large-RFQ rates $`u\lambda_1`$ and $`u\lambda_2`$. The first large RFQ has rate $`u(\lambda_1+\lambda_2)`$, and its swap probability is $`\lambda_1/(\lambda_1+\lambda_2)`$, for positive rates and $`u\gt0`$.

### 6. What to remember about the variants

| Payoff rule | Expected P&L |
| --- | --- |
| Stop at the first event, without a deadline | $`(\lambda-\mu)/(\lambda+\mu)`$ |
| Stop at the first event, with deadline $`t`$ and zero timeout payoff | $`\frac{\lambda-\mu}{\lambda+\mu}(1-e^{-(\lambda+\mu)t})`$ |
| Count every event through time $`t`$ | $`(\lambda-\mu)t`$ |
| Long-run cumulative P&L per unit time | $`\lambda-\mu`$ almost surely |

Before calculating, identify the stopping rule and what earns a payoff. “No event yet” is information about survival; “no event by the deadline” is a possible settlement outcome.

### Discussion record

On 2026-11-12, the user requested the Q41 solution, questioned why it used eventual rather than fixed-time settlement, and proposed the repeated-event infinite-horizon extension. The assistant explained the calculations above and the related rate/probability rules. No independent derivation, formal rating, elapsed time, or mastery claim is inferred from saving this discussion.

## Connections

- [Waiting Time and Competing Risks Cookbook](../../KnowledgeCards/Probability/Waiting_Time_and_Competing_Risks_Cookbook.md) — 将本题的 exponential race 推广到 non-exponential hazards、Poisson arrivals、queue position、inspection paradox 与 phase-type models。
- [SC006 — Competing Exponentials and Time-Dependent Hazards](SC006_Competing_Exponentials_and_Time_Dependent_Hazards.md) — 比较 exponential 的无记忆性与 Gamma clock 的年龄依赖。
