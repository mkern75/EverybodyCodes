from time import time
from collections import defaultdict

INF = 1 << 31

# ********************************* part 1
time_start = time()

INPUT_FILE = "./data/q20_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid = [list(line) for line in data]
n_rows, n_cols = len(grid), len(grid[0])


def neighbours(r, c):
    if (r + c) & 1 == 1:
        candidates = [(r, c - 1), (r, c + 1), (r + 1, c)]
    else:
        candidates = [(r, c - 1), (r, c + 1), (r - 1, c)]
    res = []
    for rn, cn in candidates:
        if 0 <= rn < n_rows and rn <= cn <= n_cols - 1 - rn:
            res.append((rn, cn))
    return res


def count_trampoline_pairs():
    res = 0
    for r in range(n_rows):
        for c in range(n_cols - 1):
            if grid[r][c] == "T":
                for rn, cn in neighbours(r, c):
                    if (r, c) < (rn, cn) and grid[rn][cn] == "T":
                        res += 1
    return res


ans1 = count_trampoline_pairs()
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 1
time_start = time()

INPUT_FILE = "./data/q20_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid = [list(line) for line in data]
n_rows, n_cols = len(grid), len(grid[0])
rs, cs = next((r, c) for r in range(n_rows) for c in range(n_cols) if grid[r][c] == "S")


def bfs(start):
    dist = defaultdict(lambda: INF, {start: 0})
    todo = [start]
    for r, c in todo:
        if grid[r][c] == "E":
            return dist[r, c]
        for rn, cn in neighbours(r, c):
            if grid[rn][cn] in "TSE" and dist[rn, cn] == INF:
                dist[rn, cn] = dist[r, c] + 1
                todo.append((rn, cn))
    return INF


ans2 = bfs((rs, cs))
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()

INPUT_FILE = "./data/q20_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid = [list(line) for line in data]
n_rows, n_cols = len(grid), len(grid[0])
rs, cs = next((r, c) for r in range(n_rows) for c in range(n_cols) if grid[r][c] == "S")


def rotate(grid):
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


grids = [grid, rotate(grid), rotate(rotate(grid))]


def neighbours3(r, c, s):
    if (r + c) & 1 == 1:
        candidates = [(r, c), (r, c - 1), (r, c + 1), (r + 1, c)]
    else:
        candidates = [(r, c), (r, c - 1), (r, c + 1), (r - 1, c)]
    res = []
    for rn, cn in candidates:
        if 0 <= rn < n_rows and rn <= cn <= n_cols - 1 - rn:
            res.append((rn, cn, (s + 1) % 3))
    return res


def bfs3(start):
    dist = defaultdict(lambda: INF, {start: 0})
    todo = [start]
    for r, c, s in todo:
        if grids[s][r][c] == "E":
            return dist[r, c, s]
        for rn, cn, sn in neighbours3(r, c, s):
            if grids[sn][rn][cn] in "TSE" and dist[rn, cn, sn] == INF:
                dist[rn, cn, sn] = dist[r, c, s] + 1
                todo.append((rn, cn, sn))
    return INF


ans3 = bfs3((rs, cs, 0))
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
