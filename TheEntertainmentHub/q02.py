from time import time
from collections import deque

# ********************************* part 1
time_start = time()
INPUT_FILE = "./TheEntertainmentHub/data/q02_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ballons = deque(list(data[0]))
bolts = "RGB"
n_bolts = 0

while ballons:
    bolt = bolts[n_bolts % 3]
    n_bolts += 1
    while ballons.popleft() == bolt:
        pass

ans1 = n_bolts
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./TheEntertainmentHub/data/q02_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

repeats = 100
ballons = list(data[0]) * repeats
half = len(ballons) // 2
ballons1 = deque(ballons[:half])
ballons2 = deque(ballons[half:])
bolts = "RGB"
n_bolts = 0

while ballons1 or ballons2:
    bolt = bolts[n_bolts % 3]
    n_bolts += 1
    while len(ballons2) > len(ballons1):
        ballons1.append(ballons2.popleft())
    even = (len(ballons1) == len(ballons2))
    ballon = ballons1.popleft()
    if bolt == ballon and even:
        ballons2.popleft()

ans2 = n_bolts
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./TheEntertainmentHub/data/q02_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

repeats = 100_000
ballons = list(data[0]) * repeats
half = len(ballons) // 2
ballons1 = deque(ballons[:half])
ballons2 = deque(ballons[half:])
bolts = "RGB"
n_bolts = 0

while ballons1 or ballons2:
    bolt = bolts[n_bolts % 3]
    n_bolts += 1
    while len(ballons2) > len(ballons1):
        ballons1.append(ballons2.popleft())
    even = (len(ballons1) == len(ballons2))
    ballon = ballons1.popleft()
    if bolt == ballon and even:
        ballons2.popleft()

ans3 = n_bolts
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
