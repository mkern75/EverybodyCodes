from time import time
import re


class Node:
    def __init__(self, parent, rank, symbol):
        self.parent = parent
        self.rank = rank
        self.symbol = symbol
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, rank, symbol):
        if self.root is None:
            self.root = Node(None, rank, symbol)
            return self.root
        node = self.root
        while True:
            if rank < node.rank:
                if node.left is None:
                    node.left = Node(node, rank, symbol)
                    return node.left
                else:
                    node = node.left
            elif rank > node.rank:
                if node.right is None:
                    node.right = Node(node, rank, symbol)
                    return node.right
                else:
                    node = node.right
            else:
                assert False

    def symbols_most_nodes(self) -> str:
        if not self.root:
            return ""
        most_nodes = [self.root]
        nodes = [self.root]
        while nodes:
            nodes_new = []
            for node in nodes:
                if node.left:
                    nodes_new.append(node.left)
                if node.right:
                    nodes_new.append(node.right)
            nodes = nodes_new
            if len(nodes) > len(most_nodes):
                most_nodes = nodes
        return "".join(node.symbol for node in most_nodes)


# ********************************* part 1
time_start = time()
INPUT_FILE = "./EchoesOfEnigmatus/data/q02_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

tree_left, tree_right = Tree(), Tree()
for row in data:
    m = re.match(r"ADD id=(\d+) left=\[(\d+),(.*)] right=\[(\d+),(.*)]", row)
    rank_left, symbol_left = int(m.groups()[1]), m.groups()[2]
    rank_right, symbol_right = int(m.groups()[3]), m.groups()[4]
    tree_left.add(rank_left, symbol_left)
    tree_right.add(rank_right, symbol_right)

ans1 = tree_left.symbols_most_nodes() + tree_right.symbols_most_nodes()
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./EchoesOfEnigmatus/data/q02_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

tree_left, tree_right = Tree(), Tree()
id_map = {}
for row in data:
    if row.startswith("ADD"):
        m = re.match(r"ADD id=(\d+) left=\[(\d+),(.*)] right=\[(\d+),(.*)]", row)
        id = int(m.groups()[0])
        rank_left, symbol_left = int(m.groups()[1]), m.groups()[2]
        rank_right, symbol_right = int(m.groups()[3]), m.groups()[4]
        node_left = tree_left.add(rank_left, symbol_left)
        node_right = tree_right.add(rank_right, symbol_right)
        id_map[id] = (node_left, node_right)

    elif row.startswith("SWAP"):
        m = re.match(r"SWAP (\d+)", row)
        id = int(m.groups()[0])
        node_left, node_right = id_map[id]
        node_left.rank, node_right.rank = node_right.rank, node_left.rank
        node_left.symbol, node_right.symbol = node_right.symbol, node_left.symbol

ans2 = tree_left.symbols_most_nodes() + tree_right.symbols_most_nodes()
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./EchoesOfEnigmatus/data/q02_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

tree_left, tree_right = Tree(), Tree()
id_map = {}
for row in data:
    if row.startswith("ADD"):
        m = re.match(r"ADD id=(\d+) left=\[(\d+),(.*)] right=\[(\d+),(.*)]", row)
        id = int(m.groups()[0])
        rank_left, symbol_left = int(m.groups()[1]), m.groups()[2]
        rank_right, symbol_right = int(m.groups()[3]), m.groups()[4]
        node_left = tree_left.add(rank_left, symbol_left)
        node_right = tree_right.add(rank_right, symbol_right)
        id_map[id] = (node_left, node_right)

    elif row.startswith("SWAP"):
        m = re.match(r"SWAP (\d+)", row)
        id = int(m.groups()[0])
        node_left, node_right = id_map[id]

        if id == 1:
            tree_left, tree_right = tree_right, tree_left
        else:
            parent_left = node_left.parent
            parent_right = node_right.parent
            if parent_left.left == node_left:
                parent_left.left = node_right
            else:
                parent_left.right = node_right
            if parent_right.left == node_right:
                parent_right.left = node_left
            else:
                parent_right.right = node_left
            node_left.parent, node_right.parent = parent_right, parent_left

ans3 = tree_left.symbols_most_nodes() + tree_right.symbols_most_nodes()
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
