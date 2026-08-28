from time import time


def check_horizontal(r, c, horizontal_offset):
    return horizontal_offset[r % (len(horizontal_offset))] == c & 1


def check_vertical(r, c, vertical_offset):
    return vertical_offset[c % (len(vertical_offset))] == r & 1


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q03_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

width = int(data[0].split("=")[1])
height = int(data[1].split("=")[1])
horizontal_offset = list(map(int, list(data[2].split("=")[1])))
vertical_offset = list(map(int, list(data[3].split("=")[1])))

ans1 = 0
for r in range(height):
    for c in range(width):
        stiches = 0
        stiches += check_horizontal(r, c, horizontal_offset)
        stiches += check_horizontal(r + 1, c, horizontal_offset)
        stiches += check_vertical(r, c, vertical_offset)
        stiches += check_vertical(r, c + 1, vertical_offset)
        if stiches == 4:
            ans1 += 1

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q03_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

width = int(data[0].split("=")[1])
height = int(data[1].split("=")[1])
horizontal_offset = list(map(int, list(data[2].split("=")[1])))
vertical_offset = list(map(int, list(data[3].split("=")[1])))

colour = [[0] * width for _ in range(height)]
for r in range(height):
    if r > 0:
        if check_horizontal(r, 0, horizontal_offset):
            colour[r][0] = 1 - colour[r - 1][0]
        else:
            colour[r][0] = colour[r - 1][0]
    for c in range(1, width):
        if check_vertical(r, c, vertical_offset):
            colour[r][c] = 1 - colour[r][c - 1]
        else:
            colour[r][c] = colour[r][c - 1]

cnt = [0] * 2
for r in range(height):
    for c in range(width):
        stiches = 0
        stiches += check_horizontal(r, c, horizontal_offset)
        stiches += check_horizontal(r + 1, c, horizontal_offset)
        stiches += check_vertical(r, c, vertical_offset)
        stiches += check_vertical(r, c + 1, vertical_offset)
        if stiches == 4:
            cnt[colour[r][c]] += 1
ans2 = max(cnt)

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q03_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

width = int(data[0].split("=")[1])
height = int(data[1].split("=")[1])
horizontal_offset = list(map(int, list(data[2].split("=")[1])))
vertical_offset = list(map(int, list(data[3].split("=")[1])))

h = 2 * len(horizontal_offset)
w = 2 * len(vertical_offset)

colour = [[0] * w for _ in range(h)]
for r in range(h):
    if r > 0:
        if check_horizontal(r, 0, horizontal_offset):
            colour[r][0] = 1 - colour[r - 1][0]
        else:
            colour[r][0] = colour[r - 1][0]
    for c in range(1, w):
        if check_vertical(r, c, vertical_offset):
            colour[r][c] = 1 - colour[r][c - 1]
        else:
            colour[r][c] = colour[r][c - 1]

# full segments from top left
multiplier1 = (height // h) * (width // w)
cnt1 = [0] * 2
for r in range(h):
    for c in range(w):
        stiches = 0
        stiches += check_horizontal(r, c, horizontal_offset)
        stiches += check_horizontal(r + 1, c, horizontal_offset)
        stiches += check_vertical(r, c, vertical_offset)
        stiches += check_vertical(r, c + 1, vertical_offset)
        if stiches == 4:
            cnt1[colour[r][c]] += 1

# partial segments on the right
multiplier2 = height // h
cnt2 = [0] * 2
for r in range(h):
    for c in range(width % w):
        stiches = 0
        stiches += check_horizontal(r, c, horizontal_offset)
        stiches += check_horizontal(r + 1, c, horizontal_offset)
        stiches += check_vertical(r, c, vertical_offset)
        stiches += check_vertical(r, c + 1, vertical_offset)
        if stiches == 4:
            cnt2[colour[r][c]] += 1

# partial segments at the bottom
multiplier3 = width // w
cnt3 = [0] * 2
for r in range(height % h):
    for c in range(w):
        stiches = 0
        stiches += check_horizontal(r, c, horizontal_offset)
        stiches += check_horizontal(r + 1, c, horizontal_offset)
        stiches += check_vertical(r, c, vertical_offset)
        stiches += check_vertical(r, c + 1, vertical_offset)
        if stiches == 4:
            cnt3[colour[r][c]] += 1

# partial segment at the bottom right
cnt4 = [0] * 2
for r in range(height % h):
    for c in range(width % w):
        stiches = 0
        stiches += check_horizontal(r, c, horizontal_offset)
        stiches += check_horizontal(r + 1, c, horizontal_offset)
        stiches += check_vertical(r, c, vertical_offset)
        stiches += check_vertical(r, c + 1, vertical_offset)
        if stiches == 4:
            cnt4[colour[r][c]] += 1

ans3 = max(cnt1[i] * multiplier1 + cnt2[i] * multiplier2 + cnt3[i] * multiplier3 + cnt4[i] for i in range(2))

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
