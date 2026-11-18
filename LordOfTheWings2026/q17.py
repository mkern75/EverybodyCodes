from time import time
from collections import defaultdict

TOP, RIGHT, BOTTOM, LEFT = 0, 1, 2, 3


def parse(data):
    R, C = len(data), len(data[0])
    grid = defaultdict(lambda: ".")
    for r in range(R):
        for c in range(C):
            if data[r][c] == "#":
                grid[r, c] = "#"
    return R, C, grid


def neighbours(r, c):
    for rn, cn in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
        yield rn, cn


def neighbours2(r, c, d):
    if d == TOP:
        res = [(r, c - 1, TOP), (r, c + 1, TOP), (r, c, LEFT), (r, c, RIGHT), (r - 1, c - 1, RIGHT),
               (r - 1, c + 1, LEFT)]
    elif d == BOTTOM:
        res = [(r, c - 1, BOTTOM), (r, c + 1, BOTTOM), (r, c, LEFT), (r, c, RIGHT), (r + 1, c - 1, RIGHT),
               (r + 1, c + 1, LEFT)]
    elif d == RIGHT:
        res = [(r - 1, c, RIGHT), (r + 1, c, RIGHT), (r, c, TOP), (r, c, BOTTOM), (r - 1, c + 1, BOTTOM),
               (r + 1, c + 1, TOP)]
    elif d == LEFT:
        res = [(r - 1, c, LEFT), (r + 1, c, LEFT), (r, c, TOP), (r, c, BOTTOM), (r - 1, c - 1, BOTTOM),
               (r + 1, c - 1, TOP)]
    else:
        assert False
    for rn, cn, dn in res:
        yield rn, cn, dn


def solve1(R, C, grid):
    steps = 0
    curr = [(0, 0)]
    seen = {(0, 0)}
    while True:
        nxt = []
        for r, c in curr:
            if (r, c) == (R - 1, C - 1):
                return steps
            for rn, cn in neighbours(r, c):
                if grid[rn, cn] == "#" and (rn, cn) not in seen:
                    nxt.append((rn, cn))
                    seen.add((rn, cn))
        steps += 1
        curr = nxt


def solve2(R, C, grid):
    res = 0
    for r in range(R):
        for c in range(C):
            if grid[r, c] == "#":
                for rn, cn in neighbours(r, c):
                    if grid[rn, cn] == ".":
                        res += 1
    return res


def solve3(R, C, grid):
    edges = set()
    for r in range(R):
        for c in range(C):
            if grid[r, c] == "#":
                for rn, cn, d in [(r - 1, c, TOP), (r + 1, c, BOTTOM), (r, c - 1, LEFT), (r, c + 1, RIGHT)]:
                    if grid[rn, cn] == ".":
                        edges.add((r, c, d))
    n_edges = len(edges)

    # check path going down from start / arriving from left at the finish
    path = []
    todo = {(0, 0, LEFT), (R - 1, C - 1, BOTTOM)}

    # remove edges for start / finish
    edges.remove((0, 0, LEFT))
    edges.remove((0, 0, TOP))
    edges.remove((R - 1, C - 1, BOTTOM))
    edges.remove((R - 1, C - 1, RIGHT))

    while todo:
        todo_next = set()
        for r, c, d in todo:
            path.append((r, c, d))
            for rn, cn, dn in neighbours2(r, c, d):
                if (rn, cn, dn) in edges:
                    todo_next.add((rn, cn, dn))
                    edges.remove((rn, cn, dn))
        todo = todo_next

    return min(len(path), n_edges - len(path))


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q17_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans1 = solve1(*parse(data))

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q17_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans2 = solve2(*parse(data))

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q17_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans3 = solve3(*parse(data))

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
