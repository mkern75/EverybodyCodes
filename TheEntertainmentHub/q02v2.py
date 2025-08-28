from time import time

# ********************************* part 1
time_start = time()
INPUT_FILE = "./TheEntertainmentHub/data/q02_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ballons = list(data[0])
n_ballons = len(ballons)
bolts = "RGB"
n_bolts = 0
i = 0

while i < n_ballons:
    bolt = bolts[n_bolts % 3]
    n_bolts += 1
    while i < n_ballons and ballons[i] == bolt:
        i += 1
    i += 1

ans1 = n_bolts
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./TheEntertainmentHub/data/q02_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

repeats = 100
ballons = list(data[0]) * repeats
n_ballons = len(ballons)
popped = [False] * n_ballons

bolts = "RGB"
n_bolts = 0
i = 0

while n_ballons > 0:
    bolt = bolts[n_bolts % 3]
    n_bolts += 1
    while popped[i]:
        i += 1
    if ballons[i] == bolt and n_ballons & 1 == 0:
        popped[i] = True
        popped[-n_ballons // 2] = True
        n_ballons -= 2
    else:
        popped[i] = True
        n_ballons -= 1

ans2 = n_bolts
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./TheEntertainmentHub/data/q02_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

repeats = 100_000
ballons = list(data[0]) * repeats
n_ballons = len(ballons)
popped = [False] * n_ballons

bolts = "RGB"
n_bolts = 0
i = 0

while n_ballons > 0:
    bolt = bolts[n_bolts % 3]
    n_bolts += 1
    while popped[i]:
        i += 1
    if ballons[i] == bolt and n_ballons & 1 == 0:
        popped[i] = True
        popped[-n_ballons // 2] = True
        n_ballons -= 2
    else:
        popped[i] = True
        n_ballons -= 1

ans3 = n_bolts
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
