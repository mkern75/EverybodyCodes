from time import time


def parse_segments(s: str, repeats: int = 1):
    segments = []
    for _ in range(repeats):
        for i, char in enumerate(s):
            if not segments or char != segments[-1][0]:
                segments.append([char, 1])
            else:
                segments[-1][-1] += 1
    return segments


def solve(segments):
    if len(segments) <= 1:
        return True, 0, 0, []

    char = segments[0][0]
    for i in range(len(segments) - 1, 0, -1):
        if segments[i][0] == char:
            last = i
            break
    else:
        return False, 0, 0, segments[1:]

    total_flips = 0
    total_flip_length = 0
    il = 1
    ir = last
    segments_remaining = segments[ir + 1:][::-1]  # initially reversed
    current_flip_length = sum(segments[i][1] for i in range(il, ir + 1))

    while il <= ir:

        assert segments[ir][0] == char
        total_flips += 1
        total_flip_length += current_flip_length
        current_flip_length -= segments[ir][1]
        ir -= 1
        while segments[il][0] != char:
            current_flip_length -= segments[il][1]
            if segments_remaining and segments[il][0] == segments_remaining[-1][0]:
                segments_remaining[-1][1] += segments[il][1]
            else:
                segments_remaining.append(segments[il])
            il += 1

        if il > ir:
            break

        assert segments[il][0] == char
        total_flips += 1
        total_flip_length += current_flip_length
        current_flip_length -= segments[il][1]
        il += 1
        while segments[ir][0] != char:
            current_flip_length -= segments[ir][1]
            if segments_remaining and segments[ir][0] == segments_remaining[-1][0]:
                segments_remaining[-1][1] += segments[ir][1]
            else:
                segments_remaining.append(segments[ir])
            ir -= 1

    return False, total_flips, total_flip_length, segments_remaining[::-1]


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q16_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans1 = 0
shelf = parse_segments(data[0])
while True:
    finished, flips, _, shelf = solve(shelf)
    if finished:
        break
    ans1 += flips

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q16_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans2 = 0
shelf = parse_segments(data[0], 10)
while True:
    finished, _, flip_length, shelf = solve(shelf)
    if finished:
        break
    ans2 += flip_length

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q16_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans3 = 0
shelf = parse_segments(data[0], 100)
while True:
    finished, _, flip_length, shelf = solve(shelf)
    if finished:
        break
    ans3 += flip_length

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
