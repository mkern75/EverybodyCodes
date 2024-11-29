from time import time

N8 = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def rotate(dir, grid, r, c):
    offset = 1 if dir == "L" else -1
    mem = []
    for i in range(8):
        mem += [grid[r + N8[i][0]][c + N8[i][1]]]
    for i in range(8):
        grid[r + N8[i][0]][c + N8[i][1]] = mem[(i + offset) % 8]


def calc_mapping(grid, key):
    n, m = len(grid), len(grid[0])
    grid_other = [[] for _ in range(n)]
    for r in range(n):
        for c in range(m):
            grid_other[r] += [(r, c)]
    i = 0
    for r in range(1, n - 1):
        for c in range(1, m - 1):
            rotate(key[i], grid_other, r, c)
            i = (i + 1) % len(key)
    mapping = {}
    for r in range(n):
        for c in range(m):
            rr, cc = grid_other[r][c]
            mapping[rr, cc] = r, c
    return mapping


def find_cycle(mapping, rs, cs):
    cycle = [(rs, cs)]
    r, c = rs, cs
    while True:
        r, c = mapping[r, c]
        if r == rs and c == cs:
            break
        cycle += [(r, c)]
    return cycle


def calc_cycles(grid, key):
    n, m = len(grid), len(grid[0])
    cycles = [[[] for _ in range(m)] for _ in range(n)]
    mapping = calc_mapping(grid, key)
    for r in range(n):
        for c in range(m):
            cycles[r][c].extend(find_cycle(mapping, r, c))
    return cycles


def simulate(grid, key, cnt):
    n, m = len(grid), len(grid[0])
    res = [["."] * m for _ in range(n)]
    cycles = calc_cycles(grid, key)
    for r in range(n):
        for c in range(m):
            rr, cc = cycles[r][c][cnt % len(cycles[r][c])]
            res[rr][cc] = grid[r][c]
    for row in res:
        if ">" in row and "<" in row:
            s = "".join(row)
            return s[s.index(">") + 1: s.index("<")]
    assert False


# ********************************* part 1
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q19_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

key = data[0]
grid = [list(data[i]) for i in range(2, len(data))]

ans1 = simulate(grid, key, 1)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q19_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

key = data[0]
grid = [list(data[i]) for i in range(2, len(data))]

ans2 = simulate(grid, key, 100)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q19_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

key = data[0]
grid = [list(data[i]) for i in range(2, len(data))]

ans3 = simulate(grid, key, 1048576000)
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
