from time import time


def parse(data):
    hands = list(map(int, data[0].split()[1].split(":")))
    direction = list(data[1].split()[1].split(":"))
    current = list(map(int, data[2].split()[1].split(":")))
    move = list(map(int, data[3].split()[1].split(":")))
    return hands, direction, current, move


def check(p1_before: int, p1_after: int, hand1: int, p2_before: int, p2_after: int, hand2: int) -> int:
    if p1_before * hand2 == p2_before * hand1:
        return 0
    if p1_after * hand2 == p2_after * hand1:
        return 1
    if p1_before == hand1 - 1 and p1_after == 0:
        p1_after = hand1
    if p1_before == 0 and p1_after == hand1 - 1:
        p1_before = hand1
    if p2_before == hand2 - 1 and p2_after == 0:
        p2_after = hand2
    if p2_before == 0 and p2_after == hand2 - 1:
        p2_before = hand2
    if p1_before * hand2 < p2_before * hand1 and p1_after * hand2 >= p2_after * hand1:
        return 1
    if p1_before * hand2 > p2_before * hand1 and p1_after * hand2 <= p2_after * hand1:
        return 1
    return 0


def one_step(t, current, hands, direction, move):
    res = current[:]
    for i in range(3):
        if t <= move[i]:
            res[i] += 1 if direction[i] == "CW" else -1
            res[i] %= hands[i]
    return res


def solve(hands, direction, current, move):
    max_moves = max(move)
    res = 0
    t = 0
    mem = {tuple(current): (t, res)}

    while t < max_moves:

        t += 1
        nxt = one_step(t, current, hands, direction, move)
        res += check(current[0], nxt[0], hands[0], current[1], nxt[1], hands[1])
        res += check(current[0], nxt[0], hands[0], current[2], nxt[2], hands[2])
        res += check(current[1], nxt[1], hands[1], current[2], nxt[2], hands[2])
        current = nxt

        if t in move:
            mem = {}

        if tuple(current) in mem:
            t_earlier, res_earlier = mem[tuple(current)]
            delta_t = t - t_earlier
            delta_res = res - res_earlier

            max_t = max_moves - t
            for m in move:
                if t <= m:
                    max_t = min(max_t, m - t)

            k = max_t // delta_t
            t += k * delta_t
            res += k * delta_res
            mem = {}

        mem[tuple(current)] = (t, res)

    return res


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q13_p1.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

ans1 = sum(solve(*parse(data)) for data in blocks)

print(f"part 1: {ans1} ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q13_p2.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

ans2 = sum(solve(*parse(data)) for data in blocks)

print(f"part 2: {ans2} ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q13_p3.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

ans3 = sum(solve(*parse(data)) for data in blocks)

print(f"part 3: {ans3} ({time() - time_start:.3f}s)")
