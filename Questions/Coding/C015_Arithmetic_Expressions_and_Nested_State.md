# C015 — Arithmetic Expressions and Nested State

## Metadata

- Category: Coding
- Tags: Stacks, Parsing, Unary Signs, Scope
- Date Added: 2026-10-22
- Original drill dates: 2026-10-13
- Status: Archived interview material; original follow-up remains Pending; performance is recorded separately below.

## Interview drill — 2026-10-13 Q1

Source and assessment: [2026-10-13 Q1](../../DailyTests/2026-10-13.md#q1--arithmetic-expressions-and-nested-state). The reference material below does not change that attempt’s recorded result.

### Question

Implement runnable Python 3 `evaluate(expression: str) -> int` for valid expressions containing nonnegative integer literals, `+`, `-`, parentheses and whitespace. Consecutive unary signs are allowed; whitespace never splits a literal. Up to 200,000 characters with deep nesting; no `eval`, parsing libraries or recursion-limit changes. Assume constant-cost integer arithmetic. Explain correctness/complexity and run four distinct edge tests.

Examples: `1 - (2 - (3 + 4))` gives 6; `-(-3 + 2) - 4` gives -3; `1--2` gives 3. **Pending follow-up:** how must the representation change for multiplication precedence? No extra implementation required.

### Key solution

Keep a current total, next-operand sign and whether an operand is expected. A stack saves each outer total and connecting sign; closing a parenthesis folds the inner total back into its parent.

```python
def evaluate(expression: str) -> int:
    stack = []
    total = 0
    sign = 1
    expecting_operand = True
    i = 0

    while i < len(expression):
        s = expression[i]
        if s.isspace():
            i += 1
            continue

        if s.isdigit():
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            total += sign * num
            sign = 1
            expecting_operand = False
            continue

        if s in '+-':
            if expecting_operand:
                sign *= 1 if s == '+' else -1
            else:
                sign = 1 if s == '+' else -1
                expecting_operand = True

        if s == '(':
            stack.append((total, sign))
            total = 0
            sign = 1
            expecting_operand = True

        if s == ')':
            outer_total, outer_sign = stack.pop()
            total = outer_total + outer_sign * total
            expecting_operand = False

        i += 1

    return total
```

Each character is scanned once: time $`O(n)`$, auxiliary space $`O(d)`$ for maximum nesting depth $`d`$.

## Assessment history

- [2026-10-13 Q1 — assessment](../../DailyTests/2026-10-13.md#q1--arithmetic-expressions-and-nested-state)

## Related questions and knowledge

- [C018 — Maximum-Sum Path in a Tree](C018_Maximum_Sum_Path_in_a_Tree.md) — Nested state and iterative traversal without deep Python recursion.
