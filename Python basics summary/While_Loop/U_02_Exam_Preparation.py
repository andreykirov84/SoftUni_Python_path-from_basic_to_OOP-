max_bad_marks = int(input())
last_problem = None
problems = 0
poor_mark = 4
poor_mark_number = 0
ll = []
while True:
    problem_name = input()
    if problem_name != 'Enough':
        problem_mark = int(input())
        if problem_mark > poor_mark:
            last_problem = problem_name
            ll.append(problem_mark)
            problems += 1
        else:
            poor_mark_number += 1
            if problems == max_bad_marks:
                print(f"You need a break, {max_bad_marks} poor grades.")
                break
            else:
                last_problem = problem_name
                ll.append(problem_mark)
                problems += 1
    else:
        average_score = sum(ll) / len(ll)
        print(f"Average score: {average_score:.2f}")
        print(f"Number of problems: {problems}")
        print(f"Last problem: {last_problem}")
        break
