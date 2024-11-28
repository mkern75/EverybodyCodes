from time import time

INF = 1 << 31


def bfs(grid, starts):
    n, m = len(grid), max(len(row) for row in grid)
    dist = [[INF] * m for _ in range(n)]
    q = []
    for r, c in starts:
        dist[r][c] = 0
        q += [(r, c)]
    for r, c in q:
        for rn, cn in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if 0 <= rn < n and 0 <= cn < m and grid[rn][cn] in ".P":
                if dist[r][c] + 1 < dist[rn][cn]:
                    dist[rn][cn] = dist[r][c] + 1
                    q += [(rn, cn)]
    return dist


# ********************************* part 1
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q18_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid = data
n, m = len(grid), max(len(row) for row in grid)
rs, cs = next(r for r in range(n) if grid[r][0] == "."), 0
trees = [(r, c) for r in range(n) for c in range(m) if grid[r][c] == "P"]

dist = bfs(grid, [(rs, cs)])
ans1 = max(dist[r][c] for r, c in trees)

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q18_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid = data
n, m = len(grid), max(len(row) for row in grid)
rs1, cs1 = next(r for r in range(n) if grid[r][0] == "."), 0
rs2, cs2 = next(r for r in range(n) if grid[r][m - 1] == "."), m - 1
trees = [(r, c) for r in range(n) for c in range(m) if grid[r][c] == "P"]

dist = bfs(grid, [(rs1, cs1), (rs2, cs2)])
ans2 = max(dist[r][c] for r, c in trees)

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q18_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid = data
n, m = len(grid), max(len(row) for row in grid)
trees = [(r, c) for r in range(n) for c in range(m) if grid[r][c] == "P"]

dist = [bfs(grid, [(r, c)]) for r, c in trees]
ans3 = INF
for r in range(n):
    for c in range(m):
        if grid[r][c] == ".":
            ans3 = min(ans3, sum(d[r][c] for d in dist))

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
