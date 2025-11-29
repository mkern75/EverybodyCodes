from time import time
from collections import defaultdict

INF = 1 << 31

# ********************************* part 1
time_start = time()


def neighbours(r, c, n_rows, n_cols):
    if (r + c) & 1 == 1:
        candidates = [(r, c - 1), (r, c + 1), (r + 1, c)]
    else:
        candidates = [(r, c - 1), (r, c + 1), (r - 1, c)]
    res = []
    for rn, cn in candidates:
        if 0 <= rn < n_rows and rn <= cn <= n_cols - 1 - rn:
            res.append((rn, cn))
    return res


INPUT_FILE = "./data/q20_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid = [list(line) for line in data]
n_rows, n_cols = len(grid), len(grid[0])

ans1 = 0
for r in range(n_rows):
    for c in range(n_cols - 1):
        if grid[r][c] == "T":
            for rn, cn in neighbours(r, c, n_rows, n_cols):
                if grid[rn][cn] == "T":
                    ans1 += 1
ans1 //= 2

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 1
time_start = time()


def find_start(grid):
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char == "S":
                return r, c
    assert False


INPUT_FILE = "./data/q20_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid = [list(line) for line in data]
n_rows, n_cols = len(grid), len(grid[0])
rs, cs = find_start(grid)

ans2 = INF
dist = defaultdict(lambda: INF)
dist[rs, cs] = 0
bfs = [(rs, cs)]
for r, c in bfs:
    if grid[r][c] == "E":
        ans2 = dist[r, c]
        break
    for rn, cn in neighbours(r, c, n_rows, n_cols):
        if grid[rn][cn] in "TSE" and dist[rn, cn] == INF:
            dist[rn, cn] = dist[r, c] + 1
            bfs.append((rn, cn))

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()


def rotate(grid):
    n_rows, n_cols = len(grid), len(grid[0])
    grid_new = [["." for _ in range(n_cols)] for _ in range(n_rows)]
    for c in range(0, n_cols, 2):
        rn = c // 2
        cn = n_cols - 1 - c // 2
        for r in range(n_rows):
            if r + c < n_cols and grid[r][r + c] != ".":
                grid_new[rn][cn] = grid[r][r + c]
                cn -= 1
            if r + c + 1 < n_cols and grid[r][r + c + 1] != ".":
                grid_new[rn][cn] = grid[r][r + c + 1]
                cn -= 1
    return grid_new


def neighbours_part3(r, c, s, n_rows, n_cols):
    if (r + c) & 1 == 1:
        candidates = [(r, c), (r, c - 1), (r, c + 1), (r + 1, c)]
    else:
        candidates = [(r, c), (r, c - 1), (r, c + 1), (r - 1, c)]
    res = []
    for rn, cn in candidates:
        if 0 <= rn < n_rows and rn <= cn <= n_cols - 1 - rn:
            res.append((rn, cn, (s + 1) % 3))
    return res


INPUT_FILE = "./data/q20_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid = [list(line) for line in data]
n_rows, n_cols = len(grid), len(grid[0])
rs, cs = find_start(grid)
grids = [grid, rotate(grid), rotate(rotate(grid))]

ans3 = INF
dist = defaultdict(lambda: INF)
dist[rs, cs, 0] = 0
bfs = [(rs, cs, 0)]
for r, c, s in bfs:
    if grids[s][r][c] == "E":
        ans3 = dist[r, c, s]
        break
    for rn, cn, sn in neighbours_part3(r, c, s, n_rows, n_cols):
        if grids[sn][rn][cn] in "TSE" and dist[rn, cn, sn] == INF:
            dist[rn, cn, sn] = dist[r, c, s] + 1
            bfs.append((rn, cn, sn))

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
