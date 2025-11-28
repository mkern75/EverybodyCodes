from time import time
from collections import defaultdict

INF = 1 << 31

# ********************************* part 1
time_start = time()


def load_gaps(data):
    gaps = defaultdict(list)
    for line in data:
        x, y, sz = map(int, line.split(","))
        gaps[x].append((y, y + sz + 1))
    return gaps


def calc_dist(x1, y1, x2, y2):
    assert x1 < x2
    dx = x2 - x1
    dy = y2 - y1
    assert dx & 1 == dy & 1
    if abs(dy) > abs(dx):
        return INF
    res = 0
    if dy > 0:
        res += dy
    dx -= abs(dy)
    res += dx // 2
    return res


def solve(gaps):
    dist = defaultdict(lambda: INF)
    dist[0, 0] = 0
    for x in sorted(gaps.keys()):
        dist_next = defaultdict(lambda: INF)
        for y1, y2 in gaps[x]:
            for y in range(y1, y2 + 1):
                if (x + y) & 1:
                    continue
                for (x_from, y_from), d in dist.items():
                    d_extra = calc_dist(x_from, y_from, x, y)
                    if d_extra != INF:
                        dist_next[x, y] = dist[x_from, y_from] + d_extra
                        break
        dist = dist_next
    return min(dist.values())


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
