"""Run small independent DP checks: python3 path/to/verify.py.

No network, third-party packages, or test framework required.
"""

import ast
from collections import deque
from itertools import product
from pathlib import Path
from random import Random
import re

import reference as dp


COUNTS: dict[str, int] = {}


def check(group, actual, expected):
    if actual != expected:
        raise AssertionError(f"{group}: got {actual!r}, expected {expected!r}")
    COUNTS[group] = COUNTS.get(group, 0) + 1


def subsets(nums):
    for mask in range(1 << len(nums)):
        yield [nums[i] for i in range(len(nums)) if mask & (1 << i)]


def brute_robber(nums):
    return max(
        sum(nums[i] for i in range(len(nums)) if mask & (1 << i))
        for mask in range(1 << len(nums))
        if not (mask & (mask << 1))
    )


def bfs_coins(coins, amount):
    queue = deque([(0, 0)])
    seen = {0}
    while queue:
        total, count = queue.popleft()
        if total == amount:
            return count
        for coin in coins:
            nxt = total + coin
            if nxt <= amount and nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, count + 1))
    return -1


def brute_lis(nums):
    return max(
        len(seq) for seq in subsets(nums)
        if all(a < b for a, b in zip(seq, seq[1:]))
    )


def brute_stock(prices):
    # Enumerate full action histories, including cash and explicit cooldown.
    def walk(day, holding, cooldown, cash):
        if day == len(prices):
            return cash if not holding else float("-inf")
        outcomes = [walk(day + 1, holding, False, cash)]
        if holding:
            outcomes.append(walk(day + 1, False, True, cash + prices[day]))
        elif not cooldown:
            outcomes.append(walk(day + 1, True, False, cash - prices[day]))
        return max(outcomes)
    return walk(0, False, False, 0)


def brute_game(nums):
    # Fixed Player 1 perspective. No current-player score-difference recurrence.
    def play(remaining, p1_turn, p1_score, p2_score):
        if not remaining:
            return p1_score - p2_score
        choices = [(remaining[0], remaining[1:]),
                   (remaining[-1], remaining[:-1])]
        if p1_turn:
            return max(play(rest, False, p1_score + value, p2_score)
                       for value, rest in choices)
        return min(play(rest, True, p1_score, p2_score + value)
                   for value, rest in choices)
    return play(tuple(nums), True, 0, 0)


def brute_jobs(start, end, profit):
    jobs = list(zip(start, end, profit))
    best = 0
    for chosen in subsets(jobs):
        compatible = all(
            a[1] <= b[0] or b[1] <= a[0]
            for i, a in enumerate(chosen) for b in chosen[i + 1:]
        )
        if compatible:
            best = max(best, sum(job[2] for job in chosen))
    return best


def examples():
    cases = [
        (dp.house_robber, ([2, 1, 4],), 6),
        (dp.house_robber, ([4, 5, 4],), 8),
        (dp.house_robber, ([0],), 0),
        (dp.house_robber, ([],), 0),
        (dp.coin_change, ([1, 3, 4], 6), 2),
        (dp.coin_change, ([3, 5], 7), -1),
        (dp.coin_change, ([2], 0), 0),
        (dp.coin_change, ([2], 4), 2),
        (dp.can_partition, ([1, 5, 11, 5],), True),
        (dp.can_partition, ([2, 2, 3, 5],), False),
        (dp.can_partition, ([1, 2, 5],), False),
        (dp.can_partition, ([1, 2],), False),
        (dp.can_partition, ([],), True),
        (dp.lis_length, ([3, 1, 2, 2, 4],), 3),
        (dp.lis_length, ([1, 2, 3, 0],), 3),
        (dp.lis_length, ([5, 5, 5],), 1),
        (dp.lis_length, ([],), 0),
        (dp.stock_cooldown, ([1, 2, 3, 0, 2],), 3),
        (dp.stock_cooldown, ([1, 2, 0, 3],), 3),
        (dp.stock_cooldown, ([3, 2, 1],), 0),
        (dp.stock_cooldown, ([1],), 0),
        (dp.stock_cooldown, ([],), 0),
        (dp.predict_the_winner, ([1, 5, 2],), False),
        (dp.predict_the_winner, ([1, 5, 233, 7],), True),
        (dp.predict_the_winner, ([1, 1],), True),
        (dp.predict_the_winner, ([],), True),
        (dp.job_scheduling, ([1, 2, 3], [3, 4, 5], [5, 6, 5]), 10),
        (dp.job_scheduling, ([1, 1], [2, 2], [5, 6]), 6),
        (dp.job_scheduling, ([3, 1], [5, 3], [7, 4]), 11),
        (dp.job_scheduling, ([], [], []), 0),
    ]
    for function, args, expected in cases:
        saved = [arg[:] if isinstance(arg, list) else arg for arg in args]
        check("examples", function(*args), expected)
        check("input_unchanged", list(args), saved)


def differential_checks():
    rng = Random(20261025)
    for _ in range(60):
        nums = [rng.randrange(8) for _ in range(rng.randrange(9))]
        check("robber_subset", dp.house_robber(nums), brute_robber(nums))
        positive = [x + 1 for x in nums]
        expected = any(2 * sum(s) == sum(positive) for s in subsets(positive))
        check("partition_subset", dp.can_partition(positive), expected)
        seq = [x - 3 for x in nums]
        check("lis_subset", dp.lis_length(seq), brute_lis(seq))
        coins = sorted(set(rng.randint(1, 8) for _ in range(3)))
        amount = rng.randrange(21)
        check("coin_bfs", dp.coin_change(coins, amount), bfs_coins(coins, amount))

    # All price / game arrays of lengths 0..6 over the alphabet {0,1,2}.
    for length in range(7):
        for values in product(range(3), repeat=length):
            nums = list(values)
            check("stock_actions", dp.stock_cooldown(nums), brute_stock(nums))
            difference = brute_game(nums)
            check("game_difference", dp.winner_score_difference(nums), difference)
            check("game_winner", dp.predict_the_winner(nums), difference >= 0)

    for _ in range(80):
        n = rng.randrange(9)
        start = [rng.randint(1, 7) for _ in range(n)]
        end = [s + rng.randint(1, 4) for s in start]
        profit = [rng.randint(1, 12) for _ in range(n)]
        check("jobs_subset", dp.job_scheduling(start, end, profit),
              brute_jobs(start, end, profit))
    check("negative_profit_extension",
          dp.job_scheduling([1, 2], [2, 3], [-5, -2]), 0)


def check_documented_code():
    directory = Path(__file__).resolve().parent
    reference_tree = ast.parse((directory / "reference.py").read_text())
    expected = {node.name: ast.dump(node, include_attributes=False)
                for node in reference_tree.body if isinstance(node, ast.FunctionDef)}
    solution = (directory / "03_Solutions.md").read_text()
    found = {}
    for block in re.findall(r"```python\n(.*?)\n```", solution, flags=re.S):
        for node in ast.parse(block).body:
            if isinstance(node, ast.FunctionDef):
                found[node.name] = ast.dump(node, include_attributes=False)
    check("documented_code", found, expected)
    if "<!-- CODE " in solution:
        raise AssertionError("Unexpanded solution code placeholder")


if __name__ == "__main__":
    examples()
    differential_checks()
    check_documented_code()
    for group, count in COUNTS.items():
        print(f"{group}: {count} passed")
    print(f"PASS: {sum(COUNTS.values())} checks")
