from time import time


def load_locations(data):
    loc = {"T": []}
    for r, row in enumerate(data):
        for c, x in enumerate(row):
            if x in "ABC":
                loc[x] = (r, c)
            elif x == "T":
                loc["T"] += [(r, c, 1)]
            elif x == "H":
                loc["T"] += [(r, c, 2)]
    return loc


def hit_targets(loc):
    res = 0
    ra, ca = loc["A"]
    rb, cb = loc["B"]
    rc, cc = loc["C"]
    for rt, ct, ft in loc["T"]:
        delta_a = ct - ca - (rt - ra)
        delta_b = ct - cb - (rt - rb)
        delta_c = ct - cc - (rt - rc)
        if delta_a % 3 == 0:
            res += ft * 1 * delta_a // 3
        elif delta_b % 3 == 0:
            res += ft * 2 * delta_b // 3
        elif delta_c % 3 == 0:
            res += ft * 3 * delta_c // 3
    return res


def simulate(r, c, f, power, delay, pos_meteor):
    t = delay
    for _ in range(power):
        t, r, c = t + 1, r + 1, c + 1
        if t >= len(pos_meteor) or r > pos_meteor[t][0] or c > pos_meteor[t][1]:
            return []
        if pos_meteor[t] == (r, c):
            return [(t, r, c, power, f)]
    for _ in range(power):
        t, r, c = t + 1, r, c + 1
        if t >= len(pos_meteor) or r > pos_meteor[t][0] or c > pos_meteor[t][1]:
            return []
        if pos_meteor[t] == (r, c):
            return [(t, r, c, power, f)]
    for _ in range(power + 2):
        t, r, c = t + 1, r - 1, c + 1
        if t >= len(pos_meteor) or r > pos_meteor[t][0] or c > pos_meteor[t][1]:
            return []
        if pos_meteor[t] == (r, c):
            return [(t, r, c, power, f)]
    return []


# ********************************* part 1
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q12_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

loc = load_locations(data)
ans1 = hit_targets(loc)

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q12_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

loc = load_locations(data)
ans2 = hit_targets(loc)

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q12_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
ans3 = 0

ra, ca = 0, 0
rb, cb = 1, 0
rc, cc = 2, 0
targets = [tuple(map(int, line.split()))[::-1] for line in data]

for i, (rt, ct) in enumerate(targets):

    if i % 100 == 0:
        print(f"    {str(i).ljust(4, ' ')} ", end="")
    if i % 100 == 99:
        print("#")
    else:
        print("#", end="")

    k = min(rt, ct)
    pos_meteor = [(rt - t, ct - t) for t in range(k + 1)]

    hits = []
    for power in range(1, rt // 2 + 2):
        for delay in range(2):
            for r, c, f in [(ra, ca, 1), (rb, cb, 2), (rc, cc, 3)]:
                hits.extend(simulate(r, c, f, power, delay, pos_meteor))

    highest = max(h[1] for h in hits)
    hits_highest = [h for h in hits if h[1] == highest]
    ans3 += min(h[3] * h[4] for h in hits_highest)

print()
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
