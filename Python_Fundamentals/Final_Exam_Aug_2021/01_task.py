text = input()

while True:
    command = input().split(' ')
    if command[0] == 'End':
        break

    elif command[0] == 'Translate':
        replace_text = command[1]
        replacement = command[2]
        text = text.replace(replace_text, replacement)
        print(text)

    elif command[0] == 'Includes':
        included_string = command[1]
        if included_string in text:
            print('True')
        else:
            print('False')

    elif command[0] == 'Start':
        included_string = command[1]
        print(text.startswith(included_string))

    elif command[0] == 'Lowercase':
        text = text.lower()
        print(text)

    elif command[0] == 'FindIndex':
        print(text.rfind(command[1]))

    elif command[0] == 'Remove':
        start_index = int(command[1])
        count = int(command[2])
        text = text[:start_index] + text[start_index + count:]
        print(text)

