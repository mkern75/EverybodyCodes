from time import time


def ff(r, c, f):
    return (r << 48) | (c << 32) | f


def fr(x):
    return x >> 48, (x >> 32) & 0xFFFF, x & 0xFFFFFFFF


def bfs(grid, rs, cs, herbs, progress_output=False):
    herb_ids = sorted({grid[r][c] for r, c in herbs})
    f_target = (1 << len(herb_ids)) - 1

    seen = [[set() for _ in range(m)] for _ in range(n)]
    seen[rs][cs] |= {0}
    q = [ff(rs, cs, 0)]
    dist = 0
    while q:
        qn = []

        if progress_output:
            if dist % 100 == 0:
                print(f"    {str(dist).ljust(4, ' ')} ", end="")
            if dist % 100 == 99:
                print("#")
            else:
                print("#", end="")

        for x in q:
            r, c, f = fr(x)

            if r == rs and c == cs and f == f_target:
                if progress_output:
                    print()
                return dist

            for rn, cn in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if r != 0 or (0 <= rn < n and 0 <= cn < m):
                    if grid[rn][cn] not in "#~":
                        fn = f
                        if grid[rn][cn].isalpha():
                            fn |= 1 << herb_ids.index(grid[rn][cn])
                        if fn not in seen[rn][cn]:
                            seen[rn][cn] |= {fn}
                            qn += [ff(rn, cn, fn)]

        q = qn
        dist += 1


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

grid = data
n, m = len(grid), max(len(row) for row in grid)
rs, cs = 0, next(c for c in range(m) if grid[0][c] == ".")
herbs = [(r, c) for r in range(n) for c in range(m) if grid[r][c].isalpha()]

ans3 = bfs(grid, rs, cs, herbs, True)
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")

