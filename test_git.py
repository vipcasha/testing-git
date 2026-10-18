print('helloworld!')
for i in range(10):
    print(i)
class Item:
    def __init__(self, name):
        self.name = name
i1 = Item('alex')

d1 = {'alex': 17}
class Hero(Item):
    def __init__(self, name, hp, mana):
        super().__init__(name)
        self.hp = hp
        self.mana = mana
    def __str__(self):
        return f'Name: {self.name}; hp: {self.hp}; mana: {self.mana}'

player1 = Hero('dark seer', 300, 150)
print(player1)