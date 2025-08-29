from time import time

overall_start = time()

quests = ["q01", "q02v2", "q03"]

for quest_id, quest in enumerate(quests, start = 1):
    print(f"Quest {quest_id}")
    exec(open(f"./TheEntertainmentHub/{quest}.py").read())
    print(f"running time so far: {time() - overall_start:.3f}s")
    print()

print(f"total running time: {time() - overall_start:.3f}s")