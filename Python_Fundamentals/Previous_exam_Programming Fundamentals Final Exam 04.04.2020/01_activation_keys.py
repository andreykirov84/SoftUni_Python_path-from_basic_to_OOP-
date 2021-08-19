raw_activation_key = input()
command = input().split('>>>')
while command[0] != 'Generate':
    if command[0] == 'Contains':
        substring = command[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
            command = input().split('>>>')
        else:
            print("Substring not found!")
            command = input().split('>>>')

    elif command[0] == 'Flip':
        start_index = int(command[2])
        end_index = int(command[3])
        if command[1] == 'Upper':
            changed_slice = raw_activation_key[start_index:end_index].upper()
        else:
            changed_slice = raw_activation_key[start_index:end_index].lower()

        raw_activation_key = raw_activation_key[:start_index] + changed_slice + raw_activation_key[end_index:]
        print(raw_activation_key)
        command = input().split('>>>')

    elif command[0] == 'Slice':
        start_index = int(command[1])
        end_index = int(command[2])
        raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[end_index:]
        print(raw_activation_key)
        command = input().split('>>>')

print(f"Your activation key is: {raw_activation_key}")

