from time import time
from heapq import heappop, heappush

INF = 1 << 31


def dijsktra(grid, start, end):
    n, m = len(grid), max(len(row) for row in grid)
    rs, cs = next((r, c) for r in range(n) for c in range(m) if grid[r][c] == start)
    dist = [[INF] * m for _ in range(n)]
    dist[rs][cs] = 0

    def level(r, c):
        return 0 if grid[r][c] in [start, end] else int(grid[r][c])

    def diff(r1, c1, r2, c2):
        lvl1 = level(r1, c1)
        lvl2 = level(r2, c2)
        return min(abs(lvl1 - lvl2), abs((lvl1 + 10) - lvl2), abs(lvl1 - (lvl2 + 10))) + 1

    q = [(dist[rs][cs], rs, cs)]
    while q:
        d, r, c = heappop(q)
        if d > dist[r][c]:
            continue
        if grid[r][c] == end:
            return d
        for rn, cn in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if 0 <= rn < n and 0 <= cn < m:
                if grid[rn][cn] in "0123456789" or grid[rn][cn] == end:
                    delta = diff(r, c, rn, cn)
                    if d + delta < dist[rn][cn]:
                        dist[rn][cn] = d + delta
                        heappush(q, (dist[rn][cn], rn, cn))


# ********************************* part 1
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q13_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans1 = dijsktra(data, "S", "E")
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q13_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans2 = dijsktra(data, "S", "E")
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q13_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans3 = dijsktra(data, "E", "S")
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
