from time import time

def runic_word(grid):
    res = []
    for r in range(2, 6):
        sr = {grid[r][0], grid[r][1], grid[r][-2], grid[r][-1]}
        for c in range(2, 6):
            sc = {grid[0][c], grid[1][c], grid[-2][c], grid[-1][c]}
            res += [list(sr.intersection(sc))[0]]
    return "".join(res)


def runic_word_extended(grid, rb, cb):
    used = set()
    for r in range(2, 6):
        for c in range(2, 6):
            if grid[rb + r][cb + c] != ".":
                used.add(grid[rb + r][cb + c])
    progress = False
    ok = True
    while ok:
        ok = False
        for r in range(2, 6):
            for c in range(2, 6):
                if grid[rb + r][cb + c] != ".":
                    continue
                sr, sc = [], []
                for i in [0, 1, 6, 7]:
                    if grid[rb + r][cb + i] not in used:
                        sr += [grid[rb + r][cb + i]]
                    if grid[rb + i][cb + c] not in used:
                        sc += [grid[rb + i][cb + c]]
                common = []
                for s in sr:
                    if s in sc:
                        common += [s]
                if len(common) == 1 and common[0] != "?":
                    s = common[0]
                    used.add(s)
                    grid[rb + r][cb + c] = s
                    ok = True
                    progress = True
                elif sr.count("?") == sc.count("?") == 0:
                    return -1, progress
                elif not sr or not sc:
                    return -1, progress
                elif len(sr) == len(sc) == 1:
                    if sr[0] == "?" and sc[0] != "?":
                        s = sc[0]
                        used.add(s)
                        grid[rb + r][cb + c] = s
                        ok = True
                        progress = True
                        for i in [0, 1, 6, 7]:
                            if grid[rb + r][cb + i] == "?":
                                grid[rb + r][cb + i] = s
                    elif sr[0] != "?" and sc[0] == "?":
                        s = sr[0]
                        used.add(s)
                        grid[rb + r][cb + c] = s
                        ok = True
                        progress = True
                        for i in [0, 1, 6, 7]:
                            if grid[rb + i][cb + c] == "?":
                                grid[rb + i][cb + c] = s

    cnt = 0
    for r in range(2, 6):
        for c in range(2, 6):
            if grid[rb + r][cb + c] != ".":
                cnt += 1
    return 1 if cnt == 16 else 0, progress


def power(word):
    p = 0
    for i, c in enumerate(word, 1):
        p += i * (ord(c) - 64)
    return p


# ********************************* part 1
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q10_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans1 = runic_word(data)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q10_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
ans2 = 0

for i in range(7):
    for j in range(15):
        rb = i * 9
        cb = j * 9
        g = [["*"] * 8 for _ in range(8)]
        for r in range(8):
            for c in range(8):
                g[r][c] = data[rb + r][cb + c]
        ans2 += power(runic_word(g))

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q10_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

grid = [list(row) for row in data]
n = (len(grid) - 2) // 6
m = (len(grid[0]) - 2) // 6

res = [[-2] * m for _ in range(n)]

progress = True
while progress:
    progress = False
    for i in range(n):
        for j in range(m):
            rb = i * 6
            cb = j * 6
            r, p = runic_word_extended(grid, rb, cb)
            res[i][j] = r
            progress = progress | p

ans3 = 0
for i in range(n):
    for j in range(m):
        if res[i][j] == 1:
            rb = i * 6
            cb = j * 6
            w = []
            for r in range(2, 6):
                w.extend(grid[rb + r][cb + 2:cb + 6])
            ans3 += power("".join(w))

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")

