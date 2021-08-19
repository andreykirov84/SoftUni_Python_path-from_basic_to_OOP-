from collections import deque

success_flag = True
text = deque(input())

brackets = {'{': '}', '[': ']', '(': ')'}

while len(text) > 1:
    first_bracket = text.popleft()
    second_bracket = text.pop()
    if brackets[first_bracket] != second_bracket:
        success_flag = False
        break

if success_flag:
    print('YES')
else:
    print('NO')
