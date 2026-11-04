from time import time
from collections import Counter

INF = 1 << 63


def load(data):
    graph, energy = {}, {}
    for line in data:
        parts = line.split(", ")
        id = int(parts[0][3:])
        energy[id] = int(parts[1][7:])
        graph[id] = list(map(int, parts[2][12:].split(",")))
    return graph, energy


def simulate(start, impulse_initial, graph, energy, explosion=INF):
    energy_current = energy.copy()
    todo = Counter({(start, impulse_initial): 1})
    active = {id: True for id in graph.keys()}

    while todo:
        todo_next = Counter()
        for (id, strength), cnt in todo.items():
            if not active[id] or not strength:
                continue
            energy_current[id] += cnt * strength
            for cid in graph[id]:
                todo_next[(cid, strength - 1)] += cnt

        for id, e in energy_current.items():
            if e >= explosion:
                active[id] = False
                energy_current[id] = 0
                for cid in graph[id]:
                    todo_next[(cid, 10)] += 1

        todo = todo_next

    return sum(energy_current.values())


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q07_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

graph, energy = load(data)
start = max(graph.keys(), key=lambda id: len(graph[id]))
ans1 = simulate(start, 5, graph, energy)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q07_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

graph, energy = load(data)
start = max(graph.keys(), key=lambda id: len(graph[id]))
ans2 = simulate(start, 10, graph, energy)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q07_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

graph, energy = load(data)
ans3 = max(simulate(start, 10, graph, energy, 1000000) for start in graph.keys())
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
