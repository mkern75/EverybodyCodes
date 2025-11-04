from time import time

# ********************************* part 1
time_start = time()
INPUT_FILE = "./TheSongOfDucksAndDragons2025/data/q01_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

names = data[0].split(",")
k = len(names)
instr = [-int(s[1:]) if s[0] == "L" else int(s[1:]) for s in data[2].split(",")]

idx = 0
for i in instr:
    idx = min(max(idx + i, 0), k - 1)
ans1 = names[idx]
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./TheSongOfDucksAndDragons2025/data/q01_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

names = data[0].split(",")
k = len(names)
instr = [-int(s[1:]) if s[0] == "L" else int(s[1:]) for s in data[2].split(",")]

idx = 0
for i in instr:
    idx = (idx + i) % k
ans2 = names[idx]
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./TheSongOfDucksAndDragons2025/data/q01_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

names = data[0].split(",")
k = len(names)
instr = [-int(s[1:]) if s[0] == "L" else int(s[1:]) for s in data[2].split(",")]

for i in instr:
    i = i % k
    names[0], names[i] = names[i], names[0]
ans3 = names[0]
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
