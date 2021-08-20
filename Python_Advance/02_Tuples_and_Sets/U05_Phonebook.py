phonebook = {}
name_count = 0
while True:
    text = input().split('-')
    if len(text[0]) == 1:
        name_count = int(text[0])
        break
    else:
        name = text[0]
        tel_number = text[1]
        phonebook[name] = tel_number

for _ in range(name_count):
    name = input()
    if name not in phonebook:
        print(f"Contact {name} does not exist.")
    else:
        print(f"{name} -> {phonebook[name]}")


