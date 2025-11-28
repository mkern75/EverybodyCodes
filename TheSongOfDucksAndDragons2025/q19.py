from time import time
from collections import defaultdict

# ********************************* part 1
time_start = time()


def load_gaps(data):
    gaps = defaultdict(list)
    for line in data:
        x, y, sz = map(int, line.split(","))
        gaps[x].append([y, y + sz - 1])
    for lst in gaps.values():
        lst.sort()
    return gaps


def intersect(x1, y1_low, y1_high, x2, y2_low, y2_high):
    assert x1 < x2
    dx = x2 - x1
    y3_low = y1_low - dx
    y3_high = y1_high + dx
    y_low = max(y2_low, y3_low)
    y_low += (x2 + y_low) & 1
    y_high = min(y2_high, y3_high)
    y_high -= (x2 + y_high) & 1
    return (y_low, y_high) if y_low <= y_high else (-1, -1)


def solve(gaps):
    x = 0
    y_reachable = [[0, 0]]
    for x_next in sorted(gaps.keys()):
        y_reachable_next = []
        for y_low, y_high in y_reachable:
            for y_next_gap_low, y_next_gap_high in gaps[x_next]:
                y_next_low, y_next_high = intersect(x, y_low, y_high, x_next, y_next_gap_low, y_next_gap_high)
                if y_next_low != -1:
                    if y_reachable_next and y_next_low <= y_reachable_next[-1][1]:
                        y_reachable_next[-1][1] = y_next_high
                    else:
                        y_reachable_next.append([y_next_low, y_next_high])
        x, y_reachable = x_next, y_reachable_next
    return y_reachable[0][0] + (x - y_reachable[0][0]) // 2


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
