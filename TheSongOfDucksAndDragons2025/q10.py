from time import time
from functools import cache

# ********************************* part 1
time_start = time()


def load_board(board) -> tuple[int, int, tuple[int, int], set[tuple[int, int]], set[tuple[int, int]]]:
    n_rows, n_cols = len(board), len(board[0])
    dragon, sheep, hides = (-1, -1), set(), set()
    for r in range(n_rows):
        for c in range(n_cols):
            if board[r][c] == "D":
                dragon = (r, c)
            elif board[r][c] == "S":
                sheep.add((r, c))
            elif board[r][c] == "#":
                hides.add((r, c))
    return n_rows, n_cols, dragon, sheep, hides


def calc_dragon_moves(n_rows: int, n_cols: int) -> list[list[list[tuple[int, int]]]]:
    moves = [[[] for _ in range(n_cols)] for _ in range(n_rows)]
    for r in range(n_rows):
        for c in range(n_cols):
            for dr, dc in [(-1, -2), (-1, 2), (-2, 1), (-2, -1), (1, -2), (1, 2), (2, -1), (2, 1)]:
                rn, cn = r + dr, c + dc
                if 0 <= rn < n_rows and 0 <= cn < n_cols:
                    moves[r][c].append((rn, cn))
    return moves


INPUT_FILE = "./data/q10_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

n_rows, n_cols, dragon, sheep, _ = load_board(data)
dragon_moves = calc_dragon_moves(n_rows, n_cols)

reachable = {dragon}
for _ in range(4):
    reachable_new = set()
    for pos in reachable:
        reachable_new.update(dragon_moves[pos[0]][pos[1]])
    reachable.update(reachable_new)
ans1 = len(reachable.intersection(sheep))
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q10_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

n_rows, n_cols, dragon, sheep, hides = load_board(data)
dragon_moves = calc_dragon_moves(n_rows, n_cols)

ans2 = 0
reachable = {dragon}
for _ in range(20):

    reachable_new = set()
    for pos in reachable:
        reachable_new.update(dragon_moves[pos[0]][pos[1]])
    reachable = reachable_new
    eaten = sheep.intersection(reachable).difference(hides)
    ans2 += len(eaten)
    sheep.difference_update(eaten)

    sheep_new = set()
    for pos in sheep:
        sheep_new.add((pos[0] + 1, pos[1]))
    sheep = sheep_new
    eaten = sheep.intersection(reachable).difference(hides)
    ans2 += len(eaten)
    sheep.difference_update(eaten)

print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()


def get_safe_positions(n_rows: int, n_cols, hides):
    safe = set()
    for r in range(n_rows - 1, -1, -1):
        for c in range(n_cols):
            if (r, c) in hides:
                if r == n_rows - 1 or (r + 1, c) in safe:
                    safe.add((r, c))
    return safe


INPUT_FILE = "./data/q10_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

n_rows, n_cols, dragon, sheep, hides = load_board(data)
dragon_moves = calc_dragon_moves(n_rows, n_cols)
safe = get_safe_positions(n_rows, n_cols, hides)


@cache
def solve(dragon: tuple[int, int], n_sheep: int, sheep_rows: tuple, turn: int = 0) -> int:
    # sheep move
    if turn == 0:
        res = 0
        can_escape = False
        has_move = False
        for c in range(n_cols):
            if sheep_rows[c] == -1:
                continue
            if sheep_rows[c] + 1 >= n_rows:
                can_escape = True
            elif (sheep_rows[c] + 1, c) in safe:
                can_escape = True
            elif (sheep_rows[c] + 1, c) != dragon or (sheep_rows[c] + 1, c) in hides:
                has_move = True
                sheep_rows_new = list(sheep_rows)
                sheep_rows_new[c] += 1
                sheep_rows_new = tuple(sheep_rows_new)
                res += solve(dragon, n_sheep, sheep_rows_new, 1)
        if not can_escape and not has_move:
            res += solve(dragon, n_sheep, sheep_rows, 1)
        return res

    # dragon move
    else:
        res = 0
        for dragon_new in dragon_moves[dragon[0]][dragon[1]]:
            if sheep_rows[dragon_new[1]] == dragon_new[0] and dragon_new not in hides:
                n_sheep_new = n_sheep - 1
                if not n_sheep_new:
                    res += 1
                else:
                    sheep_rows_new = list(sheep_rows)
                    sheep_rows_new[dragon_new[1]] = -1
                    sheep_rows_new = tuple(sheep_rows_new)
                    res += solve(dragon_new, n_sheep_new, sheep_rows_new, 0)
            else:
                res += solve(dragon_new, n_sheep, sheep_rows, 0)
        return res


sheep_rows = [-1] * n_cols
for r, c in sheep:
    sheep_rows[c] = r

ans3 = solve(dragon, len(sheep), tuple(sheep_rows))
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
