class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError('Цена не может быть отрицательной!')
        self._price = value

    @property
    def discounted_price(self):
            return self._price * 0.8

product = Product('Наушники', 5000)

print(product.price)             # 5000
print(product.discounted_price)  # 4000

product.price = 6000
print(product.discounted_price)  # 4800

product.price = -100  # Должен возникнуть ValueError

