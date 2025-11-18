from time import time
from collections import deque

# ********************************* part 1
time_start = time()


def simulate(arr, max_cycle=1 << 63):
    cycle = 0
    while cycle < max_cycle:
        change = False
        for i in range(len(arr) - 1):
            if nums[i] > nums[i + 1]:
                nums[i] -= 1
                nums[i + 1] += 1
                change = True
        if not change:
            break
        cycle += 1
    while cycle < max_cycle:
        change = False
        for i in range(len(arr) - 1):
            if nums[i] < nums[i + 1]:
                nums[i] += 1
                nums[i + 1] -= 1
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
n = len(nums)
target = sum(nums) // n

assert n >= 2
assert all(nums[i] < nums[i + 1] for i in range(n - 1))

sum_left, count_left = nums[0], 1
sum_right, count_right = nums[-1], 1
nums = deque(nums[1:-1])

cycle = 0
while nums:
    c_left = count_left * nums[0] - sum_left
    c_right = sum_right - count_right * nums[-1]
    c = min(c_left, c_right)
    sum_left += c
    sum_right -= c
    cycle += c
    if c_left == c and nums:
        sum_left += nums.popleft()
        count_left += 1
    if c_right == c and nums:
        sum_right += nums.pop()
        count_right += 1
cycle += target * count_left - sum_left

ans3 = cycle
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
