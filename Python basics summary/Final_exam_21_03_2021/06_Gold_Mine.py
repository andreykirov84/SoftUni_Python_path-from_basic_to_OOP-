locations = int(input())

for _ in range(locations):
    expected_yield = float(input())
    days = int(input())
    total_yield = 0
    yield_per_day = 0
    average_daily_yield = 0

    for _ in range(days):
        yield_per_day = float(input())
        total_yield += yield_per_day
        average_daily_yield = total_yield / days

    if expected_yield <= average_daily_yield:
        print(f"Good job! Average gold per day: {average_daily_yield:.2f}.")
    else:
        print(f"You need {expected_yield - average_daily_yield:.2f} gold.")
