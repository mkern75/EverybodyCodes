from time import time

# ********************************* part 1
time_start = time()


def simulate(arr, max_cycle=1 << 63):
    cycle = 0
    while cycle < max_cycle:
        change = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i] -= 1
                arr[i + 1] += 1
                change = True
        if not change:
            break
        cycle += 1
    while cycle < max_cycle:
        change = False
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                arr[i] += 1
                arr[i + 1] -= 1
                change = True
        if not change:
            break
        cycle += 1
    check_sum = sum(i * v for i, v in enumerate(arr, start=1))
    return cycle, check_sum


INPUT_FILE = "./data/q11_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
nums = [int(line) for line in data]

_, ans1 = simulate(nums, 10)
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q11_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
nums = [int(line) for line in data]

ans2, _ = simulate(nums)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q11_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
nums = [int(line) for line in data]

assert all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))
target = sum(nums) // len(nums)
lower = sum(target - x for x in nums if x < target)
higher = sum(x - target for x in nums if x > target)
assert lower == higher

ans3 = lower
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
