from time import time
from math import trunc, ceil, prod

# ********************************* part 1
time_start = time()
INPUT_FILE = "./TheSongOfDucksAndDragons2025/data/q04_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

rotations = 2025
gears = list(map(int, data))
ans1 = trunc(rotations * gears[0] / gears[-1])
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./TheSongOfDucksAndDragons2025/data/q04_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

target = 10000000000000
gears = list(map(int, data))
ans2 = ceil(target * gears[-1] / gears[0])
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./TheSongOfDucksAndDragons2025/data/q04_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

rotations = 100
first_gear, last_gear = int(data[0]), int(data[-1])
gear_pairs = [tuple(map(int, line.split("|"))) for line in data[1:-1]]
ans3 = trunc(rotations * first_gear / last_gear * prod(x[1] / x[0] for x in gear_pairs))
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
