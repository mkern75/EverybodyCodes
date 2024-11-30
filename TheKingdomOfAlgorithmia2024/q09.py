from time import time

# ********************************* part 1
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q09_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

nums = [int(x) for x in data]
mx = max(nums)

c = [1, 3, 5, 10]
dp = [mx] * (mx + 1)
dp[0] = 0
for i in range(1, mx + 1):
    for x in c:
        if i - x >= 0:
            dp[i] = min(dp[i], dp[i - x] + 1)

ans1 = sum(dp[i] for i in nums)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q09_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
nums = [int(x) for x in data]
mx = max(nums)

c = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]
dp = [mx] * (mx + 1)
dp[0] = 0
for i in range(1, mx + 1):
    for x in c:
        if i - x >= 0:
            dp[i] = min(dp[i], dp[i - x] + 1)

ans2 = sum(dp[i] for i in nums)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q09_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

nums = [int(x) for x in data]
mx = max(nums)

c = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]
dp = [mx] * (mx + 1)
dp[0] = 0
for i in range(1, mx + 1):
    for x in c:
        if i - x >= 0:
            dp[i] = min(dp[i], dp[i - x] + 1)

ans3 = 0
for i in nums:
    best = mx
    h = i // 2
    for lo in range(h - 51, h + 1):
        hi = i - lo
        if hi - lo <= 100:
            best = min(best, dp[lo] + dp[hi])
    ans3 += best

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")

