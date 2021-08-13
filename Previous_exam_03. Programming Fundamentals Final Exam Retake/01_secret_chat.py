text = input()
command = input().split(':|:')
while command[0] != 'Reveal':
    if command[0] == 'InsertSpace':
        text_index = int(command[1])
        text = text[:text_index] + ' ' + text[text_index:]
        print(text)
        command = input().split(':|:')

    elif command[0] == "Reverse":
        substring = command[1]
        if substring in text:
            text = text.replace(substring, '', 1)
            text += substring[::-1]
            print(text)
            command = input().split(':|:')
        else:
            print("error")
            command = input().split(':|:')

    elif command[0] == 'ChangeAll':
        substring = command[1]
        replacement_text = command[2]
        text = text.replace(substring, replacement_text)
        print(text)
        command = input().split(':|:')

print(f"You have a new text message: {text}")
