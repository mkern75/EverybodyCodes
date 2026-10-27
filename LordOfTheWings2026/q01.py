from time import time
import re


def nums(s: str) -> list[int]:
    return list(map(int, re.findall(r"-?\d+", s)))


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q01_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
a = nums(data[0])

b = [r ** 2 for r in range(1, 10_001)]
ans1 = sum(next(y - x for y in b if y >= x) for x in a)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q01_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
a = nums(data[0])

b = [(r + 2) ** 2 - r ** 2 for r in range(1, 10_001)]
ans2 = sum(next(y - x for y in b if y >= x) for x in a)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q01_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
a = nums(data[0])

b = [r ** 2 - 1 for r in range(3, 10_001, 2)]
ans3 = sum(next(y - x for y in b if y >= x) for x in a)
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
