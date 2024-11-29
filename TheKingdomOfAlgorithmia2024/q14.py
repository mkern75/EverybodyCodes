from time import time
from collections import defaultdict
from heapq import heappop, heappush

INF = 1 << 31


def grow_branch(steps):
    branch = set()
    x, y, z = 0, 0, 0
    for step in steps:
        d, v = step[0], int(step[1:])
        dx, dy, dz = 0, 0, 0
        if d == "U":
            dy = 1
        elif d == "D":
            dy = -1
        elif d == "R":
            dx = 1
        elif d == "L":
            dx = -1
        elif d == "F":
            dz = 1
        elif d == "B":
            dz = -1
        for i in range(v):
            x += dx
            y += dy
            z += dz
            branch.add((x, y, z))
    return branch, (x, y, z)


def dijsktra(plant, start):
    xs, ys, zs = start
    dist = defaultdict(lambda: INF)
    dist[xs, ys, zs] = 0
    q = [(0, xs, ys, zs)]
    while q:
        d, x, y, z = heappop(q)
        if d > dist[x, y, z]:
            continue
        for xn, yn, zn, in [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)]:
            if (xn, yn, zn) in plant:
                dn = d + 1
                if dn < dist[xn, yn, zn]:
                    dist[xn, yn, zn] = dn
                    heappush(q, (dn, xn, yn, zn))
    return dist


# ********************************* part 1
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q14_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

steps = data[0].split(",")
plant, _ = grow_branch(steps)
ans1 = max(y for _, y, _ in plant)

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q14_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

steps_all = [row.split(",") for row in data]
plant = set()
for steps in steps_all:
    branch, _ = grow_branch(steps)
    plant.update(branch)
ans2 = len(plant)

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q14_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

steps_all = [row.split(",") for row in data]

plant, leaves = set(), set()
for steps in steps_all:
    branch, leaf = grow_branch(steps)
    plant.update(branch)
    leaves.add(leaf)
trunk = [(x, y, z) for x, y, z in plant if x == z == 0]

ans3 = INF
for start in trunk:
    dist = dijsktra(plant, start)
    ans3 = min(ans3, sum(dist[leaf] for leaf in leaves))

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
