# The nodes of the tree must be numbered 0 to n-1.
class BasicTree:
    def __init__(self, n: int):
        self.n = n
        self.root = -1
        self.depth = -1
        self.parent = [-1] * n
        self.node_depth = [-1] * n
        self.bfs_tour = []
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u: int, v: int):
        self.adj[u] += [v]
        self.adj[v] += [u]

    def build(self, root: int):
        self.root = root
        self.parent[root] = -1
        self.node_depth[root] = 0
        self.bfs_tour = [root]
        for v in self.bfs_tour:
            for u in self.adj[v]:
                if u != self.parent[v]:
                    self.parent[u] = v
                    self.node_depth[u] = self.node_depth[v] + 1
                    self.bfs_tour += [u]
        self.depth = self.node_depth[self.bfs_tour[-1]]

    def is_leaf(self, node: int) -> bool:
        if node == self.root:
            return len(self.adj[node]) == 0
        else:
            return len(self.adj[node]) == 1

    def is_root(self, node: int) -> bool:
        return node == self.root

    def children(self, node: int):
        for v in self.adj[node]:
            if v != self.parent[node]:
                yield v


def build_tree(data):
    parent, children = {}, {}
    for line in data:
        v, lu = line.split(":")
        lu = lu.split(",")
        children[v] = lu
        for u in lu:
            if u != "@":
                parent[u] = v
    return parent, children


# ********************************* part 1
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q06_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
ans1 = ""

root = "RR"
parent, children = build_tree(data)

q = [[root]]
while q:
    qn, leaves = [], []
    for path in q:
        for u in children[path[-1]]:
            if u == "@":
                leaves += [path + [u]]
            else:
                qn += [path + [u]]
    if len(leaves) == 1:
        ans1 = "".join(leaves[0])
        break
    q = qn

print(f"part 1: {ans1}")

# ********************************* part 2
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q06_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
ans2 = ""

root = "RR"
parent, children = build_tree(data)

q = [[root]]
while q:
    qn, leaves = [], []
    for path in q:
        if path[-1] in children:
            for u in children[path[-1]]:
                if u == "@":
                    leaves += [path + [u]]
                else:
                    qn += [path + [u]]
    if len(leaves) == 1:
        ans2 = "".join(x[0] for x in leaves[0])
        break
    q = qn

print(f"part 2: {ans2}")

# ********************************* part 3
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q06_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
ans3 = ""

root = "RR"
parent, children = build_tree(data)

q = [[root]]
while q:
    qn, leaves = [], []
    for path in q:
        if path[-1] in children:
            for u in children[path[-1]]:
                if u == "@":
                    leaves += [path + [u]]
                else:
                    qn += [path + [u]]
    if len(leaves) == 1:
        ans3 = "".join(x[0] for x in leaves[0])
        break
    q = qn

print(f"part 3: {ans3}")

