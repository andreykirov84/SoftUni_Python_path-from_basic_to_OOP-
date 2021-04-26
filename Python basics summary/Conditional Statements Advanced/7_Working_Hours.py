working_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
hour = int(input())
day = input()
if 10 <= hour <= 18 and day in working_days:
    print('open')
else:
    print('closed')
