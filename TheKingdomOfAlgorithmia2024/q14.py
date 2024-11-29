from time import time

DIR = {"R": (1, 0, 0), "L": (-1, 0, 0), "U": (0, 1, 0), "D": (0, -1, 0), "F": (0, 0, 1), "B": (0, 0, -1)}


def grow_branch(steps):
    branch = set()
    x, y, z = 0, 0, 0
    for step in steps:
        d, v = step[0], int(step[1:])
        dx, dy, dz = DIR[d]
        for i in range(v):
            x, y, z = x + dx, y + dy, z + dz
            branch.add((x, y, z))
    return branch, (x, y, z)


def bfs_dist(plant, start):
    xs, ys, zs = start
    dist = {(xs, ys, zs): 0}
    q = [(xs, ys, zs)]
    for x, y, z in q:
        for dx, dy, dz in DIR.values():
            xn, yn, zn = x + dx, y + dy, z + dz
            if (xn, yn, zn) in plant and (xn, yn, zn) not in dist:
                dist[xn, yn, zn] = dist[x, y, z] + 1
                q += [(xn, yn, zn)]
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

dist = [bfs_dist(plant, leaf) for leaf in leaves]  # there are fewer leaves that segments in the trunk
ans3 = min(sum(dist[i][t] for i in range(len(leaves))) for t in trunk)

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
