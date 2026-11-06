from time import time
import re
from collections import Counter


def parse(line):
    _, growth, limit = map(int, re.findall(r"-?\d+", line))
    return growth, limit


def simulate1(growth, limit):
    time = 1
    branches = Counter({1: 1})
    branching_points = 0
    while branching_points + sum(sz * cnt for sz, cnt in branches.items()) < limit:
        time += 1
        branches_new = Counter()
        for sz, cnt in branches.items():
            if sz + 1 < growth:
                branches_new[sz + 1] += cnt
            else:
                branches_new[growth // 2] += 2 * cnt
                branches_new[1] += cnt
                branching_points += cnt
        branches = branches_new
    return time


def simulate2(growth, limit):
    time = 1
    branches = Counter({1: 1})
    branching_points = 0
    while branching_points + 1 < limit:
        step = growth - max(branches.keys())
        time += step
        branches_new = Counter()
        for sz, cnt in branches.items():
            if sz + step < growth:
                branches_new[sz + step] += cnt
            else:
                branches_new[growth // 2] += 2 * cnt
                branches_new[1] += cnt
                branching_points += cnt
        branches = branches_new
    return time


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q09_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans1 = sum(simulate1(*parse(line)) for line in data)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q09_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans2 = sum(simulate2(*parse(line)) for line in data)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q09_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans3 = sum(simulate2(*parse(line)) for line in data)
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
