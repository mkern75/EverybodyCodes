from time import time

# ********************************* part 1
time_start = time()
INPUT_FILE = "./TheEntertainmentHub/data/q02_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

balloons = list(data[0])
n_balloons = len(balloons)
bolts = "RGB"
n_bolts = 0
i = 0

while i < n_balloons:
    bolt = bolts[n_bolts % 3]
    n_bolts += 1
    while i < n_balloons and balloons[i] == bolt:
        i += 1
    i += 1

ans1 = n_bolts
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./TheEntertainmentHub/data/q02_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

repeats = 100
balloons = list(data[0]) * repeats
n_balloons = len(balloons)
popped = [False] * n_balloons

bolts = "RGB"
n_bolts = 0
i = 0

while n_balloons > 0:
    bolt = bolts[n_bolts % 3]
    n_bolts += 1
    while popped[i]:
        i += 1
    if balloons[i] == bolt and n_balloons & 1 == 0:
        popped[i] = True
        popped[-n_balloons // 2] = True
        n_balloons -= 2
    else:
        popped[i] = True
        n_balloons -= 1

ans2 = n_bolts
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./TheEntertainmentHub/data/q02_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

repeats = 100_000
balloon_seq = list(data[0])
n_balloons_seq = len(balloon_seq)
n_balloons = n_balloons_seq * repeats
popped = [False] * n_balloons

bolts = "RGB"
n_bolts = 0
i = 0

while n_balloons > 0:
    bolt = bolts[n_bolts % 3]
    n_bolts += 1
    while popped[i]:
        i += 1
    if balloon_seq[i % n_balloons_seq] == bolt and n_balloons & 1 == 0:
        popped[i] = True
        popped[-n_balloons // 2] = True
        n_balloons -= 2
    else:
        popped[i] = True
        n_balloons -= 1

ans3 = n_bolts
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
