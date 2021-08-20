username_number = int(input())
usernames = set()

for _ in range(username_number):
    name = input()
    usernames.add(name)

username_list = list(usernames)
for i in range(usernames.__len__()):
    print(username_list[i])