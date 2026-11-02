from time import time


class Grid:

    def __init__(self, n_rows, n_cols):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self._grid = [["?"] * self.n_cols for _ in range(self.n_rows)]

    @classmethod
    def load_from_data(cls, data):
        grid = Grid(len(data), len(data[0]))
        for r, line in enumerate(data):
            for c, val in enumerate(line):
                grid.set(r, c, val)
        return grid

    def set(self, r, c, val):
        self._grid[r][c] = val

    def get(self, r, c):
        return self._grid[r][c]

    def neighbours(self, r, c):
        for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
            rn, cn = r + dr, c + dc
            if 0 <= rn < self.n_rows and 0 <= cn < self.n_cols:
                yield rn, cn

    def count_neightbours(self, r, c, target):
        return sum(1 for rn, cn in self.neighbours(r, c) if self.get(rn, cn) in target)

    def count(self, target):
        return sum(1 for r in range(self.n_rows) for c in range(self.n_cols) if self.get(r, c) in target)

    def find_land(self):
        self.set(self.n_rows // 2, self.n_cols // 2, "#")
        todo = {(self.n_rows // 2, self.n_cols // 2)}
        while todo:
            todo_next = set()
            for r, c in todo:
                for rn, cn in self.neighbours(r, c):
                    if self.get(rn, cn) == "#":
                        continue
                    if self.count_neightbours(rn, cn, "#1") >= 5:
                        self.set(rn, cn, "#")
                        todo_next.add((rn, cn))
            todo = todo_next
        for r in range(self.n_rows):
            for c in range(self.n_cols):
                if self.get(r, c) != "#":
                    self.set(r, c, ".")

    def find_sand(self):
        todo = set()
        for r in range(self.n_rows):
            for c in range(self.n_cols):
                if self.get(r, c) == "#":
                    if self.count_neightbours(r, c, ".") >= 1 or r in [0, self.n_rows - 1] or c in [0, self.n_cols - 1]:
                        self.set(r, c, "=")
                        todo.add((r, c))
        while todo:
            todo_next = set()
            for r, c in todo:
                for rn, cn in self.neighbours(r, c):
                    if self.get(rn, cn) in ".=":
                        continue
                    if self.count_neightbours(rn, cn, "=") >= 5:
                        self.set(rn, cn, "=")
                        todo_next.add((rn, cn))
            todo = todo_next

    def find_trees(self):
        self._find_initial_trees()
        for _ in range(2):
            self._run_growth_step()

    def _check_pattern(self, r, c):
        if self.get(r, c) != "#":
            return False
        for rr in range(r - 2, r + 3):
            for cc in range(c - 2, c + 3):
                if (rr, cc) in [(r, c), (r - 2, c - 2), (r - 2, c + 2), (r + 2, c - 2), (r + 2, c + 2)]:
                    continue
                if self.get(rr, cc) not in "#@":
                    return False
        return True

    def _check_tree_growth(self, r, c):
        if self.get(r, c) != "#":
            return False
        if self.count_neightbours(r, c, "=") != 0:
            return False
        if self.count_neightbours(r, c, "@") < 4:
            return False
        return True

    def _find_initial_trees(self):
        for r in range(2, self.n_rows - 2):
            for c in range(2, self.n_cols - 2):
                if self._check_pattern(r, c):
                    self.set(r, c, "@")

    def _run_growth_step(self):
        grid_new = [self._grid[r][:] for r in range(self.n_rows)]
        for r in range(self.n_rows):
            for c in range(self.n_cols):
                if self._check_tree_growth(r, c):
                    grid_new[r][c] = "@"
        for r in range(self.n_rows):
            for c in range(self.n_cols):
                self.set(r, c, grid_new[r][c])


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q05_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid = Grid.load_from_data(data)
grid.find_land()
ans1 = grid.count("#")
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q05_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid = Grid.load_from_data(data)
grid.find_land()
grid.find_sand()
ans2 = grid.count("=")
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q05_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid = Grid.load_from_data(data)
grid.find_land()
grid.find_sand()
grid.find_trees()
ans3 = grid.count("@")
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
