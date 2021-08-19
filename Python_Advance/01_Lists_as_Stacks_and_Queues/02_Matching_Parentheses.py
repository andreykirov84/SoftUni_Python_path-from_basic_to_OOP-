text = input()
opening = []
for i in range(len(text)):
    if text[i] == '(':
        opening.append(i)
    elif text[i] == ')':
        print(text[opening.pop():i+1])

