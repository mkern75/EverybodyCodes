from time import time


# ********************************* part 1

def check(name, rules):
    for i in range(len(name) - 1):
        if name[i] not in rules or name[i + 1] not in rules[name[i]]:
            return False
    return True


time_start = time()
INPUT_FILE = "./data/q07_p1.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

names = list(blocks[0][0].split(","))
rules = {}
for line in blocks[1]:
    left, right = line.split(" > ")
    rules[left] = set(right.split(","))

ans1 = next((name for name in names if check(name, rules)), "")
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q07_p2.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

names = list(blocks[0][0].split(","))
rules = {}
for line in blocks[1]:
    left, right = line.split(" > ")
    rules[left] = set(right.split(","))

ans2 = sum(idx for idx, name in enumerate(names, start=1) if check(name, rules))
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q07_p3.txt"
# INPUT_FILE = "./data/q07_p3_test.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

names = list(blocks[0][0].split(","))
rules = {}
for line in blocks[1]:
    left, right = line.split(" > ")
    rules[left] = set(right.split(","))

names = sorted(name for name in names if check(name, rules))
tmp = []
for i in range(len(names)):
    if i == 0 or not names[i].startswith(names[i - 1]):
        tmp.append(names[i])
names = tmp

ans3 = 0
for name in names:
    bfs = [(name[-1], len(name))]
    for last_char, len_name in bfs:
        if 7 <= len_name <= 11:
            ans3 += 1
        if len_name < 11 and last_char in rules:
            for last_char_new in rules[last_char]:
                bfs.append((last_char_new, len_name + 1))
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
