""" 1. My first solution - 60% in judge system"""
year = input()
while len(list(year)) != len(set(year)):
    year = str(int(year) + 1)

print(year)
"""2. My second  solution - 100% """
input_year = int(input())
next_year = input_year + 1
next_happy_year = ""
brake_first_loop = False
while True:
    str_next_year = str(next_year)
    next_happy_year = str_next_year[0]
    for i in range(1, len(str_next_year)):
        for j in range(0, i):
            if str_next_year[i] == next_happy_year[j]:
                brake_first_loop = True
                break
        if brake_first_loop:
            break
        else:
            next_happy_year = next_happy_year + str_next_year[i]
    if len(next_happy_year) == len(str_next_year):
        break
    next_happy_year = ""
    brake_first_loop = False
    next_year += 1
print(next_happy_year)
