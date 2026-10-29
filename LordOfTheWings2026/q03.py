from time import time

# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q03_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]


def calc(a: str, b: str) -> int:
    res = 0
    ka = len(a)
    kb = len(b)
    for i in range(kb):
        x = int(a[(ka - 1 - i) % ka])
        y = int(b[kb - 1 - i])
        e = i
        res += y * x ** e
    return res


ans1 = 0
for line in data:
    a, b = line.split()
    a = a[a.index("-") + 1:]
    ans1 += calc(a, b)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q03_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans2 = 0
for line in data:
    a, b = line.split()
    a = a[a.index("-") + 1:]
    ans2 += calc(a, b)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q03_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]


def valid(a, b):
    v = calc(a, b)
    for i in range(int(b)):
        if calc(a, str(i)) == v:
            return False
    return True


ans3 = 0
for line in data:
    a, b = line.split()
    a = a[a.index("-") + 1:]
    if valid(a, b):
        ans3 += calc(a, b)
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
