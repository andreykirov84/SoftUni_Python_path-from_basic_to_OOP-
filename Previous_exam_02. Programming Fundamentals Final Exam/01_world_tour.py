text = input()

while True:
    command = input().split(":")
    if command[0] == 'Travel':
        break
    elif command[0] == 'Add Stop':
        insert_index = int(command[1])
        insert_string = command[2]
        if insert_index < len(text):
            text = text[:insert_index] + insert_string + text[insert_index:]
            print(text)
        else:
            print(text)

    elif command[0] == 'Remove Stop':
        start_remove_index = int(command[1])
        end_remove_index = int(command[2])
        if start_remove_index < len(text) and end_remove_index < len(text):
            text = text[:start_remove_index] + text[end_remove_index + 1:]
            print(text)
        else:
            print(text)

    elif command[0] == 'Switch':
        old_string = command[1]
        new_string = command[2]
        if old_string in text:
            text = text.replace(old_string, new_string)
            print(text)
        else:
            print(text)

print(f"Ready for world tour! Planned stops: {text}")
