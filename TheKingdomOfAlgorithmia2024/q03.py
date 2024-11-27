# ********************************* part 1
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q03_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

n, m = len(data), len(data[0])

g = [[-1] * m for _ in range(n)]
q = []

for r in range(n):
    for c in range(m):
        if data[r][c] == ".":
            g[r][c] = 0
            q += [(r, c)]

for r, c in q:
    for rn, cn in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if 0 <= rn < n and 0 <= cn < m:
            if g[rn][cn] == -1:
                g[rn][cn] = g[r][c] + 1
                q += [(rn, cn)]

ans1 = sum(sum(row) for row in g)
print(f"part 1: {ans1}")

# ********************************* part 2
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q03_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

n, m = len(data), len(data[0])

g = [[-1] * m for _ in range(n)]
q = []

for r in range(n):
    for c in range(m):
        if data[r][c] == ".":
            g[r][c] = 0
            q += [(r, c)]

for r, c in q:
    for rn, cn in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if 0 <= rn < n and 0 <= cn < m:
            if g[rn][cn] == -1:
                g[rn][cn] = g[r][c] + 1
                q += [(rn, cn)]

ans2 = sum(sum(row) for row in g)
print(f"part 2: {ans2}")

# ********************************* part 3
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q03_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

n, m = len(data), len(data[0])
d = [["."] * (m + 2) for _ in range(n + 2)]
for r in range(n):
    for c in range(m):
        d[r + 1][c + 1] = data[r][c]
n += 2
m += 2

g = [[-1] * m for _ in range(n)]
q = []

for r in range(n):
    for c in range(m):
        if d[r][c] == ".":
            g[r][c] = 0
            q += [(r, c)]

while q:
    qn = []
    for r, c in q:
        for rn, cn in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1), (r + 1, c + 1), (r + 1, c - 1), (r - 1, c + 1),
                       (r - 1, c - 1)]:
            if 0 <= rn < n and 0 <= cn < m:
                if g[rn][cn] == -1:
                    g[rn][cn] = g[r][c] + 1
                    qn += [(rn, cn)]
    q = qn

ans3 = sum(sum(row) for row in g)
print(f"part 3: {ans3}")

