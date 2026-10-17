from items import Item

class Inventory:
    def __init__(self):
        self.inventory = []
    def add_item(self, item):
        self.inventory.append(item)
    def remove_item(self, item):
        self.inventory.remove(item)
    def show_items(self):
        for i in self.inventory:
            print(i)
    def total_value(self):
        total = 0
        for i in self.inventory:
            total += i.price
        return total
    def sort_by_price(self):
        return self.inventory.sort(key=lambda item: item.price)
    def __len__(self):
        return len(self.inventory)
    def __str__(self):
        return ', '.join(str(item) for item in self.inventory)
    def __add__(self, other):
        if isinstance(other, Item):
            self.add_item(other)
            return self
        elif isinstance(other, Inventory):
            new_inventory = Inventory()
            new_inventory.inventory = self.inventory.copy() + other.inventory.copy()
            return new_inventory
        else:
            raise TypeError('Можно добавить только предмет или инвентарь')