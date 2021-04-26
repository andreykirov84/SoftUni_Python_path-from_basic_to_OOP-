import math

breed_life = {
    'British Shorthair': [13, 14],
    'Siamese': [15, 16],
    'Persian': [14, 15],
    'Ragdoll': [16, 17],
    'American Shorthair': [12, 13],
    'Siberian': [11, 12],
}
index = None

cat_breed = input()
if cat_breed not in breed_life.keys():
    print(f'{cat_breed} is invalid cat!')
else:
    cat_sex = input()
    if cat_sex == 'm':
        index = 0
    else:
        index = 1
    cat_months = breed_life[cat_breed][index] * 2

    print(f"{math.floor(cat_months)} cat months")

