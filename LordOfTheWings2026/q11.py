from time import time

INF = 1 << 31


def parse(data):
    n = int(data[0][9:])
    shortcuts = []
    for line in data[2:]:
        u, v = map(lambda x: int(x) - 1, line.split())
        shortcuts.append((u, v))
    return n, shortcuts


def calc_distance(n, edges, start):
    dist = [INF] * n
    dist[start] = 0
    todo = [start]
    for u in todo:
        for v in edges[u]:
            if dist[v] == INF:
                dist[v] = dist[u] + 1
                todo.append(v)
    return dist


def solve(n, k, shortcuts):
    edges = [[] for _ in range(n)]
    for u in range(n):
        for i in range(1, k + 1):
            edges[u].append((u - i) % n)
            edges[u].append((u + i) % n)
    res1 = n * sum(calc_distance(n, edges, 0))

    for u, v in shortcuts:
        edges[u].append(v)
        edges[v].append(u)
    res2 = sum(sum(calc_distance(n, edges, start)) for start in range(n))

    return res1 - res2


def calc_all_portal_options(crystals):
    res = []
    all_pairs_helper([], crystals, res)
    return res


def all_pairs_helper(so_far, remaining, res):
    if not remaining:
        res.append(so_far)
    for i in range(1, len(remaining)):
        all_pairs_helper(so_far + [(remaining[0], remaining[i])], remaining[1:i] + remaining[i + 1:], res)


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q11_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

n, shortcuts = parse(data)
ans1 = solve(n, 1, shortcuts)

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q11_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

n, shortcuts = parse(data)
ans2 = 0
for u in range(n - 1):
    for v in range(u + 1, n):
        ans2 = max(ans2, solve(n, 3, shortcuts + [(u, v)]))

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q11_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

n, shortcuts = parse(data)
ans3 = 0
for i in range(n // 8):
    crystals = [i + j * (n // 8) for j in range(8)]
    for extra_portals in calc_all_portal_options(crystals):
        ans3 = max(ans3, solve(n, 3, shortcuts + extra_portals))

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
