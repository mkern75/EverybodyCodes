# ********************************* part 1
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q04_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
ans1 = 0

a = list(int(row) for row in data)
n = len(a)
mn = 1 << 31
sm = 0
for x in a:
    mn = min(mn, x)
    sm += x

ans1 = sm - n * mn
print(f"part 1: {ans1}")

# ********************************* part 2
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q04_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
ans2 = 0

a = list(int(row) for row in data)
n = len(a)
mn = 1 << 31
sm = 0
for x in a:
    mn = min(mn, x)
    sm += x

ans2 = sm - n * mn
print(f"part 2: {ans2}")

# ********************************* part 3
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q04_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
ans3 = 0

a = sorted(int(row) for row in data)
n = len(a)
mid = a[n // 2]

for x in a:
    ans3 += abs(x - mid)
print(f"part 3: {ans3}")

