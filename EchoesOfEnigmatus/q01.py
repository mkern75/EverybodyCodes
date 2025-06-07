from time import time
import re


def nums(line):
    return list(map(int, re.findall(r"[-+]?\d+", line)))


# ********************************* part 1
time_start = time()
INPUT_FILE = "./EchoesOfEnigmatus/data/q01_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]


def eni(n, exp, mod):
    x, a = 1, []
    for _ in range(exp):
        x = x * n % mod
        a.append(x)
    return int("".join(map(str, reversed(a))))


ans1 = 0
for row in data:
    a, b, c, x, y, z, m = nums(row)
    ans1 = max(ans1, eni(a, x, m) + eni(b, y, m) + eni(c, z, m))
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./EchoesOfEnigmatus/data/q01_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]


def eni2(n, exp, mod):
    if exp <= 5:
        return eni(n, exp, mod)
    x, a = pow(n, exp - 5, mod), []
    for _ in range(5):
        x = x * n % mod
        a.append(x)
    return int("".join(map(str, reversed(a))))


ans2 = 0
for row in data:
    a, b, c, x, y, z, m = nums(row)
    ans2 = max(ans2, eni2(a, x, m) + eni2(b, y, m) + eni2(c, z, m))
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./EchoesOfEnigmatus/data/q01_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]


def eni3(n, exp, mod):
    x, a, idx = 1, [], [-1] * mod
    for i in range(exp):
        x = x * n % mod
        if idx[x] != -1:
            i = idx[x]
            q, r = divmod(exp - i, len(a) - i)
            return sum(a[:i]) + q * sum(a[i:]) + sum(a[i:i + r])
        idx[x] = i
        a.append(x)
    return sum(a)


ans3 = 0
for row in data:
    a, b, c, x, y, z, m = nums(row)
    ans3 = max(ans3, eni3(a, x, m) + eni3(b, y, m) + eni3(c, z, m))
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
