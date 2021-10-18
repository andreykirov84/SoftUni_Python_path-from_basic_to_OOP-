def stock_availability(inventory, command, *args):
    if command == 'delivery':
        for item in args:
            inventory.append(item)
        return inventory
    elif command == 'sell':
        if not args:
            inventory.pop(0)
            return inventory
        else:
            if str(args[0]).isnumeric():
                if args[0] < len(inventory) + 1:
                    for _ in range(args[0]):
                        inventory.pop(0)
            else:
                for item in args:
                    if item in inventory:
                        try:
                            while True:
                                inventory.remove(item)
                        except:
                            pass
            return inventory



# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# expectedresult = ['choco', 'vanilla', 'banana', 'caramel', 'berry']

# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# expectedresult = ['vanilla', 'banana']
#
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))

print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))

print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))