from time import time
from math import prod

# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q16_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

n_cols = 90
spell = list(map(int, data[0].split(",")))
ans1 = sum(n_cols // x for x in spell)

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q16_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

cols = list(map(int, data[0].split(",")))
n_cols = len(cols)
spell = []
for i in range(n_cols):
    while cols[i]:
        spell += [i + 1]
        for j in range(i, n_cols, i + 1):
            cols[j] -= 1
ans2 = prod(spell)

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q16_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

cols = list(map(int, data[0].split(",")))
n_cols = len(cols)
spell = []
for i in range(n_cols):
    while cols[i]:
        spell += [i + 1]
        for j in range(i, n_cols, i + 1):
            cols[j] -= 1

total = 202520252025000
lo, hi = 0, 1 << 63
while lo + 1 < hi:
    mid = (lo + hi) // 2
    if sum(mid // x for x in spell) <= total:
        lo = mid
    else:
        hi = mid
ans3 = lo

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
