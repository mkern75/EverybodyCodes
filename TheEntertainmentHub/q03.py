from time import time

# ********************************* part 1
time_start = time()
INPUT_FILE = "./TheEntertainmentHub/data/q03_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]


class Die:
    def __init__(self, id, faces, seed):
        self.id = id
        self.faces = faces
        self.face_idx = 0
        self.seed = seed
        self.pulse = seed
        self.roll_number = 1

    def roll(self):
        spin = self.roll_number * self.pulse
        self.face_idx += spin
        self.face_idx %= len(self.faces)
        self.pulse += spin
        self.pulse %= self.seed
        self.pulse += 1 + self.roll_number + self.seed
        self.roll_number += 1
        return self.faces[self.face_idx]

    @classmethod
    def load_from_input(cls, line):
        n, f, s = line.split(" ")
        id = int(n[:-1])
        faces = list(map(int, f[7:-1].split(",")))
        seed = int(s[5:])
        return Die(id, faces, seed)


dice = [Die.load_from_input(line) for line in data]

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

dice = [Die.load_from_input(line) for line in blocks[0]]
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


def ff(r, c, i):
    return r | (c << 10) | (i << 20)


def fr(state):
    return state & 0x3FF, (state >> 10) & 0x3FF, (state >> 20)


dice = [Die.load_from_input(line) for line in blocks[0]]

grid = [list(map(int, list(line))) for line in blocks[1]]
n_rows, n_cols = len(grid), len(grid[0])
coins = [[0] * n_cols for _ in range(n_rows)]

for die in dice:
    rolls = []
    q = []
    seen = set()
    for r in range(n_rows):
        for c in range(n_cols):
            state = ff(r, c, 0)
            q.append(state)
            seen.add(state)

    while q:
        r, c, i = fr(q.pop())

        if len(rolls) == i:
            rolls.append(die.roll())

        if grid[r][c] != rolls[i]:
            continue

        coins[r][c] = 1

        states = [ff(r, c, i + 1)]
        if r - 1 >= 0:
            states.append(ff(r - 1, c, i + 1))
        if r + 1 < n_rows:
            states.append(ff(r + 1, c, i + 1))
        if c - 1 >= 0:
            states.append(ff(r, c - 1, i + 1))
        if c + 1 < n_cols:
            states.append(ff(r, c + 1, i + 1))
        for state in states:
            if state not in seen:
                q.append(state)
                seen.add(state)

ans3 = sum(sum(row) for row in coins)
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
