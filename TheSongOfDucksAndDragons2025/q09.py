from time import time

# ********************************* part 1
time_start = time()


def similarity(child: str, parent1: str, parent2: str) -> int:
    c1, c2 = 0, 0
    for i in range(len(child)):
        if child[i] != parent1[i] and child[i] != parent2[i]:
            return 0
        if child[i] == parent1[i]:
            c1 += 1
        if child[i] == parent2[i]:
            c2 += 1
    return c1 * c2


INPUT_FILE = "./data/q09_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

dna = list(line.split(":")[1] for line in data)
ans1 = max(similarity(dna[0], dna[1], dna[2]),
           similarity(dna[1], dna[0], dna[2]),
           similarity(dna[2], dna[0], dna[1]))
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()


def is_child(child: str, parent1: str, parent2: str) -> bool:
    for i in range(len(child)):
        if child[i] != parent1[i] and child[i] != parent2[i]:
            return False
    return True


def find_parents(i: int, dna: list[str]) -> tuple:
    n = len(dna)
    for j in range(n - 1):
        if i == j:
            continue
        for k in range(j + 1, n):
            if i == k:
                continue
            if is_child(dna[i], dna[j], dna[k]):
                return j, k
    return -1, -1


INPUT_FILE = "./data/q09_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

dna = list(line.split(":")[1] for line in data)
n = len(dna)

ans2 = 0
for i in range(n):
    p1, p2 = find_parents(i, dna)
    if p1 != -1 and p2 != -1:
        ans2 += similarity(dna[i], dna[p1], dna[p2])
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()


class DSU:
    def __init__(self, n):
        self._parent = list(range(n))

    def find(self, x):
        parent = self._parent
        y = x
        while x != parent[x]:
            x = parent[x]
        while y != x:
            parent[y], y = x, parent[y]
        return x

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        self._parent[y] = x
        return True


INPUT_FILE = "./data/q09_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

dna = list(line.split(":")[1] for line in data)
n = len(dna)

dsu = DSU(n)
for i in range(n):
    p1, p2 = find_parents(i, dna)
    if p1 != -1 and p2 != -1:
        dsu.unite(i, p1)
        dsu.unite(i, p2)

sz, sm = [0] * n, [0] * n
for i in range(n):
    sz[dsu.find(i)] += 1
    sm[dsu.find(i)] += i + 1  # 1-indexed
ans3 = sm[sz.index(max(sz))]
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
