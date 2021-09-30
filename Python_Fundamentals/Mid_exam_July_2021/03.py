messages = []
command = input().split()
while command[0] != 'end':
    if command[0] == 'Chat':
        text = command[1]
        messages.append(text)
        command = input().split()

    elif command[0] == 'Delete':
        text = command[1]
        if text in messages:
            messages.remove(text)
        command = input().split()

    elif command[0] == 'Edit':
        old_text = command[1]
        if old_text in messages:
            text_index = messages.index(old_text)
            new_text = command[2]
            messages[text_index] = new_text
        command = input().split()

    elif command[0] == 'Pin':
        text = command[1]
        if text in messages:
            text_index = messages.index(text)
            item = messages.pop(text_index)
            messages.append(item)
        command = input().split()

    elif command[0] == 'Spam':
        messages += command[1:]
        command = input().split()

print(*messages, sep='\n')
