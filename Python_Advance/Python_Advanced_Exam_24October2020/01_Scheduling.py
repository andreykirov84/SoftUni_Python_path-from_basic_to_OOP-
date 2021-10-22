jobs = [int(x) for x in input().split(', ')]
target_index = int(input())
cycles_needed = 0
for i in range(jobs[target_index] + 1):
    while i in jobs:
        idx = jobs.index(i)
        cycles_needed += jobs.pop(idx)

print(cycles_needed)
