from collections import deque

people = deque(input().split(' '))
number = int(input())

while len(people) > 1:
    counter = number
    while counter > 0:
        child = people.popleft()
        people.append(child)
        counter -= 1
    print(f'Removed {people.pop()}')

print(f'Last is {people.pop()}')



