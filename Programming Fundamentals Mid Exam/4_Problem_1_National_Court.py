first = int(input())
second = int(input())
third = int(input())
total_people = int(input())
people_per_hour = first + second + third
breaks = total_people // (people_per_hour * 3)
if total_people % people_per_hour != 0:
    time_needed = total_people // people_per_hour + 1 + breaks
else:
    time_needed = total_people // people_per_hour + breaks
print(f'Time needed: {time_needed}h.')
