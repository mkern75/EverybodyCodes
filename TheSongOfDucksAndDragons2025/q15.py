from time import time
from collections import defaultdict
from heapq import heappop, heappush

# ********************************* part 1
time_start = time()


def build_wall(instr):
    x, y, dx, dy = 0, 0, 0, 1
    wall = {(x, y)}
    for direct, amount in instr:
        dx, dy = (-dy, dx) if direct == "L" else (dy, -dx)
        for _ in range(amount):
            x += dx
            y += dy
            wall.add((x, y))
    return (0, 0), (x, y), wall


def calc_dist(start, end, wall):
    dist = defaultdict(lambda: 1 << 63)
    dist[start] = 0
    todo = [start]
    for (x, y) in todo:
        d = dist[x, y]
        for xn, yn in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if (xn, yn) == end:
                return dist[x, y] + 1
            elif (xn, yn) not in wall:
                if d + 1 < dist[xn, yn]:
                    dist[xn, yn] = d + 1
                    todo.append((xn, yn))
    assert False


INPUT_FILE = "./data/q15_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

instr = [(x[0], int(x[1:])) for x in data[0].split(",")]
start, end, wall = build_wall(instr)
ans1 = calc_dist(start, end, wall)

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()

INPUT_FILE = "./data/q15_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

instr = [(x[0], int(x[1:])) for x in data[0].split(",")]
start, end, wall = build_wall(instr)
ans2 = calc_dist(start, end, wall)

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
    x, y, dx, dy = 0, 0, 0, 1
    wall_segments = []
    for direct, amount in instr:
        dx, dy = (-dy, dx) if direct == "L" else (dy, -dx)
        xn, yn = x + amount * dx, y + amount * dy
        wall_segments.append((x, y, xn, yn))
        x, y = xn, yn
    return (0, 0), (x, y), wall_segments


def init_compression(wall_segments):
    x_values, y_values = set(), set()
    for x1, y1, x2, y2 in wall_segments:
        x_values.update([x1 - 1, x1, x1 + 1, x2 - 1, x2, x2 + 1])
        y_values.update([y1 - 1, y1, y1 + 1, y2 - 1, y2, y2 + 1])
    return CoordinateCompression(x_values), CoordinateCompression(y_values)


def compress(start, end, wall_segments, compression):
    start = (compression[0].compressed_value(start[0]), compression[1].compressed_value(start[1]))
    end = (compression[0].compressed_value(end[0]), compression[1].compressed_value(end[1]))
    wall = set()
    for x1, y1, x2, y2 in wall_segments:
        x1 = compression[0].compressed_value(x1)
        y1 = compression[1].compressed_value(y1)
        x2 = compression[0].compressed_value(x2)
        y2 = compression[1].compressed_value(y2)
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                wall.add((x1, y))
        else:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                wall.add((x, y1))
    return start, end, wall


def calc_dist3(start, end, wall, compression):
    x_min, x_max = 0, compression[0].n_compressed_values() - 1
    y_min, y_max = 0, compression[1].n_compressed_values() - 1
    dist = defaultdict(lambda: 1 << 63)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, (x, y) = heappop(pq)
        if d != dist[x, y]:
            continue
        if (x, y) == end:
            return d
        for xn, yn in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if xn < x_min or xn > x_max or yn < y_min or yn > y_max:
                continue
            dx = abs(compression[0].original_value(x) - compression[0].original_value(xn))
            dy = abs(compression[1].original_value(y) - compression[1].original_value(yn))
            dn = d + dx + dy
            if (xn, yn) == end or (xn, yn) not in wall:
                if dn < dist[xn, yn]:
                    dist[xn, yn] = dn
                    heappush(pq, (dn, (xn, yn)))
    assert False


INPUT_FILE = "./data/q15_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

instr = [(x[0], int(x[1:])) for x in data[0].split(",")]
start, end, wall_segments = build_wall_segments(instr)
compression = init_compression(wall_segments)
start, end, wall = compress(start, end, wall_segments, compression)
ans3 = calc_dist3(start, end, wall, compression)

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
