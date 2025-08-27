from time import time

# ********************************* part 1
time_start = time()
INPUT_FILE = "./TheEntertainmentHub/data/q0x_p1_test.txt"
# INPUT_FILE = "./TheEntertainmentHub/data/q0x_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
# blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

ans1 = 0
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
# INPUT_FILE = "./TheEntertainmentHub/data/q0x_p2_test.txt"
# INPUT_FILE = "./TheEntertainmentHub/data/q0x_p2.txt"
# data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
# blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

ans2 = 0
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
# INPUT_FILE = "./TheEntertainmentHub/data/q0x_p3_test.txt"
# INPUT_FILE = "./TheEntertainmentHub/data/q0x_p3.txt"
# data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
# blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

ans3 = 0
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
