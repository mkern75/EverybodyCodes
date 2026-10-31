from time import time


def neighbours(r, c, R, C):
    for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
        rn, cn = r + dr, c + dc
        if 0 <= rn < R and 0 <= cn < C:
            yield rn, cn


def count_neightbours(r, c, grid, target):
    return sum(1 for rn, cn in neighbours(r, c, len(grid), len(grid[0])) if grid[rn][cn] in target)


def count_grid(grid, target):
    return sum(1 for row in grid for x in row if x in target)


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q05_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]


def find_land(grid):
    R, C = len(grid), len(grid[0])

    grid[R // 2][C // 2] = "#"
    todo = {(R // 2, C // 2)}

    while todo:
        todo_next = set()
        for r, c in todo:
            for rn, cn in neighbours(r, c, R, C):
                if grid[rn][cn] == "#":
                    continue
                if count_neightbours(rn, cn, grid, "#1") >= 5:
                    grid[rn][cn] = "#"
                    todo_next.add((rn, cn))
        todo = todo_next

    for r in range(R):
        for c in range(C):
            if grid[r][c] != "#":
                grid[r][c] = "."


grid = [list(line) for line in data]
find_land(grid)
ans1 = count_grid(grid, "#")

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q05_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]


def find_sand(grid):
    R, C = len(grid), len(grid[0])

    todo = set()
    for r in range(R):
        for c in range(C):
            if grid[r][c] == "#":
                if count_neightbours(r, c, grid, ".") >= 1 or r == 0 or r == R - 1 or c == 0 or c == C - 1:
                    grid[r][c] = "="
                    todo.add((r, c))

    while todo:
        todo_next = set()
        for r, c in todo:
            for rn, cn in neighbours(r, c, R, C):
                if grid[rn][cn] in ".=":
                    continue
                if count_neightbours(rn, cn, grid, "=") >= 5:
                    grid[rn][cn] = "="
                    todo_next.add((rn, cn))
        todo = todo_next


grid = [list(line) for line in data]
find_land(grid)
find_sand(grid)
ans2 = count_grid(grid, "=")

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q05_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]


def check_pattern(r, c, grid):
    if grid[r][c] != "#":
        return False
    for rr in range(r - 2, r + 3):
        for cc in range(c - 2, c + 3):
            if (rr, cc) in [(r, c), (r - 2, c - 2), (r - 2, c + 2), (r + 2, c - 2), (r + 2, c + 2)]:
                continue
            if grid[rr][cc] not in "#@":
                return False
    return True


def check_tree_growth(r, c, grid):
    if grid[r][c] != "#":
        return False
    if count_neightbours(r, c, grid, "=") != 0:
        return False
    if count_neightbours(r, c, grid, "@") < 4:
        return False
    return True


def find_initial_trees(grid):
    R, C = len(grid), len(grid[0])
    for r in range(2, R - 2):
        for c in range(2, C - 2):
            if check_pattern(r, c, grid):
                grid[r][c] = "@"


def run_growth_step(grid):
    R, C = len(grid), len(grid[0])
    grid_new = [grid[r][:] for r in range(R)]
    for r in range(R):
        for c in range(C):
            if check_tree_growth(r, c, grid):
                grid_new[r][c] = "@"
    return grid_new


grid = [list(line) for line in data]
find_land(grid)
find_sand(grid)
find_initial_trees(grid)
grid = run_growth_step(grid)
grid = run_growth_step(grid)
ans3 = count_grid(grid, "@")

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
