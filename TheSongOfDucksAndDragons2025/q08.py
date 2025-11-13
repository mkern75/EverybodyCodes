from time import time

# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q08_p1.txt"
# INPUT_FILE = "./data/q08_p1_test.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans1 = 0
nails = 32
nums = list(map(int, data[0].split(",")))
for x, y in zip(nums, nums[1:]):
    x, y = min(x, y), max(x, y)
    if nails & 1 == 0 and y - x == nails // 2:
        ans1 += 1
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q08_p2.txt"
# INPUT_FILE = "./data/q08_p2_test.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans2 = 0
nails = 256
nums = list(map(int, data[0].split(",")))
segm = []
for x, y in zip(nums, nums[1:]):
    x, y = min(x, y), max(x, y)
    for x1, y1 in segm:
        if x < x1 < y < y1 or x1 < x < y1 < y:
            ans2 += 1
    segm.append((x, y))
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q08_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans3 = 0
nails = 256
nums = list(map(int, data[0].split(",")))
segm = [(min(x, y), max(x, y)) for x, y in zip(nums, nums[1:])]
for x in range(1, nails):
    for y in range(x + 1, nails + 1):
        res = 0
        for x1, y1 in segm:
            if x < x1 < y < y1 or x1 < x < y1 < y or (x == x1 and y == y1):
                res += 1
        ans3 = max(ans3, res)
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
