expected_guests_number = int(input())
expected_guests = set()

for _ in range(expected_guests_number):
    name = input()
    expected_guests.add(name)


while True:
    guests = input()
    if guests != 'END':
        expected_guests.remove(guests)
    else:
        expected_guests_list = sorted(list(expected_guests))
        print(len(expected_guests_list))
        for i in range(len(expected_guests_list)):
            print(expected_guests_list[i])
        break