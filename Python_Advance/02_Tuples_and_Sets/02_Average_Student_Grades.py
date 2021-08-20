people = int(input())
students_mark = {}
for _ in range(people):
    student_name = input().split(' ')
    name = student_name[0]
    mark = float(student_name[1])

    if name not in students_mark.keys():
        students_mark[name] = [mark]
    else:
        students_mark[name].append(mark)

for name in students_mark.keys():
    average = format(sum(students_mark[name]) / len(students_mark[name]), '.2f')
    # ocenka = [students_mark[name]]
    print(f'{name} -> {" ".join(format(x, ".2f") for x in students_mark[name])} (avg: {average})')