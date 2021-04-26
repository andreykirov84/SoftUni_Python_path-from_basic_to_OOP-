budget = float(input())
season = input()
destination = None
overnight_stay = None
budget_percent = None
if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        overnight_stay = 'Camp'
        budget_percent = 0.3
    else:
        overnight_stay = 'Hotel'
        budget_percent = 0.7
elif budget > 1000:
    destination = 'Europe'
    overnight_stay = 'Hotel'
    budget_percent = 0.9

else:
    destination = 'Balkans'
    if season == 'summer':
        overnight_stay = 'Camp'
        budget_percent = 0.4
    else:
        overnight_stay = 'Hotel'
        budget_percent = 0.8

print(f"Somewhere in {destination}")
print(f'{overnight_stay} - {budget * budget_percent:.2f}')

