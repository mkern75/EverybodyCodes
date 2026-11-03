from time import time
from collections import defaultdict


def reachable(v, graph):
    res = set()
    todo = [v]
    while todo:
        v = todo.pop()
        if v in res:
            continue
        res.add(v)
        if v in graph:
            todo.extend(graph[v])
    return res


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q06_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

graph = defaultdict(list)
for line in data:
    id, ingr = line.split(":")
    graph[id] = list(ingr.split(","))

ans1 = len(reachable("NULL", graph)) - 1
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q06_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

graph = defaultdict(list)
for line in data:
    id, ingr = line.split(":")
    for x in ingr.split(","):
        graph[x].append(id)

ans2 = len(reachable("NULL", graph)) - 1
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q06_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

graph = defaultdict(list)
for line in data:
    id, ingr = line.split(":")
    for x in ingr.split(","):
        graph[x].append(id)

r1 = reachable("NULLv1", graph)
r2 = reachable("NULLv2", graph)
r3 = reachable("NULLv3", graph)
ans3 = len(r1.intersection(r2) | r1.intersection(r3) | r2.intersection(r3))
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
