from time import time
from collections import Counter


def load_machine(data):
    turns = list(map(int, data[0].split(",")))
    n = len(turns)
    faces = [[] for _ in range(n)]
    for line in data[2:]:
        for i in range(n):
            if line[i * 4:i * 4 + 3] not in ["", "   "]:
                faces[i] += [line[i * 4:i * 4 + 3]]
    return n, turns, faces


# ********************************* part 1
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q16_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

n, turns, faces = load_machine(data)

pos = [0] * n
for _ in range(100):
    for i in range(n):
        pos[i] = (pos[i] + turns[i]) % len(faces[i])

ans1 = " ".join(faces[i][pos[i]] for i in range(n))

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q16_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

n, turns, faces = load_machine(data)

pos = [0] * n
c = 0
res = {0: 0}
while True:
    c += 1
    cnt = Counter()
    for i in range(n):
        pos[i] = (pos[i] + turns[i]) % len(faces[i])
        cnt[faces[i][pos[i]][0]] += 1
        cnt[faces[i][pos[i]][2]] += 1
    res[c] = res[c - 1] + sum(v - 2 for v in cnt.values() if v >= 3)
    if all(pos[i] == 0 for i in range(n)):
        break

q, r = divmod(202420242024, c)
ans2 = q * res[c] + res[r]

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q16_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

n, turns, faces = load_machine(data)

dp = {(0,) * n: (0, 0)}
for _ in range(256):
    dp_new = {}
    for pos_before, (mn, mx) in dp.items():
        for delta in [-1, 0, +1]:
            pos = [0] * n
            cnt = Counter()
            for i in range(n):
                pos[i] = (pos_before[i] + delta + turns[i]) % len(faces[i])
                cnt[faces[i][pos[i]][0]] += 1
                cnt[faces[i][pos[i]][2]] += 1
            res = sum(v - 2 for v in cnt.values() if v >= 3)
            pos = tuple(pos)
            if pos in dp_new:
                mn_best, mx_best = dp_new[pos]
                dp_new[pos] = (min(mn_best, mn + res), max(mx_best, mx + res))
            else:
                dp_new[pos] = (mn + res, mx + res)
    dp = dp_new

mn = min(v[0] for v in dp.values())
mx = max(v[1] for v in dp.values())
ans3 = f"{mx} {mn}"

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
