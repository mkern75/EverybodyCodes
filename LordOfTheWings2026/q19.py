from time import time
from collections import Counter
from math import prod
from itertools import permutations


def parse(blocks):
    R, C = len(blocks[0]), len(blocks[0][0])
    if len(blocks) == 1:
        return R, C, blocks[0]
    else:
        return R, C, [blocks[0], blocks[1]]


def merge(col1: str, col2: str):
    if col1 > col2:
        col1, col2 = col2, col1
    if col1 == "K" or col2 == "K":
        return "K"
    elif col1 == "C" and col2 == "M":
        return "B"
    elif col1 == "C" and col2 == "Y":
        return "G"
    elif col1 == "M" and col2 == "Y":
        return "R"
    elif col1 == col2:
        return col1
    assert False


def solve1(R, C, grid):
    cnt = Counter()
    for r in range(R):
        for c in range(C):
            col1, col2 = sorted([grid[0][r][c], grid[1][r][c]])
            cnt[merge(col1, col2)] += 1
    return prod(sorted(cnt.values(), reverse=True)[:3])


def solve2(R, C, grid):
    res = 0
    for p in permutations(["K", "C", "M", "Y"]):
        cnt = Counter()
        for r in range(R):
            for c in range(C):
                i = int(grid[1][r][c]) - 1
                col1, col2 = sorted([grid[0][r][c], p[i]])
                cnt[merge(col1, col2)] += 1
        res = max(res, prod(sorted(cnt.values(), reverse=True)[:3]))
    return res


def solve3(R, C, grid):
    cnt = Counter()
    for r in range(R):
        for c in range(C):
            cnt[grid[r][c]] += 1
    a, b = cnt["K"], cnt["C"] + cnt["M"] + cnt["Y"]

    b1 = b // 2
    b2 = b - b1
    opt1 = a * b1 * b2

    b1 = b // 3
    b2 = (b - b1) // 2
    b3 = b - b1 - b2
    opt2 = b1 * b2 * b3

    return max(opt1, opt2)


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
