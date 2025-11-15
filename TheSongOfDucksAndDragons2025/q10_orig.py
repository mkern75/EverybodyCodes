from time import time
from collections import Counter, namedtuple

# ********************************* part 1
time_start = time()


def search_board(board):
    dragon, sheep, hides = (-1, -1), set(), set()
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == "D":
                dragon = (r, c)
            elif board[r][c] == "S":
                sheep.add((r, c))
            elif board[r][c] == "#":
                hides.add((r, c))
    return dragon, sheep, hides


def dragon_moves(dragon, n, m):
    moves = []
    r, c = dragon
    for dr, dc in [(-1, -2), (-1, 2), (-2, 1), (-2, -1), (1, -2), (1, 2), (2, -1), (2, 1)]:
        rn, cn = r + dr, c + dc
        if 0 <= rn < n and 0 <= cn < m:
            moves.append((rn, cn))
    return moves


INPUT_FILE = "./data/q10_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

board = [list(line) for line in data]
n, m = len(board), len(board[0])
dragon, sheep, _ = search_board(board)

reachable = {dragon}
for _ in range(4):
    reachable_new = set()
    for pos in reachable:
        reachable_new.update(dragon_moves(pos, n, m))
    reachable.update(reachable_new)
ans1 = len(reachable.intersection(sheep))
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()
INPUT_FILE = "./data/q10_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

board = [list(line) for line in data]
n, m = len(board), len(board[0])
dragon, sheep, hides = search_board(board)

ans2 = 0
reachable = {dragon}
for _ in range(20):

    reachable_new = set()
    for pos in reachable:
        reachable_new.update(dragon_moves(pos, n, m))
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
INPUT_FILE = "./data/q10_p3.txt"
# INPUT_FILE = "./data/q10_p3_test.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

board = [list(line) for line in data]
n, m = len(board), len(board[0])
dragon, sheep, hides = search_board(board)

sheep_rows = [-1] * m
for r, c in sheep:
    sheep_rows[c] = r

ans3 = 0
State = namedtuple("state", "dragon n_sheep sheep_rows")
states = Counter()
states[State(dragon, len(sheep), tuple(sheep_rows))] = 1
while states:

    # sheep moves
    states_new = Counter()
    for state, cnt in states.items():
        options = []
        can_escape = False
        for c in range(m):
            if state.sheep_rows[c] != -1:
                if state.sheep_rows[c] + 1 >= n:
                    can_escape = True
                elif (state.sheep_rows[c] + 1, c) in hides or (state.sheep_rows[c] + 1, c) != state.dragon:
                    sheep_rows_new = list(state.sheep_rows)
                    sheep_rows_new[c] += 1
                    options.append(tuple(sheep_rows_new))

        if not options and not can_escape:
            options.append(state.sheep_rows)
        for sheep_rows_new in options:
            states_new[State(state.dragon, state.n_sheep, sheep_rows_new)] += cnt
    states = states_new

    # dragon move
    states_new = Counter()
    for state, cnt in states.items():
        for dragon_new in dragon_moves(state.dragon, n, m):
            sheep_rows_new = list(state.sheep_rows)
            n_sheep_new = state.n_sheep
            if dragon_new not in hides:
                for c in range(m):
                    if (sheep_rows_new[c], c) == dragon_new:
                        n_sheep_new -= 1
                        sheep_rows_new[c] = -1
            if n_sheep_new == 0:
                ans3 += cnt
            else:
                states_new[State(dragon_new, n_sheep_new, tuple(sheep_rows_new))] += cnt
    states = states_new

print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
