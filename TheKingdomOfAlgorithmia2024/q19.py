from time import time

N8 = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
SHOW_GRID = False


def ff(r, c, m):
    return r * m + c


def fr(x, m):
    return divmod(x, m)


def rotate(dir, grid, r_centre, c_centre):
    assert dir in "LR"
    offset = 1 if dir == "L" else -1
    mem = []
    for i in range(8):
        mem += [grid[r_centre + N8[i][0]][c_centre + N8[i][1]]]
    for i in range(8):
        grid[r_centre + N8[i][0]][c_centre + N8[i][1]] = mem[(i + offset) % 8]


def calc_mapping(grid, key):
    n, m = len(grid), len(grid[0])

    gg = [[0] * m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            gg[r][c] = ff(r, c, m)

    i = 0
    for r in range(1, n - 1):
        for c in range(1, m - 1):
            rotate(key[i], gg, r, c)
            i = (i + 1) % len(key)

    mapping = [[0] * m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            rr, cc = fr(gg[r][c], m)
            mapping[rr][cc] = ff(r, c, m)
    return mapping


def find_cycle(rs, cs, mapping):
    m = len(mapping[0])
    cycle = [ff(rs, cs, m)]
    r, c = rs, cs
    while True:
        r, c = fr(mapping[r][c], m)
        if r == rs and c == cs:
            break
        cycle += [ff(r, c, m)]
    return cycle


def calc_cycles(grid, key):
    n, m = len(grid), len(grid[0])
    mapping = calc_mapping(grid, key)
    cycles = []
    cycle_id = [[-1] * m for _ in range(n)]
    cycle_pos = [[-1] * m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            if cycle_id[r][c] == -1:
                cycle = find_cycle(r, c, mapping)
                id = len(cycles)
                cycles += [cycle]
                for pos, x in enumerate(cycle):
                    rr, cc = fr(x, m)
                    cycle_id[rr][cc] = id
                    cycle_pos[rr][cc] = pos
    return cycles, cycle_id, cycle_pos


def simulate(grid, key, cnt):
    n, m = len(grid), len(grid[0])

    res = [["."] * m for _ in range(n)]
    cycles, cycle_id, cycle_pos = calc_cycles(grid, key)
    for r in range(n):
        for c in range(m):
            id = cycle_id[r][c]
            pos = cycle_pos[r][c]
            rr, cc = fr(cycles[id][(pos + cnt) % len(cycles[id])], m)
            res[rr][cc] = grid[r][c]

    if SHOW_GRID:
        print()
        for row in res:
            print("".join(row))

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
