fruit = ['banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes']
vegetable = ['tomato', 'cucumber', 'pepper', 'carrot']

food = input()

if food in fruit:
    print('fruit')
elif food in vegetable:
    print('vegetable')
else:
    print("unknown")
