# ********************************* part 1
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q01_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
s = data[0]

ans1 = s.count("B") + 3 * s.count("C")

print(f"part 1: {ans1}")

# ********************************* part 2
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q01_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
s = data[0]

ans2 = 0
for i in range(0, len(s), 2):
    if s[i:i + 2] == "xx":
        continue
    for x in [s[i], s[i + 1]]:
        if x == "A":
            ans2 += 0 + 1
        elif x == "B":
            ans2 += 1 + 1
        elif x == "C":
            ans2 += 3 + 1
        elif x == "D":
            ans2 += 5 + 1
        elif x == "x":
            ans2 -= 1

print(f"part 2: {ans2}")

# ********************************* part 3
INPUT_FILE = "./TheKingdomOfAlgorithmia2024/data/q01_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
s = data[0]

ans3 = 0
for i in range(0, len(s), 3):
    for x in [s[i], s[i + 1], s[i + 2]]:
        if x == "A":
            ans3 += 0 + 2
        elif x == "B":
            ans3 += 1 + 2
        elif x == "C":
            ans3 += 3 + 2
        elif x == "D":
            ans3 += 5 + 2
    cnt_x = s[i:i + 3].count("x")
    if cnt_x == 2:
        ans3 -= 2
    elif cnt_x == 1:
        ans3 -= 2

print(f"part 3: {ans3}")