# ********************************* part 1
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q08_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

w = h = 1
remaining = int(data[0]) - 1

while remaining > 0:
    h += 1
    w += 2
    remaining -= 2 * h - 1

ans1 = w * abs(remaining)
print(f"part 1: {ans1}")

# ********************************* part 2
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q08_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

w = h = t = 1
multiplier = int(data[0])
mod = 1111
remaining = 20240000 - 1

while remaining > 0:
    t = (t * multiplier) % mod
    h += t
    w += 2
    remaining -= w * t

ans2 = w * abs(remaining)
print(f"part 2: {ans2}")

# ********************************* part 3
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q08_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
ans3 = 0

t = 1
col = [1]
multiplier = int(data[0])
mod = 10
blocks = 202400000
remaining = blocks - 1

while remaining > 0:
    t = (t * multiplier) % mod + mod
    for i in range(len(col)):
        col[i] += t
    col += [t]
    remaining = blocks - (2 * sum(col) - col[0])

    w = len(col) * 2 - 1
    for i in range(len(col) - 2, 0, -1):
        remaining += (2 * w * col[i]) % mod * 2
    remaining += (2 * w * col[0]) % mod

ans3 = abs(remaining)
print(f"part 3: {ans3}")

