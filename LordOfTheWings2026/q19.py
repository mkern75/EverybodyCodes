from time import time
from collections import Counter
from math import prod
from itertools import permutations

MIX = {"KK": "K", "KC": "K", "CK": "K", "KM": "K", "MK": "K", "KY": "K", "YK": "K",
       "CM": "B", "MC": "B", "CY": "G", "YC": "G", "MY": "R", "YM": "R",
       "CC": "C", "MM": "M", "YY": "Y"}


def parse(blocks):
    R, C = len(blocks[0]), len(blocks[0][0])
    if len(blocks) == 1:
        return R, C, blocks[0]
    else:
        return R, C, [blocks[0], blocks[1]]


def solve1(R, C, grid):
    cnt = Counter()
    for r in range(R):
        for c in range(C):
            cnt[MIX[grid[0][r][c] + grid[1][r][c]]] += 1
    return prod(sorted(cnt.values())[-3:])


def solve2(R, C, grid):
    res = 0
    for perm in permutations(["K", "C", "M", "Y"]):
        cnt = Counter()
        for r in range(R):
            for c in range(C):
                cnt[MIX[grid[0][r][c] + perm[int(grid[1][r][c]) - 1]]] += 1
        res = max(res, prod(sorted(cnt.values())[-3:]))
    return res


def solve3(R, C, grid):
    cnt = Counter()
    for r in range(R):
        for c in range(C):
            cnt[grid[r][c]] += 1
    x, y = cnt["K"], cnt["C"] + cnt["M"] + cnt["Y"]
    a1 = y // 2
    a2 = y - a1
    b1 = y // 3
    b2 = (y - b1) // 2
    b3 = y - b1 - b2
    return max(x * a1 * a2, b1 * b2 * b3)


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q19_p1.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

ans1 = solve1(*parse(blocks))

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q19_p2.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

ans2 = solve2(*parse(blocks))

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q19_p3.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

ans3 = solve3(*parse(blocks))

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
