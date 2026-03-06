from time import time


class Node:
    def __init__(self, id, plug, left_socket, right_socket, data):
        self.id = id
        self.plug = list(plug.split(" "))
        self.left_socket = list(left_socket.split(" "))
        self.right_socket = list(right_socket.split(" "))
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert1(self, node):
        if self.left_child is None and self.left_socket == node.plug:
            self.left_child = node
            return True
        if self.left_child is not None:
            success = self.left_child.insert1(node)
            if success:
                return True
        if self.right_child is None and self.right_socket == node.plug:
            self.right_child = node
            return True
        if self.right_child is not None:
            success = self.right_child.insert1(node)
            if success:
                return True
        return False

    def insert2(self, node):
        if self.left_child is None and any(self.left_socket[i] == node.plug[i] for i in range(2)):
            self.left_child = node
            return True
        if self.left_child is not None:
            success = self.left_child.insert2(node)
            if success:
                return True
        if self.right_child is None and any(self.right_socket[i] == node.plug[i] for i in range(2)):
            self.right_child = node
            return True
        if self.right_child is not None:
            success = self.right_child.insert2(node)
            if success:
                return True
        return False

    def insert3(self, node):
        node = self.insert_left3(node)
        if node is None:
            return None
        node = self.insert_right3(node)
        if node is None:
            return None
        if self.id == 1 and node is not None:
            node = self.insert3(node)
        return node

    def insert_left3(self, node):
        if self.left_child is None:
            if any(self.left_socket[i] == node.plug[i] for i in range(2)):
                self.left_child = node
                return None
            else:
                return node
        assert self.left_child is not None
        if not all(self.left_socket[i] == self.left_child.plug[i] for i in range(2)):
            if all(self.left_socket[i] == node.plug[i] for i in range(2)):
                prev_child = self.left_child
                self.left_child = node
                return prev_child
        return self.left_child.insert3(node)

    def insert_right3(self, node):
        if self.right_child is None:
            if any(self.right_socket[i] == node.plug[i] for i in range(2)):
                self.right_child = node
                return None
            else:
                return node
        assert self.right_child is not None
        if not all(self.right_socket[i] == self.right_child.plug[i] for i in range(2)):
            if all(self.right_socket[i] == node.plug[i] for i in range(2)):
                prev_child = self.right_child
                self.right_child = node
                return prev_child
        return self.right_child.insert3(node)

    def path(self):
        left = [] if self.left_child is None else self.left_child.path()
        right = [] if self.right_child is None else self.right_child.path()
        return left + [self.id] + right


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q03_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

root = None
for line in data:
    inp = line.split(", ")
    node = Node(int(inp[0][3:]), inp[1][5:], inp[2][11:], inp[3][12:], inp[4][5:])
    if root is None:
        root = node
    else:
        root.insert1(node)
ans1 = sum(i * id for i, id in enumerate(root.path(), start=1))

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q03_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

root = None
for line in data:
    inp = line.split(", ")
    node = Node(int(inp[0][3:]), inp[1][5:], inp[2][11:], inp[3][12:], inp[4][5:])
    if root is None:
        root = node
    else:
        root.insert2(node)
ans2 = sum(i * id for i, id in enumerate(root.path(), start=1))

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q03_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

root = None
for line in data:
    inp = line.split(", ")
    node = Node(int(inp[0][3:]), inp[1][5:], inp[2][11:], inp[3][12:], inp[4][5:])
    if root is None:
        root = node
    else:
        root.insert3(node)
ans3 = sum(i * id for i, id in enumerate(root.path(), start=1))

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
