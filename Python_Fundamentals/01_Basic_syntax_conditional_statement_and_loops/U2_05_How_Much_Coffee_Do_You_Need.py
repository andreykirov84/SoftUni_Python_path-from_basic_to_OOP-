command = input()
coffee = 0
lowercase_command = ['coding', 'dog', 'cat', 'movie']
uppercase_command = ['CODING', 'DOG', 'CAT', 'MOVIE']
while command != 'END':
    if command in lowercase_command:
        coffee += 1
    elif command in uppercase_command:
        coffee += 2
    command = input()

if coffee > 5:
    print('You need extra sleep')
else:
    print(coffee)
