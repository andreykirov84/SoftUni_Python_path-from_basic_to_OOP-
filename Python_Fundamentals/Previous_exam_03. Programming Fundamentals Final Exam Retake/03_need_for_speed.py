def sorted_by_value_descending_key_ascending(dd):
    return dict(sorted(dd.items(), key=lambda x: (-x[1][0], x[0])))


MAX_FUEL = 75

cars_dict = {}
car_number = int(input())
for _ in range(car_number):
    line_input = input().split('|')
    car = line_input[0]
    mileage = int(line_input[1])
    fuel = int(line_input[2])
    cars_dict.update({car: [mileage, fuel]})

while True:
    command = input().split(' : ')
    if command[0] == 'Stop':
        break

    elif command[0] == 'Drive':
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        old_mileage, old_fuel = cars_dict[car][0], cars_dict[car][1]
        if old_fuel < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars_dict.update({car: [old_mileage + distance, old_fuel - fuel]})
            if old_mileage + distance >= 100000:
                cars_dict.pop(car)
                print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
                print(f"Time to sell the {car}!")
            else:
                cars_dict.update({car: [old_mileage + distance, old_fuel - fuel]})
                print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

    elif command[0] == 'Refuel':
        car = command[1]
        fuel = int(command[2])
        old_mileage, old_fuel = cars_dict[car][0], cars_dict[car][1]
        if old_fuel + fuel > MAX_FUEL:
            fuel = MAX_FUEL - old_fuel
            old_fuel = MAX_FUEL
        else:
            old_fuel += fuel
        cars_dict.update({car: [old_mileage, old_fuel]})
        print(f"{car} refueled with {fuel} liters")

    elif command[0] == 'Revert':
        car = command[1]
        kilometers = int(command[2])
        old_mileage, old_fuel = cars_dict[car][0], cars_dict[car][1]
        if old_mileage - kilometers < 10000:
            old_mileage = 10000
            cars_dict.update({car: [old_mileage, old_fuel]})
        else:
            old_mileage -= kilometers
            cars_dict.update({car: [old_mileage, old_fuel]})
            print(f"{car} mileage decreased by {kilometers} kilometers")

cars_dict = sorted_by_value_descending_key_ascending(cars_dict)

for car in cars_dict:
    mileage = cars_dict[car][0]
    fuel = cars_dict[car][1]
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")

