raw_password = input()
command = input().split(' ')

while command[0] != 'Done':
    if command[0] == 'TakeOdd':
        new_password = ''
        for number in range(1, len(raw_password), 2):
            new_password += raw_password[number]
        print(new_password)
        raw_password = new_password
        command = input().split(' ')

    elif command[0] == 'Cut':
        cut_index = int(command[1])
        length_index = int(command[2])
        substring = raw_password[cut_index:cut_index + length_index]
        raw_password = raw_password.replace(substring, '', 1)  # replace the first occurrence of substring with empty one
        print(raw_password)
        command = input().split(' ')

    elif command[0] == 'Substitute':
        substitute_string = command[1]
        new_string = command[2]
        if substitute_string in raw_password:
            raw_password = raw_password.replace(substitute_string, new_string)
            print(raw_password)
            command = input().split(' ')
        else:
            print(f"Nothing to replace!")
            command = input().split(' ')

print(f"Your password is: {raw_password}")

