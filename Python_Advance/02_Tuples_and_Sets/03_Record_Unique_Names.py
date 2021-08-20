people = int(input())
people_list = []

for _ in range(people):
    name = input()
    if name not in people_list:
        people_list.append(name)

for i in range(len(people_list)):
    print(people_list[i])