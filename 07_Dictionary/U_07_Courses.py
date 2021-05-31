def sort_dict_by_value_len(dict_):
    return sorted(dict_.items(), key=lambda kv: (len(kv[1]), kv[0]))


def sorted_by_decreased_value(dict):
    # return sorted(dict.items(), key=lambda t: t[::-1], reverse=True)
    value_key_pairs = ((value, key) for (key, value) in dict.items())
    sorted_value_key_pairs = sorted(value_key_pairs, reverse=True)
    return sorted_value_key_pairs

def sorted_by_increased_value(dict):
    return sorted(dict.items(), key=lambda t: t[::-1])


"""filling the dictionary with data"""
command = input()
courses = {}
while command != 'end':
    command = command.split(' : ')
    if command[0] not in courses:
        courses.update({command[0]: [command[1]] })
    else:
        student = courses.get(command[0])
        student.append(command[1])
    command = input()

"""Sorting the dictionary"""
sort_dict_by_value_len(courses)
new_dict = {}
for key, value in courses.items():
    new_dict.update({key: len(value)})
ordered_list = sorted_by_decreased_value(new_dict)


"""Print the data"""
for sublist in ordered_list:
    key = sublist[1]
    student_number = sublist[0]
    print(f"{key}: {student_number}")
    student_list = courses.get(key)
    student_list.sort()
    for student in student_list:
        print(f'-- {student}')
