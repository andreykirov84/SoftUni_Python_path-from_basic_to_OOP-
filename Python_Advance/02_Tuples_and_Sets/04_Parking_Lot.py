cars = int(input())
cars_list = {}

for _ in range(cars):
    cars_name = input().split(', ')
    direction = cars_name[0]
    registration = cars_name[1]

    if direction == "IN":
        cars_list[registration] = 1
    else:
        cars_list.pop(registration)

final_list = (cars_list.keys())
if len(final_list) == 0:
    print('Parking Lot is Empty')
else:
    for key in cars_list.keys():
        print(key)