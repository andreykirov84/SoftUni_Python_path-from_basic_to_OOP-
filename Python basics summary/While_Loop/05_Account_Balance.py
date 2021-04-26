balance = 0
end_word = 'NoMoreMoney'
number = input()
is_proper = True
while is_proper:
    if number == end_word:
        is_proper = False
    else:
        number = float(number)
        if number < 0:
            print("Invalid operation!")
            break
        else:
            balance += number
            print(f'Increase: {number:.2f}')
        number = input()
print(f'Total: {balance:.2f}')
