steps_goal = 10000
current_steps = 0
while True:
    steps = input()
    if steps != "Going home":
        steps = int(steps)
        current_steps += steps
        if current_steps >= steps_goal:
            print("Goal reached! Good job!")
            print(f"{current_steps - steps_goal} steps over the goal!")
            break
    else:
        last_steps = int(input())
        current_steps += last_steps
        if current_steps >= steps_goal:
            print("Goal reached! Good job!")
            print(f"{current_steps - steps_goal} steps over the goal!")
            break
        else:
            print(f"{steps_goal - current_steps} more steps to reach goal.")
            break
