from time import time
from collections import defaultdict

INF = 1 << 63
DIR = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}


class Simulation:
    def __init__(self, data, limit=INF, debug=False):
        self.walls = set()
        self.ghosts = []
        for r, row in enumerate(data):
            for c, char in enumerate(row):
                if char == "#":
                    self.walls.add((r, c))
                elif char in DIR:
                    self.ghosts.append([r, c, DIR[char][0], DIR[char][1]])
        self.limit = limit
        self.collisions = [0] * len(self.ghosts)
        self.n_collisions = 0
        self.cycle = 0
        self.debug = debug

    def _purge_disappeared_ghosts(self):
        if any(c == self.limit for c in self.collisions):
            self.ghosts = [g for g, c in zip(self.ghosts, self.collisions) if c < self.limit]
            self.collisions = [c for c in self.collisions if c < self.limit]
            if self.debug:
                print(f"cycle={self.cycle:_}  ghosts={len(self.ghosts)}")

    def run_one_cycle(self):
        self.cycle += 1
        for i, (r, c, dr, dc) in enumerate(self.ghosts):
            if (r + dr, c + dc) in self.walls:
                # 90-degree rotation clockwise
                self.ghosts[i][2], self.ghosts[i][3] = self.ghosts[i][3], -self.ghosts[i][2]
                self.collisions[i] += 1
                self.n_collisions += 1
            else:
                self.ghosts[i][0] += dr
                self.ghosts[i][1] += dc
        same = defaultdict(list)
        for i, (r, c, _, _) in enumerate(self.ghosts):
            if self.collisions[i] < self.limit:
                same[r, c].append(i)
        for lst in same.values():
            if len(lst) > 1:
                for i in lst:
                    # 180-degree rotation
                    self.ghosts[i][2], self.ghosts[i][3] = -self.ghosts[i][2], -self.ghosts[i][3]
                    self.collisions[i] += 1
                self.n_collisions += len(lst)
        self._purge_disappeared_ghosts()

    def run_full_simulation(self):
        mem = {}  # position memory
        while self.ghosts:
            self.run_one_cycle()

            # check whether current position has been encountered before
            pos = tuple(tuple(g) for g in self.ghosts)
            if pos not in mem:
                mem[pos] = (self.cycle, tuple(self.collisions))  # add to memory
                continue

            # delta to when current position was previously encountered
            cycle_prev, collisions_prev = mem[pos]
            delta_cycle = self.cycle - cycle_prev
            delta_collisions = [x - y for x, y, in zip(self.collisions, collisions_prev)]

            # apply delta as often as possible within limit
            factor = INF
            for i, delta in enumerate(delta_collisions):
                if delta > 0:
                    factor = min(factor, (self.limit - self.collisions[i] - 1) // delta)  # the -1 is important!!!
            for i, delta in enumerate(delta_collisions):
                self.collisions[i] += factor * delta
                self.n_collisions += factor * delta
            self.cycle += factor * delta_cycle

            self._purge_disappeared_ghosts()

            # reset position memory
            pos = tuple(tuple(g) for g in self.ghosts)
            mem = {pos: (self.cycle, tuple(self.collisions))}

        return self.cycle


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q10_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

sim = Simulation(data)
for _ in range(10):
    sim.run_one_cycle()
ans1 = sim.n_collisions
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q10_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

sim = Simulation(data, 10_000)
ans2 = sim.run_full_simulation()
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q10_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

sim = Simulation(data, 1_000_000_000_000)
ans3 = sim.run_full_simulation()
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
