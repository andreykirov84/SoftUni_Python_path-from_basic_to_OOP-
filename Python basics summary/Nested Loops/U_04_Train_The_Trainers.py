n = int(input())
ll_marks = []
ll_final_marks =[]
task_name = input()
number_of_tasks = 0
average_mark = None
while task_name != "Finish":
    for _ in range(n):
        mark = float(input())
        ll_marks.append(mark)
        average_mark = sum(ll_marks) / n
    print(f'{task_name} - {average_mark:.2f}.')
    ll_final_marks.append(average_mark)
    number_of_tasks += 1
    ll_marks = []
    average_mark = None
    task_name = input()
print(f"Student's final assessment is {sum(ll_final_marks) / number_of_tasks:.2f}.")
