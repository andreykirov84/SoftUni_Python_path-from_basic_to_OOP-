total_time = int(input())
scene_number = int(input())
scene_time = int(input())
preparation_time = 0.15*total_time

required_time = preparation_time + scene_time * scene_number

if required_time > total_time:
    razlika = round(required_time - total_time)
    print(f'Time is up! To complete the movie you need {razlika} minutes.')

else:
    razlika = round(total_time - required_time)
    print(f'You managed to finish the movie on time! You have {razlika} minutes left!')
