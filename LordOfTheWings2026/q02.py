from time import time
from collections import defaultdict


def parse(line):
    n, edges = 0, defaultdict(set)
    for s in line.split():
        x, c, y = int(s[0]), s[1], int(s[2])
        n = max(n, x + 1, y + 1)
        if c == ">":
            edges[x].add(y)
        else:
            edges[y].add(x)
    return n, edges


def topological_sort_kahn(n_nodes, directed_edges):
    in_degree = [0] * n_nodes
    for edges in directed_edges.values():
        for v in edges:
            in_degree[v] += 1
    res = []
    stack = [v for v, d in enumerate(in_degree) if d == 0]
    while stack:
        v = stack.pop()
        res += [v]
        for u in directed_edges[v]:
            in_degree[u] -= 1
            if in_degree[u] == 0:
                stack += [u]
    return res if len(res) == n_nodes else None


def solve(n, edges):
    res = 0
    ts = topological_sort_kahn(n, edges)
    assert ts is not None
    for k in ts:
        if k != 0:
            res = (res * 10) + k
    return res


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q02_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans1 = 0
for line in data:
    n_nodes, edges = parse(line)
    ans1 += solve(n_nodes, edges)

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q02_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans2 = 0
for line in data:
    n_nodes, edges = parse(line)
    ans2 += solve(n_nodes, edges)

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q02_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans3 = 0
for line in data:
    n_nodes, edges = parse(line)
    ans3 += solve(n_nodes, edges)

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
