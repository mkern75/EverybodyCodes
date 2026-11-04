from time import time
from collections import Counter


def load(data):
    ids, energy, connections = [], {}, {}
    for line in data:
        parts = line.split(", ")
        id = int(parts[0][3:])
        ids.append(id)
        energy[id] = int(parts[1][7:])
        connections[id] = list(map(int, parts[2][12:].split(",")))
    return ids, energy, connections


def simulate(id_start, impulse_start, ids, energy_start, connections, explosion=1 << 31):
    energy = energy_start.copy()
    todo = Counter({(id_start, impulse_start): 1})
    active = {id: True for id in ids}

    while todo:
        todo_next = Counter()
        for (id, strength), cnt in todo.items():
            if not active[id] or strength == 0:
                continue
            energy[id] += cnt * strength
            for cid in connections[id]:
                if not active[cid]:
                    continue
                todo_next[(cid, strength - 1)] += cnt

        for id, e in energy.items():
            if e >= explosion:
                active[id] = False
                energy[id] = 0
                for cid in connections[id]:
                    if not active[cid]:
                        continue
                    todo_next[(cid, 10)] += 1

        todo = todo_next

    return energy


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q07_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ids, energy, connections = load(data)
start = max(ids, key=lambda id: len(connections[id]))
ans1 = sum(simulate(start, 5, ids, energy, connections).values())
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q07_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ids, energy, connections = load(data)
start = max(ids, key=lambda id: len(connections[id]))
ans2 = sum(simulate(start, 10, ids, energy, connections).values())
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q07_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ids, energy, connections = load(data)
ans3 = max(sum(simulate(start, 10, ids, energy, connections, 1000000).values()) for start in ids)
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
