""" sort dictionary by increased value (by def), or by decreased value if decreased = True. If we have 2 equal values
they will be sorted also by key (alphabetically) if equal_alphabetic_sort=True (by def)"""


def sort_dict_by_value(dict, decreased=False, equal_alphabetic_sort=True):
    dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=decreased)}
    value_key_pairs = ((value, key) for (key, value) in dict.items())
    sorted_value_key_pairs = sorted(value_key_pairs, reverse=decreased)
    if equal_alphabetic_sort:
        for i in range(0, len(sorted_value_key_pairs) - 1):
            if sorted_value_key_pairs[i][1] > sorted_value_key_pairs[i + 1][1]:
                sorted_value_key_pairs[i], sorted_value_key_pairs[i + 1] = sorted_value_key_pairs[i + 1], \
                                                                           sorted_value_key_pairs[i]
    return {k: v for v, k in sorted_value_key_pairs}


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
len_dict = {}
for key, value in courses.items():
    len_dict.update({key: len(value)})
print(len_dict)
ordered_list = sorted_by_decreased_value(len_dict)
print(ordered_list)

"""Print the data"""
for sublist in ordered_list:
    key = sublist[1]
    student_number = sublist[0]
    print(f"{key}: {student_number}")
    student_list = courses.get(key)
    student_list.sort()
    for student in student_list:
        print(f'-- {student}')

