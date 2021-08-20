text = input().split(' ')
text = [float(x) for x in text]

already_count = []
for number in text:
    if number not in already_count:
        print(f'{number} - {text.count(number)} times')
        already_count.append(number)
