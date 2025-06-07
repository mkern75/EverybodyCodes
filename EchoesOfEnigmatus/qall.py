from time import time

overall_start = time()

for quest in range(1, 4):
    print(f"Quest {quest}")
    exec(open(f"./EchoesOfEnigmatus/q{quest:02d}.py").read())
    print(f"running time so far: {time() - overall_start:.3f}s")
    print()

print(f"total running time: {time() - overall_start:.3f}s")