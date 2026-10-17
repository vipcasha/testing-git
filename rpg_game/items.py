class Item:
    def __init__(self, kind, name, price):
        self.kind = kind
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Цена не может быть отрицательной')
        self._price = value

    def to_dict(self):
        return {'kind': self.kind, 'name': self.name, 'price': self.price}
    
    def __str__(self):
        return f'{self.name} - {self._price} rub.'
    
    def __lt__(self, other):
        return self._price < other._price
    
    def __repr__(self):
        return f"Item('{self.kind} {self.name}', {self._price})"

class Armor(Item):
    def __init__(self, kind, name, price, defense):
        super().__init__(kind, name, price)
        self.defense = defense

    def __str__(self):
        return f'{self.name} - {self.price} rub. | Защита: {self.defense}'
    
    def to_dict(self):
        data = super().to_dict()
        data['defense'] = self.defense
        return data


class Weapon(Item):
    def __init__(self, kind, name, price, damage):
        super().__init__(kind, name, price)
        self.damage = damage

    def __str__(self):
        return f'{self.name} - {self.price} rub. | Урон: {self.damage}'
    
    def to_dict(self):
        data = super().to_dict()
        data['damage'] = self.damage
        return data


if __name__ == "__main__":
    potion = Item('item', 'Зелье', 100)
    sword = Weapon('weapon', 'Меч', 500, 40)
    helmet = Armor('armor' ,'Шлем', 300, 15)

    assert potion.to_dict() == {
        'kind': 'item',
        'name': 'Зелье',
        'price': 100
    }

    assert sword.to_dict() == {
        'kind': 'weapon',
        'name': 'Меч',
        'price': 500,
        'damage': 40
    }

    assert helmet.to_dict() == {
        'kind': 'armor',
        'name': 'Шлем',
        'price': 300,
        'defense': 15
    }

    print('Все тесты пройдены!')