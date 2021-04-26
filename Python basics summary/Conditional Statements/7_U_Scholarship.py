from math import floor

income = float(input())
average_mark = float(input())
min_income = float(input())
social_scholarship_money = 0.35 * min_income
excellent_scholarship_money = average_mark * 25


def social_scholarship():
    if income < min_income and average_mark >= 4.5:
        return True


def excellent_scholarship():
    if average_mark >= 5.5:
        return True


if social_scholarship() and excellent_scholarship():
    if social_scholarship_money > excellent_scholarship_money:
        print(f'You get a Social scholarship {floor(social_scholarship_money)} BGN')
    else:
        print(f'You get a scholarship for excellent results {floor(excellent_scholarship_money)} BGN')

elif social_scholarship():
    print(f'You get a Social scholarship {floor(social_scholarship_money)} BGN')

elif excellent_scholarship():
    print(f'You get a scholarship for excellent results {floor(excellent_scholarship_money)} BGN')

else:
    print("You cannot get a scholarship!")

