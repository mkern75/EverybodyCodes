from time import time
from collections import Counter


def get_columns(data):
    col = [[] for _ in range(4)]
    for line in data:
        row = list(map(int, line.split()))
        for i, x in enumerate(row):
            col[i] += [x]
    return col


def insert_into_column(n, col):
    k = len(col)
    nn = (n - 1) % (2 * k) + 1
    if nn <= k:
        col.insert(nn - 1, n)
    else:
        col.insert(k - (nn - k - 1), n)


def get_number(col):
    return int("".join(map(str, [c[0] for c in col])))


# ********************************* part 1
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q05_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
ans1 = 0

col = get_columns(data)

for rnd in range(1, 10 + 1):
    v = col[(rnd - 1) % 4].pop(0)
    insert_into_column(v, col[rnd % 4])

ans1 = get_number(col)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q05_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
ans2 = 0

col = get_columns(data)

cnt = Counter()
rnd = 1
while True:
    v = col[(rnd - 1) % 4].pop(0)
    insert_into_column(v, col[rnd % 4])
    n = get_number(col)
    cnt[n] += 1
    if cnt[n] == 2024:
        ans2 = n * rnd
        break
    rnd += 1

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q05_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
ans3 = 0

col = get_columns(data)

seen = set()
rnd = 1
while True:
    v = col[(rnd - 1) % 4].pop(0)
    insert_into_column(v, col[rnd % 4])
    n = get_number(col)
    ans3 = max(ans3, n)
    h = tuple([hash(rnd % 4)] + [hash(tuple(c)) for c in col])
    if h in seen:
        break
    else:
        seen.add(h)

    rnd += 1

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")

