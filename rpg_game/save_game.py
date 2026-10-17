import json
from items import Item, Weapon, Armor
from inventory import Inventory

def is_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool)

def get_type(data):
    if 'kind' in data:
        return 'kind'
    if 'damage' in data:
        return 'weapon'
    if 'defense' in data:
        return 'armor'
    return 'item'

def check_field(data, field):
    if field not in data:
        return False, f'нет поля {field}'
    value = data['field']
    if not is_number(value):
        return False, f'поле должно быть числом {value}'
    if value < 0:
        return False, f'{value} должно быть неотрицательным'
    return True, None



def validate_item(data):
    if not isinstance(data, dict):
        return False, f'{data} должно быть словарем'

    kind = get_type(data)

    if 'name' not in data:
        return False, f'не поля name'

    if not isinstance(data['name'], str):
        return False, 'name должно быть строкой'

    if 'price' not in data:
        return False, 'нет price'

    if not isinstance(data['price'], (int, float)):
        return False, 'price должго быть числом'

    if data['price'] < 0:
        return False, 'price не может быть меньше нуля'

    if kind == 'weapon':
        ok, err = check_field(data, 'damage')
        if not ok:
            return False, err
    if kind == 'armor':
        ok, err = check_field(data, 'defense')
        if not ok:
            return False, err
    return True, None

def save_inventory(inventory, filename='save.json'):
    data = [item.to_dict() for item in inventory.inventory]

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_inventory(filename='save.json'):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print('сохранение не найдено, создан новый файл')
        return Inventory()

    except json.JSONDecodeError:
        print('Файл сохранения поврежден!')
        return Inventory()
    
    inventory = Inventory()

    if not isinstance(data, list):
        print('Ошибка: сохранение должно содержать список!')
        return Inventory()

    for item_data in data:
        if not validate_item(item_data):
            print('Пропущен предмет с некоторыми данными!')
            continue
        if item_data['kind'] == 'weapon':
            item = Weapon(
                item_data['kind'],
                item_data['name'],
                item_data['price'],
                item_data['damage']
            )
        elif item_data['kind'] == 'armor':
            item = Armor(
                item_data['kind'],
                item_data['name'],
                item_data['price'],
                item_data['defense']
            )
        else:
            item = Item(
                item_data['kind'],
                item_data['name'],
                item_data['price']
            )
        inventory + item
    return inventory



if __name__ == '__main__':
    inventory = Inventory()
    inventory + Item('item', 'Зелье', 15)
    inventory + Weapon('weapon', 'Меч', 500, 40)
    inventory + Armor('armor', 'Шлем', 300, 15)

    save_inventory(inventory)
    print('Инвентарь сохранён!')

    loaded_inventory = load_inventory()
    print('Загруженный инвентарь:')
    loaded_inventory.show_items()
    print('Всего предметов:', len(loaded_inventory))