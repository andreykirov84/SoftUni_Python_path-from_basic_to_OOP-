# def value_key_sorted_dict(dd):
#     return sorted(dd.items(), key=lambda x: (x[1], x[0]), reverse=True)
#
#
# forcedict = {}
#
# command = input()
# while command != 'Lumpawaroo':
#     if '|' in command:
#         command = command.split(' | ')
#         forcesite = command[0]
#         name = command[1]
#         if forcesite not in forcedict:
#             forcedict[forcesite] = [name]
#             command = input()
#         else:
#             forcedict[forcesite] = [name]
#             command = input()
#     else:
#         command = command.split(' -> ')
#         name = command[0]
#         new_site = command[1]
#         flat_value_list = [item for sublist in forcedict.values() for item in sublist]
#
#         if name not in flat_value_list and new_site not in forcedict:
#             forcedict[new_site] = [name]
#             print(f"{name} joins the {new_site} side!")
#             command = input()
#         elif name not in flat_value_list and new_site in forcedict:
#             forcedict[new_site] += [name]
#             print(f"{name} joins the {new_site} side!")
#             command = input()
#         else:
#             for key in forcedict:
#                 if name in forcedict[key]:
#                     forcedict[key].remove(name)
#             forcedict[new_site] += [name]
#             print(f"{name} joins the {new_site} side!")
#             command = input()
#
# forcedict = dict(value_key_sorted_dict(forcedict))
#
#
# for site in forcedict:
#     if len(forcedict[site]) != 0:
#         ll = sorted(forcedict[site])
#         print(f'Side: {site}, Members: {len(forcedict[site])}')
#         for name in ll:
#             print(f'! {name}')

line = input()
sides = {}

while line != "Lumpawaroo":
    if " | " in line:
        args = line.split(" | ")
        side = args[0]
        user = args[1]
        # TODO If you receive forceSide | forceUser, you should check if such forceUser already exists, and if not, add him/her to the corresponding side
        if side not in sides:
            sides[side] = []

        all_values = []

        for current_list in sides.values():
            all_values += current_list

        if user not in all_values:
            sides[side].append(user)

    else:
        args = line.split(" -> ")
        user = args[0]
        side = args[1]
        old_side = ""

        for key, value in sides.items():
            if user in value:
                old_side = key
                break

        if old_side != "":
            sides[old_side].remove(user)

            if side not in sides:
                sides[side] = []

            sides[side].append(user)
        else:
            if side not in sides:
                sides[side] = []

            sides[side].append(user)

        print(f"{user} joins the {side} side!")

    line = input()

sides = dict(sorted(sides.items(), key=lambda x: (-len(x[1]), x[0])))

for side, users in sides.items():
    if len(users) == 0:
        continue

    print(f"Side: {side}, Members: {len(users)}")

    for user in sorted(users):
        print(f"! {user}")