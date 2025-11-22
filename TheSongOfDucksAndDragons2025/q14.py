from time import time
from copy import deepcopy

# ********************************* part 1
time_start = time()


def load_grid(data):
    grid = []
    for line in data:
        grid.append([0 if c == "." else 1 for c in line])
    return grid


def simulate_one_round(grid):
    n, m = len(grid), len(grid[0])
    grid_new = [[0] * m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            cnt = 0
            for rr, cc in [(r - 1, c - 1), (r - 1, c + 1), (r + 1, c - 1), (r + 1, c + 1)]:
                if 0 <= rr < n and 0 <= cc < m:
                    cnt += grid[rr][cc]
            if grid[r][c] == cnt & 1:
                grid_new[r][c] = 1
    return grid_new


def count_tiles(grid):
    return sum(sum(row) for row in grid)


INPUT_FILE = "./data/q14_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid = load_grid(data)
ans1 = 0
for _ in range(10):
    grid = simulate_one_round(grid)
    ans1 += count_tiles(grid)

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()

INPUT_FILE = "./data/q14_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid = load_grid(data)
ans2 = 0
for _ in range(2025):
    grid = simulate_one_round(grid)
    ans2 += count_tiles(grid)

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()


def check_pattern(grid, pattern):
    ng, mg = len(grid), len(grid[0])
    np, mp = len(pattern), len(pattern[0])
    sn = (ng - np) // 2
    sm = (mg - mp) // 2
    for r in range(np):
        for c in range(mp):
            if grid[sn + r][sm + c] != pattern[r][c]:
                return False
    return True


INPUT_FILE = "./data/q14_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid = [[0] * 34 for _ in range(34)]
pattern = load_grid(data)
iteration = 0
cycle = -1
grids, iterations, tiles = [], [], []

while True:
    iteration += 1
    grid = simulate_one_round(grid)
    if check_pattern(grid, pattern):
        if grid in grids:
            cycle = iteration - iterations[0]
            break
        grids.append(deepcopy(grid))
        iterations.append(iteration)
        tiles.append(count_tiles(grid))

ans3 = 0
for iteration, cnt in zip(iterations, tiles):
    ans3 += (1 + (1000000000 - iteration) // cycle) * cnt

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
