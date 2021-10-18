import os

while True:
    command = input().split('-')
    command_type = command[0]
    if command_type == 'End':
        break

    file_name = command[1]

    if command_type == 'Create':
        open(file_name, 'w').close()

    elif command_type == 'Add':
        content = command[2]
        with open(file_name, 'a') as file:
            file.write(content)
            file.write('\n')

    elif command_type == 'Replace':
        old_string = command[2]
        new_string = command[3]
        if os.path.exists(file_name):
            with open(file_name, 'r+') as file:
                text = file.read().replace(old_string, new_string)
                file.truncate(0)
                file.write(text)
        else:
            print(f"An error occurred")

    elif command_type == 'Delete':
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print(f"An error occurred")


