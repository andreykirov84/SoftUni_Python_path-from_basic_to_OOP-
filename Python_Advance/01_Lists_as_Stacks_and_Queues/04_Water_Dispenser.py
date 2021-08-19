from collections import deque


def water_dispenser():
    water = int(input())
    people = deque()
    while True:
        command = input()
        if command == "Start":
            break
        people.append(command)

    while True:
        command = input().split(' ')
        if command[0] == "End":
            break
        elif command[0] == "refill":
            water += int(command[1])
        else:
            person_water = int(command[0])
            person = people.popleft()
            if person_water <= water:
                water -= person_water
                print(f'{person} got water')
            else:
                print((f'{person} must wait'))
    print(f'{water} liters left')


water_dispenser()
