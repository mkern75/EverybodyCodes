from time import time
from collections import defaultdict

N_SEGMENTS = {"0": 6, "1": 2, "2": 5, "3": 5, "4": 4, "5": 5, "6": 6, "7": 3, "8": 7, "9": 6, "+": 2, "-": 1, "=": 2,
              "A": 6, " ": 0}

PLUS_MINUS = defaultdict(list, {
    "0": ["6", "9", "A"],
    "2": ["3"],
    "3": ["2", "5"],
    "5": ["3"],
    "6": ["0", "9", "A"],
    "9": ["0", "3", "6", "A"],
    "A": ["0", "6", "9"], })

MINUS = defaultdict(list, {
    "6": ["5"],
    "7": ["1"],
    "8": ["0", "6", "9", "A"],
    "9": ["3", "5"],
    "+": ["-"], })

PLUS = defaultdict(list, {
    "0": ["8"],
    "1": ["7"],
    "3": ["9"],
    "5": ["6", "9"],
    "6": ["8"],
    "9": ["8"],
    "A": ["8"],
    "-": ["+"], })


def count_segments(s):
    return sum(N_SEGMENTS[c] for c in s)


def base11(n):
    res = []
    while n:
        n, d = divmod(n, 11)
        res.append("A" if d == 10 else str(d))
    return "".join(res)[::-1]


def calc(num1, op, num2, base):
    if op == "+":
        return int(num1, base) + int(num2, base)
    elif op == "-":
        return int(num1, base) - int(num2, base)
    else:
        assert False


def check(s, base=10):
    p = s.split(" ")
    return calc(*p[:3], base) == calc(*p[4:7], base)


def test_all(s):
    base = 11
    if check(s, base):
        return True
    s = list(s)
    for i in range(len(s)):
        if PLUS_MINUS[s[i]]:
            ss = s[:]
            for other in PLUS_MINUS[s[i]]:
                ss[i] = other
                if check("".join(ss), base):
                    return True
    for i in range(len(s)):
        if not MINUS[s[i]]:
            continue
        for j in range(len(s)):
            if j == i or not PLUS[s[j]]:
                continue
            for c1 in MINUS[s[i]]:
                for c2 in PLUS[s[j]]:
                    ss = s[:]
                    ss[i] = c1
                    ss[j] = c2
                    if check("".join(ss), base):
                        return True
    return False


def solve1(data):
    res = 0
    for line in data:
        if check(line):
            res += count_segments(line)
    return res


def solve2(data):
    res = 0
    for line in data:
        if check(line, 11):
            res += count_segments(line)
    return base11(res)


def solve3(data):
    res = 0
    for line in data:
        if test_all(line):
            res += count_segments(line)
    return base11(res)


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q20_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
ans1 = solve1(data)

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q20_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans2 = solve2(data)

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q20_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans3 = solve3(data)

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
