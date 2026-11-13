from time import time
from collections import Counter, defaultdict
from heapq import heappop, heappush

INF = RIM = 1 << 31


class DSU:
    def __init__(self, n: int):
        self._parent = list(range(n))

    def find(self, x: int) -> int:
        parent = self._parent
        y = x
        while x != parent[x]:
            x = parent[x]
        while y != x:
            parent[y], y = x, parent[y]
        return x

    def unite(self, x: int, y: int) -> bool:
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        self._parent[y] = x
        return True


def idx(r, c, C):
    return r * C + c


def neighbours(r, c, R, C):
    for rn, cn in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
        if 0 <= rn < R and 0 <= cn < C:
            yield rn, cn


def build_dsu(grid, R, C):
    dsu = DSU(R * C)
    for r in range(R):
        for c in range(C):
            for rn, cn in neighbours(r, c, R, C):
                if grid[r][c] == grid[rn][cn]:
                    dsu.unite(idx(r, c, C), idx(rn, cn, C))
    return dsu


def solve1(grid):
    R, C = len(grid), len(grid[0])
    dsu = build_dsu(grid, R, C)

    res = 2 * (R + C)  # rim
    for r in range(R):
        for c in range(C):
            for rn, cn in neighbours(r, c, R, C):
                if dsu.find(idx(r, c, C)) < dsu.find(idx(rn, cn, C)):
                    res += 1
    return res


def build_adj(dsu, R, C):
    adj = defaultdict(Counter)
    # inside
    for r in range(R):
        for c in range(C):
            x = dsu.find(idx(r, c, C))
            for rn, cn in neighbours(r, c, R, C):
                y = dsu.find(idx(rn, cn, C))
                if x != y:
                    adj[x][y] += 1
    # rim
    for r in range(R):
        adj[RIM][dsu.find(idx(r, 0, C))] += 1
        adj[dsu.find(idx(r, 0, C))][RIM] += 1
        adj[RIM][dsu.find(idx(r, C - 1, C))] += 1
        adj[dsu.find(idx(r, C - 1, C))][RIM] += 1
    for c in range(C):
        adj[RIM][dsu.find(idx(0, c, C))] += 1
        adj[dsu.find(idx(0, c, C))][RIM] += 1
        adj[RIM][dsu.find(idx(R - 1, c, C))] += 1
        adj[dsu.find(idx(R - 1, c, C))][RIM] += 1
    return adj


def prim(adj, portals):
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


def solve2(grid):
    R, C = len(grid), len(grid[0])
    dsu = build_dsu(grid, R, C)
    adj = build_adj(dsu, R, C)
    return prim(adj, set())


def solve3(grid):
    R, C = len(grid), len(grid[0])
    dsu = build_dsu(grid, R, C)
    adj = build_adj(dsu, R, C)

    res = INF
    portal = sorted({dsu.find(idx(r, c, C)) for r in range(R) for c in range(C)})
    for i in range(len(portal) - 1):
        for j in range(i + 1, len(portal)):
            res = min(res, prim(adj, {portal[i], portal[j]}))
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
