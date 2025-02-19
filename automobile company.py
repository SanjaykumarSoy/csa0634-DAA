import numpy as np
from itertools import permutations
times = np.array([[5, 9, 3], [6, 8, 4], [7, 6, 5]])
transfers = np.array([[0, 2, 3], [2, 0, 4], [3, 4, 0]])
dependencies = [(0, 1), (1, 2)]
def total_time(schedule):
    time = 0
    for i in range(len(schedule) - 1):
        time += times[schedule[i]][i] + transfers[schedule[i]][schedule[i + 1]]
    return time + times[schedule[-1]][len(schedule) - 1]
min_time = float('inf')
best_schedule = None
for perm in permutations(range(3)):
    if all(perm.index(dep[0]) < perm.index(dep[1]) for dep in dependencies):
        current_time = total_time(perm)
        if current_time < min_time:
            min_time = current_time
            best_schedule = perm

print(f"Optimal Schedule: {best_schedule}, Minimum Time: {min_time}")
