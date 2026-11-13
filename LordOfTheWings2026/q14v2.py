from time import time
from collections import Counter, defaultdict
from heapq import heappop, heappush

RIM = "rim"


def neighbours(r, c, R, C):
    for rn, cn in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
        if 0 <= rn < R and 0 <= cn < C:
            yield rn, cn


def build_adj(grid):
    adj = defaultdict(Counter)
    R, C = len(grid), len(grid[0])
    # inside
    for r in range(R):
        for c in range(C):
            for rn, cn in neighbours(r, c, R, C):
                if grid[r][c] != grid[rn][cn]:
                    adj[grid[r][c]][grid[rn][cn]] += 1
    # rim
    for r in range(R):
        adj[RIM][grid[r][0]] += 1
        adj[grid[r][0]][RIM] += 1
        adj[RIM][grid[r][C - 1]] += 1
        adj[grid[r][C - 1]][RIM] += 1
    for c in range(C):
        adj[RIM][grid[0][c]] += 1
        adj[grid[0][c]][RIM] += 1
        adj[RIM][grid[R - 1][c]] += 1
        adj[grid[R - 1][c]][RIM] += 1
    return adj


def prim(adj, portals=frozenset()):
    res = 0
    covered = {RIM}
    pq = []
    for v, w in adj[RIM].items():
        heappush(pq, (0 if v in portals else w, v))
    while len(covered) < len(adj):
        while pq[0][1] in covered:
            heappop(pq)
        w, u = heappop(pq)
        covered.add(u)
        res += w
        for v, w in adj[u].items():
            if v not in covered:
                heappush(pq, (0 if u in portals or v in portals else w, v))
    return res


def solve1(grid):
    adj = build_adj(grid)
    return sum(sum(cnt.values()) for cnt in adj.values()) // 2


def solve2(grid):
    adj = build_adj(grid)
    return prim(adj)


def solve3(grid):
    adj = build_adj(grid)
    portal = sorted({char for row in grid for char in row})
    res = 1 << 31
    for i in range(len(portal) - 1):
        for j in range(i + 1, len(portal)):
            res = min(res, prim(adj, frozenset({portal[i], portal[j]})))
    return res


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q14_p1.txt"
grid = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans1 = solve1(grid)

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q14_p2.txt"
grid = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans2 = solve2(grid)

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q14_p3.txt"
grid = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans3 = solve3(grid)

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
