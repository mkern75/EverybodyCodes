from time import time
import re

# ********************************* part 1
time_start = time()


def load_plant_data(blocks):
    n_plants = len(blocks)
    thickness = [0] * n_plants
    adj = [[] for _ in range(n_plants)]
    for block in blocks:
        x = re.match(r"Plant (\d+) with thickness (\d+):", block[0])
        plant_id = int(x.groups()[0]) - 1
        thickness[plant_id] = int(x.groups()[1])
        for line in block[1:]:
            if "free" not in line:
                x = re.match(r"- branch to Plant (\d+) with thickness (-?\d+)", line)
                branch_id = int(x.groups()[0]) - 1
                branch_thickness = int(x.groups()[1])
                adj[plant_id].append((branch_id, branch_thickness))
    return n_plants, thickness, adj


def simulate(n_plants, thickness, adj, activation=None):
    plant_energy = [0] * n_plants
    for plant_id in range(n_plants):
        if not adj[plant_id]:
            incoming_energy = 1 if activation is None else activation[plant_id]
        else:
            incoming_energy = sum(
                branch_thickness * plant_energy[branch_id] for branch_id, branch_thickness in adj[plant_id])
        if incoming_energy >= thickness[plant_id]:
            plant_energy[plant_id] = incoming_energy
    return plant_energy[-1]


INPUT_FILE = "./data/q18_p1.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

n_plants, thickness, adj = load_plant_data(blocks)
assert all(branch_id < plant_id for plant_id in range(n_plants) for branch_id, _ in adj[plant_id])

ans1 = simulate(n_plants, thickness, adj)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()


def load_activation_data(block):
    return [list(map(int, line.split())) for line in block[1:]]


INPUT_FILE = "./data/q18_p2.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

n_plants, thickness, adj = load_plant_data(blocks[:-1])
activation = load_activation_data(blocks[-1])
assert all(branch_id < plant_id for plant_id in range(n_plants) for branch_id, _ in adj[plant_id])

ans2 = sum(simulate(n_plants, thickness, adj, act) for act in activation)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()

INPUT_FILE = "./data/q18_p3.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

n_plants, thickness, adj = load_plant_data(blocks[:-1])
activation = load_activation_data(blocks[-1])
assert all(branch_id < plant_id for plant_id in range(n_plants) for branch_id, _ in adj[plant_id])

n_inputs = sum(1 for plant_id in range(n_plants) if not adj[plant_id])
assert all(not adj[plant_id] for plant_id in range(n_inputs))

pos, neg = [0] * n_inputs, [0] * n_inputs
for plant_id in range(n_inputs, n_plants):
    for branch_id, branch_thickness in adj[plant_id]:
        if branch_id < n_inputs:
            if branch_thickness > 0:
                pos[branch_id] = 1
            elif branch_thickness < 0:
                neg[branch_id] = 1

# this is NOT true for the simple example
assert all(pos[plant_id] * neg[plant_id] == 0 for plant_id in range(n_inputs))

ans3 = 0
max_result = simulate(n_plants, thickness, adj, pos)
for act in activation:
    result = simulate(n_plants, thickness, adj, act)
    if result:
        ans3 += max_result - result

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
