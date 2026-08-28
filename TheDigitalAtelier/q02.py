from time import time
import re


def nums(line):
    return list(map(int, re.findall(r"[-+]?\d+", line)))


def sky_squares(data):
    x, y = nums(data[0])
    ax, ay = nums(data[1])
    bx, by = nums(data[2])
    cx, cy = nums(data[3])
    moves = data[4]

    visited = {(x, y)}
    for move in moves:
        if move == "A":
            x += (ax - x) // 2
            y += (ay - y) // 2
        elif move == "B":
            x += (bx - x) // 2
            y += (by - y) // 2
        elif move == "C":
            x += (cx - x) // 2
            y += (cy - y) // 2
        visited.add((x, y))
    return visited


def fireflies(squares):
    res = set()
    for x, y in squares:
        res.add((x - 1, y))
        res.add((x + 1, y))
        res.add((x, y - 1))
        res.add((x, y + 1))
    res.difference_update(squares)
    return res


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q02_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

squares = sky_squares(data)
ans1 = len(squares)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q02_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

squares = sky_squares(data)
flies = fireflies(squares)
ans2 = len(flies)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q02_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

x, y = nums(data[0])
ax, ay = nums(data[1])
bx, by = nums(data[2])
cx, cy = nums(data[3])

squares = {(x, y)}
todo = [(x, y)]
for x, y in todo:
    for mx, my in [(ax, ay), (bx, by), (cx, cy)]:
        xn = x + (mx - x) // 2
        yn = y + (my - y) // 2
        if (xn, yn) not in squares:
            squares.add((xn, yn))
            todo.append((xn, yn))

flies = fireflies(squares)
ans3 = len(flies)
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
