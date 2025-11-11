from time import time
from collections import defaultdict

# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q06_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans1 = 0
s = data[0]
mentors = 0
for c in s:
    if c == "A":
        mentors += 1
    elif c == "a":
        ans1 += mentors
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q06_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans2 = 0
s = data[0]
mentors = defaultdict(int)
for c in s:
    if c.isupper():
        mentors[c] += 1
    elif c.islower():
        ans2 += mentors[c.upper()]
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q06_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans3 = 0
repeats = 1000
limit = 1000
s = data[0]
k = len(s)
f = (limit + k - 1) // k
n = k * min(repeats, 2 * f + 1)

mentors = defaultdict(int)

# initialise sliding window
for i in range(min(limit + 1, n)):
    if s[i % k].isupper():
        mentors[s[i % k]] += 1

for i in range(n):
    if s[i % k].islower():
        if i < k * f or i >= n - k * f:
            ans3 += mentors[s[i % k].upper()]
        else:
            ans3 += (repeats - 2 * f) * mentors[s[i % k].upper()]
    # update sliding window
    j = i - limit
    if j >= 0 and s[j % k].isupper():
        mentors[s[j % k]] -= 1
    j = i + limit + 1
    if j < n and s[j % k].isupper():
        mentors[s[j % k]] += 1

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
