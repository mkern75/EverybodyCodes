from time import time
from collections import defaultdict

# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q06_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

d = {}
for line in data:
    id, ingr = line.split(":")
    d[id] = list(ingr.split(","))

done, todo = set(), ["NULL"]
while todo:
    x = todo.pop()
    if x in done:
        continue
    done.add(x)
    if x in d:
        todo.extend(d[x])

ans1 = len(done) - 1
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q06_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

d = defaultdict(list)
for line in data:
    id, ingr = line.split(":")
    for x in ingr.split(","):
        d[x].append(id)

done, todo = set(), ["NULL"]
while todo:
    x = todo.pop()
    if x in done:
        continue
    done.add(x)
    todo.extend(d[x])

ans2 = len(done) - 1
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q06_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

d = {}
for line in data:
    id, ingr = line.split(":")
    d[id] = list((ingr.split(",")))

# brute force
ans3 = 0
for v in d.keys():
    done, todo = set(), [v]
    while todo:
        x = todo.pop()
        if x in done:
            continue
        done.add(x)
        if x in d:
            todo.extend(d[x])
    if sum(1 for x in done if x.startswith("NULL")) >= 2:
        ans3 += 1

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
