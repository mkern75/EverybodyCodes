from time import time

INF = 1 << 63
UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3


class Grid:
    def __init__(self, data):
        self._grid = [list(row) for row in data]
        self.R = len(data)
        self.C = len(data[0])
        self.r_start = -1
        self.c_start = -1
        self.r_end = -1
        self.c_end = -1
        self.sulphur = {}
        for r in range(self.R):
            for c in range(self.C):
                if self._grid[r][c] == "S":
                    self.r_start, self.c_start = r, c
                elif self._grid[r][c] == "E":
                    self.r_end, self.c_end = r, c
                elif self._grid[r][c] == "@":
                    self.sulphur[r, c] = len(self.sulphur)

    def __getitem__(self, key):
        r, c = key
        return self._grid[r][c]

    def moves(self, row, column, direction):
        assert direction in [UP, RIGHT, DOWN, LEFT]
        if direction == UP:
            mv = [(row - 1, column, UP), (row, column - 1, LEFT), (row, column + 1, RIGHT)]
        elif direction == DOWN:
            mv = [(row + 1, column, DOWN), (row, column - 1, LEFT), (row, column + 1, RIGHT)]
        elif direction == LEFT:
            mv = [(row, column - 1, LEFT), (row + 1, column, DOWN), (row - 1, column, UP)]
        else:
            mv = [(row, column + 1, RIGHT), (row + 1, column, DOWN), (row - 1, column, UP)]
        for rn, cn, dn in mv:
            if 0 <= rn < self.R and 0 <= cn < self.C and self[rn, cn] != "#":
                yield rn, cn, dn


def solve1(grid: Grid) -> int:
    todo = [(grid.r_start, grid.c_start, RIGHT, 0, 0)]
    seen = {(grid.r_start, grid.c_start, RIGHT, 0)}
    for r, c, d, msk, t in todo:
        if r == grid.r_end and c == grid.c_end and msk.bit_count() == len(grid.sulphur):
            return t
        for rn, cn, dn in grid.moves(r, c, d):
            mskn = msk | (1 << grid.sulphur[rn, cn]) if grid[rn, cn] == "@" else msk
            if (rn, cn, dn, mskn) not in seen:
                seen.add((rn, cn, dn, mskn))
                todo.append((rn, cn, dn, mskn, t + 1))
    return -1


def solve2(grid: Grid, target: int, exact_match: bool = False) -> int:
    todo = [(grid.r_start, grid.c_start, RIGHT, 0, 0)]
    seen = {(grid.r_start, grid.c_start, RIGHT, 0)}
    for r, c, d, cnt, t in todo:
        if r == grid.r_end and c == grid.c_end and cnt >= target:
            if cnt == target or not exact_match:
                return t
        for rn, cn, dn in grid.moves(r, c, d):
            cntn = cnt + 1 if grid[rn, cn] == "@" else cnt
            if (rn, cn, dn, cntn) not in seen:
                seen.add((rn, cn, dn, cntn))
                todo.append((rn, cn, dn, cntn, t + 1))
    return -1


def solve3(grid: Grid, target: int) -> int:
    sulphur_cycle, time_cycle = 1, 1 << 31
    rr = grid.r_start
    for cc in range(grid.c_start + 1, grid.c_end):
        todo = [(rr, cc, RIGHT, 0, 0)]
        seen = set()
        for r, c, d, cnt, t in todo:
            if r == rr and c == cc and d != LEFT and cnt > 0:
                if t * sulphur_cycle < time_cycle * cnt:
                    sulphur_cycle, time_cycle = cnt, t
                continue
            for rn, cn, dn in grid.moves(r, c, d):
                cntn = cnt + 1 if grid[rn, cn] == "@" else cnt
                if (rn, cn, dn) not in seen:
                    seen.add((rn, cn, dn))
                    todo.append((rn, cn, dn, cntn, t + 1))

    f = max(0, target // sulphur_cycle - 10)
    return f * time_cycle + solve2(grid, target - f * sulphur_cycle, True)


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q15_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans1 = solve1(Grid(data))
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q15_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans2 = solve3(Grid(data), 2026)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q15_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans3 = solve3(Grid(data), 202620262026)
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
