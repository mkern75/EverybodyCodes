from time import time
import re


def parse(data):
    return [tuple(map(int, re.findall(r"-?\d+", line))) for line in data]


def solve(vals, use_width=False):
    res = 0
    n = len(vals)
    l, r = 0, n - 1
    y_prev = 0
    while True:
        y_curr = min(vals[l][1], vals[r][1])
        res += (vals[r][0] + (vals[r][2] if use_width else 1) - vals[l][0]) * (y_curr - y_prev)
        if vals[l][1] == y_curr:
            while l < n and vals[l][1] <= y_curr:
                l += 1
        if vals[r][1] == y_curr:
            while r >= 0 and vals[r][1] <= y_curr:
                r -= 1
        if l > r:
            break
        y_prev = y_curr
    return res


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q18_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans1 = solve(parse(data))

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q18_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans2 = solve(parse(data), True)

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q18_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans3 = solve(parse(data), True)

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
