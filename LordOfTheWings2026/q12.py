from time import time


def get_stacks(grid):
    res = []
    R, C = len(grid), len(grid[0])
    seen = set()
    for r in range(R):
        for c in range(C):
            if (r, c) in seen:
                continue
            if grid[r][c] == ".":
                seen.add((r, c))
                continue

            # bfs
            stack = {(r, c)}
            todo = [(r, c)]
            for rr, cc in todo:
                for rn, cn in [(rr + 1, cc), (rr - 1, cc), (rr, cc + 1), (rr, cc - 1)]:
                    if 0 <= rn < R and 0 <= cn < C and grid[rn][cn] == "#" and (rn, cn) not in stack:
                        stack.add((rn, cn))
                        todo.append((rn, cn))
            res.append(stack)
            seen.update(stack)

    return res


def get_bounds(area):
    r_min, r_max, c_min, c_max = 1 << 31, 0, 1 << 31, 0
    for r, c in area:
        r_min = min(r_min, r)
        r_max = max(r_max, r)
        c_min = min(c_min, c)
        c_max = max(c_max, c)
    return r_min, c_min, r_max, c_max


def solve(stack):
    r_min, c_min, r_max, c_max = get_bounds(stack)

    # rectangle (all 4 corners are part of stack)
    if (r_min, c_min) in stack and (r_min, c_max) in stack and (r_max, c_min) in stack and (r_max, c_max) in stack:

        # without gap
        if (r_max - r_min + 1) * (c_max - c_min + 1) == len(stack):
            return min(r_max - r_min + 1, c_max - c_min + 1)

        # with gap
        else:

            gap = {(r, c) for r in range(r_min, r_max + 1) for c in range(c_min, c_max + 1) if ((r, c) not in stack)}
            r2_min, c2_min, r2_max, c2_max = get_bounds(gap)

            res1 = r_max - r_min + 1 - (r2_max - r2_min + 1)
            res1 += min(r2_max - r2_min + 1, c2_min - c_min)
            res1 += min(r2_max - r2_min + 1, c_max - c2_max)

            res2 = c_max - c_min + 1 - (c2_max - c2_min + 1)
            res2 += min(c2_max - c2_min + 1, r2_min - r_min)
            res2 += min(c2_max - c2_min + 1, r_max - r2_max)

            return min(res1, res2)

    # L-shaped
    else:
        left, right = 0, 0
        for r in range(r_min, r_max + 1):
            left += int((r, c_min) in stack)
            right += int((r, c_max) in stack)
        top, bottom = 0, 0
        for c in range(c_min, c_max + 1):
            top += int((r_min, c) in stack)
            bottom += int((r_max, c) in stack)
        return min(r_max - r_min + 1, c_max - c_min + 1, min(left, right) + min(top, bottom))


# ********************************* part 1
time_start = time()
INPUT_FILE = "./data/q12_p1.txt"
grid = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans1 = sum(solve(stack) for stack in get_stacks(grid))

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q12_p2.txt"
grid = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans2 = sum(solve(stack) for stack in get_stacks(grid))

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q12_p3.txt"
grid = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans3 = sum(solve(stack) for stack in get_stacks(grid))

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
