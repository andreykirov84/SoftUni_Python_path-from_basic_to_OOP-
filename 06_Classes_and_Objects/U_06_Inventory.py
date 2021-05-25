class Inventory:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.items = []

    def add_item(self, item):
        if len(self.items) < self.__capacity:
            self.items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        result = "Items: "
        result += self.items[0]
        for i in range(1, len(self.items)):
            result += f', {self.items[i]}'
        result += f'.\nCapacity left: {len(self.items) - self.__capacity}'
        return result


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
