from time import time

import re


def nums(line):
    return list(map(int, re.findall(r"[-+]?\d+", line)))


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q01_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]


def calc1(jumps):
    x = 0
    visited = {x}
    for jump in jumps:
        if x - jump >= 0 and x - jump not in visited:
            x -= jump
        else:
            x += jump
        visited.add(x)
    return x


ans1 = sum(calc1(nums(line)) for line in data)

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q01_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]


def calc2(jumps):
    x = 0
    visited = {x}
    for jump in jumps:
        if x - jump >= 0 and x - jump not in visited:
            x -= jump
        else:
            while x + jump in visited:
                jump += 1
            x += jump
        visited.add(x)
    return x


ans2 = sum(calc2(nums(line)) for line in data)

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q01_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]


def is_crossing(l1, r1, l2, r2):
    if l1 <= l2 and r2 <= r1:
        return False
    if l2 <= l1 and r1 <= r2:
        return False
    if r1 <= l2:
        return False
    if r2 <= l1:
        return False
    return True


def check(l, r, arcs):
    for l2, r2 in arcs:
        if is_crossing(l, r, l2, r2):
            return False
    return True


def calc3(jumps):
    x = 0
    visited = {x}
    arcs = [[], []]
    mx = [0, 0]
    f = 0
    for jump in jumps:
        if x - jump >= 0 and x - jump not in visited:
            if check(x - jump, x, arcs[f]):
                visited.add(x - jump)
                arcs[f].append((x - jump, x))
                mx[f] = max(mx[f], x)
                x -= jump
                f = 1 - f
                continue

        skip = False
        while x + jump in visited or not check(x, x + jump, arcs[f]):
            jump += 1
            if jump > mx[f] + 1:
                skip = True
                break
        if not skip:
            visited.add(x + jump)
            arcs[f].append((x, x + jump))
            mx[f] = max(mx[f], x + jump)
            x += jump
            f = 1 - f

    return x


ans3 = sum(calc3(nums(line)) for line in data)

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
