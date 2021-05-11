key = int(input())
number = int(input())
message = ''
for _ in range(number):
    ascii_number = ord(input()) + key
    message += chr(ascii_number)

print(message)
