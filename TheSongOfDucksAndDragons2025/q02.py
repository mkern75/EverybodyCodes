from time import time

# ********************************* part 1
time_start = time()


def add(u, v):
    return u[0] + v[0], u[1] + v[1]


def multiply(u, v):
    return u[0] * v[0] - u[1] * v[1], u[0] * v[1] + u[1] * v[0]


def divide(u, v):
    assert v[0] > 0 and v[1] > 0
    x = u[0] // v[0] if u[0] >= 0 else -(-u[0] // v[0])
    y = u[1] // v[1] if u[1] >= 0 else -(-u[1] // v[1])
    return x, y


INPUT_FILE = "./data/q02_p1.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

a = tuple(map(int, data[0][3:-1].split(",")))
ans1 = (0, 0)
for _ in range(3):
    ans1 = multiply(ans1, ans1)
    ans1 = divide(ans1, (10, 10))
    ans1 = add(ans1, a)
print(f"part 1: [{ans1[0]},{ans1[1]}]  ({time() - time_start:.3f}s)")

# ********************************* part 2
time_start = time()


def engrave(a, b, sz):
    res = 0
    for r in range(sz):
        x = a[0] + (b[0] - a[0]) * r // (sz - 1)
        for c in range(sz):
            y = a[1] + (b[1] - a[1]) * c // (sz - 1)
            z = (x, y)
            r = (0, 0)
            ok = True
            for _ in range(100):
                r = multiply(r, r)
                r = divide(r, (100_000, 100_000))
                r = add(r, z)
                if not (-1000000 <= r[0] <= 1000000) or not (-1000000 <= r[1] <= 1000000):
                    ok = False
                    break
            if ok:
                res += 1
    return res


INPUT_FILE = "./data/q02_p2.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

a = tuple(map(int, data[0][3:-1].split(",")))
b = add(a, (1000, 1000))
ans2 = engrave(a, b, 101)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

# ********************************* part 3
time_start = time()
INPUT_FILE = "./data/q02_p3.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

a = tuple(map(int, data[0][3:-1].split(",")))
b = add(a, (1000, 1000))
ans3 = engrave(a, b, 1001)
print(f"part 3: {ans3}  ({time() - time_start:.3f}s)")
