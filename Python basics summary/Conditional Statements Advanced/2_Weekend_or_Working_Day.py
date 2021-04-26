week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

weekend = ['Saturday', 'Sunday']

day = input()

if day in week:
    print("Working day")
elif day in weekend:
    print("Weekend")
else:
    print("Error")
