# students = {}
# command = input().split(':')
# while len(command) != 1:
#     name = command[0]
#     id_number = command[1]
#     course = command[2]
#     if course in students:
#         students[course] += [name, id_number]
#     else:
#         students[course] = [name, id_number]
#     command = input().split(':')
#
#
# ll = students[command[0]]
# for i in range(0, len(ll), 2):
#     print(f'{ll[i]} - {ll[i+1]}')

students = {}
command = input()

while ":" in list(command):
    command = command.split(":")
    name = command[0]
    id_number = command[1]
    course = command[2]
    if course in students:
        students[course] += [name, id_number]
    else:
        students[course] = [name, id_number]
    command = input()


ll = students[command]
for i in range(0, len(ll), 2):
    print(f'{ll[i]} - {ll[i+1]}')
