# Daily Testing Results

Interview performance logs, kept separately from canonical question notes and knowledge cards.

## Sessions

| Date | Session | Results in question order | Review / status |
| --- | --- | --- | --- |
| [2026-10-20](2026-10-20.md) | Four-question drill, continued October 21–22; all discussed | Q1–Q4 Partial / Hinted overall; independent subparts preserved; none Pending | Q3 part 1 Cold Solve; Q4 calibration/core scoring and accuracy-limit interpretation correct, arithmetic/writing clarifications preserved; probability evaluation and hit-rate/calibration curves discussed; actual times unknown |
| [2026-10-18](2026-10-18.md) | Four-question drill; all discussed | Q1–Q4 Partial / Hinted | Tree-path states, Gaussian sign geometry, duplicated-data inference and collision timing; Q1 rewrite self-reported/unverified; Q3 arithmetic and Q4 known-method clarifications preserved; actual times unknown |
| [2026-10-17](2026-10-17.md) | Four-question drill; all discussed | Q1–Q4 Partial / Hinted overall; Q2.1 and Q3.1 Cold Solve | Heap state updates (I), long-cycle counting, exact endpoint bounds, signal smoothing / costs; final Q1 user repair unsubmitted; actual times unknown |
| [2026-10-15](2026-10-15.md) | Four-question drill, continued October 16; Q4 completed | Q1–Q3 Partial / Hinted; Q4 Mastered; original cache prompt withdrawn before attempt | Q4 independently solved with conceptual understanding; no further Q4 review needed. Median merge repairs and supplied partition solution; independent coin construction with cost correction; Neyman–Pearson new knowledge taught; Q1 initial approx. 22–23 min, other actual times unknown |
| [2026-10-14](2026-10-14.md) | Retrieval and three-question interview session; final review Pending | R1 Partial / Hinted; R2 independent by user report, submission unverified; Q1–Q3 Partial / Hinted overall | DSU core independent, typo repaired and code tested; weighted inference guided; validation feedback corrected; actual times unknown |
| [2026-10-13](2026-10-13.md) | Survival Mode — continued October 14 | Q1–Q5 Partial / Hinted on main questions; Q5 decision follow-up Pending | Q4 CLT/SE/CI and counterexample reviewed; Q5 Bayes odds explained; Q1 fixes completed by user report; Q1 multiplication follow-up unattempted; actual times unknown |
| [2026-10-11](2026-10-11.md) | Make-up drill October 12; guided continuation October 13 | Q3 independent correct (timing unknown); all seven other questions Partial / Hinted; none Pending | Dijkstra, inference and matrix foundations; reference formulas and review links; actual times unknown |
| [2026-10-10](2026-10-10.md) | Survival Mode — continued October 11 | Q1/Q2/Q4/Q5/Q6 Partial / Hinted; Q3/Q8 Miss; Q7 Partial | A/B and gradient-descent foundations; Q1 initial 12 min, Q2 initial 9 min; other times unrecorded |
| [2026-10-09](2026-10-09.md) | Quant Interview Drill — repeat-audited set | Q1 P/Y; Q2 Y/G; Q3 replacement Y; Q4 original G repeat; Q4 replacement G; Q5 P/Y; Q6a M/P; Q6b G; Q7 Y; Q8/Q9 accidental repeats | All attempted prompts, target budgets, replacement questions, repeat classifications, and review tags; actual times not recorded |
| [2026-10-08](2026-10-08.md) | Quant Interview Drill — broader / harder set | Q1 M/P; Q2 P/Y; Q3 P/M; Q4 P/Y; Q5 G/Y; Q6 G; Q7 Y; Q8 G/Y | All eight prompts and ratings; target times; Q5–Q8 actual 5 min total; tagged knowledge gaps |
| [2026-10-07](2026-10-07.md) | Quant Interview Drill | Q1 P/Y; Q2 G; Q3 P+/Y-G; Q4 P/Y; Q5 G; Q6 G-ish; Q7 Y/G | All seven prompts and ratings; target times; Q5 actual 1 min; Q6 ambiguous timing preserved; review / retrieval notes |
| [2026-10-06](2026-10-06.md) | Quant Interview Drill | Q1 Y; Q2 Y; Q3 G/Y; Q4 Y; Q5 G; Q6 Y+; Q7 Y/G | All seven prompts, ratings, user-reported timings, and concise feedback recorded |

## Recording Convention

- Use the [daily-test template](../Templates/DailyTestTemplate.md): Session → Results → each item's Question / Key solution / Review focus → Next review. October 10–14 logs use this concise format; earlier logs remain historical records.
- Keep complete problem assumptions, the essential derivation or reference code, and **specific weak points**. Omit attempt-by-attempt transcripts and repetitive feedback. Retain only evidence needed for the rating, genuine independent successes, meaningful typo/wording clarifications and code-verification limits.
- Results: **Cold Solve**, **Partial / Hinted**, **Miss**, **Pending**. K = Knowledge, R = Retrieval, I = Implementation; leave K/R unresolved without evidence. Guided completion is not cold mastery. Self-reported completion and directly verified work remain distinguishable.
- **Mastered** records explicitly confirmed independent solving and conceptual understanding, as requested for October 15 Q4. Do not keep mastered items in pending or remedial-review queues.
- Actual time is **Not recorded** unless the user reports it; prompt budgets and timestamps are not elapsed time. A time-capped attempt is not necessarily a completed solve. Unsubmitted code is unverified, not unpracticed.
- Retests are dated observations. Label **intentional spaced repetition**, with the original date, question and gap; accidental repeats do not count as new coverage. Keep removed prompts identifiable by a short source link.
- Use protected inline math and fenced math blocks throughout, including prompts and complexity statements. Follow the [math guide](../Tools/MathMarkdownGuide.md), run the checker, and inspect rendered output.
- Older M/P and G/Y/R ratings retain their original meaning and modifiers; do not retrospectively invent a cold-solve grade. DailyTests do not change finalized subject-note counts in Progress.md.

## Current Training Structure

Updated by the October 15–16 request; supersedes the previous retrieval/review-block format and new-structure cap.

- Give **4–5 substantive interview questions**, in English, without topic labels or initial hints/solutions. Keep realistic budgets; the recent solving preference is approximately 45–60 minutes.
- Prioritize genuinely new interview problems and underlying solution patterns. Avoid superficial variants of familiar material. Prefer algorithmic reasoning over engineering-heavy coding; require runnable Python when appropriate.
- **No separate retrieval or review block.** The user handles revision independently. Save explanations and performance assessment until after an attempt, or an explicit request for help/answers.
- Mainly core interview material, with at most one clearly labeled stretch question. A new foundation should not be treated as a timed retrieval failure; first-learning time is not a familiar-topic solving budget.
- Weekly targets: Coding 35%, Probability 30%, Statistics 20%, ML/Time Series 10%, Linear Algebra/Optimization 5%. Do not force every topic into one session or add filler questions.
- Compare the latest 2–3 tests by underlying solution pattern. Repeat only deliberately for an identified gap; consult [Backlog](../Backlog.md) and recent continuations before proposing supposedly pending questions.
- [October 15 Q4](2026-10-15.md#q4--feasible-correlations-and-zero-variance-portfolios) is **Mastered**, independently solved with conceptual understanding confirmed October 16. No additional Q4 review or remedial practice is needed.

## Navigation

- [Main Index](../INDEX.md)
- [Progress](../Progress.md)
