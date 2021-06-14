total_number = 0
ll = input()

if len(ll) != 0:
    ll = ll.split(' ')

for item in ll:
    if len(item) > 0:
        first_letter = item[0]
        last_letter = item[-1]
        number = int(item[1:-1])
        result_number = 0
        if first_letter.isupper():
            result_number = number / (ord(first_letter) - 64)
        else:
            result_number = number * (ord(first_letter) - 96)

        if last_letter.isupper():
            total_number += result_number - (ord(last_letter) - 64)
        else:
            total_number += result_number + (ord(last_letter) - 96)

print(f'{round(total_number, 2):.2f}')

