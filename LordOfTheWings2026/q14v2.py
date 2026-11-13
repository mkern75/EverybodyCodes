from time import time
from collections import Counter, defaultdict
from heapq import heappop, heappush

RIM = "rim"


def parse(data):
    grid = defaultdict(lambda: RIM)
    for r, row in enumerate(data):
        for c, char in enumerate(row):
            grid[r, c] = char
    return grid, len(data), len(data[0])


def adjacency(grid, R, C):
    adj = defaultdict(Counter)
    for r in range(R):
        for c in range(C):
            for rn, cn in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if grid[r, c] != grid[rn, cn]:
                    adj[grid[r, c]][grid[rn, cn]] += 1
                    if grid[rn, cn] == RIM:
                        adj[RIM][grid[r, c]] += 1
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


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q14_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid, R, C = parse(data)
adj = adjacency(grid, R, C)
ans1 = sum(sum(cnt.values()) for cnt in adj.values()) // 2

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q14_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid, R, C = parse(data)
adj = adjacency(grid, R, C)
ans2 = prim(adj)

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q14_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid, R, C = parse(data)
adj = adjacency(grid, R, C)
portal = sorted({grid[r, c] for r in range(R) for c in range(C)})
ans3 = 1 << 31
for i in range(len(portal) - 1):
    for j in range(i + 1, len(portal)):
        ans3 = min(ans3, prim(adj, frozenset({portal[i], portal[j]})))

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
