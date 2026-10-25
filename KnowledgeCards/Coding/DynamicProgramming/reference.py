"""Seven classic DP problems. Python 3.10+, standard library only.

Teaching contracts follow the linked problems; empty inputs are also handled.
Amounts and array values must meet each problem's documented assumptions.
"""

from bisect import bisect_right


def house_robber(nums: list[int]) -> int:
    """LC 198: nonnegative values, adjacent positions cannot both be chosen."""
    prev2 = prev1 = 0
    for value in nums:
        current = max(prev1, prev2 + value)
        prev2, prev1 = prev1, current
    return prev1


def coin_change(coins: list[int], amount: int) -> int:
    """LC 322: positive denominations, unlimited use, nonnegative amount."""
    impossible = amount + 1
    dp = [0] + [impossible] * amount
    for total in range(1, amount + 1):
        for coin in coins:
            if coin <= total:
                dp[total] = min(dp[total], dp[total - coin] + 1)
    return -1 if dp[amount] == impossible else dp[amount]


def can_partition(nums: list[int]) -> bool:
    """LC 416: positive integers; each array position is usable once."""
    total = sum(nums)
    if total % 2:
        return False
    target = total // 2
    possible = [False] * (target + 1)
    possible[0] = True
    for value in nums:
        for subtotal in range(target, value - 1, -1):
            possible[subtotal] = (
                possible[subtotal] or possible[subtotal - value]
            )
    return possible[target]


def lis_length(nums: list[int]) -> int:
    """LC 300: quadratic DP for the strictly increasing subsequence length."""
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def stock_cooldown(prices: list[int]) -> int:
    """LC 309: day-end hold / sold-today / rest, one-day cooldown."""
    hold = sold = float("-inf")
    rest = 0
    for price in prices:
        next_hold = max(hold, rest - price)
        next_sold = hold + price
        next_rest = max(rest, sold)
        hold, sold, rest = next_hold, next_sold, next_rest
    return int(max(rest, sold))


def winner_score_difference(nums: list[int]) -> int:
    """LC 486 helper: optimal current-player minus other-player score."""
    n = len(nums)
    if n == 0:
        return 0
    dp = [[0] * n for _ in range(n)]
    for left in range(n - 1, -1, -1):
        dp[left][left] = nums[left]
        for right in range(left + 1, n):
            dp[left][right] = max(
                nums[left] - dp[left + 1][right],
                nums[right] - dp[left][right - 1],
            )
    return dp[0][n - 1]


def predict_the_winner(nums: list[int]) -> bool:
    """LC 486: both play optimally; a tie counts as a first-player win."""
    return winner_score_difference(nums) >= 0


def job_scheduling(
    start_time: list[int], end_time: list[int], profit: list[int]
) -> int:
    """LC 1235: start < end; touching endpoints are compatible."""
    jobs = sorted(zip(start_time, end_time, profit), key=lambda job: job[1])
    ends = [end for _, end, _ in jobs]
    dp = [0] * (len(jobs) + 1)
    for i, (start, _, reward) in enumerate(jobs):
        compatible_count = bisect_right(ends, start, 0, i)
        dp[i + 1] = max(dp[i], dp[compatible_count] + reward)
    return dp[-1]
