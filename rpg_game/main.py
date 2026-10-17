from items import Item, Weapon, Armor
from inventory import Inventory

inventory = Inventory()

inventory + Item('Зелье', 100)
inventory + Weapon('Меч', 500, 40)
inventory + Armor('Шлем', 300, 15)

print(inventory)
print(f'Общая стоимость: {inventory.total_value()} руб.')
print(f'Количество предметов: {len(inventory)}')

