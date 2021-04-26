week = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday',
}


def is_valid(number):
    if number in week.keys():
        return True


input_value = int(input())
if is_valid(input_value):
    print(week[input_value])
else:
    print('Error')
