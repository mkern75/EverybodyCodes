from time import time

# ********************************* part 1
time_start = time()


def explode(start, grid, n, m, destroyed_before=None):
    if destroyed_before is None:
        destroyed_before = set()
    if all((r, c) in destroyed_before for r, c in start):
        return set()
    destroyed_new = set(start)
    todo = start[:]
    for r, c in todo:
        for rr, cc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if 0 <= rr < n and 0 <= cc < m:
                if (rr, cc) not in destroyed_before and (rr, cc) not in destroyed_new:
                    if grid[rr][cc] <= grid[r][c]:
                        destroyed_new.add((rr, cc))
                        todo.append((rr, cc))
    return destroyed_new


INPUT_FILE = "./data/q12_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid = [list(map(int, list(line))) for line in data]
n, m = len(grid), len(grid[0])
ans1 = len(explode([(0, 0)], grid, n, m))
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q12_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid = [list(map(int, list(line))) for line in data]
n, m = len(grid), len(grid[0])
ans2 = len(explode([(0, 0), (n - 1, m - 1)], grid, n, m))
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q12_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid = [list(map(int, list(line))) for line in data]
n, m = len(grid), len(grid[0])

destroyed = set()
for _ in range(3):
    best = set()
    for r in range(n):
        for c in range(m):
            destroyed_tmp = explode([(r, c)], grid, n, m, destroyed)
            if len(destroyed_tmp) > len(best):
                best = destroyed_tmp
    destroyed.update(best)
ans3 = len(destroyed)
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
