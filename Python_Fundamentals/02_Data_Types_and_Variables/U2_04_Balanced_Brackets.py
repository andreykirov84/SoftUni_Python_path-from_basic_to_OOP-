lines = int(input())
open_brackets = 0
close_brackets = 0
flag = True
for _ in range(lines):
    input_string = input()
    if input_string == '(':
        open_brackets += 1
    if input_string == ')':
        close_brackets += 1
    if open_brackets > close_brackets + 1:
        flag = False
        break

if open_brackets != close_brackets:
    flag = False

if flag:
    print('BALANCED')
else:
    print('UNBALANCED')
