def multiply(matrix, vector):
    n = len(vector)
    result_vector = [0] * n
    for r in range(n):
        for c in range(n):
            result_vector[r] += matrix[r][c] * vector[c]
    return result_vector


# ********************************* part 1
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q11_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

d = {}
for line in data:
    k, v = line.split(":")
    d[k] = list(v.split(","))

cat = sorted(d.keys())
n = len(cat)

cnt = [0] * n
a = cat.index("A")
cnt[a] = 1

mult = [[0] * n for _ in range(n)]
for k, vl in d.items():
    for v in vl:
        mult[cat.index(v)][cat.index(k)] += 1

for _ in range(4):
    cnt = multiply(mult, cnt)

ans1 = sum(cnt)
print(f"part 1: {ans1}")

# ********************************* part 2
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q11_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

d = {}
for line in data:
    k, v = line.split(":")
    d[k] = list(v.split(","))

cat = sorted(d.keys())
n = len(cat)

cnt = [0] * n
z = cat.index("Z")
cnt[z] = 1

mult = [[0] * n for _ in range(n)]
for k, vl in d.items():
    for v in vl:
        mult[cat.index(v)][cat.index(k)] += 1

for _ in range(10):
    cnt = multiply(mult, cnt)

ans2 = sum(cnt)
print(f"part 2: {ans2}")

# ********************************* part 3
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q11_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

d = {}
for line in data:
    k, v = line.split(":")
    d[k] = list(v.split(","))

cat = sorted(d.keys())
n = len(cat)

mult = [[0] * n for _ in range(n)]
for k, vl in d.items():
    for v in vl:
        mult[cat.index(v)][cat.index(k)] += 1

mn = 1 << 63
mx = 0

for start in cat:
    cnt = [0] * n
    cnt[cat.index(start)] = 1
    for _ in range(20):
        cnt = multiply(mult, cnt)
    res = sum(cnt)
    mn = min(mn, res)
    mx = max(mx, res)

ans3 = mx - mn
print(f"part 3: {ans3}")

