from time import time


def parse(s: str, repeats: int = 1):
    letters, cnt = [], []
    for _ in range(repeats):
        for i, char in enumerate(s):
            if not letters or char != letters[-1]:
                letters.append(char)
                cnt.append(1)
            else:
                cnt[-1] += 1
    return letters, cnt


def solve(letters, cnt):
    if len(letters) <= 1:
        return True, 0, 0, [], []

    char = letters[0]
    for i in range(len(letters) - 1, 0, -1):
        if letters[i] == char:
            last = i
            break
    else:
        return False, 0, 0, letters[1:], cnt[1:]

    total_flips = 0
    total_flip_length = 0
    il = 1
    ir = last
    letters_remaining = letters[ir + 1:][::-1]  # initially reversed so we can add to the end
    cnt_remaining = cnt[ir + 1:][::-1]  # initially reversed so we can add to the end
    current_flip_length = sum(cnt[i] for i in range(il, ir + 1))

    while il <= ir:

        assert letters[ir] == char
        total_flips += 1
        total_flip_length += current_flip_length
        current_flip_length -= cnt[ir]
        ir -= 1
        while letters[il] != char:
            current_flip_length -= cnt[il]
            if letters_remaining and letters[il] == letters_remaining[-1]:
                cnt_remaining[-1] += cnt[il]
            else:
                letters_remaining.append(letters[il])
                cnt_remaining.append(cnt[il])
            il += 1

        if il > ir:
            break

        assert letters[il] == char
        total_flips += 1
        total_flip_length += current_flip_length
        current_flip_length -= cnt[il]
        il += 1
        while letters[ir] != char:
            current_flip_length -= cnt[ir]
            if letters_remaining and letters[ir] == letters_remaining[-1]:
                cnt_remaining[-1] += cnt[ir]
            else:
                letters_remaining.append(letters[ir])
                cnt_remaining.append(cnt[ir])
            ir -= 1

    return False, total_flips, total_flip_length, letters_remaining[::-1], cnt_remaining[::-1]


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q16_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans1 = 0
letters, cnt = parse(data[0])
while True:
    finished, flips, _, letters, cnt = solve(letters, cnt)
    if finished:
        break
    ans1 += flips

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q16_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans2 = 0
letters, cnt = parse(data[0], 10)
while True:
    finished, _, flip_length, letters, cnt = solve(letters, cnt)
    if finished:
        break
    ans2 += flip_length

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q16_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans3 = 0
letters, cnt = parse(data[0], 100)
while True:
    finished, _, flip_length, letters, cnt = solve(letters, cnt)
    if finished:
        break
    ans3 += flip_length

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
