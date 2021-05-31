def sorted_by_decreased_value(dict):
    return {k: v for k, v in sorted(dict.items(), reverse=True, key=lambda item: item[1])}


students = {}
pop_students = []

for _ in range(int(input())):
    name = input()
    mark = float(input())
    if name in students:
        students.get(name).append(mark)
    else:
        students.update({name: [mark]})

for key, value in students.items():
    average = sum(value) / len(value)
    if average >= 4.50:
        students.update({key: average})
    else:
        pop_students.append(key)

for key in pop_students:
    students.pop(key)

print(students)
print(sorted_by_decreased_value(students))
[print(f'{key} -> {value:.2f}') for key, value in sorted_by_decreased_value(students).items()]
