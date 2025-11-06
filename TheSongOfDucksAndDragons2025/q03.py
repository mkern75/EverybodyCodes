from time import time
from collections import Counter

# ********************************* part 1
time_start = time()
INPUT_FILE = "./TheSongOfDucksAndDragons2025/data/q03_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

nums = list(map(int, data[0].split(",")))
ans1 = sum(set(nums))
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./TheSongOfDucksAndDragons2025/data/q03_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

nums = list(map(int, data[0].split(",")))
ans2 = sum(sorted(set(nums))[:20])
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./TheSongOfDucksAndDragons2025/data/q03_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

nums = list(map(int, data[0].split(",")))
cnt = Counter(nums)
ans3 = cnt.most_common(1)[0][1]
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
