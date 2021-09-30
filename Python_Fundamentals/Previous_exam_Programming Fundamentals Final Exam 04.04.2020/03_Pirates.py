def sorted_by_value_descending_key_ascending(dd):
    return dict(sorted(dd.items(), key=lambda x: (-x[1][1], x[0])))


cities = {}
command = input().split('||')
while command[0] != 'Sail':
    city = command[0]
    population = int(command[1])
    gold = int(command[2])
    if city not in cities:
        cities.update({city: [population, gold]})
        command = input().split('||')
    else:
        old_population = cities[city][0]
        old_gold = cities[city][1]
        new_population = old_population + population
        new_gold = old_gold + gold
        cities.update({city: [new_population, new_gold]})
        command = input().split('||')

command = input().split('=>')
while command[0] != 'End':
    if command[0] == 'Plunder':
        city = command[1]
        people = int(command[2])
        gold = int(command[3])
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
        old_population = cities[city][0]
        old_gold = cities[city][1]
        new_population = old_population - people
        new_gold = old_gold - gold
        if new_population > 0 and new_gold > 0:
            cities.update({city: [new_population, new_gold]})
            command = input().split('=>')
        else:
            cities.pop(city)
            print(f'{city} has been wiped off the map!')
            command = input().split('=>')
    elif command[0] == 'Prosper':
        city = command[1]
        gold = int(command[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
            command = input().split('=>')
        else:
            old_population = cities[city][0]
            old_gold = cities[city][1]
            new_gold = old_gold + gold
            cities.update({city: [old_population, new_gold]})
            print(f"{gold} gold added to the city treasury. {city} now has {new_gold} gold.")
            command = input().split('=>')

sorted_cities = sorted_by_value_descending_key_ascending(cities)
if len(sorted_cities.keys()) > 0:
    print(f'Ahoy, Captain! There are {len(sorted_cities.keys())} wealthy settlements to go to:')
    for city in sorted_cities:
        citizens = sorted_cities[city][0]
        gold = sorted_cities[city][1]
        print(f'{city} -> Population: {citizens} citizens, Gold: {gold} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
