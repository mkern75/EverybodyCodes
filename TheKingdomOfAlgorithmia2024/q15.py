from time import time

INF = 1 << 63


def ff(r, c, f):
    return (r << 48) | (c << 32) | f


def fr(x):
    return x >> 48, (x >> 32) & 0xFFFF, x & 0xFFFFFFFF


def bfs(grid, rs, cs, herbs, c_min=None, c_max=None):
    n, m = len(grid), max(len(row) for row in grid)
    if c_min is None:
        c_min = 0
    if c_max is None:
        c_max = m - 1

    herb_ids = sorted({grid[r][c] for r, c in herbs})
    f_target = (1 << len(herb_ids)) - 1

    seen = [[set() for _ in range(m)] for _ in range(n)]
    seen[rs][cs] |= {0}

    dist = 0
    q = [ff(rs, cs, 0)]
    while q:
        qn = []

        for x in q:
            r, c, f = fr(x)

            if r == rs and c == cs and f == f_target:
                return dist

            for rn, cn in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= rn < n and c_min <= cn <= c_max:
                    if grid[rn][cn] not in "#~":
                        fn = f
                        if grid[rn][cn].isalpha():
                            fn |= 1 << herb_ids.index(grid[rn][cn])
                        if fn not in seen[rn][cn]:
                            seen[rn][cn] |= {fn}
                            qn += [ff(rn, cn, fn)]

        q = qn
        dist += 1


def solve_part_3(grid):
    """This takes advantage of the unique characteristics of the input grid."""
    n, m = len(grid), max(len(row) for row in grid)

    # start point
    rs, cs = 0, next(c for c in range(m) if grid[0][c] == ".")

    # entry point to left segment
    r1, c1 = 75, 85
    grid[r1][c1] = "Z"  # dummy herb

    # entry point to right segment
    r2, c2 = 75, 169
    grid[r2][c2] = "Y"  # dummy herb

    herbs_left, herbs_middle, herbs_right = [], [], []
    for r in range(n):
        for c in range(m):
            if grid[r][c].isalpha():
                if c <= c1:
                    herbs_left += [(r, c)]
                if c1 <= c <= c2:
                    herbs_middle += [(r, c)]
                if c2 <= c:
                    herbs_right += [(r, c)]

    dist_left = bfs(grid, r1, c1, herbs_left, 0, c1)
    dist_midle = bfs(grid, rs, cs, herbs_middle, c1, c2)
    dist_right = bfs(grid, r2, c2, herbs_right, c2, m - 1)

    return dist_left + dist_midle + dist_right


# ********************************* part 1
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q15_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid = data
n, m = len(grid), max(len(row) for row in grid)
rs, cs = 0, next(c for c in range(m) if grid[0][c] == ".")
herbs = [(r, c) for r in range(n) for c in range(m) if grid[r][c].isalpha()]

ans1 = bfs(grid, rs, cs, herbs)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q15_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid = data
n, m = len(grid), max(len(row) for row in grid)
rs, cs = 0, next(c for c in range(m) if grid[0][c] == ".")
herbs = [(r, c) for r in range(n) for c in range(m) if grid[r][c].isalpha()]

ans2 = bfs(grid, rs, cs, herbs)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q15_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid = [list(row) for row in data]
n, m = len(grid), max(len(row) for row in grid)
rs, cs = 0, next(c for c in range(m) if grid[0][c] == ".")
herbs = [(r, c) for r in range(n) for c in range(m) if grid[r][c].isalpha()]

ans3 = solve_part_3(grid)
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
