from time import time


class DisjointSetUnion:
    def __init__(self, n):
        self._parent = list(range(n))
        self._size = [1] * n
        self._set_count = n

    def find_set(self, x):
        """Finds the representative of the set that x belongs to."""
        parent = self._parent
        xx = x
        while x != parent[x]:
            x = parent[x]
        while xx != x:
            parent[xx], xx = x, parent[xx]
        return x

    def same_set(self, x, y):
        """Returns true if x and y belong to the same set, and false otherwise."""
        return self.find_set(x) == self.find_set(y)

    def unite_sets(self, x, y):
        """Unites two sets; returns True if the sets were not united before and False otherwise."""
        x = self.find_set(x)
        y = self.find_set(y)
        if x == y:
            return False
        self._parent[y] = x
        self._size[x] += self._size[y]
        self._set_count -= 1
        return True

    def set_size(self, x):
        """Returns the size of the set that x belongs to."""
        return self._size[self.find_set(x)]

    def n_sets(self):
        """Returns the number of disjoint sets."""
        return self._set_count


def manhattan_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def load_stars(data):
    stars = []
    for i, row in enumerate(data):
        for j, c in enumerate(row):
            if c == "*":
                stars += [(j + 1, len(data) - i)]
    return stars


# ********************************* part 1
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q17_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

stars = load_stars(data)
n = len(stars)

dist = sorted((manhattan_dist(*stars[i], *stars[j]), i, j) for i in range(n - 1) for j in range(i + 1, n))
dsu = DisjointSetUnion(n)

ans1 = n
for d, i, j in dist:
    if not dsu.same_set(i, j):
        dsu.unite_sets(i, j)
        ans1 += d

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q17_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

stars = load_stars(data)
n = len(stars)

dist = sorted((manhattan_dist(*stars[i], *stars[j]), i, j) for i in range(n - 1) for j in range(i + 1, n))
dsu = DisjointSetUnion(n)

ans2 = n
for d, i, j in dist:
    if not dsu.same_set(i, j):
        dsu.unite_sets(i, j)
        ans2 += d

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q17_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

stars = load_stars(data)
n = len(stars)

dist = []
for i in range(n - 1):
    for j in range(i + 1, n):
        d = manhattan_dist(*stars[i], *stars[j])
        if d < 6:
            dist += [(d, i, j)]
dist.sort()

dsu = DisjointSetUnion(n)

dist_dsu = [0] * n
for d, i, j in dist:
    if not dsu.same_set(i, j):
        di = dist_dsu[dsu.find_set(i)]
        dj = dist_dsu[dsu.find_set(j)]
        dsu.unite_sets(i, j)
        dist_dsu[dsu.find_set(i)] = di + dj + d

const = sorted([dsu.set_size(i) + dist_dsu[i] for i in range(n) if dsu.find_set(i) == i], reverse=True)
ans3 = const[0] * const[1] * const[2]

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
