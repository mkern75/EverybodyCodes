from collections import defaultdict
from heapq import heappop, heappush

# ********************************* part 1
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q14_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans1 = 0
steps = data[0].split(",")
h = 0

for step in steps:
    d, v = step[0], int(step[1:])
    if d == "U":
        h += v
    elif d == "D":
        h -= v
    ans1 = max(ans1, h)

print(f"part 1: {ans1}")

# ********************************* part 2
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q14_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

steps_all = [row.split(",") for row in data]

plant = set()
for steps in steps_all:
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
            plant.add((x, y, z))

ans2 = len(plant)
print(f"part 2: {ans2}")

# ********************************* part 3
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q14_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

steps_all = [row.split(",") for row in data]

plant, leaves = set(), set()
for steps in steps_all:
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
            plant.add((x, y, z))
    leaves.add((x, y, z))

trunk = [(x, y, z) for x, y, z in plant if x == z == 0]


def dijsktra(plant, start):
    xs, ys, zs = start
    dist = defaultdict(lambda: 1 << 31)
    dist[xs, ys, zs] = 0
    q = [(dist[xs, ys, zs], xs, ys, zs)]
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


ans3 = 1 << 31
for start in trunk:
    dist = dijsktra(plant, start)
    ans3 = min(ans3, sum(dist[leave] for leave in leaves))
print(f"part 3: {ans3}")

