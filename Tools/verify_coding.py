"""Run the actual Python blocks in every coding note and independent small-case oracles.

Usage: python3 Tools/verify_coding.py
Question-signature stubs are executed before their complete implementations.
Each note has its own namespace; no copied implementation is tested instead.
"""
import contextlib
import io
import itertools
from pathlib import Path
import random
import re
import statistics

ROOT = Path(__file__).resolve().parents[1]


def load_notes():
    notes = {}
    for path in sorted((ROOT / 'Questions/Coding').glob('*.md')):
        namespace = {'__name__': '__coding_reference__'}
        blocks = re.findall(r'^```python\n(.*?)^```\s*$', path.read_text(), re.M | re.S)
        assert blocks, f'{path.name}: missing Python implementation'
        for index, block in enumerate(blocks, 1):
            with contextlib.redirect_stdout(io.StringIO()):
                exec(compile(block, f'{path.name}:block{index}', 'exec'), namespace)
        notes[path.name.split('_')[0]] = namespace
    return notes


def verify(notes):
    rng = random.Random(20261108)
    def f(id, name):
        return notes[id][name]

    for _ in range(350):
        a = [rng.randrange(-5, 6) for _ in range(rng.randrange(10))]
        original = a[:]
        lower, upper = sorted([rng.randrange(-8, 9), rng.randrange(-8, 9)])
        sums = [sum(a[i:j]) for i in range(len(a)) for j in range(i + 1, len(a) + 1)]
        expected = sum(lower <= s <= upper for s in sums)
        assert f('C001', 'count_range_sums')(a, lower, upper) == expected
        assert f('C001', 'count_range_sums_merge')(a, lower, upper) == expected
        target = rng.randrange(1, 10)
        lengths = [j-i for i in range(len(a)) for j in range(i+1, len(a)+1)
                   if sum(a[i:j]) >= target]
        length, window = f('C002', 'shortest_subarray_at_least_k')(a, target)
        assert length == min(lengths, default=-1)
        if window is not None:
            i, j = window
            assert j-i+1 == length and sum(a[i:j+1]) >= target
        binary = [rng.randrange(2) for _ in a]
        expected = max([0] + [j-i for i in range(len(a)) for j in range(i+1, len(a)+1)
                              if sum(binary[i:j])*2 == j-i])
        assert f('C007', 'longest_balanced')(binary) == expected
        expected = 0
        for value in set(a):
            end = value
            while end in set(a):
                end += 1
            expected = max(expected, end-value)
        for name in ('longest_consecutive', 'longest_consecutive_boundary'):
            assert f('C006', name)(a) == expected
        lis = [1] * len(a)
        for j in range(len(a)):
            lis[j] = 1 + max([0] + [lis[i] for i in range(j) if a[i] < a[j]])
        if 'C020' in notes:
            assert f('C020', 'min_deletions')(a) == len(a)-max(lis, default=0)
        if a:
            online = f('C003', 'OnlineMedian')()
            for i, x in enumerate(a):
                online.add(x)
                assert online.median() == statistics.median(a[:i+1])
            for k in range(1, len(a)+1):
                expected = [statistics.median(a[i:i+k]) for i in range(len(a)-k+1)]
                assert f('C003', 'rolling_medians')(a, k) == expected
                expected = [max(a[i:i+k]) for i in range(len(a)-k+1)]
                for name in ('max_sliding_window_tree', 'max_sliding_window_dp', 'max_sliding_window_deque'):
                    assert f('C004', name)(a, k) == expected
                assert f('C004', 'Solution')().maxSlidingWindow(a, k) == expected
                expected = max(range(len(a)-k+1), key=lambda i: sum(a[i:i+k]))
                assert f('C005', 'max_sum_fixed_k')(a, k) == expected
                candidates = [(sum(a[i:j]), -i, -j, i, j)
                              for i in range(len(a)) for j in range(i+k, len(a)+1)]
                total, _, _, i, j = max(candidates)
                for name in ('max_sum_at_least_k', 'max_sum_at_least_k_constant_space'):
                    assert f('C005', name)(a, k) == (i, j, total)
                expected = sorted(a, reverse=True)[k-1]
                for name in ('kth_largest_heap', 'kth_largest_quickselect'):
                    assert f('C010', name)(a, k) == expected
            positives = [abs(x)+1 for x in a]
            k = rng.randrange(1, len(a)+2)
            best = sum(positives)
            for mask in range(1 << (len(a)-1)):
                groups, total = [], positives[0]
                for i, x in enumerate(positives[1:]):
                    if mask >> i & 1:
                        groups.append(total)
                        total = 0
                    total += x
                groups.append(total)
                if len(groups) <= k:
                    best = min(best, max(groups))
            assert f('C009', 'minimize_largest_group_sum')(positives, k) == best
        assert a == original

    for _ in range(350):
        n = rng.randrange(1, 8)
        edges = [(rng.randrange(n), rng.randrange(n), rng.randrange(6)) for _ in range(rng.randrange(14))]
        s, t = rng.randrange(n), rng.randrange(n)
        # Independent Bellman-Ford on an explicitly materialized two-layer graph.
        expanded = []
        for u, v, cost in edges:
            expanded.extend([(2*u, 2*v, cost), (2*u+1, 2*v+1, cost), (2*u, 2*v+1, 0)])
        dist = [float('inf')] * (2*n)
        dist[2*s] = 0
        for _ in range(2*n-1):
            for u, v, cost in expanded:
                dist[v] = min(dist[v], dist[u]+cost)
        expected = min(dist[2*t:2*t+2])
        assert f('C013', 'cheapest_trip')(n, edges, s, t) == (expected if expected < float('inf') else -1)
        jobs = []
        for _ in range(rng.randrange(9)):
            start = rng.randrange(6)
            jobs.append((start, start+rng.randrange(1, 5), rng.randrange(-3, 10)))
        best = 0
        for mask in range(1 << len(jobs)):
            chosen = sorted(jobs[i] for i in range(len(jobs)) if mask >> i & 1)
            if all(a[1] <= b[0] for a, b in zip(chosen, chosen[1:])):
                best = max(best, sum(job[2] for job in chosen))
        assert f('C014', 'max_profit')(jobs) == best
        intervals = [(s, e) for s, e, p in jobs]
        count, allocation = f('C017', 'allocate_units')(intervals)
        expected = max([0] + [sum(s <= point < e for s,e in intervals) for point in range(10)])
        assert count == expected and len(allocation) == len(intervals)
        assert all(0 <= unit < count for unit in allocation)
        for i, j in itertools.combinations(range(len(intervals)), 2):
            if allocation[i] == allocation[j]:
                assert intervals[i][1] <= intervals[j][0] or intervals[j][1] <= intervals[i][0]
        a = sorted(rng.randrange(-4, 5) for _ in range(rng.randrange(8)))
        b = sorted(rng.randrange(-4, 5) for _ in range(rng.randrange(8)))
        k = rng.randrange(30)
        if 'C022' in notes:
            assert f('C022', 'smallest_sums')(a,b,k) == sorted(x+y for x in a for y in b)[:k]
        if a or b:
            assert f('C016', 'combined_median')(a,b) == statistics.median(a+b)
        source = ''.join(rng.choice('abc') for _ in range(rng.randrange(8)))
        target = ''.join(rng.choice('abc') for _ in range(rng.randrange(8)))
        assert f('C012', 'min_changes')(source,target) == f('C012', 'min_changes_rolling')(source,target)

    # Trigger heap rebuilding on long monotone streams and repeated values.
    for a in (list(range(5000)), list(range(5000, 0, -1)), [2]*5000):
        for k in (1, 2, 7, 32):
            assert f('C003', 'rolling_medians')(a,k) == [statistics.median(a[i:i+k]) for i in range(len(a)-k+1)]


if __name__ == '__main__':
    notes = load_notes()
    verify(notes)
    print(f'PASS: {len(notes)} coding notes, all Python blocks and seeded reference comparisons')
