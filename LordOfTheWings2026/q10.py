from time import time
from collections import defaultdict

INF = 1 << 63
DIR = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}


def parse(data):
    walls, ghosts = set(), []
    for r, row in enumerate(data):
        for c, char in enumerate(row):
            if char == "#":
                walls.add((r, c))
            elif char in DIR:
                ghosts.append([r, c, DIR[char][0], DIR[char][1]])
    return walls, ghosts


def run_one_cycle(walls, ghosts, collisions, limit=INF):
    cnt_new_collisions = 0
    for i, (r, c, dr, dc) in enumerate(ghosts):
        if collisions[i] == limit:
            continue
        if (r + dr, c + dc) in walls:
            ghosts[i][2], ghosts[i][3] = ghosts[i][3], -ghosts[i][2]  # 90-degree rotation clockwise
            collisions[i] += 1
            cnt_new_collisions += 1
        else:
            ghosts[i][0] += dr
            ghosts[i][1] += dc
    same = defaultdict(list)
    for i, (r, c, _, _) in enumerate(ghosts):
        if collisions[i] < limit:
            same[r, c].append(i)
    for lst in same.values():
        if len(lst) > 1:
            for i in lst:
                ghosts[i][2], ghosts[i][3] = -ghosts[i][2], -ghosts[i][3]  # 180-degree rotation
                collisions[i] += 1
            cnt_new_collisions += len(lst)
    return cnt_new_collisions


def active_ghosts(collisions, limit=INF):
    return sum(1 for x in collisions if x < limit)


def calc_state(ghosts, collisions, limit=INF):
    return tuple(tuple(ghosts[i]) if collisions[i] < limit else (-1, -1, -1, -1) for i in range(len(ghosts)))


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q10_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

walls, ghosts = parse(data)
collisions = [0] * len(ghosts)

ans1 = 0
for _ in range(10):
    ans1 += run_one_cycle(walls, ghosts, collisions)

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q10_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

walls, ghosts = parse(data)
collisions = [0] * len(ghosts)
limit = 10_000
cycle = 0

while active_ghosts(collisions, limit):
    cycle += 1
    run_one_cycle(walls, ghosts, collisions, limit)
ans2 = cycle

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q10_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

walls, ghosts = parse(data)
collisions = [0] * len(ghosts)
limit = 1_000_000_000_000
cycle = 0
mem = {}

while active_ghosts(collisions, limit):
    cycle += 1
    run_one_cycle(walls, ghosts, collisions, limit)

    state = calc_state(ghosts, collisions, limit)
    if state not in mem:
        mem[state] = (cycle, tuple(collisions))
        continue

    cycle_prev, collisions_prev = mem[state]
    delta_collisions = [x - y for x, y, in zip(collisions, collisions_prev)]
    delta_cycle = cycle - cycle_prev

    factor = INF
    for i in range(len(ghosts)):
        if collisions[i] < limit and delta_collisions[i] > 0:
            factor = min(factor, (limit - collisions[i] - 1) // delta_collisions[i])
    for i in range(len(ghosts)):
        if collisions[i] < limit:
            collisions[i] += factor * delta_collisions[i]
    cycle += factor * delta_cycle

    state = calc_state(ghosts, collisions, limit)
    mem = {state: (cycle, tuple(collisions))}  # reset memory

ans3 = cycle
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
