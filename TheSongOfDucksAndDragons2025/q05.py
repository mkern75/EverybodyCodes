from time import time
from collections import namedtuple

Sword = namedtuple("sword", "id fishbone")


def load_sword(input_line: str) -> Sword:
    left, right = input_line.split(":")
    id, nums = int(left), list(map(int, right.split(",")))
    fishbone = []
    for x in nums:
        for i, (l, m, r) in enumerate(fishbone):
            if l is None and x < m:
                fishbone[i][0] = x
                break
            if r is None and m < x:
                fishbone[i][2] = x
                break
        else:
            fishbone.append([None, x, None])
    return Sword(id, fishbone)


def calc_quality(sword: Sword) -> int:
    return int("".join(map(str, [seg[1] for seg in sword.fishbone])))


def evaluate(sword: Sword) -> tuple:
    res = [calc_quality(sword)]
    res += [int("".join(map(str, [x for x in seg if x is not None]))) for seg in sword.fishbone]
    res += [sword.id]
    return tuple(res)


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q05_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

sword = load_sword(data[0])
ans1 = calc_quality(sword)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q05_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

quality = [calc_quality(load_sword(line)) for line in data]
ans2 = max(quality) - min(quality)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q05_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

evals = sorted((evaluate(load_sword(line)) for line in data), reverse=True)
ans3 = sum(ev[-1] * i for i, ev in enumerate(evals, start=1))
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
