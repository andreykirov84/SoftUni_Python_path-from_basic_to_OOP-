from collections import deque

people = deque()
while True:
    command = input()
    if command == 'End':
        break
    elif command == 'Paid':
        print(*people, sep='\n')
        people = deque()
    else:
        people.append(command)

print(f'{len(people)} people remaining.')
