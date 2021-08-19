command = input().split(' ')
first = command[0]
second = command[1]
total_sum = 0
if len(second) < len(first):    # first is always not longer than second
    first, second = second, first

for i in range(len(first)):
    total_sum += ord(first[i]) * ord(second[i])

for j in range(len(first), len(second)):
    total_sum += ord(second[j])

print(total_sum)