from time import time

MOVE = ((-1, 0,), (0, 1), (1, 0), (0, -1))
MOVE_EXT = ((-1, 0,), (-1, 0,), (-1, 0,), (0, 1), (0, 1), (0, 1),
            (1, 0), (1, 0), (1, 0), (0, -1), (0, -1), (0, -1))


def load(data):
    r_curr, c_curr = 0, 0
    targets = []
    for r, line in enumerate(data):
        for c, x in enumerate(line):
            if x == "@":
                r_curr, c_curr = r, c
            elif x == "#":
                targets.append((r, c))
    return r_curr, c_curr, targets


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q02_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

r_curr, c_curr, targets = load(data)
r_target, c_target = targets[0]
seen = {(r_curr, c_curr)}
k = 0

ans1 = 0
while (r_curr, c_curr) != (r_target, c_target):
    ans1 += 1
    while (r_curr + MOVE[k][0], c_curr + MOVE[k][1]) in seen:
        k = (k + 1) % len(MOVE)
    r_curr += MOVE[k][0]
    c_curr += MOVE[k][1]
    seen.add((r_curr, c_curr))
    k = (k + 1) % len(MOVE)

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q02_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

r_curr, c_curr, targets = load(data)
seen = {(r_curr, c_curr)}
seen.update(targets)
todo = set()
for r, c in targets:
    for dr, dc in MOVE:
        todo.add((r + dr, c + dc))
todo.difference_update(seen)
k = 0


def flood():
    r_min = min(r for r, _ in seen) - 1
    r_max = max(r for r, _ in seen) + 1
    c_min = min(c for _, c in seen) - 1
    c_max = max(c for _, c in seen) + 1
    q = [(r_min, c_min)]
    s = {(r_min, c_min)}
    while q:
        r, c = q.pop()
        for dr, dc in MOVE:
            rn = r + dr
            cn = c + dc
            if r_min <= rn <= r_max and c_min <= cn <= c_max and (rn, cn) not in s and (rn, cn) not in seen:
                s.add((rn, cn))
                q.append((rn, cn))
    for r in range(r_min, r_max + 1):
        for c in range(c_min, c_max + 1):
            if (r, c) not in s and (r, c) not in seen:
                seen.add((r, c))
                todo.discard((r, c))


ans2 = 0
while todo:
    ans2 += 1
    while (r_curr + MOVE[k][0], c_curr + MOVE[k][1]) in seen:
        k = (k + 1) % len(MOVE)
    r_curr += MOVE[k][0]
    c_curr += MOVE[k][1]
    seen.add((r_curr, c_curr))
    todo.discard((r_curr, c_curr))
    k = (k + 1) % len(MOVE)
    flood()

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q02_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

r_curr, c_curr, targets = load(data)
seen = {(r_curr, c_curr)}
seen.update(targets)
todo = set()
for r, c in targets:
    for dr, dc in MOVE:
        todo.add((r + dr, c + dc))
todo.difference_update(seen)
k = 0

ans3 = 0
while todo:
    ans3 += 1
    while (r_curr + MOVE_EXT[k][0], c_curr + MOVE_EXT[k][1]) in seen:
        k = (k + 1) % len(MOVE_EXT)
    r_curr += MOVE_EXT[k][0]
    c_curr += MOVE_EXT[k][1]
    seen.add((r_curr, c_curr))
    todo.discard((r_curr, c_curr))
    k = (k + 1) % len(MOVE_EXT)
    flood()

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
