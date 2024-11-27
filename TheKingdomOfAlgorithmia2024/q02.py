# ********************************* part 1
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q02_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

words = list(data[0][6:].split(","))
message = data[2]
ans1 = 0
for i in range(len(message)):
    for word in words:
        if message[i:].startswith(word):
            ans1 += 1

print(f"part 1: {ans1}")

# ********************************* part 2
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q02_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

words = list(data[0][6:].split(","))
ans2 = 0
for line in data[2:]:
    s = line
    k = len(s)
    cnt = [0] * k
    for _ in range(2):
        for i in range(k):
            for word in words:
                if s[i:].startswith(word):
                    for j in range(i, i + len(word)):
                        cnt[j] = 1
        s = s[::-1]
        cnt = cnt[::-1]
    ans2 += sum(cnt)

print(f"part 2: {ans2}")

# ********************************* part 2
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q02_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

words = list(data[0][6:].split(","))
g = data[2:]
n, m = len(g), len(g[0])

cnt = [[0] * m for _ in range(n)]
for r in range(n):
    for c in range(m):
        for word in words:
            k = len(word)
            if all(word[i] == g[r][(c + i) % m] for i in range(k)):
                for i in range(k):
                    cnt[r][(c + i) % m] = 1
            if all(word[i] == g[r][(c - i) % m] for i in range(k)):
                for i in range(k):
                    cnt[r][(c - i) % m] = 1
            if r + (k - 1) < n:
                if all(word[i] == g[r + i][c] for i in range(k)):
                    for i in range(k):
                        cnt[r + i][c] = 1
            if r - (k - 1) >= 0:
                if all(word[i] == g[r - i][c] for i in range(k)):
                    for i in range(k):
                        cnt[r - i][c] = 1

ans3 = sum(sum(row) for row in cnt)
print(f"part 3: {ans3}")

