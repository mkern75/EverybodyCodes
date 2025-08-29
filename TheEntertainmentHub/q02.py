from time import time
from collections import deque

# ********************************* part 1
time_start = time()
INPUT_FILE = "./TheEntertainmentHub/data/q02_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

balloons = deque(list(data[0]))
bolts = "RGB"
n_bolts = 0

while balloons:
    bolt = bolts[n_bolts % 3]
    n_bolts += 1
    while balloons and balloons.popleft() == bolt:
        pass

ans1 = n_bolts
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./TheEntertainmentHub/data/q02_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

repeats = 100
balloons = list(data[0]) * repeats
half = len(balloons) // 2
balloons1 = deque(balloons[:half])
balloons2 = deque(balloons[half:])
bolts = "RGB"
n_bolts = 0

while balloons1 or balloons2:
    bolt = bolts[n_bolts % 3]
    n_bolts += 1
    while len(balloons2) > len(balloons1):
        balloons1.append(balloons2.popleft())
    even = (len(balloons1) == len(balloons2))
    balloon = balloons1.popleft()
    if bolt == balloon and even:
        balloons2.popleft()

ans2 = n_bolts
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./TheEntertainmentHub/data/q02_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

repeats = 100_000
balloons = list(data[0]) * repeats
half = len(balloons) // 2
balloons1 = deque(balloons[:half])
balloons2 = deque(balloons[half:])
bolts = "RGB"
n_bolts = 0

while balloons1 or balloons2:
    bolt = bolts[n_bolts % 3]
    n_bolts += 1
    while len(balloons2) > len(balloons1):
        balloons1.append(balloons2.popleft())
    even = (len(balloons1) == len(balloons2))
    balloon = balloons1.popleft()
    if bolt == balloon and even:
        balloons2.popleft()

ans3 = n_bolts
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
