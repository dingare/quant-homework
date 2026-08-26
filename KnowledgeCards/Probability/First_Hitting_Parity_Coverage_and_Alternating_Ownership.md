# First-Hitting Parity, Coverage, and Alternating Ownership

## Purpose

This card organizes a recurring problem pattern: a random walk first visits a location at a first-hitting time; the parity of that time determines whose turn it is; and the final payoff is the sum of the ownership indicators for all targets. [P011 — Parity of First-Hitting Times on an Odd Cycle](../../Questions/Probability/P011_Parity_of_First_Hitting_Times_on_an_Odd_Cycle.md) is the representative problem, but the same framework also covers gambler's ruin, path or cycle coverage, alternating ownership, and second-order difference equations.

The main decision split is:

$$
\text{expected total only}\Rightarrow\text{indicators and linearity of expectation};
$$

$$
\text{boundary identity or mean time only}\Rightarrow\text{first-step recursion or martingales};
$$

$$
\text{hitting-time parity or alternating ownership}\Rightarrow\text{augment the state or use a parity-flipping recursion}.
$$

## 1. Base Template: Gambler's Ruin

Consider a nearest-neighbor random walk on $\{0,1,\ldots,N\}$. Let $X_0=i$, where $0\lt i\lt N$. At each step the walk moves one unit to the right with probability $p$ and one unit to the left with probability $q=1-p$. The process stops upon reaching $0$ or $N$, so these are absorbing boundaries. Define the first time either boundary is reached by

$$
T=\inf\{t\ge0:X_t\in\{0,N\}\}.
$$

Equivalently, a gambler starts with capital $i$, wins one unit with probability $p$, and loses one unit with probability $q$. We ask whether the gambler goes broke at $0$ before building the bankroll to $N$.

### Boundary-Hitting Probability: What Are We Computing?

The quantity of interest is not the probability of being at $N$ at some fixed time. It is the probability, starting from $i$, of hitting $N$ before hitting $0$. Write

$$
h_i=P_i(X_T=N)=P_i(T_N\lt T_0),
$$

where

$$
T_0=\inf\{t\ge0:X_t=0\},
\qquad
T_N=\inf\{t\ge0:X_t=N\},
\qquad
T=T_0\wedge T_N.
$$

The subscript $i$ means that $X_0=i$. A nearest-neighbor path cannot cross a boundary without first touching it, so the stopped position is either $0$ or $N$. Consequently,

$$
X_T=N\mathbf1_{\{T_N\lt T_0\}},
\qquad
E_i[X_T]=Nh_i.
$$

This identity connects the expected stopped position directly to the required first-hitting probability and is the key to the martingale solution.

#### Fair Walk: Martingale and Optional-Stopping Derivation

When $p=q=1/2$,

$$
E[X_{t+1}\mid\mathcal F_t]=X_t,
$$

so $X_t$ is a martingale. Intuitively, a fair game has no directional advantage at the next step, and the conditional expected capital remains unchanged before absorption.

The safest optional-stopping argument first uses the bounded stopping time $T\wedge n$. The optional stopping theorem gives

$$
E_i[X_{T\wedge n}]=E_i[X_0]=i.
$$

For an absorbing random walk on a finite interval, $T\lt\infty$ almost surely. Moreover, $0\le X_{T\wedge n}\le N$. Thus $X_{T\wedge n}\to X_T$, and bounded convergence allows us to let $n\to\infty$:

$$
E_i[X_T]=i.
$$

On the other hand, $X_T$ takes only the values $0$ and $N$, so

$$
E_i[X_T]
=0\cdot P_i(X_T=0)+N\cdot P_i(X_T=N)
=Nh_i.
$$

Comparing the two expressions yields

$$
Nh_i=i,
\qquad
\boxed{h_i=\frac{i}{N}}.
$$

Therefore,

$$
P_i(T_0\lt T_N)=1-h_i=1-\frac{i}{N}.
$$

The interview-level intuition is one sentence: the expected capital in a fair game stays at $i$, and the terminal capital can only be $0$ or $N$, so the probability of finishing at $N$ must be $i/N$.

#### Biased Walk: Constructing an Exponential Martingale

When $p\ne q$, $X_t$ is no longer a martingale because its one-step drift is $p-q$. Set

$$
r=\frac qp,
\qquad
M_t=r^{X_t}.
$$

Then

$$
E[M_{t+1}\mid\mathcal F_t]
=r^{X_t}\left(pr+\frac q r\right)
=r^{X_t}(q+p)
=M_t,
$$

so $M_t=(q/p)^{X_t}$ is a martingale. Again, first stop at $T\wedge n$. Because $X_{T\wedge n}\in\{0,1,\ldots,N\}$, the stopped martingale is bounded between two finite constants. Combining this boundedness with $T\lt\infty$ almost surely and taking limits gives

$$
E_i[r^{X_T}]=r^i.
$$

At absorption, $X_T$ is either $0$ or $N$. Hence

$$
r^i
=r^0P_i(X_T=0)+r^NP_i(X_T=N)
=(1-h_i)+r^Nh_i.
$$

Rearranging,

$$
r^i-1=h_i(r^N-1),
$$

and therefore

$$
\boxed{
h_i=\frac{1-r^i}{1-r^N}
=\frac{1-(q/p)^i}{1-(q/p)^N}
},
\qquad p\ne q.
$$

The probability of hitting the lower boundary first remains $1-h_i$. If $p\gt q$, the rightward drift makes $h_i$ larger than the fair-walk value $i/N$; if $p\lt q$, it makes $h_i$ smaller. This is a quick check that the ratio has not been inverted. As $p\to q$, the biased formula converges to $i/N$.

#### Equivalent Route: First-Step Analysis and Boundary Recurrence

The same probability $h_i=P_i(T_N\lt T_0)$ can be found without martingales. From an interior state $i$, the first step moves to $i+1$ with probability $p$ and to $i-1$ with probability $q$. By the Markov property, the conditional probabilities of subsequently hitting $N$ first are $h_{i+1}$ and $h_{i-1}$. Therefore,

$$
h_i=ph_{i+1}+qh_{i-1},
\qquad h_0=0,\quad h_N=1.
$$

The boundary conditions are part of the event definition: starting from $0$ is already failure, whereas starting from $N$ is already success.

For a fair walk, the recurrence becomes

$$
h_{i+1}-h_i=h_i-h_{i-1}.
$$

The neighboring differences are constant, so $h_i=A+Bi$. Substituting $h_0=0$ and $h_N=1$ gives

$$
h_i=\frac{i}{N},
$$

in agreement with optional stopping.

For a biased walk, substitute $h_i=\lambda^i$ into the recurrence to obtain the characteristic equation

$$
p\lambda^2-\lambda+q=0.
$$

Its roots are $1$ and $q/p$, so the general solution of the second-order difference equation is

$$
h_i=A+B\left(\frac qp\right)^i.
$$

Applying the two boundary conditions produces

$$
h_i=\frac{1-(q/p)^i}{1-(q/p)^N},
$$

again matching the exponential-martingale result. These approaches do not compute different quantities: both begin with the same event $\{T_N\lt T_0\}$. First-step analysis uses the local recurrence satisfied by its probability, whereas the martingale method uses a global expectation constraint at the stopped position. In an interview, the martingale route is usually shorter when the boundaries are simple and the martingale is apparent; first-step recursion is often safer when the state is more complicated, overshoot is possible, or extra conditions are imposed.

### Mean Absorption Time

Let $e_i=E_i[T]$. First-step analysis gives

$$
e_i=1+pe_{i+1}+qe_{i-1},
\qquad e_0=e_N=0.
$$

For a fair walk,

$$
e_i=i(N-i).
$$

This also follows from the martingale $X_t^2-t$ and optional stopping. In the biased case, let $\mu=p-q$. Then $X_t-\mu t$ is a martingale. Combining optional stopping with $E_i[X_T]=Nh_i$ gives

$$
e_i=\frac{Nh_i-i}{p-q}
=\frac{i-Nh_i}{q-p}.
$$

Because the state space is finite, absorption occurs almost surely and $E[T]\lt\infty$, so these stopping arguments can be made rigorous. On an unbounded domain, with unbounded jumps, or for a stopping time that may have infinite expectation, it is not enough to write “by optional stopping”; one must check bounded stopping times, uniform integrability, or an appropriate integrable domination condition. See [P002](../../Questions/Probability/P002_Optional_Stopping_Fair_Games_and_Why_Stop_Loss_Does_Not_Create_Alpha.md).

### What This Base Template Does Not Record

$h_i$ identifies the exit boundary, and $e_i$ gives the mean time to exit. Neither tells us whether $T$ is odd or even. If alternating turns make ownership depend on $T\bmod2$, time parity must be retained in the state.

## 2. Four Connected Problem Families

### A. First Hitting and Gambler's Ruin

- **Recognition cues:** “Which boundary is reached first?”, “Reach a target before ruin,” or “Does take-profit or stop-loss trigger first?”
- **Standard tools:** $h_i=ph_{i+1}+qh_{i-1}$; for mean time use $e_i=1+pe_{i+1}+qe_{i-1}$; for simple boundaries, consider martingales and optional stopping first.
- **What it captures:** Exit identity, hitting probability, and mean stopping time. For unequal steps and overshoot, use a finite-state system instead; see [P007](../../Questions/Probability/P007_Unequal_Jump_Random_Walk_First_Step_Analysis.md).
- **What it misses:** Position alone does not record hitting-time parity, visit order, or the complete path.
- **Interview variants:** Biased coins, asymmetric boundaries, conditional hitting times, unequal jumps and overshoot, and Brownian motion with drift.

### B. Parity-Augmented Hitting Times and Alternating Turns

- **Recognition cues:** “First arrive after an odd or even number of steps,” “Two players alternate moves,” or “Which player receives the first-visit reward?”
- **Standard tools:** Augment the state to $(X_t,t\bmod2)$; alternatively, let $q_i=P_i(T\text{ is odd})$. For a fair walk,

$$
q_i=1-\frac{q_{i-1}+q_{i+1}}2.
$$

- **Role of martingales:** The ordinary $X_t$ martingale is insufficient. Incorporate $(-1)^t$ or the probability generating function $z^T$; evaluating at $z=-1$ extracts the parity imbalance.
- **What it captures:** First-hitting parity and alternating ownership.
- **What it misses:** Marginal ownership probabilities for individual targets generally do not reveal dependence among targets or the final win probability. The win probability also needs structural constraints.
- **Interview variants:** Two-layer parity states for a biased walk, rotation every $k$ steps, player-specific weights, and the joint probability of a boundary and a parity.

### C. Coverage and Visited Sets on Paths and Cycles

- **Recognition cues:** “Collect a reward on the first visit to each vertex,” “Continue until every vertex is covered,” or “Cut the cycle or lift it to the integer line.”
- **Standard structure:** The visited set of a one-dimensional walk is always an interval $[\min X_t,\max X_t]$. A cycle can be cut into an interval whose endpoints represent a target, or lifted to the integer line so that its range can be studied.
- **Role of linearity of expectation:** For a target $v$, define $I_v=\mathbf1\{v\text{ belongs to a given player}\}$. Then $E[\sum_v I_v]=\sum_vP(I_v=1)$; independence is not required.
- **What it captures:** Expected coverage payoff, the last unvisited vertex, and bipartite coloring constraints on a path. In P011, deleting the final vertex leaves an even-length path, forcing the final scores to differ by exactly one.
- **What it misses:** Linearity of expectation alone does not give variance, joint ownership, or win probability. One must additionally prove the support of the possible scores or compute joint probabilities.
- **Interview variants:** Even versus odd cycles, weighted vertices, nonuniform starting points, path cover time, the distribution of the last-visited vertex, and whether bipartite structure still helps on a general graph.

### D. Second-Order Difference Equations

- **Recognition cues:** Nearest-neighbor first-step analysis connects only $i-1$, $i$, and $i+1$, with two boundary conditions.
- **Standard tools:** For a homogeneous recurrence, try $a_i=\lambda^i$. For a nonhomogeneous term, first find a particular solution or shift the sequence. Distinct roots give $A\lambda_1^i+B\lambda_2^i$; a repeated root gives

$$
a_i=(A+Bi)\lambda^i.
$$

- **Role in parity problems:** After shifting by $r_i=q_i-1/2$, the characteristic equation is $(\lambda+1)^2=0$, so the term $(A+Bi)(-1)^i$ must be retained. The negative root represents alternation, and the repeated root creates a linear envelope.
- **What it captures:** Boundary hitting, mean time, discounted quantities, and parity generating functions as boundary-value problems.
- **What it misses:** The equation cannot choose the correct state, event, or boundary conditions for you. If parity is omitted from the state, an elegant solution still answers the wrong question.
- **Interview variants:** Geometric roots for a biased walk, constant nonhomogeneous terms, repeated roots, the $z^T$ generating function, and higher-order recurrences from larger jumps. See the [second-order difference equations card](Second_Order_Difference_Equations_for_Random_Walk_Hitting_Problems.md).

## 3. Recognition and Method-Selection Decision Tree

1. **Is the outcome a sum of rewards over targets?** If yes, first assign an ownership indicator to each target and use linearity of expectation; do not start by seeking the joint distribution.
2. **For one target, does the event depend only on which boundary is hit first?** If yes, cut the graph into an interval and write the ordinary hitting recurrence; when the boundaries are simple, a martingale may be shorter.
3. **Does the acting player rotate with the step count, or does the problem ask about odd/even arrival?** If yes, immediately add $t\bmod2$ to the state or write a recursion in which parity flips after one step.
4. **Is the mean stopping time required?** Add the current step's $+1$ to the probability recurrence. In the fair case consider $X_t^2-t$; in the biased case consider $X_t-(p-q)t$.
5. **Does the problem ask about covering a path or cycle?** Check whether the visited set is an interval, whether the cycle can be cut, and whether bipartite coloring or a last-vertex argument applies.
6. **Did first-step analysis produce a nearest-neighbor linear recurrence?** Solve the second-order difference equation: find a particular solution first, then check for repeated roots and impose both boundary conditions.
7. **Do you want to infer a win probability from an expectation?** This is valid only after proving that the final value has exactly two possible outcomes; otherwise, the expectation does not determine the win probability.

## 4. Review Path from Simple to Complex

| Order | Problem to Master | Why It Comes Next | New Ingredient | Entry |
| --- | --- | --- | --- | --- |
| 1 | **Start here: fair gambler's ruin.** From $i$, find the probability of reaching $N$ first and the mean absorption time | Establishes the common language of boundary values, first-step recursion, and optional stopping | Harmonic recurrence; $X_t$ and $X_t^2-t$ | [P002](../../Questions/Probability/P002_Optional_Stopping_Fair_Games_and_Why_Stop_Loss_Does_Not_Create_Alpha.md) |
| 2 | Biased gambler's ruin | Shows a linear solution becoming geometric on the same state space | $(q/p)^{X_t}$; centered martingale; two distinct characteristic roots | Section 1 of this card |
| 3 | Finite-interval exit with unequal step sizes | Prevents mechanical use of nearest-neighbor formulas | Overshoot; finite-state linear system | [P007](../../Questions/Probability/P007_Unequal_Jump_Random_Walk_First_Step_Analysis.md) |
| 4 | Probability that interval absorption occurs at an odd time | First problem that forces recognition that position alone is insufficient | Parity flip; $(X_t,t\bmod2)$; repeated root $-1$ | [Second-order difference equations card](Second_Order_Difference_Equations_for_Random_Walk_Hitting_Problems.md) |
| 5 | Expected first-visit rewards on a path | Extends one target to many dependent targets | Indicators; linearity of expectation without independence | [Indicator Cookbook](Indicator_Random_Variables_Cookbook.md) |
| 6 | **P011: alternating ownership on an odd cycle** | Combines hitting parity, cutting a cycle, interval coverage, and score structure | Integer-line lift; last vertex; bipartite path; expectation to win probability | [P011](../../Questions/Probability/P011_Parity_of_First_Hitting_Times_on_an_Odd_Cycle.md) |
| 7 | Biased, weighted, or even-cycle versions | Tests which conclusions rely on fairness, uniformity, and odd-cycle structure | Two-layer recurrence; weighted linearity; bipartite exceptions | P011 Practice Variants |

At every stage, answer four questions: What is the state? What are the boundaries? What is the one-step recursion? What information does the state omit?

## 5. Where P011 Fits

P011 uses all four families. Ordinary gambler's ruin shows that the endpoint parameter of the eventually covered interval on the integer lift is uniform. Matching coordinate parity with time parity maps first visits to player ownership. Indicators and linearity of expectation aggregate the ownership of every brick. The parity-flipping recursion produces the repeated root $-1$. Finally, deleting the last vertex leaves a bipartite path, allowing the expected score difference to be converted into a win probability.

The most important diagnosis is therefore not whether one remembers a particular closed form, but this distinction:

$$
\boxed{
\text{Ordinary hitting needs position only; alternating ownership must retain the time phase.}
}
$$

## Connections

- [P011 — Parity of First-Hitting Times on an Odd Cycle](../../Questions/Probability/P011_Parity_of_First_Hitting_Times_on_an_Odd_Cycle.md)
- [P002 — Optional Stopping](../../Questions/Probability/P002_Optional_Stopping_Fair_Games_and_Why_Stop_Loss_Does_Not_Create_Alpha.md)
- [P007 — Unequal-Jump Random Walk](../../Questions/Probability/P007_Unequal_Jump_Random_Walk_First_Step_Analysis.md)
- [Indicator Random Variables Cookbook](Indicator_Random_Variables_Cookbook.md)
- [Second-Order Difference Equations for Random-Walk Hitting Problems](Second_Order_Difference_Equations_for_Random_Walk_Hitting_Problems.md)

## What to Remember

$$
\boxed{
\text{First ask whether the state is sufficient; then choose linearity, a martingale, or parity augmentation.}
}
$$
