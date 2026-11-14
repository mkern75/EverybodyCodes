from time import time
from collections import defaultdict

INF = 1 << 63
UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3


def parse(grid):
    R, C = len(grid), len(grid[0])
    rs, cs = -1, -1
    re, ce = -1, -1
    sulphur = {}
    for r in range(R):
        for c in range(C):
            if grid[r][c] == "S":
                rs, cs = r, c
            if grid[r][c] == "E":
                re, ce = r, c
            if grid[r][c] == "@":
                sulphur[r, c] = len(sulphur)
    return R, C, rs, cs, re, ce, sulphur


def moves(r, c, d):
    if d == UP:
        return [(r - 1, c, UP), (r, c - 1, LEFT), (r, c + 1, RIGHT)]
    elif d == DOWN:
        return [(r + 1, c, DOWN), (r, c - 1, LEFT), (r, c + 1, RIGHT)]
    elif d == LEFT:
        return [(r, c - 1, LEFT), (r + 1, c, DOWN), (r - 1, c, UP)]
    elif d == RIGHT:
        return [(r, c + 1, RIGHT), (r + 1, c, DOWN), (r - 1, c, UP)]
    else:
        assert False


def solve1(grid):
    R, C, rs, cs, re, ce, sulphur = parse(grid)
    todo = [(rs, cs, RIGHT, 0, 0)]
    seen = {(rs, cs, RIGHT, 0)}
    for r, c, d, msk, t in todo:
        if r == re and c == ce and msk.bit_count() == len(sulphur):
            return t
        for rn, cn, dn in moves(r, c, d):
            if 0 <= rn < R and 0 <= cn < C and grid[rn][cn] != "#":
                mskn = msk | (1 << sulphur[rn, cn]) if grid[rn][cn] == "@" else msk
                if (rn, cn, dn, mskn) not in seen:
                    seen.add((rn, cn, dn, mskn))
                    todo.append((rn, cn, dn, mskn, t + 1))
    return -1


def solve2(grid):
    R, C, rs, cs, re, ce, sulphur = parse(grid)
    todo = [(rs, cs, RIGHT, 0, 0)]
    seen = {(rs, cs, RIGHT, 0)}
    for r, c, d, cnt, t in todo:
        if r == re and c == ce and cnt >= 2026:
            return t
        for rn, cn, dn in moves(r, c, d):
            if 0 <= rn < R and 0 <= cn < C and grid[rn][cn] != "#":
                cntn = cnt + 1 if grid[rn][cn] == "@" else cnt
                if (rn, cn, dn, cntn) not in seen:
                    seen.add((rn, cn, dn, cntn))
                    todo.append((rn, cn, dn, cntn, t + 1))
    return -1


def find_best_cycles(grid):
    R, C, rs, cs, re, ce, sulphur = parse(grid)
    best = defaultdict(lambda: INF)
    rr = rs
    for cc in range(cs + 1, ce):
        todo = [(rr, cc, RIGHT, 0, 0)]
        seen = {(rr, cc, RIGHT)}
        for r, c, d, cnt, t in todo:
            if r == rs and c == cc and cnt > 0:
                if cnt < best[cnt]:
                    best[cnt] = t
                continue
            for rn, cn, dn in moves(r, c, d):
                if 0 <= rn < R and 0 <= cn < C and grid[rn][cn] != "#":
                    cntn = cnt + 1 if grid[rn][cn] == "@" else cnt
                    if (rn, cn, dn) not in seen:
                        seen.add((rn, cn, dn))
                        todo.append((rn, cn, dn, cntn, t + 1))
    return min([(k, v) for k, v in best.items()], key=lambda x: x[1] / x[0])


def solve3(grid):
    target = 202620262026
    sulphur_cycle, time_cycle = find_best_cycles(grid)
    f = max(0,target // sulphur_cycle - 3)
    res = f * time_cycle
    target -= f * sulphur_cycle

    R, C, rs, cs, re, ce, sulphur = parse(grid)
    todo = [(rs, cs, RIGHT, 0, 0)]
    seen = {(rs, cs, RIGHT, 0)}
    for r, c, d, cnt, t in todo:
        if r == re and c == ce and cnt == target:
            return res + t
        for rn, cn, dn in moves(r, c, d):
            if 0 <= rn < R and 0 <= cn < C and grid[rn][cn] != "#":
                cntn = cnt + 1 if grid[rn][cn] == "@" else cnt
                if (rn, cn, dn, cntn) not in seen:
                    seen.add((rn, cn, dn, cntn))
                    todo.append((rn, cn, dn, cntn, t + 1))
    return -1


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q15_p1.txt"
grid = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans1 = solve1(grid)

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q15_p2.txt"
grid = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans2 = solve2(grid)

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q15_p3.txt"
# INPUT_FILE = "./data/q15_p3_test.txt"
grid = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans3 = solve3(grid)

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
