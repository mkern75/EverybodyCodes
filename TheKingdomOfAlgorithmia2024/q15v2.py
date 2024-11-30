from time import time
from heapq import heappop, heappush

INF = 1 << 63


def ff(dist, idx, f):
    return (dist << 48) | (idx << 32) | f


def fr(x):
    return x >> 48, (x >> 32) & 0xFFFF, x & 0xFFFFFFFF


def bfs_dist(grid, rs, cs):
    n, m = len(grid), max(len(row) for row in grid)
    dist = [[INF] * m for _ in range(n)]
    dist[rs][cs] = 0
    q = [(rs, cs)]
    for r, c in q:
        for rn, cn in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if 0 <= rn < n and 0 <= cn < m and grid[rn][cn] != "#":
                if dist[r][c] + 1 < dist[rn][cn]:
                    dist[rn][cn] = dist[r][c] + 1
                    q += [(rn, cn)]
    return dist


def dijkstra(grid, rs, cs, herbs):
    herb_ids = sorted({grid[r][c] for r, c in herbs})
    f_target = (1 << len(herb_ids)) - 1

    poi = [(rs, cs, 0)] + [(r, c, 1 << herb_ids.index(grid[r][c])) for r, c in herbs]
    k = len(poi)

    poi_dist = [bfs_dist(grid, r, c) for r, c, _ in poi]
    dist = [[INF] * (1 << len(herb_ids)) for _ in range(k)]
    dist[0][0] = 0

    q = [ff(0, 0, 0)]
    cnt = 0
    while q:
        cnt += 1
        d, i, f = fr(heappop(q))
        if i == 0 and f == f_target:
            return d
        if d > dist[i][f]:
            continue
        for j in range(k):
            fn = f | poi[j][2]
            if f == fn and (f != f_target or j != 0):
                continue
            dn = d + poi_dist[i][poi[j][0]][poi[j][1]]
            if dn < dist[j][fn]:
                dist[j][fn] = dn
                heappush(q, ff(dn, j, fn))


# ********************************* part 1
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q15_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid = data
n, m = len(grid), max(len(row) for row in grid)
rs, cs = 0, next(c for c in range(m) if grid[0][c] == ".")
herbs = [(r, c) for r in range(n) for c in range(m) if grid[r][c].isalpha()]

ans1 = dijkstra(grid, rs, cs, herbs)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q15_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid = data
n, m = len(grid), max(len(row) for row in grid)
rs, cs = 0, next(c for c in range(m) if grid[0][c] == ".")
herbs = [(r, c) for r in range(n) for c in range(m) if grid[r][c].isalpha()]

ans2 = dijkstra(grid, rs, cs, herbs)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q15_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid = data
n, m = len(grid), max(len(row) for row in grid)
rs, cs = 0, next(c for c in range(m) if grid[0][c] == ".")
herbs = [(r, c) for r in range(n) for c in range(m) if grid[r][c].isalpha()]

ans3 = dijkstra(grid, rs, cs, herbs)
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
