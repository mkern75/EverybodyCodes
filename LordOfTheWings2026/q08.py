from time import time
from collections import defaultdict

DIRECTIONS = [(1, 1), (1, -1), (0, -2), (-1, -1), (-1, 1), (0, 2)]


def parse(data):
    R, C = len(data), len(data[0])
    grid = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if data[r][c] != ".":
                grid[r][c] = int(data[r][c])
    return grid


def simulate(grid, direction=0):
    res = []
    dr, dc = DIRECTIONS[direction]
    R, C = len(grid), len(grid[0])
    shadow = [[0] * C for _ in range(R)]

    if dr == 1 and dc == 1:
        seq = [(r, c) for r in range(R) for c in range(C)]
    elif dr == 1 and dc == -1:
        seq = [(r, c) for r in range(R) for c in range(C - 1, -1, -1)]
    elif dr == 0 and dc == -2:
        seq = [(r, c) for r in range(R) for c in range(C - 1, -1, -1)]
    elif dr == -1 and dc == -1:
        seq = [(r, c) for r in range(R - 1, -1, -1) for c in range(C - 1, -1, -1)]
    elif dr == -1 and dc == 1:
        seq = [(r, c) for r in range(R - 1, -1, -1) for c in range(C)]
    elif dr == 0 and dc == 2:
        seq = [(r, c) for r in range(R) for c in range(C)]
    else:
        assert False

    for r, c in seq:
        if 0 <= r - dr < R and 0 <= c - dc < C:
            shadow[r][c] = max(shadow[r - dr][c - dc] - 1, 0)
        if grid[r][c] > shadow[r][c]:
            res += [(r, c)]
            shadow[r][c] = grid[r][c]

    return res


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q08_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid = parse(data)
ans1 = len(simulate(grid))
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q08_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid = parse(data)
ans2 = sum(len(simulate(grid, d)) for d in range(len(DIRECTIONS)))
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q08_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid = parse(data)

ans3 = 0
cycle = 0
warriors = 0
seeds = defaultdict(list)

while warriors < 100000:

    # grow seeds
    for r, c in seeds[cycle]:
        grid[r][c] = 1

    # simulate round
    res = simulate(grid, cycle % 6)
    ans3 += len(res)

    # determine warriors and growth
    for r, c in res:
        if grid[r][c] == 9:
            warriors += 1
            seeds[cycle + 4].append((r, c))
            grid[r][c] = 0
        else:
            grid[r][c] += 1

    cycle += 1

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
