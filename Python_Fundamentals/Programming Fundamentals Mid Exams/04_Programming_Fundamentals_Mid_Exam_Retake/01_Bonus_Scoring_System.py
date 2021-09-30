import math

students = int(input())
lectures = int(input())
initial_bonus = int(input())
max_bonus = 0
student_lectures = 0

for _ in range(students):
    student_attendances = int(input())
    total_bonus = student_attendances / lectures * (5 + initial_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        student_lectures = student_attendances

print(f'Max Bonus: {math.ceil(max_bonus)}.')
print(f'The student has attended {student_lectures} lectures.')
