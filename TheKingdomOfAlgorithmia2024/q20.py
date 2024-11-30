from time import time

NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3
MOVES = {NORTH: [(0, -1, WEST), (-1, 0, NORTH), (0, 1, EAST)],
         EAST: [(-1, 0, NORTH), (0, 1, EAST), (1, 0, SOUTH)],
         SOUTH: [(0, 1, EAST), (1, 0, SOUTH), (0, -1, WEST)],
         WEST: [(1, 0, SOUTH), (0, -1, WEST), (-1, 0, NORTH)]}
ALTITUDE_CHANGE = {"+": 1, ".": -1, "-": -2, "S": -1, "A": -1, "B": -1, "C": -1}
CHECK_POINTS = "ABC"


def ff(r, c, d, p=0):
    return (r << 28) | (c << 16) | (d << 4) | p


def fr(x):
    return x >> 28, (x >> 16) & 0xFFF, (x >> 4) & 0xF, x & 0xF


# ********************************* part 1
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q20_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid = data
n, m = len(data), len(data[0])
rs, cs = 0, next(c for c, v in enumerate(grid[0]) if v == "S")

s = {ff(rs, cs, d): 1000 for d in MOVES.keys()}  # states
for _ in range(100):
    sn = {}
    for x, alt in s.items():
        r, c, d, _ = fr(x)
        for dr, dc, dn in MOVES[d]:
            rn, cn = r + dr, c + dc
            if 0 <= rn < n and 0 <= cn < m and grid[rn][cn] in ".-+":
                altn = alt + ALTITUDE_CHANGE[grid[rn][cn]]
                x = ff(rn, cn, dn)
                if x in sn:
                    sn[x] = max(sn[x], altn)
                else:
                    sn[x] = altn
    s = sn
ans1 = max(s.values())

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q20_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid = data
n, m = len(data), len(data[0])
rs, cs = 0, next(c for c, v in enumerate(grid[0]) if v == "S")

s = {ff(rs, cs, d, 0): 10_000 for d in MOVES.keys()}  # states
t = 0
ans2 = -1

while ans2 == -1:
    t += 1
    sn = {}
    for x, alt in s.items():
        r, c, d, p = fr(x)
        for dr, dc, dn in MOVES[d]:
            rn, cn, pn = r + dr, c + dc, p
            if 0 <= rn < n and 0 <= cn < m and grid[rn][cn] in ".-+ABCS":
                altn = alt + ALTITUDE_CHANGE[grid[rn][cn]]
                if grid[rn][cn] == "S":
                    if altn >= 10_000 and pn == len(CHECK_POINTS):
                        ans2 = t
                        break
                    else:
                        continue
                elif grid[rn][cn] in CHECK_POINTS:
                    if pn == CHECK_POINTS.index(grid[rn][cn]):
                        pn += 1
                    else:
                        continue
                x = ff(rn, cn, dn, pn)
                if x in sn:
                    sn[x] = max(sn[x], altn)
                else:
                    sn[x] = altn
    s = sn

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q20_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid = data
n, m = len(data), len(data[0])
rs, cs = 0, next(c for c, v in enumerate(grid[0]) if v == "S")

ans3 = 0
alt = 384_400
r, c = 0, next(c for c, v in enumerate(grid[0]) if v == "S")
d = SOUTH
t = 0

"""Remember, you're solving puzzles, not finding general solutions, so checking your input notes could be important!"""
while alt > 0:  # this logic is unique to my puzzle input
    t += 1
    if t <= 4:
        c = c + 1
        d = EAST
        alt += ALTITUDE_CHANGE[grid[r][c]]
    else:
        r = (r + 1) % n
        d = SOUTH
        alt += ALTITUDE_CHANGE[grid[r][c]]
        ans3 += 1

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
