from time import time

# ********************************* part 1
time_start = time()

INPUT_FILE = "./data/q13_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

turns = 2025
wheel = [1] + [0] * len(data)
for i, line in enumerate(data):
    x = int(line)
    
    if i & 1:
        wheel[-(i // 2 + 1)] = x
    else:
        wheel[1 + (i // 2)] = x

ans1 = wheel[turns % len(wheel)]
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()


def load_wheel_ranges(data):
    k = len(data)
    wheel = [(1, 1)] + [(0, 0)] * k
    for i, line in enumerate(data):
        a, b = map(int, line.split("-"))
        if i & 1:
            wheel[-(i // 2 + 1)] = (b, a)
        else:
            wheel[1 + (i // 2)] = (a, b)
    return wheel


def turn_wheel(turns, wheel):
    cnt = sum(max(a, b) - min(a, b) + 1 for a, b in wheel)
    turns %= cnt
    i = 0
    while True:
        a, b = wheel[i]
        if a <= b:
            c = b - a + 1
            if turns < c:
                return a + turns
            turns -= c
        else:
            c = a - b + 1
            if turns < c:
                return a - turns
            turns -= c
        i += 1


INPUT_FILE = "./data/q13_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

turns = 20252025
wheel = load_wheel_ranges(data)
ans2 = turn_wheel(turns, wheel)

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q13_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

turns = 202520252025
wheel = load_wheel_ranges(data)
ans3 = turn_wheel(turns, wheel)

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
