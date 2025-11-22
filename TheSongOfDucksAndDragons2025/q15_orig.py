from time import time
from collections import defaultdict
from heapq import heappop, heappush

# ********************************* part 1
time_start = time()


def build_wall(instr):
    x_start, y_start = 0, 0
    dx, dy = 0, 1
    wall = {(x_start, y_start)}
    x, y = x_start, y_start
    for d, n in instr:
        if d == "L":
            dx, dy = -dy, dx
        else:
            dx, dy = dy, -dx
        for _ in range(n):
            x += dx
            y += dy
            wall.add((x, y))
    x_end, y_end = x, y
    return x_start, y_start, x_end, y_end, wall


def calc_dist(x_start, y_start, x_end, y_end, wall):
    dist = defaultdict(lambda: 1 << 63)
    dist[x_start, y_start] = 0
    todo = [(x_start, y_start)]
    for x, y in todo:
        d = dist[x, y]
        for xn, yn in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if (xn, yn) == (x_end, y_end):
                return dist[x, y] + 1
            elif (xn, yn) not in wall:
                if d + 1 < dist[xn, yn]:
                    dist[xn, yn] = d + 1
                    todo.append((xn, yn))
    assert False


INPUT_FILE = "./data/q15_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

instr = [(x[0], int(x[1:])) for x in data[0].split(",")]
x_start, y_start, x_end, y_end, wall = build_wall(instr)
ans1 = calc_dist(x_start, y_start, x_end, y_end, wall)

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()

INPUT_FILE = "./data/q15_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

instr = [(x[0], int(x[1:])) for x in data[0].split(",")]
x_start, y_start, x_end, y_end, wall = build_wall(instr)
ans2 = calc_dist(x_start, y_start, x_end, y_end, wall)

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()


class CoordinateCompression:
    def __init__(self, original_values, n_bits=64):
        import random
        self._rand_bits = random.getrandbits(n_bits)  # anti-hacking!
        self._orig_vals = []
        self._map = {}
        for x in sorted(original_values):
            if not self._orig_vals or x != self._orig_vals[-1]:
                self._orig_vals += [x]
                self._map[x ^ self._rand_bits] = len(self._map)
        self.n = len(self._orig_vals)

    def compressed_value(self, original_value):
        return self._map[original_value ^ self._rand_bits]

    def original_value(self, compressed_value):
        return self._orig_vals[compressed_value]

    def n_compressed_values(self):
        return self.n


def build_wall_segments(instr):
    x_start, y_start = 0, 0
    dx, dy = 0, 1
    wall_segments = []
    x, y = x_start, y_start
    for d, n in instr:
        if d == "L":
            dx, dy = -dy, dx
        else:
            dx, dy = dy, -dx
        xn = x + n * dx
        yn = y + n * dy
        wall_segments.append((x, y, xn, yn))
        x, y = xn, yn
    x_end, y_end = x, y
    return x_start, y_start, x_end, y_end, wall_segments


def calc_dist3(x_start, y_start, x_end, y_end, wall, compression_x, compression_y):
    x_min = compression_x.compressed_value(min(compression_x._orig_vals))
    x_max = compression_x.compressed_value(max(compression_x._orig_vals))
    y_min = compression_x.compressed_value(min(compression_x._orig_vals))
    y_max = compression_x.compressed_value(max(compression_x._orig_vals))
    dist = defaultdict(lambda: 1 << 63)
    dist[x_start, y_start] = 0
    pq = [(0, x_start, y_start)]
    while pq:
        d, x, y = heappop(pq)
        if d != dist[x, y]:
            continue
        if (x, y) == (x_end, y_end):
            return d
        for xn, yn in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if xn < x_min or xn > x_max or yn < y_min or yn > y_max:
                continue
            dx = abs(compression_x.original_value(x) - compression_x.original_value(xn))
            dy = abs(compression_y.original_value(y) - compression_y.original_value(yn))
            if (xn, yn) == (x_end, y_end) or (xn, yn) not in wall:
                if d + dx + dy < dist[xn, yn]:
                    dist[xn, yn] = d + dx + dy
                    heappush(pq, (d + dx + dy, xn, yn))
    assert False


INPUT_FILE = "./data/q15_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

instr = [(x[0], int(x[1:])) for x in data[0].split(",")]
x_start, y_start, x_end, y_end, wall_segments = build_wall_segments(instr)

x_values, y_values = [], []
for x1, y1, x2, y2 in wall_segments:
    x_values.extend([x1 - 1, x1, x1 + 1, x2 - 1, x2, x2 + 1])
    y_values.extend([y1 - 1, y1, y1 + 1, y2 - 1, y2, y2 + 1])

compression_x = CoordinateCompression(x_values)
compression_y = CoordinateCompression(y_values)

x_start_comp = compression_x.compressed_value(x_start)
x_end_comp = compression_x.compressed_value(x_end)
y_start_comp = compression_y.compressed_value(y_start)
y_end_comp = compression_y.compressed_value(y_end)

wall_comp = set()
for x1, y1, x2, y2 in wall_segments:
    x1_comp = compression_x.compressed_value(x1)
    y1_comp = compression_y.compressed_value(y1)
    x2_comp = compression_x.compressed_value(x2)
    y2_comp = compression_y.compressed_value(y2)
    for x_comp in range(min(x1_comp, x2_comp), max(x1_comp, x2_comp) + 1):
        for y_comp in range(min(y1_comp, y2_comp), max(y1_comp, y2_comp) + 1):
            wall_comp.add((x_comp, y_comp))

ans3 = calc_dist3(x_start_comp, y_start_comp, x_end_comp, y_end_comp, wall_comp, compression_x, compression_y)
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
