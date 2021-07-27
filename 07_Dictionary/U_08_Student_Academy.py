def value_key_sorted_dict(dd):
    return sorted(dd.items(), key=lambda x: (x[1]), reverse=True)


def average(lst):
    return sum(lst) / len(lst)


student_dict = {}

for _ in range(int(input())):
    name = input()
    mark = float(input())
    if name not in student_dict:
        student_dict[name] = [mark]
    else:
        student_dict[name] += [mark]

for name in student_dict:
    all_marks = student_dict[name]
    average_mark = average(all_marks)
    student_dict[name] = average_mark

student_dict = dict(value_key_sorted_dict(student_dict))

for name in student_dict:
    if student_dict[name] >= 4.50:
        print(f'{name} -> {student_dict[name]:.2f}')

