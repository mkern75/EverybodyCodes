from time import time
from collections import defaultdict, deque


def segment(s: str):
    seg = []
    for i, char in enumerate(s):
        if i == 0 or char != s[i - 1]:
            seg.append([char, 1])
        else:
            seg[-1][-1] += 1
    return seg


def merge(seg):
    res = []
    for i, (char, cnt) in enumerate(seg):
        if i == 0 or char != res[-1][0]:
            res.append([char, cnt])
        else:
            res[-1][1] += cnt
    return res


def scan(seg):
    d = defaultdict(list)
    for i, (char, cnt) in enumerate(seg):
        d[char].append((i, cnt))
    for char, cnt in seg:
        if len(d[char]) > 1:
            i = d[char][0][0]
            j = d[char][-1][0]
            seg_new = merge(seg[:i + 1] + list(reversed(seg[i + 1:j + 1])) + seg[j + 1:])
            flips = sum(seg[k][1] for k in range(i + 1, j + 1))
            return flips, seg_new
    return 0, seg


def scan_fast(s):
    d = defaultdict(list)
    for i, (char, sz) in enumerate(s):
        d[char].append((i, sz))
    for char, _ in s:
        if len(d[char]) > 1:
            flips = 0
            left = d[char][0][0] + 1
            seg_left = s[:left]
            right = d[char][-1][0]
            seg_right = deque(s[right + 1:])
            current = sum(s[i][1] for i in range(left, right + 1))

            while left <= right:

                assert s[right][0] == char
                flips += current
                current -= s[right][1]
                seg_left.append(s[right])
                right -= 1
                while s[left][0] != char:
                    current -= s[left][1]
                    seg_right.appendleft(s[left])
                    left += 1

                if left > right:
                    break

                assert s[left][0] == char
                flips += current
                current -= s[left][1]
                seg_left.append(s[left])
                left += 1
                while s[right][0] != char:
                    current -= s[right][1]
                    seg_right.appendleft(s[right])
                    right -= 1

            return flips, merge(seg_left + list(seg_right))

    return 0, s


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q16_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans1 = 0
shelf = segment(data[0])
while True:
    flips, shelf = scan(shelf)
    if not flips:
        break
    ans1 += 1

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q16_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans2 = 0
shelf = segment(data[0] * 10)
while True:
    flips, shelf = scan_fast(shelf)
    if not flips:
        break
    ans2 += flips

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q16_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans3 = 0
shelf = segment(data[0] * 100)
while True:
    flips, shelf = scan_fast(shelf)
    if not flips:
        break
    ans3 += flips

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
