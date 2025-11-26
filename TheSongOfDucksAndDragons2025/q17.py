from time import time
from heapq import heappop, heappush

INF = 1 << 31

# ********************************* part 1
time_start = time()


def load_grid(data):
    n_rows, n_cols = len(data), len(data[0])
    rv, cv = 0, 0
    rs, cs = 0, 0
    grid = [[0] * n_cols for _ in range(n_rows)]
    for r in range(n_rows):
        for c in range(n_cols):
            if data[r][c] == "@":
                rv, cv = r, c
            elif data[r][c] == "S":
                rs, cs = r, c
            else:
                grid[r][c] = int(data[r][c])
    return n_rows, n_cols, grid, rv, cv, rs, cs


def within_radius(r, c, rv, cv, radius):
    return (r - rv) ** 2 + (c - cv) ** 2 <= radius ** 2


INPUT_FILE = "./data/q17_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

n_rows, n_cols, grid, rv, cv, _, _ = load_grid(data)

ans1 = 0
radius = 10
for r in range(n_rows):
    for c in range(n_cols):
        if within_radius(r, c, rv, cv, radius):
            ans1 += grid[r][c]

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q17_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

n_rows, n_cols, grid, rv, cv, _, _ = load_grid(data)

destruction = [0]
radius = 0
stop = False
while not stop:
    stop = True
    radius += 1
    res = 0
    for r in range(n_rows):
        for c in range(n_cols):
            if grid[r][c] > 0 and within_radius(r, c, rv, cv, radius):
                res += grid[r][c]
                grid[r][c] = 0
                stop = False
    destruction.append(res)
ans2 = max(destruction) * destruction.index(max(destruction))

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q17_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

n_rows, n_cols, grid, rv, cv, rs, cs = load_grid(data)


def calc_dist(radius_destroyed, left):
    dist = [[INF] * n_cols for _ in range(n_rows)]
    if within_radius(rs, cs, rv, cv, radius_destroyed):
        return dist
    dist[rs][cs] = 0
    pq = [(0, rs, cs)]
    while pq:
        d, r, c = heappop(pq)
        if d > dist[r][c]:
            continue
        for rn, cn in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if rn < 0 or n_rows <= rn or cn < 0 or n_cols <= cn:
                continue
            if rn == rv and ((left and cn >= cv) or (not left and cn <= cv)):
                continue
            if within_radius(rn, cn, rv, cv, radius_destroyed):
                continue
            dn = d + grid[rn][cn]
            if dn < dist[rn][cn]:
                dist[rn][cn] = dn
                heappush(pq, (dn, rn, cn))
    return dist


radius_destroyed = 0
while True:
    radius_destroyed += 1
    dist_left = calc_dist(radius_destroyed, True)
    dist_right = calc_dist(radius_destroyed, False)
    best = INF
    for r in range(rv + 1, n_rows):
        best = min(best, dist_left[r][cv] + dist_right[r][cv] - grid[r][cv])
    if best < (radius_destroyed + 1) * 30:
        ans3 = best * radius_destroyed
        break

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
