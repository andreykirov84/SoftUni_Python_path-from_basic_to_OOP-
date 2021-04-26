total_food_g = int(input()) * 1000
eat = 0
command = input()
while command != 'Adopted':
    ration = int(command)
    eat += ration
    command = input()
if total_food_g >= eat:
    print(f"Food is enough! Leftovers: {total_food_g - eat} grams.")
else:
    print(f"Food is not enough. You need {eat - total_food_g} grams more.")
