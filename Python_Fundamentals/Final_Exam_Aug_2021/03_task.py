def sorted_by_value_descending_key_ascending(dd):
    return dict(sorted(dd.items(), key=lambda x: (-x[1][1], x[0])))


users_dd = {}
MAX_MESSAGES = int(input())

while True:
    command = input().split('=')
    if command[0] == 'Statistics':
        break

    elif command[0] == 'Add':
        username = command[1]
        sent_number = int(command[2])
        received_number = int(command[3])
        if username not in users_dd:
            users_dd[username] = [sent_number, received_number]
            # users_dd.update({username: [sent_number, received_number]})

    elif command[0] == 'Message':
        sender = command[1]
        receiver = command[2]
        if sender in users_dd and receiver in users_dd:
            sender_sent_number = users_dd[sender][0] + 1
            sender_received_number = users_dd[sender][1]
            receiver_sent_number = users_dd[receiver][0]
            receiver_received_number = users_dd[receiver][1] + 1
            if sender_sent_number + sender_received_number == MAX_MESSAGES:
                print(f"{sender} reached the capacity!")
                users_dd.pop(sender)
            else:
                users_dd.update({sender: [sender_sent_number, sender_received_number]})
            if receiver_received_number + receiver_sent_number == MAX_MESSAGES:
                print(f"{receiver} reached the capacity!")
                users_dd.pop(receiver)
            else:
                users_dd.update({receiver: [receiver_sent_number, receiver_received_number]})

    elif command[0] == 'Empty':
        username = command[1]
        if username == 'All':
            users_dd = {}
            # for user in users_dd:
            #     users_dd.update({user: [0, 0]})
        else:
            users_dd.pop(username)

for user in users_dd:
    users_dd[user].append(users_dd[user][0] + users_dd[user][1])


users_dd = sorted_by_value_descending_key_ascending(users_dd)

print(f'Users count: {len(users_dd.keys())}')
for user in users_dd:
    print(f'{user} - {users_dd[user][2]}')





