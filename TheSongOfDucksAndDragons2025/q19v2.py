from time import time
from collections import defaultdict

# ********************************* part 1
time_start = time()


def load_gaps(data):
    gaps = defaultdict(list)
    for line in data:
        x, y, sz = map(int, line.split(","))
        gaps[x].append((y, y + sz - 1))
    return gaps


def is_reachable(x1, y1, x2, y2):
    assert x1 < x2
    assert abs(x2 - x1) & 1 == abs(y2 - y1) & 1
    return abs(y2 - y1) <= x2 - x1


def solve(gaps):
    x_prev = 0
    reachable_prev = {0}
    for x in sorted(gaps.keys()):
        reachable = set()
        for y1, y2 in gaps[x]:
            for y in range(y1, y2 + 1):
                if (x + y) & 1:
                    continue
                for y_prev in reachable_prev:
                    if is_reachable(x_prev, y_prev, x, y):
                        reachable.add(y)
                        break
        x_prev, reachable_prev = x, reachable
    x_sol, y_sol = x_prev, min(reachable_prev)
    return y_sol + (x_sol - y_sol) // 2


INPUT_FILE = "./data/q19_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

gaps = load_gaps(data)
ans1 = solve(gaps)

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()

INPUT_FILE = "./data/q19_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

gaps = load_gaps(data)
ans2 = solve(gaps)

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()

INPUT_FILE = "./data/q19_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

gaps = load_gaps(data)
ans3 = solve(gaps)

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
