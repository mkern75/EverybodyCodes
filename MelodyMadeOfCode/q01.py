from time import time


def str_to_bin(s: str) -> int:
    res, b = 0, 1
    for c in reversed(s):
        if c.isupper():
            res += b
        b <<= 1
    return res


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q01_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans1 = 0
for line in data:
    id, rest = line.split(":")
    id = int(id)
    red, green, blue = map(str_to_bin, rest.split(" "))
    if green > max(red, blue):
        ans1 += id

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q01_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans2 = 0
highest_shine, lowest_colour_sum = -1, 0
for line in data:
    id, rest = line.split(":")
    id = int(id)
    red, green, blue, shine = map(str_to_bin, rest.split(" "))
    colour_sum = red + green + blue
    if (shine > highest_shine) or (shine == highest_shine and colour_sum < lowest_colour_sum):
        ans2 = id
        highest_shine, lowest_colour_sum = shine, colour_sum

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q01_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

groups = [[] for _ in range(6)]
for line in data:
    id, rest = line.split(":")
    id = int(id)
    red, green, blue, shine = map(str_to_bin, rest.split(" "))

    c = -1
    if red > max(green, blue):
        c = 0
    elif green > max(red, blue):
        c = 1
    elif blue > max(red, green):
        c = 2

    s = -1
    if shine <= 30:
        s = 0
    elif shine >= 33:
        s = 1

    if c != -1 and s != -1:
        groups[c * 2 + s].append(id)

ans3 = 0
max_size = 0
for group in groups:
    if len(group) > max_size:
        max_size = len(group)
        ans3 = sum(group)

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
