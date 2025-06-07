from time import time
import re
from math import gcd
from typing import List


def extended_gcd(a, b):
    s, old_s = 0, 1
    r, old_r = b, a
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
    return old_r, old_s, (old_r - old_s * a) // b if b else 0


def composite_chinese_remainder(a: List[int], m: List[int]):
    x, m_prod = 0, 1
    for bi, mi in zip(a, m):
        g, s, _ = extended_gcd(m_prod, mi)
        if ((bi - x) % mi) % g:
            return None
        x += m_prod * (s * ((bi - x) % mi) // g)
        m_prod = (m_prod * mi) // gcd(m_prod, mi)
    return x % m_prod


# ********************************* part 1
time_start = time()
INPUT_FILE = "./EchoesOfEnigmatus/data/q03_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans1 = 0
days = 100
for row in data:
    x, y = map(int, re.findall(r"(\d+)", row))
    z = x + y - 1
    x += days % z
    y -= days % z
    if y < 1:
        x -= z
        y += z
    ans1 += x + 100 * y
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./EchoesOfEnigmatus/data/q03_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

a, m = [], []
for row in data:
    x, y = map(int, re.findall(r"(\d+)", row))
    a += [y - 1]
    m += [x + y - 1]
ans2 = composite_chinese_remainder(a, m)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./EchoesOfEnigmatus/data/q03_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

a, m = [], []
for row in data:
    x, y = map(int, re.findall(r"(\d+)", row))
    a += [y - 1]
    m += [x + y - 1]
ans3 = composite_chinese_remainder(a, m)
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
