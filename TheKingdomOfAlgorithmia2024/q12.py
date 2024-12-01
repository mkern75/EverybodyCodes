from time import time


def load_locations(data):
    loc = {"T": []}
    for r, row in enumerate(data):
        for c, x in enumerate(row):
            if x == "A":
                loc["A"] = (r, c, 1)
            elif x == "B":
                loc["B"] = (r, c, 2)
            elif x == "C":
                loc["C"] = (r, c, 3)
            elif x == "T":
                loc["T"] += [(r, c, 1)]
            elif x == "H":
                loc["T"] += [(r, c, 2)]
    return loc


def hit_targets(loc):
    res = 0
    for rs, cs, ms in [loc["A"], loc["B"], loc["C"]]:
        for rt, ct, mt in loc["T"]:
            delta = ct - cs - (rt - rs)
            if delta % 3 == 0:
                res += ms * mt * delta // 3
    return res


def calc_hit(rt, ct, rs, cs, ms):
    t_delay = 0
    if (ct - cs) & 1:
        t_delay = 1
        rt -= 1
        ct -= 1

    delta = ct - cs
    # details of hit if possible
    t_hit = delta // 2
    r_hit = rt - delta // 2
    c_hit = ct - delta // 2
    dr = r_hit - rs
    dc = c_hit - cs

    if r_hit < 0:
        return None
    if dc < dr:
        return None

    # hit in phase 1
    p_hit = dr
    if dr == dc:
        return t_delay + t_hit, r_hit, c_hit, p_hit, ms

    # hit in phase 2
    p_hit = dr
    if p_hit < dc <= 2 * p_hit:
        return t_delay + t_hit, r_hit, c_hit, p_hit, ms

    # hit in phase 3
    p_hit, r = divmod(dr + t_hit, 3)
    if r == 0:
        return t_delay + t_hit, r_hit, c_hit, p_hit, ms

    return None


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

segments = [(0, 0, 1), (1, 0, 2), (2, 0, 3)]
targets = [tuple(map(int, line.split()))[::-1] for line in data]

ans3 = 0
for rt, ct in targets:
    hits = []
    for rs, cs, ms in segments:
        hit = calc_hit(rt, ct, rs, cs, ms)
        if hit is not None:
            hits += [hit]
    highest = max(h[1] for h in hits)
    hits_highest = [h for h in hits if h[1] == highest]
    ans3 += min(h[3] * h[4] for h in hits_highest)

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
