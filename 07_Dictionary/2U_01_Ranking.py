def sorted_by_value_descending_key_ascending(dd):
    return dict(sorted(dd.items(), key=lambda x: (-x[1], x[0])))


contest_dict = {}
students_dict = {}

while True:
    command = input().split(':')
    if command[0] == 'end of contests':
        break
    else:
        contest = command[0]
        contest_password = command[1]
        contest_dict.update({contest: contest_password})

while True:
    command = input().split('=>')
    if command[0] == 'end of submissions':
        break
    else:
        contest = command[0]
        password = command[1]
        username = command[2]
        score = int(command[3])
        if contest in contest_dict and password == contest_dict[contest]:
            if username not in students_dict:
                students_dict[username][contest] = score
            else:
                if contest not in students_dict[username]:
                    students_dict[username][contest] = score
                else:
                    old_score = students_dict[username][contest]
                    if score > old_score:
                        students_dict[username][contest] = score

print(students_dict)





