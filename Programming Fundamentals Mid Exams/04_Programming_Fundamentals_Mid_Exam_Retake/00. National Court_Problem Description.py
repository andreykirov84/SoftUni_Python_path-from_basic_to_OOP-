import math

first = int(input())
second = int(input())
third = int(input())
people = int(input())

total_people_per_hour = first + second + third
time = math.ceil(people / total_people_per_hour)
if time % 3 == 0:
    breaks = time // 3 - 1
else:
    breaks = time // 3

time += breaks

print(f"Time needed: {time}h.")


