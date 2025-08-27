from time import time


def play(start_slot, sequence, machine):
    h, w = len(machine), len(machine[0])
    r, c = -1, 2 * start_slot
    i = 0
    while r < h - 1:
        r += 1
        if machine[r][c] == "*":
            if sequence[i] == "L":
                if c == 0:
                    c += 1
                else:
                    c -= 1
            else:
                if c == w - 1:
                    c -= 1
                else:
                    c += 1
            i += 1
    final_slot = c // 2
    return max(0, 2 * (final_slot + 1) - (start_slot + 1))


# ********************************* part 1
time_start = time()
INPUT_FILE = "./TheEntertainmentHub/data/q01_p1.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

machine = blocks[0]
sequences = blocks[1]

ans1 = sum(play(start_slot, sequence, machine) for start_slot, sequence in enumerate(sequences))
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./TheEntertainmentHub/data/q01_p2.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

machine = blocks[0]
sequences = blocks[1]
n_slots = (len(machine[0]) + 1) // 2

ans2 = 0
for sequence in sequences:
    ans2 += max(play(start_slot, sequence, machine) for start_slot in range(n_slots))
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./TheEntertainmentHub/data/q01_p3.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

machine = blocks[0]
sequences = blocks[1]
n_slots = (len(machine[0]) + 1) // 2
n_tokens = len(sequences)

res = [[0] * n_slots for _ in range(n_tokens)]
for i, sequence in enumerate(sequences):
    for start_slot in range(n_slots):
        res[i][start_slot] = play(start_slot, sequence, machine)

dp_min = [1 << 31] * (1 << n_slots)
dp_max = [0] * (1 << n_slots)
dp_min[0] = 0
to_check = {0}
for i, sequence in enumerate(sequences):
    to_check_new = set()
    for start_slot in range(n_slots):
        for pos in to_check:
            pos_new = pos | (1 << start_slot)
            if pos_new != pos:
                dp_min[pos_new] = min(dp_min[pos_new], dp_min[pos] + res[i][start_slot])
                dp_max[pos_new] = max(dp_max[pos_new], dp_max[pos] + res[i][start_slot])
                to_check_new.add(pos_new)
    to_check = to_check_new

ans_min = min(dp_min[pos] for pos in to_check)
ans_max = max(dp_max[pos] for pos in to_check)
ans3 = f"{ans_min} {ans_max}"
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
