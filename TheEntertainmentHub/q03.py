from time import time

# ********************************* part 1
time_start = time()
INPUT_FILE = "./TheEntertainmentHub/data/q03_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]


class Die:
    def __init__(self, id, faces, seed):
        self.id = id
        self.faces = faces
        self.seed = seed
        self.pulse = seed
        self.roll_number = 1
        self.face = 0

    def roll(self):
        spin = self.roll_number * self.pulse
        self.face += spin
        self.face %= len(self.faces)
        self.pulse += spin
        self.pulse %= self.seed
        self.pulse += 1 + self.roll_number + self.seed
        self.roll_number += 1
        return self.faces[self.face]

    @classmethod
    def load_from_line(cls, line):
        n, f, s = line.split(" ")
        id = int(n[:-1])
        faces = list(map(int, f[7:-1].split(",")))
        seed = int(s[5:])
        return Die(id, faces, seed)


dice = [Die.load_from_line(line) for line in data]

target = 10_000
actual = 0
rolls = 0

while actual < target:
    rolls += 1
    for die in dice:
        actual += die.roll()

ans1 = rolls
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./TheEntertainmentHub/data/q03_p2.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

dice = [Die.load_from_line(line) for line in blocks[0]]
n_dice = len(dice)

racetrack = list(map(int, list(blocks[1][0])))
pos = [0] * n_dice
finishing_order = []

while len(finishing_order) < n_dice:
    for i, die in enumerate(dice):
        if pos[i] < len(racetrack) and racetrack[pos[i]] == die.roll():
            pos[i] += 1
            if pos[i] == len(racetrack):
                finishing_order.append(i + 1)

ans2 = ",".join(map(str, finishing_order))
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./TheEntertainmentHub/data/q03_p3.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]


def ff(r, c, d, i):
    return (r << 48) | (c << 32) | (d << 16) | i


def fr(mask):
    return mask >> 48, (mask >> 32) & 0xFFFF, (mask >> 16) & 0xFFFF, mask & 0xFFFF


dice = [Die.load_from_line(line) for line in blocks[0]]
n_dice = len(dice)

grid = [list(map(int, list(line))) for line in blocks[1]]
n_rows, n_cols = len(grid), len(grid[0])
coins = [[0] * n_cols for _ in range(n_rows)]

rolls = [[] for _ in range(n_dice)]
q = []
seen = set()
for r in range(n_rows):
    for c in range(n_cols):
        for d in range(n_dice):
            mask = ff(r, c, d, 0)
            q.append(mask)
            seen.add(mask)

while q:
    r, c, d, i = fr(q.pop())

    if len(rolls[d]) == i:
        rolls[d].append(dice[d].roll())

    if grid[r][c] != rolls[d][i]:
        continue

    coins[r][c] = 1

    masks = [ff(r, c, d, i + 1)]
    if r - 1 >= 0:
        masks.append(ff(r - 1, c, d, i + 1))
    if r + 1 < n_rows:
        masks.append(ff(r + 1, c, d, i + 1))
    if c - 1 >= 0:
        masks.append(ff(r, c - 1, d, i + 1))
    if c + 1 < n_cols:
        masks.append(ff(r, c + 1, d, i + 1))
    for mask in masks:
        if mask not in seen:
            q.append(mask)
            seen.add(mask)

ans3 = sum(sum(row) for row in coins)
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
