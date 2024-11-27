from itertools import combinations


def load_notes(data):
    devices, notes = [], []
    for line in data:
        x, y = line.split(":")
        devices += [x]
        notes += [y.split(",")]
    return devices, notes


def load_track(data):
    track = [data[0][0], data[0][1]]
    n, m = len(data), max(len(row) for row in data)
    seen = [[False] * m for _ in range(n)]
    seen[0][0] = seen[0][1] = True
    r, c = 0, 1
    done = False
    while not done:
        done = True
        for rn, cn in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if 0 <= rn < n and 0 <= cn < len(data[rn]):
                if not seen[rn][cn] and data[rn][cn] != " ":
                    r, c = rn, cn
                    track += [data[r][c]]
                    seen[r][c] = True
                    done = False
                    break
    return track[1:] + track[0:1]


def loop(n, notes, track):
    total, power_level, i = 0, 10, 0
    for _ in range(n):
        for c in track:
            if c == "+":
                power_level += 1
            elif c == "-":
                power_level -= 1
            else:
                if notes[i % len(notes)] == "+":
                    power_level += 1
                elif notes[i % len(notes)] == "-":
                    power_level -= 1
            total += power_level
            i += 1
    return total


# ********************************* part 1
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q07_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

devices, notes = load_notes(data)

essence = []
for note in notes:
    total, power_level = 0, 10
    for i in range(10):
        action = note[i % len(note)]
        if action == "+":
            power_level += 1
        elif action == "-":
            power_level = max(0, power_level - 1)
        total += power_level
    essence += [total]

idx = sorted(range(len(devices)), key=lambda i: -essence[i])

ans1 = "".join(devices[i] for i in idx)
print(f"part 1: {ans1}")

# ********************************* part 2
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q07_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
INPUT_FILE2 = "./TheKingdomOfAlgorithmia2024/data/q07_p2_track.txt"
data2 = [line.rstrip('\n') for line in open(INPUT_FILE2, "r")]
ans2 = ""

devices, notes = load_notes(data)
n = len(devices)
track = load_track(data2)

essence = []
for i in range(n):
    essence += [loop(10, notes[i], track)]

idx = sorted(range(len(devices)), key=lambda i: -essence[i])

ans2 = "".join(devices[i] for i in idx)
print(f"part 2: {ans2}")

# ********************************* part 3
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q07_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
INPUT_FILE2 = "./TheKingdomOfAlgorithmia2024/data/q07_p3_track.txt"
data2 = [line.rstrip('\n') for line in open(INPUT_FILE2, "r")]
ans3 = 0

devices, notes = load_notes(data)
n = len(devices)
track = load_track(data2)

essence_to_beat = loop(2024, notes[0], track)
for c1 in combinations(range(11), 6):
    for c2 in combinations(c1, 3):
        note = ["+"] * 11
        for c in c1:
            note[c] = "-"
        for c in c2:
            note[c] = "="
        if loop(2024, note, track) > essence_to_beat:
            ans3 += 1
print(f"part 3: {ans3}")

