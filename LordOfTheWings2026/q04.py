from time import time
import re
from collections import defaultdict


def nums(s: str) -> list[int]:
    return list(map(int, re.findall(r"-?\d+", s)))


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q04_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

times = defaultdict(int)
for line in data:
    id, _, _, t = nums(line)
    times[id] += t
ranking = sorted(times.keys(), key=lambda id: times[id])

ans1 = 0
for i, id in enumerate(ranking, start=1):
    ans1 += i * times[id]
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q04_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

parts = defaultdict(int)
times = defaultdict(int)
for line in data:
    id, _, _, t = nums(line)
    parts[id] += 1
    times[id] += t
ranking = sorted(parts.keys(), key=lambda id: (-parts[id], times[id]))

ans2 = 0
for i, id in enumerate(ranking, start=1):
    ans2 += i * times[id]
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q04_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ids = set()
quests = set()
times = defaultdict(int)
for line in data:
    id, q, p, t = nums(line)
    ids.add(id)
    quests.add(q)
    times[id, q, p] = t

# cumulative times for parts 2 and 3
for q in quests:
    for id in ids:
        for p in [2, 3]:
            if (id, q, p) in times:
                times[id, q, p] += times[id, q, p - 1]


def rank(a):
    res = []
    for i in range(len(a)):
        res.append(res[-1] if i > 0 and a[i][0] == a[i - 1][0] else i + 1)
    return res


points = defaultdict(int)
for q in quests:
    for p in [1, 2, 3]:
        a = []
        for id in ids:
            if (id, q, p) in times:
                a.append((times[id, q, p], id))
        a.sort()
        ranking = rank(a)
        for pos, (_, id) in zip(ranking, a):
            points[id] += max(0, 50 * p + 1 - pos)

b = sorted(((p, id) for id, p in points.items()), key=lambda x: -x[0])
ranking = rank(b)

ans3 = 0
for pos, (p, _) in zip(ranking, b):
    ans3 += pos * p
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
