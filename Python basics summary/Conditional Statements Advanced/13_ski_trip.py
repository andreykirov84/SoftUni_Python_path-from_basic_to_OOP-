rooms = {
    'room for one person': [18, 18, 18],
    'apartment': [17.50, 16.25, 12.50],
    'president apartment': [31.50, 29.75, 28],
    }

days = int(input())
room_type = input()
feedback = input()
nights = days - 1
index = None
room_price = None

if days < 0:
    index = 0
elif 10 <= days <= 15:
    index = 1
else:
    index = 2

if feedback == 'positive':
    room_price = rooms[room_type][index] * 1.25
elif feedback == 'negative':
    room_price = rooms[room_type][index] * 0.9


print(f'{room_price * nights:.2f}')
